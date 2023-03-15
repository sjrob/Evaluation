mkfifo test.csv
python mosq_numbers_from_csv.py test.csv > $2 & ; cat $1 > test.csv
rm test.csv
