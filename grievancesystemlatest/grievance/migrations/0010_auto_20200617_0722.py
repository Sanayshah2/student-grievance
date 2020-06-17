# Generated by Django 3.0.6 on 2020-06-17 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0009_auto_20200617_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='designation',
            field=models.CharField(choices=[('Security Head', 'Security Head'), ('Canteen Owner', 'Canteen Owner'), ('HOD', 'HOD'), ('Senior Librarian', 'Senior Librarian'), ('Vice-Principal', 'Vice-Principal'), ('Principal', 'Principal')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='complain',
            name='related_to',
            field=models.CharField(choices=[('Management', 'Management'), ('Canteen', 'Canteen'), ('Security', 'Security'), ('Library', 'Library'), ('Faculty', 'Faculty')], default='', max_length=20, verbose_name='Complain Related to'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('In Progress', 'In Progress'), ('Solved', 'Solved'), ('Viewed', 'Viewed')], default='Pending', max_length=20),
        ),
    ]
