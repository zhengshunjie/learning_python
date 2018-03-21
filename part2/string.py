mystr='xxxSPAMxxx'
print(mystr.find('SPAM'))
mystr='xxaaxxaa'
print(mystr.replace('aa','SPAM'))

mystr='xxxSPAMxxx'
print('SPAM' in mystr)

mystr='\t Ni\n'
print(mystr.strip())

print(mystr.rstrip())

mystr='SHRUBBERY'
print(mystr.lower())

print(mystr.isalpha())

print(mystr.isdigit())


mystr='aaa,bbb,ccc'
mystr.split(',')
print(mystr.split(','))

mystr='a b\nc\nd'
print(mystr.split())

delim='NI'

print(delim.join(['aaa','bbb','ccc']))