BEGIN;

-- Running upgrade 98ce186d11f2 -> e258be71ed9f

ALTER TABLE license_lrn ADD COLUMN duration INTEGER DEFAULT '1';

ALTER TABLE license_switch ADD COLUMN duration INTEGER DEFAULT '1';

UPDATE alembic_version SET version_num='e258be71ed9f' WHERE alembic_version.version_num = '98ce186d11f2';

COMMIT;

UPDATE version_information set major_ver='1.0.11',minor_ver='98ce186d11f2:e258be71ed9f',build_date='2018-12-07 02:30:03' where program_name='class4v6';
