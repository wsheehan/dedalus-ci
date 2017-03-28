# Get dedalus paths
source /home/dedalus/dedalus/bin/activate

for dir in simulations/*
do
    echo $dir
    bash $dir/test.sh
done