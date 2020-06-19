# Generated by Django 3.0.3 on 2020-06-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='designation',
            field=models.CharField(choices=[('Vice-Principal', 'Vice-Principal'), ('Principal', 'Principal'), ('HOD', 'HOD'), ('Canteen Owner', 'Canteen Owner'), ('Security Head', 'Security Head'), ('Senior Librarian', 'Senior Librarian')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='complain',
            name='related_to',
            field=models.CharField(choices=[('Library', 'Library'), ('Faculty', 'Faculty'), ('Management', 'Management'), ('Canteen', 'Canteen'), ('Security', 'Security')], default='', max_length=20, verbose_name='Complain Related to'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='status',
            field=models.CharField(choices=[('In Progress', 'In Progress'), ('Viewed', 'Viewed'), ('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Solved', 'Solved')], default='Pending', max_length=20),
        ),
    ]
