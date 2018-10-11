import xml.etree.ElementTree as ET
from glob import glob

fnames = glob('output/*/**.xml') + glob('output/*.xml')

for fname in fnames:
    tree = ET.parse(fname)
    tree.write(fname)
