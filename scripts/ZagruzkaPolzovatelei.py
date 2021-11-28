import csv
from urllib.request import Request

from django.contrib.auth.models import User
from rest_framework.response import Response

from apps.core.models import MedOrganizacia, Polzovateli
from centr.settings import BASE_DIR


def script_zagruzka_polzovatelei(request):
    """
    скрипт для удаление всех пользователей и создания с нуля
    шапка csv: ЛПУ,Пользователь,Логин,Пароль
    пользователи могут быть не удаленны из-за защиты полей
    """
    Polzovateli.objects.all().delete()
    User.objects.all().delete()

    with open(f'{BASE_DIR}/scripts/users.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            print(row['Логин'], '---', row['ЛПУ'].replace('"',""))
            user = User.objects.create_user(
                username=row['Логин'],
                password = row['Пароль'],
                is_staff = True
            )


            med_organiizaciya = MedOrganizacia.objects.get(nazvanie=row['ЛПУ'].replace('"',""))

            if row['Пользователь'] == 'Консультант':
                rol = 4
            elif row['Пользователь'] == 'Оператор':
                rol = 2
            elif row['Пользователь'] == 'Оператор РД':
                rol = 2

            Polzovateli.objects.create(
                user=user,
                med_organiizaciya=med_organiizaciya,
                rol=rol
            ).save()

    return Response('ок')