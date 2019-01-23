BEGIN;

-- Running upgrade f11572091a96 -> 95d13495228a

ALTER TABLE transaction_log ADD COLUMN amount_total NUMERIC DEFAULT '0' NOT NULL;

UPDATE alembic_version SET version_num='95d13495228a' WHERE alembic_version.version_num = 'f11572091a96';

COMMIT;

UPDATE version_information set major_ver='1.0.14',minor_ver='f11572091a96:95d13495228a',build_date='2019-01-22 18:14:23' where program_name='class4v6';
