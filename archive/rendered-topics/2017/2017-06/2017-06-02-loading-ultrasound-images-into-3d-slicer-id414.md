# Loading ultrasound images into 3d slicer

**Topic ID**: 414
**Date**: 2017-06-02
**URL**: https://discourse.slicer.org/t/loading-ultrasound-images-into-3d-slicer/414

---

## Post #1 by @pcodrington (2017-06-02 00:18 UTC)

<p>I tried loading ultrasound images of a cervix onto 3d Slicer and this error message popped up: Could not load: Unknown - as DWI Volume as a Diffusion Volume.</p>
<p>Attached is a folder I tried to load.</p>
<p>Thank you in advance for your help.</p>

---

## Post #2 by @ihnorton (2017-06-02 13:39 UTC)

<p>I don’t see any attached folder, but if you do share something, please make sure the files are anonymized (no patient information at all). It would also be better to share through Dropbox or Google Drive, so it doesn’t take up too much space on this server and so you can control the expiration of the link.</p>
<p>The “DWI Volume…” message is probably unrelated, most likely none of the other plugins return “yes”, but the DWI one returns “yes with low confidence” so Slicer tries it. I will make some changes to reduce that (then you should just get an error, until some other compatible plugin is available/identified).</p>

---
