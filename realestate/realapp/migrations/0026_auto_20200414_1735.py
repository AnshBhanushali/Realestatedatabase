from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0025_auto_20200414_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realestate.City'),
        ),
        migrations.AlterField(
            model_name='area',
            name='area',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='area',
            name='zipcode',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Zipcode',
        ),
    ]