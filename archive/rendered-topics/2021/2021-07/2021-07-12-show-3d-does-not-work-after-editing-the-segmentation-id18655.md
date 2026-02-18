# Show 3D does not work after editing the segmentation

**Topic ID**: 18655
**Date**: 2021-07-12
**URL**: https://discourse.slicer.org/t/show-3d-does-not-work-after-editing-the-segmentation/18655

---

## Post #1 by @bywbilly (2021-07-12 21:50 UTC)

<p>Hi,</p>
<p>I have a CT scan and its segmentation. I can create a 3D view of the segmentation through the show 3D of the segmentation editor module.</p>
<p>However, when I create a new label using the threshold method in the segmentation editor module, I cannot render the 3D view ever. Moreover, after I did this, I cannot render a segmentation that I can render before. I have to reopen slicer app to do the show 3D function.</p>
<p>And I checked the log, there are no warning/error messages. Also, I am sure I click the button to make sure the 3D model is in the middle. And I also try to turn the surface smooth off but it didn’t work.</p>
<p>I am wondering do you have any idea why? My slicer version is 4.11.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2021-07-13 01:55 UTC)

<p>Please test if you can reproduce this issue with the latest Slicer Preview Release.</p>

---

## Post #3 by @rbumm (2021-07-13 16:19 UTC)

<p>Did you maybe select the overwrite option when you used the threshold function to create the new, additional segment?</p>

---

## Post #4 by @rbumm (2021-07-13 16:31 UTC)

<p>I just tried the whole thing with “allow overlap” and 3.11 as well as the latest slicer build and did not get such a problem.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1e8cfe61d9f1dc38ab9c4466e22a54a8daee9e2.png" alt="image" data-base62-sha1="yw1RODLhvhDouYqiSVPf75Pm7Um" width="220" height="85"></p>

---
