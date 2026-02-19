---
topic_id: 44254
title: "How To Create Dynamic Stylustoreference Transform From Ndi T"
date: 2025-08-29
url: https://discourse.slicer.org/t/44254
---

# How to create dynamic StylusToReference transform from NDI tracker data?

**Topic ID**: 44254
**Date**: 2025-08-29
**URL**: https://discourse.slicer.org/t/how-to-create-dynamic-stylustoreference-transform-from-ndi-tracker-data/44254

---

## Post #1 by @jonh_wick (2025-08-29 14:37 UTC)

<p>Hi all,大家好</p>
<p>I am working with an NDI tracker in 3D Slicer and I have two transforms provided dynamically by the tracker:</p>
<ul>
<li>
<p><strong>StylusToTracker</strong></p>
</li>
<li>
<p><strong>ReferenceToTracker</strong></p>
</li>
</ul>
<p>What I would like to obtain in real time is the transform:</p>
<ul>
<li><strong>StylusToReference</strong></li>
</ul>
<p>I have read through the <em>SlicerIGT Tutorial U04</em> materials, and I understand the general idea of transform concatenation. However, I am still not clear how to properly set this up in Slicer so that StylusToReference is updated dynamically during tracking.</p>
<p>Questions:</p>
<ol>
<li>
<p>Should I use the “Add derived transform” function in PLUS or set up a Transform node hierarchy directly in Slicer?</p>
</li>
<li>
<p>If using Slicer, should I simply parent Stylus under Reference and then harden transforms, or is there a way to keep StylusToReference continuously updated without hardening?</p>
</li>
<li>
<p>Is there an example in the SlicerIGT extension that specifically shows how to compute a live StylusToReference from tracker transforms?</p>
</li>
</ol>
<p>Any clarification or example pipeline would be greatly appreciated!</p>
<p>Thanks a lot!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/0111f4ef292c00dd31e1b9bde44ca911ef664892.png" data-download-href="/uploads/short-url/9sWSzNNSMDUgoyC75WjmdGgcwy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/0111f4ef292c00dd31e1b9bde44ca911ef664892.png" alt="image" data-base62-sha1="9sWSzNNSMDUgoyC75WjmdGgcwy" width="690" height="128" data-dominant-color="E5ECF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1030×192 9.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d35ed8d173eae5efa5e8c3b55375ce07dd7693fb.png" data-download-href="/uploads/short-url/u9RXcFDx3Ute9OX00zW5egdNzBN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d35ed8d173eae5efa5e8c3b55375ce07dd7693fb.png" alt="image" data-base62-sha1="u9RXcFDx3Ute9OX00zW5egdNzBN" width="690" height="149" data-dominant-color="D4E5CF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1097×237 13.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2025-08-29 18:28 UTC)

<p>I have had to set up something very similar to this.  The way I solved it was to change the PlusServerLauncher xml configuration file so that it was transmitting TrackerToReference rather than ReferenceToTracker.  Then, I set up a transform hierarchy with TrackerToReference as the parent of StylusToTracker.  These two transforms are updated continuously from the tracker-streamed data, and combined, they provide the StylusToReference transformation. Any object (e.g. a stylus surface model) with is then placed under StylusToTracker transform will move correctly relative to the reference.</p>

---
