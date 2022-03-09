#!/bin/bash
# OSX/Linux version
# Create the SQLite database and table
. common_OSX.sh

FILE="Civic_Art_Collection.csv"
FOLDER="notebooks/data"
COLLECTION="civicArt.db"
FILE_FORMAT="csv"
TABLE_NAME="civicArtTable"
DIR="$( pwd )"
THIS_SCRIPT=`basename "$0"`
showStep "running $GREEN $THIS_SCRIPT $RESET in $GREEN $DIR $RESET"
showStep "Creating $GREEN $COLLECTION $RESET collection with $GREEN $TABLE_NAME $RESET table\n-----> Data sourced from $GREEN $FOLDER/$FILE $RESET "
NEWLINE="$'\n'"
sc_1=".timeout 2000"
sc_2=".mode $FILEFORMAT $TABLE_NAME "
sc_3=".import $FOLDER/$FILE $TABLE_NAME"
SQLite_STRING="$sc_1 \n$sc_2 \n$sc_3\n"
# echo -e $SQLite_STRING
# printf '%s\n%s\n%s' $sc_1 $sc_2 $sc_3
sqlite3 $COLLECTION  <<< $( echo -e $SQLite_STRING )
sqlite3 .open" $COLLECTION"
sqlite3 .mode "$FILEFORMAT  $TABLE_NAME"
sqlite3 .import "$FOLDER/$FILE $TABLE_NAME"