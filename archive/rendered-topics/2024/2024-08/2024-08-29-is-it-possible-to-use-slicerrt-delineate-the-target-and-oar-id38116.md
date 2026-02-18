# Is it possible to use slicerRT delineate the target and OAR?

**Topic ID**: 38116
**Date**: 2024-08-29
**URL**: https://discourse.slicer.org/t/is-it-possible-to-use-slicerrt-delineate-the-target-and-oar/38116

---

## Post #1 by @LGDi (2024-08-29 13:09 UTC)

<p>I have imported the DICOM images. Can I use slicerRT to delineate the target and further calculate the dose?</p>

---

## Post #2 by @cpinter (2024-08-29 13:21 UTC)

<p>One of the most advanced features of Slicer is image segmentation</p>
<p>I’d start with this page of the documentation</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" target="_blank" rel="noopener">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" target="_blank" rel="noopener">Image Segmentation — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Also there are tons of discussions on the forum about it, but I recommend checking out the new AI based automatic segmentations</p>
<aside class="quote quote-modified" data-post="1" data-topic="26710">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/new-extension-fully-automatic-whole-body-ct-segmentation-in-2-minutes-using-totalsegmentator/26710">New extension: Fully automatic whole-body CT segmentation in 2 minutes using TotalSegmentator</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    The <a href="https://github.com/lassoan/SlicerTotalSegmentator#totalsegmentator">TotalSegmentator AI model is now available as an extension for 3D Slicer</a> version 5.2 and above (see installation instructions <a href="https://github.com/lassoan/SlicerTotalSegmentator#setup">here</a>). 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7de17ed588712331572fcd5de59f85ae9f2c9d1.jpeg" data-download-href="/uploads/short-url/uNEukuqDrXUWbSpuiA6BDwYo6Ln.jpeg?dl=1" title="image">[image]</a> 
A large number of AI segmentation models have been developed over the past few years, but <a href="https://github.com/wasserth/TotalSegmentator">TotalSegmentator</a> stands out in several aspects: 


it can segment many structures: 104 anatomical structures (all abdominal organs, bones, larger vessels, muscles)

it is very robust: it can segment any whole-body, abdominal, chest CT images, regardless of image…
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="1" data-topic="35680">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/new-extension-monai-auto3dseg-raise-the-bar-in-ai-medical-image-segmentation/35680">New extension: MONAI Auto3DSeg - raise the bar in AI medical image segmentation</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" style="--category-badge-color: #ED207B; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
    </div>
  </div>
  <blockquote>
    <a name="new-extension-monai-auto3dseg-raise-the-bar-in-ai-medical-image-segmentation-1" class="anchor" href="#new-extension-monai-auto3dseg-raise-the-bar-in-ai-medical-image-segmentation-1"></a>New extension: MONAI Auto3DSeg - raise the bar in AI medical image segmentation
MONAI Auto3DSeg extension is a collaboration between MONAI and 3D Slicer developer teams (led by Andres Diaz Pinto - NVIDIA and Andras Lasso - PerkLab) to improve on the state-of-the-art in fully automatic 3D medical image segmentation and make the results widely accessible. 
The extension comes with dozens of pre-trained segmentation models for specific clinical use cases, which are designed to be fast and run anywh…
  </blockquote>
</aside>


---
