import subprocess
import re
from pathlib import Path
from typing import Optional

def download_dataset(type: bool, subtype: Optional[str] = None, size: Optional[str] = None):
    website = "https://pizzachili.dcc.uchile.cl/texts/"
    website_copy = website
    all_subtypes = ["sources", "pitches", "proteins", "dna", "english", "dblp.xml"]
    website_subtypes = ["code", "music", "protein", "dna", "nlang", "xml"]
    sizes = ["50MB", "100MB", "200MB"]
    extractions = []
    
    if type and (subtype in all_subtypes or not subtype):
        if size not in sizes and size:
            print("Size not given.")
            return 0

        if size:
            size = "." + size
        else:
            size = ""
        if not subtype:
            for k in all_subtypes:
                website_suffix = website_subtypes[all_subtypes.index(k)]
                website += website_suffix + "/" + k + size + ".gz"
                extractions.append(website)
                website = website_copy
        else:
            website_suffix = website_subtypes[all_subtypes.index(subtype)]
            website += website_suffix + "/" + subtype + size + ".gz"
            extractions.append(website)

        for link in extractions:
            file_path = re.search(r'([^\/]+$)', link).group()
            command = ["curl", link, "--output", file_path]
            print("Extracting from " + link + "...")
                                
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("Done. Size of file: " + str(Path(file_path).stat().st_size * 1e-6) + "\n---\n")
    else:
        return 0