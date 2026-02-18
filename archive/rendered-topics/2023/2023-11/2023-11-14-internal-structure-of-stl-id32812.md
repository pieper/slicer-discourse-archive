# Internal Structure of STL

**Topic ID**: 32812
**Date**: 2023-11-14
**URL**: https://discourse.slicer.org/t/internal-structure-of-stl/32812

---

## Post #1 by @WillSteger (2023-11-14 16:06 UTC)

<p>Hi,<br>
I’m a new 3D Slicer user attempting to use it for dental research purposes. Specifically, I have been sent a series of STL models built from microCT scans and have been asked to isolate the enamel-dentine junction (EDJ) of the tooth (an internal tissue layer of the tooth). My understanding of an STL file is that it is a surface mesh only, and I would therefore be unable to view the internal tissue of the tooth. Usually, I would use something like Avizo/Amira that is on my lab desktop and perform the segmentation of the EDJ and assembly of the EDJ myself, but I currently have access to neither the desktop nor the original mCT images. Is there any way to do this task on 3D Slicer with an STL file?</p>

---

## Post #2 by @lassoan (2023-11-14 23:18 UTC)

<p>The EDJ may be recognizable on the surface mesh, but not as reliably as on the CT images. Probably the best is to confirm this with the person who gave you the task.</p>

---

## Post #3 by @manjula (2023-11-15 11:30 UTC)

<p>Hi,</p>
<p>I think it is impossible to define the EDJ from a surface mesh. Why not use the microCT ?</p>

---

## Post #4 by @Ugi_Mikla (2023-11-17 12:00 UTC)

<p>That might not be possible unless 3D models of dentin and enamel we’re done separetly. However that would not give You the entire info neither.</p>

---
