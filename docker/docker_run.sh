nvidia-docker build -t rl_tutorials .

# nvidia-docker run -it \
#       -v /nfs_mount:/nfs_mount \
#       -v /home/michael/Documents/Kheiron:/src \
#       --name=michael_container \
#       michael

nvidia-docker run -it \
	      -p 8888:8888 \
	      -v /nfs_mount:/nfs_mount \
	      -v /home/michael/Documents/Kheiron/malignancy_segmentation:/src/malignancy_segmentation \
	      --env="DISPLAY" \
	      --env="QT_X11_NO_MITSHM=1" \
	      --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
	      --name rl_tutorials_container_ipython \
	      michael
