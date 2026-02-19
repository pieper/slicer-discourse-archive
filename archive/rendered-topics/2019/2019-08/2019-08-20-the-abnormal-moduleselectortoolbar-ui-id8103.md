---
topic_id: 8103
title: "The Abnormal Moduleselectortoolbar Ui"
date: 2019-08-20
url: https://discourse.slicer.org/t/8103
---

# The abnormal ModuleSelectorToolBar UI

**Topic ID**: 8103
**Date**: 2019-08-20
**URL**: https://discourse.slicer.org/t/the-abnormal-moduleselectortoolbar-ui/8103

---

## Post #1 by @JaceYang (2019-08-20 02:22 UTC)

<p>Hello everyone:<br>
I have modified the qSlicerModuleSelectorToolBar.cxx and the qSlicerModulesMenu.cxx.Then something strange happened.<br>
on some computers the UI is normal.And on some computers the UI is abnormal as this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca88ffe5c68da5b522743f9d4de0e08fcc372e16.png" alt="image" data-base62-sha1="sTHY641iaBqYRy0mNV4fAkBoCRo" width="401" height="58"><br>
And when I moved the ModuleSelectorToolBar, it cannot dock in the toolbar:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3871a4f16c06390f8b0a02e1698e705551cef77f.png" alt="image" data-base62-sha1="83kdEgP6F2CQkHgfmWy06Alk0wf" width="404" height="58"><br>
I have already updated the NVIDIA display driver to the lastest version and there’s no intel core display card on this computer.<br>
I think there’s no problem in the modified code because on some other computers the UI is normal.<br>
Any help will be appreciated.</p>

---

## Post #2 by @lassoan (2019-08-21 16:17 UTC)

<p>Does the unmodified  qSlicerModuleSelectorToolBar work correctly? If yes, then most likely the problem is caused by your changes. Without seeing what you have modified we have no chance of guessing what is wrong with it.</p>

---
