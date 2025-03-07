import json
import os


FILE_LOCATION = "data/data.json"


def load_repo_data(file_path):
  """
  Load repository data from the given JSON file.
  """
  try:
    with open(file_path, 'r', encoding='utf-8') as f:
      return json.load(f)
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found")
    return []
  except json.JSONDecodeError:
    print(f"Error: File '{file_path}' contains invalid JSON")
    return

def get_metrics(data):
  """
  Get repository data from the JSON file.
  """
  return [{
    "unique_contributors_count": repo_data["unique_contributors_count"],
    "median_contributions_per_contributor": repo_data["median_contributions_per_contributor"],
    "mean_contributions_per_contributor": repo_data["mean_contributions_per_contributor"],
    "average_weekly_commits": repo_data["average_weekly_commits"],
    "commit_consistency": repo_data["commit_consistency"],
  } for repo_data in data]

def get_metrics_ranges(data):
  """
  Get the range of repository data.
  """
  metrics = get_metrics(data)
  return {
    "unique_contributors_count": (min([repo["unique_contributors_count"] for repo in metrics]), max([repo["unique_contributors_count"] for repo in metrics])),
    "median_contributions_per_contributor": (min([repo["median_contributions_per_contributor"] for repo in metrics]), max([repo["median_contributions_per_contributor"] for repo in metrics])),
    "mean_contributions_per_contributor": (min([repo["mean_contributions_per_contributor"] for repo in metrics]), max([repo["mean_contributions_per_contributor"] for repo in metrics])),
    "average_weekly_commits": (min([repo["average_weekly_commits"] for repo in metrics]), max([repo["average_weekly_commits"] for repo in metrics])),
    "commit_consistency": (min([repo["commit_consistency"] for repo in metrics]), max([repo["commit_consistency"] for repo in metrics])),
  }
