# export in single fscv file

**Topic ID**: 18823
**Date**: 2021-07-20
**URL**: https://discourse.slicer.org/t/export-in-single-fscv-file/18823

---

## Post #1 by @Kever_L (2021-07-20 19:16 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.11.20210226 r29738<br>
Expected behavior: export all curves + fiducial in a single .fcsv<br>
Actual behavior: only possible to save curves individually in several .fscv</p>
<p>Hello,<br>
I was wondering if there is a way to export my fiducials and curves in a signle fcsv files instead of saving one files per curves or “group” of fiducials</p>
<p>Thank you in advance</p>

---

## Post #2 by @muratmaga (2021-07-20 19:40 UTC)

<p>You can use the MergeMarkups of SlicerMorph to merge open curve markups into a single markups node. Here is the tutorial <a href="https://github.com/SlicerMorph/Tutorials/tree/main/MergeMarkups" class="inline-onebox">Tutorials/MergeMarkups at main · SlicerMorph/Tutorials · GitHub</a></p>
<p>You should be able keep your fiducials in a single markup node without any problem. A fiducial markup node can contain any number of fiducials in it. Perhaps you are generating a Fiducial nodes as singletons (see this <a href="https://discourse.slicer.org/t/markups-node-creation-icon-is-confusing-users/9016" class="inline-onebox">Markups node creation icon is confusing users</a>). In any event, you can copy and paste fiducials across nodes.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c6114037b4871ba72b7992f6ce00cf6004c6926.png" alt="image" data-base62-sha1="aTGh9ZazwvwFy3GdqrijBdx740u" width="396" height="75"></p>

---
