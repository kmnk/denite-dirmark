import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)

import dirmark.util as dm
from denite.source.base import Base

BOOKMARKS_HIGHLIGHT_SYNTAX = [
    {'name': 'bm_name', 'link': 'Keyword', 're': r'^\[.*\]\ze\s'}
]


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'defx/bookmarks'
        self.kind = 'command'

    def highlight(self):
        for syn in BOOKMARKS_HIGHLIGHT_SYNTAX:
            self.vim.command(
                'syntax match {0}_{1} /{2}/ contained containedin={0}'.format(
                    self.syntax_name, syn['name'], syn['re']
                )
            )
            self.vim.command(
                'highlight default link {0}_{1} {2}'.format(
                    self.syntax_name, syn['name'], syn['link']
                )
            )

    def gather_candidates(self, context):
        # TODO: get by comma separated group names
        group = (
            context['args'][0]
            if len(context['args']) >= 1
            else dm.get_default_group(self.vim)
        )

        if not group or group == '':
            raise ValueError(f'Group value is invalid: {group}')

        try:
            dirmark_dict = dm.read(self.vim)
        except FileNotFoundError:
            return []

        group_dict = dirmark_dict['group'].get(group, None)

        if not group_dict:
            return []

        return [
            {
                'word': f"[{v['name']}] {v['path']}",
                'action__name': v['name'],
                'action__group': group,
                'action__command': f"call defx#call_action('cd', ['{v['path']}'])",
            }
            for v in group_dict['dirmarks']
        ]


def main():
    pass


if __name__ == '__main__':
    main()
