import json

# sides should be
# "left", "right", "front", "behind", "top"
#  0      1       2           3       4
# this the side of the viewer's right not 
# the human mesh's right side
# z should be set between 2 and 18 for all sides besides top down view

# Create a dictionary with height and side fields

# top does not need a height and can be dumb number
data = {
    "camera_settings": [
        {
            "side": 4,
            "height": 10
        }
    ]
}

for side in range(0, 4):
    for height in range(2, 19):
        data["camera_settings"].append(
            {
                "side": side,
                "height": height
            }
        )

# Write to JSON file
with open('camera_settings.json', 'w') as f:
    json.dump(data, f, indent=4)

print("JSON file created successfully!")
