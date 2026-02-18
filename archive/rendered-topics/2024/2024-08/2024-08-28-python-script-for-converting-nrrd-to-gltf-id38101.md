# Python script for converting nrrd to gltf

**Topic ID**: 38101
**Date**: 2024-08-28
**URL**: https://discourse.slicer.org/t/python-script-for-converting-nrrd-to-gltf/38101

---

## Post #1 by @anuragp2018 (2024-08-28 20:56 UTC)

<p>Hello<br>
i want python script that convert nrrd to 3d like slicer convert 3d.</p>

---

## Post #2 by @lassoan (2024-08-28 20:58 UTC)

<p>NRRD is already 3D, no conversion is necessary. Do you need the data in a certain file format?</p>

---

## Post #3 by @anuragp2018 (2024-08-29 03:44 UTC)

<p>yes in gltf or glb format</p>

---

## Post #4 by @cpinter (2024-08-29 09:01 UTC)

<p>For this you will need to segment the structures and then export the closed surface to GLTF.</p>
<p>Here are two extensions that can do automatic segmentation. The TotalSegmentator video includes GLTF export as well towards the end.</p>
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

## Post #5 by @anuragp2018 (2024-08-29 09:22 UTC)

<p>but i want to export gltf using python script</p>

---

## Post #6 by @cpinter (2024-08-29 09:25 UTC)

<p>The GLTF exporter module is written in python. See what functions it has and call them appropriately.</p>

---

## Post #7 by @anuragp2018 (2024-09-01 18:11 UTC)

<p>but it uses slicer i don’t want to use slicer.</p>

---

## Post #8 by @chir.set (2024-09-01 18:18 UTC)

<aside class="quote no-group" data-username="anuragp2018" data-post="7" data-topic="38101">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anuragp2018/48/77765_2.png" class="avatar"> anuragp2018:</div>
<blockquote>
<p>but it uses slicer i don’t want to use slicer</p>
</blockquote>
</aside>
<p>Are you serious? Please recall it’s a Slicer forum. Developers kindly offer free support here, but your demand will drive them in a confused state.</p>

---

## Post #9 by @lassoan (2024-09-02 03:13 UTC)

<p>Yes, “i don’t want to use slicer” is indeed confusing, especially because it can mean so many things. Do you mean that you don’t want to use Slicer GUI, or don’t want to use Slicer’s Python environment, don’t want to use libraries that Slicer is using (mainly ITK and VTK), …?</p>
<p>In general, we give the simplest solution to the questions that users are asking, which uses the Slicer GUI or Python scripting within Slicer. However, since Slicer usually just adds a thin wrapper over pip-installable libraries, you can start from a script that runs in Slicer, and then step by step replace Slicer-specific parts (by looking at what Slicer does and replicate that with your own code).</p>

---
