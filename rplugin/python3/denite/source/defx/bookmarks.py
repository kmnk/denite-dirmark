import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)

if True:
    import dirmark.util as dm
    from denite.source.base import Base


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'defx/bookmarks'
        self.kind = 'command'

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
                'word': v['name'],
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
