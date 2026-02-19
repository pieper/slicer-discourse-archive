---
topic_id: 38099
title: "Visualizing The Neutral Axis On Segment Geometry"
date: 2024-08-28
url: https://discourse.slicer.org/t/38099
---

# Visualizing the neutral axis on segment geometry

**Topic ID**: 38099
**Date**: 2024-08-28
**URL**: https://discourse.slicer.org/t/visualizing-the-neutral-axis-on-segment-geometry/38099

---

## Post #1 by @CristianK (2024-08-28 20:42 UTC)

<p>Hi <a class="mention" href="/u/jmhuie">@jmhuie</a></p>
<p>I was wondering if it would be possible to plot the neutral axis on the structure cross-section when aligned with the principal axis. I am comparing structures that vary considerably in cross-section shape and would be interesting to visualize where exactly the neutral axis is being positioned.</p>
<p>I also have a doubt regarding the custom neutral axis option. Since I am working with 3D surfaces generated in another software, which I import as .ply files into 3D slicer, it seems that I am not able to work with the custom neutral axis, right? Is there a way to allow for the definition of a custom neutral axis without needing to segment the structure in 3D slicer?</p>
<p>With best regards, and thanks in advance,</p>
<p>Cristian.</p>

---

## Post #2 by @jmhuie (2024-08-29 16:53 UTC)

<aside class="quote no-group" data-username="CristianK" data-post="1" data-topic="38099">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/35a633/48.png" class="avatar"> CristianK:</div>
<blockquote>
<p>I was wondering if it would be possible to plot the neutral axis on the structure cross-section when aligned with the principal axis. I am comparing structures that vary considerably in cross-section shape and would be interesting to visualize where exactly the neutral axis is being positioned.</p>
</blockquote>
</aside>
<p>Unfortunately this is currently no method for visualizing the major and minor axes. You can use BoneJ in ImageJ if you really need to visualize the neutral axes</p>
<aside class="quote no-group" data-username="CristianK" data-post="1" data-topic="38099">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/35a633/48.png" class="avatar"> CristianK:</div>
<blockquote>
<p>Is there a way to allow for the definition of a custom neutral axis without needing to segment the structure in 3D slicer?</p>
</blockquote>
</aside>
<p>There is! Because Segment Geometry requires certain inputs you just need to convert your .ply files into the right formats. Here are the steps how to do that: <a href="https://github.com/jmhuie/SlicerBiomech/tree/main/Tutorials/SegmentGeometry#using-a-pre-made-mesh" class="inline-onebox" rel="noopener nofollow ugc">SlicerBiomech/Tutorials/SegmentGeometry at main · jmhuie/SlicerBiomech · GitHub</a></p>

---

## Post #3 by @CristianK (2024-08-30 13:06 UTC)

<p>Thanks <a class="mention" href="/u/jmhuie">@jmhuie</a> ,</p>
<p>I followed those steps to measure the cross-section parameters, but I was not allowed to customize the neutral axis. When I check this option, nothing happens, no axis appears that allows me to move and so on. I was only able to align with the principal axes.</p>

---

## Post #4 by @jmhuie (2024-09-05 16:19 UTC)

<p><a class="mention" href="/u/cristiank">@CristianK</a> what version of Slicer are you running? If you send me your scene, I can try trouble shooting.</p>

---

## Post #6 by @jmhuie (2024-09-05 20:09 UTC)

<aside class="quote no-group" data-username="CristianK" data-post="5" data-topic="38099">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/35a633/48.png" class="avatar"> CristianK:</div>
<blockquote>
<p>I attached the scene file here (<a href="https://drive.google.com/file/d/1dyRkwIJZlf4eV7XT9x7ROOBPlv2Uwq9J/view?usp=sharing" rel="noopener nofollow ugc">2024-09-05-Scene.mrml - Google Drive</a>) but I realized that I got several warnings and errors in the process, which may help to explain what is happening wrong.</p>
</blockquote>
</aside>
<p>Thanks for sharing but I actually need all of the files for your Scene. When you go to save the scene, if you change the format to .mrb it’ll save the Scene and all the associated files in a single file.</p>

---

## Post #8 by @CristianK (2024-09-11 13:53 UTC)

<p>Hi Jonathan,</p>
<p>Sorry for the late reply, but the fact is that I am having several troubles to save the file. When I use a .ply mesh to measure cross-section data, I am not able to save the scene in a single file, because I get some errors and warnings. Then I saved every file separately and uploaded it (<a href="https://drive.google.com/drive/folders/1QUPksX78V6ZvXSK0WEekSvlafoc6O3EU?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">scene - Google Drive</a>), along with a print with the errors (Imagem1 from the previous link). I also tried to segment the structure in 3D Slicer and used segment geometry, but surprisingly I was also not able to customize the neutral axis. The slider to change the neutral axis position opens, but I am not allowed to move it. I also uploaded this scene here (<a href="https://drive.google.com/file/d/1IUXKZ6pFihQ685tDIJNMtc4NT1AcRfqf/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">2024-09-09-M.tibialis.mrb - Google Drive</a>), and in this case, I was able to save it as .mrb.</p>
<p>I also uploaded the .ply file I am using (<a href="https://drive.google.com/file/d/1V4P6dMgKyZSyNT2NTf3K95kWd5WkPlVw/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">M.tibialis_oriented.ply - Google Drive</a>).</p>
<p>Let me know if you need something else.</p>
<p>In all cases, I was able to measure cross-section properties, and when I checked the “Use custom neutral axis” button it generated additional data that seemed to be related to this function, but I wasn’t able to customize it. This fact, along with the errors while trying to save the scene makes me wonder if what I am measuring is reliable or not.</p>
<p>Many thanks again for looking into it.</p>

---

## Post #9 by @jmhuie (2024-09-19 00:05 UTC)

<p>Posting an answer for perpetuity.</p>
<p>With the PLY file, as of Slicer 5.6.2 (not in 5.6.1) you need to perform an extra step. After you convert the binary label map as a scalar volume, you then need to go to the Segment Editor module and set the “Source Volume” of your segmentation as the scalar volume. After that, the neutral axis should work.</p>

---
