#!/bin/bash

#
#

echo "make_fits.py ..."
make_fits.py
echo "ok"

echo "fits_to_MJD.py ..."
fits_to_MJD.py
echo "ok"

echo "fits_to_jpeg.py ..."
fits_to_jpeg.py
echo "ok"

echo "crop.py ..."
crop.py
echo "ok"

echo "finish !!!!!!!!"
