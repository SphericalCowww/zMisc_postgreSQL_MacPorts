# zMisc_postgreSQL_MacPorts
Mostly a record for how to set it up:

### Run
    (window1)
    sudo su - postgres
    cd /opt/local/var/db/postgresql11/
    ./pg_start
    (window2)
    psql -U username -d dbname < aligulac.sql (from http://aligulac.com/about/db/)
    python3 readPostGreSQL.py
    (window1)
    ./pg_stop
    exit
### Setup
    sudo port install postgresql11 postgresql11-server
    sudo port select postgresql postgresql11
    sudo port load postgresql11-server
    
    sudo mkdir -p /opt/local/var/db/postgresql11/defaultdb
    sudo chown -R postgres:postgres /opt/local/var/db/postgresql11
    sudo su postgres -c '/opt/local/lib/postgresql11/bin/initdb -D /opt/local/var/db/postgresql11/defaultdb'

    sudo mkdir -p /opt/local/var/log/postgresql11
    sudo chown -R postgres:postgres /opt/local/var/log/postgresql11
    
    sudo dscl . -create /Users/postgres UserShell /bin/bash
    
    sudo vim /opt/local/var/db/postgresql11/defaultdb/pg_hba.conf
      # "local" is for Unix domain socket connections only
      local   all             all                                     trust
      # IPv4 local connections:
      host    all             all             127.0.0.1/32            trust
    
    sudo su - postgres
    sudo vim /opt/local/var/db/postgresql11/pg_start 
      #!/bin/sh 
      /opt/local/lib/postgresql11/bin/pg_ctl -D /opt/local/var/db/postgresql11/defaultdb -l /opt/local/var/log/postgresql11/postgres.log start &
    sudo vim /opt/local/var/db/postgresql11/pg_stop
      #!/bin/sh 
      /opt/local/lib/postgresql11/bin/pg_ctl -D /opt/local/var/db/postgresql11/defaultdb -l /opt/local/var/log/postgresql11/postgres.log

    cd /opt/local/var/db/postgresql11/
    ./pg_start
    /opt/local/lib/postgresql11/bin/createuser username
    /opt/local/lib/postgresql11/bin/psql
      ALTER USER username with SUPERUSER;
      CREATE DATABASE dbname;
      \q
    ./pg_stop
    exit

###References
    Mos
