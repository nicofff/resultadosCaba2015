for i in `seq 1 7377`;
do
if [ ! -f data/$i.json ];
then
    if [ $(ps -ef | grep -v grep | grep curl | wc -l) -gt 50 ]; then
    echo "More than 20 curls, sleeping for a while"
    sleep 1
fi
    curl https://apielecciones.buenosaires.gob.ar/api/mesa?id=$i -o data/$i.json &
fi
done
