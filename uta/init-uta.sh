set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER uta_admin;
        CREATE USER anonymous;
	CREATE DATABASE uta;
	GRANT ALL PRIVILEGES ON DATABASE uta TO uta_admin;
EOSQL

# Populate the UTA postgresql database with data gotten from
# biocommons.org
# gzip -cdq ${UTA_VERSION} | grep -v "^REFRESH MATERIALIZED VIEW" | psql -h /var/run/postgresql -U uta_admin --echo-errors --single-transaction -v ON_ERROR_STOP=1 -d uta -p 5432
