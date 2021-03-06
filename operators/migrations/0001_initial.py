# Generated by Django 3.0.5 on 2020-04-02 00:42

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('side', models.CharField(choices=[('', "choose operator's side"), ('ATT', 'Attacker'), ('DEF', 'Defender')], default='', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('operator', models.ManyToManyField(related_name='weapons', to='operators.Operator')),
            ],
        ),
        migrations.CreateModel(
            name='Skin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('operator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='skins', to='operators.Operator')),
            ],
        ),
        migrations.CreateModel(
            name='Gadget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('operator', models.OneToOneField(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='gadget', to='operators.Operator')),
            ],
        ),
    ]
