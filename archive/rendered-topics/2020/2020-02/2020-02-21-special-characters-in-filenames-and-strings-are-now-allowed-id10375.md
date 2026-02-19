---
topic_id: 10375
title: "Special Characters In Filenames And Strings Are Now Allowed"
date: 2020-02-21
url: https://discourse.slicer.org/t/10375
---

# Special characters in filenames and strings are now allowed

**Topic ID**: 10375
**Date**: 2020-02-21
**URL**: https://discourse.slicer.org/t/special-characters-in-filenames-and-strings-are-now-allowed/10375

---

## Post #1 by @lassoan (2020-02-21 04:12 UTC)

<p>Starting from Slicer Preview Release 4.11.0-2020-02-21, special characters are permitted in file names and in any other user-defined text (such as node names, string parameters, etc.).</p>
<p>It was a large change throughout Slicer and some dependent libraries, therefore it is expected that special characters can cause problems or do not appear correctly at some places, but these are now considered errors that we should be able to fix them (so please report if you encounter any problem).</p>
<p>On Windows, the required UTF-8 code page support is only available from Windows 10 Version 1903 (May 2019 Update), so earlier Windows versions must be updated to use non-ASCII characters.</p>
<p>For more information and developer instructions, see this topic: <a href="https://discourse.slicer.org/t/slicer-switches-to-utf-8-everywhere/10374" class="inline-onebox">Slicer switches to UTF-8 everywhere</a></p>

---
