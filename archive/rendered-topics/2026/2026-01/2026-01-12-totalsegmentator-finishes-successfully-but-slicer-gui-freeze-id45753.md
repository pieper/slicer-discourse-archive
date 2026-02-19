---
topic_id: 45753
title: "Totalsegmentator Finishes Successfully But Slicer Gui Freeze"
date: 2026-01-12
url: https://discourse.slicer.org/t/45753
---

# TotalSegmentator finishes successfully but Slicer GUI freezes on macOS (M2-Pro Sequoia) after completion

**Topic ID**: 45753
**Date**: 2026-01-12
**URL**: https://discourse.slicer.org/t/totalsegmentator-finishes-successfully-but-slicer-gui-freezes-on-macos-m2-pro-sequoia-after-completion/45753

---

## Post #1 by @Lennart99 (2026-01-12 16:37 UTC)

<p>Hi everyone,</p>
<p>I am using the TotalSegmentator extension in slicer to segment MRI data. The data is successfully loaded and apparently segmented, however, before loading the segments into slicer and making them accessible, Slicer freezes after the “saving segmentations“ log. I have tried running it in the fast and normal mode, both result in the same outcome. Slicer must then be force-quit. I am using an M2 Pro. Has anyone here experienced something similar and was able to solve the issue?</p>
<p>Any help would be greatly appreciated.</p>
<p>Thanks a lot!</p>

---

## Post #2 by @lassoan (2026-01-12 16:39 UTC)

<p>Does it help if you wait a long time (e.g., 1 hour)?<br>
Can you show a screenshot of the log window?</p>

---

## Post #3 by @Lennart99 (2026-01-12 18:46 UTC)

<p>Thank you for looking at the issue.</p>
<p>unfortunately waiting for a long time won’t help. I am currently running TotalSegmentator from the terminal and importing the NIFTI files to Slicer manually. It does work fairly well, but is manual another step.<br>
The log window basically shows exactly the same as the console of the terminal. I have attached the screenshot. At the point</p>
<p>…“Saving segmentations…</p>
<p>Saved in 18.84s“…</p>
<p>3D Slicer freezes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d64d3f2a84758c622e68426f94cf94952210353.png" data-download-href="/uploads/short-url/1UuefTpVwyvIfODVPpxWEhFTXUv.png?dl=1" title="Bildschirmfoto 2026-01-12 um 19.38.48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d64d3f2a84758c622e68426f94cf94952210353_2_690x190.png" alt="Bildschirmfoto 2026-01-12 um 19.38.48" data-base62-sha1="1UuefTpVwyvIfODVPpxWEhFTXUv" width="690" height="190" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d64d3f2a84758c622e68426f94cf94952210353_2_690x190.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d64d3f2a84758c622e68426f94cf94952210353_2_1035x285.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d64d3f2a84758c622e68426f94cf94952210353.png 2x" data-dominant-color="DFDFDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2026-01-12 um 19.38.48</span><span class="informations">1140×314 42 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
