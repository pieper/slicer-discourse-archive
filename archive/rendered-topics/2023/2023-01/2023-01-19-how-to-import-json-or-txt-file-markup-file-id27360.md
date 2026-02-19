---
topic_id: 27360
title: "How To Import Json Or Txt File Markup File"
date: 2023-01-19
url: https://discourse.slicer.org/t/27360
---

# How to import .json or .txt file markup file

**Topic ID**: 27360
**Date**: 2023-01-19
**URL**: https://discourse.slicer.org/t/how-to-import-json-or-txt-file-markup-file/27360

---

## Post #1 by @Kae1 (2023-01-19 18:02 UTC)

<p>Hi there. How do you import a .json or .txt file to use as a markup file?<br>
I am quite new to Slicer, so a simple clear answer would be much appreciated.</p>
<p>When I drag and drop the json or txt file into Slicer, or else go through the load data button in Slicer, I get a ‘failed to load’ error message.</p>
<p>This file is a simple .txt file with four columns representing the label and x, y, z coordinates for a range of electrodes to be used with/superimposed on a brain CT scan.</p>
<p>The json file is created simply by changing the file type manually from .txt to .json.<br>
I don’t mind whether I used the .txt or the .json file. My whole aim here is simply to import these x,y,z electrode coordinates rather than create the markup file manually inside 3dSlicer.</p>
<p>Any help much appreciated.</p>
<p>Kae</p>

---

## Post #2 by @mau_igna_06 (2023-01-19 18:26 UTC)

<p>Hi</p>
<p>I think you may need to edit your file according to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups" rel="noopener nofollow ugc">this documentation</a></p>
<p>Hope it helps</p>

---

## Post #3 by @Kae1 (2023-01-24 04:59 UTC)

<p>Thanks for this. I have re written my electrode position markup file in the format suggested for a .json file. This markup file successfully loads into Slicer on Windows, but not on Slicer on my Mac.<br>
Any suggestions?</p>
<p>The following is an abbreviation of the script used:</p>
<p>{“<span class="mention">@schema</span>”: “<a href="https://raw.githubusercontent.com/Slicer/Slicer/main/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.0.json#" rel="noopener nofollow ugc">https://raw.githubusercontent.com/Slicer/Slicer/main/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.0.json#</a>”,<br>
“markups”: [{“type”: “Fiducial”, “coordinateSystem”: “LPS”, “controlPoints”: [<br>
{ “label”: “A”, “position”: [ 230.000000 , 255.000000 , 173.000000 ]},<br>
{ “label”: “A1”, “position”: [ 254.000000 , 250.000000 , 131.000000 ]},<br>
{ “label”: “B”, “position”: [ 281.000000 , 250.000000 , 177.000000 ]},<br>
{ “label”: “B1”, “position”: [ 264.000000 , 249.000000 , 133.000000 ]},<br>
]}]}</p>

---

## Post #4 by @mau_igna_06 (2023-01-24 20:51 UTC)

<p>you should be able to test if your file or string is json-valid using:</p>
<pre><code class="lang-auto">import json
dataDictionary = json.loads(yourString)
print(dataDictionary)
</code></pre>
<p>Please check the json module python documentation. A json markups file should be valid in any OS. Also you could create some fiducials with Slicer GUI as test data, save it and open the file on a text editor to see where the error is compared with the file you crafted</p>
<p>Hope it helps</p>

---
