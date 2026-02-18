# Exclude pleural effusion from CT lung segmentation (CT lung analyzer)

**Topic ID**: 30506
**Date**: 2023-07-11
**URL**: https://discourse.slicer.org/t/exclude-pleural-effusion-from-ct-lung-segmentation-ct-lung-analyzer/30506

---

## Post #1 by @mikiN (2023-07-11 01:25 UTC)

<p>Ask a question about lung segmentation.<br>
I am performing segmentation for chest CT using lungmask, but inevitably pleural effusion is also segmented together. I am now erasing the pleural fluid with an eraser for each thin-slice one by one. However, that is very time-consuming and difficult.<br>
Is there a better way to do this?</p>

---

## Post #2 by @mikiN (2023-07-11 01:26 UTC)

<p>I use “R231CovidWeb”.</p>

---

## Post #3 by @rbumm (2023-07-11 05:27 UTC)

<p>Try TotalSegmenter in the AI options of lung segmentation, I have seen detecting it pleural fluid fairly well,  if you still got problems drop us a note here.</p>

---

## Post #4 by @mikiN (2023-09-06 12:36 UTC)

<p>I get an error like this. I am in trouble, please help…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d6d2ae1477ec640185633c92105514b6be15a45.png" data-download-href="/uploads/short-url/kb7dfaqqPmd4URjI4DJjDllwaK9.png?dl=1" title="スクリーンショット 2023-09-06 213811" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d6d2ae1477ec640185633c92105514b6be15a45.png" alt="スクリーンショット 2023-09-06 213811" data-base62-sha1="kb7dfaqqPmd4URjI4DJjDllwaK9" width="690" height="199" data-dominant-color="E6E3E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2023-09-06 213811</span><span class="informations">999×289 24.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @rbumm (2023-09-06 13:29 UTC)

<p>This is due to the fact that TotalSegmentator is not properly installed on your system.<br>
Please download and install the Totalsegmenator extension.<br>
Restart Slicer.<br>
Test the extension.<br>
If problems persist you may need to install the TotalSegmentator weights via a VPN.</p>

---
