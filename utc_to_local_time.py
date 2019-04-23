from datetime import datetime
from dateutil import tz

def get_time():

	utc = tz.gettz('UTC')
	local = tz.tzlocal()

	data = datetime.utcnow()
	data = data.replace(tzinfo = utc)
	data = data.astimezone(local).isoformat()
	date, time = data.split('T')
	local_time, _ = time.split('.')

	return local_time


if __name__ == '__main__':

	time = get_time()

	print("\nYour local time is: {}\n".format(time))
