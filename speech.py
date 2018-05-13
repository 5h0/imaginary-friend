# do this
# mkdir tmp_mbrola
# cd tmp_mbrola
# wget http://www.tcts.fpms.ac.be/synthesis/mbrola/bin/pclinux/mbr301h.zip
# unzip mbr301h.zip
# sudo cp mbrola-linux-i386 /usr/bin/mbrola
# wget http://www.tcts.fpms.ac.be/synthesis/mbrola/dba/en1/en1-980910.zip
# unzip en1-980910.zip
# sudo mkdir /usr/share/mbrola
# sudo cp en1/en1 /usr/share/mbrola/en1
# cd ..
# sudo rm -Rf ./tmp_mbrola/
# espeak -v mb-en1 -s 160 "Hello world"

# command: espeak -v mb-en1 -a 200 -s 150 "Hello world" -> super podesavanja za musko
# ili za zensko: espeak -v mb-en1+f4 -a 200 -s 130 "Hello world." -> za zensko

import os


def say(text):
    command = "espeak -v mb-en1+f4 -s 110 -a 200 '" + text + "'"
    os.system(command)
