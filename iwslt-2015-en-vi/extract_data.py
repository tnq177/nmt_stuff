from __future__ import print_function

from codecs import open
from itertools import izip
import xml.etree.ElementTree as ET
from lxml import html

def extract_dev(infile1, infile2, outfile1, outfile2):
    use_tags = ['description', 'title', 'seg']
    open(outfile1, 'w').close()
    open(outfile2, 'w').close()
    of1 = open(outfile1, 'w', 'utf-8')
    of2 = open(outfile2, 'w', 'utf-8')
    root1 = ET.parse(infile1).getroot()
    root2 = ET.parse(infile2).getroot()

    for tag in use_tags:
        tags_1 = root1.iter(tag)
        tags_2 = root2.iter(tag)

        assert sum(1 for _ in tags_1) == sum(1 for _ in tags_2)

        tags_1 = root1.iter(tag)
        tags_2 = root2.iter(tag)

        for t1, t2 in izip(tags_1, tags_2):
            if t1.tag == use_tags[-1]:
                assert t1.get('id') == t2.get('id')

            text1 = t1.text
            text2 = t2.text

            text1 = text1.strip()
            text2 = text2.strip()
            of1.write(text1 + '\n')
            of2.write(text2 + '\n')

    of1.close()
    of2.close()

def extract_train(infile1, infile2, outifle1, outfile2):
    use_tags = ['html', 'description', 'p']
    open(outifle1, 'w').close()
    open(outfile2, 'w').close()
    of1 = open(outifle1, 'w', 'utf-8')
    of2 = open(outfile2, 'w', 'utf-8')
    with open(infile1, 'r', 'utf-8') as if1, open(infile2, 'r', 'utf-8') as if2:
        for line1, line2 in izip(if1, if2):
            if line1.strip() and line2.strip():
                doc1 = html.fromstring(line1)
                doc2 = html.fromstring(line2)

                if doc1.tag not in use_tags or doc2.tag not in use_tags:
                    continue

                if doc1.tag != doc2.tag:
                    print(doc1.tag)
                    print(doc1.text_content())
                    print(doc2.tag)
                    print(doc2.text_content())
                assert doc1.tag == doc2.tag
                text1 = doc1.text_content()
                text2 = doc2.text_content()
                of1.write(text1)
                of2.write(text2)
    of1.close()
    of2.close()

if __name__ == '__main__':
    extract_train('./en-vi/train.tags.en-vi.en', './en-vi/train.tags.en-vi.vi', './en-vi/train.en-vi.en', './en-vi/train.en-vi.vi')
    extract_dev('./en-vi/IWSLT15.TED.dev2010.en-vi.en.xml', './en-vi/IWSLT15.TED.dev2010.en-vi.vi.xml', './en-vi/IWSLT15.TED.dev2010.en-vi.en', './en-vi/IWSLT15.TED.dev2010.en-vi.vi')
    extract_dev('./en-vi/IWSLT15.TED.tst2010.en-vi.en.xml', './en-vi/IWSLT15.TED.tst2010.en-vi.vi.xml', './en-vi/IWSLT15.TED.tst2010.en-vi.en', './en-vi/IWSLT15.TED.tst2010.en-vi.vi')
    extract_dev('./en-vi/IWSLT15.TED.tst2011.en-vi.en.xml', './en-vi/IWSLT15.TED.tst2011.en-vi.vi.xml', './en-vi/IWSLT15.TED.tst2011.en-vi.en', './en-vi/IWSLT15.TED.tst2011.en-vi.vi')
    extract_dev('./en-vi/IWSLT15.TED.tst2012.en-vi.en.xml', './en-vi/IWSLT15.TED.tst2012.en-vi.vi.xml', './en-vi/IWSLT15.TED.tst2012.en-vi.en', './en-vi/IWSLT15.TED.tst2012.en-vi.vi')
    extract_dev('./en-vi/IWSLT15.TED.tst2013.en-vi.en.xml', './en-vi/IWSLT15.TED.tst2013.en-vi.vi.xml', './en-vi/IWSLT15.TED.tst2013.en-vi.en', './en-vi/IWSLT15.TED.tst2013.en-vi.vi')
