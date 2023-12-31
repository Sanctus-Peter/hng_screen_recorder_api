# Generated by Django 4.2.5 on 2023-09-30 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecordingSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recording_id', models.CharField(max_length=255, unique=True)),
                ('mime_type', models.CharField(max_length=255)),
                ('status', models.CharField(default='recording', max_length=20)),
                ('transcription', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecordingChunk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('is_last_chunk', models.BooleanField(default=False)),
                ('file_path', models.FileField(upload_to='recording_chunks/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.recordingsession')),
            ],
        ),
    ]
