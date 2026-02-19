---
topic_id: 27274
title: "No Node When Loading Dicom"
date: 2023-01-16
url: https://discourse.slicer.org/t/27274
---

# No Node when loading DICOM

**Topic ID**: 27274
**Date**: 2023-01-16
**URL**: https://discourse.slicer.org/t/no-node-when-loading-dicom/27274

---

## Post #1 by @Kevin (2023-01-16 19:03 UTC)

<p>Operating system: Window 8<br>
Slicer version: 5.2.1<br>
Expected behavior: Node be clickable in the left menu<br>
Actual behavior: Non Node of data loaded but the view is ok.</p>
<p>I have a critical error but i don’ t understand hoow to fix it :<br>
E: DcmElement: Unknown Tag &amp; Data (f0fa,800d) larger (895628728) than remaining bytes in file</p>

---

## Post #2 by @pieper (2023-01-16 19:57 UTC)

<p>That indicates the file is likely corrupted or not a dicom file.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>

---

## Post #3 by @lassoan (2023-01-17 05:42 UTC)

<aside class="quote no-group" data-username="Kevin" data-post="1" data-topic="27274">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/2acd7d/48.png" class="avatar"> Kevin:</div>
<blockquote>
<p>Expected behavior: Node be clickable in the left menu<br>
Actual behavior: Non Node of data loaded but the view is ok.</p>
</blockquote>
</aside>
<p>This issue has been recently <a href="https://github.com/Slicer/Slicer/commit/aa245559e6027c8bf568ff96365dff9aed5be773">fixed in the Slicer Preview Release</a>. If using the Data module as a workaround is not acceptable for you then you can switch to a recent Slicer Preview Release.</p>

---
