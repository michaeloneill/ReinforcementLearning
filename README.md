# RL Tutorial

## Overview

This tutorial focuses on two important and widely used RL algorithms, semi-gradient n-step Sarsa and Sarsa( λ ), as applied to the Mountain Car problem. These algorithms, aside from being useful, pull together a lot of the key concepts in RL and so provide a great way to learn about RL more generally. Value functions, policy iteration, on vs off-policy control, bootstrapping, tabular vs approximate solution methods, state featurization and eligibility traces can all be understood by studying these two algorithms.

## Running the notebook

1. Clone the Repo
2. Install docker
3. cd to ReinforcementLearning/docker/base and execute ./docker_run. This will build the ubuntu 16.04 base image (takes a while)
3. cd up one level to the docker folder and edit Line 5, changing /Users/michaeloneill/Documents/ReinforcementLearning to match the full path of your cloned version of the repo.
4. Execute ./docker_run from the docker folder. This will build and run an image derived from the base image and including more specific dependencies/permission configs required to run the notebook, dropping you into a container.
4. cd to /src/ReinforcementLearning from within the container and execute xvfb-run -s "-screen 0 1400x900x24" jupyter notebook --port=8888 --ip=0.0.0.0. This will open the notebook viewable at localhost:8888.
