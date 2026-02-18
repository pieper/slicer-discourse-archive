# .CSV files as markup files

**Topic ID**: 16574
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/csv-files-as-markup-files/16574

---

## Post #1 by @CHumphreys (2021-03-16 14:36 UTC)

<p>Hi everyone,</p>
<p>I have a bunch of csv files with landmark data that I got from an older version of 3D slicer. When i try to load the scene that is linked to these csv files, they don’t come seem to open. Has anyone else had this issue and know of a way to convert csv files to fcsv so they can open? I have converted from fscv to csv previously but then those files won’t open in slicer either.</p>
<p>Any help would be greatly appreciated <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #2 by @muratmaga (2021-03-16 21:01 UTC)

<p>csv files will be read as table. FCSV has a header that enables them to be loaded correctly as markups. If you converted your fcsv to csv, you probably stripped the header. You might be able to reconstitute by simply copy and pasting the header from a blank fcsv file you create.</p>

---

## Post #3 by @lassoan (2021-03-26 03:24 UTC)

<p>You can also easily combine and edit markup control point lists using copy-paste. You can copy-paste points directly to an Excel sheet, edit/remove rows, and copy-paste them back to Slicer.</p>

---

## Post #4 by @CHumphreys (2021-03-26 10:18 UTC)

<p>Thank you both <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>I have managed to rebuild the markup files so that they now reopen. The copy and paste of the points from the csv files back into slicer worked a treat!</p>

---
