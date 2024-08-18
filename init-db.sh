#!/bin/bash
set -e

# Adiciona a configuração de trust no pg_hba.conf
echo "local all all trust" >> /var/lib/postgresql/data/pg_hba.conf
echo "host all all 127.0.0.1/32 trust" >> /var/lib/postgresql/data/pg_hba.conf

# Executa o comando padrão para iniciar o PostgreSQL
exec "$@"
