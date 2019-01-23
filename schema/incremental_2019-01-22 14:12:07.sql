BEGIN;

-- Running upgrade ca11a5c702c2 -> f11572091a96

ALTER TABLE transaction_log ADD COLUMN transaction_fee NUMERIC DEFAULT '0' NOT NULL;

UPDATE alembic_version SET version_num='f11572091a96' WHERE alembic_version.version_num = 'ca11a5c702c2';

COMMIT;

UPDATE version_information set major_ver='1.0.14',minor_ver='ca11a5c702c2:f11572091a96',build_date='2019-01-22 14:12:12' where program_name='class4v6';
