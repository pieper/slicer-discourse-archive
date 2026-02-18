# Convert.dcm to .ply , is it possible?

**Topic ID**: 28133
**Date**: 2023-03-02
**URL**: https://discourse.slicer.org/t/convert-dcm-to-ply-is-it-possible/28133

---

## Post #1 by @dsa934 (2023-03-02 04:28 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>Hi , slicer users !</p>
<p>I want to directly convert it to .ply to import both the modeling information and texture information of the dcm file exported from 3shape, but I know that if there is no decryption key, I have to use brute force.</p>
<p>Is the decryption work possible in 3d slicer?</p>
<p>The meaning of the .dcm file is as follows:</p>
<ul>
<li>not dicom file(CT) ,  3 shape’s export type</li>
</ul>

---

## Post #2 by @lassoan (2023-03-02 07:01 UTC)

<p>Sorry, I find it very hard to understand what you would like to do. What outputs you can export from 3shape, in which file format? Can you provide an example file? (upload it somewhere and post the link here)</p>

---

## Post #3 by @dsa934 (2023-03-02 09:42 UTC)

<p>Hi, <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be8d8ed6f9d4700841c6e31ac90f2d9cc8077599.jpeg" data-download-href="/uploads/short-url/rbI0mNT2mryAgOWGAZHOncf0WDf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be8d8ed6f9d4700841c6e31ac90f2d9cc8077599_2_626x499.jpeg" alt="image" data-base62-sha1="rbI0mNT2mryAgOWGAZHOncf0WDf" width="626" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be8d8ed6f9d4700841c6e31ac90f2d9cc8077599_2_626x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be8d8ed6f9d4700841c6e31ac90f2d9cc8077599_2_939x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be8d8ed6f9d4700841c6e31ac90f2d9cc8077599.jpeg 2x" data-dominant-color="DADBDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">992×792 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>(ref. <a href="https://www.youtube.com/watch?v=xN80A7kRmHA" class="inline-onebox" rel="noopener nofollow ugc">Convert dcm files into stl with 3shape - YouTube</a> )</p>
<p>There are many ways to convert DCM 3D Model file to STL file.<br>
However, texture information cannot be used in this case.</p>
<p>So, I want to convert directly from DCM 3D Model file to .ply to utilize the texture information.</p>
<p>is it possible to 3D slicer ?</p>

---

## Post #4 by @whu (2023-03-02 10:49 UTC)

<p>maybe you can try to convert the .stl or the .nrrd format to .ply<br>
there is the full opensource c code for reading and writing to .ply<br>
may it help.</p>

---

## Post #5 by @dsa934 (2023-03-02 23:22 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="3" data-topic="28133">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>There are many ways to convert DCM 3D Model file to STL file.<br>
However, texture information cannot be used in this case.</p>
<p>So, I want to convert directly from DCM 3D Model file to .ply to utilize the texture information.</p>
</blockquote>
</aside>
<p><strong>Convert ‘.dcm’ to ‘.ply’</strong></p>

---

## Post #6 by @lassoan (2023-03-03 05:47 UTC)

<p>I’m not sure if there is a way to store textured surface mesh in standard DICOM information object. Even if there is, 3shape probably uses private fields instead, as it allows them to lock people into using their software and charge extra for various data export features.</p>
<p>If they don’t offer textures surface mesh export (or it is not affordable) then you can reverse-engineer the contents of the private fields. However, they can change the private fields at anytime and they can make it very hard to decipher the private field contents if they want to.</p>
<p>Overall, probably your best options are either</p>
<ul>
<li>A. pay for the appropriate data export features in 3shape, or</li>
<li>B: switch to a more open, more affordable system</li>
</ul>

---

## Post #7 by @gahe (2024-01-19 04:49 UTC)

<p>Hi Andras<br>
I am new to Slicer, but the software is very good and intuitive, and on top, one find nearly all the answers here in the forum if somethings comes up. Pretty cool!<br>
And it was clear that, when I faced the same problem like the OP had, I would find the answer here.<br>
So back to the start:<br>
It seems, and my research on the internet confirmed this, that 3shape uses a proprietary file system. Unfortunately, the academic institution where I work lacked the necessary expertise for such matters and invested in this closed system to establish an archive with thousands of scanned plaster casts (and is still working on it). On the other hand, 3shape, as always, seems to have only seen the money and sold the system.<br>
Now we researchers are the ones bearing the brunt of it. The models in the archive folder are accessible, but worthless because, for further processing, one has to export each model into the .stl format by hand, using a 3shape software.<br>
Therefore, a “walk through” on how to bypass this system would be immensely helpful. Unfortunately, this is far beyond my knowledge, but I would be willing to provide a scan, if someone wants to give a try.<br>
We would be very, very grateful for the help.</p>

---

## Post #8 by @jirkatosta (2025-01-04 12:25 UTC)

<p>Hello,</p>
<p>I believe the confusion here is because of DCM file extension is used for two completely different file formats.</p>
<ol>
<li>DICOM files, which Slicer can open and convert into something else.</li>
<li>3Shape intra-oral scanner file format, containing textured meshes. And this format is unknown to Slicer. Please try other mesh-processing software instead, e.g. MeshInspector <a href="https://meshinspector.com/" rel="noopener nofollow ugc">https://meshinspector.com/</a> that can open DCM meshes and resave them as Stl, Obj or Ply.</li>
</ol>

---

## Post #9 by @Ayberk_Yagiz (2025-01-09 09:00 UTC)

<p>You can use this link to convert 3shape DCM files to .stl</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://allonguide.com/index.php/convert-3shape-dcm-to-stl-format/">
  <header class="source">
      <img src="https://i0.wp.com/allonguide.com/wp-content/uploads/2021/09/cropped-favicon.png?fit=32%2C32&amp;ssl=1" class="site-icon" width="32" height="32">

      <a href="https://allonguide.com/index.php/convert-3shape-dcm-to-stl-format/" target="_blank" rel="noopener nofollow ugc" title="01:43AM - 05 December 2024">All on Guide - Surgical Guides for All – 5 Dec 24</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:300/53;"><img src="https://allonguide.com/wp-content/uploads/2021/09/allonguide_logo300x53.jpg" class="thumbnail" width="300" height="53"></div>

<h3><a href="https://allonguide.com/index.php/convert-3shape-dcm-to-stl-format/" target="_blank" rel="noopener nofollow ugc">Convert .dcm Intra Oral Scan File to .stl Format - All on Guide</a></h3>

  <p>Do your customers keep sending you 3Shape DCM files even though you don’t have a 3Shape membership? No problem! Upload your files using the form below, and we’ll convert them to .STL files for you. You’ll receive the converted files via email within...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
