#!/usr/bin/env python3

import click
import requests
import threading

def Handler(start, end, url, filename):
	# starting, end of the file	
	headers = {'Range': 'bytes=%d-%d' % (start, end)}

	# requets the chunk
	r = requests.get(url, headers = headers, stream = True)

	with open(filename, "r+b") as fp:
		fp.seek(start)
		fp.write(r.content)

@click.command(help='Downloads specified file form a given url')
@click.option('--num_threads', default = 5, help='Number of threads')
@click.option('--name', type = click.Path(), help='Name of file for saving content')
@click.argument('url', type = click.Path())
@click.pass_context
	
def download_file(ctx, url, name, num_threads):
	r = requests.head(url)
	
	if name:
		file_name = name
	else:
		file_name = url.splt('/')[-1]
	
	try:
		file_size = int(r.headers['content-length'])
	except:
		print("Invalid url")

	part = (int) (file_size / num_threads)

	fp = open(file_name, "wb")
	#fp.write('\0' * file_size)
	fp.close()	

	print("File size : %d" % part)
	for i in range(num_threads):
		start = part * i
	
		print("Start pos: %f" % start )

		end = start + part

		t = threading.Thread(target = Handler,
			kwargs = {'start' : start, 'end' : end, 'url' : url, 'filename' : file_name})

		t.setDaemon(True)
		t.start()

	main_thread = threading.current_thread()
	
	for t in threading.enumerate():
		if t is main_thread:
			continue
		t.join()

if __name__ == '__main__':
	download_file()
	
			
