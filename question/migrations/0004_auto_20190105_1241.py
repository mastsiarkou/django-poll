# Generated by Django 2.1.4 on 2019-01-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20190105_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='choice',
            field=models.CharField(choices=[('1', 'Radiohead: Kid A'), ('2', 'Pink Floyd: The dark side of the moon'), ('3', 'The Beatles: Abbey Road'), ('4', 'Massive Attack: Mezzanine'), ('5', 'Nirvana: Nevermind')], max_length=1),
        ),
    ]
