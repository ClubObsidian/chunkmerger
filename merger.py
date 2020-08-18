import argparse
import nbt
import os
import shutil
from region import RegionFile

def is_valid_world_folder(check_folder):
    if os.path.exists(check_folder) == False or os.path.isfile(check_folder):
        return False
    
    region_folder = check_folder + '/region/'
    if os.path.exists(region_folder) and os.path.isfile(region_folder) == False:
        return True

    return False

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('-s', '--source', dest='source', required=True, help='Source world folder')
arg_parser.add_argument('-d', '--destination', '--dest', dest='dest', required=True, help='Destination world folder')

args = arg_parser.parse_args()

if not is_valid_world_folder(args.source):
    print(args.source + ' is not a valid world folder!')
    exit()

if not is_valid_world_folder(args.dest):
    print(args.dest + ' is not a valid world folder!')
    exit()

source_region_folder = args.source + "/region/"
dest_region_folder = args.dest + "/region/"

for file in os.listdir(source_region_folder):
	source_file_name = source_region_folder + file
	destination_file_name = dest_region_folder + file
	file_exists = os.path.isfile(destination_file_name)
	if not file_exists:
		shutil.copyfile(source_file_name, destination_file_name)
		print('Destination ' + destination_file_name + ' did not exist, copying...')
		continue

	source = RegionFile(source_file_name)
	destination = RegionFile(destination_file_name)

	for x in range(0, 32):
		for z in range(0, 32):
			source_chunk = source.get_chunk(x, z)
			if source_chunk is not None:
				destination_chunk = destination.get_chunk(x, z)
				if destination_chunk is None:
					print('Write ' + str(x) + ',' + str(z))
					destination.write_chunk(x, z, source_chunk)