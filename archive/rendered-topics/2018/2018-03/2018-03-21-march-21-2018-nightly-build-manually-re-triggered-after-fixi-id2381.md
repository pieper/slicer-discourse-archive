---
topic_id: 2381
title: "March 21 2018 Nightly Build Manually Re Triggered After Fixi"
date: 2018-03-21
url: https://discourse.slicer.org/t/2381
---

# March 21, 2018: Nightly build manually re-triggered after fixing regression due to AtlasCreatorLogic removal

**Topic ID**: 2381
**Date**: 2018-03-21
**URL**: https://discourse.slicer.org/t/march-21-2018-nightly-build-manually-re-triggered-after-fixing-regression-due-to-atlascreatorlogic-removal/2381

---

## Post #1 by @jcfr (2018-03-21 06:18 UTC)

<p>Since AtlasCreator logic was promptly removed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27088">r27088</a> (STYLE: Remove unused AtlasCreator loadable module logic) but it was still needed by EMSegment:</p>
<ul>
<li>AtlasCreator logic was directly added to the EMSegment module (see <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer3?view=revision&amp;revision=17153">r17153</a>)</li>
<li>Slicer EMSegment remote module was updated to reference the new version of EMSegment: <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27090">r27090</a></li>
<li>build on the factory were manually re-triggered to not clean the build directory and use the new version of Slicer</li>
<li>existing macOS and Windows entries were manually removed</li>
</ul>
<p>For these reasons, the dashboard will not show anything in the “Update” column.</p>
<p>CDash entries prior to the re-trigger:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e88c5431a6b397e4a96dfe00f8ee98c8c47f5c92.png" data-download-href="/uploads/short-url/xbdqr2l3yvfbbteGrnzIwnDLey6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e88c5431a6b397e4a96dfe00f8ee98c8c47f5c92_2_690x67.png" alt="image" data-base62-sha1="xbdqr2l3yvfbbteGrnzIwnDLey6" width="690" height="67" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e88c5431a6b397e4a96dfe00f8ee98c8c47f5c92_2_690x67.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e88c5431a6b397e4a96dfe00f8ee98c8c47f5c92_2_1035x100.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e88c5431a6b397e4a96dfe00f8ee98c8c47f5c92_2_1380x134.png 2x" data-dominant-color="B5C0C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1558×152 29.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>CDash entries after the removing old entries, and manually triggering the build:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e208913cfb1e31d666e233e07ca211285172ec3.png" data-download-href="/uploads/short-url/khjvtBExF1uMetgkkOfz6OXhgeT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e208913cfb1e31d666e233e07ca211285172ec3_2_690x74.png" alt="image" data-base62-sha1="khjvtBExF1uMetgkkOfz6OXhgeT" width="690" height="74" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e208913cfb1e31d666e233e07ca211285172ec3_2_690x74.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e208913cfb1e31d666e233e07ca211285172ec3_2_1035x111.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e208913cfb1e31d666e233e07ca211285172ec3_2_1380x148.png 2x" data-dominant-color="BCCAD5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1548×167 26.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
