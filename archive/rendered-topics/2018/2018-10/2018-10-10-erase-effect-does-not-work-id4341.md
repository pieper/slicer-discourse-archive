---
topic_id: 4341
title: "Erase Effect Does Not Work"
date: 2018-10-10
url: https://discourse.slicer.org/t/4341
---

# Erase effect does not work

**Topic ID**: 4341
**Date**: 2018-10-10
**URL**: https://discourse.slicer.org/t/erase-effect-does-not-work/4341

---

## Post #1 by @Ash_Alarfaj (2018-10-10 09:56 UTC)

<p>Hi<br>
mac<br>
3d slicer version 4.8<br>
usually, I use threshold effect then correct by erasing or painting, but today the erase effect does not work.<br>
please see attachment</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/181fe86d94d804a323d554c178fdc20169a1b50c.jpeg" data-download-href="/uploads/short-url/3rpOWBLQUqtj59YQWBBXXrBpf9W.jpeg?dl=1" title="34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/181fe86d94d804a323d554c178fdc20169a1b50c_2_690x387.jpeg" alt="34" data-base62-sha1="3rpOWBLQUqtj59YQWBBXXrBpf9W" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/181fe86d94d804a323d554c178fdc20169a1b50c_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/181fe86d94d804a323d554c178fdc20169a1b50c_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/181fe86d94d804a323d554c178fdc20169a1b50c.jpeg 2x" data-dominant-color="9D9798"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">34</span><span class="informations">1366×768 388 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2018-10-10 11:38 UTC)

<p>Please add a copy of the log (under Help -&gt; report a bug)</p>

---

## Post #3 by @Ash_Alarfaj (2018-10-10 12:05 UTC)

<p>Hi<br>
okay, But I think this happened due to very thin slice thickness(2mm) and gap(4mm). when I’ve tried for slice thick 5, gap5 mm the problem disappeared. when I faced this problem again I will report bug.<br>
thanks</p>

---

## Post #4 by @pieper (2018-10-10 12:45 UTC)

<p>Hi <a class="mention" href="/u/ash_alarfaj">@Ash_Alarfaj</a> - just use the Report a bug dialog to get the log text to paste here (first review to make sure there’s no patient identifiers in it).  This will probably give the info needed to see what’s going on (can’t tell from just the screenshot).  There is probably an error message from when the tool didn’t work.  Depending on what’s in the log we may want to have a bug report filed.</p>

---

## Post #5 by @lassoan (2018-10-10 12:55 UTC)

<p>Most likely the issue is fixed in recent nightly version. <a class="mention" href="/u/ash_alarfaj">@Ash_Alarfaj</a> if you experience any similar issues using latest Slicer-4.9.x version then let us know.</p>

---
