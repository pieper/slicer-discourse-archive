---
topic_id: 2503
title: "Pre Selecting Foreground And Background Volumes"
date: 2018-04-03
url: https://discourse.slicer.org/t/2503
---

# Pre-selecting Foreground and Background Volumes

**Topic ID**: 2503
**Date**: 2018-04-03
**URL**: https://discourse.slicer.org/t/pre-selecting-foreground-and-background-volumes/2503

---

## Post #1 by @asheu (2018-04-03 15:15 UTC)

<p>I want to pre-select the background and foreground volumes manually. Like seen below, right now there are no volumes selected for the background and foreground layer.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4b3309a7c348e33c719f84c3ba1716bb8f8ae7b.png" alt="image" data-base62-sha1="nv0duECvtKCuzTEQckzBpI8adfR" width="573" height="313"></p>
<p>I have tried the following methods but even after updating the view, the combo box value itself is not changed.</p>
<p>lm = slicer.app.layoutManager()<br>
sliceWidget = lm.sliceWidget(‘Red’)<br>
ForeCombo = findChild(sliceWidget, ‘ForegroundComboBox’)<br>
ForeCombo.setCurrentNodeID(‘whole_mouse_80micron_ct’)</p>
<p>I have also tried directly modifying the slice widget like so:</p>
<p>red_logic = slicer.app.layoutManager().sliceWidget(“Red”).sliceLogic()<br>
red_cn = red_logic.GetSliceCompositeNode()<br>
red_logic.GetSliceCompositeNode().SetBackgroundVolumeID(slicer.util.getNode(‘dwi’).GetID())</p>
<p>Any help would be appreciated!</p>

---

## Post #2 by @pieper (2018-04-03 15:30 UTC)

<p>This works for me:</p>
<pre><code class="lang-auto">import SampleData
h = SampleData.SampleDataLogic().downloadMRHead()
c = SampleData.SampleDataLogic().downloadCTACardio()
red_logic = slicer.app.layoutManager().sliceWidget('Red').sliceLogic()
red_cn = red_logic.GetSliceCompositeNode()
red_cn.SetBackgroundVolumeID(h.GetID())
</code></pre>
<p>And afterwards you should have this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a662831bd997a5168d1e1a2f08488b012b01e89d.jpeg" alt="image" data-base62-sha1="nJUjVq0iArEqZZVlgjqdcoPAmbb" width="689" height="377"></p>

---

## Post #3 by @adamrankin (2018-04-03 15:32 UTC)

<p>As Steve mentioned. More examples at</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository</a></p>

---

## Post #4 by @lassoan (2018-04-03 22:36 UTC)

<p>I think the easiest way to set which volumes to show in slice views is by using slicer.util.setSliceViewerLayers:</p>
<p><a href="http://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.setSliceViewerLayers" class="onebox" target="_blank">http://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.setSliceViewerLayers</a></p>

---
