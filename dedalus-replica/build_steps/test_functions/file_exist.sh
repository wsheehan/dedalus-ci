FILE=$1

# Check that a file was created
if [ ! -f $FILE ]
then
    echo "error: file not found" 1>&2
    exit 1
fi