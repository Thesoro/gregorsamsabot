import xmltodict

print "pre"
x = open('wiktdict.xml')
print "1"
data = x.readline()
print "2"
print data
for i in range(0,10000):
  d = x.readline()

for i in range(0,1000):
  print x.readline()
# d = data
# # d = xmltodict.parse(data)
# print "post"
# print d.iteritems()[0]
