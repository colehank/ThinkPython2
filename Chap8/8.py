#count(str[,start[,end]])返回str在string中出现的次数，如果start或者end指定则返回指定范围内str出现的次数

word = 'banana'
count = word.count('a') 
print(count)



#8.3
def is_palindrome(word):
	new_word = word[::-1]
	if new_word == word:
		return True
	else:
		return False
 
print(is_palindrome('asa'))

