from django.contrib import admin

# O modelo Person é do MongoEngine (Document), não pode ser registrado no Admin.
# O Admin continua funcionando para User, Group e outros modelos Django (SQLite).