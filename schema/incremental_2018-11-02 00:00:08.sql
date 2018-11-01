BEGIN;

-- Running upgrade 3d35a639b36b -> cf0fe8ceaba4

ALTER TABLE license_lrn ADD COLUMN is_enabled BOOLEAN;

ALTER TABLE license_switch ADD COLUMN is_enabled BOOLEAN;

UPDATE alembic_version SET version_num='cf0fe8ceaba4' WHERE alembic_version.version_num = '3d35a639b36b';

COMMIT;

UPDATE version_information set major_ver='1.0.4',minor_ver='3d35a639b36b:cf0fe8ceaba4',build_date='2018-11-02 00:00:13' where program_name='class4v6';
