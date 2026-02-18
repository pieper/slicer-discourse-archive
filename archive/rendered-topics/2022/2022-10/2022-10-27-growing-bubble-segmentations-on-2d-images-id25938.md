# Growing Bubble Segmentations on 2D Images

**Topic ID**: 25938
**Date**: 2022-10-27
**URL**: https://discourse.slicer.org/t/growing-bubble-segmentations-on-2d-images/25938

---

## Post #1 by @nysfour (2022-10-27 17:00 UTC)

<p>Are there any published guides on how to perform a simple growing region segmentation on a 2D Image? I have been unable to find any concrete examples, only references to resampling the scalar volume. I am looking for the ability to place a bubble in a 2D plane and have it grow to create a mask. Thank you!</p>

---

## Post #2 by @mau_igna_06 (2022-10-27 19:27 UTC)

<p>Please google “growcut itk”</p>
<p>Here is one apparently interesting result:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://pypi.org/project/itk-growcut/">
  <header class="source">
      <img src="https://pypi.org/static/images/favicon.6a76275d.ico" class="site-icon" width="32" height="30">

      <a href="https://pypi.org/project/itk-growcut/" target="_blank" rel="noopener">PyPI</a>
  </header>

  <article class="onebox-body">
    <img src="https://pypi.org/static/images/twitter.6fecba6f.jpg" class="thumbnail onebox-avatar" width="300" height="300">

<h3><a href="https://pypi.org/project/itk-growcut/" target="_blank" rel="noopener">itk-growcut</a></h3>

  <p>Segments a 3D image from foreground and background seeds.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hope it helps</p>

---

## Post #3 by @nysfour (2022-11-11 14:19 UTC)

<p>Thank you, is there another plug in for 2D images possibly?</p>

---

## Post #4 by @lassoan (2022-11-11 15:34 UTC)

<p>“Grow from seeds” algorithm implementation does not look into boundary voxels, as it allows some performance optimizations that we always know that every voxel has a neighbor in all directions. Since in a single-slice image, there are no neighbor slices, each voxel is a boundary voxel, and therefore the algorithm does not work on such images. It would not be hard to modify the algorithm to have a special path for 2D images, I guess we just haven’t invested the time into this because 2D image segmentation is inherently so much simpler and there are several other segmentation tools that work in 2D images as well.</p>
<p>If we get more information on what you want to achieve then we may be able to recommend segmentation tools for that. What kind of images are you working with? What are you segmenting? Can you provide a screenshot?</p>

---

## Post #5 by @nysfour (2022-11-11 15:56 UTC)

<p>I am working with color jpgs, and am trying to segment a portion of the image containing a medical subject. Ideally, a growing bubble could be used because manual segmentation, even with the brush, is still not efficient when segmenting high image volumes.</p>

---

## Post #6 by @lassoan (2022-11-11 19:35 UTC)

<p>What kind of color jpgs (photos of the skin, histology slides, …) do you work with? What is the “medical subject”? It is important for us to know what the problem you want to solve for two reasons:</p>
<ul>
<li>We can tell if there are relevant tools in Slicer that you can use.</li>
<li>If there is no good solution yet then we know that there is some unmet user need and (especially if others request similar features, too) we improve our tools/add new tools accordingly.</li>
</ul>

---

## Post #7 by @nysfour (2022-11-12 00:32 UTC)

<p>The medical subject is a human and it is a color image of skin, and the aim is to segment the subject so that the mask can be overlayed thermal images taken concurrently to get the ground truth thermal signature and prevent any radiant heat from affecting the signature of the subject.</p>

---

## Post #8 by @lassoan (2022-11-12 04:05 UTC)

<p>Thank you for the additional details.</p>
<p>Currently, Segment Editor module always uses the first component of a multi-component image (R channel in an RGB image), so if you want to use a different channel or a combination of channels then you need to convert the vector volume to a scalar (for example, using “Vector to scalar volume” module).</p>
<p>For highlighting similar regions, you can try these effects (they work on single-slice images):</p>
<ul>
<li>Level tracing</li>
<li>Flood filling (provided by SegmentEditorExtraEffects extension)</li>
</ul>
<p>If they are not sufficient then you may experiment with filters in SimpleITK, using the Simple Filters module. You may post a few images to the <a href="https://discourse.itk.org/">ITK forum</a> to get ideas on what filters could be used for (semi)automatic segmentation. Maybe itk-growcut (that was implemented based on Slicer’s “Grow from seeds” segment editor effect) can be used on single-slice images.</p>

---

## Post #9 by @nysfour (2022-11-12 07:06 UTC)

<p>Thank you very much! I greatly appreciate it</p>

---
