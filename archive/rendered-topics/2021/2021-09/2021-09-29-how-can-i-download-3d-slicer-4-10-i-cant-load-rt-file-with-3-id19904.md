# How can I download 3D slicer 4.10, I can't load RT file with 3D slicer 4.11 for CT scan

**Topic ID**: 19904
**Date**: 2021-09-29
**URL**: https://discourse.slicer.org/t/how-can-i-download-3d-slicer-4-10-i-cant-load-rt-file-with-3d-slicer-4-11-for-ct-scan/19904

---

## Post #1 by @KAMONCHAT_APIVANICHK (2021-09-29 01:07 UTC)

<p>I would like to download older version of 3D slicer, 3D slicer 4.10, instead of 4.11. Newest version can’t be opened my RTSTRUCT file, it ignored my file. I can’t continuously work. How can I down load older version.</p>

---

## Post #2 by @KAMONCHAT_APIVANICHK (2021-09-28 15:52 UTC)

<p>I installed 3D slicer 4.11 but I can’t open any RT structure data. I had opened it with old version. Why?</p>

---

## Post #3 by @Sunderlandkyl (2021-09-29 02:20 UTC)

<p>Can you upload a log file? (in application menu bar: Help-&gt;Report a bug).</p>

---

## Post #4 by @Sunderlandkyl (2021-09-29 02:22 UTC)

<p>Also, do you have SlicerRT installed?</p>

---

## Post #5 by @cpinter (2021-09-29 09:21 UTC)

<p>Please download the latest Slicer release, install the SlicerRT extension, open the DICOM module, import the folder containing your dataset and load the whole study from the DICOM browser. Let us know if it works.</p>

---

## Post #6 by @lassoan (2021-09-29 14:33 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="19904">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>open the DICOM module, import the folder containing your dataset and load the whole study from the DICOM browser</p>
</blockquote>
</aside>
<p>See step-by-step instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#read-dicom-files-into-the-scene">here</a>.</p>

---
