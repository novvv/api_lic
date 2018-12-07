BEGIN;

-- Running upgrade 6fa1546cba13 -> 98ce186d11f2

ALTER TABLE package_switch DROP CONSTRAINT package_switch_switch_uuid_fkey;

ALTER TABLE payment ADD COLUMN switch_uuid VARCHAR(64);

CREATE INDEX ix_payment_switch_uuid ON payment (switch_uuid);

UPDATE alembic_version SET version_num='98ce186d11f2' WHERE alembic_version.version_num = '6fa1546cba13';

COMMIT;

UPDATE version_information set major_ver='1.0.9',minor_ver='6fa1546cba13:98ce186d11f2',build_date='2018-12-07 01:54:31' where program_name='class4v6';
