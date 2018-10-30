BEGIN;

-- Running upgrade e19d1c7311c9 -> 22238fc9f214

ALTER TABLE license_lrn ADD CONSTRAINT uq_license_lrn_package_lrn_uuid_user_uuid UNIQUE (package_lrn_uuid, user_uuid);

ALTER TABLE license_switch ADD CONSTRAINT uq_license_switch_package_switch_uuid_user_uuid UNIQUE (package_switch_uuid, user_uuid);

UPDATE alembic_version SET version_num='22238fc9f214' WHERE alembic_version.version_num = 'e19d1c7311c9';

COMMIT;

UPDATE version_information set major_ver='1.0.3',minor_ver='e19d1c7311c9:22238fc9f214',build_date='2018-10-30 20:04:11' where program_name='class4v6';
