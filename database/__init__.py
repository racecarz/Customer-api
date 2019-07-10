#!/usr/bin/env python3
""" Database module

This module is used for database initialization of Flask
SQL Alchemy
"""
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy


__session_options = {'autocommit':True}
__engine_options = {'isolation_level':'READ COMMITTED'}

db = SQLAlchemy(session_options=__session_options)
