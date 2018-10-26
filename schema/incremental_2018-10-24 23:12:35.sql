BEGIN;

-- Running upgrade 56c8b65dd6a3 -> 802754132737

ALTER TABLE payment ADD COLUMN description TEXT;

ALTER TABLE payment ADD COLUMN user_uuid VARCHAR(36);

CREATE INDEX ix_payment_user_uuid ON payment (user_uuid);

ALTER TABLE payment ADD FOREIGN KEY(user_uuid) REFERENCES "user" (user_uuid) ON DELETE CASCADE;

UPDATE alembic_version SET version_num='802754132737' WHERE alembic_version.version_num = '56c8b65dd6a3';

COMMIT;

UPDATE version_information set major_ver='1.0.1',minor_ver='56c8b65dd6a3:802754132737',build_date='2018-10-24 23:12:41' where program_name='class4v6';
