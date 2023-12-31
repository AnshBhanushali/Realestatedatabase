from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0019_auto_20200414_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='area',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='zipcode',
            field=models.CharField(max_length=50, null=True),
        ),
    ]