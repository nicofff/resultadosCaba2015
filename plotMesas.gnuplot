set datafile separator " "
set key left top
set style data histogram
plot 'porcMesas.csv' using 1:4 title "PRO" with lines, "" using 1:5 title "ECO" with lines, "" using 1:6 title "Blanco" with lines 
