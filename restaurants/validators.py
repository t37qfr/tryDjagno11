from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not valid number',
             params={'value':value},
            )

def validate_email(value):
    email=value
    if '.edu' in email:
        raise ValidationError('We do not accept edu emails')


CATEGORIES=['Mexican', 'Asien', 'Sweet', 'American']

def validate_category(value):
    if not value in CATEGORIES:
        raise ValidationError(f'{value} not a valid category')