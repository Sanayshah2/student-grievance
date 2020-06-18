# Generated by Django 3.0.3 on 2020-06-18 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='designation',
            field=models.CharField(choices=[('Canteen Owner', 'Canteen Owner'), ('Security Head', 'Security Head'), ('Principal', 'Principal'), ('HOD', 'HOD'), ('Vice-Principal', 'Vice-Principal'), ('Senior Librarian', 'Senior Librarian')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='complain',
            name='related_to',
            field=models.CharField(choices=[('Management', 'Management'), ('Security', 'Security'), ('Canteen', 'Canteen'), ('Faculty', 'Faculty'), ('Library', 'Library')], default='', max_length=20, verbose_name='Complain Related to'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='status',
            field=models.CharField(choices=[('In Progress', 'In Progress'), ('Viewed', 'Viewed'), ('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Solved', 'Solved')], default='Pending', max_length=20),
        ),
    ]
