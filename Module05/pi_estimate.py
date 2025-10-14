import numpy as np

def estimate_PI(num_points: int, seed=None):
    """ Aproximate value of PI using Monte Carlo simulation"""
    
    rng = np.random.default_rng(seed=seed)
    
    # Random sampling points uniformly distributed between [0, 1]
    x_pts =rng.random(num_points)
    y_pts =rng.random(num_points)
    
    # Compute distance to origin
    distance = np.sqrt((x_pts - 0)**2 + (y_pts - 0)**2)
    
    mask_inside = distance <= 1 # This provides a Boolean 1D array
    
    dist_inside = distance[mask_inside]
    
    count_inside = dist_inside.size
    
    ratio = count_inside / num_points
    
    pi_est = 4 * ratio
    return pi_est


if __name__ == "__main__":
    import matplotlib.pyplot as plt
#    num_points = 100
#    seed = None
#    pi_est = estimate_PI(num_points, seed=seed)
    
#    print(f'pi estimated as: {pi_est}, with {num_points} sampling points.')
    seed = None
    num_points_list = np.linspace(100, 100000, num=10, dtype='int')
    num_runs = 100
    npts_cases = len(num_points_list)
    
    pi_est_array = np.zeros((num_runs,  npts_cases))
    
    for i_run in range(num_runs):
        for j_npts in range( npts_cases):
            pi_est_array[i_run, j_npts] = estimate_PI(
                num_points=num_points_list[j_npts],
                seed=seed
            )

    pi_est_mean = np.mean(pi_est_array, axis=0)
    pi_est_std = np.std(pi_est_array, axis=0)
    
    fig, ax = plt.subplots()
    ax.plot(num_points_list, pi_est_mean, '-o', label='Estimated PI')
    ax.plot([num_points_list[0],num_points_list[-1]],
            [np.pi, np.pi], label='True PI')
    ax.legend()
    ax.fill_between(num_points_list, pi_est_mean - pi_est_std, 
                    pi_est_mean + pi_est_std, alpha=0.2)
    ax.set_xlabel('Number of points [-]')
    ax.set_ylabel('Value [-]')  
    ax.set_title('Estimate PI with Monte Carlo simulation')
    plt.grid()
    plt.tight_layout()
    fig.savefig('estimation_of_pi.png', dpi=300)
    plt.show()  