from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('release_year', models.IntegerField(validators=[movies.models.validate_release_year])),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3, validators=[movies.models.validate_rating])),
            ],
        ),
    ]
