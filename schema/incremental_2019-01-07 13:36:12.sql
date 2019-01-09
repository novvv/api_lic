BEGIN;

-- Running upgrade 82e5ccccac94 -> ac5b9a2035df

ALTER TABLE payment DROP COLUMN amount_total;

UPDATE alembic_version SET version_num='ac5b9a2035df' WHERE alembic_version.version_num = '82e5ccccac94';

COMMIT;

UPDATE version_information set major_ver='1.0.11',minor_ver='82e5ccccac94:ac5b9a2035df',build_date='2019-01-07 13:36:17' where program_name='class4v6';
