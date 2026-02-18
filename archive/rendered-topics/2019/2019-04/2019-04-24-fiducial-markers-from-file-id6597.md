# Fiducial markers from file

**Topic ID**: 6597
**Date**: 2019-04-24
**URL**: https://discourse.slicer.org/t/fiducial-markers-from-file/6597

---

## Post #1 by @Jainey (2019-04-24 23:56 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.10<br>
Expected behavior: Attempting to add fiducial markers from FCSV file<br>
Actual behavior: False command<br>
I am trying to import fiducial markers from saved FCSV file to the current image. I have tried this command.</p>
<p>slicer.util.loadMarkupsFiducialList(‘D:/fcsv/C.fcsv/to/list/F.fcsv’)<br>
I am getting a false error- Am I specifying the path wrong. I ve no programming knowledge.</p>
<p>Could someone please help.</p>
<p>My fcsv is store in D; FCSV folder and as C.fcsv</p>
<p>Thanks a lot</p>

---

## Post #2 by @lassoan (2019-04-25 03:29 UTC)

<p>I can successfully load a .fcsv file on Windows10 using <code>slicer.util.loadMarkupsFiducialList("c:/Users/andra/Documents/F.fcsv")</code>. If you can load the same file using “Add data” dialog then most likely you entered an incorrect path.</p>

---

## Post #3 by @Jainey (2019-05-01 17:31 UTC)

<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a> This sorted the problem</p>

---
