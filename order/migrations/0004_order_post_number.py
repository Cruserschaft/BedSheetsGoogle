# Generated by Django 4.1.2 on 2022-10-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_person_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='post_number',
            field=models.CharField(blank=True, default='', max_length=5, verbose_name='Відділення'),
        ),
    ]