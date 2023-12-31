from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0004_auto_20200407_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_purchase', models.DateField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.Agent')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.Client')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.Property')),
            ],
        ),
    ]