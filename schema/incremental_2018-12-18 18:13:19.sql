BEGIN;

-- Running upgrade 79ff7aba0109 -> 5a18f169eb3c

CREATE TABLE switch_daily (
    id SERIAL NOT NULL, 
    client_id VARCHAR(36), 
    from_ip VARCHAR(30) NOT NULL, 
    from_port INTEGER, 
    max_cps INTEGER, 
    max_cap INTEGER, 
    call_duration INTEGER, 
    detail VARCHAR(1024), 
    sip_addr VARCHAR(250), 
    start_date TIMESTAMP WITH TIME ZONE, 
    report_date VARCHAR(16), 
    create_time TIMESTAMP WITH TIME ZONE DEFAULT now(), 
    PRIMARY KEY (id)
);

CREATE INDEX ix_switch_daily_client_id ON switch_daily (client_id);

CREATE INDEX ix_switch_daily_from_ip ON switch_daily (from_ip);

CREATE INDEX ix_switch_daily_report_date ON switch_daily (report_date);

UPDATE alembic_version SET version_num='5a18f169eb3c' WHERE alembic_version.version_num = '79ff7aba0109';

COMMIT;

UPDATE version_information set major_ver='1.0.11',minor_ver='79ff7aba0109:5a18f169eb3c',build_date='2018-12-18 18:13:25' where program_name='class4v6';
