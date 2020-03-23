#!/bin/bash

#
#

tar xzf *tgz
rm -f *reg *image.img.gz *20.0keV_rbn.img.gz

echo "MakeFits.py ..."
python MakeFits.py
echo "ok"

echo "RenameMJD.py ..."
python RenameMJD.py
echo "ok"

echo "MakeJpeg.py ..."
python MakeJpeg.py
echo "ok"

echo "Crop.py ..."
python Crop.py
echo "ok"

rm -rf fits jpeg
mv crop InputImage

echo "finish !!!!!!!!"
