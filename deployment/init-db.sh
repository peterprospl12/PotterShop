#!/bin/bash

# Konfiguracja dla importu bazy danych
DB_HOST="admin-mysql_db.1.l98q1e4h4cnparwuxzj1eqk2r"        # Host bazy danych (nazwa kontenera)
DB_USER="root"                  # Nazwa użytkownika bazy danych
DB_PASS="student"               # Hasło do bazy danych
DB_NAME="BE_188667"             # Nazwa bazy danych do utworzenia
DUMP_FILE="./prestashop.sql" # Ścieżka do pliku dump na hoście

# Sprawdzanie, czy plik dump istnieje
if [ ! -f "$DUMP_FILE" ]; then
    echo "Plik dump $DUMP_FILE nie istnieje."
    exit 1
fi

# Usunięcie tabeli, jeśli istnieje
docker exec -i $DB_HOST mysql -u "$DB_USER" -p"$DB_PASS" -e "USE $DB_NAME; DROP TABLE IF EXISTS $TABLE_NAME;"

# Tworzenie bazy danych, jeśli nie istnieje
docker exec -i $DB_HOST mysql -u "$DB_USER" -p"$DB_PASS" -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"

# Importowanie danych z pliku dump
docker exec -i $DB_HOST mysql -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" < "$DUMP_FILE"

# Sprawdzanie statusu operacji
if [ $? -eq 0 ]; then
    echo "Baza danych została pomyślnie zaimportowana z pliku: $DUMP_FILE"
else
    echo "Wystąpił błąd przy imporcie bazy danych."
    exit 1
fi


