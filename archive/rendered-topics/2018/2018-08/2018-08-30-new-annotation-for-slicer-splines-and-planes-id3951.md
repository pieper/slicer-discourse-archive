---
topic_id: 3951
title: "New Annotation For Slicer Splines And Planes"
date: 2018-08-30
url: https://discourse.slicer.org/t/3951
---

# New Annotation for Slicer - Splines and Planes

**Topic ID**: 3951
**Date**: 2018-08-30
**URL**: https://discourse.slicer.org/t/new-annotation-for-slicer-splines-and-planes/3951

---

## Post #1 by @Johan_Andruejol (2018-08-30 15:12 UTC)

<p>Hi everyone,</p>
<p>We have developed new annotation support for Slicer in the form of Splines and Planes. Here is a preview:</p>
<p>Planes:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb2e3c2dcf929723d021bb7f003afd46b0250453.png" data-download-href="/uploads/short-url/sZpZ39i35hYxnY6eXqMFMD34hGP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cb2e3c2dcf929723d021bb7f003afd46b0250453_2_690x413.png" alt="image" data-base62-sha1="sZpZ39i35hYxnY6eXqMFMD34hGP" width="690" height="413" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cb2e3c2dcf929723d021bb7f003afd46b0250453_2_690x413.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cb2e3c2dcf929723d021bb7f003afd46b0250453_2_1035x619.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cb2e3c2dcf929723d021bb7f003afd46b0250453_2_1380x826.png 2x" data-dominant-color="9BA3CF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2269×1359 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Note: Planes annotation are only available in the 3D view</p>
<p>Splines:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be66bd06ebf017f0ac49c1a03abe7a22f081eaeb.jpeg" data-download-href="/uploads/short-url/ramPN8DnBuoNaUWSHc63qh8Oyr9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be66bd06ebf017f0ac49c1a03abe7a22f081eaeb_2_690x439.jpeg" alt="image" data-base62-sha1="ramPN8DnBuoNaUWSHc63qh8Oyr9" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be66bd06ebf017f0ac49c1a03abe7a22f081eaeb_2_690x439.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be66bd06ebf017f0ac49c1a03abe7a22f081eaeb_2_1035x658.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be66bd06ebf017f0ac49c1a03abe7a22f081eaeb_2_1380x878.jpeg 2x" data-dominant-color="595A6F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3090×1966 655 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>These fulfill the needs we have for them, but I don’t think they could be considered “feature complete”. They don’t have a GUI to interact with them for example. Where do you think would be a good idea to share these so the community can have access to it ? As an extension ?</p>
<p>Each of these new annotation uses the Markups nodes as a base. Unfortunately, they don’t have a generic storage node for them yet. We were thinking we should add a one. The plan would be:</p>
<ul>
<li>Add a generic markup storage node to save to JSon</li>
<li>Allow subclasses to easily add attributes to store in the JSon for:
<ul>
<li>The whole markup node</li>
<li>Each individual markup<br>
The current vtkMRMLMarkupsFiducialStorageNode would stay as-is, leaving the user the option to save to (*.fcsv, *.acsv) with it or to JSON with the new generic storage node.</li>
</ul>
</li>
</ul>
<p>What do you think ?</p>
<p>Thanks !<br>
Johan</p>

---

## Post #2 by @cpinter (2018-08-30 15:29 UTC)

<p>This looks great, thank you!</p>
<p>I think we can comment more on what’s needed if we see the code. Could you issue a PR?</p>
<p>Without seeing it I think that</p>
<ul>
<li>this should go into the core</li>
<li>even if it uses markups nodes it should have its own node with storage and display nodes</li>
<li>even if there is no module GUI for this yet, it would be very important to have VTK widgets to interact with the splines in the slice views</li>
</ul>

---

## Post #3 by @lassoan (2018-08-30 15:48 UTC)

<p>Just share the code as is. If it is implemented as a modification in Slicer core, just push it to your own fork. I’ve been working on very similar features, so I have a good idea of how to proceed, but I would need to see what you have already.</p>

---

## Post #4 by @jamesobutler (2018-08-30 19:41 UTC)

<p>Very cool. I’m guessing the code is what’s found in <a href="https://github.com/BICCN/cell-locator/pull/15" rel="nofollow noopener">BICCN/cell-location PR #15</a></p>

---

## Post #5 by @Johan_Andruejol (2018-08-31 15:29 UTC)

<p>I have pushed a PR <a href="https://github.com/Slicer/Slicer/pull/1010" rel="nofollow noopener">here (1)</a> for preview. It’s easier to comment on these than on a branch.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a>: I am working on a storage node (see the plan for the JSON generic markup storage node). In our applications we have not needed any specialized behavior for the display so I have not implement any yet.<br>
The planes are not available in the 2D view, but the splines are. You can interact with them too.</p>
<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a>: Yes indeed.</p>
<p>(1): <a href="https://github.com/Slicer/Slicer/pull/1010" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1010</a></p>

---

## Post #6 by @timeanddoctor (2018-09-08 01:20 UTC)

<p>Cool. Did the fuction avaliable now? How to use it now?</p>

---

## Post #7 by @lassoan (2018-09-09 12:11 UTC)

<p>The feature is not available in the nightly release yet. You need to build Slicer using the branch referenced in the pull request above if you want to try it now.</p>

---
