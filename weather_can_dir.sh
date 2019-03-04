#!/bin/bash

wget -O ./stations_dir/raw_directory.csv ftp://client_climate@ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/Station%20Inventory%20EN.csv  

python clean_dir_file.py 
python3 clean_dir_file.py 
echo $?