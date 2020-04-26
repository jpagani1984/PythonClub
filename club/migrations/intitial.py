from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by', to='users.Users')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by', to='users.Users')),
                ('attendance', models.ManyToManyField(related_name='other_user', to='users.Users')),
                ('event_time', models.DateTimeField(auto_now_add=True)),
                ('event_date', models.DateTimeField(auto_now_add=True)),
                ('meeting_time', models.DateTimeField(auto_now_add=True)),
                ('meeting_date', models.DateTimeField(auto_now_add=True)),
                ],
        ),
    ]
    