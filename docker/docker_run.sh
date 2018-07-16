docker build -t gym .

docker run -it \
       -p 8888:8888 \
       -v /Users/michaeloneill/Documents/ReinforcementLearning:/src/ReinforcementLearning \
       --env="DISPLAY" \
       --env="QT_X11_NO_MITSHM=1" \
       --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
       --name gym_container \
       gym
