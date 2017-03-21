FILE=$1
CHECK_FILE=$2

# Check that a file was created
if [ ! -f $FILE ]
then
    echo "error: file not found" 1>&2
    exit 1
fi

# Check if Files are binary match
if cmp -s $FILE $CHECK_FILE
then
    echo "files match"
else
    echo "error: resulting file not as expected" 1>&2
    exit 1
fi