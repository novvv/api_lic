BEGIN;

-- Running upgrade cf0fe8ceaba4 -> d40606f1a9c0

ALTER TABLE package_switch ADD COLUMN sub_type INTEGER;

UPDATE alembic_version SET version_num='d40606f1a9c0' WHERE alembic_version.version_num = 'cf0fe8ceaba4';

COMMIT;

UPDATE version_information set major_ver='1.0.4',minor_ver='cf0fe8ceaba4:d40606f1a9c0',build_date='2018-11-05 16:25:51' where program_name='class4v6';
