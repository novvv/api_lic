BEGIN;

-- Running upgrade b07f61c2b5e5 -> 229b9974924f

ALTER TABLE transaction_log ADD COLUMN user_uuid VARCHAR(36);

CREATE INDEX ix_transaction_log_user_uuid ON transaction_log (user_uuid);

ALTER TABLE transaction_log ADD FOREIGN KEY(user_uuid) REFERENCES "user" (user_uuid) ON DELETE CASCADE;

UPDATE alembic_version SET version_num='229b9974924f' WHERE alembic_version.version_num = 'b07f61c2b5e5';

COMMIT;

UPDATE version_information set major_ver='1.0.18',minor_ver='b07f61c2b5e5:229b9974924f',build_date='2019-04-12 15:16:52' where program_name='class4v6';
