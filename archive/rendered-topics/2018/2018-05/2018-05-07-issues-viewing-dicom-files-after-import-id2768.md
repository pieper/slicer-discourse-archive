---
topic_id: 2768
title: "Issues Viewing Dicom Files After Import"
date: 2018-05-07
url: https://discourse.slicer.org/t/2768
---

# issues viewing DICOM files after import

**Topic ID**: 2768
**Date**: 2018-05-07
**URL**: https://discourse.slicer.org/t/issues-viewing-dicom-files-after-import/2768

---

## Post #1 by @goetzf (2018-05-07 15:57 UTC)

<p>I have been following tutorials on how to load DICOM data and I can’t figure out why my data look weird. The scans were done with a GE vtome (not sure of all the specifics) and a nano-scale tube. The .dcm files were output from VG-Studio. When I load the .dcm files, the viewers look terrible. I know I’m doing something wrong but I’m very new to this process and I don’t know where to start. All of the tutorials I looked at so far involve loading perfect datasets of humans and I’m looking at a leech.</p>
<p>Any help would be greatly appreciated!</p>
<p>Attached should be a screen shot of the viewer.</p>
<p>Freya</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/856842385b4c9e618a2097c1955f3e58e7388988.jpeg" data-download-href="/uploads/short-url/j2aSmcW4CMTjOf0WsjtWW95N6Gs.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/856842385b4c9e618a2097c1955f3e58e7388988_2_561x500.jpg" alt="image" data-base62-sha1="j2aSmcW4CMTjOf0WsjtWW95N6Gs" width="561" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/856842385b4c9e618a2097c1955f3e58e7388988_2_561x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/856842385b4c9e618a2097c1955f3e58e7388988_2_841x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/856842385b4c9e618a2097c1955f3e58e7388988_2_1122x1000.jpg 2x" data-dominant-color="555562"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1210×1077 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @gcsharp (2018-05-07 16:32 UTC)

<p>Hi Freya,</p>
<p>Based on the image in the lower right, it looks like you have projection data (aka sinogram data).  When you scroll through the upper left, does it look like a sequence of images taken at different angles?  If so, you need to ask the scanner technician for “reconstructed” data.</p>
<p>Greg</p>

---

## Post #3 by @goetzf (2018-05-07 16:56 UTC)

<p>Hi Greg,<br>
That is exactly what I loaded, projections. So, “reconstructed data” can also be exported as .dcm files? Thank you for your patience while I wrap my brain around this. In the past I have serially sectioned animals, photographed each section, registered those photographs and plan on segmenting those stacks. This is similar but obviously much more high tech.</p>
<p>Freya</p>

---

## Post #4 by @gcsharp (2018-05-07 17:30 UTC)

<p>Hi Freya,</p>
<p>I consider it very likely that a reconstruction can be exported.  If you go to the operator computer console and look through the menus, you can probably figure it out.</p>
<p>Greg</p>

---

## Post #5 by @goetzf (2018-05-07 20:36 UTC)

<p>Hi Greg,<br>
You are correct. Seems like in VG Studio it might be called “slices” or something like that.<br>
Thanks for your prompt response today. Now I’m on to searching for how to perform reconstructions on a leech.</p>
<p>Have a great day!</p>
<p>Freya</p>

---
