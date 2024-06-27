# This file is used by Alembic to run migrations.
from backend.app import app, db
import os
from sqlalchemy import engine_from_config, pool

config = app.config
config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL'))

target_metadata = db.metadata

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = db.engine
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
