from django.db import migrations


def convert_to_uuid(apps, schema_editor):
    cursor = schema_editor.connection.cursor()
    cursor.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")

    tables = [
        'api_quranreadinglog',
        'api_revisionlog',
        'api_adhkarlog',
        'api_missedfast',
        'api_measurement',
        'api_weightlog',
        'api_sleeplog',
        'api_cyclelog',
        'api_healthnote',
        'api_book',
        'api_readingsession',
        'api_perfumeformula',
        'api_perfumeversion',
        'api_savingsentry',
        'api_savingsgoal',
        'api_purchaseplan',
        'api_wealthprofile',
        'api_journalentry',
        'api_person',
        'api_callreminder',
        'api_timelinesevent',
    ]

    for table in tables:
        try:
            cursor.execute(
                "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' AND table_name = %s)",
                [table],
            )
            if not cursor.fetchone()[0]:
                continue

            cursor.execute(
                "SELECT data_type FROM information_schema.columns WHERE table_schema = 'public' AND table_name = %s AND column_name = 'id'",
                [table],
            )
            row = cursor.fetchone()
            if not row:
                continue

            if row[0] and row[0].lower() == 'uuid':
                continue

            cursor.execute(
                f"""
                DO $$
                BEGIN
                    IF EXISTS (
                        SELECT 1
                        FROM information_schema.columns
                        WHERE table_schema = 'public'
                          AND table_name = '{table}'
                          AND column_name = 'id'
                    )
                    AND NOT EXISTS (
                        SELECT 1
                        FROM information_schema.columns
                        WHERE table_schema = 'public'
                          AND table_name = '{table}'
                          AND column_name = 'id'
                          AND data_type = 'uuid'
                    ) THEN
                        ALTER TABLE {table} ALTER COLUMN id TYPE uuid USING gen_random_uuid();
                    END IF;
                EXCEPTION WHEN OTHERS THEN
                    RAISE NOTICE 'Skipped UUID conversion for {table}';
                END $$;
                """
            )
        except Exception:
            # Ignore table-level failures so the migration can continue safely.
            continue


def reverse_code(apps, schema_editor):
    return None


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0008_convert_memorizationentry_id_to_uuid'),
    ]

    operations = [
        migrations.RunPython(convert_to_uuid, reverse_code),
    ]
