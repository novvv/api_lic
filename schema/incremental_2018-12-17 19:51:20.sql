BEGIN;

-- Running upgrade 8abd30c15b00 -> 79ff7aba0109

alter table package_switch alter column switch_uuid type varchar(128);

alter table payment alter column switch_uuid type varchar(128);

UPDATE alembic_version SET version_num='79ff7aba0109' WHERE alembic_version.version_num = '8abd30c15b00';

COMMIT;

UPDATE version_information set major_ver='1.0.11',minor_ver='8abd30c15b00:79ff7aba0109',build_date='2018-12-17 19:51:26' where program_name='class4v6';
