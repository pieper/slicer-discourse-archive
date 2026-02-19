---
topic_id: 25127
title: "How To Load Custom Presets When Slicer Starts Up"
date: 2022-09-07
url: https://discourse.slicer.org/t/25127
---

# How to load custom presets when Slicer starts up

**Topic ID**: 25127
**Date**: 2022-09-07
**URL**: https://discourse.slicer.org/t/how-to-load-custom-presets-when-slicer-starts-up/25127

---

## Post #1 by @user4 (2022-09-07 01:33 UTC)

<p>Hi,all.<br>
I want to remove the CT presets and add my own presets in volume rendering module when Slicer starts up.I have seen some related topics and currently my idea is divided into two steps.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45a232367f9c74b3e4130a850ba8a3bd90b39323.jpeg" data-download-href="/uploads/short-url/9W0rQkoi0D3EMnxLj7eB49kzQwb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45a232367f9c74b3e4130a850ba8a3bd90b39323_2_690x320.jpeg" alt="image" data-base62-sha1="9W0rQkoi0D3EMnxLj7eB49kzQwb" width="690" height="320" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45a232367f9c74b3e4130a850ba8a3bd90b39323_2_690x320.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45a232367f9c74b3e4130a850ba8a3bd90b39323.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45a232367f9c74b3e4130a850ba8a3bd90b39323.jpeg 2x" data-dominant-color="DDD8DA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1029×478 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol>
<li>Create my own <em>presets.mrml</em> file as follows:</li>
</ol>
<pre><code class="lang-auto">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;MRML version="Slicer4.4.0"&gt;
  &lt;VolumeProperty id="vtkMRMLVolumeProperty1" name="MyPreset1"     references="IconVolume:vtkMRMLVectorVolumeNode1;" interpolation="1" shade="1" diffuse="0.66" ambient="0.1" specular="0.62" specularPower="14" scalarOpacity="10 -3.52844023704529 0 56.7852325439453 0 79.2550277709961 0.428571432828903 415.119384765625 1 641 1" gradientOpacity="4 0 1 160.25 1" colorTransfer="16 0 0 0 0 98.7223 0.196078431372549 0.945098039215686 0.956862745098039 412.406 0 0.592157 0.807843 641 1 1 1" /&gt;
  &lt;!-- &lt;VectorVolume id="vtkMRMLVectorVolumeNode1" references="storage:vtkMRMLVolumeArchetypeStorageNode1;" /&gt; --&gt;
  &lt;!-- &lt;VolumeArchetypeStorage id="vtkMRMLVolumeArchetypeStorageNode1" fileName="MyPreset1.png"  fileListMember0="MyPreset1.png" /&gt; --&gt;

  &lt;VolumeProperty id="vtkMRMLVolumeProperty2" name="MyPreset2"     references="IconVolume:vtkMRMLVectorVolumeNode2;" interpolation="1" shade="1" diffuse="0.66" ambient="0.1" specular="0.62" specularPower="14" scalarOpacity="10 -3.52844023704529 0 56.7852325439453 0 79.2550277709961 0.428571432828903 415.119384765625 1 641 1" gradientOpacity="4 0 1 160.25 1" colorTransfer="16 0 0 0 0 98.7223 0.196078431372549 0.945098039215686 0.956862745098039 412.406 0 0.592157 0.807843 641 1 1 1" /&gt;
  &lt;!-- &lt;VectorVolume id="vtkMRMLVectorVolumeNode2" references="storage:vtkMRMLVolumeArchetypeStorageNode2;" /&gt; --&gt;
  &lt;!-- &lt;VolumeArchetypeStorage id="vtkMRMLVolumeArchetypeStorageNode2" fileName="MyPreset2.png"  fileListMember0="MyPreset2.png" /&gt; --&gt;
&lt;/MRML&gt;
</code></pre>
<ol start="2">
<li>Open the Slicer App,run the code below:</li>
</ol>
<pre><code class="lang-auto">presetsScenePath = ".\presets\MyPresets.mrml"

# Read presets scene
customPresetsScene = slicer.vtkMRMLScene()
vrPropNode = slicer.vtkMRMLVolumePropertyNode()
customPresetsScene.RegisterNodeClass(vrPropNode)
customPresetsScene.SetURL(presetsScenePath)
customPresetsScene.Connect()

# Add presets to volume rendering logic
vrLogic = slicer.modules.volumerendering.logic()
presetsScene = vrLogic.GetPresetsScene()
vrNodes = customPresetsScene.GetNodesByClass("vtkMRMLVolumePropertyNode")
vrNodes.UnRegister(None)
for itemNum in range(vrNodes.GetNumberOfItems()):
    print('test')
    node = vrNodes.GetItemAsObject(itemNum)
    vrLogic.AddPreset(node)
</code></pre>
<p>So right now I can see my own presets in rendering module,however is there a way to add my presets when Slicer starts up and I don’t need to run any code?I think maybe I should put this snippet into some main functions called by Slicer.<br>
Thank you in advance for your help!</p>

---

## Post #2 by @Sunderlandkyl (2022-09-07 14:58 UTC)

<p>You can edit your application startup file (“.slicerrc.py”) which is run every time Slicer starts, and add the python code to that file:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file</a></p>

---
