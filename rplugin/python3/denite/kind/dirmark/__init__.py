# __init__.py
"""
denite.nvim kind: dirmark
"""

from denite.kind.directory import Kind as Directory

import dirmark.util as dm

class Kind(Directory):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'dirmark'

    def action_lcd(self, context):
        target = context['targets'][0]
        self.vim.command('lcd {0}'.format(target['action__path']))

    def action_delete(self, context):
        # TODO: implement multi target delete logic
        target = context['targets'][0]
        group = target['action__group']
        name = target['action__name']

        try:
            dirmark_dict = dm.read(self.vim)
        except FileNotFoundError:
            # not to do
            return

        group_dict = dirmark_dict['group'].get(group, None)

        if not group_dict:
            # not to do
            return

        group_dict['dirmarks'] = [
            d for d in group_dict['dirmarks'] if d['name'] != name
        ]

        dm.write(self.vim, dirmark_dict)

def main(): pass

if __name__ == '__main__': main()
