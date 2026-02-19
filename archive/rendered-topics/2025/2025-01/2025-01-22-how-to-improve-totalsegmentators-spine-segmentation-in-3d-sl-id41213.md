---
topic_id: 41213
title: "How To Improve Totalsegmentators Spine Segmentation In 3D Sl"
date: 2025-01-22
url: https://discourse.slicer.org/t/41213
---

# How to Improve TotalSegmentator's Spine Segmentation in 3D Slicer?

**Topic ID**: 41213
**Date**: 2025-01-22
**URL**: https://discourse.slicer.org/t/how-to-improve-totalsegmentators-spine-segmentation-in-3d-slicer/41213

---

## Post #1 by @wenlin_x (2025-01-22 09:26 UTC)

<p>Hi,</p>
<p>I am using TotalSegmentator to segment the spine from CT scans. However, I noticed that certain parts, such as the spinous processes, are not segmented very well. I would like to manually refine the segmentation results based on the original CT data.</p>
<p>I have the following questions:</p>
<ol>
<li>Is it feasible to manually enhance the TotalSegmentator segmentation results using 3D Slicer?</li>
<li>What is the best workflow in 3D Slicer to compare the TotalSegmentator segmentation results with the original CT data and add missing details to the segmentation?</li>
</ol>
<p>Any guidance or suggestions would be greatly appreciated!</p>
<p>Thank you in advance!</p>

---

## Post #2 by @pieper (2025-01-22 19:09 UTC)

<p>The general pathway would be to provide improved manual segmentations (i.e. use the Segment Editor) and then retrain a model like TotalSegmentator either using nnU-Net, MONAI Label, or MONAI Auto3DSeg.  There’s a lot of documentation about these methods, but they do require some effort to learn and use.  It would be great if you could create and share improved segmentations.</p>
<p>Note there is also this dataset of already segmented vertebrae that could also be used to train models that may be more robust / higher resolution than TotalSegmentator and it would be great if people could work on that.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.cancerimagingarchive.net/collection/spine-mets-ct-seg/">
  <header class="source">
      <img src="https://www.cancerimagingarchive.net/wp-content/uploads/2019/12/cropped-TCIA-Favicon-Transparent-32x32.png" class="site-icon" width="32" height="32">

      <a href="https://www.cancerimagingarchive.net/collection/spine-mets-ct-seg/" target="_blank" rel="noopener">The Cancer Imaging Archive (TCIA)</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/242;"><img src="https://www.cancerimagingarchive.net/wp-content/uploads/Spine-Mets-CT-SEG_selected_image.png" class="thumbnail" width="690" height="243"></div>

<h3><a href="https://www.cancerimagingarchive.net/collection/spine-mets-ct-seg/" target="_blank" rel="noopener">Spine-Mets-CT-SEG - The Cancer Imaging Archive (TCIA)</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I haven’t tried it myself, but this tool looks very promising for the task of correcting model outputs:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW41_2024_MIT/Projects/SegmentationVerificationModuleForFinalizingMultiLabelAiSegmentations/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW41_2024_MIT/Projects/SegmentationVerificationModuleForFinalizingMultiLabelAiSegmentations/" target="_blank" rel="noopener">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW41_2024_MIT/Projects/SegmentationVerificationModuleForFinalizingMultiLabelAiSegmentations/" target="_blank" rel="noopener">Project Description</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
