# Manually Set Up Slicer mrmlSceneChanged signals

**Topic ID**: 22548
**Date**: 2022-03-16
**URL**: https://discourse.slicer.org/t/manually-set-up-slicer-mrmlscenechanged-signals/22548

---

## Post #1 by @tsims (2022-03-16 19:36 UTC)

<p>Hello everyone!</p>
<p>I have been setting up a Slicer extensions that will create a number of inputs based on conditions in the scene, but I want to make sure that my qMRMLNodeComboBox is still recieving the scene change signals from the parent widget, what would be the best way to go about doing this?</p>
<p>My code right now looks something like this:</p>
<pre><code class="lang-auto"># Load widget from .ui file (created by Qt Designer).
        self.initialUiWidget = slicer.util.loadUI(
            self.resourcePath("UI/Core.ui")
        )
        self.layout.addWidget(self.initialUiWidget)
        self.ui = slicer.util.childWidgetVariables(self.initialUiWidget)

        # Set up Model Inputs
        ModelTabLayout = self.ui.ModelTab.layout()
        added = 2
        for key in self.InputModels:
            widget = slicer.util.loadUI(self.resourcePath("UI/InputSelector.ui"))
            widget.ModelLabel.text = key
            ModelTabLayout.addWidget(widget, added, 0)
            # I want to add the connection to the scene change here ideally
            added += 1

        # Set scene in MRML widgets.
        self.initialUiWidget.setMRMLScene(slicer.mrmlScene)
</code></pre>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2022-03-16 19:42 UTC)

<p>What you do looks good. You can call <code>setMRMLScene</code> on the parent widget or on individual qMRMLNodeCombobox widgets anytime. If you set the same scene again it will not cause any problem (it will be just ignored).</p>

---
