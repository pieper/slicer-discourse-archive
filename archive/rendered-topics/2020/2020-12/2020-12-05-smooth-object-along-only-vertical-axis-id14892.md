# Smooth object along only vertical axis

**Topic ID**: 14892
**Date**: 2020-12-05
**URL**: https://discourse.slicer.org/t/smooth-object-along-only-vertical-axis/14892

---

## Post #1 by @LuckyLuke (2020-12-05 05:51 UTC)

<p>I saw this post a month ago or so and I am wondering about the same thing:</p><aside class="quote quote-modified" data-post="1" data-topic="14613">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/noobforslicer/48/10900_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/smoothing-effect-only-in-1-axis/14613">Smoothing effect only in 1 axis</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    is it possible to have smoothing effect only affect the one axis, the one that vertically goes through slices. 
In other words, if the resolution of a slice is good but slices were spaced a lot,  if the 2mm or 3mm smooth is applied, it affects all directions, that way resolution in the slice is sadly lost. 
so is there an option to smooth only 1 direction? 

for example add extra slices between these and make a voxel through interplation 
Or
somehow manouver 3D models to be smoothen only in 1 di…
  </blockquote>
</aside>

<p>I have horizontal images in really nice resolution but they are spaced quite a lot 2mm!</p>
<p>Now interest is to preserve the horizontal details but somehow smoothen the transition in one axis from one slice to another.</p>
<p>That way it will not look like a stacked one upon another high res images but indeed will look like 1 model. Sure details will theoretically alwazs be missing in that axis but who cares if it looks nice?! right?</p>
<p>However this what Mustafa wrote is not understandable for me.</p>
<p>HE mentioned some “simple filters” what is that?</p>
<p>And what does he mean by a “scalar” volume?</p>

---

## Post #2 by @LuckyLuke (2020-12-05 05:51 UTC)

<p>As Murat has suggested I am trying to use smart filters but I have no idea which median or gaussian filter to choose in order to smooth object in one axis only.</p>
<p>also have no idea where do I select the axis?</p>
<p>muratmaga, please assist!?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42be5bcc83eac7b18b689e1d58d55431b09aa87f.png" data-download-href="/uploads/short-url/9wrlYuwvppJK5J0YmXDA9jZhBMz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42be5bcc83eac7b18b689e1d58d55431b09aa87f_2_638x500.png" alt="image" data-base62-sha1="9wrlYuwvppJK5J0YmXDA9jZhBMz" width="638" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42be5bcc83eac7b18b689e1d58d55431b09aa87f_2_638x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42be5bcc83eac7b18b689e1d58d55431b09aa87f_2_957x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42be5bcc83eac7b18b689e1d58d55431b09aa87f.png 2x" data-dominant-color="F0F3F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1260×987 31.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @NoobForSlicer (2020-12-05 06:09 UTC)

<p>I think you are from the same dormitory as I am.</p>
<p>I think I figured out the way in 3ds max how to do this… to lock the information in 2 axis and just modify objects in 1 axis. But one would require license and where I do internship not allowed to use illegal license software.</p>
<p>Are you doing the same internship?</p>

---

## Post #4 by @NoobForSlicer (2020-12-05 06:10 UTC)

<p>I am not sure what muratmaga was saying about croping volume is true.</p>

---

## Post #5 by @LuckyLuke (2020-12-05 06:18 UTC)

<p>yes I am on the third floor.</p>
<p>I think we were given similar datasets</p>

---

## Post #6 by @LuckyLuke (2020-12-05 06:19 UTC)

<p>Problem with that is quite a lot of effort to imoprt and export modify.</p>
<p>Maybe something about filters he was saying would be of help.</p>
<p>Also I don’t like 3ds max paid solutions, I prefer open source alternatives if they exist. Always support open source.</p>

---

## Post #7 by @muratmaga (2020-12-05 06:30 UTC)

<p>As you can see there are three radius fields, one for each axis. If you want to smooth only in the Z direction. Enter 0,0, and whatever the radius you want for Z.</p>

---

## Post #8 by @lassoan (2020-12-05 06:42 UTC)

<p>I gave a solution <a href="https://discourse.slicer.org/t/smoothing-effect-only-in-1-axis/14613/13">here</a> that preserves all details in-plane and interpolates smoothly in between. I would recommend to use this very carefully, because it may make the result look higher resolution than it actually is and therefore potentially mislead users.</p>
<p>The correct solution is to acquire proper images that contain all the details you need.</p>

---

## Post #9 by @NoobForSlicer (2020-12-05 07:04 UTC)

<p>I am trying to do this but volume is missing in the drop down menu<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10d2cc90edb6bbdc5156108fe301c2fbe8b32147.png" data-download-href="/uploads/short-url/2oPh17VrfApBbm2uZjFDdUi37Xp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10d2cc90edb6bbdc5156108fe301c2fbe8b32147_2_637x500.png" alt="image" data-base62-sha1="2oPh17VrfApBbm2uZjFDdUi37Xp" width="637" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10d2cc90edb6bbdc5156108fe301c2fbe8b32147_2_637x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10d2cc90edb6bbdc5156108fe301c2fbe8b32147_2_955x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10d2cc90edb6bbdc5156108fe301c2fbe8b32147_2_1274x1000.png 2x" data-dominant-color="F0F0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1352×1060 37.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the data I have loaded it in twice though<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc410d2e8af13b95f1c172d06c1dd561eaaa6451.png" data-download-href="/uploads/short-url/vqspLRknHlJiaySMI8vxsaxKMjn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc410d2e8af13b95f1c172d06c1dd561eaaa6451.png" alt="image" data-base62-sha1="vqspLRknHlJiaySMI8vxsaxKMjn" width="690" height="304" data-dominant-color="FAF6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">760×335 8.43 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What could be the problem?</p>

---

## Post #10 by @muratmaga (2020-12-05 07:05 UTC)

<p>You chose a binaryFilter, which I presume expects a labelmap. Is your volume a labelmap?</p>

---

## Post #11 by @NoobForSlicer (2020-12-05 07:08 UTC)

<p>Helo Lassoan, since I was unable to get the SmartFilters to work yet, I can not tell exactly if I want this solution or not.</p>
<p>My main objective is exactly that, once exported as OBJ, it should look prettier. Whether information in between is missing or not is completely irrelevant for this case.</p>
<p>But I don’t know what these “filters” are since can’t get them to run. Maybe they are just some illusion and once exported as OBJ it would still look the same?!</p>
<p>First have to try to make this SmartFilters work but yes, what you have described is exactly what I need, the problem is that images are not segmented manually but with threshold. We cannot tell threshold to skip the slices gained through interpolation.</p>

---

## Post #12 by @NoobForSlicer (2020-12-05 07:11 UTC)

<p>no, it is a simple png sequences processed somewhere to have only the organ of interest and background is white.</p>
<p>I loaded it tried it nothing appears.<br>
Loaded it as nrrd tried it nothing appears<br>
changed filter to image filter, still not there<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd8efbde547aaaf2546f5d607c2d755249e91c12.png" data-download-href="/uploads/short-url/r2UAaGrXOlHmuVMQ1ClJHf3YKf8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd8efbde547aaaf2546f5d607c2d755249e91c12.png" alt="image" data-base62-sha1="r2UAaGrXOlHmuVMQ1ClJHf3YKf8" width="690" height="457" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1053×698 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2020-12-05 07:12 UTC)

<p>Don’t worry about the filters, you don’t need them (they would produce much worse looking result). Just insert blank slices between the segmented ones, convert to segmentation, and fill the gaps using “Fill between slices”.</p>

---

## Post #14 by @NoobForSlicer (2020-12-05 07:13 UTC)

<p>sounds like a good idea! I would need a script that would create blank slices! That is a great solution but can be achieved!! Thank you so much. That will be it indeed.</p>

---

## Post #15 by @NoobForSlicer (2020-12-05 07:16 UTC)

<p>I can not choose which slice spacing to make because these scans were already made and images processed somehow for some purposes. I am just doing my part here and then have to present a couple of dozens of segmentations somewhere and that is it. Normally I do not need to make them look pretty.</p>

---

## Post #16 by @NoobForSlicer (2020-12-05 07:24 UTC)

<p>I will do what you said but it would require much more ram and dealing with preprocessing those pngs <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> but yes what you have shown is exactly what I need, thank  you million times over.</p>

---
