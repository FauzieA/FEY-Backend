from rest_framework import viewsets, permissions
from .models import (
    CharacterProfile,
    WorkoutSession,
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
from .serializers import (
    CharacterProfileSerializer,
    WorkoutSessionSerializer,
    SalahLogSerializer,
    MemorizationLogSerializer,
    DhikrLogSerializer,
    XpEventSerializer,
    AchievementRecordSerializer,
    AppSettingsSerializer,
    PersonalRecordSerializer,
    WorkoutPlanSerializer,
    QuranReadingLogSerializer,
    MemorizationEntrySerializer,
    RevisionLogSerializer,
    AdhkarLogSerializer,
    MissedFastSerializer,
    MeasurementSerializer,
    WeightLogSerializer,
    SleepLogSerializer,
    CycleLogSerializer,
    HealthNoteSerializer,
    BookSerializer,
    ReadingSessionSerializer,
    PerfumeFormulaSerializer,
    PerfumeVersionSerializer,
    SavingsEntrySerializer,
    SavingsGoalSerializer,
    PurchasePlanSerializer,
    WealthProfileSerializer,
    JournalEntrySerializer,
    PersonSerializer,
    CallReminderSerializer,
    TimelineEventSerializer
)

class CharacterProfileViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CharacterProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkoutSessionViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkoutSession.objects.filter(user=self.request.user).order_by('-started_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SalahLogViewSet(viewsets.ModelViewSet):
    serializer_class = SalahLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SalahLog.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MemorizationLogViewSet(viewsets.ModelViewSet):
    serializer_class = MemorizationLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MemorizationLog.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DhikrLogViewSet(viewsets.ModelViewSet):
    serializer_class = DhikrLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DhikrLog.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ==========================================
# CHARACTER & GAMIFICATION VIEWSETS
# ==========================================
class XpEventViewSet(viewsets.ModelViewSet):
    serializer_class = XpEventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return XpEvent.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AchievementRecordViewSet(viewsets.ModelViewSet):
    serializer_class = AchievementRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AchievementRecord.objects.filter(user=self.request.user).order_by('-unlocked_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AppSettingsViewSet(viewsets.ModelViewSet):
    serializer_class = AppSettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AppSettings.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PersonalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PersonalRecord.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkoutPlanViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkoutPlan.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ==========================================
# FAITH MODULE VIEWSETS (Extended)
# ==========================================
class QuranReadingLogViewSet(viewsets.ModelViewSet):
    serializer_class = QuranReadingLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return QuranReadingLog.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MemorizationEntryViewSet(viewsets.ModelViewSet):
    serializer_class = MemorizationEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MemorizationEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RevisionLogViewSet(viewsets.ModelViewSet):
    serializer_class = RevisionLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RevisionLog.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdhkarLogViewSet(viewsets.ModelViewSet):
    serializer_class = AdhkarLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AdhkarLog.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MissedFastViewSet(viewsets.ModelViewSet):
    serializer_class = MissedFastSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MissedFast.objects.filter(user=self.request.user).order_by('-missed_on')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ==========================================
# HEALTH MODULE VIEWSETS
# ==========================================
class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Measurement.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WeightLogViewSet(viewsets.ModelViewSet):
    serializer_class = WeightLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WeightLog.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SleepLogViewSet(viewsets.ModelViewSet):
    serializer_class = SleepLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SleepLog.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CycleLogViewSet(viewsets.ModelViewSet):
    serializer_class = CycleLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CycleLog.objects.filter(user=self.request.user).order_by('-start_date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HealthNoteViewSet(viewsets.ModelViewSet):
    serializer_class = HealthNoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return HealthNote.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ==========================================
# LIBRARY MODULE VIEWSETS
# ==========================================
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReadingSessionViewSet(viewsets.ModelViewSet):
    serializer_class = ReadingSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ReadingSession.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ==========================================
# PERFUMERY MODULE VIEWSETS
# ==========================================
class PerfumeFormulaViewSet(viewsets.ModelViewSet):
    serializer_class = PerfumeFormulaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PerfumeFormula.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PerfumeVersionViewSet(viewsets.ModelViewSet):
    serializer_class = PerfumeVersionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PerfumeVersion.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ==========================================
# WEALTH MODULE VIEWSETS
# ==========================================
class SavingsEntryViewSet(viewsets.ModelViewSet):
    serializer_class = SavingsEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SavingsEntry.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SavingsGoalViewSet(viewsets.ModelViewSet):
    serializer_class = SavingsGoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SavingsGoal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PurchasePlanViewSet(viewsets.ModelViewSet):
    serializer_class = PurchasePlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PurchasePlan.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WealthProfileViewSet(viewsets.ModelViewSet):
    serializer_class = WealthProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WealthProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ==========================================
# LIFE MODULE VIEWSETS
# ==========================================
class JournalEntryViewSet(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Person.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CallReminderViewSet(viewsets.ModelViewSet):
    serializer_class = CallReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CallReminder.objects.filter(user=self.request.user).order_by('-due_date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TimelineEventViewSet(viewsets.ModelViewSet):
    serializer_class = TimelineEventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TimelineEvent.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)