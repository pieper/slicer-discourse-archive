# Change display default settings to abdominal window

**Topic ID**: 26048
**Date**: 2022-11-03
**URL**: https://discourse.slicer.org/t/change-display-default-settings-to-abdominal-window/26048

---

## Post #1 by @jawbra (2022-11-03 10:32 UTC)

<p>Hey there,</p>
<p>I am wondering if there is a possibility to change the settings for imported DICOMS to be displayed in the soft tissue/abdomen window by default.  I will be doing a lot of annotations on the abdominal region and a default window of settings W:400 L:-150 would be perfect, saving the time of changing the window for every single study.</p>
<p>Any help is much appreciated, thanks in advance.</p>

---

## Post #2 by @chir.set (2022-11-03 11:22 UTC)

<p>I’m using this in .slicerrc.py :</p>
<pre><code class="lang-auto">def setPreferredScalarVolumeWindowLevel(inputVolume):
    if inputVolume is None or inputVolume.GetClassName() != "vtkMRMLScalarVolumeNode":
        return
    # https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository
    displayNode = inputVolume.GetDisplayNode()
    displayNode.AutoWindowLevelOff()
    # CT-Bones
    displayNode.SetWindow(1000)
    displayNode.SetLevel(400)
</code></pre>
<p>You may adapt it and map it to a keyboard shortcut, or add an observer to the scene on its ‘onNodeAdded’ event.</p>

---

## Post #3 by @jawbra (2022-11-04 09:51 UTC)

<p>Thank you, this worked for me!</p>

---
