BEGIN;

-- Running upgrade cb4c870de32e -> d7b99512de3c

ALTER TABLE license ADD COLUMN user_uuid VARCHAR(36);

CREATE INDEX ix_license_user_uuid ON license (user_uuid);

ALTER TABLE license ADD FOREIGN KEY(user_uuid) REFERENCES "user" (user_uuid) ON DELETE CASCADE;

ALTER TABLE license_lrn ADD COLUMN type INTEGER;

DROP INDEX ix_license_period_user_uuid;

ALTER TABLE license_period DROP CONSTRAINT license_period_user_uuid_fkey;

ALTER TABLE license_period DROP COLUMN user_uuid;

ALTER TABLE license_switch ADD COLUMN type INTEGER;

UPDATE alembic_version SET version_num='d7b99512de3c' WHERE alembic_version.version_num = 'cb4c870de32e';

COMMIT;

UPDATE version_information set major_ver='1.0.28',minor_ver='cb4c870de32e:d7b99512de3c',build_date='2018-10-08 14:37:11' where program_name='class4v6';
