---
topic_id: 11535
title: "Bug Screencapture Always Deletes Temp Files With Fix And Pul"
date: 2020-05-14
url: https://discourse.slicer.org/t/11535
---

# BUG - ScreenCapture always deletes temp files (with fix and pull request)

**Topic ID**: 11535
**Date**: 2020-05-14
**URL**: https://discourse.slicer.org/t/bug-screencapture-always-deletes-temp-files-with-fix-and-pull-request/11535

---

## Post #1 by @hherhold (2020-05-14 12:40 UTC)

<p>Hey all,</p>
<p>I found an issue with ScreenCapture this morning where it would delete the temp files even if “image series” is selected. This would result in Slicer making the image series and then deleting it. The file deletion should only occur when the images are used for making a video or Lightbox. I made a fix and submitted a pull request, please let me know if the request is not formatted correctly (been a while since I did this) and I can resubmit.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---
