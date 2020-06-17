# Generated by Django 3.0.6 on 2020-06-17 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0007_auto_20200617_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='designation',
            field=models.CharField(choices=[('Vice-Principal', 'Vice-Principal'), ('Principal', 'Principal'), ('HOD', 'HOD'), ('Senior Librarian', 'Senior Librarian'), ('Canteen Owner', 'Canteen Owner'), ('Security Head', 'Security Head')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='complain',
            name='related_to',
            field=models.CharField(choices=[('Faculty', 'Faculty'), ('Library', 'Library'), ('Canteen', 'Canteen'), ('Management', 'Management'), ('Security', 'Security')], default='', max_length=20, verbose_name='Complain Related to'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='status',
            field=models.CharField(choices=[('Viewed', 'Viewed'), ('In Progress', 'In Progress'), ('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Solved', 'Solved')], default='Pending', max_length=20),
        ),
    ]
