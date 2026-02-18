# "Segment Editor" Panel Completely Blank

**Topic ID**: 15793
**Date**: 2021-02-02
**URL**: https://discourse.slicer.org/t/segment-editor-panel-completely-blank/15793

---

## Post #1 by @d_roscoe_j (2021-02-02 13:11 UTC)

<p>I’ve been working on editing a VOL file and when I select “Segment Editor” to start removing parts of the model, the panel that should contain all the segment editor tools is completely blank.<br>
I’ve attempted to uninstall and re-install the software and done everything within my limited scope to try and view this set of options, but keep running in to the same issue.</p>
<p>Has anyone faced this issue or know how I might resolve it?<br>
Thanks!</p>

---

## Post #2 by @lassoan (2021-02-02 13:27 UTC)

<p>Can you attach a screenshot?</p>
<p>You may need to reset your application settings by deleting (or temporarily renaming) the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location">.ini files</a>.</p>

---

## Post #3 by @d_roscoe_j (2021-02-03 20:33 UTC)

<p>Thank you for your quick response!<br>
I followed that link and, while searching for the files it was telling me to search for (never found them) I started looking through the error log.</p>
<p>Found that<br>
“the module  “SegmentEditor” has no widget representation”<br>
and<br>
<strong>there is no UI for the module "SegmentEditor"</strong></p>
<p>After searching for the issue with that new info, I found another blog post (that you’d responded to) and found the solution!</p>
<p>I had it saved to a folder for a “User” that had an apostrophe in the name (“Roscoe’s PC”) and this punctuation was what evidently caused the issue.<br>
Uninstalled and Changed the destination folder when re-installing, and the problem went away!</p>
<p>Thanks again!</p>

---
