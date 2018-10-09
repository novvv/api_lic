BEGIN;

-- Running upgrade d72cae15953e -> cb4c870de32e

CREATE TABLE rate (
    rate_uuid VARCHAR(36) DEFAULT uuid_generate_v4() NOT NULL, 
    type INTEGER, 
    rate NUMERIC DEFAULT '0' NOT NULL, 
    PRIMARY KEY (rate_uuid)
);

CREATE TABLE license (
    license_uuid VARCHAR(36) DEFAULT uuid_generate_v4() NOT NULL, 
    rate_uuid VARCHAR(36), 
    PRIMARY KEY (license_uuid), 
    FOREIGN KEY(rate_uuid) REFERENCES rate (rate_uuid) ON DELETE CASCADE
);

CREATE INDEX ix_license_rate_uuid ON license (rate_uuid);

CREATE TABLE license_lrn (
    license_uuid VARCHAR(36) NOT NULL, 
    cps INTEGER, 
    PRIMARY KEY (license_uuid), 
    FOREIGN KEY(license_uuid) REFERENCES license (license_uuid) ON DELETE CASCADE
);

CREATE INDEX ix_license_lrn_license_uuid ON license_lrn (license_uuid);

CREATE TABLE license_period (
    license_period_uuid VARCHAR(36) DEFAULT uuid_generate_v4() NOT NULL, 
    license_uuid VARCHAR(36), 
    user_uuid VARCHAR(36) NOT NULL, 
    start_time TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
    end_time TIMESTAMP WITH TIME ZONE, 
    cost NUMERIC DEFAULT '0' NOT NULL, 
    PRIMARY KEY (license_period_uuid), 
    FOREIGN KEY(license_uuid) REFERENCES license (license_uuid) ON DELETE CASCADE, 
    FOREIGN KEY(user_uuid) REFERENCES "user" (user_uuid) ON DELETE CASCADE
);

CREATE INDEX ix_license_period_license_uuid ON license_period (license_uuid);

CREATE INDEX ix_license_period_user_uuid ON license_period (user_uuid);

CREATE TABLE license_switch (
    license_uuid VARCHAR(36) NOT NULL, 
    ip VARCHAR(16) NOT NULL, 
    PRIMARY KEY (license_uuid), 
    FOREIGN KEY(license_uuid) REFERENCES license (license_uuid) ON DELETE CASCADE
);

CREATE INDEX ix_license_switch_license_uuid ON license_switch (license_uuid);

CREATE TABLE notification (
    notification_uuid VARCHAR(36) DEFAULT uuid_generate_v4() NOT NULL, 
    user_uuid VARCHAR(36), 
    subject VARCHAR(64) NOT NULL, 
    content TEXT NOT NULL, 
    created_on TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
    PRIMARY KEY (notification_uuid), 
    FOREIGN KEY(user_uuid) REFERENCES "user" (user_uuid) ON DELETE CASCADE
);

CREATE INDEX ix_notification_user_uuid ON notification (user_uuid);

CREATE TABLE payment (
    payment_uuid VARCHAR(36) DEFAULT uuid_generate_v4() NOT NULL, 
    license_period_uuid VARCHAR(36), 
    amount NUMERIC DEFAULT '0' NOT NULL, 
    paid_time TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
    type INTEGER, 
    PRIMARY KEY (payment_uuid), 
    FOREIGN KEY(license_period_uuid) REFERENCES license_period (license_period_uuid) ON DELETE CASCADE
);

CREATE INDEX ix_payment_license_period_uuid ON payment (license_period_uuid);

UPDATE alembic_version SET version_num='cb4c870de32e' WHERE alembic_version.version_num = 'd72cae15953e';

COMMIT;

UPDATE version_information set major_ver='1.0.28',minor_ver='d72cae15953e:cb4c870de32e',build_date='2018-10-08 13:49:03' where program_name='class4v6';
