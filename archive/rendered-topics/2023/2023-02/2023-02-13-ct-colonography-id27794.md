---
topic_id: 27794
title: "Ct Colonography"
date: 2023-02-13
url: https://discourse.slicer.org/t/27794
---

# CT Colonography

**Topic ID**: 27794
**Date**: 2023-02-13
**URL**: https://discourse.slicer.org/t/ct-colonography/27794

---

## Post #1 by @TSzabo123 (2023-02-13 14:29 UTC)

<p>I am trying to create a colon fly through using CT images to recreate a CT colonography. Is there a way to do this in Slicer? I have not been able to find an extension, and there is no preset in the volume rendering. I’ve included an example of what I’m trying to recreate (our pacs system does this but doesn’t allow us to export the model)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f66c620b18d7547ae09176ea80fd3b3db65ce392.png" alt="image" data-base62-sha1="z9XFmHZcSOlOJKmYTphn08KX2kG" width="390" height="328"></p>

---

## Post #2 by @lassoan (2023-02-13 14:30 UTC)

<p>You can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/endoscopy.html#endoscopy">Endoscopy</a> module for this. You can either use it without any segmentation (using Volume Rendering) or by segmenting the colon using Segment Editor module.</p>

---

## Post #3 by @mau_igna_06 (2023-02-13 18:31 UTC)

<p><a class="mention" href="/u/tszabo123">@TSzabo123</a> I’m surprissed by the quality of the inside-instestine views (3D renderings from CT) does this picture come from a company’s demo or you made using your own data? What about the similar to x-ray view that even renders intestine creases on the bottom left? Was that centerline autodetected?</p>
<p>Thank you</p>

---

## Post #4 by @lassoan (2023-02-13 21:39 UTC)

<p>This good image quality is quite common for diagnostic virtual endoscopies. The colon is thorougly cleaned out and filled with CO2, so it is just a very simple rendering of the air/tissue boundary.</p>
<p>You can get the entire lumen using simple thresholding in Segment Editor. From that, you can get the centerline using VMTK extension’s Extract Centerline module. Sometimes the centerline can take “shortcuts” between loops that are very close to each other or when the centerline is smoothed, but that is preventable with a  little post-processing of the segment (such as slightly shrinking the segment) and avoiding strong curve smoothing.</p>

---

## Post #5 by @TSzabo123 (2023-02-15 12:37 UTC)

<p>Hi Andras,<br>
Thanks for the quick reply. I kept searching for Ct colonography and virtual colonoscopy. Didn’t even think to search under endoscopy. I haven’t quite figured out how to pipeline segmentation to endoscopy but this definitely looks like the right direction.</p>
<p>And yes this is from our Pacs. We use syngo.via and the segmentation is quite good and the centerline is mostly accurate. The best feature is the stool remover/stool tagging though <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
