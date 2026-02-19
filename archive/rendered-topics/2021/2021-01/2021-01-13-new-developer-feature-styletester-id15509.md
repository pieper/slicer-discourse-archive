---
topic_id: 15509
title: "New Developer Feature Styletester"
date: 2021-01-13
url: https://discourse.slicer.org/t/15509
---

# New Developer Feature - StyleTester

**Topic ID**: 15509
**Date**: 2021-01-13
**URL**: https://discourse.slicer.org/t/new-developer-feature-styletester/15509

---

## Post #1 by @Sam_Horvath (2021-01-13 16:42 UTC)

<p>We’ve added a new utility module to the SlicerSandbox extension,  <a href="https://github.com/PerkLab/SlicerSandbox/tree/master/StyleTester">StyleTester</a>.  StyleTester allows you to test modifying the appearance of the Slicer GUI using <a href="https://doc.qt.io/qt-5/stylesheet.html">Qt Style Sheets</a>.  Qt Style Sheets provide an very powerful method for customizing every aspect of the appearance of a Qt-based application like Slicer.</p>
<p>QSS code can be entered into the editor, or loaded from / saved to .qss files.  The module provides a set of example widgets that can be used to view effects of stylesheets on the most widely used objects. The StyleTester source code is also a good reference for reading and using stylesheets in custom code.</p>
<p>Example of applying a simple stylesheet to all of Slicer:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Before Apply</th>
<th>After Apply</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/859dd75fab8f8943658533db9241fc3321fa2982.png" data-download-href="/uploads/short-url/j41FYoLgxYrS4W9ntd3mhchsdTc.png?dl=1" title="Screenshot 2021-01-13 09.44.04"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/859dd75fab8f8943658533db9241fc3321fa2982_2_275x500.png" alt="Screenshot 2021-01-13 09.44.04" data-base62-sha1="j41FYoLgxYrS4W9ntd3mhchsdTc" width="275" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/859dd75fab8f8943658533db9241fc3321fa2982_2_275x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/859dd75fab8f8943658533db9241fc3321fa2982_2_412x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/859dd75fab8f8943658533db9241fc3321fa2982_2_550x1000.png 2x" data-dominant-color="393939"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-01-13 09.44.04</span><span class="informations">979×1778 57.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td></td>
</tr>
</tbody>
</table>
</div><p>The StyleTester is available starting in today’s Preview build through the SandBox extension.</p>
<hr>
<p>Sam</p>

---
