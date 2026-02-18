# Batch Processing Method for Json Files in Separate Folders

**Topic ID**: 37335
**Date**: 2024-07-12
**URL**: https://discourse.slicer.org/t/batch-processing-method-for-json-files-in-separate-folders/37335

---

## Post #1 by @griffinfi (2024-07-12 14:51 UTC)

<p>Operating system: MacOS 15.0, Apple M3, RAM 16 GB<br>
Slicer version: macOS 5.6.2</p>
<p>Hi all,</p>
<p>I have been using slicer to segment two facial muscles on individual nrrd files   exported from CT scans. I have measured each muscle with curves using the Markup tool, and have kept them in individual folders (Folder 1 = 1.nrrd, 1.segmentation-1.nrrd, 1.segmentation-2.nrrd, curves.json). I now aim to record the lengths of all curves measured. However, I have 600 curves to obtain length data from. (100 files, 6 curves per file).</p>
<p>Is there a batch processing method to do this? Or in the least, export a CSV file per folder? My final goal is to congregate all datapoints into one CSV file. I am new to slicer .</p>
<p>Thank you in advance!</p>

---

## Post #2 by @smrolfe (2024-07-12 18:12 UTC)

<p>Following <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-a-table-of-control-point-labels-and-positions" rel="noopener nofollow ugc">this example in the python script repo</a>, you can get the length from the curve filename using:</p>
<pre><code class="lang-auto">pip_install("pandas")
import pandas as pd
length = pd.DataFrame.from_dict(pd.read_json("your_json_path"))['markups'][0]['measurements'][0]['value']
</code></pre>
<p>This will work if you already have the curve length in the JSON file. If you don’t have this, I can follow up with some pointers on automating this.</p>

---

## Post #3 by @griffinfi (2024-07-13 15:08 UTC)

<p>Thank you so much for your help! Success!</p>

---
