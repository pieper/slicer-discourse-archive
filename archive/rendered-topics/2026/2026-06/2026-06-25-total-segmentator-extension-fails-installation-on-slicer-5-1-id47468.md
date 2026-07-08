---
topic_id: 47468
title: "Total Segmentator Extension Fails Installation on Slicer 5.12.0"
date: 2026-06-25
url: https://discourse.slicer.org/t/47468
last_bumped: 2026-07-07T15:08:02.809Z
---

# Total Segmentator Extension Fails Installation on Slicer 5.12.0

**Topic ID**: 47468
**Date**: 2026-06-25
**URL**: https://discourse.slicer.org/t/total-segmentator-extension-fails-installation-on-slicer-5-12-0/47468

---

## Post #1 by @amyers (2026-06-25 19:22 UTC)

<p>On Windows 11, I just installed Slicer 5.12.0 revision 34621, built 2026-06-24. I was able to install DentalSegmentator, SlicerOpenAnatomy, NNUnet, etc; however, TotalSegmentator failed to install.</p>
<p>This is the error I received: “Failed to retrieve metadata for TotalSegmentator extension” Is it related to <a href="https://discourse.slicer.org/t/extension-manager-hangs-and-crashes-slicer-5-10-today/47452/3" class="inline-onebox">Extension manager hangs and crashes Slicer 5.10 today - #3 by mikebind</a> ? I read that post, restarted my system and still see the issue. Before restarting, I deleted the old 3D Slicer 5.10.0 files in AppData/Local/slicer.org.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5ad08bb9f2ae6d36287d2163944c4a01e87d7b6.png" data-download-href="/uploads/short-url/wLO40mlSNlUEMFnL7Uipq9ImN4a.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5ad08bb9f2ae6d36287d2163944c4a01e87d7b6_2_690x408.png" alt="image" data-base62-sha1="wLO40mlSNlUEMFnL7Uipq9ImN4a" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5ad08bb9f2ae6d36287d2163944c4a01e87d7b6_2_690x408.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5ad08bb9f2ae6d36287d2163944c4a01e87d7b6_2_1035x612.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5ad08bb9f2ae6d36287d2163944c4a01e87d7b6_2_1380x816.png 2x" data-dominant-color="F2F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×1136 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a log file I can look or configure for a non-development build?</p>
<p>Are there any useful python console debug commands for this situation?</p>
<p>Thanks,<br>
Alex</p>

---

## Post #2 by @amyers (2026-07-07 13:04 UTC)

<p>I just installed TotalSegmentator without the error: “Failed to retrieve metadata for TotalSegmentator extension.” Does anyone think this was an extension manager server error?</p>

---

## Post #3 by @amyers (2026-07-07 15:08 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> just spoke to me about this and the issue is resolved.</p>

---
