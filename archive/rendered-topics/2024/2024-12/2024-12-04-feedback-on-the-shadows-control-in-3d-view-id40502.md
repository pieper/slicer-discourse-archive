# Feedback on the shadows control in 3D view

**Topic ID**: 40502
**Date**: 2024-12-04
**URL**: https://discourse.slicer.org/t/feedback-on-the-shadows-control-in-3d-view/40502

---

## Post #1 by @muratmaga (2024-12-04 06:22 UTC)

<p>During our workshop, a common request/consensus has emerged. The newly introduced shadows features in 3D viewer is nice. However, it does need a few additional features to be more functional.</p>
<ol>
<li>A way to  reset the options. Currently when you create a really poor shadow settings combinations, you cannot recover from it without resetting the scene. Or you have to turn off the shadows. There should be a button that says “Reset all settings”. Or something like that</li>
<li>As you are sliding one option, slight mouse movement activate the next option (for example when you are sliding on the intensity scale, you suddenly find yourselv sliding along intensity shift).</li>
<li>The names of the settings does not convey any information about what’s being changed. (E.g., what is size scale? Size of what?). Either we have to provide some documentation somewhere, or make the options more interpretable. Without these, the only option to experiment with those settings and without being able to recover from poor combinations (issue <span class="hashtag-raw">#1</span>), people give up after a while. No one wants to keep reloading data to discover the features.</li>
</ol>

---

## Post #2 by @mau_igna_06 (2024-12-04 19:48 UTC)

<p>I have set a combobox on BoneReconstructionPlanner to change lighting as the Lights modules of Sandbox extension does, it has only 4 options, so it’s easy to use:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/d9c0521f3dfb830478136b37c2fe2fb5e3ea3023/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L926-L944">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/d9c0521f3dfb830478136b37c2fe2fb5e3ea3023/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L926-L944" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/d9c0521f3dfb830478136b37c2fe2fb5e3ea3023/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L926-L944" target="_blank" rel="noopener nofollow ugc">SlicerIGT/SlicerBoneReconstructionPlanner/blob/d9c0521f3dfb830478136b37c2fe2fb5e3ea3023/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L926-L944</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="926" style="counter-reset: li-counter 925 ;">
          <li>def onLightsRenderingComboBox(self, text):
</li>
          <li>  lightsLogic = slicer.modules.lights.widgetRepresentation().self().logic
</li>
          <li>  viewNodesList = slicer.util.getNodesByClass("vtkMRMLViewNode")
</li>
          <li>  for viewNode in viewNodesList:
</li>
          <li>    lightsLogic.addManagedView(viewNode)
</li>
          <li>  if text == "Lamp":
</li>
          <li>    lightsLogic.setUseLightKit(False)
</li>
          <li>    lightsLogic.setSingleLightIntensity(1.0)
</li>
          <li>    lightsLogic.setUseSSAO(False)
</li>
          <li>  elif text == "Lamp and Shadows":
</li>
          <li>    lightsLogic.setUseLightKit(False)
</li>
          <li>    lightsLogic.setSingleLightIntensity(1.0)
</li>
          <li>    lightsLogic.setUseSSAO(True)
</li>
          <li>  elif text == "MultiLamp":
</li>
          <li>    lightsLogic.setUseLightKit(True)
</li>
          <li>    lightsLogic.setUseSSAO(False)
</li>
          <li>  elif text == "MultiLamp and Shadows":
</li>
          <li>    lightsLogic.setUseLightKit(True)
</li>
          <li>    lightsLogic.setUseSSAO(True)
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You should be able to copy-paste the function and use it (Sandbox extension needs to be installed)</p>
<p>HIH</p>

---
