#Standalone installation
##Web server Requirements
1. `yum install nginx`
2. `service nginx start`


## Database Requirements
1. Postgresql 9.0 and above
2. `git clone https://github.com/RhodiumToad/ip4r.git`
3. `cd ip4r`
4. `make install`
5. `psql -c 'create extension ip4r;'`
6. `git clone https://github.com/dimitri/prefix.git`
7. `cd prefix`
8. `make install`
9. `psql -c 'create extension prefix;'`
10. `psql -c 'create extension btree_gist;'`
11. `createuser -c -s webbackend`
 
## Python Requirements
1. Python >= 3.5 (in /usr/local/bin)
2. PIP => 9.0.1
3. install falcon_rest from git:
 
`git clone ssh://ssh://git@stash.denovolab.com:7999/af/falcon_rest.git` 
 
`/usr/local/bin/python3.5 setup.py install`
3. see requirements.txt

##installation steps
1. cd to any temporary writable dir and get tarball from git:
1. `git archive --remote=ssh://git@stash.denovolab.com:7999/clas6/webbackend.git HEAD:dist api-dnl-head.tar.gz | tar -x` 
2. `pip install --upgrade api-dnl-head.tar.gz`
3. all needed data files wil be installed to /opt/denovolab_v6/api_dnl
4. `cd /opt/denovolab_v6/api_dnl`
5. `cat schema/schema.sql | psql -U webbackend -d class4_dnl`
6. `cat schema/class4_update_record.sql | psql -U webbackend -d class4_dnl`
7. `cat schema/data.sql | psql -U webbackend -d class4_dnl`
8. change api.ini api_host must be external ip address or dns name of api
9. api_schema depend of nginx "http" ot "https" configuration
10. installation will create following entry points for api_dnl:
 
    `/usr/local/bin/api_dnl_run`  <-- run gunicorn web service
    `/usr/local/bin/api_dnl_pcaploader` <-- exec pcap loader 
    `/usr/local/bin/api_dnl_pjsipcall` <-- exec test call service
    `/usr/local/bin/api_dnl_ws_broker` <-- exec web socket callback service
    `/usr/local/bin/api_dnl_worker` <-- exec celery run task service
    `/usr/local/bin/api_dnl_beat` <-- exec celery schedule task service
 
##standalone upgrade version
1. `git archive --remote=ssh://stash.denovolab.com:7999/cls/license-portal-api.git HEAD:dist api_lic-head.tar.gz | tar -x` 
2. `pip install --upgrade builds/api_lic-head.tar.gz`
3. `cd /opt/denovolab/api_lic`
4. `sudo /usr/local/bin/alembic upgrade head`
 
## Run
`cd /opt/denovo`

`/usr/local/bin/api_lic_run`

# Development Installation
##install
1. `git clone http://stash.denovolab.com/scm/clas6/webbackend.git`
2. `cd webbackend`
3. `virtualenv --prompt '[webbackend] ' -p /path/to/python3.x`
4. `source venv/bin/activate`
4. install falcon_rest as for above
5. `pip install -r requirements.txt`
## Prepare to run
`pip install gunicorn`
## Run
* Run LIC API `make run-staging-dnl`

## Deployng release to server
1. `echo "user@1.2.3.4" > .server`
2. `user must have ssh on this server
3. `make build-ver`
4. `make deploy`
# Run tests
python3.5 -m unittest discover api_smsc.test