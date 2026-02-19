---
topic_id: 5301
title: "Import Dicom Files Problem"
date: 2019-01-07
url: https://discourse.slicer.org/t/5301
---

# Import DICOM files problem

**Topic ID**: 5301
**Date**: 2019-01-07
**URL**: https://discourse.slicer.org/t/import-dicom-files-problem/5301

---

## Post #1 by @Thomas (2019-01-07 15:31 UTC)

<p>Hello. I have problem with importing data to 3D  Slicer. I can see how my data is importing slice by slice, but when the loading is 100% there is just one transversal slice and I can’t work with it as a stack. I already read FAQ\DICOM, but still don’t now. Thank you for your advices.</p>

---

## Post #2 by @cpinter (2019-01-07 16:22 UTC)

<p>Did you use the DICOM browser (import -&gt; load)?</p>
<p>FYI besides the FAQ, there is an actual module wiki page too: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM</a></p>

---

## Post #3 by @Thomas (2019-01-07 19:47 UTC)

<p>Yes, I tried it. But my data  are anonymised so Slicer creates 27 studies of sigle image instead of 27 images stuck. I thought when I just pick these slices by ADD DATA, it could be ok.</p>

---

## Post #4 by @lassoan (2019-01-07 20:09 UTC)

<aside class="quote no-group" data-username="Thomas" data-post="3" data-topic="5301">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e36b37/48.png" class="avatar"> Thomas:</div>
<blockquote>
<p>But my data are anonymised so Slicer creates 27 studies of sigle image instead of 27 images stuck</p>
</blockquote>
</aside>
<p>It is then anonymized incorrectly. Anonymization should not disintegrate the image series.</p>
<p>You can reassign image slices to the same image series again using DICOMPatcher module might be able to fix it but you should rather fix your DICOM anonymization process.</p>
<p>What software did you use for anonymization?</p>

---

## Post #5 by @Thomas (2019-01-07 20:44 UTC)

<p>I’m not sure, I have already got them anonymized, but I think it was done by some DIY skript in Matlab. Therefore  you might be right. Thank you.</p>

---

## Post #6 by @lassoan (2019-01-07 22:25 UTC)

<p>By default, Matlab’s DICOM write function creates invalid volume. See a bit more information and potential solutions in this topic: <a href="https://discourse.slicer.org/t/how-to-import-all-dicom-files-into-one-volume/5260/11" class="inline-onebox">How to import all dicom files into one volume</a></p>
<p>Matlab is really limited compared to Python when it comes to medical image computing, analysis, and visualization. I would recommend you to try to fully implement your workflow using Python-based tools. All features of Slicer and several important medical image computing libraries are available in Slicer’s embedded Python interpreter, so most probably you can implement custom processing workflow directly in Slicer.</p>

---

## Post #7 by @Thomas (2019-01-08 19:27 UTC)

<p>OK, I will check it. Thank you very much!</p>

---
