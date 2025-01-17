import requests
from bs4 import BeautifulSoup

# Replace this with your GitHub username
USERNAME = "winter24"

# URL for the GitHub contributions page
CONTRIBUTIONS_URL = f"https://github.com/users/{USERNAME}/contributions"

# Fetch contributions data from the GitHub contributions page
response = requests.get(CONTRIBUTIONS_URL)
if response.status_code != 200:
    print(f"Failed to fetch data: {response.status_code}")
    exit()

# Parse the contributions data using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
contributions = []

# Extract daily contributions from the SVG
for rect in soup.find_all("rect", {"data-count": True}):
    contributions.append(int(rect["data-count"]))

# Check if contributions data is empty
if not contributions:
    print("No contributions data found!")
    contributions = [0] * 365  # Fallback for an empty graph (365 days of zeros)

# Normalize the data for the graph
max_contributions = max(contributions)
if max_contributions == 0:
    normalized = [0] * len(contributions)  # Prevent division by zero
else:
    normalized = [(y / max_contributions) * 100 for y in contributions]  # Scale to fit height

# Function to generate SVG path for the graph
def generate_graph_svg(data):
    if not data:
        return ""
    path_d = f"M0,{100 - data[0]:.2f}"  # Start point
    for i, y in enumerate(data[1:], 1):
        x = i * (700 / len(data))  # Compute x-coordinate
        path_d += f" L{x:.2f},{100 - y:.2f}"  # Line to next point
    return f'<path d="{path_d}" fill="none" stroke="#F8D866" stroke-width="2" />'

# Generate the SVG path for the graph
graph_svg = generate_graph_svg(normalized)

# Generate the full SVG file
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
    GitHub Profile Summary: {USERNAME}
  </text>
  
  <!-- Contributions -->
  <text x="30" y="80" style="font-size: 16px; fill: #C9D1D9;">
    Contributions in the Last Year: {sum(contributions)}
  </text>
  
  <!-- Graph -->
  {graph_svg}
</svg>
"""

# Write the SVG content to a file
output_file = "./cards/stats.svg"
with open(output_file, "w") as file:
    file.write(svg_template)

print(f"SVG file generated: {output_file}")
