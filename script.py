import json
import os
import shutil

path_json='/content/Uni3D/test_dataids.json'
source_folder='/content/Uni3D/uni3d_data/objaverse_lvis'
destination_base_folder = "/content/Uni3D/data/test_datasets/objaverse_lvis"


with open(path_json, 'r') as json_file:
    cloud_points = json.load(json_file)



# Ensure the destination folder exists
os.makedirs(destination_base_folder, exist_ok=True)

# Iterate through each 3D cloud point
for point in cloud_points:
    file_path = point[3]

    # Check if the file exists in the source folder
    source_file = source_folder+file_path
    if os.path.exists(source_file):
        # Construct the destination file path
        relative_path = os.path.dirname(file_path)
        destination_folder = destination_base_folder + relative_path
        os.makedirs(destination_folder, exist_ok=True)
        destination_file = destination_folder+"/"+os.path.basename(file_path)

        # Copy the file to the destination folder
        try:
            # Copy the file to the destination folder
            shutil.copy2(source_file, destination_file)
            print(f"File '{file_path}' copied to '{destination_file}'")
        except OSError as e:
            print(f"Error copying '{file_path}': {e}")
