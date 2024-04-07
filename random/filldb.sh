#!/usr/bin/env bash

for purl in $(curl -s 'https://pokeapi.co/api/v2/pokemon?offset=1&limit=51' | jq -r '.results[].url')
do
    pk="$(curl -s $purl | 
        jq '{num: .id, 
            name: .name, 
            hp: .stats[0].base_stat, 
            atk: .stats[1].base_stat, 
            def: .stats[2].base_stat, 
            satk: .stats[3].base_stat, 
            sdef: .stats[4].base_stat, 
            speed: .stats[5].base_stat, 
            type1: .types[0].type.name | ascii_upcase, 
            type2: (if .types[1] then .types[1].type.name | ascii_upcase else null end)}'
        )"

    echo $pk | curl -H "Content-Type: application/json" -d '@-' http://localhost:8080/pokemon
done
