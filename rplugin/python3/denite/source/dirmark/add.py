# add.py
"""
denite.nvim source: add
"""

from denite.source.file import Source as File

class Source(File):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'dirmark/add'
        self.kind = 'dirmark/add'

    def gather_candidates(self, context):
        candidates = [c for c in super().gather_candidates(context)
                      if c['kind'] == 'directory']

        if not candidates: return candidates

        return candidates

def main(): pass

if __name__ == '__main__': main()
