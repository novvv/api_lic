BEGIN;

-- Running upgrade 5824b1c6a0c6 -> b07f61c2b5e5

ALTER TABLE license_lrn DROP CONSTRAINT uq_license_lrn_package_lrn_uuid_user_uuid;

ALTER TABLE license_switch DROP CONSTRAINT uq_license_switch_package_switch_uuid_user_uuid;

UPDATE alembic_version SET version_num='b07f61c2b5e5' WHERE alembic_version.version_num = '5824b1c6a0c6';

COMMIT;

UPDATE version_information set major_ver='1.0.14',minor_ver='5824b1c6a0c6:b07f61c2b5e5',build_date='2019-04-11 13:55:20' where program_name='class4v6';
