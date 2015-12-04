# arr = [2,1,3,5]
# for i in range(len(arr)-1):
# 	if arr[i] > arr[i+1]:
# 		arr[i],arr[i+1] = arr[i+1],arr[i]
# print arr

# arr = [2,1,3,5]
# print arr
# m = 0
# for j in range(len(arr)-1):
# 	for i in range(len(arr)-1-j):
# 		m = m+1
# 		if arr[i]>arr[i+1]:
# 			arr[i],arr[i+1] =  arr[i+1],arr[i]
# print arr
# print m

# arr = [1,2,3]# print arr
# arr [-1:] = [arr[len(arr)-1],4]
# print arr

# arr = [1,2,3,4,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
# print arr.index(4)+1
# print arr.index(4,arr.index(4)+1)

# todo_list = []

# while True:
# 	action = raw_input('please input add or do:')
# 	if action == 'add':
# 		work = raw_input('input you want todo')
# 		todo_list.append(work)
# 	elif action todo_list[0]
# 		print todo_list[0]
# 		del todo_list[0]
# 		if len(todo_list) == 0:
			# print 'end'
# 			break
# 
# 

# arr = [1,2,3,4,5]
# arr.append(arr.pop())
# print arr

# arr = ['a','b','c']
# arr.remove('a')
# print arr

# num_list = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
# unqiue_dict = {}
# for i in num_list:
# 	unqiue_dict[i]=1
# for key in unqiue_dict:
# 	print key
# for i in num_list:
# 	if i not in unqiue_list:
# 		unqiue_list.append(i)
# 		
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
unqiue_list = []

for num in arr1:
	if num in arr2 and num not in unqiue_list:
		unqiue_list.append(num)
print unqiue_list
