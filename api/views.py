from django.http import Http404
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
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
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return CharacterProfile.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class WorkoutSessionViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSessionSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

    def get_queryset(self):
        return WorkoutSession.objects.all().order_by('-started_at')

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        # Support upsert via PUT
        try:
            return super().update(request, *args, **kwargs)
        except (WorkoutSession.DoesNotExist, Http404, NotFound):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SalahLogViewSet(viewsets.ModelViewSet):
    serializer_class = SalahLogSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return SalahLog.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()


class MemorizationLogViewSet(viewsets.ModelViewSet):
    serializer_class = MemorizationLogSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return MemorizationLog.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class DhikrLogViewSet(viewsets.ModelViewSet):
    serializer_class = DhikrLogSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return DhikrLog.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()


# ==========================================
# CHARACTER & GAMIFICATION VIEWSETS
# ==========================================
class XpEventViewSet(viewsets.ModelViewSet):
    serializer_class = XpEventSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

    def get_queryset(self):
        return XpEvent.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        # Support upsert via PUT
        try:
            return super().update(request, *args, **kwargs)
        except (XpEvent.DoesNotExist, Http404, NotFound):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AchievementRecordViewSet(viewsets.ModelViewSet):
    serializer_class = AchievementRecordSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return AchievementRecord.objects.all().order_by('-unlocked_at')

    def perform_create(self, serializer):
        serializer.save()


class AppSettingsViewSet(viewsets.ModelViewSet):
    serializer_class = AppSettingsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return AppSettings.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class PersonalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalRecordSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

    def get_queryset(self):
        return PersonalRecord.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        # Support upsert via PUT
        try:
            return super().update(request, *args, **kwargs)
        except (PersonalRecord.DoesNotExist, Http404, NotFound):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class WorkoutPlanViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return WorkoutPlan.objects.all()

    def perform_create(self, serializer):
        serializer.save()


# ==========================================
# FAITH MODULE VIEWSETS (Extended)
# ==========================================
class QuranReadingLogViewSet(viewsets.ModelViewSet):
    serializer_class = QuranReadingLogSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return QuranReadingLog.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()


class MemorizationEntryViewSet(viewsets.ModelViewSet):
    serializer_class = MemorizationEntrySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return MemorizationEntry.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class RevisionLogViewSet(viewsets.ModelViewSet):
    serializer_class = RevisionLogSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return RevisionLog.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()


class AdhkarLogViewSet(viewsets.ModelViewSet):
    serializer_class = AdhkarLogSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return AdhkarLog.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()


class MissedFastViewSet(viewsets.ModelViewSet):
    serializer_class = MissedFastSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return MissedFast.objects.all().order_by('-missed_on')

    def perform_create(self, serializer):
        serializer.save()


# ==========================================
# HEALTH MODULE VIEWSETS
# ==========================================
class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Measurement.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()


class WeightLogViewSet(viewsets.ModelViewSet):
    serializer_class = WeightLogSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return WeightLog.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()


class SleepLogViewSet(viewsets.ModelViewSet):
    serializer_class = SleepLogSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return SleepLog.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()


class CycleLogViewSet(viewsets.ModelViewSet):
    serializer_class = CycleLogSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return CycleLog.objects.all().order_by('-start_date')

    def perform_create(self, serializer):
        serializer.save()


class HealthNoteViewSet(viewsets.ModelViewSet):
    serializer_class = HealthNoteSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return HealthNote.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()


# ==========================================
# LIBRARY MODULE VIEWSETS
# ==========================================
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Book.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class ReadingSessionViewSet(viewsets.ModelViewSet):
    serializer_class = ReadingSessionSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return ReadingSession.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()


# ==========================================
# PERFUMERY MODULE VIEWSETS
# ==========================================
class PerfumeFormulaViewSet(viewsets.ModelViewSet):
    serializer_class = PerfumeFormulaSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return PerfumeFormula.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class PerfumeVersionViewSet(viewsets.ModelViewSet):
    serializer_class = PerfumeVersionSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return PerfumeVersion.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()


# ==========================================
# WEALTH MODULE VIEWSETS
# ==========================================
class SavingsEntryViewSet(viewsets.ModelViewSet):
    serializer_class = SavingsEntrySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return SavingsEntry.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()


class SavingsGoalViewSet(viewsets.ModelViewSet):
    serializer_class = SavingsGoalSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return SavingsGoal.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class PurchasePlanViewSet(viewsets.ModelViewSet):
    serializer_class = PurchasePlanSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return PurchasePlan.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save()


class WealthProfileViewSet(viewsets.ModelViewSet):
    serializer_class = WealthProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return WealthProfile.objects.all()

    def perform_create(self, serializer):
        serializer.save()


# ==========================================
# LIFE MODULE VIEWSETS
# ==========================================
class JournalEntryViewSet(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return JournalEntry.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Person.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class CallReminderViewSet(viewsets.ModelViewSet):
    serializer_class = CallReminderSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return CallReminder.objects.all().order_by('-due_date')

    def perform_create(self, serializer):
        serializer.save()


class TimelineEventViewSet(viewsets.ModelViewSet):
    serializer_class = TimelineEventSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return TimelineEvent.objects.all().order_by('-date')

    def perform_create(self, serializer):
        serializer.save()