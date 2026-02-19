---
topic_id: 16045
title: "Why Per Frame Transforms Stored In Seq Mhd Files Are Not Con"
date: 2021-02-17
url: https://discourse.slicer.org/t/16045
---

# Why per-frame transforms stored in .seq.mhd files are not converted from LPS to RAS?

**Topic ID**: 16045
**Date**: 2021-02-17
**URL**: https://discourse.slicer.org/t/why-per-frame-transforms-stored-in-seq-mhd-files-are-not-converted-from-lps-to-ras/16045

---

## Post #1 by @nathanbmnt (2021-02-17 23:32 UTC)

<p>When I load a .seq.mhd file, the IJKtoRAS matrix is unity:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6ca50cf5fb9236bbadccb9a5d5cc46b316ae51e6.png" alt="image" data-base62-sha1="fv7bxyvFdqaR6Ahe3tAJVqfJmqW" width="637" height="228"></p>
<p>I would expect the IJKtoRAS matrix to have -1 and -1 as the first two diagonal values from the top, because .mhd volumes are always in LPS coordinates. This is how non-sequence .mha’s load:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fccaa8c80a570782f55341df9eb4b77fcbc92325.png" alt="image" data-base62-sha1="A4iw7BatJOWHtosIWYyDsp0i4Kx" width="643" height="224"></p>
<p><code>ElementSpacing</code> is positive on both of these files.</p>

---

## Post #2 by @lassoan (2021-02-17 23:41 UTC)

<p>Seq.mhd file stores per-frame transforms to specify image geometry (origin, spacing, axis directions) for each frame.</p>
<p>If you want to have store a 3D image sequence where all 3D images have the same geometry, which is specified in standard fields then you need to use nrrd file format. We switched to nrrd from mha format because does not have clear definition of image dimensions (which axis means what).</p>

---

## Post #3 by @nathanbmnt (2021-02-18 05:21 UTC)

<p>Each frame transform is unity in my .seq.mhd though, so shouldn’t the image data still be treated as LPS?</p>

---

## Post #4 by @lassoan (2021-02-18 13:12 UTC)

<p>seq.mhd can store many transforms for each frame, each has a name, so you know exactly what coordinate systems it transforms between. There is no such assumptions like “world coordinate is LPS”, so there is nothing that the reader would need to modify when loading. It is up to you to name and interpret the transforms correctly.</p>
<p>The best the SlicerIGT importer could do is to detect …ToLPS and LPSTo… transforms and convert them to …ToRAS and RASTo… transforms but this would cause more problems than it would solve. If you want to have transforms to/from RAS coordinate system then you can either add them to the file when you create it; or you can add a diag([-1,-1,1,1]) transform in the transform hierarchy in Slicer to convert between LPS and RAS.</p>
<p>Since the patient-attached Reference marker typically does not move relative to the patient, we usually store all transforms relative to the Reference and compute and store ReferenceToRAS in Slicer.</p>

---
