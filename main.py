import glob
import os
from uploadVideo import get_authenticated_service, initialize_upload
from oauth2client.tools import argparser, run_flow
from apiclient.errors import HttpError

if __name__ == '__main__':
	for fn in glob.glob('./video/*.flv'):
		argparser.add_argument("--file", default=fn)
		argparser.add_argument("--title", default=fn.split('/')[-1][:-4])
		args = argparser.parse_args()
		if not os.path.exists(args.file):
			exit("Please specify a valid file using the --file= parameter.")
		break
		youtube = get_authenticated_service(args)
		try:
			initialize_upload(youtube, args)
			os.remove(fn)
		except HttpError, e:
			print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)