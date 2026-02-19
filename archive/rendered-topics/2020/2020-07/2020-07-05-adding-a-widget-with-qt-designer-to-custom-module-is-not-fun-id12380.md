---
topic_id: 12380
title: "Adding A Widget With Qt Designer To Custom Module Is Not Fun"
date: 2020-07-05
url: https://discourse.slicer.org/t/12380
---

# Adding a widget with Qt Designer to custom module is not functional

**Topic ID**: 12380
**Date**: 2020-07-05
**URL**: https://discourse.slicer.org/t/adding-a-widget-with-qt-designer-to-custom-module-is-not-functional/12380

---

## Post #1 by @chir.set (2020-07-05 11:43 UTC)

<p>I could not get a qMRMLNodeComboBox to work in a custom module created by Extension Wizard.</p>
<p>It is added to the module’s UI with Qt Designer and its nodeTypes property set to vtkMRMLScalarVolumeNode. The attached screenshot shows that the appended qMRMLNodeComboBox is always disabled, and above all, is never populated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ada7168983876adf5045f32520b8fb2cbe00b372.png" data-download-href="/uploads/short-url/oMcAnRAxOLuRoL26fy0JKxFSGkO.png?dl=1" title="Screenshot_20200705_121652" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ada7168983876adf5045f32520b8fb2cbe00b372_2_428x499.png" alt="Screenshot_20200705_121652" data-base62-sha1="oMcAnRAxOLuRoL26fy0JKxFSGkO" width="428" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ada7168983876adf5045f32520b8fb2cbe00b372_2_428x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ada7168983876adf5045f32520b8fb2cbe00b372.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ada7168983876adf5045f32520b8fb2cbe00b372.png 2x" data-dominant-color="33383D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20200705_121652</span><span class="informations">572×667 31.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Whether the appended qMRMLNodeComboBox is added to updateGUIFromParameterNode and to updateParameterNodeFromGUI does not help.</p>
<p>Qt Designer is helpful to design UI, but I could not get it to work. Please see this <a href="https://yadi.sk/d/RW_LiqrYqCgg0Q" rel="noopener nofollow ugc">link</a> for the test module used here, and advise about a fix.</p>
<p>Regards.</p>

---

## Post #2 by @jamesobutler (2020-07-05 12:45 UTC)

<p>I think that is usually the case when you haven’t set the mrmlScene to the mrml widget. See <a href="https://github.com/Slicer/Slicer/blob/36f626ac5dabad2052da1e429b4565034a2726bb/Utilities/Templates/Modules/Scripted/TemplateKey.py#L117-L120" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/36f626ac5dabad2052da1e429b4565034a2726bb/Utilities/Templates/Modules/Scripted/TemplateKey.py#L117-L120</a></p>

---

## Post #3 by @chir.set (2020-07-05 19:16 UTC)

<p>Yes, now it works, will have to discover other hidden features of Qt Designer. Thank you.</p>

---
