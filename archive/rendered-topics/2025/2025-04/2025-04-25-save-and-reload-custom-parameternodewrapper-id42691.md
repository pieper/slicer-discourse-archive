---
topic_id: 42691
title: "Save And Reload Custom Parameternodewrapper"
date: 2025-04-25
url: https://discourse.slicer.org/t/42691
---

# save and reload custom parameterNodeWrapper 

**Topic ID**: 42691
**Date**: 2025-04-25
**URL**: https://discourse.slicer.org/t/save-and-reload-custom-parameternodewrapper/42691

---

## Post #1 by @ipostuma (2025-04-25 16:19 UTC)

<p>Hi,</p>
<p>I probably have a silly question, but I didn’t manage to find an answer in the forum. I am trying to write a custom module to manage a treatment planning simulation. Part of this module consist in associating segmented volumes to a material. I have now a working QT widget where the user can add this information and the data is managed within the python script with:</p>
<pre><code class="lang-auto">@parameterPack
class MaskParameters:
    node: vtkMRMLScalarVolumeNode
    material: str

@parameterNodeWrapper
class GenerateInputParameterNode:

    CT: MaskParameters
    GTV: MaskParameters
    OAR: list[MaskParameters]
    Other: list[MaskParameters]
    AddVolume: vtkMRMLScalarVolumeNode
</code></pre>
<p>I would like to save the user generated data with the scene or medical record bundle. Is this possible ? Is there an example I could use as a guideline ?</p>
<p>thanks in advance !</p>

---

## Post #2 by @lassoan (2025-04-25 16:19 UTC)

<p>Parameter nodes are saved into the scene (in the .mrml file).</p>

---

## Post #3 by @ipostuma (2025-04-28 16:54 UTC)

<p>Hi, yes it was indeed a silly question.</p>
<p>My problem was that I didn’t update the GUI after the user loaded the saved scene. That said, things are now working as planned.</p>
<p>For future reference, I managed to understand my problem by printing the content of the _parameterNode once the scene is uploaded:</p>
<pre><code class="lang-auto">for attr, value in vars(self._parameterNode).items():  # or obj.__dict__.items()
            print(f"{attr} = {value}")
</code></pre>

---
