
def countCharacters( words, chars):
	"""
	:type words: List[str]
	:type chars: str
	:rtype: int
	"""
	counter = 0
	compare = None
	for word in words:
		compare = chars
		isvalid = True
		for ch in word:
			if ch in compare:
				compare = compare.replace(ch,"",1)
			else:
				isvalid = False
				break
		if isvalid:
			counter+= len(word)
	return counter


print(countCharacters(["ca","tt","hat","tree"], "atach"))