#!/bin/bash

echo "Starting the duma server..."
uvicorn src.duma.api_service.simulation_service:app --host 127.0.0.1 --port 8001
