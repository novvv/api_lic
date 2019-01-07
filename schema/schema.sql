--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.11
-- Dumped by pg_dump version 9.6.11

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


--
-- Name: config_payment; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.config_payment (
    id integer NOT NULL,
    charge_type integer,
    stripe_email character varying(64),
    stripe_skey character varying(64),
    stripe_pkey character varying(64),
    stripe_svc_charge integer,
    stripe_test_mode boolean,
    confirm_enabled boolean,
    email_confirm_to character varying(64),
    notification_enabled boolean,
    email_cc_to character varying(64),
    paypal_email character varying(64),
    paypal_pkey character varying(128),
    paypal_skey character varying(128),
    paypal_svc_charge numeric,
    paypal_test_mode boolean
);


--
-- Name: config_payment_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.config_payment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: config_payment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.config_payment_id_seq OWNED BY public.config_payment.id;


--
-- Name: dnl_license_info; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.dnl_license_info (
    id integer NOT NULL,
    carrier_name character varying(100),
    ss_type smallint DEFAULT 0 NOT NULL,
    status smallint DEFAULT 1 NOT NULL,
    ss_name character varying(100) NOT NULL,
    uuid character varying(128) NOT NULL,
    recv_ip character varying(16) NOT NULL,
    recv_port integer,
    ss_bind_mac character varying(18) NOT NULL,
    ss_bind_ip character varying(16) NOT NULL,
    ss_bind_port integer,
    max_cap integer DEFAULT 500 NOT NULL,
    max_cps integer DEFAULT 100 NOT NULL,
    start_time timestamp with time zone DEFAULT ('now'::text)::date,
    end_time timestamp with time zone DEFAULT (('now'::text)::date + '3650 days'::interval),
    expires integer DEFAULT 3650,
    update_time timestamp with time zone,
    create_time timestamp with time zone DEFAULT now(),
    create_user smallint DEFAULT 0 NOT NULL
);


--
-- Name: dnl_license_info_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.dnl_license_info_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: dnl_license_info_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.dnl_license_info_id_seq OWNED BY public.dnl_license_info.id;


--
-- Name: dnl_license_info_record; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.dnl_license_info_record (
    record_id integer NOT NULL,
    id integer,
    carrier_name character varying(100),
    ss_type smallint,
    status smallint,
    ss_name character varying(100),
    uuid character varying(128),
    recv_ip character varying(16),
    recv_port integer,
    ss_bind_mac character varying(18),
    ss_bind_ip character varying(16),
    ss_bind_port integer,
    max_cap integer,
    max_cps integer,
    start_time timestamp with time zone,
    end_time timestamp with time zone,
    expires integer,
    update_time timestamp with time zone,
    create_time timestamp with time zone,
    create_user smallint,
    "time" numeric,
    flag character(1)
);


--
-- Name: dnl_license_info_record_record_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.dnl_license_info_record_record_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: dnl_license_info_record_record_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.dnl_license_info_record_record_id_seq OWNED BY public.dnl_license_info_record.record_id;


--
-- Name: dnl_license_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.dnl_license_log (
    id integer NOT NULL,
    uuid character varying(128) NOT NULL,
    recv_ip character varying(16) NOT NULL,
    recv_port integer,
    cap integer DEFAULT 0 NOT NULL,
    cps integer DEFAULT 0 NOT NULL,
    start_time timestamp with time zone,
    end_time timestamp with time zone,
    sip_addr character varying(256),
    status smallint DEFAULT 0 NOT NULL,
    create_time timestamp with time zone DEFAULT now()
);


--
-- Name: dnl_license_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.dnl_license_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: dnl_license_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.dnl_license_log_id_seq OWNED BY public.dnl_license_log.id;


--
-- Name: dnl_pre_licensing_info; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.dnl_pre_licensing_info (
    id integer NOT NULL,
    ip character varying(16) NOT NULL,
    cap integer DEFAULT 0 NOT NULL,
    cps integer DEFAULT 0 NOT NULL,
    expires integer,
    create_time timestamp with time zone DEFAULT now()
);


--
-- Name: dnl_pre_licensing_info_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.dnl_pre_licensing_info_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: dnl_pre_licensing_info_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.dnl_pre_licensing_info_id_seq OWNED BY public.dnl_pre_licensing_info.id;


--
-- Name: dnl_pre_licensing_info_record; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.dnl_pre_licensing_info_record (
    record_id integer NOT NULL,
    id integer,
    ip character varying(16),
    cap integer,
    cps integer,
    expires integer,
    create_time timestamp with time zone DEFAULT now(),
    "time" numeric,
    flag character(1)
);


--
-- Name: dnl_pre_licensing_info_record_record_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.dnl_pre_licensing_info_record_record_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: dnl_pre_licensing_info_record_record_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.dnl_pre_licensing_info_record_record_id_seq OWNED BY public.dnl_pre_licensing_info_record.record_id;


--
-- Name: email_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.email_log (
    id integer NOT NULL,
    name character varying(64) NOT NULL,
    subject character varying(1024) NOT NULL,
    email_from character varying(255) NOT NULL,
    email_to character varying(255) NOT NULL,
    email_cc character varying(512),
    content_text text NOT NULL,
    status character varying(512),
    sender_id character varying(36)
);


--
-- Name: email_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.email_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: email_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.email_log_id_seq OWNED BY public.email_log.id;


--
-- Name: email_template; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.email_template (
    name character varying(64) NOT NULL,
    subject character varying(1024) NOT NULL,
    email_from character varying(255) NOT NULL,
    email_cc character varying(512),
    content_text text,
    content_html text NOT NULL,
    hint text
);


--
-- Name: file; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.file (
    uuid character varying(36) NOT NULL,
    path character varying(1024) NOT NULL,
    belongs_to_table character varying(255) NOT NULL,
    belongs_to_field character varying(255) NOT NULL,
    belongs_to_pk character varying(128),
    uploaded_on timestamp with time zone NOT NULL,
    attached_on timestamp with time zone DEFAULT now(),
    public boolean DEFAULT false
);


--
-- Name: file__tmp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.file__tmp (
    uuid character varying(36) NOT NULL,
    path character varying(1024) NOT NULL,
    belongs_to_table character varying(255) NOT NULL,
    belongs_to_field character varying(255) NOT NULL,
    uploaded_on timestamp with time zone DEFAULT now(),
    public boolean DEFAULT false
);


--
-- Name: file_download_token; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.file_download_token (
    id integer NOT NULL,
    file_uuid character varying(36),
    token character varying(1024)
);


--
-- Name: file_download_token_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.file_download_token_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: file_download_token_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.file_download_token_id_seq OWNED BY public.file_download_token.id;


--
-- Name: license_lrn; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.license_lrn (
    cost numeric DEFAULT '0'::numeric NOT NULL,
    end_time timestamp with time zone,
    license_lrn_uuid character varying(36) DEFAULT public.uuid_generate_v4() NOT NULL,
    ordered_amount integer,
    package_lrn_uuid character varying(36),
    start_time timestamp with time zone DEFAULT now() NOT NULL,
    user_uuid character varying(36),
    ip character varying(16) NOT NULL,
    is_enabled boolean,
    duration integer DEFAULT 1
);


--
-- Name: license_switch; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.license_switch (
    cost numeric DEFAULT '0'::numeric NOT NULL,
    end_time timestamp with time zone,
    license_switch_uuid character varying(36) DEFAULT public.uuid_generate_v4() NOT NULL,
    ordered_amount integer,
    package_switch_uuid character varying(36),
    start_time timestamp with time zone DEFAULT now() NOT NULL,
    user_uuid character varying(36),
    ip character varying(16) NOT NULL,
    is_enabled boolean,
    duration integer DEFAULT 1
);


--
-- Name: license_update_history; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.license_update_history (
    id integer NOT NULL,
    uuid character varying(100),
    license_channel integer,
    license_cps integer,
    license_day integer,
    client_name character varying(100),
    remarks character varying(100),
    action smallint DEFAULT '0'::smallint NOT NULL,
    status_1 smallint DEFAULT '0'::smallint NOT NULL,
    status_2 smallint DEFAULT '0'::smallint NOT NULL,
    progress character varying(200),
    operator character varying(50),
    create_on timestamp with time zone DEFAULT now() NOT NULL,
    remain character varying
);


--
-- Name: license_update_history_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.license_update_history_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: license_update_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.license_update_history_id_seq OWNED BY public.license_update_history.id;


--
-- Name: lrn_permission_update_history; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.lrn_permission_update_history (
    id integer NOT NULL,
    switch_ip character varying(16),
    permit_cps integer,
    client_name character varying(100),
    remarks character varying(200),
    action smallint DEFAULT '0'::smallint NOT NULL,
    status_1 smallint DEFAULT '0'::smallint NOT NULL,
    progress character varying(200) DEFAULT '0'::character varying NOT NULL,
    operator character varying(50),
    create_on timestamp with time zone DEFAULT now() NOT NULL,
    remain character varying
);


--
-- Name: lrn_permission_update_history_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.lrn_permission_update_history_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: lrn_permission_update_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.lrn_permission_update_history_id_seq OWNED BY public.lrn_permission_update_history.id;


--
-- Name: notification; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.notification (
    notification_uuid character varying(36) DEFAULT public.uuid_generate_v4() NOT NULL,
    user_uuid character varying(36),
    subject character varying(64) NOT NULL,
    content text NOT NULL,
    created_on timestamp with time zone DEFAULT now() NOT NULL
);


--
-- Name: object_revision; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.object_revision (
    id bigint NOT NULL,
    user_id character varying(36) NOT NULL,
    entity_name character varying(64) NOT NULL,
    entity_pk character varying(64) NOT NULL,
    action character varying(16) NOT NULL,
    revision_number integer NOT NULL,
    revision_time timestamp with time zone NOT NULL,
    restored_from_revision_id bigint
);


--
-- Name: object_revision_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.object_revision_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: object_revision_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.object_revision_id_seq OWNED BY public.object_revision.id;


--
-- Name: object_revision_record; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.object_revision_record (
    id bigint NOT NULL,
    object_revision_id bigint NOT NULL,
    field_name character varying(64) NOT NULL,
    old_value text,
    new_value text
);


--
-- Name: object_revision_record_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.object_revision_record_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: object_revision_record_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.object_revision_record_id_seq OWNED BY public.object_revision_record.id;


--
-- Name: package_lrn; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.package_lrn (
    package_lrn_uuid character varying(36) DEFAULT public.uuid_generate_v4() NOT NULL,
    package_name character varying(64),
    cps integer,
    type integer,
    lrn_port integer,
    dip_count integer,
    amount integer,
    enabled boolean
);


--
-- Name: package_switch; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.package_switch (
    package_switch_uuid character varying(36) DEFAULT public.uuid_generate_v4() NOT NULL,
    package_name character varying(64),
    type integer,
    switch_port integer,
    minute_count integer,
    amount integer,
    enabled boolean,
    switch_uuid character varying(128),
    sub_type integer,
    expire_date timestamp with time zone,
    start_date timestamp with time zone DEFAULT now() NOT NULL
);


--
-- Name: payment; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.payment (
    payment_uuid character varying(36) DEFAULT public.uuid_generate_v4() NOT NULL,
    paid_time timestamp with time zone DEFAULT now() NOT NULL,
    type integer,
    description text,
    user_uuid character varying(36),
    license_lrn_uuid character varying(36),
    license_switch_uuid character varying(36),
    amount_lrn numeric DEFAULT '0'::numeric NOT NULL,
    amount_switch numeric DEFAULT '0'::numeric NOT NULL,
    switch_uuid character varying(128)
);


--
-- Name: plan; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.plan (
    plan_uuid character varying(36) DEFAULT public.uuid_generate_v4() NOT NULL,
    type integer,
    amount numeric DEFAULT '0'::numeric NOT NULL
);


--
-- Name: switch; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.switch (
    switch_uuid character varying(36) DEFAULT public.uuid_generate_v4() NOT NULL,
    switch_ip character varying(16),
    enabled boolean,
    current_port_count integer,
    minute_remaining integer,
    expired_on timestamp with time zone,
    email character varying(256)
);


--
-- Name: switch_daily; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.switch_daily (
    id integer NOT NULL,
    client_id character varying(36),
    from_ip character varying(30) NOT NULL,
    from_port integer,
    max_cps integer,
    max_cap integer,
    call_duration integer,
    detail character varying(1024),
    sip_addr character varying(250),
    start_date timestamp with time zone,
    report_date character varying(16),
    create_time timestamp with time zone DEFAULT now()
);


--
-- Name: switch_daily_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.switch_daily_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: switch_daily_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.switch_daily_id_seq OWNED BY public.switch_daily.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."user" (
    user_uuid character varying(36) DEFAULT public.uuid_generate_v4() NOT NULL,
    email character varying(128) NOT NULL,
    password character varying(72),
    is_admin boolean,
    last_login timestamp with time zone,
    is_active boolean,
    confirmed_on timestamp with time zone,
    created_on timestamp with time zone DEFAULT now(),
    logo_file_uuid character varying(36),
    alert_license_expired boolean DEFAULT true,
    alert_license_purchased boolean DEFAULT true,
    alert_license_will_expired boolean DEFAULT true,
    alert_payment_received boolean DEFAULT true
);


--
-- Name: config_payment id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.config_payment ALTER COLUMN id SET DEFAULT nextval('public.config_payment_id_seq'::regclass);


--
-- Name: dnl_license_info id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dnl_license_info ALTER COLUMN id SET DEFAULT nextval('public.dnl_license_info_id_seq'::regclass);


--
-- Name: dnl_license_info_record record_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dnl_license_info_record ALTER COLUMN record_id SET DEFAULT nextval('public.dnl_license_info_record_record_id_seq'::regclass);


--
-- Name: dnl_license_log id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dnl_license_log ALTER COLUMN id SET DEFAULT nextval('public.dnl_license_log_id_seq'::regclass);


--
-- Name: dnl_pre_licensing_info id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dnl_pre_licensing_info ALTER COLUMN id SET DEFAULT nextval('public.dnl_pre_licensing_info_id_seq'::regclass);


--
-- Name: dnl_pre_licensing_info_record record_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dnl_pre_licensing_info_record ALTER COLUMN record_id SET DEFAULT nextval('public.dnl_pre_licensing_info_record_record_id_seq'::regclass);


--
-- Name: email_log id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.email_log ALTER COLUMN id SET DEFAULT nextval('public.email_log_id_seq'::regclass);


--
-- Name: file_download_token id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.file_download_token ALTER COLUMN id SET DEFAULT nextval('public.file_download_token_id_seq'::regclass);


--
-- Name: license_update_history id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_update_history ALTER COLUMN id SET DEFAULT nextval('public.license_update_history_id_seq'::regclass);


--
-- Name: lrn_permission_update_history id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.lrn_permission_update_history ALTER COLUMN id SET DEFAULT nextval('public.lrn_permission_update_history_id_seq'::regclass);


--
-- Name: object_revision id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.object_revision ALTER COLUMN id SET DEFAULT nextval('public.object_revision_id_seq'::regclass);


--
-- Name: object_revision_record id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.object_revision_record ALTER COLUMN id SET DEFAULT nextval('public.object_revision_record_id_seq'::regclass);


--
-- Name: switch_daily id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.switch_daily ALTER COLUMN id SET DEFAULT nextval('public.switch_daily_id_seq'::regclass);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: config_payment config_payment_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.config_payment
    ADD CONSTRAINT config_payment_pkey PRIMARY KEY (id);


--
-- Name: dnl_license_info dnl_license_info_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dnl_license_info
    ADD CONSTRAINT dnl_license_info_pkey PRIMARY KEY (id);


--
-- Name: dnl_license_info_record dnl_license_info_record_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dnl_license_info_record
    ADD CONSTRAINT dnl_license_info_record_pkey PRIMARY KEY (record_id);


--
-- Name: dnl_license_log dnl_license_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dnl_license_log
    ADD CONSTRAINT dnl_license_log_pkey PRIMARY KEY (id);


--
-- Name: dnl_pre_licensing_info dnl_pre_licensing_info_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dnl_pre_licensing_info
    ADD CONSTRAINT dnl_pre_licensing_info_pkey PRIMARY KEY (id);


--
-- Name: dnl_pre_licensing_info_record dnl_pre_licensing_info_record_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dnl_pre_licensing_info_record
    ADD CONSTRAINT dnl_pre_licensing_info_record_pkey PRIMARY KEY (record_id);


--
-- Name: email_log email_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.email_log
    ADD CONSTRAINT email_log_pkey PRIMARY KEY (id);


--
-- Name: email_template email_template_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.email_template
    ADD CONSTRAINT email_template_pkey PRIMARY KEY (name);


--
-- Name: file__tmp file__tmp_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.file__tmp
    ADD CONSTRAINT file__tmp_pkey PRIMARY KEY (uuid);


--
-- Name: file_download_token file_download_token_file_uuid_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.file_download_token
    ADD CONSTRAINT file_download_token_file_uuid_key UNIQUE (file_uuid);


--
-- Name: file_download_token file_download_token_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.file_download_token
    ADD CONSTRAINT file_download_token_pkey PRIMARY KEY (id);


--
-- Name: file file_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.file
    ADD CONSTRAINT file_pkey PRIMARY KEY (uuid);


--
-- Name: license_lrn license_lrn_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_lrn
    ADD CONSTRAINT license_lrn_pk PRIMARY KEY (license_lrn_uuid);


--
-- Name: license_switch license_switch_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_switch
    ADD CONSTRAINT license_switch_pk PRIMARY KEY (license_switch_uuid);


--
-- Name: license_update_history license_update_history_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_update_history
    ADD CONSTRAINT license_update_history_pkey PRIMARY KEY (id);


--
-- Name: lrn_permission_update_history lrn_permission_update_history_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.lrn_permission_update_history
    ADD CONSTRAINT lrn_permission_update_history_pkey PRIMARY KEY (id);


--
-- Name: notification notification_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.notification
    ADD CONSTRAINT notification_pkey PRIMARY KEY (notification_uuid);


--
-- Name: object_revision object_revision_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.object_revision
    ADD CONSTRAINT object_revision_pkey PRIMARY KEY (id);


--
-- Name: object_revision_record object_revision_record_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.object_revision_record
    ADD CONSTRAINT object_revision_record_pkey PRIMARY KEY (id);


--
-- Name: package_lrn package_lrn_package_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.package_lrn
    ADD CONSTRAINT package_lrn_package_name_key UNIQUE (package_name);


--
-- Name: package_lrn package_lrn_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.package_lrn
    ADD CONSTRAINT package_lrn_pkey PRIMARY KEY (package_lrn_uuid);


--
-- Name: package_switch package_switch_package_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.package_switch
    ADD CONSTRAINT package_switch_package_name_key UNIQUE (package_name);


--
-- Name: package_switch package_switch_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.package_switch
    ADD CONSTRAINT package_switch_pkey PRIMARY KEY (package_switch_uuid);


--
-- Name: payment payment_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_pkey PRIMARY KEY (payment_uuid);


--
-- Name: plan plan_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.plan
    ADD CONSTRAINT plan_pkey PRIMARY KEY (plan_uuid);


--
-- Name: switch_daily switch_daily_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.switch_daily
    ADD CONSTRAINT switch_daily_pkey PRIMARY KEY (id);


--
-- Name: switch switch_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.switch
    ADD CONSTRAINT switch_pkey PRIMARY KEY (switch_uuid);


--
-- Name: license_lrn uq_license_lrn_package_lrn_uuid_user_uuid; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_lrn
    ADD CONSTRAINT uq_license_lrn_package_lrn_uuid_user_uuid UNIQUE (package_lrn_uuid, user_uuid);


--
-- Name: license_switch uq_license_switch_package_switch_uuid_user_uuid; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_switch
    ADD CONSTRAINT uq_license_switch_package_switch_uuid_user_uuid UNIQUE (package_switch_uuid, user_uuid);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_dnl_license_info_carrier_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_dnl_license_info_carrier_name ON public.dnl_license_info USING btree (carrier_name);


--
-- Name: ix_dnl_license_info_ss_bind_mac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_dnl_license_info_ss_bind_mac ON public.dnl_license_info USING btree (ss_bind_mac);


--
-- Name: ix_dnl_license_info_ss_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_dnl_license_info_ss_name ON public.dnl_license_info USING btree (ss_name);


--
-- Name: ix_dnl_license_info_ss_type; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_dnl_license_info_ss_type ON public.dnl_license_info USING btree (ss_type);


--
-- Name: ix_dnl_license_info_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_dnl_license_info_uuid ON public.dnl_license_info USING btree (uuid);


--
-- Name: ix_dnl_license_log_recv_ip; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_dnl_license_log_recv_ip ON public.dnl_license_log USING btree (recv_ip);


--
-- Name: ix_dnl_license_log_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_dnl_license_log_uuid ON public.dnl_license_log USING btree (uuid);


--
-- Name: ix_email_log_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_email_log_name ON public.email_log USING btree (name);


--
-- Name: ix_license_lrn_ip; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_lrn_ip ON public.license_lrn USING btree (ip);


--
-- Name: ix_license_lrn_package_lrn_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_lrn_package_lrn_uuid ON public.license_lrn USING btree (package_lrn_uuid);


--
-- Name: ix_license_lrn_user_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_lrn_user_uuid ON public.license_lrn USING btree (user_uuid);


--
-- Name: ix_license_switch_ip; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_switch_ip ON public.license_switch USING btree (ip);


--
-- Name: ix_license_switch_package_switch_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_switch_package_switch_uuid ON public.license_switch USING btree (package_switch_uuid);


--
-- Name: ix_license_switch_user_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_switch_user_uuid ON public.license_switch USING btree (user_uuid);


--
-- Name: ix_license_update_history_status_1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_update_history_status_1 ON public.license_update_history USING btree (status_1);


--
-- Name: ix_license_update_history_status_2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_update_history_status_2 ON public.license_update_history USING btree (status_2);


--
-- Name: ix_license_update_history_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_update_history_uuid ON public.license_update_history USING btree (uuid);


--
-- Name: ix_lrn_permission_update_history_progress; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_lrn_permission_update_history_progress ON public.lrn_permission_update_history USING btree (progress);


--
-- Name: ix_lrn_permission_update_history_status_1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_lrn_permission_update_history_status_1 ON public.lrn_permission_update_history USING btree (status_1);


--
-- Name: ix_notification_user_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_notification_user_uuid ON public.notification USING btree (user_uuid);


--
-- Name: ix_object_revision_action; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_object_revision_action ON public.object_revision USING btree (action);


--
-- Name: ix_object_revision_entity_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_object_revision_entity_name ON public.object_revision USING btree (entity_name);


--
-- Name: ix_object_revision_entity_pk; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_object_revision_entity_pk ON public.object_revision USING btree (entity_pk);


--
-- Name: ix_object_revision_revision_number; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_object_revision_revision_number ON public.object_revision USING btree (revision_number);


--
-- Name: ix_object_revision_user_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_object_revision_user_id ON public.object_revision USING btree (user_id);


--
-- Name: ix_package_switch_switch_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_package_switch_switch_uuid ON public.package_switch USING btree (switch_uuid);


--
-- Name: ix_payment_license_lrn_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_payment_license_lrn_uuid ON public.payment USING btree (license_lrn_uuid);


--
-- Name: ix_payment_license_switch_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_payment_license_switch_uuid ON public.payment USING btree (license_switch_uuid);


--
-- Name: ix_payment_switch_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_payment_switch_uuid ON public.payment USING btree (switch_uuid);


--
-- Name: ix_payment_user_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_payment_user_uuid ON public.payment USING btree (user_uuid);


--
-- Name: ix_switch_daily_client_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_switch_daily_client_id ON public.switch_daily USING btree (client_id);


--
-- Name: ix_switch_daily_from_ip; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_switch_daily_from_ip ON public.switch_daily USING btree (from_ip);


--
-- Name: ix_switch_daily_report_date; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_switch_daily_report_date ON public.switch_daily USING btree (report_date);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: license_lrn license_lrn_package_lrn_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_lrn
    ADD CONSTRAINT license_lrn_package_lrn_uuid_fkey FOREIGN KEY (package_lrn_uuid) REFERENCES public.package_lrn(package_lrn_uuid) ON DELETE CASCADE;


--
-- Name: license_lrn license_lrn_user_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_lrn
    ADD CONSTRAINT license_lrn_user_uuid_fkey FOREIGN KEY (user_uuid) REFERENCES public."user"(user_uuid) ON DELETE CASCADE;


--
-- Name: license_switch license_switch_package_switch_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_switch
    ADD CONSTRAINT license_switch_package_switch_uuid_fkey FOREIGN KEY (package_switch_uuid) REFERENCES public.package_switch(package_switch_uuid) ON DELETE CASCADE;


--
-- Name: license_switch license_switch_user_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_switch
    ADD CONSTRAINT license_switch_user_uuid_fkey FOREIGN KEY (user_uuid) REFERENCES public."user"(user_uuid) ON DELETE CASCADE;


--
-- Name: notification notification_user_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.notification
    ADD CONSTRAINT notification_user_uuid_fkey FOREIGN KEY (user_uuid) REFERENCES public."user"(user_uuid) ON DELETE CASCADE;


--
-- Name: object_revision_record object_revision_record_object_revision_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.object_revision_record
    ADD CONSTRAINT object_revision_record_object_revision_id_fkey FOREIGN KEY (object_revision_id) REFERENCES public.object_revision(id) ON DELETE CASCADE;


--
-- Name: payment payment_license_lrn_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_license_lrn_uuid_fkey FOREIGN KEY (license_lrn_uuid) REFERENCES public.license_lrn(license_lrn_uuid) ON DELETE CASCADE;


--
-- Name: payment payment_license_switch_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_license_switch_uuid_fkey FOREIGN KEY (license_switch_uuid) REFERENCES public.license_switch(license_switch_uuid) ON DELETE CASCADE;


--
-- Name: payment payment_user_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_user_uuid_fkey FOREIGN KEY (user_uuid) REFERENCES public."user"(user_uuid) ON DELETE CASCADE;


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

