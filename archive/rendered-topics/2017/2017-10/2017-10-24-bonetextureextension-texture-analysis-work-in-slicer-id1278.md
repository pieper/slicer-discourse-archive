---
topic_id: 1278
title: "Bonetextureextension Texture Analysis Work In Slicer"
date: 2017-10-24
url: https://discourse.slicer.org/t/1278
---

# BoneTextureExtension: Texture Analysis Work in Slicer

**Topic ID**: 1278
**Date**: 2017-10-24
**URL**: https://discourse.slicer.org/t/bonetextureextension-texture-analysis-work-in-slicer/1278

---

## Post #1 by @bpaniagua (2017-10-24 19:31 UTC)

<blockquote>
<p>Dear Professor Beatriz:<br>
Sorry to bother you! I am really meeting some problems with 3DSlicer. May I ask you a few questions？</p>
<ol>
<li>I want to use HeterogeneityCAD modules to obtain texture features, but it is not in the module list. Module list like follow:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9986f5b48ec1f2dd23258192e2f6b67a21ce04db.png" data-download-href="/uploads/short-url/lUacAhzXh1dr4lJk65BEkH6rGcz.png?dl=1" title="Attachment"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9986f5b48ec1f2dd23258192e2f6b67a21ce04db_2_628x500.png" alt="Attachment" data-base62-sha1="lUacAhzXh1dr4lJk65BEkH6rGcz" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9986f5b48ec1f2dd23258192e2f6b67a21ce04db_2_628x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9986f5b48ec1f2dd23258192e2f6b67a21ce04db_2_942x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9986f5b48ec1f2dd23258192e2f6b67a21ce04db_2_1256x1000.png 2x" data-dominant-color="F2F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Attachment</span><span class="informations">2038×1622 534 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
How could I import this model.？</li>
<li>Could I use .png or .off data as my input data? It always shows error when I import data.<br>
Thanks,<br>
Miao</li>
</ol>
</blockquote>
<p>Hi Miao,</p>
<p>Thanks so much for your email, I hope you dont mind I respond to your email in the Slicer forum.</p>
<ol>
<li>
<p>I am not aware of HeterogeneityCAD modules, do you mean <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/BoneTextureExtension">BoneTexture extension</a>?</p>
</li>
<li>
<p>It is possible to load png data into Slicer. Specifically for analysis in the BoneTextureExtension you will need to save/export that image into nrrd or other volumetric image formats.</p>
</li>
</ol>
<p>Please provide a bit more of info, and I/the rest of the Slicer community will try to do our best to help.<br>
Best,</p>
<p>Bea</p>

---

## Post #2 by @fedorov (2017-10-24 20:07 UTC)

<p>HeterogeneityCAD is an extension, not a core module - you will first need to install it using ExtensionManager.</p>
<p>You can also consider looking into the Radiomics extension that provides the Slicer interface to the pyradiomics library, which can be used to calculate ~1500 features: <a href="http://pyradiomics.readthedocs.io/en/latest/">http://pyradiomics.readthedocs.io/en/latest/</a></p>
<p>cc: <a class="mention" href="/u/joostjm">@JoostJM</a></p>

---

## Post #3 by @jbvimort (2017-10-24 20:15 UTC)

<p>The BoneTexture Extension is not able to compute textural features for 2D images, it only can be used for 3D scans in Slicer.</p>
<p>Therefore you can consider using the itk_texturefeatures python package that contain filter able to compute 1st order, Run Length an Co-occurrence textural features and textural feature maps for 2D and 3D images and can easily be intalled: pip install itk_texturefeatures.</p>
<p>More informations and code examples can be found here:<br>
<a href="http://www.insight-journal.org/browse/publication/985" class="onebox" target="_blank" rel="nofollow noopener">http://www.insight-journal.org/browse/publication/985</a><br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/InsightSoftwareConsortium/ITKTextureFeatures" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/319479?s=400&amp;v=4" class="thumbnail onebox-avatar" width="300" height="300">

<h3><a href="https://github.com/InsightSoftwareConsortium/ITKTextureFeatures" target="_blank" rel="nofollow noopener">InsightSoftwareConsortium/ITKTextureFeatures</a></h3>

<p>Fast, Texture Feature Maps from N-Dimensional Images - InsightSoftwareConsortium/ITKTextureFeatures</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #4 by @Miao_Fan (2017-10-25 03:36 UTC)

<p>Got it. It works. Thank you!</p>

---

## Post #5 by @Miao_Fan (2017-10-25 03:37 UTC)

<p>I have install itk_texturefeature. How could I use it?</p>

---

## Post #6 by @Miao_Fan (2017-10-25 13:06 UTC)

<p>The BoneTexture Extension is not able to compute textural features for 2D images, it only can be used for 3D scans in Slicer. But I need to deal with 2D images. Is there any module can compute 2D images?</p>

---

## Post #7 by @jbvimort (2017-10-25 13:15 UTC)

<p>You can find some python code examples here:</p>
<ul>
<li>For the run length features: <a href="https://github.com/jbvimort/ITKTextureFeatures/blob/AllowingFloat/example/computeGLRLMFeatures.py" rel="nofollow noopener">https://github.com/jbvimort/ITKTextureFeatures/blob/AllowingFloat/example/computeGLRLMFeatures.py</a>
</li>
<li>For the co-occurrence features: <a href="https://github.com/jbvimort/ITKTextureFeatures/blob/AllowingFloat/example/computeGLCMFeatures.py" rel="nofollow noopener">https://github.com/jbvimort/ITKTextureFeatures/blob/AllowingFloat/example/computeGLCMFeatures.py</a>
</li>
</ul>
<p>Those two examples are for 3D images but it’s easy to adapt them in order to work with 2D images by moving dimension from 3 to 2 in each code.</p>

---

## Post #8 by @Miao_Fan (2017-10-25 15:05 UTC)

<p>I could obtain .off files which contain 3D points. Is there any function that can output a .nrrd file?</p>

---

## Post #9 by @lassoan (2017-10-27 02:22 UTC)

<p>You can always create 3D volume from a “2D” image (single-slice 3D image) by resampling. Probably the simplest is to use CropVolume module for that.</p>

---
