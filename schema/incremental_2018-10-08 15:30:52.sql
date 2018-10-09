BEGIN;

-- Running upgrade d7b99512de3c -> 2d3470cd5603

ALTER TABLE email_log DROP COLUMN sender_id;

ALTER TABLE email_log ADD COLUMN sender_id VARCHAR(36);

UPDATE alembic_version SET version_num='2d3470cd5603' WHERE alembic_version.version_num = 'd7b99512de3c';

COMMIT;

UPDATE version_information set major_ver='1.0.28',minor_ver='d7b99512de3c:2d3470cd5603',build_date='2018-10-08 15:30:57' where program_name='class4v6';
