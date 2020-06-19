# Generated by Django 3.0.3 on 2020-06-19 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0004_auto_20200619_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='admin',
            name='designation',
            field=models.CharField(choices=[('Senior Librarian', 'Senior Librarian'), ('Principal', 'Principal'), ('Security Head', 'Security Head'), ('HOD', 'HOD'), ('Canteen Owner', 'Canteen Owner'), ('Vice-Principal', 'Vice-Principal')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='complain',
            name='related_to',
            field=models.CharField(choices=[('Management', 'Management'), ('Security', 'Security'), ('Library', 'Library'), ('Faculty', 'Faculty'), ('Canteen', 'Canteen')], default='', max_length=20, verbose_name='Complain Related to'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='status',
            field=models.CharField(choices=[('Viewed', 'Viewed'), ('In Progress', 'In Progress'), ('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Solved', 'Solved')], default='Pending', max_length=20),
        ),
    ]
