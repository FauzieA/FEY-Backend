from django.test import TestCase
from unittest.mock import Mock

from .serializers import WorkoutSessionSerializer


class WorkoutSessionSerializerTests(TestCase):
    def test_create_accepts_anonymous_request_without_auth(self):
        data = {
            'plan_id': 'plan-1',
            'plan_title': 'Upper Body',
            'completed_at': '2026-08-04T12:00:00Z',
            'duration_minutes': 45,
            'completed': True,
            'exercises': [
                {
                    'exercise_id': 'bench_press',
                    'exercise_name': 'Bench Press',
                    'sets': [
                        {'set_num': 1, 'reps': 10, 'weight_kg': 20, 'completed': True},
                    ],
                }
            ],
        }

        serializer = WorkoutSessionSerializer(
            data=data,
            context={'request': Mock(user=None)},
        )

        self.assertTrue(serializer.is_valid(), serializer.errors)
        instance = serializer.save()

        self.assertEqual(instance.plan_title, 'Upper Body')
        self.assertEqual(instance.exercises.count(), 1)
        self.assertEqual(instance.exercises.first().sets.count(), 1)
