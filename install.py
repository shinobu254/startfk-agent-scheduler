import neko

if not neko.is_installed("sqlalchemy"):
    neko.run_pip("install sqlalchemy", "requirement for task-scheduler")
