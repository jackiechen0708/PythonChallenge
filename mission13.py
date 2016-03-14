import xmlrpclib

server=xmlrpclib.Server("http://www.pythonchallenge.com/pc/phonebook.php")
# print server.phone("Bert")
#ie explore can open the file evil4.jpg.....................
print server.phone('Bert')
print server.phone('leopold')