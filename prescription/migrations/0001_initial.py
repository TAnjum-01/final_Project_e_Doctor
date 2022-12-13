# Generated by Django 4.1.4 on 2022-12-12 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='prescription',
            fields=[
                ('pres_id', models.IntegerField(primary_key=True, serialize=False)),
                ('symptoms', models.TextField()),
                ('medicine', models.TextField()),
                ('d_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]