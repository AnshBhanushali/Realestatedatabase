from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0020_auto_20200414_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='area',
        ),
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.RemoveField(
            model_name='address',
            name='zipcode',
        ),
    ]