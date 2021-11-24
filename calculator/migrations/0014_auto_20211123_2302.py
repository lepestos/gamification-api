# Generated by Django 3.2.8 on 2021-11-23 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0013_alter_bingo_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('budget_in_percents', models.DecimalField(decimal_places=2, max_digits=3)),
                ('participants', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='discount',
            old_name='discount',
            new_name='value',
        ),
        migrations.RenameModel(
            old_name='Bingo',
            new_name='BingoDiscount',
        ),
        migrations.DeleteModel(
            name='DiscountOfProduct',
        ),
        migrations.AddField(
            model_name='discountproduct',
            name='bingo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bingo_items', to='calculator.bingodiscount'),
        ),
        migrations.AddField(
            model_name='discountproduct',
            name='discount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bingo_items', to='calculator.discount'),
        ),
        migrations.AddField(
            model_name='discountproduct',
            name='lot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bingo_items', to='calculator.lot'),
        ),
    ]
