cat $1 | cut -f3 | cut -d' ' -f4 | cut -c2-6 -c8 | awk '{print substr($0,0,5) , substr($0,6,6)}' | sed 's/F/0/g' | sed 's/T/1/g' | sed 's/?/-1/g' >> $2
