from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import uuid

class CharacterProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='character_profile', null=True, blank=True)
    level = models.IntegerField(default=1)
    current_xp = models.IntegerField(default=0)
    next_level_xp = models.IntegerField(default=300)
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0) # Added for streak analytics
    last_workout_date = models.DateTimeField(null=True, blank=True)
    
    # RPG Attributes: {STR, END, VOL, CON}
    attributes = models.JSONField(default=dict)
    
    # Lifetime summary stats for instant profile dashboard rendering
    total_workouts_completed = models.IntegerField(default=0)
    total_hours_trained = models.FloatField(default=0.0)
    
    # Sync fields
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        username = self.user.username if self.user else 'anonymous'
        return f"{username}'s Profile (Lv. {self.level})"


class WorkoutSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_sessions', null=True, blank=True)
    plan_id = models.CharField(max_length=50, blank=True, null=True)
    plan_title = models.CharField(max_length=100, blank=True, null=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField()
    duration_seconds = models.IntegerField(default=0)
    duration_minutes = models.IntegerField(default=0)
    
    # Macro Analytics metrics
    total_sets_completed = models.IntegerField(default=0)
    total_reps_completed = models.IntegerField(default=0)
    
    # Intensity & Rating Analytics
    average_rpe = models.FloatField(default=0.0) # Rate of Perceived Exertion (1-10) for intensity analytics
    session_rating = models.IntegerField(null=True, blank=True) # User feedback (1-5 stars)
    
    xp_earned = models.IntegerField(default=0)
    completed = models.BooleanField(default=True)
    
    # Sync fields
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        username = self.user.username if self.user else 'anonymous'
        return f"Workout Session ({self.plan_title or 'Custom'}) - {username}"


class SessionExercise(models.Model):
    session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE, related_name='exercises')
    exercise_id = models.CharField(max_length=100)
    exercise_name = models.CharField(max_length=100, blank=True, null=True)
    
    # Metadata for muscle distribution charts and category filters
    category = models.CharField(max_length=50, blank=True, null=True) # e.g., "Upper Push", "Lower Body"
    primary_muscle = models.CharField(max_length=50, blank=True, null=True) # e.g., "Chest", "Quads"
    
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.exercise_name or self.exercise_id}"


class ExerciseSetLog(models.Model):
    exercise = models.ForeignKey(SessionExercise, on_delete=models.CASCADE, related_name='sets')
    set_num = models.IntegerField(default=1)
    
    # Performance metrics
    reps = models.IntegerField(default=0)
    weight_kg = models.FloatField(default=0.0)
    duration_sec = models.IntegerField(default=0) # For time-based exercises (planks, holds)
    
    # Advanced Set Analytics Fields
    set_type = models.CharField(max_length=20, default='working') # 'warmup', 'working', 'drop_set', 'failure'
    rpe = models.IntegerField(null=True, blank=True) # Individual set intensity rating
    estimated_1rm = models.FloatField(default=0.0) # Calculated strength milestone tracking (e.g., Brzycki formula)
    rest_seconds_after = models.IntegerField(default=0) # Tracking rest efficiency
    
    completed = models.BooleanField(default=True)

    def __str__(self):
        return f"Set {self.set_num}: {self.reps} reps @ {self.weight_kg}kg ({self.set_type})"


# ==========================================
# LIFESTYLE TRACKERS (Salah, Memorization, Dhikr)
# ==========================================
class SalahLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salah_logs', null=True, blank=True)
    date = models.DateField()
    fajr = models.CharField(max_length=20, default='pending')     # 'on_time', 'delayed', 'missed', 'qada'
    dhuhr = models.CharField(max_length=20, default='pending')
    asr = models.CharField(max_length=20, default='pending')
    maghrib = models.CharField(max_length=20, default='pending')
    isha = models.CharField(max_length=20, default='pending')

    class Meta:
        unique_together = ('date',)


class MemorizationLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memorization_logs', null=True, blank=True)
    title = models.CharField(max_length=100) # e.g., "Surah Al-Mulk"
    status = models.CharField(max_length=30, default='in_progress') # 'memorizing', 'revising', 'completed'
    current_verse = models.IntegerField(default=0)
    total_verses = models.IntegerField(default=0)
    last_practiced = models.DateField(auto_now=True)


class DhikrLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dhikr_logs', null=True, blank=True)
    date = models.DateField()
    dhikr_type = models.CharField(max_length=50) # e.g., "Astaghfar", "Salawat"
    count = models.IntegerField(default=0)
    target_count = models.IntegerField(default=100)

    class Meta:
        unique_together = ('user', 'date', 'dhikr_type')


# ==========================================
# CHARACTER & GAMIFICATION
# ==========================================
class XpEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='xp_events', null=True, blank=True)
    module = models.CharField(max_length=50)  # training, faith, health, library, perfumery, wealth, life
    activity = models.CharField(max_length=100)
    amount = models.IntegerField()
    attribute = models.CharField(max_length=50)  # discipline, devotion, strength, vitality, knowledge, craft, stewardship, connection
    date = models.DateField()
    session_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class AchievementRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements', null=True, blank=True)
    achievement_id = models.CharField(max_length=100, unique=True)
    unlocked_at = models.DateTimeField(auto_now_add=True)


class AppSettings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='app_settings', null=True, blank=True)
    default_rest_seconds = models.IntegerField(default=90)
    sound_enabled = models.BooleanField(default=True)
    vibration_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class PersonalRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personal_records', null=True, blank=True)
    exercise_id = models.CharField(max_length=100)
    weight = models.FloatField()
    reps = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'exercise_id', 'date')


class WorkoutPlan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans', null=True, blank=True)
    plan_id = models.CharField(max_length=50, unique=True)  # e.g., 'plan_mon'
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True, null=True)
    day_of_week = models.IntegerField(null=True, blank=True)
    target_muscles = models.JSONField(default=list, blank=True)
    exercises = models.JSONField()  # List of exercise objects with exerciseId, exerciseName, targetSets, targetReps, targetWeightKg


# ==========================================
# FAITH MODULE (Extended)
# ==========================================
class QuranReadingLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quran_reading_logs', null=True, blank=True)
    date = models.DateField()
    surah = models.CharField(max_length=100)
    from_ayah = models.IntegerField()
    to_ayah = models.IntegerField()
    pages = models.IntegerField(null=True, blank=True)
    minutes = models.IntegerField(null=True, blank=True)
    reflection = models.TextField(blank=True, null=True)


class MemorizationEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memorization_entries', null=True, blank=True)
    surah = models.CharField(max_length=100)
    from_ayah = models.IntegerField()
    to_ayah = models.IntegerField()
    status = models.CharField(max_length=20)  # learning, memorized, needs-work
    started_at = models.DateTimeField(auto_now_add=True)
    last_reviewed_at = models.DateTimeField(null=True, blank=True)


class RevisionLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='revision_logs', null=True, blank=True)
    date = models.DateField()
    surah = models.CharField(max_length=100)
    quality = models.IntegerField()  # 1-5 self-assessed recall quality
    notes = models.TextField(blank=True, null=True)


class AdhkarLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adhkar_logs', null=True, blank=True)
    date = models.DateField(unique=True)
    morning = models.BooleanField(default=False)
    evening = models.BooleanField(default=False)
    after_prayer = models.BooleanField(default=False)
    istighfar_count = models.IntegerField(default=0)


class MissedFast(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='missed_fasts', null=True, blank=True)
    missed_on = models.DateField()
    reason = models.CharField(max_length=200, blank=True, null=True)
    made_up_on = models.DateField(null=True, blank=True)


# ==========================================
# HEALTH MODULE
# ==========================================
class Measurement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='measurements', null=True, blank=True)
    date = models.DateField()
    waist_cm = models.FloatField(null=True, blank=True)
    hips_cm = models.FloatField(null=True, blank=True)
    chest_cm = models.FloatField(null=True, blank=True)
    thigh_cm = models.FloatField(null=True, blank=True)
    arm_cm = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)


class WeightLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weight_logs', null=True, blank=True)
    date = models.DateField()
    weight_kg = models.FloatField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('date',)


class SleepLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sleep_logs', null=True, blank=True)
    date = models.DateField()  # Date the night started
    hours = models.FloatField()
    quality = models.IntegerField()  # 1-5 self-assessed
    notes = models.TextField(blank=True, null=True)

    class Meta: 
        unique_together = ('date',)


class CycleLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cycle_logs', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    symptoms = models.TextField(blank=True, null=True)
    flow = models.IntegerField(null=True, blank=True)  # 1-5 self-assessed


class HealthNote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='health_notes', null=True, blank=True)
    date = models.DateField()
    category = models.CharField(max_length=20)  # symptom, appointment, medication, general
    title = models.CharField(max_length=200)
    details = models.TextField(blank=True, null=True)


# ==========================================
# LIBRARY MODULE
# ==========================================
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    total_pages = models.IntegerField()
    current_page = models.IntegerField(default=0)
    status = models.CharField(max_length=20)  # reading, finished, waiting
    started_at = models.DateField(null=True, blank=True)
    finished_at = models.DateField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    series_name = models.CharField(max_length=200, blank=True, null=True)
    expected_release_date = models.DateField(null=True, blank=True)


class ReadingSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_sessions', null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='sessions')
    date = models.DateField()
    pages_read = models.IntegerField()
    minutes = models.IntegerField(null=True, blank=True)


# ==========================================
# PERFUMERY MODULE
# ==========================================
class PerfumeFormula(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='perfume_formulas', null=True, blank=True)
    name = models.CharField(max_length=200)
    inspiration = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    archived = models.BooleanField(default=False)


class PerfumeVersion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='perfume_versions', null=True, blank=True)
    formula = models.ForeignKey(PerfumeFormula, on_delete=models.CASCADE, related_name='versions')
    version = models.CharField(max_length=50)
    date = models.DateField()
    unit = models.CharField(max_length=10)  # drops, g, ml
    ingredients = models.JSONField()  # List of {name, note, amount}
    observations = models.TextField(blank=True, null=True)
    rating = models.IntegerField(null=True, blank=True)


# ==========================================
# WEALTH MODULE
# ==========================================
class SavingsEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savings_entries', null=True, blank=True)
    date = models.DateField()
    amount = models.FloatField()
    goal = models.ForeignKey('SavingsGoal', on_delete=models.SET_NULL, null=True, blank=True, related_name='entries')
    note = models.TextField(blank=True, null=True)


class SavingsGoal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savings_goals', null=True, blank=True)
    name = models.CharField(max_length=200)
    target_amount = models.FloatField()
    target_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateField(null=True, blank=True)


class PurchasePlan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_plans', null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    priority = models.CharField(max_length=10)  # low, medium, high
    created_at = models.DateTimeField(default=timezone.now)
    purchased_at = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)


class WealthProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wealth_profile', null=True, blank=True)
    currency = models.CharField(max_length=10, default='USD')
    hourly_rate = models.FloatField(default=0.0)
    monthly_savings_target = models.FloatField(default=0.0)


# ==========================================
# LIFE MODULE
# ==========================================
class JournalEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal_entries', null=True, blank=True)
    date = models.DateField()
    title = models.CharField(max_length=200)
    body = models.TextField()
    mood = models.IntegerField(null=True, blank=True)
    gratitude = models.TextField(blank=True, null=True)


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='people', null=True, blank=True)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    cadence_days = models.IntegerField()  # How often (in days) to reach out
    last_contacted_at = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)


class CallReminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='call_reminders', null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='reminders')
    due_date = models.DateField()
    completed_at = models.DateField(null=True, blank=True)
    note = models.TextField(blank=True, null=True)


class TimelineEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='timeline_events', null=True, blank=True)
    date = models.DateField()
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20)  # milestone, memory, decision, travel, other
    description = models.TextField(blank=True, null=True)