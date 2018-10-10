BEGIN;

-- Running upgrade 2d3470cd5603 -> 68a956c4de09

ALTER TABLE license_period ADD COLUMN ordered_amount INTEGER;

UPDATE alembic_version SET version_num='68a956c4de09' WHERE alembic_version.version_num = '2d3470cd5603';

COMMIT;

UPDATE version_information set major_ver='1.0.1',minor_ver='2d3470cd5603:68a956c4de09',build_date='2018-10-09 22:36:05' where program_name='class4v6';
