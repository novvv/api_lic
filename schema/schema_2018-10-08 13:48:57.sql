--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.10
-- Dumped by pg_dump version 9.6.10

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
-- Name: email_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.email_log (
    id integer NOT NULL,
    sender_id integer,
    name character varying(64) NOT NULL,
    subject character varying(1024) NOT NULL,
    email_from character varying(255) NOT NULL,
    email_to character varying(255) NOT NULL,
    email_cc character varying(512),
    content_text text NOT NULL,
    status character varying(512)
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
    content_text text NOT NULL,
    content_html text,
    hint text NOT NULL
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
-- Name: license; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.license (
    license_uuid character varying(36) DEFAULT public.uuid_generate_v4() NOT NULL,
    rate_uuid character varying(36)
);


--
-- Name: license_lrn; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.license_lrn (
    license_uuid character varying(36) NOT NULL,
    cps integer
);


--
-- Name: license_period; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.license_period (
    license_period_uuid character varying(36) DEFAULT public.uuid_generate_v4() NOT NULL,
    license_uuid character varying(36),
    user_uuid character varying(36) NOT NULL,
    start_time timestamp with time zone DEFAULT now() NOT NULL,
    end_time timestamp with time zone,
    cost numeric DEFAULT '0'::numeric NOT NULL
);


--
-- Name: license_switch; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.license_switch (
    license_uuid character varying(36) NOT NULL,
    ip character varying(16) NOT NULL
);


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
    user_id integer NOT NULL,
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
-- Name: payment; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.payment (
    payment_uuid character varying(36) DEFAULT public.uuid_generate_v4() NOT NULL,
    license_period_uuid character varying(36),
    amount numeric DEFAULT '0'::numeric NOT NULL,
    paid_time timestamp with time zone DEFAULT now() NOT NULL,
    type integer
);


--
-- Name: rate; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.rate (
    rate_uuid character varying(36) DEFAULT public.uuid_generate_v4() NOT NULL,
    type integer,
    rate numeric DEFAULT '0'::numeric NOT NULL
);


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
    logo_file_uuid character varying(36)
);


--
-- Name: email_log id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.email_log ALTER COLUMN id SET DEFAULT nextval('public.email_log_id_seq'::regclass);


--
-- Name: file_download_token id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.file_download_token ALTER COLUMN id SET DEFAULT nextval('public.file_download_token_id_seq'::regclass);


--
-- Name: object_revision id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.object_revision ALTER COLUMN id SET DEFAULT nextval('public.object_revision_id_seq'::regclass);


--
-- Name: object_revision_record id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.object_revision_record ALTER COLUMN id SET DEFAULT nextval('public.object_revision_record_id_seq'::regclass);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


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
-- Name: license_lrn license_lrn_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_lrn
    ADD CONSTRAINT license_lrn_pkey PRIMARY KEY (license_uuid);


--
-- Name: license_period license_period_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_period
    ADD CONSTRAINT license_period_pkey PRIMARY KEY (license_period_uuid);


--
-- Name: license license_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license
    ADD CONSTRAINT license_pkey PRIMARY KEY (license_uuid);


--
-- Name: license_switch license_switch_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_switch
    ADD CONSTRAINT license_switch_pkey PRIMARY KEY (license_uuid);


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
-- Name: payment payment_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_pkey PRIMARY KEY (payment_uuid);


--
-- Name: rate rate_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rate
    ADD CONSTRAINT rate_pkey PRIMARY KEY (rate_uuid);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_email_log_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_email_log_name ON public.email_log USING btree (name);


--
-- Name: ix_license_lrn_license_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_lrn_license_uuid ON public.license_lrn USING btree (license_uuid);


--
-- Name: ix_license_period_license_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_period_license_uuid ON public.license_period USING btree (license_uuid);


--
-- Name: ix_license_period_user_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_period_user_uuid ON public.license_period USING btree (user_uuid);


--
-- Name: ix_license_rate_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_rate_uuid ON public.license USING btree (rate_uuid);


--
-- Name: ix_license_switch_license_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_license_switch_license_uuid ON public.license_switch USING btree (license_uuid);


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
-- Name: ix_payment_license_period_uuid; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_payment_license_period_uuid ON public.payment USING btree (license_period_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: license_lrn license_lrn_license_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_lrn
    ADD CONSTRAINT license_lrn_license_uuid_fkey FOREIGN KEY (license_uuid) REFERENCES public.license(license_uuid) ON DELETE CASCADE;


--
-- Name: license_period license_period_license_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_period
    ADD CONSTRAINT license_period_license_uuid_fkey FOREIGN KEY (license_uuid) REFERENCES public.license(license_uuid) ON DELETE CASCADE;


--
-- Name: license_period license_period_user_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_period
    ADD CONSTRAINT license_period_user_uuid_fkey FOREIGN KEY (user_uuid) REFERENCES public."user"(user_uuid) ON DELETE CASCADE;


--
-- Name: license license_rate_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license
    ADD CONSTRAINT license_rate_uuid_fkey FOREIGN KEY (rate_uuid) REFERENCES public.rate(rate_uuid) ON DELETE CASCADE;


--
-- Name: license_switch license_switch_license_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.license_switch
    ADD CONSTRAINT license_switch_license_uuid_fkey FOREIGN KEY (license_uuid) REFERENCES public.license(license_uuid) ON DELETE CASCADE;


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
-- Name: payment payment_license_period_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_license_period_uuid_fkey FOREIGN KEY (license_period_uuid) REFERENCES public.license_period(license_period_uuid) ON DELETE CASCADE;


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

