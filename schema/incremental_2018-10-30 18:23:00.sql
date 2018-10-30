BEGIN;

-- Running upgrade 79580b1c9691 -> e19d1c7311c9

CREATE TABLE switch (
    switch_uuid VARCHAR(36) DEFAULT uuid_generate_v4() NOT NULL, 
    switch_ip VARCHAR(16), 
    enabled BOOLEAN, 
    current_port_count INTEGER, 
    minute_remaining INTEGER, 
    expired_on TIMESTAMP WITH TIME ZONE, 
    email VARCHAR(256), 
    PRIMARY KEY (switch_uuid)
);

ALTER TABLE package_switch ADD COLUMN switch_uuid VARCHAR(36);

CREATE INDEX ix_package_switch_switch_uuid ON package_switch (switch_uuid);

ALTER TABLE package_switch ADD FOREIGN KEY(switch_uuid) REFERENCES switch (switch_uuid) ON DELETE CASCADE;

ALTER TABLE package_switch DROP COLUMN switch_ip;

UPDATE alembic_version SET version_num='e19d1c7311c9' WHERE alembic_version.version_num = '79580b1c9691';

COMMIT;

UPDATE version_information set major_ver='1.0.3',minor_ver='79580b1c9691:e19d1c7311c9',build_date='2018-10-30 18:23:05' where program_name='class4v6';
