from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0007_auto_20200408_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='facing',
            field=models.CharField(blank=True, choices=[('north', 'north'), ('south', 'south'), ('west', 'west'), ('east', 'east')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='property_image'),
        ),
    ]