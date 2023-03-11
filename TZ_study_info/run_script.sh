mkfifo test.csv
python mosq_numbers_from_csv.py test.csv > out.csv & ; cat $1 > test.csv
rm test.csv
