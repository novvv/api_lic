##webbackend makefile
SHELL := /bin/bash
LOCAL_PYTHON = source venv/bin/activate && python3
LOCAL_ALEMBIC = source venv/bin/activate && PYTHONPATH=./ alembic -c api_lic/alembic.ini
HEAD := $(shell PYTHONPATH=./ alembic -c api_lic/alembic.ini history | head -n 1 | sed "s/ -> /:/g" | sed "s/ .*//g" )
BUILD := $(shell date "+%F\ %T")
REVISION?=head
VERSION := $(shell grep '__version__ =' api_lic/__version__.py | sed "s/__version__ = '//" | sed "s/'//g")
SERVER := $(shell head -n 1 .server)
#SERVER_PRE := $(shell head -n 1 .server_pre)
PYTHONPATH=../make
API_HOME = /opt/denovo/api_lic


all: build-py deploy upgrade

build-py:
	echo "Build $(VERSION)"
	sed -i s/__minor__\ =\ \'.*\'/__minor__\ =\ \'`cat .git/refs/heads/master`\'/ api_lic/__version__.py
	sed -i s/__date__\ =\ \'.*\'/__date__\ =\ \'$(BUILD)\'/ api_lic/__version__.py
	bin/api_gen.sh
	$(LOCAL_PYTHON) setup.py build
	$(LOCAL_PYTHON) setup.py sdist
	cp dist/api_lic-$(VERSION).tar.gz dist/api_lic-head.tar.gz
	#git add -f dist/api_lic-head.tar.gz
	#git commit -m "$(VERSION)"
	#git push


deploy:
	echo "Deploying $(VERSION)"
	scp dist/api_lic-head.tar.gz $(SERVER):~/builds/
	##scp api.ini $(SERVER):~/api_lic/api_new.ini
	#ssh $(SERVER) "cd ~/builds && git archive --remote=ssh://git@stash.denovolab.com:7999/lic/api_engine.git HEAD:dist api_lic-head.tar.gz | tar -x"
	ssh $(SERVER) "sudo /usr/local/bin/pip3.5 install --upgrade ~/builds/api_lic-head.tar.gz"
	#scp dist/api_lic-$(VERSION).tar.gz $(SERVER_PRE):~/dist/
	#scp env_staging $(SERVER_PRE):/usr/local/env_staging_dnl
	#ssh $(SERVER_PRE) "sudo /home/novv/deploy api_lic-$(VERSION).tar.gz"
	#ssh $(SERVER_PRE) "sudo /home/novv/deploy api_lic-$(VERSION).tar.gz"
	

upgrade:
	echo "Upgrading to $(REVISION)"
	#scp api_lic/alembic.ini $(SERVER):$(API_HOME)/alembic.ini
	ssh $(SERVER) "cd $(API_HOME) && /usr/local/bin/alembic -c alembic.ini upgrade $(REVISION)"


swagger:
	$(LOCAL_PYTHON) -m api_lic.swagger > swagger.json
	$(LOCAL_PYTHON) -m api_lic.swagger yaml > swagger.yaml

test:
	source env_dev && FAKE_DB_TEXT_FUNCTION=1 py.test -x api_lic/tests

test-pg:
	source env_dev && DB_CONN_STRING_TEST=postgresql://dnl_api:ferthuk@localhost:5432/dnl_api py.test -xs api_lic/tests

run:
	venv/bin/gunicorn api_lic.wsgi:app -b 127.0.0.1:8008 --reload

migrations-generate:
	PYTHONPATH=./ alembic -c api_lic/alembic.ini revision --autogenerate -m "$(LABEL)"
	
migrations-upgrade:
	echo "PYTHONPATH="$(PYTHONPATH)
	echo "HEAD="$(HEAD)
	echo "BUILD="$(BUILD)
#HELL:
	PYTHONPATH=./ alembic -c api_lic/alembic.ini upgrade $(REVISION)
	PYTHONPATH=./ alembic -c api_lic/alembic.ini history > schema/history.txt
	PYTHONPATH=./ alembic -c api_lic/alembic.ini upgrade $(HEAD) --sql > schema/incremental_$(BUILD).sql
	#PYTHONPATH=./ alembic -c api_lic/alembic.ini upgrade head --sql > schema/incremental_$(BUILD).sql
	echo "UPDATE version_information set major_ver='$(VERSION)',minor_ver='$(HEAD)',build_date='`date +%F\ %T`' where program_name='class4v6';" >>  schema/incremental_$(BUILD).sql
	pg_dump -s -O -d lic > schema/schema_$(BUILD).sql
	cp schema/schema_$(BUILD).sql schema/schema.sql
	cat schema/templates/users.sql >> schema/data.sql
	#pg_dump -d lic -a -t mail_sender >> schema/data.sql
	cp schema/data.sql schema/data_$(BUILD).sql
	
update-record:
	cat schema/class4_update_record.sql | psql -q -d lic
	cat schema/class4_update_record.sql | ssh $(SERVER) psql -q -d lic -U postgres
	cat schema/class4_update_record.sql | ssh $(SERVER_PRE) psql -q -d lic -U postgres
initadmin:
	#PYTHONPATH=./ python api_lic/initadmin.py
	ssh $(SERVER) "python3 /usr/local/lib/python3.5/site-packages/api_lic/initadmin.py"
