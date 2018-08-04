# add.py
"""
denite.nvim source: add
"""

from denite.source.directory_rec import Source as DirectoryRec

class Source(DirectoryRec):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'dirmark/add'
        self.kind = 'dirmark/add'

    def gather_candidates(self, context):
        candidates = super().gather_candidates(context)

        if not candidates: return candidates

        return candidates

def main(): pass

if __name__ == '__main__': main()
