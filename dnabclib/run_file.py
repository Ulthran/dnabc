import gzip
import itertools

from .util import (
    parse_fastq, FastqRead,
    )

class IndexFastqSequenceFile(object):
    """Non-demultiplexed Illumina read data."""
    def __init__(self, fwd_fp, rev_fp, idx_fp):
        self.forward_filepath = fwd_fp
        self.reverse_filepath = rev_fp
        self.index_filepath = idx_fp

    def demultiplex(self, assigner, writer):
        idx_file = gzip.open(self.index_filepath, "rb")
        fwd_file = gzip.open(self.forward_filepath, "rb")
        rev_file = gzip.open(self.reverse_filepath, "rb")
        idxs = (FastqRead(x) for x in parse_fastq(idx_file))
        fwds = (FastqRead(x) for x in parse_fastq(fwd_file))
        revs = (FastqRead(x) for x in parse_fastq(rev_file))
        try:
            for idx, fwd, rev in itertools.izip(idxs, fwds, revs):
                sample = assigner.assign(idx)
                writer.write((fwd, rev), sample)
        finally:
            idx_file.close()
            fwd_file.close()
            rev_file.close()
        return assigner.read_counts
    
