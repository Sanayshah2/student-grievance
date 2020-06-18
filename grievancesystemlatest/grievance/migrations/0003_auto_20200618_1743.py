# Generated by Django 3.0.3 on 2020-06-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0002_auto_20200617_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='transfer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='admin',
            name='designation',
            field=models.CharField(choices=[('HOD', 'HOD'), ('Vice-Principal', 'Vice-Principal'), ('Senior Librarian', 'Senior Librarian'), ('Principal', 'Principal'), ('Canteen Owner', 'Canteen Owner'), ('Security Head', 'Security Head')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='complain',
            name='related_to',
            field=models.CharField(choices=[('Canteen', 'Canteen'), ('Management', 'Management'), ('Library', 'Library'), ('Security', 'Security'), ('Faculty', 'Faculty')], default='', max_length=20, verbose_name='Complain Related to'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='status',
            field=models.CharField(choices=[('Viewed', 'Viewed'), ('Rejected', 'Rejected'), ('Solved', 'Solved'), ('In Progress', 'In Progress'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]
