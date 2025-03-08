from application import FILE_LOCATION, load_repo_data, get_metrics, get_metrics_ranges, get_min_max_metrics, reward_function
from algorithm import particle_swarm_optimization


data = load_repo_data(FILE_LOCATION)
metrics = get_metrics(data)
metrics_ranges = get_metrics_ranges(metrics)

best_pos, best_val = particle_swarm_optimization(dim=9, bounds=get_min_max_metrics(), reward_function=reward_function)
print("Best Position:", best_pos)
print("Best Value:", best_val)
