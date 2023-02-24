for file in $1; do tail -n +2 $file | cut -d',' -f1,2,4,8- ; done
