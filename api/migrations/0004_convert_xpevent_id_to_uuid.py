from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_add_missing_fields'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                CREATE EXTENSION IF NOT EXISTS pgcrypto;
                ALTER TABLE api_xpevent ADD COLUMN new_id uuid NOT NULL DEFAULT gen_random_uuid();
                ALTER TABLE api_xpevent DROP CONSTRAINT api_xpevent_pkey;
                ALTER TABLE api_xpevent DROP COLUMN id;
                ALTER TABLE api_xpevent RENAME COLUMN new_id TO id;
                ALTER TABLE api_xpevent ADD PRIMARY KEY (id);
            """,
            reverse_sql="""
                ALTER TABLE api_xpevent DROP CONSTRAINT api_xpevent_pkey;
                ALTER TABLE api_xpevent ADD COLUMN id integer;
                ALTER TABLE api_xpevent DROP COLUMN new_id;
                ALTER TABLE api_xpevent ADD PRIMARY KEY (id);
            """,
        ),
    ]
