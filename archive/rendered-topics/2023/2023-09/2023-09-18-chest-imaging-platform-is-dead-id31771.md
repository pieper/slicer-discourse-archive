---
topic_id: 31771
title: "Chest Imaging Platform Is Dead"
date: 2023-09-18
url: https://discourse.slicer.org/t/31771
---

# Chest Imaging Platform is dead?

**Topic ID**: 31771
**Date**: 2023-09-18
**URL**: https://discourse.slicer.org/t/chest-imaging-platform-is-dead/31771

---

## Post #1 by @volkodavmyx (2023-09-18 13:59 UTC)

<p>Hi everyone!</p>
<p>5.2.2 is the last release on witch Chest Imaging Platform is available in Extension Manager.<br>
On 5.3.0 and 5.4.0 you can only install Lung segmenter as a part of CIP.</p>
<p>There are no more updates for module planned?<br>
MIP viewer was very useful…</p>
<p>Best,<br>
Nikolai</p>

---

## Post #2 by @rbumm (2023-09-18 15:05 UTC)

<p>That is weird, actually, I have no idea why this happened…</p>

---

## Post #3 by @lassoan (2023-09-18 18:55 UTC)

<p>CIP is <a href="https://github.com/acil-bwh/ChestImagingPlatform/commits/develop">continuously developed</a> and there are ongoing efforts to secure dedicated funding for reworking/modernizing it. The commit history may be misleading, as development happens in <code>develop</code> branch and not in <code>master</code>.</p>
<p>CIP is available for the previous stable release (Slicer-5.2.2):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ace29de65f641421360c4de7df1757743937c04.jpeg" data-download-href="/uploads/short-url/1xAtDI7Z96tbHkfz5qCrRDK3xMU.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ace29de65f641421360c4de7df1757743937c04_2_690x472.jpeg" alt="image" data-base62-sha1="1xAtDI7Z96tbHkfz5qCrRDK3xMU" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ace29de65f641421360c4de7df1757743937c04_2_690x472.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ace29de65f641421360c4de7df1757743937c04_2_1035x708.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ace29de65f641421360c4de7df1757743937c04_2_1380x944.jpeg 2x" data-dominant-color="C6C9CF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1315 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>CIP has had a <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3150082">build error on Slicer-5.4/5.5 due to some optimization of include files in Slicer core</a>. I’ve <a href="https://github.com/acil-bwh/SlicerCIP/commit/33258fe757304d1570ef9b34fd3fe562b8ee44a5">fixed the issue</a> now, so Chest_Imaging_Platform extension should be available for Slicer-4.4/4.5 from tomorrow.</p>

---
