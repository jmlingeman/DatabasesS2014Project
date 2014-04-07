__author__ = 'jesse'


class Page:
    def __init__(self, size):
        self.data = []
        self.size = size
        self.reads = 0
        self.writes = 0

    def append(self, datum):
        self.reads += 1
        if len(self.data) + 1 > self.size:
            return False
        else:
            self.writes += 1
            self.data.append(datum)
            return True

    def get(self):
        self.reads += 1
        return self.data


class Block:
    def __init__(self, size, page_size):
        self.size = size
        self.page_size = page_size
        self.reads = 0
        self.writes = 0

        self.random_reads = 0
        self.seq_reads = 0

        # Initialize the number of pages that this block can contain
        self.pages = []

    def newPage(self):
        self.reads += 1
        if len(self.pages) + 1 > self.size:
            return False
        else:
            self.writes += 1
            self.pages.append(Page(self.page_size))
            return True

    def readPage(self, seq):
        pass


class Disk:
    """
    Class to keep track of the blocks we are using for our methods.
    Initialize with number of blocks, block size, and page size
    """

    def __init__(self, n_blocks, block_size, page_size):
        self.n_blocks = n_blocks
        self.block_size = block_size
        self.page_size = page_size
        self.blocks = []

        self.last_written_block = None

        # Initialize the blocks for this drive configuration
        for i in range(n_blocks):
            self.blocks.append(Block(block_size, page_size))

            # And now we have a hard drive!

    def put(self, data):
        """
        Puts data into the next available slot on the hard disk
        """

