BEGIN;

-- Running upgrade d74fb65a2c6c -> a0ecabe25ded

CREATE TABLE config_payment (
    id SERIAL NOT NULL, 
    charge_type INTEGER, 
    stripe_email VARCHAR(64), 
    stripe_skey VARCHAR(64), 
    stripe_pkey VARCHAR(64), 
    stripe_svc_charge INTEGER, 
    stripe_test_mode BOOLEAN, 
    confirm_enabled BOOLEAN, 
    email_confirm_to VARCHAR(64), 
    notification_enabled BOOLEAN, 
    email_cc_to VARCHAR(64), 
    PRIMARY KEY (id)
);

UPDATE alembic_version SET version_num='a0ecabe25ded' WHERE alembic_version.version_num = 'd74fb65a2c6c';

COMMIT;

UPDATE version_information set major_ver='1.0.7',minor_ver='d74fb65a2c6c:a0ecabe25ded',build_date='2018-11-23 21:03:27' where program_name='class4v6';
