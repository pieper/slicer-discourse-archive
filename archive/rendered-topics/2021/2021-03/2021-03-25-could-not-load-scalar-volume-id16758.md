# Could not load...scalar volume

**Topic ID**: 16758
**Date**: 2021-03-25
**URL**: https://discourse.slicer.org/t/could-not-load-scalar-volume/16758

---

## Post #1 by @Patrick (2021-03-25 05:54 UTC)

<p>Hi,</p>
<p>I just updated to the most current version of Slicer. When I tried re-opening my DICOM files, there is a pop-up saying the file cannot be loaded as a scalar volume (I was able to open these files prior to updating). I’ve read the other forum posts regarding this situation but am unsure as to how to fix it.</p>
<p>Thank you in advance for the help.</p>
<p>Patrick</p>

---

## Post #2 by @pieper (2021-03-25 12:48 UTC)

<p>Check the troubleshooting guide, and if you still have trouble let us know the exact versions of Slicer that did and didn’t work with this data. If there’s been a regression in the software we’d want to know the details and fix it.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>

---

## Post #3 by @Patrick (2021-03-26 02:23 UTC)

<p>I currently have version 4.11.20210226 installed. This is the version that does not work with the data.<br>
The previous version I had installed, that worked with the data, was 4.10.2 (not sure of the numbers following)</p>
<p>Thank you.</p>

---

## Post #4 by @pieper (2021-03-26 14:20 UTC)

<p>That helps, thanks.</p>
<p>I don’t think there are any known regressions, so it’s probably something unique to this data.  Can you confirm you tried the troubleshooting suggestions?  What did you find?</p>

---

## Post #5 by @jmarcelopes (2021-05-24 22:37 UTC)

<p>I’m having the same problem as well. All my DICOM files are showing the “Scalar Mode” trouble with the 20210226 version</p>

---

## Post #6 by @pieper (2021-05-24 22:40 UTC)

<p>We’d like to get to the bottom of any dicom regressions.  Did you try the troubleshooting steps?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>

---

## Post #7 by @jmarcelopes (2021-05-24 22:45 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="16758">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>We’d like to get to the bottom of any dicom regressions.</p>
</blockquote>
</aside>
<p>Thanks for the support. Yes, I’ve tried. Already downloaded the original files with no anonymazer. I think I’m going to try an older version</p>

---

## Post #8 by @jmarcelopes (2021-05-24 22:57 UTC)

<p>And if you need, I can share de data with no problem, thanks a lot</p>

---

## Post #9 by @pieper (2021-05-27 19:20 UTC)

<p>If you are still having trouble and can post anonymized example data to a dropbox, google drive, or similar than probably someone can have a look at it.</p>

---
