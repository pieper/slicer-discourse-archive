---
topic_id: 371
title: "Subjecthierarchy Module Does Not Work In The Nightly Build"
date: 2017-05-24
url: https://discourse.slicer.org/t/371
---

# SubjectHierarchy Module does not work in the nightly build

**Topic ID**: 371
**Date**: 2017-05-24
**URL**: https://discourse.slicer.org/t/subjecthierarchy-module-does-not-work-in-the-nightly-build/371

---

## Post #1 by @brhoom (2017-05-24 14:08 UTC)

<p>Hi<br>
for sometimes now I have this problem. Is it a bug? or you replace it with something else?<br>
regards!<br>
Ibraheem</p>

---

## Post #2 by @lassoan (2017-05-24 14:24 UTC)

<p>Subject hierarchy module has been merged with Data module. You need to update your toolbar shortcuts (menu: Edit / Application settings / Modules): delete Subject Hierarchy, add Data module to Favorite modules. Alternatively, you can just delete your Slicer.ini file (in your application settings directory) and next time you start Slicer, it’ll recreate the correct shortcuts.</p>

---
