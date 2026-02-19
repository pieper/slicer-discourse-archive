---
topic_id: 2469
title: "Working With Large Datasets"
date: 2018-03-29
url: https://discourse.slicer.org/t/2469
---

# Working with large datasets

**Topic ID**: 2469
**Date**: 2018-03-29
**URL**: https://discourse.slicer.org/t/working-with-large-datasets/2469

---

## Post #1 by @arumiat (2018-03-29 13:05 UTC)

<p>Hi all, I have the luck of having some really nice high-res / microCT scans to work with. They are around the 1-2GB mark as original .dcms &amp; if loaded into fijiJ show up as 16bit individual images. I can get the sizes down of course by</p>
<ul>
<li>cropping the area of interest</li>
<li>then resizing each images x/y to 256x256</li>
<li>saving as an 8bit JPG</li>
</ul>
<p>But this still leaves me often with a 70MB file(if saved as nifti) or folder of imags</p>
<p><a href="https://youtu.be/z_R7zyILIPw" rel="nofollow noopener">I’m loading these across the web</a> <strong>so it would be good to get them down even further, if possible</strong>.</p>
<p>Do any of you have any tips for getting small image sizes whilst maintaining as high image quality as possible? Happy to explore Slicers abilities, as well as other methods you may have heard of (am familiar w fiji/imageJ)</p>
<p>Thanks!<br>
T<br>
PS love the new forums =)</p>

---

## Post #2 by @lassoan (2018-03-30 01:42 UTC)

<p>You can crop and downsample further using Crop volumes module. If file size matters, use compression (nrrd, mha use lossless compression with not too high compression ratio).</p>
<p>What is the reason you need to reduce data size? What specific constraints you have? What information do you need to preserve?</p>

---

## Post #3 by @arumiat (2018-03-30 11:10 UTC)

<p>Hi Andras thanks.</p>
<p>In essence</p>
<ol>
<li>we have built a browser-based medical imaging viewer</li>
<li>with the aim of having a reference library of studies for our users of both normal and pathological conditions</li>
</ol>
<p>Our desire:<br>
So ideally we’d like</p>
<ul>
<li>these studies to load across the internet as quickly as possible,</li>
<li>whilst maintaining as much detail as the originals as possible</li>
</ul>
<p>we can currently load .dcm and .nifti files into our imagine viewer. If you think nrrd and mha might offer some benefits related to the above, we can look at adding this ability too?</p>

---

## Post #4 by @ihnorton (2018-03-30 13:48 UTC)

<aside class="quote no-group" data-username="arumiat" data-post="3" data-topic="2469">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f05b48/48.png" class="avatar"> arumiat:</div>
<blockquote>
<p>these studies to load across the internet as quickly as possible,<br>
whilst maintaining as much detail as the originals as possible</p>
</blockquote>
</aside>
<p>The approach in most digital pathology software is to generate several tiled layers at multiple resolutions – typically 3-7 depending on the raw resolution (some microscopy modalities can generate 100GB+ images). The client gets the lowest-resolution version first as a preview, and then subsets of each layer (only the tiles in view) are served on-demand and stitched on the client, as the user zooms in and moves around. That way you are transferring at-most a few screens worth of data at a time. Over a LAN the latency is not noticeable, and over a decent internet connection on the same continent the approach should be very usable. If you are trying to serve to global users you should make sure that requesting new tiles takes exactly 1 round-trip, because latency over satellite (or e.g. BOS-SYD) can be several-hundred ms, and that will add up quickly if your client is chatty.</p>
<p>For research use the above approach should be fine. For clinical diagnostics there may be stricter requirements because you can’t have a radiologist accidentally look at a lossy image. But I have seen a similar approach from a well-known vendor where the un-loaded parts of an image were rendered immediately, but unusably blurry, in order to make the client feel more responsive.</p>
<p>It’s been a while since I worked in this area, but there are a few open source projects you could look at – the one I remember is <a href="https://openseadragon.github.io/">OpenSeaDragon</a>, which some microscopy groups have used. Kitware had a viewer built from scratch too, but I don’t remember the name.</p>

---

## Post #5 by @fedorov (2018-03-30 21:42 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/DigitalSlideArchive/HistomicsTK">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/DigitalSlideArchive/HistomicsTK" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/d0168a3719c799fa2ee4def6e291592f8b59d649152de0a1a6cb056908f63168/DigitalSlideArchive/HistomicsTK" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/DigitalSlideArchive/HistomicsTK" target="_blank" rel="noopener">GitHub - DigitalSlideArchive/HistomicsTK: A Python toolkit for pathology...</a></h3>

  <p>A Python toolkit for pathology image analysis algorithms. - GitHub - DigitalSlideArchive/HistomicsTK: A Python toolkit for pathology image analysis algorithms.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @pieper (2018-03-31 17:05 UTC)

<p>Are there any suggestions or existing projects for efficiently serving multiresolution high-res 3D data, like the microCT that <a class="mention" href="/u/arumiat">@arumiat</a> wants to work with?</p>

---

## Post #7 by @timeanddoctor (2018-04-02 02:24 UTC)

<p>Hi, Dear arumiat<br>
I am a doctor and recently I was looking for a Micro-CT(DICOM) of the knee joint of Mice, for Morphological Education. But nothing was found from internet. In this post, it seems to be a Micro-CT. And could you have a copy-sharing for me and my students. My <a href="mailto:Email:timeandoctor3@163.com">Email:timeandoctor3@163.com</a>.<br>
And I would be appreciat if anyone can tell me something about a free download link of knee joint of Mice by Micro-CT.<br>
Thanks.<br>
Li Zhenzhu,</p>

---

## Post #8 by @arumiat (2018-04-02 08:14 UTC)

<p>Thanks all =).</p>
<p>Isaiah &amp; Andrey I will take a look at that. It seems perhaps a little complex for our needs but I will investigate it some more and see if it might help to some degree.</p>
<p>Yes Steve would be great if anyone knows of projects or workflows that manage to do what we’re trying to do already.</p>
<p>I can do some tests to see what happens to our current sequences when saved as nrrd / mha as well.</p>
<p>Currently the studies are around 700x700px and 1800 slices in the Z. I can also resample the data in the z-direction in Slicer right? I would be happy to double or triple the slice thickness on these studies to reduce the number of images in the Z axis, as this would save volume significantly right? I need to look at the resample module in Slicer for this right?</p>

---

## Post #9 by @lassoan (2018-04-02 13:19 UTC)

<p>Probably Crop volume module is the most suitable for reducing extent and spacing of a volume. I recommend resample to isotropic spacing if you plan to visualize your image in 3D.</p>

---

## Post #10 by @arumiat (2018-04-03 16:13 UTC)

<p>Thanks I will try Andras.</p>
<p>Li Zhenzhu we don’t have any mice microCT unfortunately. You can perhaps contact a laboratory and ask them to donate a specimen post-mortem, which you can then send to a local commercial microCT scanner?</p>

---

## Post #11 by @timeanddoctor (2018-04-04 15:02 UTC)

<p>Thank you for your repply.<br>
I am going to medical teaching in my hospital after reconstructed by 3d slicer.<br>
I also try to get help from our medical university laboratory in which has a microCT scanner maching.</p>

---
