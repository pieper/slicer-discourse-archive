---
topic_id: 47709
title: "Asking for more mask save format"
date: 2026-07-22
url: https://discourse.slicer.org/t/47709
last_bumped: 2026-07-23T03:47:09.289Z
---

# Asking for more mask save format

**Topic ID**: 47709
**Date**: 2026-07-22
**URL**: https://discourse.slicer.org/t/asking-for-more-mask-save-format/47709

---

## Post #1 by @zhousy5310 (2026-07-22 07:49 UTC)

<p>Hi all,</p>
<p>May i ask why does 3D slicer only support output the segmentation results as these 4: .seg.nrrd; .seg.nhdr; .nrrd; .nhdr.</p>
<p>Is it possible, without using plugins, to save the segmentation results separately into .nii.gz?</p>
<p>Best,</p>
<p>Harry</p>

---

## Post #2 by @ebrahim (2026-07-22 12:32 UTC)

<p>You could convert the segmentation to a labelmap, which is a type of volume node and so can be exported as nii.gz.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/399178422cd8f4c3d8f44351e0060c90695b04fe.png" data-download-href="/uploads/short-url/8dgSLyi40FKopfGhUurzkpVBYKy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/399178422cd8f4c3d8f44351e0060c90695b04fe.png" alt="image" data-base62-sha1="8dgSLyi40FKopfGhUurzkpVBYKy" width="525" height="376"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">525×376 35.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Deep_Learning (2026-07-22 15:06 UTC)

<p>There are a number of threads on this.   Some written by me…   I would love a .seg.nii.gz. That would be recognized by Slicer as a segmentation similar to .seg.nrrd.  Admin has his rationale.  Best to write a pastabele script that converts to labelmap and then saves as nii.gz.</p>

---

## Post #4 by @zhousy5310 (2026-07-23 02:29 UTC)

<p>I see. Thanks for sharing. It works on my side. Now I can see extra 2 options:“mask” &amp; “colorTable” when i save. <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=15" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @zhousy5310 (2026-07-23 02:36 UTC)

<p>May i ask what’s the reason? Currently it’s a bit tedious, especially for people unfamiliar with 3D slicer.</p>
<p>I need to go into “Segmentation”, select the correct segmentation, right click to “Export visible segments to binary labelmap”, click “save”, pick the <em>right</em> thing to save, and edit the file format to the <em>right</em> one.</p>
<p>While other tools, like ITK-SNAP, allows many direct output options, e.g. NiFTI.</p>
<p>Of course slicer can do more than ITK-SNAP functional-wise, but it’s kinda of confusing for why not implementing more output options.</p>

---

## Post #6 by @muratmaga (2026-07-23 03:47 UTC)

<aside class="quote no-group" data-username="zhousy5310" data-post="5" data-topic="47709">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/8491ac/48.png" class="avatar"> zhousy5310:</div>
<blockquote>
<p>May i ask what’s the reason? Currently it’s a bit tedious, especially for people unfamiliar with 3D slicer.</p>
</blockquote>
</aside>
<p>My understanding NIFTI format has very little header (a few hundred bytes), and cannot accommodate all the metadata about the segments that is necessary to restore the segmentation accurate from the file.</p>
<aside class="quote no-group" data-username="zhousy5310" data-post="5" data-topic="47709">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/8491ac/48.png" class="avatar"> zhousy5310:</div>
<blockquote>
<p>While other tools, like ITK-SNAP, allows many direct output options, e.g. NiFTI.</p>
</blockquote>
</aside>
<p>They output labelmaps, not segmentation. If you are comfortable with labelmaps and do not want all the nice features a segmentation object provides (such as overlap, or restricting your segmentation to a specific segment etc), you are perfectly fine to save them as nii.gz, just right click choose export as labelmap, and then save nii.gz.You might even turn this into single action.</p>
<p>But you may want to read this first: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#representations" class="inline-onebox" rel="noopener nofollow ugc">Image Segmentation — 3D Slicer documentation</a></p>

---
