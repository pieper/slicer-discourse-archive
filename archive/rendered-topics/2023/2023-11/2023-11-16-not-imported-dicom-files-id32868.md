---
topic_id: 32868
title: "Not Imported Dicom Files"
date: 2023-11-16
url: https://discourse.slicer.org/t/32868
---

# Not imported DICOM files

**Topic ID**: 32868
**Date**: 2023-11-16
**URL**: https://discourse.slicer.org/t/not-imported-dicom-files/32868

---

## Post #1 by @luarpy (2023-11-16 23:40 UTC)

<p>Hello<br>
I could see that Slicer for Linux is not able to load all the DICOM files present in a folder. I have checked the following checks:</p>
<ul>
<li>Files exist: yes</li>
<li>Slicer for Windows loads them: yes</li>
<li>The files contain data: yes</li>
<li>Are errors or warnings during import: no</li>
</ul>
<p>What could be the steps to follow? What else should I check?<br>
Any help is appreciated!</p>

---

## Post #2 by @pieper (2023-11-16 23:43 UTC)

<p>Perhaps narrow down to two files, one that loads and one that doesn’t and inspect what’s possibly different about them.</p>

---

## Post #3 by @luarpy (2023-11-17 18:23 UTC)

<p>Do you mean internally, all the DICOM tags?</p>

---

## Post #4 by @pieper (2023-11-17 19:04 UTC)

<p>Probably not the dicom tags if the files load correctly on windows, but maybe something about the file path or permissions.  It’s hard to think of any reason two versions of slicer would treat the same dicom files differently.</p>

---

## Post #5 by @luarpy (2023-11-30 18:41 UTC)

<p>I have noticed that files are missing when Slicer loads a folder with DICOM content.<br>
I wanted to share this simple script to generate a CSV file to check name by name which files are missing from the list in Slicer:</p>
<pre data-code-wrap="python"><code class="lang-python">import pydicom
import sys
import csv
import os

from os import listdir
from os.path import join,isfile

def main():
    input_dir = sys.argv[1]
    output_file = sys.argv[2]
    ds_dict = {               
                "PatientID": None,       
                "FileName": None,
                "SeriesNumber": None,     
                "SeriesDescription": None,
                "Modality": None}      
    input_dir = os.path.abspath(input_dir)

    with open(output_file, 'a') as f:
        w = csv.DictWriter(f, ds_dict.keys())
        w.writeheader()
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                file_abspath = os.path.join(input_dir, file)
                if file_abspath.endswith('EXTREME'):
                    try:
                        ds = pydicom.dcmread(file_abspath, force=True)
                        ds_dict["FileName"] =             str(file)
                        ds_dict["PatientID"] =            str(ds.PatientID)
                        ds_dict["SeriesNumber"] =         str(ds.SeriesNumber)
                        ds_dict["SeriesDescription"] =    str(ds.SeriesDescription)
                        ds_dict["Modality"] =             str(ds.Modality)
                        
                        w.writerow(ds_dict)
                        ds_dict = ds_dict.fromkeys(ds_dict, None)
                    except Exception as ex:
                        print(str(ex))
                        continue
        
    f.close()

if __name__ == "__main__":
    main()
</code></pre>
<p>To run it, just type it in the command line:</p>
<pre data-code-wrap="bash"><code class="lang-bash">python script.py input_folder/ output.csv
</code></pre>
<p>The generated CSV file can be opened with any spreadsheet software. By copying the unloaded file to a separate folder and importing it with the “Import DICOM” tool, I can load the missing files one by one.</p>

---

## Post #6 by @pieper (2023-11-30 21:44 UTC)

<aside class="quote no-group" data-username="luarpy" data-post="5" data-topic="32868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luarpy/48/67016_2.png" class="avatar"> luarpy:</div>
<blockquote>
<p>By copying the unloaded file to a separate folder and importing it with the “Import DICOM” tool, I can load the missing files one by one.</p>
</blockquote>
</aside>
<p>So this indicates that the files didn’t load due to something about the folder they were originally in?</p>

---

## Post #7 by @luarpy (2023-11-30 21:58 UTC)

<p>Nope, I checked by moving the parent directory to see if it could be due to a too long path. But the files are arbitrarily missing</p>

---

## Post #8 by @pieper (2023-11-30 22:08 UTC)

<p>Is there a way you can turn this into a report that can be reproduced on other machines?</p>

---

## Post #9 by @luarpy (2023-11-30 23:53 UTC)

<p>Do you mean by sharing the DICOM files I use (I should consult it) or with a public example DB? I could get an estimate of what is missing in proportion to those that exist.</p>

---

## Post #10 by @pieper (2023-12-01 22:03 UTC)

<p>What I mean is that it’s not clear if this is an issue with the files or your system of if it’s something to do with Slicer itself.  If you are able to provide a set of data and instructions that can be replicated elsewhere it might be possible to get to the heart of the issue.</p>

---
