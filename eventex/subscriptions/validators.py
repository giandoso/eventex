from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('Cpf deve conter apenas numeros', 'digits')
    if len(value) != 11:
        raise ValidationError('Cpf deve conter 11 numeros', 'lenght')
