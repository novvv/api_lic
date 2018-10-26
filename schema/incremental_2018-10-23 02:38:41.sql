BEGIN;

-- Running upgrade 68a956c4de09 -> 56c8b65dd6a3

CREATE TABLE license_update_history (
    id SERIAL NOT NULL, 
    uuid VARCHAR(100), 
    license_channel INTEGER, 
    license_cps INTEGER, 
    license_day INTEGER, 
    client_name VARCHAR(100), 
    remarks VARCHAR(100), 
    action SMALLINT DEFAULT '0' NOT NULL, 
    status_1 SMALLINT DEFAULT '0' NOT NULL, 
    status_2 SMALLINT DEFAULT '0' NOT NULL, 
    progress VARCHAR(200), 
    operator VARCHAR(50), 
    create_on TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
    remain VARCHAR, 
    PRIMARY KEY (id)
);

CREATE INDEX ix_license_update_history_status_1 ON license_update_history (status_1);

CREATE INDEX ix_license_update_history_status_2 ON license_update_history (status_2);

CREATE INDEX ix_license_update_history_uuid ON license_update_history (uuid);

CREATE TABLE lrn_permission_update_history (
    id SERIAL NOT NULL, 
    switch_ip VARCHAR(16), 
    permit_cps INTEGER, 
    client_name VARCHAR(100), 
    remarks VARCHAR(200), 
    action SMALLINT DEFAULT '0' NOT NULL, 
    status_1 SMALLINT DEFAULT '0' NOT NULL, 
    progress VARCHAR(200) DEFAULT '0' NOT NULL, 
    operator VARCHAR(50), 
    create_on TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
    remain VARCHAR, 
    PRIMARY KEY (id)
);

CREATE INDEX ix_lrn_permission_update_history_progress ON lrn_permission_update_history (progress);

CREATE INDEX ix_lrn_permission_update_history_status_1 ON lrn_permission_update_history (status_1);

UPDATE alembic_version SET version_num='56c8b65dd6a3' WHERE alembic_version.version_num = '68a956c4de09';

COMMIT;

UPDATE version_information set major_ver='1.0.1',minor_ver='68a956c4de09:56c8b65dd6a3',build_date='2018-10-23 02:38:47' where program_name='class4v6';
