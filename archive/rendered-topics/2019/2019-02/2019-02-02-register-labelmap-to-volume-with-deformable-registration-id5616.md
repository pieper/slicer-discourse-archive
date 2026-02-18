# Register labelmap to volume with deformable registration

**Topic ID**: 5616
**Date**: 2019-02-02
**URL**: https://discourse.slicer.org/t/register-labelmap-to-volume-with-deformable-registration/5616

---

## Post #1 by @Hamburgerfinger (2019-02-02 05:32 UTC)

<p>Hi!  I’d like to deform an atlas (labelmap) to align with a CT image.  Can someone please share a convenient way of doing this in Slicer?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2019-02-02 10:20 UTC)

<p>If you have a CT with the labelmap, then you can <a href="https://www.slicer.org/wiki/Documentation/Nightly/Registration/RegistrationLibrary" rel="nofollow noopener">register</a> the two CTs and then put the labelmap in the resulting transform.</p>

---

## Post #3 by @Hamburgerfinger (2019-02-02 13:18 UTC)

<p>Thanks! If I don’t have two CTs, in other words I only have the label map defining a reference geometry and a want to deform that that to align with a single CT.</p>

---

## Post #4 by @lassoan (2019-02-02 13:56 UTC)

<p>You can use Fiducial Registration Wizard module (in SlicerIGT extension) to register the atlas labelmap to patient image by specifying matching anatomical landmark points.</p>

---
