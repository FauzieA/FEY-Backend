from rest_framework import serializers
from .models import (
    CharacterProfile,
    WorkoutSession,
    SessionExercise,
    ExerciseSetLog,
    SalahLog,
    MemorizationLog,
    DhikrLog,
    XpEvent,
    AchievementRecord,
    AppSettings,
    PersonalRecord,
    WorkoutPlan,
    QuranReadingLog,
    MemorizationEntry,
    RevisionLog,
    AdhkarLog,
    MissedFast,
    Measurement,
    WeightLog,
    SleepLog,
    CycleLog,
    HealthNote,
    Book,
    ReadingSession,
    PerfumeFormula,
    PerfumeVersion,
    SavingsEntry,
    SavingsGoal,
    PurchasePlan,
    WealthProfile,
    JournalEntry,
    Person,
    CallReminder,
    TimelineEvent
)

class CharacterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterProfile
        fields = [
            'id', 'level', 'current_xp', 'next_level_xp', 
            'current_streak', 'longest_streak', 'last_workout_date', 
            'attributes', 'total_workouts_completed', 'total_hours_trained',
            'created_at', 'updated_at'
        ]


class ExerciseSetLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseSetLog
        fields = [
            'id', 'set_num', 'reps', 'weight_kg', 'duration_sec', 
            'set_type', 'rpe', 'estimated_1rm', 'rest_seconds_after', 'completed'
        ]


class SessionExerciseSerializer(serializers.ModelSerializer):
    sets = ExerciseSetLogSerializer(many=True)

    class Meta:
        model = SessionExercise
        fields = ['id', 'exercise_id', 'exercise_name', 'category', 'primary_muscle', 'notes', 'sets']


class WorkoutSessionSerializer(serializers.ModelSerializer):
    exercises = SessionExerciseSerializer(many=True)
    total_volume_kg = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = WorkoutSession
        fields = [
            'id', 'plan_id', 'plan_title', 'started_at', 'completed_at',
            'duration_seconds', 'duration_minutes', 'total_volume_kg',
            'total_sets_completed', 'total_reps_completed', 'average_rpe',
            'session_rating', 'xp_earned', 'completed', 'exercises',
            'created_at', 'updated_at'
        ]

    def get_total_volume_kg(self, obj):
        total = 0.0
        for exercise in obj.exercises.all():
            for set_log in exercise.sets.all():
                total += (getattr(set_log, 'reps', 0) or 0) * (getattr(set_log, 'weight_kg', 0.0) or 0.0)
        return total

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises', [])
        request = self.context.get('request')
        user = None
        if request is not None and hasattr(request, 'user'):
            user_obj = request.user
            user = user_obj if getattr(user_obj, 'is_authenticated', False) else None

        # Create session (user is now optional)
        session = WorkoutSession.objects.create(user=user, **validated_data)

        # Create nested exercises and sets
        for ex_data in exercises_data:
            sets_data = ex_data.pop('sets', [])
            exercise = SessionExercise.objects.create(session=session, **ex_data)

            for set_data in sets_data:
                ExerciseSetLog.objects.create(exercise=exercise, **set_data)

        return session


class SalahLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalahLog
        fields = ['id', 'date', 'fajr', 'dhuhr', 'asr', 'maghrib', 'isha']


class MemorizationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemorizationLog
        fields = ['id', 'title', 'status', 'current_verse', 'total_verses', 'last_practiced']


class DhikrLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DhikrLog
        fields = ['id', 'date', 'dhikr_type', 'count', 'target_count']


# ==========================================
# CHARACTER & GAMIFICATION SERIALIZERS
# ==========================================
class XpEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = XpEvent
        fields = ['id', 'module', 'activity', 'amount', 'attribute', 'date', 'session_id', 'created_at', 'updated_at']


class AchievementRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementRecord
        fields = ['id', 'achievement_id', 'unlocked_at']


class AppSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSettings
        fields = ['id', 'default_rest_seconds', 'sound_enabled', 'vibration_enabled', 'created_at', 'updated_at']


class PersonalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalRecord
        fields = ['id', 'exercise_id', 'weight', 'reps', 'date', 'created_at', 'updated_at']


class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = ['id', 'plan_id', 'title', 'name', 'day_of_week', 'target_muscles', 'exercises']


# ==========================================
# FAITH MODULE SERIALIZERS (Extended)
# ==========================================
class QuranReadingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuranReadingLog
        fields = ['id', 'date', 'surah', 'from_ayah', 'to_ayah', 'pages', 'minutes', 'reflection']


class MemorizationEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MemorizationEntry
        fields = ['id', 'surah', 'from_ayah', 'to_ayah', 'status', 'started_at', 'last_reviewed_at']


class RevisionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevisionLog
        fields = ['id', 'date', 'surah', 'quality', 'notes']


class AdhkarLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdhkarLog
        fields = ['id', 'date', 'morning', 'evening', 'after_prayer', 'istighfar_count']


class MissedFastSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissedFast
        fields = ['id', 'missed_on', 'reason', 'made_up_on']


# ==========================================
# HEALTH MODULE SERIALIZERS
# ==========================================
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'date', 'waist_cm', 'hips_cm', 'chest_cm', 'thigh_cm', 'arm_cm', 'notes']


class WeightLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightLog
        fields = ['id', 'date', 'weight_kg', 'notes']


class SleepLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepLog
        fields = ['id', 'date', 'hours', 'quality', 'notes']


class CycleLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CycleLog
        fields = ['id', 'start_date', 'end_date', 'symptoms', 'flow']


class HealthNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthNote
        fields = ['id', 'date', 'category', 'title', 'details']


# ==========================================
# LIBRARY MODULE SERIALIZERS
# ==========================================
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'total_pages', 'current_page', 'status', 'started_at', 'finished_at', 'rating', 'notes', 'series_name', 'expected_release_date']


class ReadingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingSession
        fields = ['id', 'book', 'date', 'pages_read', 'minutes']


# ==========================================
# PERFUMERY MODULE SERIALIZERS
# ==========================================
class PerfumeFormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfumeFormula
        fields = ['id', 'name', 'inspiration', 'created_at', 'archived']


class PerfumeVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfumeVersion
        fields = ['id', 'formula', 'version', 'date', 'unit', 'ingredients', 'observations', 'rating']


# ==========================================
# WEALTH MODULE SERIALIZERS
# ==========================================
class SavingsEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsEntry
        fields = ['id', 'date', 'amount', 'goal', 'note']


class SavingsGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsGoal
        fields = ['id', 'name', 'target_amount', 'target_date', 'created_at', 'completed_at']


class PurchasePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasePlan
        fields = ['id', 'name', 'price', 'priority', 'created_at', 'purchased_at', 'notes']


class WealthProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WealthProfile
        fields = ['id', 'currency', 'hourly_rate', 'monthly_savings_target']


# ==========================================
# LIFE MODULE SERIALIZERS
# ==========================================
class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = ['id', 'date', 'title', 'body', 'mood', 'gratitude']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'relationship', 'cadence_days', 'last_contacted_at', 'notes']


class CallReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallReminder
        fields = ['id', 'person', 'due_date', 'completed_at', 'note']


class TimelineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineEvent
        fields = ['id', 'date', 'title', 'category', 'description']