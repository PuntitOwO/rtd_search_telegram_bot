"""Configuration file"""

# Don't change this one
URL = "https://readthedocs.org/api/v3/search/"
"""API URL endpoint to request to."""

# Change these
PROJECT = "godot"
"""
Read The Docs project id for search filtering.

Will be added to search query as "project:<PROJECT>", see
https://docs.readthedocs.io/en/stable/server-side-search/syntax.html
"""

DEFAULT_URL = "https://docs.godotengine.org/"
"""
URL of the answer for an empty or too short inline query.

This will be used if the query text has 2 or less characters.
"""
DEFAULT_TEXT = "Godot Docs"
"""
Text of the answer for inline queries.

This will be used as the answer text like "[DEFAULT_TEXT](DEFAULT_URL)" if the
query text has 2 or less characters, or as "DEFAULT_TEXT: [<title>](<url>)" if
the query text has 3 or more characters and there is a search result.
"""