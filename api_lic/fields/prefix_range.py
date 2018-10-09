#prefix_range
import sqlalchemy.types as types
from sqlalchemy.ext.compiler import compiles

class PrefixRange(types.TypeDecorator):
    '''Prefixes Unicode values with "PREFIX:" on the way in and
    strips it off on the way out.
    '''

    impl = types.String

    def get_col_spec(self):
        return "prefix_range"

    def process_bind_param(self, value, dialect):
        return value

    def process_result_value(self, value, dialect):
        return value

    def copy(self, **kw):
        return PrefixRange(self.impl.length)

@compiles(PrefixRange, "postgresql")
def compile_prefix_range_postgresql(type_, compiler, **kw):
    return "prefix_range"