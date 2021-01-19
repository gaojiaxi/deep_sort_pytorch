for filename in /home/gaojiaxi/deep_sort_pytorch/sample_video/*
do
  python yolov3_deepsort.py  $filename
done;
