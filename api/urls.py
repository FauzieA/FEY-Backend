from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CharacterProfileViewSet,
    WorkoutSessionViewSet,
    SalahLogViewSet,
    MemorizationLogViewSet,
    DhikrLogViewSet,
    XpEventViewSet,
    AchievementRecordViewSet,
    AppSettingsViewSet,
    PersonalRecordViewSet,
    WorkoutPlanViewSet,
    QuranReadingLogViewSet,
    MemorizationEntryViewSet,
    RevisionLogViewSet,
    AdhkarLogViewSet,
    MissedFastViewSet,
    MeasurementViewSet,
    WeightLogViewSet,
    SleepLogViewSet,
    CycleLogViewSet,
    HealthNoteViewSet,
    BookViewSet,
    ReadingSessionViewSet,
    PerfumeFormulaViewSet,
    PerfumeVersionViewSet,
    SavingsEntryViewSet,
    SavingsGoalViewSet,
    PurchasePlanViewSet,
    DebtViewSet,
    WealthProfileViewSet,
    JournalEntryViewSet,
    PersonViewSet,
    CallReminderViewSet,
    TimelineEventViewSet
)

router = DefaultRouter()
router.register(r'profile', CharacterProfileViewSet, basename='profile')
router.register(r'workouts', WorkoutSessionViewSet, basename='workouts')
router.register(r'salah', SalahLogViewSet, basename='salah')
router.register(r'memorization', MemorizationLogViewSet, basename='memorization')
router.register(r'dhikr', DhikrLogViewSet, basename='dhikr')

# Character & Gamification
router.register(r'xp-events', XpEventViewSet, basename='xp-events')
router.register(r'achievements', AchievementRecordViewSet, basename='achievements')
router.register(r'settings', AppSettingsViewSet, basename='settings')
router.register(r'personal-records', PersonalRecordViewSet, basename='personal-records')
router.register(r'workout-plans', WorkoutPlanViewSet, basename='workout-plans')

# Faith Module (Extended)
router.register(r'quran-reading', QuranReadingLogViewSet, basename='quran-reading')
router.register(r'memorization-entries', MemorizationEntryViewSet, basename='memorization-entries')
router.register(r'revisions', RevisionLogViewSet, basename='revisions')
router.register(r'adhkar', AdhkarLogViewSet, basename='adhkar')
router.register(r'missed-fasts', MissedFastViewSet, basename='missed-fasts')

# Health Module
router.register(r'measurements', MeasurementViewSet, basename='measurements')
router.register(r'weight-logs', WeightLogViewSet, basename='weight-logs')
router.register(r'sleep-logs', SleepLogViewSet, basename='sleep-logs')
router.register(r'cycle-logs', CycleLogViewSet, basename='cycle-logs')
router.register(r'health-notes', HealthNoteViewSet, basename='health-notes')

# Library Module
router.register(r'books', BookViewSet, basename='books')
router.register(r'reading-sessions', ReadingSessionViewSet, basename='reading-sessions')

# Perfumery Module
router.register(r'perfume-formulas', PerfumeFormulaViewSet, basename='perfume-formulas')
router.register(r'perfume-versions', PerfumeVersionViewSet, basename='perfume-versions')

# Wealth Module
router.register(r'savings-entries', SavingsEntryViewSet, basename='savings-entries')
router.register(r'savings-goals', SavingsGoalViewSet, basename='savings-goals')
router.register(r'purchase-plans', PurchasePlanViewSet, basename='purchase-plans')
router.register(r'debts', DebtViewSet, basename='debts')
router.register(r'wealth-profile', WealthProfileViewSet, basename='wealth-profile')

# Life Module
router.register(r'journal-entries', JournalEntryViewSet, basename='journal-entries')
router.register(r'people', PersonViewSet, basename='people')
router.register(r'call-reminders', CallReminderViewSet, basename='call-reminders')
router.register(r'timeline-events', TimelineEventViewSet, basename='timeline-events')

urlpatterns = [
    path('', include(router.urls)),
]