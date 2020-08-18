import argparse
import nbt
import os
import shutil
from region import RegionFile

def isValidWorldFolder(checkFolder):
    if os.path.exists(checkFolder) == False or os.path.isfile(checkFolder):
        return False
    
    regionFolder = checkFolder + '/region/'
    if os.path.exists(regionFolder) and os.path.isfile(regionFolder) == False:
        return True

    return False

aParser = argparse.ArgumentParser()

aParser.add_argument('-s', '--source', required=True, help='Source world folder')
aParser.add_argument('-d', '--dest', required=True, help='Destination world folder')

args = aParser.parse_args()

if isValidWorldFolder(args.source):
    print(args.source + ' is not a valid world folder!')
    exit()

if isValidWorldFolder(args.dest):
    print(args.dest + ' is not a valid world folder!')
    exit()

sourceRegionFolder = args.source + "/region/"
destRegionFolder = args.dest + "/region/"

for file in os.listdir(sourceRegionFolder):
	source_file_name = sourceRegionFolder + file
	destination_file_name = destRegionFolder + file
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