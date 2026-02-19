---
topic_id: 18816
title: "Export 3D Image Partial Opacity"
date: 2021-07-20
url: https://discourse.slicer.org/t/18816
---

# Export 3D image partial opacity

**Topic ID**: 18816
**Date**: 2021-07-20
**URL**: https://discourse.slicer.org/t/export-3d-image-partial-opacity/18816

---

## Post #1 by @Chuns_SS (2021-07-20 11:41 UTC)

<p>Hi is there a way to export a 3D image with reduced opacity?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0f237eb394e90a6f112d76182605d67672256b1.jpeg" data-download-href="/uploads/short-url/rwSCKdffttjQ47GFvqiTpmkroJ3.jpeg?dl=1" title="Screenshot from 2021-07-19 21-35-14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0f237eb394e90a6f112d76182605d67672256b1_2_690x265.jpeg" alt="Screenshot from 2021-07-19 21-35-14" data-base62-sha1="rwSCKdffttjQ47GFvqiTpmkroJ3" width="690" height="265" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0f237eb394e90a6f112d76182605d67672256b1_2_690x265.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0f237eb394e90a6f112d76182605d67672256b1_2_1035x397.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0f237eb394e90a6f112d76182605d67672256b1_2_1380x530.jpeg 2x" data-dominant-color="8C90B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-07-19 21-35-14</span><span class="informations">2711×1042 306 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-07-20 13:58 UTC)

<p>What kind of export do you need?</p>

---

## Post #3 by @Chuns_SS (2021-07-20 16:29 UTC)

<p>Currently I’m working with obj format.</p>

---

## Post #4 by @pieper (2021-07-20 17:57 UTC)

<p><a href="https://github.com/Slicer/Slicer/blob/edc1d6e34dc3a4833212b25e92d367a9f244ff2c/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx#L668-L713">Slicer uses</a> the <code>vtkOBJExporter</code> class to capture the data, so you <a href="https://vtk.org/doc/nightly/html/classvtkOBJExporter.html">check the docs on that</a>.  OBJ may not directly support all the styling that Slicer provides.</p>

---

## Post #5 by @lassoan (2021-07-20 19:31 UTC)

<p>You can use <a href="https://github.com/PerkLab/SlicerOpenAnatomy">Slicer’s OpenAnatomy exporter</a> to export to glTF and OBJ format, using colors, and as far as I remember, also opacities. It is just a short Python script, so you can easily adjust it so that it outputs exactly what you need.</p>
<p>Would you like to export for AR/VR viewing?</p>

---

## Post #6 by @Chuns_SS (2021-07-20 20:23 UTC)

<p>Thank-you Steve and Andras for your guidance. I will check the documentation on VTK and try the exporter from perkLabs.<br>
So far I do not need AR/VR viewing.</p>

---

## Post #7 by @lassoan (2021-07-20 21:46 UTC)

<aside class="quote no-group" data-username="Chuns_SS" data-post="6" data-topic="18816">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chuns_ss/48/10007_2.png" class="avatar"> Chuns_SS:</div>
<blockquote>
<p>So far I do not need AR/VR viewing.</p>
</blockquote>
</aside>
<p>I was just wondering how you were going to use the exported models and export to Unity for AR/VR viewing is a common use case. What is the goal of the export? If you can tell more about your application then we could direct you to prior work that you can build on or to other groups that you could collaborate with.</p>

---

## Post #8 by @Chuns_SS (2021-07-21 00:50 UTC)

<p>Andras, I am a surgeon and am interested in the clincal application of the semgented images. I was fascinated by all the work that is being done on autosegmentation but I think the real usefulness lies elsewhere. Obviously my background is not coding or computer science so I’m just working on a few ideas on my own, albeit very slowly!</p>

---

## Post #9 by @lassoan (2021-07-21 01:13 UTC)

<p>OK. Let us know if we can help with anything. There are many surgeons among Slicer users, planning, guiding, and evaluating a wide range of procedures (neuro, cardiac, musculoskeletal, prostate, breast, liver, lung,…) for over 20 years, so there is a lot you can build on.</p>

---
