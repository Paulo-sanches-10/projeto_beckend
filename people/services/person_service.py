from mongoengine.errors import NotUniqueError, ValidationError
from rest_framework.exceptions import APIException

def handle_mongo_errors(func):
    """
    Decorador para capturar erros do MongoEngine e convertê-los em respostas da API.
    - NotUniqueError → CPF duplicado
    - ValidationError → CPF inválido ou campos inválidos
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotUniqueError:
            raise APIException("CPF já existe")
        except ValidationError as e:
            raise APIException(str(e))
    return wrapper