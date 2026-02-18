# Change spatial calibration

**Topic ID**: 13605
**Date**: 2020-09-22
**URL**: https://discourse.slicer.org/t/change-spatial-calibration/13605

---

## Post #1 by @ricounet67 (2020-09-22 12:13 UTC)

<p>I would like to know if it is possible to change the spatial calibration of a volume in Slicer.<br>
I import a tiff stack from a tomography reconstruction made with TomoJ (in ImageJ). I didn’t found the way to set the voxel size.<br>
Thank you</p>

---

## Post #2 by @lassoan (2020-09-22 13:00 UTC)

<p>This documentation section explains how you can import and calibrate an image stack: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html?highlight=jpg#load-a-series-of-png-jpeg-or-tiff-images-as-volume">https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html?highlight=jpg#load-a-series-of-png-jpeg-or-tiff-images-as-volume</a></p>

---

## Post #3 by @ricounet67 (2020-09-25 06:17 UTC)

<p>Thank you, as I understand this step is at the importation of the tiff stack. But one the model is generated and saved into a VTK file is it still possible to change the spatial calibration?</p>

---

## Post #4 by @Andinet_Enquobahrie (2020-09-25 12:47 UTC)

<p>Yes, you can use the Volume Information Panel to modify the image properties ( you just have to be careful when you do this as this will affect all your subsequent quantitative computations)</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#panels-and-their-use" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#panels-and-their-use" target="_blank" rel="noopener nofollow ugc">Volumes — 3D Slicer  documentation</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @ricounet67 (2020-09-25 14:42 UTC)

<p>It doesn’t seems to work with a model.<br>
When I open my VTK file, it is considered as a model and I don’t have the possibility to change the scale.</p>

---

## Post #6 by @lassoan (2020-09-25 15:44 UTC)

<p>You can easily scale models using Surface Toolbox module.</p>
<p>If you want to transform volumes and images together then it is easier to use Transforms module: create transform, set scaling factors in the diagonal values in the transformation matrix, apply transform to all nodes (models, volumes, markups, segmentations, …), then harden transform on all nodes.</p>

---
