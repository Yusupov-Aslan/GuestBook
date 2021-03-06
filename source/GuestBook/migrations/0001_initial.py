# Generated by Django 4.0 on 2022-01-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя автора')),
                ('author_mail', models.EmailField(max_length=100, verbose_name='Почта автора')),
                ('text_notes', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Текст записи')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=20, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('editing_time', models.DateTimeField(auto_now=True, verbose_name='Время редактирования')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
                'db_table': 'guest',
            },
        ),
    ]
