#!/usr/bin/bash
sudo mysql -u root -p < create_db.sql
sudo mysql -u root -p < create_table.sql
# mkdir polls
# python manage.py inspectdb > polls/models.py
# The admin password is set to "adminPassword123", do NOT use this password in practice.
