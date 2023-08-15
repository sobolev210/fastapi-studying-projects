#!/bin/bash
sleep 10 # waiting until postgres is running
alembic upgrade head
uvicorn app.main:app --host 0.0.0.0