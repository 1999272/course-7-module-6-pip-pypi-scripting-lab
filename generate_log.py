import requests
from datetime import datetime

def generate_log(log_data):
    """
    Writes a log file with the given log entries.
    Returns the filename created.
    """
    
    if not isinstance(log_data, list):
        raise TypeError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename

def fetch_data():
    """Fetches sample data from an API."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    
    sample_logs = ["User logged in", "User updated profile", "Report exported"]
    filename = generate_log(sample_logs)
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))