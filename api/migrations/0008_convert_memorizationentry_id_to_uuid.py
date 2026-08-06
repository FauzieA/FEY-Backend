from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_convert_salahlog_id_to_uuid'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                CREATE EXTENSION IF NOT EXISTS pgcrypto;

                ALTER TABLE api_memorizationentry
                ADD COLUMN IF NOT EXISTS new_id uuid NOT NULL DEFAULT gen_random_uuid();

                ALTER TABLE api_memorizationentry
                DROP CONSTRAINT IF EXISTS api_memorizationentry_pkey;

                ALTER TABLE api_memorizationentry
                DROP COLUMN IF EXISTS id;

                ALTER TABLE api_memorizationentry
                RENAME COLUMN new_id TO id;

                ALTER TABLE api_memorizationentry
                ADD PRIMARY KEY (id);
            """,
            reverse_sql="""
                ALTER TABLE api_memorizationentry
                DROP CONSTRAINT IF EXISTS api_memorizationentry_pkey;

                ALTER TABLE api_memorizationentry
                ADD COLUMN IF NOT EXISTS id integer;

                ALTER TABLE api_memorizationentry
                DROP COLUMN IF EXISTS new_id;

                ALTER TABLE api_memorizationentry
                ADD PRIMARY KEY (id);
            """,
        ),
    ]
