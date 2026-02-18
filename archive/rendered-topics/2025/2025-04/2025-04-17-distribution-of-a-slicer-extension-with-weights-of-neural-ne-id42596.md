# Distribution of a Slicer Extension with weights of neural networks

**Topic ID**: 42596
**Date**: 2025-04-17
**URL**: https://discourse.slicer.org/t/distribution-of-a-slicer-extension-with-weights-of-neural-networks/42596

---

## Post #1 by @IVarha (2025-04-17 06:38 UTC)

<p>Hello, I am developing an extension to a 3D slicer and I have noticed that I have some heavy files in resources. Is there any guidance how to handle that? GitHub does not allow files above 50 megabytes and I think that unpacking files on every launch from Resourse folder is not a best option.</p>
<p>Thank you in advance</p>

---

## Post #2 by @rfenioux (2025-04-17 07:49 UTC)

<p>What you can do is upload the weights as a release asset on github, then download them at runtime (this way you can probe the user before downloading).</p>
<p>Have a look at how it’s done in the Dental Segmentator extension <a href="https://github.com/gaudot/SlicerDentalSegmentator/blob/1e7a0f3d772bb2773d165429197a634084486d66/DentalSegmentator/DentalSegmentatorLib/PythonDependencyChecker.py#L58" rel="noopener nofollow ugc">source code</a>, where the weights are downloaded from the <a href="https://github.com/gaudot/SlicerDentalSegmentator/releases" rel="noopener nofollow ugc">github release assets</a>.</p>

---

## Post #3 by @IVarha (2025-04-24 08:54 UTC)

<p>Thank you for a reply.</p>
<p>The solution itself looks good. I think I will try to incorporate something similar to my solution. If there is no more elegant way to do that.</p>

---

## Post #4 by @lassoan (2025-04-26 12:54 UTC)

<p>Storing model weights in GitHub releases is a very robust, elegant, flexible, and free solution. It allows you to store your source code and data at the same place, and you also get basic download statistics. What more elegant way would you have in mind?</p>

---

## Post #5 by @IVarha (2025-04-28 11:19 UTC)

<p>Thang you for you reply Andras,<br>
For me ideal way would be is that I would not need to add a custom method to dowload weights.<br>
For my plugin I decreased network sizes therefore it is now allowable to upload to GitHub.</p>

---
