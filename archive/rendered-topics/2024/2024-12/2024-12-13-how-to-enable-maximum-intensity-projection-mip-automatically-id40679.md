---
topic_id: 40679
title: "How To Enable Maximum Intensity Projection Mip Automatically"
date: 2024-12-13
url: https://discourse.slicer.org/t/40679
---

# How to Enable Maximum Intensity Projection (MIP) Automatically for MRML Presets?

**Topic ID**: 40679
**Date**: 2024-12-13
**URL**: https://discourse.slicer.org/t/how-to-enable-maximum-intensity-projection-mip-automatically-for-mrml-presets/40679

---

## Post #1 by @LounesAl (2024-12-13 12:10 UTC)

<p>Hello,</p>
<p>I have created custom volume rendering presets in an MRML file. Below is an example structure:</p>
<pre data-code-wrap="xml"><code class="lang-xml">&lt;MRML version="Slicer4.4.0"&gt;
  &lt;VolumeProperty id="vtkMRMLVolumeProperty1" name="MyPreset1" references="IconVolume:vtkMRMLVectorVolumeNode1;" interpolation="1" shade="1" diffuse="0.66" ambient="0.1" specular="0.62" specularPower="14" scalarOpacity="10 -3.52844023704529 0 56.7852325439453 0 79.2550277709961 0.428571432828903 415.119384765625 1 641 1" gradientOpacity="4 0 1 160.25 1" colorTransfer="16 0 0 0 0 98.7223 0.196078431372549 0.945098039215686 0.956862745098039 412.406 0 0.592157 0.807843 641 1 1 1" /&gt;
  &lt;VectorVolume id="vtkMRMLVectorVolumeNode1" references="storage:vtkMRMLVolumeArchetypeStorageNode1;" /&gt;
  &lt;VolumeArchetypeStorage id="vtkMRMLVolumeArchetypeStorageNode1" fileName="MyPreset1.png" fileListMember0="MyPreset1.png" /&gt;

  &lt;VolumeProperty id="vtkMRMLVolumeProperty2" name="MyPreset2" references="IconVolume:vtkMRMLVectorVolumeNode2;" interpolation="1" shade="1" diffuse="0.66" ambient="0.1" specular="0.62" specularPower="14" scalarOpacity="10 -3.52844023704529 0 56.7852325439453 0 79.2550277709961 0.428571432828903 415.119384765625 1 641 1" gradientOpacity="4 0 1 160.25 1" colorTransfer="16 0 0 0 0 98.7223 0.196078431372549 0.945098039215686 0.956862745098039 412.406 0 0.592157 0.807843 641 1 1 1" /&gt;
  &lt;VectorVolume id="vtkMRMLVectorVolumeNode2" references="storage:vtkMRMLVolumeArchetypeStorageNode2;" /&gt;
  &lt;VolumeArchetypeStorage id="vtkMRMLVolumeArchetypeStorageNode2" fileName="MyPreset2.png" fileListMember0="MyPreset2.png" /&gt;
&lt;/MRML&gt;
</code></pre>
<p>I would like to automatically enable <strong>Maximum Intensity Projection (MIP)</strong> when switching to the <code>MyPreset2</code> preset.</p>
<p>Do I need to add a <code>ViewNode</code>, a <code>VolumeRenderingDisplayNode</code>, or some other configuration in the MRML file? If not, what is the best way to associate MIP with specific presets?</p>
<p>Thank you for your help!</p>

---

## Post #2 by @lassoan (2024-12-13 15:46 UTC)

<p>MIP mode has to be enabled on the view node - see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-using-maximum-intensity-projection">full example in the script repository</a>.</p>
<p>It would make more sense to include raycast technique in the volume rendering preset. I’ve added an <a href="https://github.com/Slicer/Slicer/issues/8095">issue to track this task</a>. But to reduce API churn, we probably will not change this until we need to make other significant changes/improvements to rendering presets. A grant proposal was submitted for improving volume rendering presets, so if it is successful (or if other funding sources come in) then this will all be implemented.</p>

---

## Post #3 by @LounesAl (2024-12-13 17:35 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for the clarification and for adding this to the issue tracker.</p>
<p>I plan to implement a workaround using a Python function <code>onPresetChanged</code> in my module within my extension. The function would trigger when the preset changes, allowing me to manually set the raycast technique for specific presets. For example:</p>
<pre data-code-wrap="python"><code class="lang-python">def onPresetChanged(presetName):
    if presetName == "MyPreset2":
        # Switch views to MIP mode
        for viewNode in slicer.util.getNodesByClass("vtkMRMLViewNode"):
            viewNode.SetRaycastTechnique(slicer.vtkMRMLViewNode.MaximumIntensityProjection)
</code></pre>
<p>Is there a way to integrate such a function so that it is automatically triggered when a preset is changed?</p>

---

## Post #4 by @chir.set (2024-12-13 19:00 UTC)

<aside class="quote no-group" data-username="LounesAl" data-post="3" data-topic="40679">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lounesal/48/78861_2.png" class="avatar"> LounesAl:</div>
<blockquote>
<p>when a preset is changed</p>
</blockquote>
</aside>
<p>May be there’s a cleaner way to do this, but the following should work however:</p>
<pre><code class="lang-auto">presetComboBox = slicer.util.mainWindow().findChild(slicer.qSlicerVolumeRenderingPresetComboBox, "PresetComboBox")
presetComboBox.connect("currentNodeIDChanged(QString)", yourFunction)
</code></pre>
<p>‘<code>yourFunction</code>’ will receive a preset ID, which you can follow to get the name.</p>
<p><em>BTW, I just noticed that the preset combobox does not select the chosen preset actually; that’s on preview in Linux. It is indeed selected in 5.6.</em></p>

---

## Post #5 by @LounesAl (2024-12-16 16:45 UTC)

<p>Thank you for your suggestion! Unfortunately, this line of code</p>
<pre data-code-wrap="python"><code class="lang-python">presetComboBox = slicer.util.mainWindow().findChild(slicer.qSlicerVolumeRenderingPresetComboBox, "PresetComboBox")
</code></pre>
<p>is not working in my case. The <code>presetComboBox</code> is returning <code>None</code>, so it seems the <code>PresetComboBox</code> is either not found or not available in my setup.</p>
<p>I’ve tried listing all child objects under <code>slicer.util.mainWindow()</code> but couldn’t locate it there. Could it be named differently or located somewhere else, like within the Volume Rendering module widget? Any additional pointers would be appreciated!</p>

---

## Post #6 by @chir.set (2024-12-16 17:55 UTC)

<pre><code class="lang-auto">w = getModuleWidget("VolumeRendering")
presetComboBox = w.findChild(slicer.qSlicerVolumeRenderingPresetComboBox, "PresetComboBox")
</code></pre>
<p>should work. It’s quick and dirty, but does help.</p>
<p>It’s likely that the previous code needs the VolumeRendering module to have been shown once.</p>

---

## Post #7 by @LounesAl (2024-12-17 10:43 UTC)

<p>Thank you for the help! I managed to get it working with this approach:</p>
<pre data-code-wrap="python"><code class="lang-python">def OnPresetChanged(ID: str):
    """Automatically switch to MIP when a preset is changed."""
    vrLogic = slicer.modules.volumerendering.logic()
    presetsScene = vrLogic.GetPresetsScene()
    vrNodes = presetsScene.GetNodesByClass("vtkMRMLVolumePropertyNode")
    for i in range(vrNodes.GetNumberOfItems()):
        node = vrNodes.GetItemAsObject(i)
        if node.GetID() == ID:
            raycastTechnique = "Max" if node.GetName().lower().endswith("max") else "Composite"
            SetRaycastTechnique(raycastTechnique)
            break

w = slicer.util.getModuleWidget("VolumeRendering")
presetComboBox = w.findChild(slicer.qSlicerVolumeRenderingPresetComboBox, "PresetComboBox")
presetComboBox.connect("currentNodeIDChanged(QString)", OnPresetChanged)
</code></pre>
<p>I made sure that the presets I want to activate MIP for have “Max” at the end of their names. This works well, but I’m sure there’s a cleaner or more efficient way to achieve this. Let me know if you have any suggestions!</p>

---
