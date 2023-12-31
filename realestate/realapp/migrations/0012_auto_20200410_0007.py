from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0011_auto_20200408_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_image',
            field=models.ImageField(blank=True, null=True, upload_to='realestate/statis/images/', verbose_name='property_image'),
        ),
        migrations.AddIndex(
            model_name='property',
            index=models.Index(fields=['property_name'], name='realestate__propert_eb3145_idx'),
        ),
    ]