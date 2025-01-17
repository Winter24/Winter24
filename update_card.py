import requests

# Replace this with your GitHub username
USERNAME = "winter24"

# GitHub API URL for user data
API_URL = f"https://api.github.com/users/{USERNAME}"
# GitHub API URL for contributions and repo stats (requires a custom backend or scraping GitHub contribution data)

# Fetch user data from GitHub
response = requests.get(API_URL)
if response.status_code != 200:
    print(f"Failed to fetch data: {response.status_code}")
    exit()

data = response.json()

# Extract necessary details
name = data.get("name", USERNAME)  # Fallback to username if name is not provided
public_repos = data.get("public_repos", 0)
followers = data.get("followers", 0)
following = data.get("following", 0)
created_at = data.get("created_at", "Unknown").split("T")[0]  # Parse date
contributions = "N/A"  # Placeholder (requires additional data fetching for contributions)

# SVG template
svg_template = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="700" height="200" viewBox="0 0 700 200">
  <style>
    * {{
      font-family: 'Segoe UI', Ubuntu, "Helvetica Neue", Sans-Serif;
    }}
  </style>
  <!-- Background -->
  <rect x="1" y="1" rx="5" ry="5" height="198" width="698" fill="#2b213a" stroke="#30363D" stroke-width="1"></rect>
  
  <!-- Title -->
  <text x="30" y="40" style="font-size: 22px; fill: #FF66C4;">
    GitHub Profile Summary: {name}
  </text>
  
  <!-- Contributions -->
  <text x="30" y="80" style="font-size: 16px; fill: #C9D1D9;">
    Contributions in the Last Year: {contributions}
  </text>
  
  <!-- Public Repos -->
  <text x="30" y="100" style="font-size: 16px; fill: #C9D1D9;">
    Public Repositories: {public_repos}
  </text>
  
  <!-- Followers -->
  <text x="30" y="120" style="font-size: 16px; fill: #C9D1D9;">
    Followers: {followers}
  </text>
  
  <!-- Following -->
  <text x="30" y="140" style="font-size: 16px; fill: #C9D1D9;">
    Following: {following}
  </text>
  
  <!-- Joined Date -->
  <text x="30" y="160" style="font-size: 16px; fill: #C9D1D9;">
    Joined GitHub: {created_at}
  </text>
</svg>
"""

# Write the SVG content to a file
output_file = "./cards/stats.svg"
with open(output_file, "w") as file:
    file.write(svg_template)

print(f"SVG file generated: {output_file}")
