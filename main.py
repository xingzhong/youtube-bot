import glob
from uploadVideo import get_authenticated_service, initialize_upload

if __name__ == '__main__':
	for fn in glob.glob('./video/*.flv'):
		args = {}
		args['file'] = fn
		args['title'] = fn.split('/')[-1][:-4]
		if not os.path.exists(args.file):
			exit("Please specify a valid file using the --file= parameter.")
		youtube = get_authenticated_service(args)
		try:
			initialize_upload(youtube, args)
		except HttpError, e:
			print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)