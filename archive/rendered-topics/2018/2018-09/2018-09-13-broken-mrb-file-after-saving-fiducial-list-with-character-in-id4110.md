# Broken .mrb file after saving fiducial list with "&" character in title

**Topic ID**: 4110
**Date**: 2018-09-13
**URL**: https://discourse.slicer.org/t/broken-mrb-file-after-saving-fiducial-list-with-character-in-title/4110

---

## Post #1 by @mfolson (2018-09-13 21:04 UTC)

<p>Running Slicer 4.8.1 on Windows 7.</p>
<p>Created a new fiducial list with “&amp;” in the title and saved as .mrb file. I can keep working on the file without issue as long as it is not closed. When trying to reopen the .mrb, all data is missing even though the size is ~100mb. I’ll avoid special characters from now on, but just wanted to point this out.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2018-09-13 21:06 UTC)

<p>Thanks for reporting this. The issue has been fixed a couple of months ago. Any ASCII characters can be used in node names in recent nightly versions.</p>

---
