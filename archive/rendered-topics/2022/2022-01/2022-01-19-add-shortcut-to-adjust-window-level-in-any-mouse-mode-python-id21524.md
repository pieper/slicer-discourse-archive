---
topic_id: 21524
title: "Add Shortcut To Adjust Window Level In Any Mouse Mode Python"
date: 2022-01-19
url: https://discourse.slicer.org/t/21524
---

# Add shortcut to adjust window/level in any mouse mode python script not working

**Topic ID**: 21524
**Date**: 2022-01-19
**URL**: https://discourse.slicer.org/t/add-shortcut-to-adjust-window-level-in-any-mouse-mode-python-script-not-working/21524

---

## Post #1 by @Shahnawaz_Vora (2022-01-19 07:41 UTC)

<p>I am trying to use this python script for Brightness/contrast shortcut but it gives me error . Can someone help me</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: ‘MRMLDisplayableManagerPython.vtkMRMLScalarBarDispl’ object has no attribute ‘GetWindowLevelWidget’</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c72cfe8e8111a3fb52086bf38dea6ce0449f8cf.png" data-download-href="/uploads/short-url/mk0t5V0wlHS3UHd2MpSB4ImuN6D.png?dl=1" title="discourse 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c72cfe8e8111a3fb52086bf38dea6ce0449f8cf.png" alt="discourse 1" data-base62-sha1="mk0t5V0wlHS3UHd2MpSB4ImuN6D" width="690" height="148" data-dominant-color="252426"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">discourse 1</span><span class="informations">1010×218 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-02-25 06:58 UTC)

<p>You need to use a recent Slicer Preview Release for this.</p>
<p>For reference, the complete example that allows using Ctrl+Right-click-and-drag for adjusting window/level in Red slice view is available <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#add-shortcut-to-adjust-window-level-in-any-mouse-mode">here</a>.</p>

---
