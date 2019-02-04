BEGIN;

-- Running upgrade 95d13495228a -> 5824b1c6a0c6

ALTER TABLE license_switch ADD COLUMN switch_uuid VARCHAR(128);

CREATE INDEX ix_license_switch_switch_uuid ON license_switch (switch_uuid);

DROP INDEX ix_package_switch_switch_uuid;

ALTER TABLE package_switch DROP COLUMN switch_uuid;

UPDATE alembic_version SET version_num='5824b1c6a0c6' WHERE alembic_version.version_num = '95d13495228a';

COMMIT;

UPDATE version_information set major_ver='1.0.14',minor_ver='95d13495228a:5824b1c6a0c6',build_date='2019-02-04 16:20:51' where program_name='class4v6';
