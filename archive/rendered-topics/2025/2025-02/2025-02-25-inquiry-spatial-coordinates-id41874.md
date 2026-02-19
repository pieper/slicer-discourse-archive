---
topic_id: 41874
title: "Inquiry Spatial Coordinates"
date: 2025-02-25
url: https://discourse.slicer.org/t/41874
---

# Inquiry Spatial Coordinates

**Topic ID**: 41874
**Date**: 2025-02-25
**URL**: https://discourse.slicer.org/t/inquiry-spatial-coordinates/41874

---

## Post #1 by @MPARHAM (2025-02-25 17:21 UTC)

<p>Hi everyone,</p>
<p>Glad to be back on the forum and hope everyone had a great start to this year.</p>
<p>I had a question about exporting files and coordinate systems in 3D Slicer. My objective is to recreate the segmentation used in 3D slicer in MATLAB. Which I am able to do as seen below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08371824bf00572518666a175dc56dfe14f75265.jpeg" data-download-href="/uploads/short-url/1aFRf9i2KRaYnWPl81kTbLo8g6h.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08371824bf00572518666a175dc56dfe14f75265_2_690x382.jpeg" alt="image" data-base62-sha1="1aFRf9i2KRaYnWPl81kTbLo8g6h" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08371824bf00572518666a175dc56dfe14f75265_2_690x382.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08371824bf00572518666a175dc56dfe14f75265_2_1035x573.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08371824bf00572518666a175dc56dfe14f75265.jpeg 2x" data-dominant-color="C7CAD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1063×589 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I understand that for Slicer the coordinate system is in RAS, but when exported in NRRD it is transformed to the LPS System as this coordinate system is more recognizable with other software. I wanted to check if the transformation from both coordinate system were accurate and analyze in MATLAB.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88d5db0358c4eacd4c01652fabdd1ffce7f18803.jpeg" data-download-href="/uploads/short-url/jwv7oF610AMeZXtxqJCRy8Tlfgv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88d5db0358c4eacd4c01652fabdd1ffce7f18803_2_690x329.jpeg" alt="image" data-base62-sha1="jwv7oF610AMeZXtxqJCRy8Tlfgv" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88d5db0358c4eacd4c01652fabdd1ffce7f18803_2_690x329.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88d5db0358c4eacd4c01652fabdd1ffce7f18803_2_1035x493.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88d5db0358c4eacd4c01652fabdd1ffce7f18803_2_1380x658.jpeg 2x" data-dominant-color="DFE0DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1627×776 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In my methodology, I was able to bring the points in the nrrd file and graph them to replicate Slicer’s visual display. However, one issue I am having is that the points are off by 1 pixels usually in the x, in the y or both.</p>
<p>For example, in the picture above I placed my cursor at both identical points in slicer and in my code and although they are similar, the MATLAB algorithm is 1 point off. In Slicer the coordinates for that corner are 118, 135, 61.</p>
<p>For my algorithm it read 119, 136, and 62. Luckily, for the middle value all of the other coordinates for this segmentation is reading the same layer and I am still able to duplicate the segmentation.</p>
<p>I cannot think of anyone why this is happening, but if anyone else had a thought it would be greatly appreciated.</p>
<p>Thank you,<br>
Melton  Parham</p>

---

## Post #2 by @muratmaga (2025-02-25 17:32 UTC)

<aside class="quote no-group" data-username="MPARHAM" data-post="1" data-topic="41874">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mparham/48/70304_2.png" class="avatar"> MPARHAM:</div>
<blockquote>
<p>I cannot think of anyone why this is happening, but if anyone else had a thought it would be greatly appreciated.</p>
</blockquote>
</aside>
<p>Rounding error? In slicer coordinates are continuous, there is no guarantee that you place the point in exactly on a specific IJK coordinate in image grid. Maybe try turning off the interpolation in Slicer and see if helps.</p>

---

## Post #3 by @jamesobutler (2025-02-25 17:36 UTC)

<p>Is this a Matlab 1 indexing method compared against 0 indexing method?</p>

---

## Post #4 by @MPARHAM (2025-02-25 17:50 UTC)

<p>Hi, that’s a great point! Thank you for clarifying that the points I’m selecting may not be exact. I went to Volumes &gt; Display and turned off interpolation to ensure the pixel I’m on matches the expected position. I believe this is part of the issue, so I really appreciate your help!</p>

---

## Post #5 by @MPARHAM (2025-02-25 17:52 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="41874" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Is this a Matlab 1 indexing method compared against 0 indexing method?</p>
</blockquote>
</aside>
<p>Hi James, to ensure clarity 3D slicer is 0 indexing method? If so that also explains the 1 point off. MATLAB indexing does begin at 1 and that would explain why each point is slightly off but still similar.</p>

---

## Post #6 by @jamesobutler (2025-02-25 21:07 UTC)

<p>Python and C++ (Which is what Slicer uses) is using 0 indexing. You can confirm that your dataset also has a 0,0,0 location. As you can see in my image below I was able to find the 0 index of IJK using the Data Probe and the MRHead sample dataset.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a8a7e11142518b3bab8ba0494e9fb21ae7637a2.png" data-download-href="/uploads/short-url/aDq3c1qtokFsfK9fVxr4hQyyx1g.png?dl=1" title="{B10FC4B6-9738-471A-A873-4383920AACA3}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a8a7e11142518b3bab8ba0494e9fb21ae7637a2.png" alt="{B10FC4B6-9738-471A-A873-4383920AACA3}" data-base62-sha1="aDq3c1qtokFsfK9fVxr4hQyyx1g" width="427" height="141"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{B10FC4B6-9738-471A-A873-4383920AACA3}</span><span class="informations">427×141 1.96 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @MPARHAM (2025-02-25 21:16 UTC)

<p>You are correct. Indexing is 0,0,0 and MATLAB’s indexing begins at 1.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d3e06e261355f3b2ac587f48cc30526f7187591.png" data-download-href="/uploads/short-url/diRioIUlK0XLSrwIwBko8BgOGFH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d3e06e261355f3b2ac587f48cc30526f7187591.png" alt="image" data-base62-sha1="diRioIUlK0XLSrwIwBko8BgOGFH" width="607" height="310"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">607×310 57.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also I would like to say that 3D slicer’s community is very responsive and helpful. Thank you both <a class="mention" href="/u/jamesobutler">@jamesobutler</a>  &amp; <a class="mention" href="/u/muratmaga">@muratmaga</a> for you insights. They were both very helpful.</p>

---
