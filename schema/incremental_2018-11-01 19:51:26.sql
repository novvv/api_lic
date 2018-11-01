BEGIN;

-- Running upgrade 22238fc9f214 -> 3d35a639b36b

delete from license_lrn;

delete from license_switch;

ALTER TABLE license_lrn ADD COLUMN ip VARCHAR(16) NOT NULL;

CREATE INDEX ix_license_lrn_ip ON license_lrn (ip);

DROP INDEX ix_license_lrn_plan_uuid;

ALTER TABLE license_lrn DROP CONSTRAINT license_lrn_plan_uuid_fkey;

ALTER TABLE license_lrn DROP COLUMN plan_uuid;

ALTER TABLE license_switch ADD COLUMN ip VARCHAR(16) NOT NULL;

CREATE INDEX ix_license_switch_ip ON license_switch (ip);

DROP INDEX ix_license_switch_plan_uuid;

ALTER TABLE license_switch DROP CONSTRAINT license_switch_plan_uuid_fkey;

ALTER TABLE license_switch DROP COLUMN plan_uuid;

ALTER TABLE package_lrn DROP COLUMN lrn_ip;

UPDATE alembic_version SET version_num='3d35a639b36b' WHERE alembic_version.version_num = '22238fc9f214';

COMMIT;

UPDATE version_information set major_ver='1.0.3',minor_ver='22238fc9f214:3d35a639b36b',build_date='2018-11-01 19:51:32' where program_name='class4v6';
