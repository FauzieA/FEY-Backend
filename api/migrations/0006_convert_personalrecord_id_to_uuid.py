from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_convert_workoutsession_id_to_uuid'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                CREATE EXTENSION IF NOT EXISTS pgcrypto;

                ALTER TABLE api_personalrecord
                ADD COLUMN IF NOT EXISTS new_id uuid NOT NULL DEFAULT gen_random_uuid();

                ALTER TABLE api_personalrecord
                DROP CONSTRAINT IF EXISTS api_personalrecord_pkey;

                ALTER TABLE api_personalrecord
                DROP COLUMN IF EXISTS id;

                ALTER TABLE api_personalrecord
                RENAME COLUMN new_id TO id;

                ALTER TABLE api_personalrecord
                ADD PRIMARY KEY (id);
            """,
            reverse_sql="""
                ALTER TABLE api_personalrecord
                DROP CONSTRAINT IF EXISTS api_personalrecord_pkey;

                ALTER TABLE api_personalrecord
                ADD COLUMN IF NOT EXISTS id integer;

                ALTER TABLE api_personalrecord
                DROP COLUMN IF EXISTS new_id;

                ALTER TABLE api_personalrecord
                ADD PRIMARY KEY (id);
            """,
        ),
    ]
