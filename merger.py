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
arg_parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Displays verbose debugging messages')
arg_parser.set_defaults(verbose=False)

args = arg_parser.parse_args()
verbose_logs = args.verbose

if not is_valid_world_folder(args.source):
	print(args.source + ' is not a valid world folder!')
	exit()

if not is_valid_world_folder(args.dest):
	print(args.dest + ' is not a valid world folder!')
	exit()


source_region_folder = args.source + "/region/"
dest_region_folder = args.dest + "/region/"

failed_regions = []

for file in os.listdir(source_region_folder):
	source_file_name = source_region_folder + file
	destination_file_name = dest_region_folder + file
	file_exists = os.path.isfile(destination_file_name)
	if not file_exists:
		print('Destination "' + destination_file_name + '" did not exist, copying...')
		shutil.copyfile(source_file_name, destination_file_name)
		continue

	try:
		print('Destination "' + destination_file_name + '" exists, merging...')
		source = RegionFile(source_file_name)
		destination = RegionFile(destination_file_name)
		for x in range(0, 32):
			for z in range(0, 32):
				source_chunk = source.get_chunk(x, z)
				if source_chunk is not None:
					destination_chunk = destination.get_chunk(x, z)
					if destination_chunk is None:
						destination.write_chunk(x, z, source_chunk)
						if verbose_logs:
							print('Write ' + str(x) + ',' + str(z))
	except Exception as e:
		print("Couldn't merge to " + destination_file_name)
		print(e)
		print('')
		failed_regions.append(destination_file_name)

print('\nDone!\n')
print('Regions that failed to merge:')
print(*failed_regions, sep='\n')