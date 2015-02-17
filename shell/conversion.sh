echo 'Converting image to greyscale!'

TOT=$(ls | wc -l)

COUNT=0
for INPUT in $(ls); do
    OUTFILE="bw_${INPUT}"
    convert -colorspace Gray  -resize 1000x600 ${INPUT} ${OUTFILE}
    COUNT=$(( $COUNT + 1 ))
    echo "Converted $COUNT/$TOT"
done

echo "I converted $(ls bw_* | wc -l) images."
