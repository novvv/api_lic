BEGIN;

-- Running upgrade 4b09277baffb -> 79580b1c9691

CREATE TABLE package_lrn (
    package_lrn_uuid VARCHAR(36) DEFAULT uuid_generate_v4() NOT NULL, 
    package_name VARCHAR(64), 
    cps INTEGER, 
    type INTEGER, 
    lrn_ip VARCHAR(16) NOT NULL, 
    lrn_port INTEGER, 
    dip_count INTEGER, 
    amount INTEGER, 
    enabled BOOLEAN, 
    PRIMARY KEY (package_lrn_uuid), 
    UNIQUE (package_name)
);

CREATE TABLE package_switch (
    package_switch_uuid VARCHAR(36) DEFAULT uuid_generate_v4() NOT NULL, 
    package_name VARCHAR(64), 
    type INTEGER, 
    switch_ip VARCHAR(16) NOT NULL, 
    switch_port INTEGER, 
    minute_count INTEGER, 
    amount INTEGER, 
    enabled BOOLEAN, 
    PRIMARY KEY (package_switch_uuid), 
    UNIQUE (package_name)
);

DROP INDEX ix_license_lrn_license_uuid;

ALTER TABLE license_lrn DROP CONSTRAINT license_lrn_license_uuid_fkey;

ALTER TABLE license_lrn DROP COLUMN license_uuid;

ALTER TABLE license_lrn ADD COLUMN cost NUMERIC DEFAULT '0' NOT NULL;

ALTER TABLE license_lrn ADD COLUMN end_time TIMESTAMP WITH TIME ZONE;

ALTER TABLE license_lrn ADD COLUMN license_lrn_uuid VARCHAR(36) DEFAULT uuid_generate_v4() NOT NULL;

ALTER TABLE license_lrn ADD CONSTRAINT license_lrn_pk PRIMARY KEY (license_lrn_uuid);

ALTER TABLE license_lrn ADD COLUMN ordered_amount INTEGER;

ALTER TABLE license_lrn ADD COLUMN package_lrn_uuid VARCHAR(36);

ALTER TABLE license_lrn ADD COLUMN plan_uuid VARCHAR(36);

ALTER TABLE license_lrn ADD COLUMN start_time TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL;

ALTER TABLE license_lrn ADD COLUMN user_uuid VARCHAR(36);

CREATE INDEX ix_license_lrn_package_lrn_uuid ON license_lrn (package_lrn_uuid);

CREATE INDEX ix_license_lrn_plan_uuid ON license_lrn (plan_uuid);

CREATE INDEX ix_license_lrn_user_uuid ON license_lrn (user_uuid);

ALTER TABLE license_lrn ADD FOREIGN KEY(package_lrn_uuid) REFERENCES package_lrn (package_lrn_uuid) ON DELETE CASCADE;

ALTER TABLE license_lrn ADD FOREIGN KEY(user_uuid) REFERENCES "user" (user_uuid) ON DELETE CASCADE;

ALTER TABLE license_lrn ADD FOREIGN KEY(plan_uuid) REFERENCES plan (plan_uuid) ON DELETE CASCADE;

ALTER TABLE license_lrn DROP COLUMN cps;

ALTER TABLE license_lrn DROP COLUMN type;

DROP INDEX ix_license_switch_license_uuid;

ALTER TABLE license_switch DROP CONSTRAINT license_switch_license_uuid_fkey;

ALTER TABLE license_switch DROP COLUMN license_uuid;

ALTER TABLE license_switch ADD COLUMN cost NUMERIC DEFAULT '0' NOT NULL;

ALTER TABLE license_switch ADD COLUMN end_time TIMESTAMP WITH TIME ZONE;

ALTER TABLE license_switch ADD COLUMN license_switch_uuid VARCHAR(36) DEFAULT uuid_generate_v4() NOT NULL;

ALTER TABLE license_switch ADD CONSTRAINT license_switch_pk PRIMARY KEY (license_switch_uuid);

ALTER TABLE license_switch ADD COLUMN ordered_amount INTEGER;

ALTER TABLE license_switch ADD COLUMN package_switch_uuid VARCHAR(36);

ALTER TABLE license_switch ADD COLUMN plan_uuid VARCHAR(36);

ALTER TABLE license_switch ADD COLUMN start_time TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL;

ALTER TABLE license_switch ADD COLUMN user_uuid VARCHAR(36);

CREATE INDEX ix_license_switch_package_switch_uuid ON license_switch (package_switch_uuid);

CREATE INDEX ix_license_switch_plan_uuid ON license_switch (plan_uuid);

CREATE INDEX ix_license_switch_user_uuid ON license_switch (user_uuid);

ALTER TABLE license_switch ADD FOREIGN KEY(user_uuid) REFERENCES "user" (user_uuid) ON DELETE CASCADE;

ALTER TABLE license_switch ADD FOREIGN KEY(package_switch_uuid) REFERENCES package_switch (package_switch_uuid) ON DELETE CASCADE;

ALTER TABLE license_switch ADD FOREIGN KEY(plan_uuid) REFERENCES plan (plan_uuid) ON DELETE CASCADE;

ALTER TABLE license_switch DROP COLUMN ip;

ALTER TABLE license_switch DROP COLUMN type;

ALTER TABLE payment ADD COLUMN license_lrn_uuid VARCHAR(36);

ALTER TABLE payment ADD COLUMN license_switch_uuid VARCHAR(36);

CREATE INDEX ix_payment_license_lrn_uuid ON payment (license_lrn_uuid);

CREATE INDEX ix_payment_license_switch_uuid ON payment (license_switch_uuid);

DROP INDEX ix_payment_license_period_uuid;

ALTER TABLE payment DROP CONSTRAINT payment_license_period_uuid_fkey;

ALTER TABLE payment ADD FOREIGN KEY(license_switch_uuid) REFERENCES license_switch (license_switch_uuid) ON DELETE CASCADE;

ALTER TABLE payment ADD FOREIGN KEY(license_lrn_uuid) REFERENCES license_lrn (license_lrn_uuid) ON DELETE CASCADE;

ALTER TABLE payment DROP COLUMN license_period_uuid;

DROP TABLE license_period;

DROP TABLE license;

UPDATE alembic_version SET version_num='79580b1c9691' WHERE alembic_version.version_num = '4b09277baffb';

COMMIT;

UPDATE version_information set major_ver='1.0.2',minor_ver='4b09277baffb:79580b1c9691',build_date='2018-10-29 21:29:35' where program_name='class4v6';
