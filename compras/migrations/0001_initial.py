# Generated by Django 3.2.3 on 2021-05-28 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PC', models.CharField(blank=True, max_length=100, null=True)),
                ('PC_IT', models.CharField(blank=True, max_length=100, null=True)),
                ('status_pc', models.CharField(blank=True, max_length=100, null=True)),
                ('metodo_de_cobranca', models.CharField(blank=True, choices=[('nf+nd', 'NF+ND'), ('nf', 'NF')], max_length=100, null=True)),
                ('tipo_de_progresso', models.CharField(blank=True, max_length=100, null=True)),
                ('Data', models.DateField(blank=True, null=True)),
                ('status_ps', models.CharField(blank=True, choices=[('enviado', 'Enviado'), ('emitido', 'Emitido'), ('naoemitido', 'Não Emitido')], max_length=100, null=True)),
                ('pagamento', models.CharField(blank=True, choices=[('pago', 'Pago'), ('naopago', 'Não Pago')], max_length=100, null=True)),
                ('notafiscal', models.CharField(blank=True, max_length=150, null=True)),
                ('condicao_de_pagamento', models.CharField(blank=True, choices=[('28ddl', '28ddl'), ('45ddl', '45ddl'), ('variavel', 'Variável')], max_length=100, null=True)),
                ('metodo_de_pagamento', models.CharField(blank=True, choices=[('boleto', 'Boleto'), ('transferencia', 'Transferência Bancária')], max_length=100, null=True)),
                ('prazo', models.DateField(blank=True, null=True)),
                ('forma_entrega', models.CharField(blank=True, choices=[('email', 'E-mail'), ('retira', 'Retira'), ('transportadora', 'Transportadora')], max_length=100, null=True)),
                ('frases_padrao', models.TextField(blank=True, null=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('imposto', models.CharField(blank=True, max_length=100, null=True)),
                ('porcentagem_impostos', models.DecimalField(decimal_places=4, default=0.0, max_digits=50)),
                ('fornecedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastro.fornecedor')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.CreateModel(
            name='ItemCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalhamento', models.CharField(blank=True, max_length=200, null=True)),
                ('unidade', models.CharField(blank=True, max_length=50, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=50)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.compras')),
                ('descricao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastro.compras')),
            ],
            options={
                'verbose_name': 'Item da Compra',
                'verbose_name_plural': 'Itens da Compra',
            },
        ),
    ]
