---
topic_id: 21630
title: "Dicom Import Failed Whats Wrong"
date: 2022-01-26
url: https://discourse.slicer.org/t/21630
---

# Dicom import failed, what's wrong?

**Topic ID**: 21630
**Date**: 2022-01-26
**URL**: https://discourse.slicer.org/t/dicom-import-failed-whats-wrong/21630

---

## Post #1 by @jumbojing (2022-01-26 08:12 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26bd1815514355722c535a8f6c98e36eb5d5768a.jpeg" data-download-href="/uploads/short-url/5wHh7bZGP9l4NZTRXJdRyy0Blj4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26bd1815514355722c535a8f6c98e36eb5d5768a_2_690x226.jpeg" alt="image" data-base62-sha1="5wHh7bZGP9l4NZTRXJdRyy0Blj4" width="690" height="226" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26bd1815514355722c535a8f6c98e36eb5d5768a_2_690x226.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26bd1815514355722c535a8f6c98e36eb5d5768a_2_1035x339.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26bd1815514355722c535a8f6c98e36eb5d5768a_2_1380x452.jpeg 2x" data-dominant-color="707173"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×629 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Dicom import failed, what’s wrong?</p>

---

## Post #2 by @Juicy (2022-01-26 08:18 UTC)

<p>I see you have a heap of individual volumes for each slice in your CT DICOM stack. Have you used the DICOM module to import you images? Click on the small “DCM” icon in the top left of the Slicer window to go to the DICOM module. Then drag and drop the folder containing all your CT images into the slicer window to add the images into the DICOM module. Then click on the correct patient entry and click the Load button.</p>

---

## Post #3 by @jumbojing (2022-01-26 08:32 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3421eff947eee5ab0a5051acbea2c0302f2594c7.png" data-download-href="/uploads/short-url/7rbxpVidA0cODjTf9P79UVfeeQn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3421eff947eee5ab0a5051acbea2c0302f2594c7_2_690x197.png" alt="image" data-base62-sha1="7rbxpVidA0cODjTf9P79UVfeeQn" width="690" height="197" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3421eff947eee5ab0a5051acbea2c0302f2594c7_2_690x197.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3421eff947eee5ab0a5051acbea2c0302f2594c7_2_1035x295.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3421eff947eee5ab0a5051acbea2c0302f2594c7_2_1380x394.png 2x" data-dominant-color="E3EBF2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2822×806 417 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I use the <strong>DCM</strong> import the fold, but failed…how to combine them?</p>
<pre><code class="lang-auto">Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 300: L-S SPINE_1
Imported a DICOM directory, checking for extensions
Geometric issues were found with 1 of the series. Please use caution.

Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 300: L-S SPINE - imageOrientationPatient 1
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 300: L-S SPINE - imageOrientationPatient 2
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 300: L-S SPINE - imageOrientationPatient 3
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 300: L-S SPINE - imageOrientationPatient 4
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 300: L-S SPINE - imageOrientationPatient 5
Loading with imageIOName: GDCM
....
</code></pre>

---

## Post #4 by @jumbojing (2022-01-26 08:39 UTC)

<p>Or how to merge those single dicoms into one group dcm?</p>

---

## Post #5 by @pieper (2022-01-26 12:42 UTC)

<p>The names of the loaded data indicate that they are not parallel (orientation is different in each loaded section).  Try the FAQ suggestions.  You may be able to use geometry normalization or the patcher.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>

---
