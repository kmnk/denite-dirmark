# add.py
"""
denite.nvim kind: add
"""

from denite.kind.directory import Kind as Directory
from denite.util import input

import dirmark.util as dm

class Kind(Directory):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'dirmark/add'

    def action_add(self, context):
        # TODO: implement multi target add logic
        default_group_name = dm.get_default_group(self.vim)
        group = input(self.vim, context,
                      prompt='Input group name [' + default_group_name + ']:',
                      text='')
        name = input(self.vim, context,
                     prompt='Input dirmark name:',
                     text='')

        if not group or group == '': group = default_group_name

        target = context['targets'][0]
        path = target['action__path']

        try:
            dirmark_dict = dm.read(self.vim)
        except FileNotFoundError:
            dirmark_dict = dm.new_dirmark_dict()

        group_dict = dirmark_dict['group'].setdefault(group, {
            "name": group,
            "dirmarks": [],
        })

        group_dict['dirmarks'].append({
            'name': name,
            'path': path,
        })
        dm.write(self.vim, dirmark_dict);

def main(): pass

if __name__ == '__main__': main()
