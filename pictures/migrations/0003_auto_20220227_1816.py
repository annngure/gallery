# Generated by Django 3.0 on 2022-02-27 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_category_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=30)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictures.Category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictures.Location')),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictures.Photographer')),
            ],
        ),
    ]