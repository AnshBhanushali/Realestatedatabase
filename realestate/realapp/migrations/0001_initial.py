from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_agent', models.BooleanField(default=False)),
                ('is_office', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=30)),
                ('city', models.CharField(default='Indore', max_length=30)),
                ('country', models.CharField(default='India', max_length=30)),
                ('zipcode', models.IntegerField()),
                ('description', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('property_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(choices=[('sale', 'sale'), ('rent', 'rent')], default='sale', max_length=4)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('no_of_bedrooms', models.IntegerField(default=1)),
                ('no_of_bathrooms', models.IntegerField(default=1)),
                ('facing', models.CharField(choices=[('north', 'north'), ('south', 'south'), ('west', 'west'), ('east', 'east')], max_length=6, null=True)),
                ('floor', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=True)),
                ('date_of_entry', models.DateField()),
                ('description', models.TextField(max_length=100)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realestate.Address')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realestate.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_purchase', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.Client')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.Property')),
            ],
        ),
        migrations.AddField(
            model_name='owner',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.Person'),
        ),
        migrations.AddField(
            model_name='client',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.Person'),
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.Person')),
            ],
        ),
    ]