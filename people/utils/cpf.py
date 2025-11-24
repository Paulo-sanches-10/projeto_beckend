def validar_cpf(cpf: str) -> bool:
    """
    Valida um CPF brasileiro simples (sem considerar todos os casos).
    """
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digito(cpf, peso):
        soma = sum(int(digito) * p for digito, p in zip(cpf, peso))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    d1 = calc_digito(cpf[:9], range(10, 1, -1))
    d2 = calc_digito(cpf[:10], range(11, 1, -1))

    return cpf[-2:] == d1 + d2