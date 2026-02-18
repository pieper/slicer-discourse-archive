# CT Image Series Count Missing in 3D Slicer for CT Scanner Data

**Topic ID**: 33267
**Date**: 2023-12-06
**URL**: https://discourse.slicer.org/t/ct-image-series-count-missing-in-3d-slicer-for-ct-scanner-data/33267

---

## Post #1 by @Sougata_Maity (2023-12-06 21:28 UTC)

<p>Hello, I’m having trouble determining the <strong>CT image series count</strong>. Is there a DICOM tag within the metadata that provides this information? We have configured two systems, the PACS and the CT Scanner, to interface with 3D Slicer. When we import data from the PACS to Slicer, all the information is displayed in the DICOM display window. However, we encounter difficulties when attempting to achieve the same result with CT Scan data in Slicer. Could you please guide me on how to overcome this issue?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1a51ce3936c88149dc1e7e1b9c6bd723e5ff9a2.png" data-download-href="/uploads/short-url/n3YCLZ9cPsA3RcUsVIEtm4HPNSO.png?dl=1" title="tempsnip" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1a51ce3936c88149dc1e7e1b9c6bd723e5ff9a2.png" alt="tempsnip" data-base62-sha1="n3YCLZ9cPsA3RcUsVIEtm4HPNSO" width="690" height="276" data-dominant-color="DFE8F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">tempsnip</span><span class="informations">1259×504 22.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-12-06 21:35 UTC)

<p>If you use classic DICOM information objects (that most scanners still use nowadays) then DICOM metadata does not provide any information about how many instances are in a series or how many series are in a study. If you receive a bunch of DICOM instances (e.g., files, each file containing a single image slice) you cannot even tell if you have all of them that were acquired in that series. It is all up to the application to find out how to make sense of the data that it has received. The data may be incomplete and inconsistent, may have variable spacing, or may just miss a few frames.</p>
<aside class="quote no-group" data-username="Sougata_Maity" data-post="1" data-topic="33267">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sougata_maity/48/68605_2.png" class="avatar"> Sougata_Maity:</div>
<blockquote>
<p>However, we encounter difficulties when attempting to achieve the same result with CT Scan data in Slicer.</p>
</blockquote>
</aside>
<p>How do you transfer the data from the CT scanner to Slicer?</p>

---
