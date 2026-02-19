---
topic_id: 30427
title: "Cta Brain Extraction Skull Stripping"
date: 2023-07-06
url: https://discourse.slicer.org/t/30427
---

# CTA Brain Extraction / Skull Stripping

**Topic ID**: 30427
**Date**: 2023-07-06
**URL**: https://discourse.slicer.org/t/cta-brain-extraction-skull-stripping/30427

---

## Post #1 by @Arpan_Gyawali (2023-07-06 08:43 UTC)

<p>I have a task of extracting Brain or removing skull from a brain CTA scans. To train the model first of all i need to label the mask. I am using 3D slicer segment editor for it. The process I am following is as explained in <a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/" rel="noopener nofollow ugc">Overview | 3D Slicer segmentation recipes (lassoan.github.io)</a> :</p>
<ul>
<li>Threshold: 300 to max</li>
<li>Margin grow by 1.02mm</li>
<li>Keep largest island</li>
<li>And finally extracting largest cavity using wrap solidify<br>
After these steps, still the segmentation is not that good, so I am manullly using paint and eraser tool to refine the segmentation. But the main problem is, in the brain CTA its very frustating for me to distinguish whether the particular region is blood vessel or the contrast or the bone. I have been doing this for about 1 months now but still i couldnt do it properly.<br>
Do someone has some suggestion for me? Is there s perfect window level and width for distinguishing them? Or is there any other methods?<br>
I have tried 40,80 window and here the vessels and bone has almost same contrast and also using 150,450 window, but in 3D slicer i cannot exactly provide the window value.</li>
</ul>
<p>I would be very happy if someone helped me.</p>

---

## Post #2 by @rbumm (2023-07-06 09:18 UTC)

<p>Let the SwissSkullStripper do the job.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lassoan/SlicerSwissSkullStripper">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lassoan/SlicerSwissSkullStripper" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/29ec48227b953aca96ee445bf9f273e355241efc67676a9c879ed97701ba9c01/lassoan/SlicerSwissSkullStripper" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lassoan/SlicerSwissSkullStripper" target="_blank" rel="noopener">GitHub - lassoan/SlicerSwissSkullStripper: Slice4 extension for the Swiss...</a></h3>

  <p>Slice4 extension for the Swiss Skull Stripper. Contribute to lassoan/SlicerSwissSkullStripper development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Arpan_Gyawali (2023-07-06 10:00 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a><br>
Does this work on CTA.<br>
There are plenty of Skull Stripper for MRI images. The main problem is the contrast.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68c3994c96e3ea2a1836f59162d7cccbf825e18a.jpeg" data-download-href="/uploads/short-url/eWMIYJkkqd790GOCNwZDgG6Splw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68c3994c96e3ea2a1836f59162d7cccbf825e18a_2_680x500.jpeg" alt="image" data-base62-sha1="eWMIYJkkqd790GOCNwZDgG6Splw" width="680" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68c3994c96e3ea2a1836f59162d7cccbf825e18a_2_680x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68c3994c96e3ea2a1836f59162d7cccbf825e18a_2_1020x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68c3994c96e3ea2a1836f59162d7cccbf825e18a.jpeg 2x" data-dominant-color="4D5669"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1111×816 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
These are the result</p>

---

## Post #4 by @rbumm (2023-07-06 10:18 UTC)

<p>results of their strippers? Yes, on the SwissStripper <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> extension homepage, it is said CT and MR.</p>

---

## Post #5 by @Arpan_Gyawali (2023-07-06 10:39 UTC)

<p>Ahhh yess,<br>
Maybe for CT it could work. I am finding a very hard time segmenting brain for CTA.<br>
Have any other idea?</p>

---

## Post #6 by @rbumm (2023-07-06 10:54 UTC)

<p>If it works well please acknowledge the authors.</p>

---

## Post #7 by @Mykola_Sharhan (2023-12-29 00:44 UTC)

<p>I’ve got the best results with TotalSegmentator. Although, it takes 40 seconds with GPU. SwissStripper, unfortunately, captured additional areas on CTA.</p>

---
