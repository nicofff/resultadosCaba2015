for i in `seq 1685 7377`;
do
if [ ! -f $i.json ];
then
    curl https://apielecciones.buenosaires.gob.ar/api/mesa?id=$i -o $i.json &
fi
done
