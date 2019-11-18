# add.py
"""
denite.nvim kind: add
"""
import os

from denite.kind.directory import Kind as Directory

import dirmark.util as dm

class Kind(Directory):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'dirmark/add'
        self.default_action = 'narrow'

    def action_narrow(self, context):
        target = context['targets'][0]
        context['sources_queue'].append([
            {'name': 'dirmark/add', 'args': []},
        ])
        context['path'] = target['action__path']

    def action_wide(self, context):
        target = context['targets'][0]
        context['sources_queue'].append([
            {'name': 'dirmark/add', 'args': []},
        ])
        context['path'] = os.path.dirname(os.path.dirname(target['action__path']))

    def action_add(self, context):
        # TODO: implement multi target add logic
        default_group_name = dm.get_default_group(self.vim)
        group = str(self.vim.call('denite#util#input',
                                  'Input group name [' + default_group_name + ']:',
                                  '',
                                  ''))
        name = str(self.vim.call('denite#util#input',
                                 'Input dirmark name:',
                                 '',
                                 ''))

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
