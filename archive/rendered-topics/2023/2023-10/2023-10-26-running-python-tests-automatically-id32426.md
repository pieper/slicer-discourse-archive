# Running Python tests automatically

**Topic ID**: 32426
**Date**: 2023-10-26
**URL**: https://discourse.slicer.org/t/running-python-tests-automatically/32426

---

## Post #1 by @jhlegarreta (2023-10-26 16:12 UTC)

<p>Hi,<br>
I am trying to figure out why some of the Python tests in an extension are not being executed following:<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/179#issuecomment-1665554265" class="inline-onebox" rel="noopener nofollow ugc">COMP: Update GHA workflow ensuring Slicer is built with NumPy support by jcfr · Pull Request #179 · SlicerDMRI/SlicerDMRI · GitHub</a></p>
<p>The dashboard does show some Python test being run:<br>
<a href="https://slicer.cdash.org/viewTest.php?onlypassed&amp;buildid=3189711" class="inline-onebox" rel="noopener nofollow ugc">CDash</a></p>
<p>But others are not being run, e.g.<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/2ba47ea8a5c03056823b91245a0710bee689ec26/Modules/Loadable/TractographyDisplay/Testing/Python/CMakeLists.txt#L12" rel="noopener nofollow ugc">https://github.com/SlicerDMRI/SlicerDMRI/blob/2ba47ea8a5c03056823b91245a0710bee689ec26/Modules/Loadable/TractographyDisplay/Testing/Python/CMakeLists.txt#L12</a></p>
<p>On that list, only the first one is run (not without warnings, though):<br>
<a href="https://slicer.cdash.org/test/25880272" class="inline-onebox" rel="noopener nofollow ugc">Test Results</a></p>
<p>I do see that the first one has some related additional CMake code in the previous link. I have tried to look for posts or documentation that explains how to write the related tests, and necessary CMake code, but have not found any relevant pointer.</p>
<p>Is there any resource I could have a look at to fix this situation? If not, can anybody briefly explain here how Python tests should be written and tests within an extension?</p>
<p>Thanks.</p>

---
