# Hide module panel by default

**Topic ID**: 5156
**Date**: 2018-12-20
**URL**: https://discourse.slicer.org/t/hide-module-panel-by-default/5156

---

## Post #1 by @Ulla (2018-12-20 17:49 UTC)

<p>Hi,</p>
<p>I want to configure my Slicer so that the “Module panel” won’t show up when starting Slicer. Can that be done somewhere from application settings or with a Python script?</p>
<p>It doesn’t seem to be possible from application settings, it’s only possible to select a default startup module. I have tried with slicerrc.py to get reference to qSlicerModulePanel object so that I could hide it on startup, but I haven’t find a way to do it.</p>
<p>Br, Ulla</p>

---

## Post #2 by @lassoan (2018-12-20 17:53 UTC)

<p>You can hide the module panel from Python script (that you can include in the startup script) as shown here: <a href="https://gist.github.com/lassoan/7d4cec3012155e2597ee3f47157f0a65#file-simpleview-py-L10-L11" rel="nofollow noopener">https://gist.github.com/lassoan/7d4cec3012155e2597ee3f47157f0a65#file-simpleview-py-L10-L11</a> .</p>

---

## Post #3 by @lassoan (2018-12-20 18:38 UTC)

<p>A post was merged into an existing topic: <a href="/t/make-slicer-simpler-to-use-for-new-users/5059/29">Make Slicer simpler to use for new users</a></p>

---
