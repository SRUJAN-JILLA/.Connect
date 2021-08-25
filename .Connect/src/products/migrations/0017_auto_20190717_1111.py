# Generated by Django 2.1.7 on 2019-07-17 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20190716_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='items/images')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.RelatedImage'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.Product'),
        ),
    ]