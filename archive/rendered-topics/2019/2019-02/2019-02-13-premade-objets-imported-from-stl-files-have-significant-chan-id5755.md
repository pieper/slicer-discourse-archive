---
topic_id: 5755
title: "Premade Objets Imported From Stl Files Have Significant Chan"
date: 2019-02-13
url: https://discourse.slicer.org/t/5755
---

# PreMade Objets imported from STL files have significant changes when imported as segmentations

**Topic ID**: 5755
**Date**: 2019-02-13
**URL**: https://discourse.slicer.org/t/premade-objets-imported-from-stl-files-have-significant-changes-when-imported-as-segmentations/5755

---

## Post #1 by @apparrilla (2019-02-13 13:39 UTC)

<p>Hi everyone,</p>
<p>I´m trying to make something simillar to your video tutorial " How to segment multiple vertebrae in spine CT for 3D printing" and I get in trouble with this feature.</p>
<p>I import objets from STL files to get them as segmentations and interact them with the CT bone segmentations.</p>
<p>When I get the inicial segmentation from importing from Model, its surface is almost perfect. Problems became when I try to edit this segmentation or when I try to apply logical operators between them. Representation of the segmentations change from “Closed surface” to “Binary labelmap” and surface quality decrese drastically.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01552ede97abc3025a498f50a956d482c3c53837.jpeg" data-download-href="/uploads/short-url/bMYQrOghGae3l1rW5E0kH83DLN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01552ede97abc3025a498f50a956d482c3c53837_2_627x499.jpeg" alt="image" data-base62-sha1="bMYQrOghGae3l1rW5E0kH83DLN" width="627" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01552ede97abc3025a498f50a956d482c3c53837_2_627x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01552ede97abc3025a498f50a956d482c3c53837_2_940x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01552ede97abc3025a498f50a956d482c3c53837_2_1254x998.jpeg 2x" data-dominant-color="847F8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1814×1445 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Grey: Original object (Model view)<br>
Yellow: Inicial Segmentation from Model<br>
Brown: Segmentation after trying to edit</p>
<p>As you can easily imagine, substractions of these segmentations to other from TC make inaccurate surfaces.</p>
<p>Is there any way to edit segmentations without changing to " Binary labelmap"?</p>
<p>Thanks on advance…</p>

---

## Post #2 by @pieper (2019-02-13 18:11 UTC)

<p>A lot of editing operations are possible or are only well-behaved on label maps and not on surface models, which is why Slicer converts on the fly as needed (boolean operations on surface meshes are notoriously subject to failure due to rounding errors in non-trivial cases).</p>
<p>Typically you can get better results by defining a higher resolution grid for your conversion of surfaces to label maps, and also by adjusting the smoothing when creating surfaces from the label maps.</p>

---

## Post #3 by @apparrilla (2019-02-13 19:41 UTC)

<p>I was pretty convinced the problem was label map conversion. Excuse me Steve, but I have no idea have to practice your solution… How can I improve my grid resolution for conversion? Should be any problem with scales making this change?<br>
The main editing operation I have to make is logical operator effect (substraction and copy/add) so boolean operation is the main point.<br>
Thanks for your help…</p>

---

## Post #4 by @pieper (2019-02-13 20:33 UTC)

<p>Probably the easiest way to do this is to use a volume to define a reference grid (e.g. using the sample data if you don’t have anything else) and then use the Segmentation Geometry dialog (small button to the right of the Master volume selector) and make the segmentation finer (like a 2x or 3x oversample).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a18afcd9960273b9fd25391975a8cfe2712fbae.png" data-download-href="/uploads/short-url/f8zvbjO6pX1J8twFt9bZprodSdU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a18afcd9960273b9fd25391975a8cfe2712fbae_2_690x372.png" alt="image" data-base62-sha1="f8zvbjO6pX1J8twFt9bZprodSdU" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a18afcd9960273b9fd25391975a8cfe2712fbae_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a18afcd9960273b9fd25391975a8cfe2712fbae_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a18afcd9960273b9fd25391975a8cfe2712fbae_2_1380x744.png 2x" data-dominant-color="D6D9D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1438×776 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Maybe <a class="mention" href="/u/lassoan">@lassoan</a> or <a class="mention" href="/u/cpinter">@cpinter</a> can suggest how to do this without using a volume to define the grid.</p>

---

## Post #5 by @cpinter (2019-02-13 21:32 UTC)

<p>If I understand the problem, then I just described the solution earlier today to someone else (it’s enough to just look at the bullet points):</p><aside class="quote quote-modified" data-post="2" data-topic="5756">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/difficulty-with-editing-new-segments-imported-as-stl-files/5756/2">Difficulty with editing new segments imported as stl files</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In your second screenshot you cannot edit because there is no anatomical volume selected. That’s why Segment Editor is asking you to “Select master volume to enable editing”, as shown in your screenshot as well. 
In the third case, I can see a master volume. If that “6: CHEST…” image occupies the same space in 3D as your imported STL, then you should be able to edit it. You can verify that by going to Volume Rendering and showing the CT in 3D. 
If “chaos breaks loose” means what you described ne…
  </blockquote>
</aside>

<p>It’s not the easiest workflow I know, but right now this is the best way to do it.</p>

---

## Post #6 by @apparrilla (2019-02-13 22:45 UTC)

<p>I really appreciate your help guys.<br>
I read your other answer <a class="mention" href="/u/cpinter">@cpinter</a>  and i was trying to follow your instructions but Threshold Effect of CT from DICOMS became … I got strange surfaces in 3D… I supposed i was doing something wrong… Anyway, surfaces from STL files (its segmentations) change from perfect to ugly when I touch “Surface Smoothing” check and i was unable to came back to right visualization…</p>
<p>I´m trying <a class="mention" href="/u/pieper">@pieper</a> solution and it looks the path… It improves machine needs and for any oversample over 2x, program crash when I put Show 3D button on. I have made a volumen crop throw a ROI and then oversample it till 5x. Surface quality after Threshold Effect is much better and results of substract Operator is better too.</p>
<p>It´s a bit tricky workflow and really cost demanding for the system resources but …</p>
<p>Thanks so much both.<br>
Any other idea will be appreciated…</p>

---
