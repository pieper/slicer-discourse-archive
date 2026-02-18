# How to read NRRD metadata

**Topic ID**: 7266
**Date**: 2019-06-20
**URL**: https://discourse.slicer.org/t/how-to-read-nrrd-metadata/7266

---

## Post #1 by @Leon (2019-06-20 21:25 UTC)

<p>Imported DICOM files are normally saved as a NRRD file by which the images are anonymized. Ideal for privacy reasons.<br>
But if someone sends me such a anonymized NRRD file, am I then still able to read all the other remeaning metadata inside the NRRD?</p>
<p>I did a check on the sample ‘CTChest NRRD’ and converted it to a DICOM serie. After importing this serie into the DICOM browser I was able to read some metadata, but a DICOM normally contains very many metadata. Is there a better way by which I can read all metadata in a NRRD file, or are just many data discarded during conversion?<br>
In other words: does Slicer have a NRRD metadata reader?</p>

---

## Post #2 by @lassoan (2019-06-20 22:01 UTC)

<aside class="quote no-group" data-username="Leon" data-post="1" data-topic="7266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>But if someone sends me such a anonymized NRRD file, am I then still able to read all the other remeaning metadata inside the NRRD?</p>
</blockquote>
</aside>
<p>Normally only image geometry (origin, spacing, axis directions) is saved in nrrd files, so you cannot recover any other DICOM tags.</p>
<p>If you need information in the DICOM tags then ask for an anonymized DICOM file or export DICOM tags to a separate file (e.g., using DCMTK toolkit’s dcmdump or dcm2xml tools).</p>

---
