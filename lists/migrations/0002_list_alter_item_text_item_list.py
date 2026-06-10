from django.db import migrations, models
import django.db.models.deletion

def create_default_list(apps, schema_editor):
    List = apps.get_model('lists', 'List')
    Item = apps.get_model('lists', 'Item')
    default_list = List.objects.create()
    for item in Item.objects.all():
        item.list = default_list
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
            ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lists.list'),
            ),

    ]