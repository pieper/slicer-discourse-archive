# Rendering side by side

**Topic ID**: 34268
**Date**: 2024-02-12
**URL**: https://discourse.slicer.org/t/rendering-side-by-side/34268

---

## Post #1 by @imruljubair (2024-02-12 21:17 UTC)

<p>Hello,</p>
<p>Is there any way to render 3D segmentation on multiple screen? For example, visualizing <strong>pat00-seg.nii.gz</strong> and <strong>pat00-seg-ground-truth.nii.gz</strong> side by side?</p>
<p>Thanks,<br>
Jubair</p>

---

## Post #2 by @lassoan (2024-02-12 21:20 UTC)

<p>Yes, any number of viewers can be laid out on any number of monitors.</p>
<aside class="quote quote-modified" data-post="1" data-topic="27218">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-feature-dual-monitor-and-picture-in-picture-view-layout/27218">New feature: Dual monitor and picture-in-picture view layout</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Slicer can now display 3D, slice, plot, etc. views in multiple windows and not just in the main application window - see <a href="https://youtu.be/PJuXSXkPvHs">1-minute demo video</a>. 
Display views in separate windows - can be dragged to a second screen or additional touchscreen or drawing tablet: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a351e604051ca1b0e319eb20c4b4dd2f1c024610.jpeg" data-download-href="/uploads/short-url/niNifHBkKk94D7SWYp27YY6S2dO.jpeg?dl=1" title="image">[image]</a> 
The extra window can be displayed floating over the application window as “picture-in-picture”: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f8580f53dd5d589e66bb297967b28535b19d659.jpeg" data-download-href="/uploads/short-url/6MoteFNJJeMUpKCVcplWmAXIur7.jpeg?dl=1" title="image">[image]</a> 
The additional window can be also docked into application window (any corners or sides): 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa9760a69191c1caf71940284979eb8112f217a0.jpeg" data-download-href="/uploads/short-url/ol7uGfPGHN7S6KYrpeIZXRK5yUM.jpeg?dl=1" title="image">[image]</a> 
Views can be maximized/r…
  </blockquote>
</aside>

<p>You can specify your layout in an xml string and you can automate what content you want to display where using a little Python scripting.</p>

---

## Post #3 by @imruljubair (2024-02-12 21:45 UTC)

<p>Thank you so much!! I will try that.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="34268">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can specify your layout in an xml string and you can automate what content you want to display where using a little Python scripting.</p>
</blockquote>
</aside>
<p>Could give an example? Or any link?</p>
<p>Also, just being curious: can I program to rotate all the 3D segmentation in different screen at the same time? Like, the 3D segmentation will start rotating at the same time. So that I can visually compare from all direction.</p>
<p>I appreciate your help.</p>
<p>Thanks</p>
<p>Jubair</p>

---
