---
topic_id: 4824
title: "Model Doesnt Show Colors Of Scalars"
date: 2018-11-20
url: https://discourse.slicer.org/t/4824
---

# Model doesn't show colors of scalars

**Topic ID**: 4824
**Date**: 2018-11-20
**URL**: https://discourse.slicer.org/t/model-doesnt-show-colors-of-scalars/4824

---

## Post #1 by @ghnguyen (2018-11-20 21:23 UTC)

<p>Hi,</p>
<p>I am trying to a custom loadable module in Python that has a QComboBox that shows the scalars similar to the one in the Models module. The item list and combo box work fine but the colors are not updated correctly on the model. I checked the correct ModelDisplayNode and saw that the ActiveScalarName, ScalarRangeFlag were all correct but the ScalarRange is always at (0, -1). The only way to fix this is to go to the Models module and click on that exact model node and then the color will be updated accordingly.<br>
Here are the relevant pieces of code:</p>
<pre><code>
# ComboBox
bio_mech_selector = qt.QComboBox()
bio_mech_selector.activated.connect(self.on_select_scalar)
# Function 
def on_select_scalar(self):
    if self.timeline_slider.value&gt;0:
        self.model_display_node = slicer.mrmlScene.GetNodeByID("SomeNodeID")
        self.model_display_node.SetActiveScalarName(self.bio_mech_selector.currentText)</code></pre>
<p>I have several model nodes that can be selected using a slider and use a single model_display_node. My question is how can I make the Combo Box choice apply the colors correctly without the need to go to Models module and click on each of the model nodes?</p>

---

## Post #2 by @lassoan (2018-11-20 23:57 UTC)

<p><code>SetActiveScalarName</code> only sets the scalar name, but you also need to set scalar location (point or cell data). I would recommend using <code>SetActiveScalar</code> method, which sets scalar name and location at once.</p>

---
