BEGIN;

-- Running upgrade d40606f1a9c0 -> d74fb65a2c6c

ALTER TABLE package_switch ADD COLUMN expire_date TIMESTAMP WITH TIME ZONE;

ALTER TABLE package_switch ADD COLUMN start_date TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL;

UPDATE alembic_version SET version_num='d74fb65a2c6c' WHERE alembic_version.version_num = 'd40606f1a9c0';

COMMIT;

UPDATE version_information set major_ver='1.0.5',minor_ver='d40606f1a9c0:d74fb65a2c6c',build_date='2018-11-14 16:39:38' where program_name='class4v6';
