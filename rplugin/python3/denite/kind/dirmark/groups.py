# groups.py
"""
denite.nvim kind: groups
"""
import os

from denite.kind.base import Base

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'dirmark/groups'
        self.default_action = 'run'

    def action_run(self, context):
        target = context['targets'][0]
        context['sources_queue'].append([
            {'name': 'dirmark', 'args': [target['action__name']]},
        ])
        if target['action__default_action'] != '': context['default_action'] = target['action__default_action']

def main(): pass

if __name__ == '__main__': main()
