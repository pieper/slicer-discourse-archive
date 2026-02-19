---
topic_id: 32083
title: "Registration On Intersecting Volumes"
date: 2023-10-06
url: https://discourse.slicer.org/t/32083
---

# Registration on intersecting volumes

**Topic ID**: 32083
**Date**: 2023-10-06
**URL**: https://discourse.slicer.org/t/registration-on-intersecting-volumes/32083

---

## Post #1 by @wesselk (2023-10-06 21:45 UTC)

<p>Hello, I am trying to concatenate 2 CT volumes into 1 continuous volume.  I realize that registration is generally intended for 2 scans with nearly identical captured anatomy, but I was hoping to essentially stitch together 2 scans which have a region of overlap.</p>
<p>After following <a href="https://www.youtube.com/watch?v=76qlA1INXoI" rel="noopener nofollow ugc">this tutorial</a> and some trial/error I believe it’s possible, but my output volume is noisy and seems to basically just capture the moving image.  I’m currently padding the original scans with empty layers in the direction of the overlap and using a linear transform to eyeball the registration before starting.  Since there are so many advanced features of this tool, I figured I’d ask if this is something that has been done before or if anyone can get me pointed in the right direction.  Thank you in advance for any insights!</p>

---

## Post #2 by @mikebind (2023-10-06 22:27 UTC)

<p>Try the <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes" rel="noopener nofollow ugc">StitchVolumes</a> module in the SlicerSandbox extension (installable through the Extension Manager) for the actual stitching step.  If the CT’s were acquired in the same session and the patient did not move between acquisitions, registration may not even be necessary, since the CT table motion will be accounted for in the DICOM header metadata.  If there is patient motion between acquisitions, registration will still be necessary, but the DICOM-based positioning will likely be a good starting point for registration.</p>

---
