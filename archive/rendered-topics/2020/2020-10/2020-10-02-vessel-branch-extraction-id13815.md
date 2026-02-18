# Vessel branch extraction

**Topic ID**: 13815
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/vessel-branch-extraction/13815

---

## Post #1 by @Andreas (2020-10-02 11:08 UTC)

<p>Hi all,</p>
<p>is it possible with the stable release version (4.10.2) to segment individual vascular branches of a vascular tree using Centerline Computation?</p>
<p>I have already tried the AddOn “SlicerExtension-VMTK” and the Youtube video “New vessel branch module extraction for 3D Slicer” but unfortunately without success.<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/vmtk/SlicerExtension-VMTK" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars3.githubusercontent.com/u/1390750?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/vmtk/SlicerExtension-VMTK" target="_blank" rel="noopener nofollow ugc">vmtk/SlicerExtension-VMTK</a></h3>

<p>Contribute to vmtk/SlicerExtension-VMTK development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Can you please give me instructions on how to proceed step by step?</p>
<p>Best regards</p>

---

## Post #2 by @lassoan (2020-10-02 23:54 UTC)

<p>Please use the new stable release (version 4.11.20200930) and let us know if it works as you expect.</p>

---

## Post #3 by @Andreas (2020-10-03 21:16 UTC)

<p>Many thanks for your help. With the latest version it worked now. However, I don’t know how to remove the individual branches from the trunk. Maybe it is only possible to hide individual branches.<br>
I would also like to know whether the geometry of the vessels can be changed in terms of length or diameter.<br>
I would be very grateful for your help.</p>

---

## Post #4 by @lassoan (2020-10-04 01:04 UTC)

<p>If you want to delete branches from centerline/network then just remove the vessel endpoints that you don’t need (before you start centerline/network extraction).</p>
<p>If you get the result as curves then you can show/hide/remove/edit each branch using GUI provided by Markups module. If you are comfortable processing the network/centerline tree in Python then you can use either the markups curve or model (vtkPolyData) representation. The best choice also depends on the next processing/analysis step. What is your end goal?</p>

---

## Post #5 by @Andreas (2020-10-04 20:16 UTC)

<p>Thank you for your quick reply.</p>
<p>In the attachment you can see how I try to delete vessel branches using the markups module. Unfortunately, nothing is removed from my vessel model<br>
Unfortunately I am not familiar with Python.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/551df88fb3f2bb88f97a55ebb925e15aa6c1f0ff.jpeg" data-download-href="/uploads/short-url/c8YNrlwwSf0mdAS9Y12GJfs8ZK7.jpeg?dl=1" title="Vessel branch extraction" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/551df88fb3f2bb88f97a55ebb925e15aa6c1f0ff_2_690x401.jpeg" alt="Vessel branch extraction" data-base62-sha1="c8YNrlwwSf0mdAS9Y12GJfs8ZK7" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/551df88fb3f2bb88f97a55ebb925e15aa6c1f0ff_2_690x401.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/551df88fb3f2bb88f97a55ebb925e15aa6c1f0ff_2_1035x601.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/551df88fb3f2bb88f97a55ebb925e15aa6c1f0ff_2_1380x802.jpeg 2x" data-dominant-color="7C7C83"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Vessel branch extraction</span><span class="informations">1680×978 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In the end, I am trying to create reproducibility for the removal of vascular branches. I don’t want to do this with scissors as this result is not reproducible.</p>

---

## Post #6 by @lassoan (2020-10-04 23:33 UTC)

<p>Removing endpoints only removes branches from the centerline tree. The input model is not modified.</p>
<p>There are many options for removing branches. The best choice depends on why you need to remove branches. What is your end goal? CFD analysis?</p>

---

## Post #7 by @Andreas (2020-10-05 22:18 UTC)

<p>Thank you for your help.</p>
<p>Isn’t it possible to remove the branches at the endpoints of the actual input model?</p>
<p>Can you please tell me which processing tools are recommended in addition to scissors?</p>

---

## Post #8 by @lassoan (2020-10-05 23:07 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="7" data-topic="13815">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Can you please tell me which processing tools are recommended in addition to scissors?</p>
</blockquote>
</aside>
<p>There are many options for removing branches. The best choice depends on why you need to remove branches. What is your end goal? 3D printing, CFD analysis, simulation, visualization, …?</p>

---

## Post #9 by @Andreas (2020-10-07 10:50 UTC)

<p>I want to 3D print vessel models and remove small diameter branches.</p>

---
