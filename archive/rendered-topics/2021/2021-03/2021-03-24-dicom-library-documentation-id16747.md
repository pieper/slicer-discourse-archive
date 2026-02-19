---
topic_id: 16747
title: "Dicom Library Documentation"
date: 2021-03-24
url: https://discourse.slicer.org/t/16747
---

# DICOM Library-Documentation

**Topic ID**: 16747
**Date**: 2021-03-24
**URL**: https://discourse.slicer.org/t/dicom-library-documentation/16747

---

## Post #1 by @juliangallaun (2021-03-24 13:07 UTC)

<p>Operating system: Ubuntu<br>
Slicer version: 4.11.20210226</p>
<p>Greetings slicer community, as a slicer novice I am struggling with the upload/ creation of my DICOM Library.</p>
<p>When I upload my DICOM folder, a new patient is created for every µCT slice separately, instead of one patient with all slices included. Maybe I am missing a certain Extension, with which I can manually edit my DICOM Library. Thank you for your help!</p>

---

## Post #2 by @pieper (2021-03-24 13:43 UTC)

<p>MicroCT scanners often produce non-standard dicom files.  You can try the tips linked below, or you might also try the ImageStacks module in the SlicerMorph extension.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html?highlight=dicom#troubleshooting" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html?highlight=dicom#troubleshooting</a></p>

---

## Post #3 by @muratmaga (2021-03-24 14:58 UTC)

<aside class="quote no-group" data-username="juliangallaun" data-post="1" data-topic="16747">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/juliangallaun/48/9545_2.png" class="avatar"> juliangallaun:</div>
<blockquote>
<p>When I upload my DICOM folder, a new patient is created for every µCT slice separately</p>
</blockquote>
</aside>
<p>Instead of the regular data load as, you should use the DICOM module. There is first an import step, and then the volume is loaded. If that fails, DCM2NIIX is typically a good solution to import DICOM stacks from non-clinical imaging systems.</p>

---
