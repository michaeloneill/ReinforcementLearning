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
        lambda x, y: -np.max(estimator.predict([x, y])), 2, np.stack([X, Y], axis=2))

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
        plt.figure(figsize=(10,5))
        steps_per_episode = pd.Series(steps_per_episode).rolling(
            smoothing_window).mean()  # smooth
        plt.plot(steps_per_episode, label=algo)
    plt.xlabel("Episode")
    plt.ylabel("Steps")
    plt.title("Steps per Episode")
    plt.legend()
    plt.show()


def run_grid_search(algorithm, estimator, alphas, bootstrappings, episodes=100, runs=5,
                    truncate_steps=400, bootstrapping_descriptor='bootstrapping'):
    
    estimator.reset()
    steps = np.zeros((len(bootstrappings), len(alphas)))
    for run in range(0, runs):
        for b_idx, bootstrapping in enumerate(bootstrappings):
            for a_idx, alpha in enumerate(alphas):
                for episode in range(episodes):
                    print(
                        '\r run: {}, {}: {}, alpha: {}, episode: {}'.format(
                            run, bootstrapping_descriptor, 
                            bootstrapping, alpha, episode), end="")
                    n_steps, _ = algorithm(bootstrapping, env=env, estimator=estimator)
                    steps[lmbdaIndex, alphaIndex] += n_steps
    
    # average over independent runs and episodes
    steps /= runs * episodes
    
    # truncate high step values for better display
    steps[steps > truncate_steps] = truncate_steps

    plt.figure()
    for b_idx in range(len(bootstrappings):
        plt.plot(alphas, steps[b_idx, :], 
            label='{}: {}'.format(boostrapping_destriptor, bootstrappings[b_idx]))
    plt.xlabel('alpha * number of tilings(8)')
    plt.ylabel('Average steps per episode')
    plt.ylim(140, truncate_steps - 100)
    plt.legend()