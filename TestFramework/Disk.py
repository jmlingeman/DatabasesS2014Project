__author__ = 'jesse'


class Page:
    def __init__(self, size):
        self.data = []
        self.size = size
        self.reads = 0
        self.writes = 0

    def append(self, datum):
        self.reads += 1
        # if len(self.data) + 1 > self.size:
        #     return False
        # else:
        self.writes += 1
        self.data.append(datum)
        # return True

    def get(self):
        self.reads += 1
        return self.data

    def get_status(self):
        return "Page Reads: {0}, Page Writes: {1}".format(self.reads, self.writes)

    def isempty(self):
        if len(self.data) == 0:
            return True
        else:
            return False


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
        for i in range(self.size / self.page_size):
            self.pages.append(Page(self.page_size))

    def newPage(self):
        # self.reads += 1
        if len(self.pages) + 1 > self.size:
            return False
        else:
            # self.writes += 1
            p = Page(self.page_size)
            self.pages.append(p)
            return p

    def readPage(self, seq):
        pass

    def get_status(self):
        return "Reads: {0}, Writes: {1}".format(self.reads, self.writes)


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
        self.pages_per_block = self.page_size / self.block_size
        self.empty_pages = []
        for block in self.blocks:
            self.empty_pages += block.pages


    def get_status(self):
        # Print the status of this drive and its pages
        for block in self.blocks:
            print block.get_status()
            for page in block.pages:
                print page.get_status()


    def request_page(self):
        """
         Get an empty page from the disk, if available
        """
        # print self.empty_pages
        if len(self.empty_pages) == 0:
            # If full, create new block
            b = Block(self.block_size, self.page_size)
            self.blocks.append(b)
            self.empty_pages += b.pages

        p = self.empty_pages.pop()
        return p
