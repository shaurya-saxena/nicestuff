# Generated by Django 2.1.7 on 2019-05-15 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('pid', models.IntegerField(db_column='Product ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50)),
                ('desc', models.CharField(db_column='Description', max_length=500)),
                ('cat', models.CharField(db_column='Category', max_length=50)),
                ('price', models.IntegerField(db_column='Price')),
                ('image_url', models.CharField(db_column='Image Link', max_length=200)),
                ('seller_url', models.CharField(db_column='Seller Link', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='RecommendationsAccs',
            fields=[
                ('user', models.OneToOneField(db_column='User', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rec1', models.IntegerField(db_column='Recommendation 1')),
                ('rec2', models.IntegerField(db_column='Recommendation 2')),
                ('rec3', models.IntegerField(db_column='Recommendation 3')),
                ('rec4', models.IntegerField(db_column='Recommendation 4')),
                ('rec5', models.IntegerField(db_column='Recommendation 5')),
                ('rec6', models.IntegerField(db_column='Recommendation 6')),
                ('rec7', models.IntegerField(db_column='Recommendation 7')),
                ('rec8', models.IntegerField(db_column='Recommendation 8')),
                ('rec9', models.IntegerField(db_column='Recommendation 9')),
            ],
            options={
                'verbose_name_plural': 'Accessories Recommendations',
            },
        ),
        migrations.CreateModel(
            name='RecommendationsBPC',
            fields=[
                ('user', models.OneToOneField(db_column='User', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rec1', models.IntegerField(db_column='Recommendation 1')),
                ('rec2', models.IntegerField(db_column='Recommendation 2')),
                ('rec3', models.IntegerField(db_column='Recommendation 3')),
                ('rec4', models.IntegerField(db_column='Recommendation 4')),
                ('rec5', models.IntegerField(db_column='Recommendation 5')),
                ('rec6', models.IntegerField(db_column='Recommendation 6')),
                ('rec7', models.IntegerField(db_column='Recommendation 7')),
                ('rec8', models.IntegerField(db_column='Recommendation 8')),
                ('rec9', models.IntegerField(db_column='Recommendation 9')),
            ],
            options={
                'verbose_name_plural': 'Beauty and Personal Care Recommendations',
            },
        ),
        migrations.CreateModel(
            name='RecommendationsFurn',
            fields=[
                ('user', models.OneToOneField(db_column='User', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rec1', models.IntegerField(db_column='Recommendation 1')),
                ('rec2', models.IntegerField(db_column='Recommendation 2')),
                ('rec3', models.IntegerField(db_column='Recommendation 3')),
                ('rec4', models.IntegerField(db_column='Recommendation 4')),
                ('rec5', models.IntegerField(db_column='Recommendation 5')),
                ('rec6', models.IntegerField(db_column='Recommendation 6')),
                ('rec7', models.IntegerField(db_column='Recommendation 7')),
                ('rec8', models.IntegerField(db_column='Recommendation 8')),
                ('rec9', models.IntegerField(db_column='Recommendation 9')),
            ],
            options={
                'verbose_name_plural': 'Furniture Recommendations',
            },
        ),
        migrations.CreateModel(
            name='RecommendationsHD',
            fields=[
                ('user', models.OneToOneField(db_column='User', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rec1', models.IntegerField(db_column='Recommendation 1')),
                ('rec2', models.IntegerField(db_column='Recommendation 2')),
                ('rec3', models.IntegerField(db_column='Recommendation 3')),
                ('rec4', models.IntegerField(db_column='Recommendation 4')),
                ('rec5', models.IntegerField(db_column='Recommendation 5')),
                ('rec6', models.IntegerField(db_column='Recommendation 6')),
                ('rec7', models.IntegerField(db_column='Recommendation 7')),
                ('rec8', models.IntegerField(db_column='Recommendation 8')),
                ('rec9', models.IntegerField(db_column='Recommendation 9')),
            ],
            options={
                'verbose_name_plural': 'Home Decor Recommendations',
            },
        ),
        migrations.CreateModel(
            name='RecommendationsKD',
            fields=[
                ('user', models.OneToOneField(db_column='User', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rec1', models.IntegerField(db_column='Recommendation 1')),
                ('rec2', models.IntegerField(db_column='Recommendation 2')),
                ('rec3', models.IntegerField(db_column='Recommendation 3')),
                ('rec4', models.IntegerField(db_column='Recommendation 4')),
                ('rec5', models.IntegerField(db_column='Recommendation 5')),
                ('rec6', models.IntegerField(db_column='Recommendation 6')),
                ('rec7', models.IntegerField(db_column='Recommendation 7')),
                ('rec8', models.IntegerField(db_column='Recommendation 8')),
                ('rec9', models.IntegerField(db_column='Recommendation 9')),
            ],
            options={
                'verbose_name_plural': 'Kitchen and Dining Recommendations',
            },
        ),
        migrations.CreateModel(
            name='RecommendationsMA',
            fields=[
                ('user', models.OneToOneField(db_column='User', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rec1', models.IntegerField(db_column='Recommendation 1')),
                ('rec2', models.IntegerField(db_column='Recommendation 2')),
                ('rec3', models.IntegerField(db_column='Recommendation 3')),
                ('rec4', models.IntegerField(db_column='Recommendation 4')),
                ('rec5', models.IntegerField(db_column='Recommendation 5')),
                ('rec6', models.IntegerField(db_column='Recommendation 6')),
                ('rec7', models.IntegerField(db_column='Recommendation 7')),
                ('rec8', models.IntegerField(db_column='Recommendation 8')),
                ('rec9', models.IntegerField(db_column='Recommendation 9')),
            ],
            options={
                'verbose_name': "Men's Apparel Recommendations",
                'verbose_name_plural': "Men's Apparel Recommendations",
            },
        ),
        migrations.CreateModel(
            name='RecommendationsMF',
            fields=[
                ('user', models.OneToOneField(db_column='User', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rec1', models.IntegerField(db_column='Recommendation 1')),
                ('rec2', models.IntegerField(db_column='Recommendation 2')),
                ('rec3', models.IntegerField(db_column='Recommendation 3')),
                ('rec4', models.IntegerField(db_column='Recommendation 4')),
                ('rec5', models.IntegerField(db_column='Recommendation 5')),
                ('rec6', models.IntegerField(db_column='Recommendation 6')),
                ('rec7', models.IntegerField(db_column='Recommendation 7')),
                ('rec8', models.IntegerField(db_column='Recommendation 8')),
                ('rec9', models.IntegerField(db_column='Recommendation 9')),
            ],
            options={
                'verbose_name_plural': "Men's Footwear Recommendations",
            },
        ),
        migrations.CreateModel(
            name='RecommendationsTech',
            fields=[
                ('user', models.OneToOneField(db_column='User', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rec1', models.IntegerField(db_column='Recommendation 1')),
                ('rec2', models.IntegerField(db_column='Recommendation 2')),
                ('rec3', models.IntegerField(db_column='Recommendation 3')),
                ('rec4', models.IntegerField(db_column='Recommendation 4')),
                ('rec5', models.IntegerField(db_column='Recommendation 5')),
                ('rec6', models.IntegerField(db_column='Recommendation 6')),
                ('rec7', models.IntegerField(db_column='Recommendation 7')),
                ('rec8', models.IntegerField(db_column='Recommendation 8')),
                ('rec9', models.IntegerField(db_column='Recommendation 9')),
            ],
            options={
                'verbose_name_plural': 'Tech Recommendations',
            },
        ),
        migrations.CreateModel(
            name='RecommendationsWA',
            fields=[
                ('user', models.OneToOneField(db_column='User', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rec1', models.IntegerField(db_column='Recommendation 1')),
                ('rec2', models.IntegerField(db_column='Recommendation 2')),
                ('rec3', models.IntegerField(db_column='Recommendation 3')),
                ('rec4', models.IntegerField(db_column='Recommendation 4')),
                ('rec5', models.IntegerField(db_column='Recommendation 5')),
                ('rec6', models.IntegerField(db_column='Recommendation 6')),
                ('rec7', models.IntegerField(db_column='Recommendation 7')),
                ('rec8', models.IntegerField(db_column='Recommendation 8')),
                ('rec9', models.IntegerField(db_column='Recommendation 9')),
            ],
            options={
                'verbose_name_plural': "Women's Apparel Recommendations",
            },
        ),
        migrations.CreateModel(
            name='RecommendationsWF',
            fields=[
                ('user', models.OneToOneField(db_column='User', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rec1', models.IntegerField(db_column='Recommendation 1')),
                ('rec2', models.IntegerField(db_column='Recommendation 2')),
                ('rec3', models.IntegerField(db_column='Recommendation 3')),
                ('rec4', models.IntegerField(db_column='Recommendation 4')),
                ('rec5', models.IntegerField(db_column='Recommendation 5')),
                ('rec6', models.IntegerField(db_column='Recommendation 6')),
                ('rec7', models.IntegerField(db_column='Recommendation 7')),
                ('rec8', models.IntegerField(db_column='Recommendation 8')),
                ('rec9', models.IntegerField(db_column='Recommendation 9')),
            ],
            options={
                'verbose_name_plural': "Women's Footwear Recommendations",
            },
        ),
        migrations.CreateModel(
            name='TxnHistory',
            fields=[
                ('txnid', models.IntegerField(db_column='Transaction ID', primary_key=True, serialize=False)),
                ('pid', models.IntegerField(db_column='Product ID')),
                ('user', models.IntegerField(db_column='User ID')),
                ('status', models.BooleanField(db_column='Status')),
                ('timestamp', models.IntegerField(db_column='Timestamp in seconds since 1 January 2019')),
            ],
            options={
                'verbose_name_plural': 'Transaction History',
            },
        ),
    ]
