BEGIN;

-- Running upgrade 5a18f169eb3c -> 82e5ccccac94

ALTER TABLE config_payment ADD COLUMN paypal_email VARCHAR(64);

ALTER TABLE config_payment ADD COLUMN paypal_pkey VARCHAR(64);

ALTER TABLE config_payment ADD COLUMN paypal_skey VARCHAR(64);

ALTER TABLE config_payment ADD COLUMN paypal_svc_charge NUMERIC;

ALTER TABLE config_payment ADD COLUMN paypal_test_mode BOOLEAN;

UPDATE alembic_version SET version_num='82e5ccccac94' WHERE alembic_version.version_num = '5a18f169eb3c';

COMMIT;

UPDATE version_information set major_ver='1.0.11',minor_ver='5a18f169eb3c:82e5ccccac94',build_date='2018-12-20 18:03:17' where program_name='class4v6';
