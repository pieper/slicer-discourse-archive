# Slicer IGT providing Stylus tool-tip as input in Fiducial Registation Wizard under "To fiducials"

**Topic ID**: 8562
**Date**: 2019-09-25
**URL**: https://discourse.slicer.org/t/slicer-igt-providing-stylus-tool-tip-as-input-in-fiducial-registation-wizard-under-to-fiducials/8562

---

## Post #1 by @NormandRbert (2019-09-25 13:23 UTC)

<p>I need to calibrate an O-arm imaging system to obtain an “OArmImageToOArmTransform” with an Optitrack tri-ocular camera. This is something we expect to perform infrequently hence I am trying to do this task using various module UIs instead of coding for now. We built a registration x-ray phantom with 20 divots for this task.<br>
We are creating a fiducial for each divot seen in a 3D image and/or orthogonal 2D image planes of the phantom using the “IGT”-&gt;“Fiducial Registration Wizard” under “From Fiducial”. We wish to create fiducials using an instrumented Stylus (Medtronic) using the “IGT”-&gt;“Fiducial Registration Wizard” under “To Fiducial”.</p>
<p>I am having issues passing the position of the navigated stylus tip when touching the phantom divots in the same order as I did for the 3D image. The Wizard allows fiducials to be populated via the current value of a transform, a feature that seems promising for my use. However, my StylusToReference transform is not the correct transform to populate the “To fiducials” because it is not centered on the tip.  I think I need the transform StylusToReference . StylusToStylusTip. One might think that hardening might provide the desired information but as soon as I do that my resulting transform is a snapshot i.e. is not live anymore.</p>
<p>Looking for advice on how to do this via the UI but if not possible I am not adverse to writing a module and/or running some code in the Python interactor. Regards</p>

---

## Post #2 by @Sunderlandkyl (2019-09-25 14:00 UTC)

<p>If you place StylusTipToStylus under the StylusToReference transform in the transform hierarchy (without hardening), you should then be able to place points at the StylusTip position in the Fiducial Registration Wizard.</p>

---

## Post #3 by @NormandRbert (2019-09-25 14:34 UTC)

<p>Resolved. Indeed you are right. I only realized this after submitting this post and before it was approved by the moderator  <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=9" title=":blush:" class="emoji" alt=":blush:"> Had I paid closer attention to the tutorials (<a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">http://www.slicerigt.org/wp/user-tutorial/</a>),  I might have noticed my erroneous ways.</p>

---
