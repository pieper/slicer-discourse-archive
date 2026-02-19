---
topic_id: 19992
title: "Anyone Know How Can I Export A 3D Volumen From Mindray M6 Ul"
date: 2021-10-04
url: https://discourse.slicer.org/t/19992
---

# Anyone know how can i export a 3D volumen from Mindray M6 ultrasound in DICOM format to use in Slicer?

**Topic ID**: 19992
**Date**: 2021-10-04
**URL**: https://discourse.slicer.org/t/anyone-know-how-can-i-export-a-3d-volumen-from-mindray-m6-ultrasound-in-dicom-format-to-use-in-slicer/19992

---

## Post #1 by @Andres_Carbonell (2021-10-04 14:06 UTC)

<p>Anyone know how can i export a 3D volumen from Mindray M6 ultrasound in DICOM format to use in 3DSlicer?</p>

---

## Post #2 by @Andres_Carbonell (2021-10-04 14:04 UTC)

<p>Hi!</p>
<p>I need a help</p>
<p>Anyone know, How can i do to export a volumen DICOM from Mindray M6 ultrasound?</p>

---

## Post #3 by @lassoan (2021-10-04 14:50 UTC)

<p>See previous discussion of this topic here:</p>
<aside class="quote quote-modified" data-post="10" data-topic="3613">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/74df32/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/ultrasound-mindray-dc-70/3613/10">Ultrasound Mindray DC-70</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    
  </blockquote>
</aside>

<p>To summarize, you can get individual frames out of the <code>BC_CinePartition0.bin</code> files quite easily, for example using <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess#slicerrawimageguess">RawImageGuess extension</a>:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d2be6fbd700b4aaa9029be92cbedda880e00102.jpeg" data-download-href="/uploads/short-url/k8RnMj7YyjsQBoopUrvesN67qr8.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d2be6fbd700b4aaa9029be92cbedda880e00102_2_690x420.jpeg" alt="image" data-base62-sha1="k8RnMj7YyjsQBoopUrvesN67qr8" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d2be6fbd700b4aaa9029be92cbedda880e00102_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d2be6fbd700b4aaa9029be92cbedda880e00102_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d2be6fbd700b4aaa9029be92cbedda880e00102_2_1380x840.jpeg 2x" data-dominant-color="616267"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1170 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, there seems to be some metadata stored before each slice, which throws off RawImageGuess (the module assumes that the input file contains voxels in one block). You would need to implement a reader (or hire someone for implementing it), that reads the metadata+voxels for each slice and interprets the metadata and writes the voxels into a large array (e.g., a numpy array); and in the end imports the array into a volume node. It could be a simple Python script, the hard part is get information about how to interpret the file - either by getting information from the manufacturer or by reverse engineering the files.</p>

---
