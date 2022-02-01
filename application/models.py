from django.db import models
from django.core.validators import RegexValidator

import re
from django.core.exceptions import ValidationError

# def valid_number(number):
#     reg = re.compile('^\+?\d{9,15}$')
#     if not reg.match(number):
#         raise ValidationError(u'%s hashtag doesnot comply' % number)


class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер телефона необходимо ввести в формате: '+999999999'. Допускается до 15 цифр.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'

    def __str__(self):
        return self.name

