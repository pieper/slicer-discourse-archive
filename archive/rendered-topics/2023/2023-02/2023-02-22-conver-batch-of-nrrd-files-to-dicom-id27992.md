# Conver batch of nrrd files to DICOM

**Topic ID**: 27992
**Date**: 2023-02-22
**URL**: https://discourse.slicer.org/t/conver-batch-of-nrrd-files-to-dicom/27992

---

## Post #1 by @dvdm1 (2023-02-22 22:30 UTC)

<p>Hi,</p>
<p>I want to convert a batch of a few hundred scans from nrrd to DICOM. I have been reading about using the create a dicom series in the CLI (including this topic: <a href="https://discourse.slicer.org/t/convert-nrrd-to-dicom/17251" class="inline-onebox">Convert NRRD to DICOM</a>), but I’m still unsure how to use this is practice as I’m new to slicer.<br>
Can I run the python scripts in my own python IDE, or do I have to use the python console in Slicer?<br>
And how can I give a batch of nrrd files as the input for the script?</p>
<p>Thank you in advance!</p>

---

## Post #2 by @rfenioux (2023-02-23 09:42 UTC)

<p>You can use the PythonSlicer interpreter outside of slicer (e.g. configure your IDE to use it instead of the system python). To find the path to this interpreter you can use the following commands in the python console of Slicer:</p>
<pre><code class="lang-auto">import sys
sys.executable
</code></pre>
<p>I think your second question is more a python question than a slicer question. You can adapt <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-volume-to-dicom-file-format" rel="noopener nofollow ugc">this script</a> to loop over the nrrd files in python and convert them one by one.</p>
<p>I hope this answers your questions</p>

---
