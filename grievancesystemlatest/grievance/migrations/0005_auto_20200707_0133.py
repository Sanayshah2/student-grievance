# Generated by Django 3.0.6 on 2020-07-06 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0004_auto_20200706_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='designation',
            field=models.CharField(choices=[('Canteen Owner', 'Canteen Owner'), ('Principal', 'Principal'), ('Security Head', 'Security Head'), ('HOD', 'HOD'), ('Senior Librarian', 'Senior Librarian'), ('Vice-Principal', 'Vice-Principal')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='complain',
            name='related_to',
            field=models.CharField(choices=[('Canteen', 'Canteen'), ('Security', 'Security'), ('Faculty', 'Faculty'), ('Management', 'Management'), ('Library', 'Library')], default='', max_length=20, verbose_name='Complain Related to'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('In Progress', 'In Progress'), ('Viewed', 'Viewed'), ('Solved', 'Solved'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]
