# How to download 3D Slicer version 4.11 or 4.10?

**Topic ID**: 32953
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/how-to-download-3d-slicer-version-4-11-or-4-10/32953

---

## Post #1 by @Lilyana (2023-11-22 12:10 UTC)

<p>I want to download the old version of 3D slicer, namely 4.10 or 4.11, because I want to research the area and density of the pectoralis muscle</p>

---

## Post #2 by @lassoan (2023-11-22 12:14 UTC)

<p>It should not be necessary to downgrade to such very old versions of Slicer. What operation would you like to do that you cannot seem to find in the current Slicer version?</p>
<p>Actually, there are much better Cross-sectional area measurement tools in more recent Slicer versions. For example, you can use the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/CrossSectionAnalysis.md">Cross-section analysis</a> module provided by SlicerVMTK extension.</p>

---

## Post #3 by @Lilyana (2023-11-22 13:08 UTC)

<p>I want to measure the area and density of the pectoralis muscle. In my 3D Slicer there is no body composition feature so I don’t know how to measure the area and density of the pectoralis muscle. Can you help me please?</p>
<p>This is what 3D Slicer looks like on my laptop:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1be4c1d1be98bb1a64535cc1e29c91f42943765b.png" data-download-href="/uploads/short-url/3YL05VHPMSONnKd5yoQi3Ulr1BF.png?dl=1" title="Screenshot (1615)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1be4c1d1be98bb1a64535cc1e29c91f42943765b_2_690x388.png" alt="Screenshot (1615)" data-base62-sha1="3YL05VHPMSONnKd5yoQi3Ulr1BF" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1be4c1d1be98bb1a64535cc1e29c91f42943765b_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1be4c1d1be98bb1a64535cc1e29c91f42943765b_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1be4c1d1be98bb1a64535cc1e29c91f42943765b_2_1380x776.png 2x" data-dominant-color="CECFD5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (1615)</span><span class="informations">1920×1080 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2023-11-22 13:57 UTC)

<p>Once you segmented the muscle using Segment Editor module, you can use Segment Statistics module to get average density, total volume, total surface area, etc. of the segment.</p>

---
