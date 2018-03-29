#!/bin/bash

STRING="Hello World"
echo -e " \n "
echo $STRING

echo -e "\n Hi, please type the input: \c "
read  word
echo "The word you entered is: $word"
echo -e " \n \n \t "
echo 'Creating New  file and writing : Hello world ' >First .txt

echo -e "Creating Second file and writing peom--> ~~>  \n \t  "
exec 3<> poem.txt

   
    echo "Roses are red" >&3
    echo "Violets are blue" >&3
    echo "Poems are cute" >&3
    echo "And so are you" >&3

echo -e " \n \t \t The Poem File Contents Is : \n \t \t  "
cat poem.txt
echo -e " \n \t \t End Reading File \n \t \t  "
exec 3>&-


