from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_convert_xpevent_id_to_uuid'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                CREATE EXTENSION IF NOT EXISTS pgcrypto;

                ALTER TABLE api_workoutsession
                ADD COLUMN new_id uuid NOT NULL DEFAULT gen_random_uuid();

                ALTER TABLE api_sessionexercise
                ADD COLUMN new_session_id uuid;

                UPDATE api_sessionexercise
                SET new_session_id = w.new_id
                FROM api_workoutsession w
                WHERE api_sessionexercise.session_id = w.id;

                DO $$
                DECLARE
                    r RECORD;
                BEGIN
                    FOR r IN
                        SELECT conname
                        FROM pg_constraint
                        JOIN pg_class ON pg_constraint.conrelid = pg_class.oid
                        WHERE contype = 'f'
                        AND pg_class.relname = 'api_sessionexercise'
                        AND confrelid = 'api_workoutsession'::regclass
                    LOOP
                        EXECUTE format('ALTER TABLE api_sessionexercise DROP CONSTRAINT %I', r.conname);
                    END LOOP;
                END;
                $$;

                ALTER TABLE api_workoutsession
                DROP CONSTRAINT IF EXISTS api_workoutsession_pkey;

                ALTER TABLE api_sessionexercise
                DROP COLUMN session_id;

                ALTER TABLE api_workoutsession
                DROP COLUMN id;

                ALTER TABLE api_sessionexercise
                RENAME COLUMN new_session_id TO session_id;

                ALTER TABLE api_workoutsession
                RENAME COLUMN new_id TO id;

                ALTER TABLE api_workoutsession
                ADD PRIMARY KEY (id);

                ALTER TABLE api_sessionexercise
                ADD CONSTRAINT api_sessionexercise_session_id_fkey
                FOREIGN KEY (session_id)
                REFERENCES api_workoutsession(id)
                ON DELETE CASCADE;
            """
        ),
    ]
