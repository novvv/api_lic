BEGIN;

-- Running upgrade e258be71ed9f -> 8abd30c15b00

CREATE TABLE dnl_license_info (
    id SERIAL NOT NULL, 
    carrier_name VARCHAR(100), 
    ss_type SMALLINT DEFAULT 0 NOT NULL, 
    status SMALLINT DEFAULT 1 NOT NULL, 
    ss_name VARCHAR(100) NOT NULL, 
    uuid VARCHAR(128) NOT NULL, 
    recv_ip VARCHAR(16) NOT NULL, 
    recv_port INTEGER, 
    ss_bind_mac VARCHAR(18) NOT NULL, 
    ss_bind_ip VARCHAR(16) NOT NULL, 
    ss_bind_port INTEGER, 
    max_cap INTEGER DEFAULT 500 NOT NULL, 
    max_cps INTEGER DEFAULT 100 NOT NULL, 
    start_time TIMESTAMP WITH TIME ZONE DEFAULT ('now'::text)::date, 
    end_time TIMESTAMP WITH TIME ZONE DEFAULT (('now'::text)::date + '3650 days'::interval), 
    expires INTEGER DEFAULT 3650, 
    update_time TIMESTAMP WITH TIME ZONE, 
    create_time TIMESTAMP WITH TIME ZONE DEFAULT now(), 
    create_user SMALLINT DEFAULT 0 NOT NULL, 
    PRIMARY KEY (id)
);

CREATE INDEX ix_dnl_license_info_carrier_name ON dnl_license_info (carrier_name);

CREATE INDEX ix_dnl_license_info_ss_bind_mac ON dnl_license_info (ss_bind_mac);

CREATE INDEX ix_dnl_license_info_ss_name ON dnl_license_info (ss_name);

CREATE INDEX ix_dnl_license_info_ss_type ON dnl_license_info (ss_type);

CREATE INDEX ix_dnl_license_info_uuid ON dnl_license_info (uuid);

CREATE TABLE dnl_license_info_record (
    record_id SERIAL NOT NULL, 
    id INTEGER, 
    carrier_name VARCHAR(100), 
    ss_type SMALLINT, 
    status SMALLINT, 
    ss_name VARCHAR(100), 
    uuid VARCHAR(128), 
    recv_ip VARCHAR(16), 
    recv_port INTEGER, 
    ss_bind_mac VARCHAR(18), 
    ss_bind_ip VARCHAR(16), 
    ss_bind_port INTEGER, 
    max_cap INTEGER, 
    max_cps INTEGER, 
    start_time TIMESTAMP WITH TIME ZONE, 
    end_time TIMESTAMP WITH TIME ZONE, 
    expires INTEGER, 
    update_time TIMESTAMP WITH TIME ZONE, 
    create_time TIMESTAMP WITH TIME ZONE, 
    create_user SMALLINT, 
    time NUMERIC, 
    flag CHAR(1), 
    PRIMARY KEY (record_id)
);

CREATE TABLE dnl_license_log (
    id SERIAL NOT NULL, 
    uuid VARCHAR(128) NOT NULL, 
    recv_ip VARCHAR(16) NOT NULL, 
    recv_port INTEGER, 
    cap INTEGER DEFAULT 0 NOT NULL, 
    cps INTEGER DEFAULT 0 NOT NULL, 
    start_time TIMESTAMP WITH TIME ZONE, 
    end_time TIMESTAMP WITH TIME ZONE, 
    sip_addr VARCHAR(256), 
    status SMALLINT DEFAULT 0 NOT NULL, 
    create_time TIMESTAMP WITH TIME ZONE DEFAULT now(), 
    PRIMARY KEY (id)
);

CREATE INDEX ix_dnl_license_log_recv_ip ON dnl_license_log (recv_ip);

CREATE INDEX ix_dnl_license_log_uuid ON dnl_license_log (uuid);

CREATE TABLE dnl_pre_licensing_info (
    id SERIAL NOT NULL, 
    ip VARCHAR(16) NOT NULL, 
    cap INTEGER DEFAULT 0 NOT NULL, 
    cps INTEGER DEFAULT 0 NOT NULL, 
    expires INTEGER, 
    create_time TIMESTAMP WITH TIME ZONE DEFAULT now(), 
    PRIMARY KEY (id)
);

CREATE TABLE dnl_pre_licensing_info_record (
    record_id SERIAL NOT NULL, 
    id INTEGER, 
    ip VARCHAR(16), 
    cap INTEGER, 
    cps INTEGER, 
    expires INTEGER, 
    create_time TIMESTAMP WITH TIME ZONE DEFAULT now(), 
    time NUMERIC, 
    flag CHAR(1), 
    PRIMARY KEY (record_id)
);

UPDATE alembic_version SET version_num='8abd30c15b00' WHERE alembic_version.version_num = 'e258be71ed9f';

COMMIT;

UPDATE version_information set major_ver='1.0.11',minor_ver='e258be71ed9f:8abd30c15b00',build_date='2018-12-17 12:52:47' where program_name='class4v6';
