# Generated by Django 3.2.12 on 2022-02-04 12:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='-unnamed-', max_length=200, verbose_name='Name of this brand/data source')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description of this instance of this brand/data source')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website of this brand/data source')),
                ('countries', models.CharField(blank=True, max_length=200)),
                ('tag', models.CharField(help_text=('the tag we use or this brand/datasource record at Bank.Green. ', 'Prepend this with the relevant datasource. i.e. banktrack_bank_of_america. for brands, prepend with nothing at all i.e. bank_of_america'), max_length=100, unique=True)),
                ('snippet_1', models.TextField(blank=True, default='', help_text='Used to fill in templates', verbose_name='Custom fact about the brand.')),
                ('snippet_2', models.TextField(blank=True, default='', help_text='Used to fill in templates', verbose_name='Custom fact about the brand.')),
                ('snippet_3', models.TextField(blank=True, default='', help_text='Used to fill in templates', verbose_name='Custom fact about the brand.')),
                ('permid', models.CharField(blank=True, max_length=15)),
                ('isin', models.CharField(blank=True, max_length=15)),
                ('viafid', models.CharField(blank=True, max_length=15)),
                ('lei', models.CharField(blank=True, max_length=15)),
                ('googleid', models.CharField(blank=True, max_length=15)),
                ('rssd', models.CharField(blank=True, max_length=15)),
                ('rssd_hd', models.CharField(blank=True, max_length=15)),
                ('cusip', models.CharField(blank=True, max_length=15)),
                ('thrift', models.CharField(blank=True, max_length=15)),
                ('thrift_hc', models.CharField(blank=True, max_length=15)),
                ('aba_prim', models.CharField(blank=True, max_length=15)),
                ('ncua', models.CharField(blank=True, max_length=15)),
                ('fdic_cert', models.CharField(blank=True, max_length=15)),
                ('occ', models.CharField(blank=True, max_length=15)),
                ('ein', models.CharField(blank=True, max_length=15)),
                ('source_link', models.URLField(blank=True, null=True, verbose_name="Link to the data source's webpage. i.e. the banktrack.org or b-impact webpage for the bank")),
                ('subsidiary_of_1_pct', models.IntegerField(default=0, verbose_name='percentage owned by subsidiary 1')),
                ('subsidiary_of_2_pct', models.IntegerField(default=0, verbose_name='percentage owned by subsidiary 2')),
                ('subsidiary_of_3_pct', models.IntegerField(default=0, verbose_name='percentage owned by subsidiary 3')),
                ('subsidiary_of_4_pct', models.IntegerField(default=0, verbose_name='percentage owned by subsidiary 4')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time of last update')),
                ('subsidiary_of_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subsidiary_of_1_data_source', to='brand.brand')),
                ('subsidiary_of_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subsidiary_of_2_data_source', to='brand.brand')),
                ('subsidiary_of_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subsidiary_of_3_data_source', to='brand.brand')),
                ('subsidiary_of_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subsidiary_of_4_data_source', to='brand.brand')),
            ],
        ),
    ]
