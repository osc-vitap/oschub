import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=264, unique=True)),
                ('eventCaption', models.TextField(default='', max_length=60)),
                ('eventDescription', models.TextField()),
                ('eventVenue', models.CharField(max_length=50)),
                ('eventDate', models.DateField()),
                ('eventStartTime', models.TimeField(default=datetime.time(16, 0))),
                ('eventEndTime', models.TimeField(default=datetime.time(18, 0))),
                ('eventRegEndDate', models.DateField()),
                ('eventRegEndTime', models.TimeField(default=datetime.time(16, 0))),
                ('eventSpeaker', models.TextField()),
                ('eventURL', models.URLField()),
                ('eventDocumentation', models.URLField(default='')),
                ('eventLogo', models.URLField(default='https://drive.google.com/uc?export=view&id=1hl6Xt2cnUMC5RUrmXH6w-kQD8fhuF3rC')),
            ],
        ),
        migrations.CreateModel(
            name='EventUserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=26)),
                ('studentReg', models.CharField(max_length=10)),
                ('studentEmail', models.EmailField(max_length=254)),
                ('studentRegistered', models.BooleanField(default=False)),
                ('studentCheckedIn', models.BooleanField(default=False)),
                ('eventName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventreg.Event')),
            ],
        ),
    ]
