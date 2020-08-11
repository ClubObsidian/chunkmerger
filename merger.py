import nbt
import os
import os.path
import shutil
from region import RegionFile

for file in os.listdir('source'):
	source_file_name = 'source/' + file
	destination_file_name = 'destination/' + file
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
					print("Write " + str(x) + "," + str(z))
					destination.write_chunk(x, z, source_chunk)