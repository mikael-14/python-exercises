# Generated by Django 4.2.9 on 2024-01-29 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_contactos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LigaContacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_destino', to='gestao_contactos.contacto')),
                ('origem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_origem', to='gestao_contactos.contacto')),
            ],
            options={
                'unique_together': {('origem', 'destino')},
            },
        ),
    ]