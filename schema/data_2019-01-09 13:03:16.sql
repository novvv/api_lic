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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

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

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: webbackend
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


ALTER TABLE public."user" OWNER TO webbackend;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: webbackend
--

COPY public."user" (user_uuid, email, password, is_admin, last_login, is_active, confirmed_on, created_on, logo_file_uuid) FROM stdin;
17209cf7-0274-4443-9db7-747db6d77e11	admin@example.com	$2a$12$U4GiTr/95oyszLDLCDHe/e6FXCDS1E.NzkiPdmbzqlThylXC6ZQVq	t	\N	t	\N	2018-10-06 01:14:37.895171+05	\N
17209cf7-0274-4443-9db7-747db6d77e12	_novvv@mail.ru	$2a$12$cwg/8Kjkm55C6y8H9QqxheGihPXmj6f4uXvmxXSl.V5Ll4eHzfMcW	f	\N	t	\N	2018-10-06 01:14:39.227746+05	\N
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_uuid);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: webbackend
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: user user_logo_file_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: webbackend
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_logo_file_uuid_fkey FOREIGN KEY (logo_file_uuid) REFERENCES public.file(uuid);


--
-- PostgreSQL database dump complete
--

