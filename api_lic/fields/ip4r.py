#prefix_range
import sqlalchemy.types as types
from sqlalchemy.ext.compiler import compiles

class Ip4(types.TypeDecorator):
    '''Prefixes Unicode values with "PREFIX:" on the way in and
    strips it off on the way out.
    '''

    impl = types.String

    def get_col_spec(self):
        return "ip4"

    def process_bind_param(self, value, dialect):
        return value

    def process_result_value(self, value, dialect):
        return value

    def copy(self, **kw):
        return Ip4(self.impl.length)

@compiles(Ip4, "postgresql")
def compile_ip4_postgresql(type_, compiler, **kw):
    return "ip4"

class Ip4r(types.TypeDecorator):
    '''Prefixes Unicode values with "PREFIX:" on the way in and
    strips it off on the way out.
    '''

    impl = types.String

    def get_col_spec(self):
        return "ip4r"

    def process_bind_param(self, value, dialect):
        return value

    def process_result_value(self, value, dialect):
        return value

    def copy(self, **kw):
        return Ip4r(self.impl.length)

@compiles(Ip4r, "postgresql")
def compile_ip4r_postgresql(type_, compiler, **kw):
    return "ip4r"