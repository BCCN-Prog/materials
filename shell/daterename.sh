#!/bin/bash
# Demo script for UNIX-Shell primer

function check_dupes () {
    # exit status is TRUE if a file with that name already exists
    if [ -e "$1" ];then
        return 0
    else
        return 1
    fi
}

# the loop goes recursively through all files and directories
# the -depth option ensures that all files within a
# directory are renamed before renaming the directory itself.
for ITEM in `find "$1" -depth`;do
    DIR=`dirname "$ITEM"`
    NAME=`basename "$ITEM"`
    
    ## -- START EXTENSION HANDLING -- ##
    # store extension
    # extension is eveything after the first dot 
    EXT=".${NAME#*.}"
    BASE="${NAME%%.*}"
    # if filename *starts* with a dot (e.g. .emacs)
    # then no extension!
    if ( [ -z "$BASE" ] && [ -n "$EXT" ] ); then
        BASE="$EXT"
        EXT=""
    fi
    # if filename has no extension 
    # second condition is too distinguish "name.name" from "name"
    if ( [ "$EXT" == ".$BASE" ] && [ "$NAME" == "$BASE" ] ); then
        EXT=""
    fi
    ## -- END EXTENSION HANDLING -- ##
    
    # get modification time in seconds since the epoch
    SEC=`stat --format="%Y" $ITEM`
    # format the time
    NEWBASE=`date --date="@$SEC" +%Y%m%d%H%M%S`
    ID=1
    NEWNAME="$DIR/$NEWBASE$EXT"
    # look for the next available filename
    while check_dupes "$NEWNAME"; do
        ID=$(( $ID + 1 ))
        NEWNAME="$DIR/$NEWBASE"_$ID"$EXT"
    done 
    # do the actual renaming 
    echo "Renaming \"$DIR/$NAME\" to \"$NEWNAME\""
    mv "$DIR/$NAME" $NEWNAME
done
