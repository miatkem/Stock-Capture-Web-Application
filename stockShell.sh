#!/bin/bash
if [ ! -e ~/tagsoup-1.2.1.jar ]; then
	curl http://vrici.lojban.org/~cowan/XML/tagsoup/tagsoup-1.2.1.jar > tagsoup-1.2.1.jar 
fi

for i in {0..60}
do
now=$(date +"%Y-%m-%d-%H-%M-%S")
echo "$now"
filename=${now}.html
echo "$file"
curl -o $filename http://wsj.com/mdc/public/page/2_3021-activnnm-actives.html
java -jar tagsoup-1.2.1.jar --files $filename
rm ${now}.html
filename=${now}.xhtml
Python parseStocks.py $filename
rm ${now}.xhtml
sleep 1m
done