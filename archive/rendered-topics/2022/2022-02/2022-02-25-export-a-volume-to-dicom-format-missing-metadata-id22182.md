---
topic_id: 22182
title: "Export A Volume To Dicom Format Missing Metadata"
date: 2022-02-25
url: https://discourse.slicer.org/t/22182
---

# Export a volume to DICOM format - missing metadata

**Topic ID**: 22182
**Date**: 2022-02-25
**URL**: https://discourse.slicer.org/t/export-a-volume-to-dicom-format-missing-metadata/22182

---

## Post #1 by @koeglfryderyk (2022-02-25 16:17 UTC)

<p>I followed the example from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-volume-to-dicom-file-format" rel="noopener nofollow ugc">Export a volume to DICOM file format</a>.</p>
<p>It successfully exported a volume, however, when I load the exported DICOM back to Slicer the study and patient name are missing:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3388fbab07d78081334e03d892aa9d8a6cb0d6b.png" alt="image" data-base62-sha1="yHDcScWNUaiUsOWBkBNaqJs9GL9" width="336" height="75"></p>
<p>Maybe I misunderstood something, but I thought that in this tree ‘test patient’ and ‘test study’ (as specified in the script repository) would appear.</p>
<p>MacOS, 3D Slicer 4.13.0-2022-02-16</p>

---

## Post #2 by @koeglfryderyk (2022-03-03 14:15 UTC)

<p>Turns out DICOM tags have to be set explicitly with:</p>
<pre><code class="lang-auto">exp.setTag('PatientID', patient_id)
</code></pre>
<p>The information is not automatically taken from the hierarchy tree.</p>
<p>I added an explanation to the DOCs in this <a href="https://github.com/Slicer/Slicer/pull/6238" rel="noopener nofollow ugc">pull request</a></p>

---
