"""wikitext - Do you need a lot of text  for whatever reason? Wikitext provides you with a plain text stream coming directly from Wikipedia in any of its supporting languages."""

from .plainstream import get_text, available_languages

__version__ = '0.1.0'
__author__ = 'Jimmy Callin <jimmy.callin@gmail.com>'
__all__ = ['get_text', 'available_languages']