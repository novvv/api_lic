BEGIN;

-- Running upgrade 27aa3eebd22c -> cfa25697d301

ALTER TABLE "user" ADD COLUMN alert_license_expired BOOLEAN DEFAULT 'true';

ALTER TABLE "user" ADD COLUMN alert_license_purchased BOOLEAN DEFAULT 'true';

ALTER TABLE "user" ADD COLUMN alert_license_will_expired BOOLEAN DEFAULT 'true';

ALTER TABLE "user" ADD COLUMN alert_payment_received BOOLEAN DEFAULT 'true';

UPDATE alembic_version SET version_num='cfa25697d301' WHERE alembic_version.version_num = '27aa3eebd22c';

COMMIT;

UPDATE version_information set major_ver='1.0.9',minor_ver='27aa3eebd22c:cfa25697d301',build_date='2018-11-28 00:45:35' where program_name='class4v6';
