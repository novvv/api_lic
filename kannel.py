usage: sqlacodegen [-h] [--version] [--schema SCHEMA] [--tables TABLES]
                   [--noviews] [--noindexes] [--noconstraints] [--nojoined]
                   [--noinflect] [--noclasses] [--outfile OUTFILE]
                   [url]

Generates SQLAlchemy model code from an existing database.

positional arguments:
  url                SQLAlchemy url to the database

optional arguments:
  -h, --help         show this help message and exit
  --version          print the version number and exit
  --schema SCHEMA    load tables from an alternate schema
  --tables TABLES    tables to process (comma-separated, default: all)
  --noviews          ignore views
  --noindexes        ignore indexes
  --noconstraints    ignore constraints
  --nojoined         don't autodetect joined table inheritance
  --noinflect        don't try to convert tables names to singular form
  --noclasses        don't generate classes, only tables
  --outfile OUTFILE  file to write output to (default: stdout)
