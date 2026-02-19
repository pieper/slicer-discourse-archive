---
topic_id: 46026
title: "4Dct Registration Hierarchical 3D Registration Not Recognizi"
date: 2026-02-01
url: https://discourse.slicer.org/t/46026
---

# 4DCT registration - Hierarchical 3D Registration not recognizing "Sequence"

**Topic ID**: 46026
**Date**: 2026-02-01
**URL**: https://discourse.slicer.org/t/4dct-registration-hierarchical-3d-registration-not-recognizing-sequence/46026

---

## Post #1 by @taylor_t (2026-02-01 18:38 UTC)

<p>I am trying to process 4DCT data using SlicerAutoscoper. I was able to load in the static CT images (Bone Thins Knee Bilateral), perform segmentations and export as STL files, and load in the 4D CT dynamic data (4D Knee_1).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24b9b1a07ee637a0c40626563fd5aa45646fece9.png" data-download-href="/uploads/short-url/5eT2f6ajlDncfjmDoDRHpTbVZ8Z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24b9b1a07ee637a0c40626563fd5aa45646fece9.png" alt="image" data-base62-sha1="5eT2f6ajlDncfjmDoDRHpTbVZ8Z" width="311" height="103"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">311×103 4.24 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I try to register using “Hierarchical3DRegistration”, the dynamic image files are not being recognized as a sequence. When I try to use the dropdown next to “Input CT Sequence", the list is empty.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/650e98b51df2e9c8b52ed66f83a052b1908c943f.png" data-download-href="/uploads/short-url/epZuQ0IHUIGjQVFRrcKJ65pwe4v.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/650e98b51df2e9c8b52ed66f83a052b1908c943f.png" alt="image" data-base62-sha1="epZuQ0IHUIGjQVFRrcKJ65pwe4v" width="637" height="101"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">637×101 3.95 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am wondering whether there are any pre-processing steps I need on the imported DICOM files for recognition as a sequence or conversion to .seq?</p>
<p>Thank you for your help.</p>

---
