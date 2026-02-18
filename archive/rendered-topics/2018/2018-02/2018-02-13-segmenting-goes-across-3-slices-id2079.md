# Segmenting goes across 3 slices

**Topic ID**: 2079
**Date**: 2018-02-13
**URL**: https://discourse.slicer.org/t/segmenting-goes-across-3-slices/2079

---

## Post #1 by @tnguyen (2018-02-13 15:42 UTC)

<p>Hi everyone,<br>
I was using Paint Effect in Segment Editor and I noticed that the area that I painted on 1 slice also appears on the next two adjacent slices (if I try to erase this area on these two slices, it will also erase the painted area on the first slice too)</p>
<p>Windows<br>
Version: 4.8.1<br>
Expected behavior: Area painted on one slice will be only on that slice<br>
Actual behavior: Area painted on one slice also appears on the next two adjacent slice</p>
<p>I appreciate any input on how to go about this issue, thank you!</p>

---

## Post #2 by @cpinter (2018-02-13 16:01 UTC)

<p>I can imagine two reasons:</p>
<ol>
<li>The image you segment is non-axis-aligned. After a quick search I found <a href="https://discourse.slicer.org/t/display-issue-with-rt-structs-and-mr-volume/546">this thread</a>. Please check if this is the case.</li>
<li>The Spere brush option is enabled and it also paints on adjacent slices</li>
</ol>

---

## Post #3 by @tnguyen (2018-02-13 16:14 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="2079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>this thre</p>
</blockquote>
</aside>
<p>Thanks for response Csaba, could you link the thread again? I can’t click it for some reasons</p>

---

## Post #4 by @JoostJM (2018-02-13 16:55 UTC)

<p>Additionally, it is also possible the master volume on which you are segmenting has different spacing than the volume currently selected in your viewer.</p>

---

## Post #5 by @cpinter (2018-02-13 17:26 UTC)

<p>I fixed the link, sorry about that.</p>
<p><a class="mention" href="/u/joostjm">@JoostJM</a> also has a good point. If you selected a master volume and then switched, the geometry of the original master volume is used. In that case create a new segmentation and choose the volume with the geometry you want to have.</p>

---

## Post #6 by @tnguyen (2018-02-13 18:02 UTC)

<p>After checking the images again per your suggestions, I found that it may be because my master image thickness is 3 mm and the slice thickness at the viewing panel was at 1 mm. After I reset the thickness to 3 mm, the painted area stays within 1 slice. Thank you for helping me solve this!</p>

---

## Post #7 by @DAT_Minh (2020-12-06 14:43 UTC)

<p>Hello. I have the same problem with you but I can’t imagine the steps you go through. Can you post screen shot on where to see and adjust master image thickness and slice thickness? Thank you.</p>

---

## Post #8 by @manjula (2020-12-06 15:30 UTC)

<p>Please check if this is the case and will resolve your problem with this,<br>
1.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">
  <header class="source">

      <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" target="_blank" rel="noopener nofollow ugc">3D Slicer segmentation recipes</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" target="_blank" rel="noopener nofollow ugc">Overview</a></h3>

  <p>Recipes for common medical image segmentation tasks using 3D Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<ol start="2">
<li>
<p>Check if the Sphere brush is on and that is not the effect you want.</p>
</li>
<li>
<p>View Slice thickness</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b443b1e2a91e78c1e9974666eca4ce02510a03a.png" data-download-href="/uploads/short-url/hAsUBp6sKnOw52idDGLzBc8orV0.png?dl=1" title="Screenshot from 2020-12-06 16-35-46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b443b1e2a91e78c1e9974666eca4ce02510a03a_2_690x388.png" alt="Screenshot from 2020-12-06 16-35-46" data-base62-sha1="hAsUBp6sKnOw52idDGLzBc8orV0" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b443b1e2a91e78c1e9974666eca4ce02510a03a_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b443b1e2a91e78c1e9974666eca4ce02510a03a_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b443b1e2a91e78c1e9974666eca4ce02510a03a_2_1380x776.png 2x" data-dominant-color="9293A4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-12-06 16-35-46</span><span class="informations">1920×1080 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @DAT_Minh (2020-12-06 16:57 UTC)

<p>Thank you very much. That’s a very straightforward and detailed work flow. Nice to have your respond.</p>

---
