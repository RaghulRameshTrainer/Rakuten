import re
"""
match
search
findall
sub
split
compile-finditer
"""

#matches=re.match('pet:cat',line)
#matches=re.match('pet:dog',line)
#matches=re.match('pet:...',line)
#matches=re.match('pet:.{3}',line)
#matches=re.match('pet:\w\w\w',line)
#matches=re.match('pet:\w{3}',line)
#matches=re.match('Pet:Cat',line,re.I)
#print(matches.group())

#matches=re.search("pet:cat",line)
#matches=re.search("pet:dog",line)
#matches=re.search("pet:...",line)
#print(matches.group())

#matches=re.findall('pet:...',line)
# matches=re.findall('PET:...',line,re.I)
# print(matches)

# string replace and translate
#line="pet:cat I love cat pet:dog i love dog"

#print(re.sub('love','like',line))
#print(re.split(" ",line))

mystring="""
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

#Special Characters
~!@#$%^&*()_+=-`

https://www.rakuten.com
http://www.rakuten.com
https://rakuten.com
https://www.rakuten.co.in

561-332-1343
323 432 4324
654_334_1122
231.121.1421

raghul.ramesh@gmail.com
ramesh_ramesh@gmail.com
ramesh@outlook.com
raghulramesh@yahoo.co.in

Ha HaHa
u = "https://network.mobile.rakuten.co.jp/faq/detail/10000085/"

+91-9876586199
9876586199
98765861999
987658619
8876586199
7876586199
6876586199
5876586199
4876586199
3876586199
2876586199
1876586199

"""
pattern=re.compile(r"(\+91\-)?\b[5-9]\d{9}\b")
#pattern=re.compile('u = "\w+://(\w+\.\w+\.\w+\.\w{2}\.\w{2})/((\w+)/(\w+)/(\d+))/')
#pattern=re.compile(r"\bHa\b")
#pattern=re.compile("(\w+?\.?\w+)@(\w+)\.com?(\.in)?")
#pattern=re.compile("(\w+\.)?\w+@\w+\.com?(\.in)?")
#pattern=re.compile("(\d{3})[\-\s_](\d{3})[\-\s_](\d{4})")
#pattern=re.compile("https?://(www\.)?rakuten\.com?(\.in)?")
#pattern=re.compile(".")
matches=pattern.finditer(mystring)
for match in matches:
    print(match.group())


