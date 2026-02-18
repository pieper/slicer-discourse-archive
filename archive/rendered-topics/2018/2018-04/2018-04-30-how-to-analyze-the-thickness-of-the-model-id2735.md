# How to analyze the thickness of the model

**Topic ID**: 2735
**Date**: 2018-04-30
**URL**: https://discourse.slicer.org/t/how-to-analyze-the-thickness-of-the-model/2735

---

## Post #1 by @timeanddoctor (2018-04-30 13:56 UTC)

<p>Can I analyze the thickness of a stl model, and then get a color map.<br>
The distance between the two sides of an object.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f30db8dfcca7916c3e14fd4f2352892d08d820cd.jpeg" data-download-href="/uploads/short-url/yG9qloLYxb6loylPiGjv2zcuQax.jpeg?dl=1" title="2018-04-30_215013" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f30db8dfcca7916c3e14fd4f2352892d08d820cd_2_690x293.jpeg" alt="2018-04-30_215013" data-base62-sha1="yG9qloLYxb6loylPiGjv2zcuQax" width="690" height="293" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f30db8dfcca7916c3e14fd4f2352892d08d820cd_2_690x293.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f30db8dfcca7916c3e14fd4f2352892d08d820cd_2_1035x439.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f30db8dfcca7916c3e14fd4f2352892d08d820cd.jpeg 2x" data-dominant-color="76757A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2018-04-30_215013</span><span class="informations">1366×582 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-05-01 16:04 UTC)

<p>“Thickness” is not a very well defined term for models (surface meshes), but for shell-like meshes it is probably not too difficult to estimate it robustly and accurately.</p>
<p>Potential approaches:</p>
<p>A. Extract medial surface and estimate thickness as 2x of distance from medial surface. There are various ways of computing these in Slicer. One possible workflow:</p>
<ul>
<li>Compute medial surface using <strong>Simple Filters module - BinaryThinningImageFilter</strong>.</li>
<li>Compute distance map using <strong>Simple Filters module - DanielssonDistanceMapImageFilter</strong>. Input is binary: Yes; Use image spacing: Yes.</li>
<li>Copy distance values from the distance map to model node using <strong>Probe volume with model</strong> module.</li>
</ul>
<p>Critical part is the medial surface extraction. If you find that it is not accurate enough then you may to use smaller voxel sizes for the model-&gt;labelmap conversion, or use a different medial surface extraction method (for example, medial surface extractor in VMTK or <a href="https://github.com/timhutton/vtkpowercrust">PowerCrust algorithm</a>).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/2352e218fd3bb74629d3c8fd3d10969880c1f06e.png" data-download-href="/uploads/short-url/52uhQE7xrGtVY3JJBHJTGs2fWXk.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/2352e218fd3bb74629d3c8fd3d10969880c1f06e_2_690x391.png" alt="image" data-base62-sha1="52uhQE7xrGtVY3JJBHJTGs2fWXk" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/2352e218fd3bb74629d3c8fd3d10969880c1f06e_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/2352e218fd3bb74629d3c8fd3d10969880c1f06e_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/2352e218fd3bb74629d3c8fd3d10969880c1f06e.png 2x" data-dominant-color="979391"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1272×721 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>B. Implement a custom algorithm in C++. Something like this should be very easy to implement if you are already familiar with C++ programming using VTK: <a href="http://mmmanual.com/thickness/">http://mmmanual.com/thickness/</a>.</p>

---

## Post #3 by @ALoopingIcon (2020-06-25 07:52 UTC)

<p>Another possibility is to use MeshLab to compute the Shape Diameter Function (SDF) that is  a good generic definition of the <em>thickness</em>  of a mesh.</p>
<aside class="onebox stackexchange">
  <header class="source">
      <a href="https://stackoverflow.com/questions/61787028/how-to-calculate-the-thickness-of-a-mesh/62198280#62198280" target="_blank" rel="nofollow noopener">stackoverflow.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/212800/aloopingicon" target="_blank" rel="nofollow noopener">
    <img alt="ALoopingIcon" src="https://www.gravatar.com/avatar/79265ff3220d6a12d366b2444869cbe5?s=128&amp;d=identicon&amp;r=PG" class="thumbnail onebox-avatar" width="60" height="60">
  </a>
<h4>
  <a href="https://stackoverflow.com/questions/61787028/how-to-calculate-the-thickness-of-a-mesh/62198280#62198280" target="_blank" rel="nofollow noopener">How to calculate the thickness of a mesh</a>
</h4>

<div class="tags">
  <strong>textures, texture-mapping, cad</strong>
</div>

<div class="date">
  
  answered by
  <a href="https://stackoverflow.com/users/212800/aloopingicon" target="_blank" rel="nofollow noopener">
    ALoopingIcon
  </a>
  on <a href="https://stackoverflow.com/questions/61787028/how-to-calculate-the-thickness-of-a-mesh/62198280#62198280" target="_blank" rel="nofollow noopener">03:23PM - 04 Jun 20 UTC</a>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @TNgyn (2023-12-12 10:07 UTC)

<p>Hello,</p>
<p>I’m trying to analyze the thickness of a brain structure which is already segmented.<br>
Can you maybe explain the steps of option A in more detail?<br>
For example: What is the input volume and input model of the Probe volume with model module?</p>

---
