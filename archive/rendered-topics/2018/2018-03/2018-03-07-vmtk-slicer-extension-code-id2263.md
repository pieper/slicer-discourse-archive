---
topic_id: 2263
title: "Vmtk Slicer Extension Code"
date: 2018-03-07
url: https://discourse.slicer.org/t/2263
---

# VMTK Slicer extension code

**Topic ID**: 2263
**Date**: 2018-03-07
**URL**: https://discourse.slicer.org/t/vmtk-slicer-extension-code/2263

---

## Post #1 by @mschumaker (2018-03-07 16:42 UTC)

<p>This is primarily addressed to Andras <a class="mention" href="/u/lassoan">@lassoan</a>, since it appears you’re the author of the SlicerExtension-VMTK code:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/821dd372a7bf85d249325c1dbe24202f34c48d80b7a3699aaddd313d6ef4df21/vmtk/SlicerExtension-VMTK" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/vmtk/SlicerExtension-VMTK" target="_blank" rel="noopener nofollow ugc">GitHub - vmtk/SlicerExtension-VMTK</a></h3>

  <p>Contribute to vmtk/SlicerExtension-VMTK development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’ve been trying to use some parts of the CenterlineComputation.py code, and there are some things that confuse me. What I’d like to do is create a manual vessel segmentation for a single non-branching artery, create a surface model for it, and calculate a centreline for the full length of the model. Below is an image of the artery surface model.<br>
So, I know where I would like to start and end the centreline, and it’s in the middle of the vessel at the Superior and Inferior ends. I’m confused by how CenterlineComputation.py is set up though. At least for extractNetwork, it appears that the source point is one from the wall of the vessel model, and openSurfaceAtPoint is used to isolate the source point from any cells. Am I understanding this correctly?<br>
Could you explain how the source and target points for computeCenterlines are chosen?<br>
If I know where I want the source and target to be, but there aren’t points already there, can I add points to the model and set those as the source and target?<br>
Thanks in advance for your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5401e95001da44addb67e507fb59572a7ce16276.png" data-download-href="/uploads/short-url/bZacyT19srKu0SRJo4XbMOnjhWe.png?dl=1" title="artery-model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/5401e95001da44addb67e507fb59572a7ce16276_2_594x500.png" alt="artery-model" data-base62-sha1="bZacyT19srKu0SRJo4XbMOnjhWe" width="594" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/5401e95001da44addb67e507fb59572a7ce16276_2_594x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/5401e95001da44addb67e507fb59572a7ce16276_2_891x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5401e95001da44addb67e507fb59572a7ce16276.png 2x" data-dominant-color="0B0707"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">artery-model</span><span class="informations">1026×863 41.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-03-14 16:23 UTC)

<p>Unfortunately VMTK does not have any API documentation. So, the only ways to find out how things work is to read VMTK code or ask on <a href="https://groups.google.com/forum/#!forum/vmtk-users">VMTK mailing list</a>.</p>
<p>For simple centerline extraction, you can use <code>Extract skeleton</code> module in recent nightly builds, choose to save centerline points as <code>Output markup fiducials</code>. You may need to enable “Do not prune branches”. Input image is a labelmap. If you have your vessel as a segment then you have to export it to a labelmap node using Segmentations module.</p>

---

## Post #3 by @mschumaker (2018-03-14 20:15 UTC)

<p>Thanks for your reply. I’ll have a look at these, and see what I can figure out. Thanks also for the link to the VMTK mailing list.</p>

---
