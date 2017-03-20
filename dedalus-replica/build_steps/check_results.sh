FILE=$1

# Check that a file was created
if [ ! -f $FILE ]
then
    echo "error: file not found" 1>&2
    exit 1
fi

# Check if Files are binary match
if [ ! cmp assets/1d_kdv_burgers.png $FILE ]
then
    echo "error: resulting file not as expected" 1>&2
    exit 1
fi