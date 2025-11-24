from rest_framework.test import APITestCase
from rest_framework import status

class PersonAPITest(APITestCase):
    def test_create_valid_person(self):
        data = {
            "first_name": "Joao",
            "last_name": "Silva",
            "birth_date": "1990-05-10",
            "cpf": "52998224725"
        }
        response = self.client.post("/api/people/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_cpf(self):
        data = {
            "first_name": "Maria",
            "last_name": "Souza",
            "birth_date": "1985-03-20",
            "cpf": "11111111111"
        }
        response = self.client.post("/api/people/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)