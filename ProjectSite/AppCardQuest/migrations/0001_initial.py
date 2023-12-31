# Generated by Django 5.0 on 2023-12-05 15:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('rarity', models.CharField(blank=True, choices=[('Common', 'Common'), ('Uncommon', 'Uncommon'), ('Rare', 'Rare')], max_length=50, null=True)),
                ('hp', models.IntegerField(blank=True, null=True)),
                ('card_type', models.CharField(blank=True, choices=[('Fire', 'Fire'), ('Water', 'Water'), ('Grass', 'Grass'), ('Electric', 'Electric'), ('Psychic', 'Psychic'), ('Ice', 'Ice'), ('Dragon', 'Dragon'), ('Dark', 'Dark'), ('Normal', 'Normal'), ('Fighting', 'Fighting'), ('Flying', 'Flying'), ('Poison', 'Poison'), ('Ground', 'Ground'), ('Rock', 'Rock'), ('Bug', 'Bug'), ('Ghost', 'Ghost'), ('Steel', 'Steel'), ('Fairy', 'Fairy')], max_length=50, null=True)),
                ('attack', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('weakness', models.CharField(max_length=100)),
                ('card_number', models.IntegerField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('evolution_stage', models.CharField(blank=True, max_length=50, null=True)),
                ('abilities', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('collection_date', models.DateTimeField(blank=True, null=True)),
                ('card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppCardQuest.pokemoncard')),
                ('trainers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppCardQuest.trainer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
