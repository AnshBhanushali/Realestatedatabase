from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0016_auto_20200410_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='description',
        ),
        migrations.RemoveField(
            model_name='property',
            name='facing',
        ),
        migrations.AlterField(
            model_name='property',
            name='property_image',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to='images/', verbose_name='property_image'),
        ),
    ]