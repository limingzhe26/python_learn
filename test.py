arr = []
while True:
	action = raw_input ('input you action')
	if action == 'add':
		detail = raw_input('input')
		arr.append(detail)
		print arr
	elif action  == 'do':
		if len(arr) == 0:
			break
		print arr.pop(0)



