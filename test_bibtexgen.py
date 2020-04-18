from bibtexgen import bibtex


def test_referencegen_sanity():
    b = bibtex()
    r = b.generate_references('6258b37b8d517f121c844ebad226da472761adc6')
    assert(len(r) == 8)
