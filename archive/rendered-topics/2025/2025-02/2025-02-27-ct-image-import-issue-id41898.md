# CT image import issue

**Topic ID**: 41898
**Date**: 2025-02-27
**URL**: https://discourse.slicer.org/t/ct-image-import-issue/41898

---

## Post #1 by @ZichenLi (2025-02-27 14:31 UTC)

<p>I encountered an issue while using 3D Slicer.The specific problem is that after importing the images,they become discontinuous and cannot be used for ROI delineation.What could be the possible reason for this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/213cf0ba5326325af176a86d55c4e34834e9c580.png" data-download-href="/uploads/short-url/4K2jSpNCWX8z8DFDFUNPkyaTqZG.png?dl=1" title="微信图片_20250226014715" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/213cf0ba5326325af176a86d55c4e34834e9c580.png" alt="微信图片_20250226014715" data-base62-sha1="4K2jSpNCWX8z8DFDFUNPkyaTqZG" width="690" height="271" data-dominant-color="252525"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20250226014715</span><span class="informations">1041×409 26.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-02-27 15:23 UTC)

<p>Try to switch to Advanced mode in the DICOM browser, click Examine, deselect everything and find <em>the one</em> loadable with type “Scalar volume”.</p>

---

## Post #3 by @ZichenLi (2025-02-27 15:42 UTC)

<p>Thank you very much.I have resolved this issue based on your method.</p>

---
