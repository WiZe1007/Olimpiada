import urllib.request
import xml.etree.ElementTree as ET

# Download the XML file
url = "http://aiweb.cs.washington.edu/research/projects/xmltk/xmldata/data/pir/psd7003_pv.xml"
filename = "psd7003_pv.xml"
urllib.request.urlretrieve(url, filename)

# Parse the XML file
tree = ET.parse(filename)
root = tree.getroot()

# Find the unique refid values
refids = set()
for refinfo in root.findall(".//ProteinDatabase/ProteinEntry/reference/refinfo"):
    for refid in refinfo.findall("refid"):
        refids.add(refid.text)

# Sort and display the refids as a comma-separated list
refids_list = sorted(refids)
refids_csv = ",".join(refids_list)
print(refids_csv)

