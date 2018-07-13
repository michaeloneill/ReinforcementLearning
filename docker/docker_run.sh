docker build -t gym .

# nvidia-docker run -it \
#       -v /nfs_mount:/nfs_mount \
#       -v /home/michael/Documents/Kheiron:/src \
#       --name=michael_container \
#       michael

docker run -it \
       -p 8888:8888 \
       -v /Users/michaeloneill/Documents/RL:/src/RL \
       --env="DISPLAY" \
       --env="QT_X11_NO_MITSHM=1" \
       --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
       --name gym_container \
       gym
