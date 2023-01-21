# Generated by Django 4.1.4 on 2023-01-21 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("contact_info", models.CharField(max_length=255)),
                ("loyalty_points", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_cost", models.DecimalField(decimal_places=2, max_digits=10)),
                ("order_date", models.DateTimeField()),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("contact_info", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Tax",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rate", models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount_paid", models.DecimalField(decimal_places=2, max_digits=10)),
                ("payment_method", models.CharField(max_length=255)),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.order",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("buying_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("selling_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.PositiveIntegerField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.category",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.supplier",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(to="inventory.product"),
        ),
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                (
                    "product",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.product",
                    ),
                ),
            ],
        ),
    ]
