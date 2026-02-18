# Shortcut for Sphere brush

**Topic ID**: 13460
**Date**: 2020-09-12
**URL**: https://discourse.slicer.org/t/shortcut-for-sphere-brush/13460

---

## Post #1 by @hherhold (2020-09-12 15:00 UTC)

<p>I’m trying to set up a key shortcut in python to enable/disable sphere brush in PaintEffect. The first step is code to set that parameter, which I’m doing like this:</p>
<pre><code>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
paintEffect = segmentEditorWidget.effectByName("Paint")
paintEffect.setCommonParameter("BrushSphere", False)
paintEffect.updateGUIFromMRML()
</code></pre>
<p>The parameter does not seem to change the brush behavior and I don’t get any changes reflected in the GUI. What am I doing wrong here?</p>
<p>Thanks!!!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2020-09-17 03:37 UTC)

<p>Instead of creating a new widget, refer to the Segment Editor module’s widget:</p>
<pre><code class="lang-auto">segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
paintEffect = segmentEditorWidget.effectByName("Paint")
paintEffect.setCommonParameter("BrushSphere", 1)  # enable
paintEffect.setCommonParameter("BrushSphere", 0)  # disable
</code></pre>

---

## Post #3 by @hherhold (2020-09-17 12:26 UTC)

<p>Oh, I see - I didn’t realize that I was creating a new widget (rather than finding the existing one).</p>
<p>THANKS!</p>
<p>-Hollister</p>

---
