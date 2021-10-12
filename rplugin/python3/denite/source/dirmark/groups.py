"""
denite.nvim source: groups
"""

import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)

import dirmark.util as dm
from denite.source.base import Base

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'dirmark/groups'
        self.kind = 'dirmark/groups'

    def gather_candidates(self, context):
        try:
            dirmark_dict = dm.read(self.vim)
        except FileNotFoundError:
            return []

        group_dict = dirmark_dict['group']

        return [
            {
                'word': group,
                'action__name': group,
                'action__default_action': context['args'][0] if len(context['args']) > 0 else ''
            }
            for group in group_dict.keys()
        ]

def main(): pass

if __name__ == '__main__': main()
