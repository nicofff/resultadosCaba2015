set datafile separator " "
set key left top
plot 'mesasSorted.csv' using 1:2 title "PRO" with lines, "" using 1:3 title "ECO" with lines, "" using 1:4 title "FPV" with lines , "" using 1:5 title "AYL" with lines , "" using 1:6 title "FIT" with lines
