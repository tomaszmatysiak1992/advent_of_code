#/usr/bin/env bash

set -e

template='README.md.template'
readme='README.md'
stats_match='sed-day-stats'

cp $template $readme

for dir in day_*; do
    solution=$dir/main.py
    loc=$(wc -l < $solution)
    flake=$(flake8 $solution | wc -l)
    fors=$(grep -E '(\s|^)for(\s|$)' $solution | wc -l)
    whiles=$(grep -E '(\s|^)while(\s|$)' $solution | wc -l)
    day_num=$(echo ${dir: -2} | bc)
    line="$day_num | $loc | $flake | $fors | $whiles"
    gsed -i "/$stats_match/i $line" $readme
done

gsed -i "s/$stats_match//g" $readme
