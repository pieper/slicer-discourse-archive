---
topic_id: 2369
title: "Rendering Two Nrdd Files Side To Side With Different Origin"
date: 2018-03-20
url: https://discourse.slicer.org/t/2369
---

# Rendering two NRDD files side to side with different origin, space coordinates and spacing

**Topic ID**: 2369
**Date**: 2018-03-20
**URL**: https://discourse.slicer.org/t/rendering-two-nrdd-files-side-to-side-with-different-origin-space-coordinates-and-spacing/2369

---

## Post #1 by @dcantor (2018-03-20 00:38 UTC)

<p>Hello,</p>
<p>I have two NRRD files:</p>
<ul>
<li>T2W (1)</li>
<li>ADC (2)</li>
</ul>
<p>When I load these two files in Slicer I can see that slicer automatically positions them in space according to their metadata and performs interpolation. I can tell that because (2) has a larger spacing than (1) and yet I can visualize slices from (2) as I scroll through (1).</p>
<p>I am writing a python script that take these two files and visualize them side to side. I don’t think I need to run registration since I already know the origin, spacing and orientation of each volume (as per their NRRD headers).</p>
<p>So, how can I do this: For each slice in (1) I want to show what would be the corresponding slice in (2)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f224af8e68b11bdc4e1d2b9805cc656105d20ac.png" data-download-href="/uploads/short-url/29SDjKMM9a3gbHhCXr3kj8d1w6M.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f224af8e68b11bdc4e1d2b9805cc656105d20ac_2_690x344.png" alt="image" data-base62-sha1="29SDjKMM9a3gbHhCXr3kj8d1w6M" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f224af8e68b11bdc4e1d2b9805cc656105d20ac_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f224af8e68b11bdc4e1d2b9805cc656105d20ac.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f224af8e68b11bdc4e1d2b9805cc656105d20ac.png 2x" data-dominant-color="D8E1F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">792×395 22.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I know that somehow I need to apply an affine transform and do some interpolation in (2) to change coordinates but I am a bit lost.</p>
<p>Since my frame of reference is (1), and say that its affine transform is $T_1$, perhaps I can apply $T_1^{-1}$ to (2) to obtain (2) in coordinates with respect to the origin and standard set of basis? But then what? how do I do interpolation? Any help is welcome. Thanks!</p>

---

## Post #2 by @lassoan (2018-03-20 19:06 UTC)

<p>If you do all this in Slicer then you don’t have to worry about any low-level detail. You can set up two slice viewers to show the volumes that you need to see, set the slice plane normals to have the same direction, enable slice link, make it hot-linked (long-click on slice link icon and check the “Hot linked” checkbox).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eec7381aaf5941c0c6672df310f56aeaeab6104.png" alt="image" data-base62-sha1="6H6yAVIJ7R0cPrWQBXJzkUycpP6" width="459" height="255"></p>

---

## Post #3 by @dcantor (2018-03-21 21:13 UTC)

<p>Thanks for the info Andras.</p>
<p>I found a solution using SimpleITK. For those who might run into the same problem, here it is the solution:</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.itk.org/t/resampling-with-simpleitk/790">
  <header class="source">
      <img src="https://discourse.itk.org/uploads/default/optimized/1X/71db04d41479c229accbe8bf0b99195f75f46770_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.itk.org/t/resampling-with-simpleitk/790" target="_blank" rel="noopener nofollow ugc" title="08:43PM - 21 March 2018">ITK – 21 Mar 18</a>
  </header>

  <article class="onebox-body">
    <img src="https://discourse.itk.org/uploads/default/original/1X/8a8379ed42cbc60fb262a064faca192c7d7111e7.png" class="thumbnail onebox-avatar" width="500" height="500">

<div class="title-wrapper">
  <h3><a href="https://discourse.itk.org/t/resampling-with-simpleitk/790" target="_blank" rel="noopener nofollow ugc">resampling with simpleitk</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #12A89D;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Beginner Questions</span>
        </span>
      </span>
    <div class="topic-header-extra">
      <div class="list-tags">
        <div class="discourse-tags">
          <svg class="fa d-icon d-icon-tag svg-icon svg-string"><use href="#tag"></use></svg>
            <span class="discourse-tag simple">python</span>
            <span class="discourse-tag simple">simpleitk</span>
        </div>
      </div>
    </div>
  </div>
</div>

  <p>Hi iTK!  I am new to SimpleITK and I am working in Python. I have a NRRD volume that I want to reslice according to the origin,spacing and dimensions of a second NRRD volume. I am trying to figure this out. Is there a way to do this with SimpleITK...</p>

  <p>
    <span class="label1">Reading time: 1 mins 🕑</span>
      <span class="label2">Likes: 3 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Regards,</p>
<p>Diego</p>

---

## Post #4 by @lassoan (2018-03-21 21:29 UTC)

<p>It was not clear if you need interactive view or resampling. Resampling is available in “Resample scalar/vector/DWI” module in Slicer.</p>

---

## Post #5 by @Fernando (2018-03-21 22:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>make it hot-linked</p>
</blockquote>
</aside>
<p>What does the hot link exactly do?</p>

---

## Post #6 by @lassoan (2018-03-22 00:47 UTC)

<p>Hot-link synchronizes pan&amp;zoom between slice views that has the same orientation. It is useful if you need to review multiple volumes side-by-side.</p>

---

## Post #7 by @pieper (2018-03-22 06:37 UTC)

<p>Also hot-link updates the sync on each pointer move, while regular link only updates when you release the button.</p>

---

## Post #8 by @Fernando (2018-03-22 08:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="2369" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Hot-link synchronizes pan&amp;zoom between slice views that has the same orientation. It is useful if you need to review multiple volumes side-by-side.</p>
</blockquote>
</aside>
<p>Ok, thanks.</p>
<aside class="quote no-group" data-username="pieper" data-post="7" data-topic="2369" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Also hot-link updates the sync on each pointer move, while regular link only updates when you release the button.</p>
</blockquote>
</aside>
<p>When would one prefer regular link over hot link? If the views are going to be updated anyway, why not update them immediately instead of waiting to release the mouse?</p>

---

## Post #9 by @pieper (2018-03-22 14:36 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="8" data-topic="2369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>When would one prefer regular link over hot link? If the views are going to be updated anyway, why not update them immediately instead of waiting to release the mouse?</p>
</blockquote>
</aside>
<p>It’s usually faster to only redraw the window where the mouse is moving and you are usually looking at the window where the mouse is, that’s why hot-link is just an option.</p>

---
