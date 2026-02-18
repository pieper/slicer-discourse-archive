# Save image with new window level

**Topic ID**: 22186
**Date**: 2022-02-25
**URL**: https://discourse.slicer.org/t/save-image-with-new-window-level/22186

---

## Post #1 by @codeenthusiast (2022-02-25 19:46 UTC)

<p>Hi everyone, I’m working on a deep learning project to perform automated segmentation of a ROI for given tumors.</p>
<p>I am finding that the tumor is not as visible with the pre-set window that is used upon opening the image. I can change the window level accordingly to see the ROI better but I am wondering how I can go about saving the image with the modified volume.</p>
<p>I tried saving it but upon loading it, it presumes the original window level. Thank you!</p>

---

## Post #2 by @ungi (2022-02-27 15:44 UTC)

<p>Window/level is not a property of the image data, it is just a setting in the image viewer. Changing the viewer setting does not change image data in Slicer or any other application. Deep learning algorithm does not use your viewer setting. If the tumor is visible with some window/level setting, then the information is already in the image data, and deep learning will find the tumor in the original images.</p>

---

## Post #3 by @codeenthusiast (2022-02-27 16:20 UTC)

<p>Thanks Tamas. I appreciate the clarification!</p>

---
