# Model is not showing

**Topic ID**: 4104
**Date**: 2018-09-13
**URL**: https://discourse.slicer.org/t/model-is-not-showing/4104

---

## Post #1 by @Ghaddy (2018-09-13 16:42 UTC)

<p>Hi</p>
<p>I have another promblem with tool intensity segmenter.<br>
Once i am done after hitting apply… the model is not showing on the top right (3d view)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3466a5f0bb18a16a0f586b6e95b25f79f14dff3.jpeg" data-download-href="/uploads/short-url/u91BRVXtgPHfL94zjn3P5bRiTF9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3466a5f0bb18a16a0f586b6e95b25f79f14dff3_2_666x500.jpeg" alt="image" data-base62-sha1="u91BRVXtgPHfL94zjn3P5bRiTF9" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3466a5f0bb18a16a0f586b6e95b25f79f14dff3_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3466a5f0bb18a16a0f586b6e95b25f79f14dff3_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3466a5f0bb18a16a0f586b6e95b25f79f14dff3_2_1332x1000.jpeg 2x" data-dominant-color="6A8BA3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×1200 259 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Is therr any thing i can do?</p>
<p>Thank you</p>

---

## Post #2 by @cpinter (2018-09-13 16:51 UTC)

<p>Labelmaps cannot be shown in 3D. You need to convert it to a model or segmentation node.</p>

---

## Post #3 by @Ghaddy (2018-09-13 17:16 UTC)

<p>Yes I usually save the file then open it again in Itk-snap and do the segmentation then open it again in 3d slicer and use model maker tool to creat a modrl and save it as .vtk.</p>
<p>But i thought i should get a 3d model in that tap!</p>
<p>Thank you very much</p>

---

## Post #4 by @lassoan (2018-09-13 17:19 UTC)

<p>Where this intensity segmenter module comes from? If it provides features that are not covered by existing Segment Editor effects then it could be made into a Segment Editor effect with not too much effort.</p>
<aside class="quote no-group" data-username="Ghaddy" data-post="3" data-topic="4104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/3bc359/48.png" class="avatar"> Ghaddy:</div>
<blockquote>
<p>open it again in Itk-snap and do the segmentation</p>
</blockquote>
</aside>
<p>Since the introduction of Segment Editor module, you should be able to do in Slicer most (or all) segmentation work that previously you had to do in other software. Let us know if you need any help with this.</p>

---

## Post #5 by @cpinter (2018-09-13 17:30 UTC)

<aside class="quote no-group" data-username="Ghaddy" data-post="3" data-topic="4104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/3bc359/48.png" class="avatar"> Ghaddy:</div>
<blockquote>
<p>open it again in Itk-snap and do the segmentation</p>
</blockquote>
</aside>
<p>The Segment Editor module in Slicer can do what ITK-Snap can do and more. Please try it, because this workflow jumping back and forth sounds awfully inconvenient.</p>

---

## Post #6 by @Ghaddy (2018-09-13 17:41 UTC)

<p>Thank you very much!<br>
I will try it… is there any vedio or instruction that can help step by step?</p>
<p>Thanks again and I appreciate your help</p>

---

## Post #7 by @cpinter (2018-09-13 18:08 UTC)

<p>Yes, there are a bunch of tutorials:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></p>
<p>A few others:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <a href="https://lassoan.github.io/SlicerSegmentationRecipes/" target="_blank">SlicerSegmentationRecipes</a>
  </header>
  <article class="onebox-body">
    

<h3><a href="https://lassoan.github.io/SlicerSegmentationRecipes/" target="_blank">SlicerSegmentationRecipes</a></h3>

<p>Recipes for solving common segmentation tasks using 3D Slicer</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #8 by @Ghaddy (2018-09-13 18:18 UTC)

<p>Awesome resource! Thank you</p>

---
