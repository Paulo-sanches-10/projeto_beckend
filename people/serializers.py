from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "name", "birth_date", "cpf"]

    def validate_cpf(self, value):
        # remove pontos e traço
        cpf = value.replace(".", "").replace("-", "")
        if len(cpf) != 11 or not cpf.isdigit():
            raise serializers.ValidationError("CPF deve ter 11 dígitos numéricos.")

        # valida dígitos verificadores
        def calc_digit(cpf, length):
            soma = sum(int(cpf[i]) * (length + 1 - i) for i in range(length))
            resto = soma % 11
            return "0" if resto < 2 else str(11 - resto)

        if calc_digit(cpf, 9) != cpf[9] or calc_digit(cpf, 10) != cpf[10]:
            raise serializers.ValidationError("CPF inválido.")

        return cpf  # salva apenas os números no banco