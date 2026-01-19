# ProgettoPPM - Server Monitoring Dashboard

Questo progetto è stato sviluppato come elaborato d’esame per il corso di Progettazione e Produzione Multimediale.  
Si tratta di una semplice applicazione web realizzata con Django che permette di monitorare lo stato di alcuni server di una rete locale tramite ping e di verificare la raggiungibilità dei servizi associati controllando l’apertura delle relative porte TCP.

L’accesso alla dashboard è consentito solo agli utenti autenticati. La gestione dei server, dei servizi e delle impostazioni avviene tramite il pannello di amministrazione di Django, a cui può accedere solo l'utente admin. È possibile configurare l’intervallo di aggiornamento automatico della dashboard.

Nel repository sono inclusi il file `requirements.txt` con tutte le dipendenze necessarie e il database `db.sqlite3` già popolato con alcuni dati di esempio, in modo da poter avviare il progetto e visualizzarne subito il funzionamento senza dover inserire manualmente i dati.

Per eseguire il progetto è sufficiente aprire un terminale nella cartella principale (dove si trova il file `manage.py`), creare e attivare un ambiente virtuale (venv) Python, installare le dipendenze tramite `pip install -r requirements.txt` e avviare il server con il comando `python manage.py runserver`. Non è necessario eseguire migrazioni perché il database è già incluso.

Una volta avviato il server, la dashboard è accessibile all’indirizzo http://127.0.0.1:8000/ mentre il pannello di amministrazione è disponibile all’indirizzo http://127.0.0.1:8000/admin/.

Sono già presenti utenti di esempio per il test dell’applicazione. L’account amministratore ha username `admin` e password `admin`, mentre è disponibile anche un utente normale per la sola visualizzazione della dashboard con username `test_staff` e password `test`.

