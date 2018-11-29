BEGIN;

-- Running upgrade cfa25697d301 -> 6fa1546cba13

ALTER TABLE payment ADD COLUMN amount_lrn NUMERIC DEFAULT '0' NOT NULL;

ALTER TABLE payment ADD COLUMN amount_switch NUMERIC DEFAULT '0' NOT NULL;

ALTER TABLE payment ADD COLUMN amount_total NUMERIC DEFAULT '0' NOT NULL;

ALTER TABLE payment DROP COLUMN amount;

UPDATE alembic_version SET version_num='6fa1546cba13' WHERE alembic_version.version_num = 'cfa25697d301';

COMMIT;

UPDATE version_information set major_ver='1.0.9',minor_ver='cfa25697d301:6fa1546cba13',build_date='2018-11-29 20:47:17' where program_name='class4v6';
