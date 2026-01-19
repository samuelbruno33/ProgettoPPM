import socket
import platform
import subprocess
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Server, Config

# Ping a host using the system command
def ping_host(ip):
    # Windows -n, linux -c
    if platform.system().lower() == "windows":
        cmd = ['ping', '-n', '1', ip]
    else:
        cmd = ['ping', '-c', '1', ip]
    
    try:
        # Run the command with no output
        out = subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if out == 0:
            return True
        else:
            return False
    except:
        return False


# Check the connection on a given port, if returns true then the service is open, otherwise is closed
def check_service(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    try:
        result = s.connect_ex((ip, int(port))) # TCP connectino
        s.close()
        if result == 0:
            return True
        else:
            return False
    except:
        return False


def logout_view(request):
    logout(request)
    return redirect('/admin/login/')


@login_required(login_url='/admin/login/')
def dashboard(request):
    refresh_rate = Config.objects.first()
    if refresh_rate:
        refresh_rate = refresh_rate.refresh_seconds
    else:
        refresh_rate = 60 # Default if no config found

    servers = Server.objects.all()
    
    dashboard_data = []
    
    count_online = 0
    count_total = 0
    
    for s in servers:
        count_total = count_total + 1
        
        # Check Ping
        is_up = ping_host(s.ip_address)
        if is_up:
            count_online = count_online + 1
            
        # Check Services
        services_data = []
        my_services = s.services.all() # Get services from the db
        
        for service in my_services:
            is_open = check_service(s.ip_address, service.port)
            services_data.append({
                'name': service.name,
                'port': service.port,
                'open': is_open
            })
            
        # Add to list
        dashboard_data.append({
            'name': s.name,
            'ip': s.ip_address,
            'owner': s.owner,
            'is_up': is_up,
            'services': services_data
        })

    context = {
        'servers': dashboard_data,
        'refresh_time': refresh_rate,
        'total': count_total,
        'online': count_online,
        'offline': count_total - count_online
    }
    
    return render(request, 'dashboard.html', context)