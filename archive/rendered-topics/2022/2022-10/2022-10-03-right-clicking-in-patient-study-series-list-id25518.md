# Right-clicking in patient/study/series list

**Topic ID**: 25518
**Date**: 2022-10-03
**URL**: https://discourse.slicer.org/t/right-clicking-in-patient-study-series-list/25518

---

## Post #1 by @fghazouani (2022-10-03 07:14 UTC)

<p>Hello,<br>
How to add an item like “View DICOM metadata, Delete, Export to file system, …” to the right-click in the Dicom browser.<br>
Thank you.</p>

---

## Post #2 by @pieper (2022-10-03 14:29 UTC)

<p>That code is <a href="https://github.com/commontk/CTK/blob/a4ab685c75ed4638d583f916065fa61a76633337/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp">in CTK</a> so you can modify there and rebuild the application.</p>

---

## Post #3 by @fghazouani (2022-10-03 16:38 UTC)

<aside class="quote no-group" data-username="fghazouani" data-post="1" data-topic="25518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/f07891/48.png" class="avatar"> fghazouani:</div>
<blockquote>
<p>View DICOM metadata</p>
</blockquote>
</aside>
<p>That’s great. Thank you for your reply!</p>

---
