BEGIN;

-- Running upgrade a0ecabe25ded -> 27aa3eebd22c

ALTER TABLE email_template ALTER COLUMN content_html SET NOT NULL;

ALTER TABLE email_template ALTER COLUMN content_text DROP NOT NULL;

ALTER TABLE email_template ALTER COLUMN hint DROP NOT NULL;

UPDATE alembic_version SET version_num='27aa3eebd22c' WHERE alembic_version.version_num = 'a0ecabe25ded';

COMMIT;

UPDATE version_information set major_ver='1.0.7',minor_ver='a0ecabe25ded:27aa3eebd22c',build_date='2018-11-23 21:16:05' where program_name='class4v6';
