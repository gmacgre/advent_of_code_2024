#/bin/bash
clear
# Make Command - ./driver.sh make <number>
if [ "$1" = "make" ]
then
    echo "Making Workspace for $2..."
    mkdir "$2"
    cp base.py "$2/$2-1.py"
    cp base.py "$2/$2-2.py"
    touch "$2/test-input.txt"
    touch "$2/input.txt"
# Transfer Command - ./driver.sh transfer <number>
elif [ "$1" = "transfer" ]
then
    echo "Setting up $2 part 2..."
    cp "$2/$2-1.py" "$2/$2-2.py"

# Test Command - ./driver.sh <day number> <1 or 2> <input (test or "")>
else
    if [ "$3" = "test" ]
    then
        echo "Running python $1/$1-$2.py on test input...";
        python "$1/$1-$2.py" < "$1/test-input.txt"
    else
        echo "Running python $1/$1-$2.py on full input...";
        python "$1/$1-$2.py" < "$1/input.txt"
    fi
fi