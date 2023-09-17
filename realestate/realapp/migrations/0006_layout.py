from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0005_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='img')),
            ],
        ),
    ]