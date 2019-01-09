BEGIN;

-- Running upgrade caa44c8e5fbe -> 17220f13141b

ALTER TABLE package_lrn ADD COLUMN create_on TIMESTAMP WITH TIME ZONE DEFAULT now();

ALTER TABLE package_switch ADD COLUMN create_on TIMESTAMP WITH TIME ZONE DEFAULT now();

UPDATE alembic_version SET version_num='17220f13141b' WHERE alembic_version.version_num = 'caa44c8e5fbe';

COMMIT;

UPDATE version_information set major_ver='1.0.14',minor_ver='caa44c8e5fbe:17220f13141b',build_date='2019-01-09 13:03:23' where program_name='class4v6';
