# __init__.py
"""
denite.nvim source: dirmark
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from denite.source.base import Base

import dirmark.util as dm

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'dirmark'
        self.kind = 'dirmark'

    def gather_candidates(self, context):
        # TODO: get by comma separated group names
        group = context['args'][0] if len(context['args']) >= 1 else dm.get_default_group(self.vim)

        if not group or group == '':
            raise ValueError('group value is invalid:{}'.format(group))

        try:
            dirmark_dict = dm.read(self.vim)
        except FileNotFoundError:
            return []

        group_dict = dirmark_dict['group'].get(group, None)

        if not group_dict: return []

        return [{
            'word': v['name'],
            'action__name': v['name'],
            'action__group': group,
            'action__path': v['path'],
        } for v in group_dict['dirmarks']]

def main(): pass

if __name__ == '__main__': main()
