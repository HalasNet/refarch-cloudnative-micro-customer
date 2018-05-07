from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant("admin", "pass", url = "http://cloudant-service:80", connect=True)
client.connect()
databaseName = "customers"

database = client.create_database(databaseName)

# Create a JSON document that represents
# all the data in the row.
jsonDocument = {
  "username": "foo",
  "password": "bar",
  "email": "foo@address.com",
  "firstName": "foo",
  "lastName": "fooLast",
  "imageUrl": "image"
}

jsonDocument2 = {
  "username": "user",
  "password": "pass",
  "email": "user@address.com",
  "firstName": "user",
  "lastName": "userLast",
  "imageUrl": "image"
}

session = client.session()

database.create_document(jsonDocument)
database.create_document(jsonDocument2)

client.disconnect()