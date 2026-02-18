# Multiple overlapping centerlines created by vmtkcenterlinesnetwork

**Topic ID**: 23180
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/multiple-overlapping-centerlines-created-by-vmtkcenterlinesnetwork/23180

---

## Post #1 by @Doodads (2022-04-28 16:47 UTC)

<p>Operating system: Ubuntu 20.04.2 LTS<br>
Slicer version: N.A. (using vmtk development version)<br>
Expected behavior: Centerlines split into two at each bifurcation. A single centerline running through each branch.<br>
Actual behavior: Three splits close to each other at two of the bifurcations. More than one centerline going through some branches</p>
<p>Dear vmtk support team,</p>
<p>I ran the vmtkcenterlinesnetwork on a circle of willis surface. For the most part the script was able to generate the centerlines well, except at some bifurcations and branches where multiple overlapping centerlines were observed - please refer to the attached images for a visual representation of the problem.</p>
<p>I suspect that the centerlines were not properly merged after they were generated. May I know how to resolve this issue? Are there some parameters I can tune or changes I can implement directly on the vmtkcenterlinesnetwork script? Thank you very much!</p>
<p>FYI, I am not using Slicer but the vmtkcenterlinesnetwork and I need an automated solution (i.e. without much manual input like running a script).</p>
<p>Regards,</p>
<p>Doodads<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3677ab23d94cb038d5323fce82568a427c378f6.jpeg" data-download-href="/uploads/short-url/njxwVfCMwPLLJmMGu4qAjUeATUa.jpeg?dl=1" title="Screenshot 2022-04-28 at 10.32.59 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3677ab23d94cb038d5323fce82568a427c378f6_2_666x500.jpeg" alt="Screenshot 2022-04-28 at 10.32.59 AM" data-base62-sha1="njxwVfCMwPLLJmMGu4qAjUeATUa" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3677ab23d94cb038d5323fce82568a427c378f6_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3677ab23d94cb038d5323fce82568a427c378f6_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3677ab23d94cb038d5323fce82568a427c378f6.jpeg 2x" data-dominant-color="434453"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-04-28 at 10.32.59 AM</span><span class="informations">1187×890 45.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c95e7458f93581babe32c39f22774ad119c660c4.jpeg" data-download-href="/uploads/short-url/sJol2u1XO2xrBdSBOI2KY4zXX00.jpeg?dl=1" title="Screenshot 2022-04-28 at 10.28.08 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c95e7458f93581babe32c39f22774ad119c660c4_2_664x499.jpeg" alt="Screenshot 2022-04-28 at 10.28.08 AM" data-base62-sha1="sJol2u1XO2xrBdSBOI2KY4zXX00" width="664" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c95e7458f93581babe32c39f22774ad119c660c4_2_664x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c95e7458f93581babe32c39f22774ad119c660c4_2_996x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c95e7458f93581babe32c39f22774ad119c660c4.jpeg 2x" data-dominant-color="38394A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-04-28 at 10.28.08 AM</span><span class="informations">1197×901 56.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-04-30 04:26 UTC)

<p>VMTK has two centerline extraction algorithms.</p>
<p>A simple one that determines centerline based only on the surface geometry. This works on arbitrary topology, such as the Circle of Willis.</p>
<p>And there is a more sophisticated method that computes a Voronoi diagram and searches for shortest path in between inlet and outlet points. This method provides more realistic centerline geometry, but it only works if the topology is a tree (or multiple trees). It does not work on the Circle of Willis, because the topology is not a tree. If you want to use this method on the Circle of Willis then you can extract one tree at a time (e.g., left side then the right side) and then manually merge the trees.</p>

---

## Post #3 by @Doodads (2022-05-06 03:35 UTC)

<p>Hi Andras, thanks for your response. May I know how to extract the trees and merge them after using vmtk? It would be great if you could share some example vmtk pypes or python code that could do this so I could go through and understand. Thanks again for your assistance!</p>

---
