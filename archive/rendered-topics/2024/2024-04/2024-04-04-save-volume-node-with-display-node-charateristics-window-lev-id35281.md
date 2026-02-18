# Save volume node with display node charateristics (window/level)

**Topic ID**: 35281
**Date**: 2024-04-04
**URL**: https://discourse.slicer.org/t/save-volume-node-with-display-node-charateristics-window-level/35281

---

## Post #1 by @CharNamIII (2024-04-04 11:31 UTC)

<p>Hi,</p>
<p>Is there a way to export the volume with the new window/level set?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b554608c5a9f62f4fba78bc4c65a834a1986413e.png" data-download-href="/uploads/short-url/pS7cmh8nIHMzsBPJ9Nw4M5bHcT4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b554608c5a9f62f4fba78bc4c65a834a1986413e.png" alt="image" data-base62-sha1="pS7cmh8nIHMzsBPJ9Nw4M5bHcT4" width="690" height="75" data-dominant-color="EFF2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">704×77 2.33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Everytime I export the volume, this resets. I don’t want to apply any filter to change the pixel values, just the way it looks (and that it can be saved so that when you load it it appears the way it is)</p>

---

## Post #2 by @cpinter (2024-04-04 11:35 UTC)

<p>You can save the scene and load it instead of only the volume.</p>

---

## Post #3 by @CharNamIII (2024-04-04 11:37 UTC)

<p>Is it possible to just have the volume?</p>

---

## Post #4 by @cpinter (2024-04-04 12:40 UTC)

<p>As you also noticed, the saved image file only contains the volume itself (with some geometry information). This is why there are separate display nodes in Slicer, to encapsulate the data and the display properties appropriately.</p>
<p>The DICOM standard allows saving window/level into DICOM, but I don’t think Slicer supports this on export.</p>

---

## Post #5 by @CharNamIII (2024-04-04 12:54 UTC)

<p>Thanks Cpinter,</p>
<p>You’re right, converting to DICOM does save the information but exporting it out after does not carry the window/level info.</p>

---

## Post #6 by @cpinter (2024-04-04 12:59 UTC)

<p>This is why I suggest saving the volume as a scene if this is important. You can start from an empty scene, load the volume, set the display properties, save it as an MRB, and instead of loading the volume, just load the scene on top of your current scene, whatever it may be. This should work.</p>

---
