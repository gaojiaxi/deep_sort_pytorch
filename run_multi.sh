for filename in `find . -path '*Video*/*' -name "*.av" -type f`; do
    python yolov3_deepsort.py $filename
done
