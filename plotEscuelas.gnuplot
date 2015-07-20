set datafile separator ","
set key left top
set style data histogram
plot 'totalesEscuela.csv' using 2:($5/($4-$7))*100 title "PRO" with lines, "" using 2:($6/($4-$7))*100 title "ECO" with lines, "" using 2:($7/$4)*100 title "Blanco" with lines 
