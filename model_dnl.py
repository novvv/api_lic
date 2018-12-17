# coding: utf-8
from sqlalchemy import Boolean, CHAR, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class AuthRole(Base):
    __tablename__ = 'auth_role'
    id=Column(Integer, nullable=False, server_default=text("nextval('auth_role_id_seq'::regclass)"))
    role_name=Column(String(64))
    report_pri=Column(Boolean, server_default=text("false"))
    write_pri=Column(Boolean, server_default=text("false"))
    license_pri=Column(Boolean, server_default=text("false"))
    create_time=Column(DateTime(True))

class AuthUser(Base):
    __tablename__ = 'auth_users'

    id = Column(Integer, primary_key=True, server_default=text("nextval('auth_users_id_seq'::regclass)"))
    user_name = Column(String(64))
    user_password = Column(String(64))
    create_time = Column(DateTime(True), server_default=text("('now'::text)::timestamp(0) with time zone"))
    last_login_time = Column(DateTime(True))
    user_role_id = Column(Integer)


class Captcha(Base):
    __tablename__ = 'captcha'

    captcha_id = Column(Integer, primary_key=True, server_default=text("nextval('captcha_captcha_id_seq'::regclass)"))
    captcha_time = Column(Integer, nullable=False)
    ip_address = Column(String(16), nullable=False, server_default=text("0"))
    word = Column(String(20), nullable=False)


class ClientInfo(Base):
    __tablename__ = 'client_info'

    id = Column(Integer, primary_key=True, server_default=text("nextval('client_info_id_seq'::regclass)"))
    name = Column(String(100), index=True)
    company = Column(String(300))
    contact = Column(String(200))
    billing_email = Column(String(100))


class ClientMonthlyAccounts(Base):
    __tablename__ = 'client_monthly_accounts'
    client_id=Column(Integer, index=True)
    switch_ip=Column(String(30), index=True)
    rent=Column(Numeric(30, 6))
    received_rent=Column(Numeric(30, 6))
    is_full_payment=Column(SmallInteger, nullable=False, server_default=text("0"))
    rent_date=Column(String(16), index=True)


class ClientSwitchInfo(Base):
    __tablename__ = 'client_switch_info'
    client_id=Column(Integer, index=True)
    switch_ip=Column(String(30), index=True)

class DnlLicenseInfo(Base):
    __tablename__ = 'dnl_license_info'

    id = Column(Integer, primary_key=True)#, server_default=text("nextval('dnl_license_info_id_seq'::regclass)"))
    carrier_name = Column(String(100), index=True)
    ss_type = Column(SmallInteger, nullable=False, index=True, server_default=text("0"))
    status = Column(SmallInteger, nullable=False, server_default=text("1"))
    ss_name = Column(String(100), nullable=False, index=True)
    uuid = Column(String(128), nullable=False, index=True)
    recv_ip = Column(String(16), nullable=False)
    recv_port = Column(Integer)
    ss_bind_mac = Column(String(18), nullable=False, index=True)
    ss_bind_ip = Column(String(16), nullable=False)
    ss_bind_port = Column(Integer)
    max_cap = Column(Integer, nullable=False, server_default=text("500"))
    max_cps = Column(Integer, nullable=False, server_default=text("100"))
    start_time = Column(DateTime(True), server_default=text("('now'::text)::date"))
    end_time = Column(DateTime(True), server_default=text("(('now'::text)::date + '3650 days'::interval)"))
    expires = Column(Integer, server_default=text("3650"))
    update_time = Column(DateTime(True))
    create_time = Column(DateTime(True), server_default=text("('now'::text)::timestamp(0) with time zone"))
    create_user = Column(SmallInteger, nullable=False, server_default=text("0"))


class DnlLcenseInfoRecord(Base):
    __tablename__ = 'dnl_license_info_record'
    record_id=Column(Integer, nullable=False,primary_key=True)#, server_default=text("nextval('dnl_license_info_record_record_id_seq'::regclass)"))
    id=Column(Integer)
    carrier_name=Column(String(100))
    ss_type=Column(SmallInteger)
    status=Column(SmallInteger)
    ss_name=Column(String(100))
    uuid=Column(String(128))
    recv_ip=Column(String(16))
    recv_port=Column(Integer)
    ss_bind_mac=Column(String(18))
    ss_bind_ip=Column(String(16))
    ss_bind_port=Column(Integer)
    max_cap=Column(Integer)
    max_cps=Column(Integer)
    start_time=Column(DateTime(True))
    end_time=Column(DateTime(True))
    expires=Column(Integer)
    update_time=Column(DateTime(True))
    create_time=Column(DateTime(True))
    create_user=Column(SmallInteger)
    time=Column(Numeric)
    flag=Column(CHAR(1))


class DnlLicenseLog(Base):
    __tablename__ = 'dnl_license_log'

    id = Column(Integer, primary_key=True)#, server_default=text("nextval('dnl_license_log_id_seq'::regclass)"))
    uuid = Column(String(128), nullable=False, index=True)
    recv_ip = Column(String(16), nullable=False, index=True)
    recv_port = Column(Integer)
    cap = Column(Integer, nullable=False, server_default=text("0"))
    cps = Column(Integer, nullable=False, server_default=text("0"))
    start_time = Column(DateTime(True))
    end_time = Column(DateTime(True))
    sip_addr = Column(String(256))
    status = Column(SmallInteger, nullable=False, server_default=text("0"))
    create_time = Column(DateTime(True), server_default=text("('now'::text)::timestamp(0) with time zone"))


class DnlPreLicensingInfo(Base):
    __tablename__ = 'dnl_pre_licensing_info'

    id = Column(Integer, primary_key=True)#, server_default=text("nextval('dnl_pre_licensing_info_id_seq'::regclass)"))
    ip = Column(String(16), nullable=False)
    cap = Column(Integer, nullable=False, server_default=text("0"))
    cps = Column(Integer, nullable=False, server_default=text("0"))
    expires = Column(Integer)
    create_time = Column(DateTime(True))


class DnlPreLicensingInfoRecord(Base):
    __tablename__ = 'dnl_pre_licensing_info_record'
    record_id=Column(Integer, nullable=False, primary_key=True)#server_default=text("nextval('dnl_pre_licensing_info_record_record_id_seq'::regclass)"))
    id=Column(Integer)
    ip=Column(String(16))
    cap=Column(Integer)
    cps=Column(Integer)
    expires=Column(Integer)
    create_time=Column(DateTime(True))
    time=Column(Numeric)
    flag=Column(CHAR(1))

class SwitchDaily(Base):
    __tablename__ = 'switch_daily'
    client_id=Column(Integer, index=True)
    from_ip=Column(String(30), nullable=False, index=True)
    from_port=Column(Integer)
    max_cps=Column(Integer)
    max_cap=Column(Integer)
    call_duration=Column(Integer)
    detail=Column(String(1024))
    sip_addr=Column(String(250))
    start_date=Column(DateTime(True))
    report_date=Column(String(16), index=True)
    create_time=Column(DateTime(True), server_default=func.now())

