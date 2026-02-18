# How to fix volume issue using CTlungAnalyser extension

**Topic ID**: 16347
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/how-to-fix-volume-issue-using-ctlunganalyser-extension/16347

---

## Post #1 by @full_stack_master (2021-03-04 01:52 UTC)

<p>I have imported the Ct lung analyser extension with the extension mode because I can not find the module in extensions.</p>
<p>And when I run this module, I have found the issue</p>
<p>self.resampledVolume = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLScalarVolumeNode”, “Resampled Volume”)</p>
<p>if the this function runs, inputvolume value is initialized<br>
how can I fix this issue</p>

---

## Post #2 by @lassoan (2021-03-04 01:53 UTC)

<p>Which Slicer version do you use?</p>

---

## Post #3 by @full_stack_master (2021-03-04 01:57 UTC)

<p>Our version is 4.10.</p>

---

## Post #4 by @lassoan (2021-03-04 01:59 UTC)

<p>OK, that explains it. This extension is not compatible with Slicer-4.10. Please use the latest Slicer Stable Release or Slicer Preview Release.</p>

---

## Post #5 by @full_stack_master (2021-03-04 02:33 UTC)

<p>thanks<br>
but May I find the solution how to use this module?<br>
because I have some issues to update the new version now</p>

---

## Post #6 by @lassoan (2021-03-04 02:36 UTC)

<p>Sorry, you need to upgrade to a recent Slicer version. Any computer that was manufactured in the last 5 years should work (starting from about 300 dollars), but if you don’t want to buy a computer then you can rent a virtual machine from one of the cloud providers for a few dollars per hour. You can also find free services that can run Slicer on the web, such as <a href="https://mybinder.org/v2/gh/Slicer/SlicerNotebooks/master?filepath=SlicerWeb.ipynb">Binder</a>.</p>

---

## Post #7 by @full_stack_master (2021-03-04 02:45 UTC)

<p>I am sorry but I did not mean the Money.<br>
I have already launched our own applications  which is based on 4.10 version<br>
and I can not update the base code of them now<br>
this is a bit complex<br>
so if you have any solution how to use this module without updated code<br>
please let me know</p>

---

## Post #8 by @lassoan (2021-03-04 02:47 UTC)

<p>We can help you here with upgrading your code to work with latest Slicer versions. If you need help with old Slicer versions then you need to contact a <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#commercial-partners">Slicer commercial partner</a> for getting paid support.</p>

---

## Post #9 by @lassoan (2021-03-06 12:50 UTC)

<p>2 posts were split to a new topic: <a href="/t/how-to-run-slicer-on-the-cloud-and-access-in-a-web-browser/16401">How to run Slicer on the cloud and access in a web browser</a></p>

---
