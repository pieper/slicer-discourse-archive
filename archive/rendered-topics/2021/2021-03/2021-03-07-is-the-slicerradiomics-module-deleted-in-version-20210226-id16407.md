---
topic_id: 16407
title: "Is The Slicerradiomics Module Deleted In Version 20210226"
date: 2021-03-07
url: https://discourse.slicer.org/t/16407
---

# Is the SlicerRadiomics module deleted in version 20210226?

**Topic ID**: 16407
**Date**: 2021-03-07
**URL**: https://discourse.slicer.org/t/is-the-slicerradiomics-module-deleted-in-version-20210226/16407

---

## Post #1 by @slicer365 (2021-03-07 04:38 UTC)

<p>Is the SlicerRadiomics module deleted in version 20210226?I didn’t find it.How do I know what adjustments have been made in this version, compared to the previous stable version.Sometimes I install the module, how to deal with this kind of error during startup<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcc9c843be4ea9238bf88f4df4e688db363f85cd.jpeg" data-download-href="/uploads/short-url/A4gDCHVM6StYqRy4aVG6IDjm2Wp.jpeg?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fcc9c843be4ea9238bf88f4df4e688db363f85cd_2_690x392.jpeg" alt="捕获" data-base62-sha1="A4gDCHVM6StYqRy4aVG6IDjm2Wp" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fcc9c843be4ea9238bf88f4df4e688db363f85cd_2_690x392.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcc9c843be4ea9238bf88f4df4e688db363f85cd.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcc9c843be4ea9238bf88f4df4e688db363f85cd.jpeg 2x" data-dominant-color="D8DFE5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">762×434 74.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-03-08 16:57 UTC)

<p>It works for me on linux.  There are other errors in your log - you should be able to trace back to the earliest errors to see what is not working.  Looks like there are several things failing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7107c6b414cbbced534e447ef7e9a31c1e21f47e.jpeg" data-download-href="/uploads/short-url/g7UC6n5cpl8tNKo72e1uWRqMjls.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7107c6b414cbbced534e447ef7e9a31c1e21f47e_2_690x250.jpeg" alt="image" data-base62-sha1="g7UC6n5cpl8tNKo72e1uWRqMjls" width="690" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7107c6b414cbbced534e447ef7e9a31c1e21f47e_2_690x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7107c6b414cbbced534e447ef7e9a31c1e21f47e_2_1035x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7107c6b414cbbced534e447ef7e9a31c1e21f47e.jpeg 2x" data-dominant-color="EAEBEB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1303×473 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca199f82b1376315bf6783e2911af578722d8452.jpeg" data-download-href="/uploads/short-url/sPRlsXvQP5S0uS4QlvR116jSzKy.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca199f82b1376315bf6783e2911af578722d8452_2_690x348.jpeg" alt="image" data-base62-sha1="sPRlsXvQP5S0uS4QlvR116jSzKy" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca199f82b1376315bf6783e2911af578722d8452_2_690x348.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca199f82b1376315bf6783e2911af578722d8452_2_1035x522.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca199f82b1376315bf6783e2911af578722d8452.jpeg 2x" data-dominant-color="D6D7D8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1198×605 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @jamesobutler (2021-03-17 02:13 UTC)

<p>SlicerRadiomics is currently not available to install through the Extensions Manager on the Windows  platform because the extension build is failing.</p>
<p>A fix is currently proposed at <a href="https://github.com/AIM-Harvard/SlicerRadiomics/pull/66" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix Windows build error by jamesobutler · Pull Request #66 · AIM-Harvard/SlicerRadiomics · GitHub</a></p>

---
