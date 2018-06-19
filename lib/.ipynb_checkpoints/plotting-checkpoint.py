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


def run_grid_search(algorithm, env, alphas, bootstrappings, episodes=100, runs=5,
                    truncate_length=400, trace=False):
    
    bootstrapping_type = 'lambda' if trace else 'n-step'
    lengths = np.zeros((len(bootstrappings), len(alphas)))
    for run in range(runs):
        for b_idx, bootstrapping in enumerate(bootstrappings):
            for a_idx, alpha in enumerate(alphas):
                estimator = Estimator(alpha=alpha, trace=trace)
                for episode in range(episodes):
                    print(
                        '\r run: {}, {}: {}, alpha: {}, episode: {}'.format(
                            run, bootstrapping_type, 
                            bootstrapping, alpha, episode), end="")
                    episode_length, _ = algorithm(bootstrapping, env=env, estimator=estimator)
                    lengths[b_idx, a_idx] += episode_length
    
    # average over independent runs and episodes
    lengths /= runs * episodes
    
    # truncate high step values for better display
    lengths[lengths > truncate_length] = truncate_length

    plt.figure()
    for b_idx in range(len(bootstrappings)):
        plt.plot(alphas, lengths[b_idx, :], 
            label='{}: {}'.format(boostrapping_type, bootstrappings[b_idx]))
    plt.xlabel('alpha * number of tilings(8)')
    plt.ylabel('Average steps per episode')
    plt.ylim(140, truncate_length - 100)
    plt.legend()