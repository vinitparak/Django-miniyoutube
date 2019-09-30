# Generated by Django 2.2.4 on 2019-09-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vibg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('category', models.CharField(choices=[('SD', '480p'), ('HD', '720p'), ('FHD', '1080')], max_length=3)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('video', models.FileField(upload_to='video/')),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
