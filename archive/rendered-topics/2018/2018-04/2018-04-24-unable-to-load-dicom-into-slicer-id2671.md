# Unable to load dicom into slicer

**Topic ID**: 2671
**Date**: 2018-04-24
**URL**: https://discourse.slicer.org/t/unable-to-load-dicom-into-slicer/2671

---

## Post #1 by @b_s_umesh_sherkhane (2018-04-24 09:59 UTC)

<p>Operating system: win7<br>
Slicer version:4.8<br>
Expected behavior:<br>
Actual behavior:</p>
<p>“”<br>
Slicer has caught an internal error.</p>
<p>You may be able to continue from this point, but results are undefined.</p>
<p>Suggested action is to save your work and restart.</p>
<p>If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="nofollow noopener">http://slicer.org</a></p>
<p>The message detail is:</p>
<p>Exception thrown in event: Calling methods on uninitialized ctkDICOMItem""</p>

---

## Post #2 by @pieper (2018-04-24 10:56 UTC)

<p>It’s possible your dicom files are not a form Slicer can understand - have a look at the suggestions in this FAQ:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/FAQ/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/FAQ/DICOM</a></p>

---

## Post #3 by @b_s_umesh_sherkhane (2018-05-02 10:31 UTC)

<p>Dear Steve,</p>
<p>Thank you for the response. I figured out that the local database folder of dicom browser was messed up. I resolved the issue by changing the local database folder to a new directory. It now loads the dicom files.</p>

---
