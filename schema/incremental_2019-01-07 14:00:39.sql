BEGIN;

-- Running upgrade ac5b9a2035df -> caa44c8e5fbe

ALTER TABLE "user" ADD COLUMN first_name VARCHAR(32);

ALTER TABLE "user" ADD COLUMN last_name VARCHAR(32);

CREATE INDEX ix_user_first_name ON "user" (first_name);

CREATE INDEX ix_user_last_name ON "user" (last_name);

UPDATE alembic_version SET version_num='caa44c8e5fbe' WHERE alembic_version.version_num = 'ac5b9a2035df';

COMMIT;

UPDATE version_information set major_ver='1.0.11',minor_ver='ac5b9a2035df:caa44c8e5fbe',build_date='2019-01-07 14:00:45' where program_name='class4v6';
