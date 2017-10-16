#!/usr/bin//env bash

PSQL=psql
# PSQL='sudo -u postgres psql'

$PSQL -c "create database farmboy;"
$PSQL -c "create role farmboyuser with password 'farmboypassword';"
$PSQL -c "ALTER ROLE farmboyuser CREATEDB;"
$PSQL -c "ALTER ROLE farmboyuser SET client_encoding TO 'utf8';"
$PSQL -c "ALTER ROLE farmboyuser SET default_transaction_isolation TO 'read committed';"
$PSQL -c "ALTER ROLE farmboyuser SET timezone TO 'UTC';"
$PSQL -c "ALTER ROLE farmboyuser WITH LOGIN;"
$PSQL -c "GRANT ALL PRIVILEGES ON DATABASE farmboy TO farmboyuser;"
