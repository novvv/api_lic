BEGIN;

-- Running upgrade 17220f13141b -> ca11a5c702c2

CREATE TABLE transaction_log (
    transaction_log_uuid VARCHAR(36) DEFAULT uuid_generate_v4() NOT NULL, 
    transaction_time TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
    license_lrn_uuid VARCHAR(36), 
    license_switch_uuid VARCHAR(36), 
    type INTEGER, 
    amount_lrn NUMERIC DEFAULT '0' NOT NULL, 
    amount_switch NUMERIC DEFAULT '0' NOT NULL, 
    transaction_id VARCHAR(255), 
    transaction_type VARCHAR(255), 
    from_ip VARCHAR(36), 
    transaction_src JSON, 
    status INTEGER, 
    result TEXT, 
    payment_uuid VARCHAR(36), 
    PRIMARY KEY (transaction_log_uuid), 
    FOREIGN KEY(payment_uuid) REFERENCES payment (payment_uuid) ON DELETE CASCADE
);

CREATE INDEX ix_transaction_log_payment_uuid ON transaction_log (payment_uuid);

UPDATE alembic_version SET version_num='ca11a5c702c2' WHERE alembic_version.version_num = '17220f13141b';

COMMIT;

UPDATE version_information set major_ver='1.0.14',minor_ver='17220f13141b:ca11a5c702c2',build_date='2019-01-22 13:55:34' where program_name='class4v6';
