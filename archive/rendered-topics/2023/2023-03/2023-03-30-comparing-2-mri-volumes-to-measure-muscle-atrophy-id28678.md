# Comparing 2 MRI volumes to measure muscle atrophy

**Topic ID**: 28678
**Date**: 2023-03-30
**URL**: https://discourse.slicer.org/t/comparing-2-mri-volumes-to-measure-muscle-atrophy/28678

---

## Post #1 by @feynmansum1 (2023-03-30 12:22 UTC)

<p>Hello, I am new to Slicer and was hoping for some advice.  I have 2 MRI’s of my right leg, 1 newer from a 3T instrument and 1 older study with a 1.5T.  The study areas are slightly different but mostly overlap.  I have muscle loss in the leg and I am trying to document how much. I assumed volume comparison would be ideal but perhaps an outer surface area would be easier?  Can someone recommend an approach and any tips on how to begin?  I have download the DICOM files and opened them in Slicer. Thank you.</p>

---

## Post #2 by @pieper (2023-03-30 14:09 UTC)

<p>Assuming the scans cover an overlapping field of view, it is likely that you can perform a registration, either manually with the transform module or maybe automatically (soft tissue registration is difficult, especially if the tissues have changed).  Then you can segment the same regions in both scans, either segment the same portion of the muscle in both scans or the whole portion of the leg and use the Segment Statistics module to get volume measurements.</p>

---

## Post #3 by @feynmansum1 (2023-03-31 15:13 UTC)

<p>Thank you for the suggestion, I will try the automatic registration first.  They do have an overlapping field of view.  Can you recommend a tutorial video or wiki on how to do the registration process with an MRI?</p>

---

## Post #4 by @pieper (2023-03-31 15:25 UTC)

<p>You can start <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">here for registration</a>.  It’s hard to say how which method will work best for your data.</p>

---

## Post #5 by @feynmansum1 (2023-03-31 16:46 UTC)

<p>I found SlicerTissueSegmentation (Tis_Seg) module which has a thigh specific segmentation.  This seems like it might be helpful, any recommendations/tips for using this?</p>

---

## Post #6 by @pieper (2023-03-31 17:08 UTC)

<p>I’ve never tried that one - maybe follow up with an issue on the github respository.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/MarinaSandonis/SlicerTissueSegmentation">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/MarinaSandonis/SlicerTissueSegmentation" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/700a5884d5e88c9ef993ed87e858d25790bb9f16f6906deba770801e018f0cd4/MarinaSandonis/SlicerTissueSegmentation" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/MarinaSandonis/SlicerTissueSegmentation" target="_blank" rel="noopener">GitHub - MarinaSandonis/SlicerTissueSegmentation: It gets the 2D/3D...</a></h3>

  <p>It gets the 2D/3D segmentation of the abdomen and the thigh from MR images. - GitHub - MarinaSandonis/SlicerTissueSegmentation: It gets the 2D/3D segmentation of the abdomen and the thigh from MR i...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
