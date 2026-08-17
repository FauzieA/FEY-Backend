# Generated migration for UUID primary keys and timestamp fields

from django.db import migrations, models
import django.db.models.deletion
import uuid
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        # Character Profile
        migrations.CreateModel(
            name='CharacterProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField(default=1)),
                ('xp', models.IntegerField(default=0)),
                ('streak_days', models.IntegerField(default=0)),
                ('last_active', models.DateField(null=True, blank=True)),
                ('avatar_url', models.URLField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Workout Session
        migrations.CreateModel(
            name='WorkoutSession',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('duration_minutes', models.IntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Session Exercise
        migrations.CreateModel(
            name='SessionExercise',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='api.workoutsession')),
                ('exercise_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('muscle_group', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        
        # Exercise Set Log
        migrations.CreateModel(
            name='ExerciseSetLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('session_exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets', to='api.sessionexercise')),
                ('set_number', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('weight_kg', models.FloatField(null=True, blank=True)),
                ('rpe', models.IntegerField(null=True, blank=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        
        # Salah Log
        migrations.CreateModel(
            name='SalahLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField(unique=True)),
                ('fajr', models.CharField(max_length=20)),
                ('dhuhr', models.CharField(max_length=20)),
                ('asr', models.CharField(max_length=20)),
                ('maghrib', models.CharField(max_length=20)),
                ('isha', models.CharField(max_length=20)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='prayer_logs', to='auth.user')),
            ],
        ),
        
        # Memorization Log
        migrations.CreateModel(
            name='MemorizationLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('surah', models.CharField(max_length=100)),
                ('ayah', models.IntegerField()),
                ('quality', models.IntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='memorization_logs', to='auth.user')),
            ],
        ),
        
        # Dhikr Log
        migrations.CreateModel(
            name='DhikrLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('dhikr_type', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='dhikr_logs', to='auth.user')),
            ],
        ),
        
        # XP Event
        migrations.CreateModel(
            name='XpEvent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('xp_amount', models.IntegerField()),
                ('source', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='xp_events', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Achievement Record
        migrations.CreateModel(
            name='AchievementRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('achievement_id', models.CharField(max_length=100)),
                ('unlocked_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='auth.user')),
            ],
        ),
        
        # App Settings
        migrations.CreateModel(
            name='AppSettings',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('theme', models.CharField(max_length=20, default='light')),
                ('language', models.CharField(max_length=10, default='en')),
                ('notifications_enabled', models.BooleanField(default=True)),
                ('user', models.OneToOneField(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Personal Record
        migrations.CreateModel(
            name='PersonalRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('exercise', models.CharField(max_length=100)),
                ('weight_kg', models.FloatField()),
                ('reps', models.IntegerField()),
                ('date', models.DateField()),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='personal_records', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Workout Plan
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('plan_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('day_of_week', models.CharField(max_length=20)),
                ('target_muscles', models.TextField(blank=True, null=True)),
                ('exercises', models.JSONField()),
            ],
        ),
        
        # Quran Reading Log
        migrations.CreateModel(
            name='QuranReadingLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('surah', models.CharField(max_length=100)),
                ('from_ayah', models.IntegerField()),
                ('to_ayah', models.IntegerField()),
                ('pages', models.IntegerField(null=True, blank=True)),
                ('minutes', models.IntegerField(null=True, blank=True)),
                ('reflection', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='quran_reading_logs', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Memorization Entry
        migrations.CreateModel(
            name='MemorizationEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('surah', models.CharField(max_length=100)),
                ('from_ayah', models.IntegerField()),
                ('to_ayah', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('last_reviewed_at', models.DateTimeField(null=True, blank=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='memorization_entries', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Revision Log
        migrations.CreateModel(
            name='RevisionLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('surah', models.CharField(max_length=100)),
                ('quality', models.IntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='revision_logs', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Adhkar Log
        migrations.CreateModel(
            name='AdhkarLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField(unique=True)),
                ('morning', models.BooleanField(default=False)),
                ('evening', models.BooleanField(default=False)),
                ('after_prayer', models.BooleanField(default=False)),
                ('istighfar_count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='adhkar_logs', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Missed Fast
        migrations.CreateModel(
            name='MissedFast',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('missed_on', models.DateField()),
                ('reason', models.CharField(blank=True, null=True, max_length=200)),
                ('made_up_on', models.DateField(null=True, blank=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='missed_fasts', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Measurement
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('waist_cm', models.FloatField(null=True, blank=True)),
                ('hips_cm', models.FloatField(null=True, blank=True)),
                ('chest_cm', models.FloatField(null=True, blank=True)),
                ('thigh_cm', models.FloatField(null=True, blank=True)),
                ('arm_cm', models.FloatField(null=True, blank=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Weight Log
        migrations.CreateModel(
            name='WeightLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('weight_kg', models.FloatField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='weight_logs', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('date',)},
            },
        ),
        
        # Sleep Log
        migrations.CreateModel(
            name='SleepLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('hours', models.FloatField()),
                ('quality', models.IntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sleep_logs', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('date',)},
            },
        ),
        
        # Cycle Log
        migrations.CreateModel(
            name='CycleLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('symptoms', models.TextField(blank=True, null=True)),
                ('flow', models.IntegerField(null=True, blank=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cycle_logs', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Health Note
        migrations.CreateModel(
            name='HealthNote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('details', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='health_notes', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Book
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('total_pages', models.IntegerField()),
                ('current_page', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=20)),
                ('started_at', models.DateField(null=True, blank=True)),
                ('finished_at', models.DateField(null=True, blank=True)),
                ('rating', models.IntegerField(null=True, blank=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('series_name', models.CharField(blank=True, null=True, max_length=200)),
                ('expected_release_date', models.DateField(null=True, blank=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Reading Session
        migrations.CreateModel(
            name='ReadingSession',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('pages_read', models.IntegerField()),
                ('minutes', models.IntegerField(null=True, blank=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='api.book')),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reading_sessions', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Perfume Formula
        migrations.CreateModel(
            name='PerfumeFormula',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('inspiration', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('archived', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='perfume_formulas', to='auth.user')),
            ],
        ),
        
        # Perfume Version
        migrations.CreateModel(
            name='PerfumeVersion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('version', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('unit', models.CharField(max_length=10)),
                ('ingredients', models.JSONField()),
                ('observations', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(null=True, blank=True)),
                ('formula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='api.perfumeformula')),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='perfume_versions', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Savings Goal
        migrations.CreateModel(
            name='SavingsGoal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('target_amount', models.FloatField()),
                ('target_date', models.DateField(null=True, blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed_at', models.DateField(null=True, blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='savings_goals', to='auth.user')),
            ],
        ),
        
        # Savings Entry
        migrations.CreateModel(
            name='SavingsEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('note', models.TextField(blank=True, null=True)),
                ('goal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entries', to='api.savingsgoal')),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='savings_entries', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Purchase Plan
        migrations.CreateModel(
            name='PurchasePlan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('priority', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('purchased_at', models.DateField(null=True, blank=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_plans', to='auth.user')),
            ],
        ),
        
        # Wealth Profile
        migrations.CreateModel(
            name='WealthProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('currency', models.CharField(default='USD', max_length=10)),
                ('hourly_rate', models.FloatField(default=0.0)),
                ('monthly_savings_target', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='wealth_profile', to='auth.user')),
            ],
        ),
        
        # Journal Entry
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('mood', models.IntegerField(null=True, blank=True)),
                ('gratitude', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='journal_entries', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Person
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=100)),
                ('cadence_days', models.IntegerField()),
                ('last_contacted_at', models.DateField(null=True, blank=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='people', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Call Reminder
        migrations.CreateModel(
            name='CallReminder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('due_date', models.DateField()),
                ('completed_at', models.DateField(null=True, blank=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminders', to='api.person')),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='call_reminders', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Timeline Event
        migrations.CreateModel(
            name='TimelineEvent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='timeline_events', to='auth.user')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
