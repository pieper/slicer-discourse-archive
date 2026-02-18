# Pixelated 3D view in Volume Rendering 

**Topic ID**: 15605
**Date**: 2021-01-20
**URL**: https://discourse.slicer.org/t/pixelated-3d-view-in-volume-rendering/15605

---

## Post #1 by @mlaw-migalig (2021-01-20 15:22 UTC)

<p>I loaded data via SlicerMorph SkyscanReconImport.</p>
<p>I go to Volume Rendering and slide the shift bar, everything as as usual, I reveal the bones I am interested in, but then the 3D render becomes pixelated blocks in the 3D view - I have attached a picture for reference.<br>
When moving the 3D view, the image is in good resolution, but when it is stationary the large pixels occur again.<br>
What could be the cause of this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cbc4db1978f7dc69ce6eaee241261b5cae2aa21.jpeg" data-download-href="/uploads/short-url/k50hCApT2I1ftlJ8mxyETKPinO9.jpeg?dl=1" title="103908_VolumeRender" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8cbc4db1978f7dc69ce6eaee241261b5cae2aa21_2_513x499.jpeg" alt="103908_VolumeRender" data-base62-sha1="k50hCApT2I1ftlJ8mxyETKPinO9" width="513" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8cbc4db1978f7dc69ce6eaee241261b5cae2aa21_2_513x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8cbc4db1978f7dc69ce6eaee241261b5cae2aa21_2_769x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cbc4db1978f7dc69ce6eaee241261b5cae2aa21.jpeg 2x" data-dominant-color="272728"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">103908_VolumeRender</span><span class="informations">920×895 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-01-20 18:43 UTC)

<p>This looks like a graphics driver bug. What CPU, graphics card, and operating system do you use? What is the size of your volume? What is your Slicer version? Do you see any errors or warnings in the application log (menu: Help / Report a bug)?</p>

---

## Post #3 by @muratmaga (2021-01-20 19:02 UTC)

<aside class="quote no-group" data-username="mlaw-migalig" data-post="1" data-topic="15605">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mlaw-migalig/48/9617_2.png" class="avatar"> mlaw-migalig:</div>
<blockquote>
<p>I loaded data via SlicerMorph SkyscanReconImport.</p>
</blockquote>
</aside>
<p>Can you send a screenshot of the volumes dialog box and a copy of the *Rec.log file you used to import the volume? I want to rule out the unit issue (micron to mm)…</p>

---

## Post #4 by @mlaw-migalig (2021-01-21 14:05 UTC)

<p>Is this screenshot adequate?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/455d57d130cbe780a52826f4252280c2a9ea4244.png" data-download-href="/uploads/short-url/9TCVMzXTp7lOMQAZM6NMxmY1do8.png?dl=1" title="103908_VolumeInfo_reclog.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/455d57d130cbe780a52826f4252280c2a9ea4244_2_690x383.png" alt="103908_VolumeInfo_reclog.png" data-base62-sha1="9TCVMzXTp7lOMQAZM6NMxmY1do8" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/455d57d130cbe780a52826f4252280c2a9ea4244_2_690x383.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/455d57d130cbe780a52826f4252280c2a9ea4244_2_1035x574.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/455d57d130cbe780a52826f4252280c2a9ea4244_2_1380x766.png 2x" data-dominant-color="EAEAEB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">103908_VolumeInfo_reclog.png</span><span class="informations">1921×1068 388 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @mlaw-migalig (2021-01-21 14:16 UTC)

<p>CPU: AMD Ryzen 7 5800X<br>
GPU: Nvidia GeForce RTX 3090<br>
Using Windows 64-bit</p>

---

## Post #6 by @muratmaga (2021-01-21 15:58 UTC)

<aside class="quote no-group" data-username="mlaw-migalig" data-post="4" data-topic="15605">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mlaw-migalig/48/9617_2.png" class="avatar"> mlaw-migalig:</div>
<blockquote>
<p>Is this screenshot adequate?</p>
</blockquote>
</aside>
<p>Yes, and based on these I see that SkyscanReconImport did correctly read the voxel sizes and units (5 micron). So it can be a rendering bug as <a class="mention" href="/u/lassoan">@lassoan</a> mentioned. If you can share the stack as a zip file, I can try the rendering with a RTX Titan, although normally Geforce’s usually work fine.</p>
<p>I also suggest setting the Rendering Quality to Normal from the default adaptive and see if that helps.</p>

---

## Post #7 by @mlaw-migalig (2021-01-21 19:15 UTC)

<p>Even as a zip file, the data is 6.6GB. Do you have a different suggestion for sharing the data?<br>
Thank you for all these comments to troubleshoot, I am still very much a beginner ^^’</p>

---

## Post #8 by @muratmaga (2021-01-21 19:23 UTC)

<p>People typically upload to a cloud sharing site (google drive, onedrive etc) and then share the link, that’s the preferred method.</p>
<p>Alternatively you can upload here, but then it is only going to be shared by me and slicermorph team.<br>
<a href="https://faculty.washington.edu/maga/data_dropbox/" class="onebox" target="_blank" rel="noopener nofollow ugc">https://faculty.washington.edu/maga/data_dropbox/</a></p>

---

## Post #9 by @mlaw-migalig (2021-01-21 21:34 UTC)

<p><a href="https://drive.google.com/file/d/19XhOvs4_6VAwLiZq4HhAN-XO-tOeZsgR/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/19XhOvs4_6VAwLiZq4HhAN-XO-tOeZsgR/view?usp=sharing</a></p>

---

## Post #10 by @muratmaga (2021-01-22 00:01 UTC)

<p>It is not publicly shared, asking for permission.</p>

---

## Post #11 by @muratmaga (2021-01-22 16:38 UTC)

<aside class="quote no-group" data-username="mlaw-migalig" data-post="9" data-topic="15605" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mlaw-migalig/48/9617_2.png" class="avatar"> mlaw-migalig:</div>
<blockquote>
<p><a href="https://drive.google.com/file/d/19XhOvs4_6VAwLiZq4HhAN-XO-tOeZsgR/view?usp=sharing">https://drive.google.com/file/d/19XhOvs4_6VAwLiZq4HhAN-XO-tOeZsgR/view?usp=sharing </a></p>
</blockquote>
</aside>
<p>I downloaded this from google drive, but the zip file seems corrupt, I can’t unzip it.</p>

---

## Post #12 by @mlaw-migalig (2021-01-25 12:02 UTC)

<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1n6gOLYcO61zc649zHQbXJC0kqYiaaBxL/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1n6gOLYcO61zc649zHQbXJC0kqYiaaBxL/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1n6gOLYcO61zc649zHQbXJC0kqYiaaBxL/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">21322_oraljaw.zip</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I hope this will work. I found a smaller data file that showed the same output.</p>
<ol>
<li>Loading using SlicerMorph - during Volume Rendering, pixelation of the image is seen in the 3D view when stationary.</li>
<li>When I load the series of png files using the drag/drop and unselecting ‘Single File’ - during Volume Rendering, the 3D view shows a black box that turns grey when manipulating the ‘Shift’ bar.</li>
</ol>
<p>Thank you in advance.</p>

---

## Post #13 by @muratmaga (2021-01-25 17:17 UTC)

<aside class="quote no-group" data-username="mlaw-migalig" data-post="12" data-topic="15605">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mlaw-migalig/48/9617_2.png" class="avatar"> mlaw-migalig:</div>
<blockquote>
<p>I hope this will work. I found a smaller data file that showed the same output.</p>
</blockquote>
</aside>
<p>I am checking this.</p>
<aside class="quote no-group" data-username="mlaw-migalig" data-post="12" data-topic="15605">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mlaw-migalig/48/9617_2.png" class="avatar"> mlaw-migalig:</div>
<blockquote>
<p>When I load the series of png files using the drag/drop and unselecting ‘Single File’ - during Volume Rendering, the 3D view shows a black box that turns grey when manipulating the ‘Shift’ bar.</p>
</blockquote>
</aside>
<p>Yes, that’s expected. If you use the default data load menu in Slicer, PNG is treated as an RGB image, and it is not rendered. You need to use the <code>VectorToScalarVolume</code> to be able to render this. <code>ImageStacks</code> or <code>SkyscanReconImport</code> in SlicerMorph does this automatically.</p>

---

## Post #14 by @muratmaga (2021-01-25 17:34 UTC)

<aside class="quote no-group" data-username="mlaw-migalig" data-post="12" data-topic="15605">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mlaw-migalig/48/9617_2.png" class="avatar"> mlaw-migalig:</div>
<blockquote>
<p>Loading using SlicerMorph - during Volume Rendering, pixelation of the image is seen in the 3D view when stationary.</p>
</blockquote>
</aside>
<p>I imported the data both via <code>ImageStacks</code> and <code>SkyscanReconImport</code> SlicerMorph modules, and cannot replicate the issue (see below). My laptop doesn’t have sufficient GPU RAM to render this in full resolution, so I did have to downsample a bit. Anyways, the issue is not the import or the data.</p>
<p>So going back to the rendering problem, it is possible a driver issue as <a class="mention" href="/u/lassoan">@lassoan</a> indicated above. Do you have the latest drivers for your Geforce 3090?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b6447089acf3e8662839064b21751ef68732fe9.jpeg" alt="image" data-base62-sha1="1CM5VLSOd94IzfbvqVd7PvnByUF" width="396" height="430"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35e3bce18556f64f4e65792a893eea1c45f6ccb5.jpeg" alt="image" data-base62-sha1="7GJenDi3Hr4WoWiAa7JvYDacVc9" width="367" height="439"></p>

---

## Post #15 by @mlaw-migalig (2021-01-27 15:48 UTC)

<p>The 2 lines of warning I get are the following:<br>
[WARNING][Qt] 27.01.2021 16:21:56 [] (unknown:0) - libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
[WARNING][Qt] 27.01.2021 16:22:00 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile</p>
<p>The 1 line of error is:<br>
[ERROR][VTK] 27.01.2021 16:23:11 [vtkITKArchetypeDiffusionTensorImageReaderFile (0000016515E34FE0)] (D:\D\S\Slicer-0\Libs\vtkITK\vtkITKArchetypeDiffusionTensorImageReaderFile.cxx:166) - There is more than one file, use the vtkITKArchetypeImageSeriesReader instead.</p>
<p>In terms of driver for GeForce RTX 3090, I have version 461.40.</p>
<p>I uploaded this data via drag/drop and used the VectorToScalarVolume as <a class="mention" href="/u/muratmaga">@muratmaga</a> suggested and there is no pixelation in the Volume Rendering, so I will continue to use this for now.</p>

---

## Post #16 by @muratmaga (2021-01-27 18:57 UTC)

<p>Whatever the reason for the artifact was, it wasn’t due to the <code>SkyScanReconImport</code> or <code>ImageStacks</code>. As I can’t replicate this with a RTX Titan, full resolution volume renders perfectly fine after importing it via <code>SkyscanReconImport</code> .</p>
<p>You can continue to use the default image stack loading mechanism in Slicer, but you will have to do that VectorToScalar conversion everytime you do the import, plus you will have to enter the correct image spacing. These are taken care of during the import time if you <code>ImageStack</code> and even more automatically if you use the <code>SkyscanReconImport</code> (all you have to do is to point out to the log file and it will obtain the spacing etc). That’s why we developed those two modules.</p>

---

## Post #17 by @lassoan (2021-01-28 03:48 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="16" data-topic="15605">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Whatever the reason for the artifact was, it wasn’t due to the <code>SkyScanReconImport</code> or <code>ImageStacks</code> .</p>
</blockquote>
</aside>
<p>We actually cannot be sure about this. If the image renders consistently well with the default ITK importer and not with the other modules then something might go wrong during the import. For example, there may be subtle differences in file sorting, or which method is used for grayscale conversion (luminance, average, single channel, …), etc. It could worth some more investigation.</p>

---

## Post #18 by @muratmaga (2021-01-28 05:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="15605">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We actually cannot be sure about this. If the image renders consistently well with the default ITK importer and not with the other modules then something might go wrong during the import. For example, there may be subtle differences in file sorting, or which method is used for grayscale conversion (luminance, average, single channel, …), etc. It could worth some more investigation.</p>
</blockquote>
</aside>
<p>We tested this quite a bit, and we are not aware of any issues. These are all single channel images to begin with, which default data load mechanism turns it into a multichannel image, in which all channels are identical. So regardless of what conversion you use, you end up in the same place you begin with.</p>
<p>What I wanted to test with that dataset is whether the voxel size read correctly from the log file with SkyscanReconImport. That’s a user customizable field in the Nrecon software and there are a number of prefixes that shows up in the log file over the years (mm, um, micron). And because voxel size seems to impact the 3D rendering quality in Slicer, I thought that might be an issue. It wasn’t.</p>
<aside class="quote no-group" data-username="mlaw-migalig" data-post="1" data-topic="15605">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mlaw-migalig/48/9617_2.png" class="avatar"> mlaw-migalig:</div>
<blockquote>
<p>When moving the 3D view, the image is in good resolution, but when it is stationary the large pixels occur again.</p>
</blockquote>
</aside>
<p>I think this is rendering related.</p>

---

## Post #19 by @lassoan (2021-01-28 05:35 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="18" data-topic="15605">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>And because voxel size seems to impact the 3D rendering quality in Slicer, I thought that might be an issue. It wasn’t.</p>
</blockquote>
</aside>
<p>I did some tests on two computers and it seems that you are right. If the voxel size is very small, such as in this image, then “Adaptive” quality mode of GPU volume rendering results in pixelated rendering when camera stops (full-quality image is worse than coarse quality). I check if there is an easy fix, but if it is not trivial then we can check again after the VTK9 update (that may fix it).</p>
<p><strong>Setting quality mode to “Normal” fixes the issue.</strong></p>
<p>“Normal” quality level is currently the default, but if an older Slicer version created the default settings then the default level was set to “Adaptive”.</p>

---

## Post #20 by @muratmaga (2021-01-28 05:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="19" data-topic="15605">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>“Normal” quality level is currently the default, but if an older Slicer version created the default settings then the default level was set to “Adaptive”.</p>
</blockquote>
</aside>
<p>Thanks Andras. That adaptive setting has been causing quite a bit of issues, particularly for new users. It is particularly troublesome, if they install a new release but because the default settings were carried from older one, they still have to live with “adaptive”. Personally, including an integrated GPUs, I haven’t seen a use case where adaptive makes sense.</p>
<p>Can this be overwritten automatically with a new install?</p>

---
