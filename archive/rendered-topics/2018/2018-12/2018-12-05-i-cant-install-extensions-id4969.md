---
topic_id: 4969
title: "I Cant Install Extensions"
date: 2018-12-05
url: https://discourse.slicer.org/t/4969
---

# I can't install extensions

**Topic ID**: 4969
**Date**: 2018-12-05
**URL**: https://discourse.slicer.org/t/i-cant-install-extensions/4969

---

## Post #1 by @rojer (2018-12-05 13:29 UTC)

<p>Problem report for Slicer 4.8.1 win-amd64: [The extension lib and share folds were downloaded successfully, but a warning “Failed to remove directory C:/Users/dell/AppData/Roaming/NA-MIC/Extensions-26813/SlicerDMRI/26813-win-amd64-SlicerDMRI-git3ae6094-2017-12-20” was shown. When I restarted Slicer, the module SlicerDMRI could not be found in All Modules. ]</p>

---

## Post #2 by @lassoan (2018-12-05 13:32 UTC)

<p>Probably another instance of Slicer was running (maybe in the background). Restart your computer and uninstall/install SlicerDMRI.</p>
<p>If you are interested in what application prevented deleting the folder (if it was Slicer or something else) then you can install <a href="https://lockhunter.com/" rel="nofollow noopener">LockHunter</a> tool, right-click on the folder that cannot be removed, and click on “What is locking this folder?”.</p>
<p>Please use the latest stable version (currently 4.10.0) or, if you need some recently added features, then the latest nightly version. We do not have the capacity to investigate potential problems with older releases.</p>

---
