import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm

def plot_cost_to_go(env, estimator, num_tiles=50):
    
    x = np.linspace(env.observation_space.low[0], env.observation_space.high[0], num=num_tiles)
    y = np.linspace(env.observation_space.low[1], env.observation_space.high[1], num=num_tiles)
    X, Y = np.meshgrid(x, y)
    Z = np.apply_along_axis(
        lambda obs: -np.max(estimator.predict(obs)), 2, np.stack([X, Y], axis=2))

    fig, ax = plt.subplots(figsize=(10, 5))
    p = ax.pcolor(X, Y, Z, cmap=cm.RdBu, vmin=0, vmax=200)

    ax.set_xlabel('Position')
    ax.set_ylabel('Velocity')
    ax.set_title("\"Cost To Go\" Function")
    fig.colorbar(p)
    plt.show()
    

def plot_learning_curves(stats, smoothing_window=10):
    
    plt.figure(figsize=(10,5))
    for algo, steps_per_episode in stats.items():
        steps_per_episode = pd.Series(steps_per_episode).rolling(
            smoothing_window).mean()  # smooth
        plt.plot(steps_per_episode, label=algo)
    plt.xlabel("Episode")
    plt.ylabel("Steps")
    plt.title("Steps per Episode")
    plt.legend()
    plt.show()
