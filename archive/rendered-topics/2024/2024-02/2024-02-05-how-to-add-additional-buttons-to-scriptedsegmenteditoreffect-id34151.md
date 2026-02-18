# How to add additional buttons to scriptedsegmenteditoreffect?

**Topic ID**: 34151
**Date**: 2024-02-05
**URL**: https://discourse.slicer.org/t/how-to-add-additional-buttons-to-scriptedsegmenteditoreffect/34151

---

## Post #1 by @tueboesen (2024-02-05 11:25 UTC)

<p>I am creating an extension for segment editor using the scriptedsegmenteditoreffect, and I would like to add another button to the widget.<br>
I saw how the on_apply button is added in setupOptionFrame and tried to add another button in a similar fashion</p>
<pre><code>def setupOptionsFrame(self):

    # Object scale slider
    self.objectScaleMmSlider = slicer.qMRMLSliderWidget()
    self.objectScaleMmSlider.setMRMLScene(slicer.mrmlScene)
    self.objectScaleMmSlider.quantity = "length"  # get unit, precision, etc. from MRML unit node
    self.objectScaleMmSlider.minimum = 0
    self.objectScaleMmSlider.maximum = 10
    self.objectScaleMmSlider.value = 2.0
    self.objectScaleMmSlider.setToolTip("Increasing this value smooths the segmentation and reduces leaks. This is the sigma used for edge detection.")
    self.scriptedEffect.addLabeledOptionsWidget("Object scale:", self.objectScaleMmSlider)
    self.objectScaleMmSlider.connect("valueChanged(double)", self.updateMRMLFromGUI)

    # Apply button
    self.applyButton = qt.QPushButton("Accept")
    self.applyButton.objectName = self.__class__.__name__ + "Apply"
    self.applyButton.setToolTip("Accept previewed result")
    self.scriptedEffect.addOptionsWidget(self.applyButton)
    self.applyButton.connect("clicked()", self.onApply)

    # Do Nothing button
    self.dummyButton = qt.QPushButton("Dummy")
    self.dummyButton.objectName = self.__class__.__name__ + "Dummy"
    self.dummyButton.setToolTip("Dummy things")
    self.scriptedEffect.addOptionsWidget(self.dummyButton)
    self.dummyButton.connect("clicked()", self.onDummy)
</code></pre>
<p>This adds a new button in the widget, but unfortunately I am still missing something since the button does not activate the on_dummy function as hoped. (See the image below)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd77cdcb4c2f4f526f7bc21a2992e0918bfb8777.png" data-download-href="/uploads/short-url/tjEyIWl0GTrSrjNgdcFlDlZtcMv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd77cdcb4c2f4f526f7bc21a2992e0918bfb8777_2_203x500.png" alt="image" data-base62-sha1="tjEyIWl0GTrSrjNgdcFlDlZtcMv" width="203" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd77cdcb4c2f4f526f7bc21a2992e0918bfb8777_2_203x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd77cdcb4c2f4f526f7bc21a2992e0918bfb8777_2_304x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd77cdcb4c2f4f526f7bc21a2992e0918bfb8777_2_406x1000.png 2x" data-dominant-color="EAEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">661×1621 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So how do I get more control over this button that I am adding, or is this not possible when using scriptedsegmenteditoreffect?<br>
If it is possible, then where I can find more information/documentation about this problem?</p>

---

## Post #2 by @tueboesen (2024-03-04 09:36 UTC)

<p>I still haven’t figured out an answer to this question.<br>
I have tried reading up on the scriptedsegmenteditoreffect, but I can’t really find much in terms of documentation in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/index.html" class="inline-onebox" rel="noopener nofollow ugc">Developer Guide — 3D Slicer documentation</a> and when searching for it on the github page I also do not really gain much in terms of code to look at.</p>
<p>I would appreciate if anyone could point me in the right direction</p>

---

## Post #3 by @pieper (2024-03-04 14:39 UTC)

<p>So the button is there but the <code>clicked()</code> connection is not working?  Maybe this isn’t it but your code says <code>onDummy</code> but in your message you say <code>on_dummy</code> which would not work.  One thing we don’t typically do but should is check the return value of the call to <code>connect()</code>.  It returns a boolean you can test to see if the connection worked.</p>

---

## Post #4 by @tueboesen (2024-03-04 14:54 UTC)

<p>This is embarrassing to admit, but that was indeed the problem… Thank you so much.<br>
And sorry for asking such a dumb question…</p>

---
