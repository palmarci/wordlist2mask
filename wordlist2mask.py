import sys
from collections import Counter

if (len(sys.argv) < 2):
	print("\npython wordlist to hashcat mask converter and sorter\n")
	print("Usage: 	python wordlist2mask.py [wordlist file]")
	print("Example: python wordlist2mask.py ntlm-hashes.txt\n")
	sys.exit(1)

with open(str(sys.argv[1])) as f:
    content = f.readlines()

content = [x.strip() for x in content]
masks = set()

for x in content:
	#x = x.decode('utf-8', 'ignore')
	try:
		word = ""
		for c in x:
			code = ord(c)
			if 97 <= code <= 122:
				word = word + "?l"
			elif 65 <= code <= 90:
				word = word + "?u"
			elif 48 <= code < 57:
				word = word + "?d"
			else:
				word = word + "?s"
		masks.add(word)
	except Exception:
		pass



masks = sorted(masks, key=Counter(masks).get, reverse=True)
masks = list(masks)

for i in masks:
	print(i)
