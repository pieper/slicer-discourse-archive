# GPA issue with factor

**Topic ID**: 36918
**Date**: 2024-06-20
**URL**: https://discourse.slicer.org/t/gpa-issue-with-factor/36918

---

## Post #1 by @coco (2024-06-20 15:59 UTC)

<p>Dear all, I am facing a recurrent bug with the factor option in the PCA Scatter Plot options in the module alpaca.<br>
It s a linux version on calculation server but usually, the first time I am running slicer, I manage to create the factor and the PCA gets displayed properly.<br>
Second time round, it s nothing else than temperamental. Clicking everywhere many times sometimes eventually results in success. It’s very odd.<br>
Is there any issues that are know with the factor option ?<br>
Best<br>
s</p>

---

## Post #2 by @muratmaga (2024-06-20 16:41 UTC)

<p>First what’s the version of the Slicer you are working with? Is it the latest stable (5.6.2)</p>
<p>The factor you have to define each time from scratch if you are rerunning the analysis. So if you run the GPA a second time, you still should enter the factor table entries. We are in the process of changing this, and making covariate entry as part of the input to analysis.</p>

---

## Post #3 by @coco (2024-06-21 07:07 UTC)

<p>Dear Murat,<br>
thanks for your reply.<br>
I’m using 5.6.1 so will reinstall the latest.<br>
When I reset everything without restarting the software, I still have troubles though. Good news you are working on this.<br>
Many thanks<br>
s</p>

---
