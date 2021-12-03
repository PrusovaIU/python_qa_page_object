#!/bin/bash
pytest tests "${@}"
python allure_send_results.py