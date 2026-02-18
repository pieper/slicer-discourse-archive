# Removing "ROI type" and "Inside Out" controls from qMRMLMarkupsROIWidget

**Topic ID**: 36922
**Date**: 2024-06-20
**URL**: https://discourse.slicer.org/t/removing-roi-type-and-inside-out-controls-from-qmrmlmarkupsroiwidget/36922

---

## Post #1 by @rasakereh (2024-06-20 19:37 UTC)

<p>I am developing a plugin which uses “qMRMLMarkupsROIWidget” inside of it. However, I do not want the user to be able to change the ROI type to anything but “Box”. Additionally, I prefer to remove the checkbox labelled as “Inside out:”</p>
<p>I looked into the documentation and could not find how to do it. Would you please help me with it?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2024-06-20 19:48 UTC)

<p>You can have a look at the .ui file of the <code>qMRMLMarkupsROIWidget</code> and hide the child widgets you don’t need. For example:</p>
<pre data-code-wrap="python"><code class="lang-python">widget = slicer.qMRMLMarkupsROIWidget()
widget.show()
widget.findChild("QLabel", "label").hide()
widget.findChild("QCheckBox", "insideOutCheckBox").hide()
widget.findChild("QLabel", "label_10").hide()
widget.findChild("QComboBox", "roiTypeComboBox").hide()
</code></pre>
<p>We don’t guarantee that the child widget names and types remain the same in future Slicer versions, so the ideal solution would be to add flags to the <code>qMRMLMarkupsROIWidget</code> to show/hide these components, but using the code snippet above is probably sufficient for now.</p>

---

## Post #3 by @rasakereh (2024-06-21 15:07 UTC)

<p>Thanks! Sounds reasonable. For what it’s worth, one can also iterate over all the children and find the relevant element using the element type and label for instance. It will make the solution immune to name changes!</p>

---

## Post #4 by @lassoan (2024-06-21 19:17 UTC)

<p>You have to use the Qt object name to identify a widget. Label or other text is not suitable for several reasons, for example not all widgets have some constant text  label, and even if they have, the label is language dependent (your script would break if someone changes the application language).</p>
<p>Widget class (<code>QLabel</code>, etc.) is indeed redundant. You don’t have to specify it if for example you use a Slicer helper function (or somewhat more complex Qt API). I just wanted to keep things simple show in my above example that there is nothing Slicer-specific about all these. Anyway, if you find the above code inconvenient then you can do this instead:</p>
<pre data-code-wrap="python"><code class="lang-python">widget = slicer.qMRMLMarkupsROIWidget()
for name in ["label", "insideOutCheckBox", "label_10", "roiTypeComboBox"]:
    slicer.util.findChild(widget, name).hide()
widget.show()
</code></pre>

---
