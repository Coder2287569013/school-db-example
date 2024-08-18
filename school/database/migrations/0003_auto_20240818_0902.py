# Generated by Django 3.2.23 on 2024-08-18 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_rename_head_teacher_grade_class_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='subjects',
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.grade')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.teacher')),
            ],
        ),
    ]
