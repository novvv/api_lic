BEGIN;

-- Running upgrade 802754132737 -> 4b09277baffb

CREATE TABLE plan (
    plan_uuid VARCHAR(36) DEFAULT uuid_generate_v4() NOT NULL, 
    type INTEGER, 
    amount NUMERIC DEFAULT '0' NOT NULL, 
    PRIMARY KEY (plan_uuid)
);

ALTER TABLE license ADD COLUMN plan_uuid VARCHAR(36);

CREATE INDEX ix_license_plan_uuid ON license (plan_uuid);

DROP INDEX ix_license_rate_uuid;

ALTER TABLE license DROP CONSTRAINT license_rate_uuid_fkey;

ALTER TABLE license ADD FOREIGN KEY(plan_uuid) REFERENCES plan (plan_uuid) ON DELETE CASCADE;

ALTER TABLE license DROP COLUMN rate_uuid;

DROP TABLE rate;

UPDATE alembic_version SET version_num='4b09277baffb' WHERE alembic_version.version_num = '802754132737';

COMMIT;

UPDATE version_information set major_ver='1.0.2',minor_ver='802754132737:4b09277baffb',build_date='2018-10-29 15:35:00' where program_name='class4v6';
