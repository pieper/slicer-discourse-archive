# Volumes module:  allow user to define their own preset Display configuration(s)

**Topic ID**: 20235
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/volumes-module-allow-user-to-define-their-own-preset-display-configuration-s/20235

---

## Post #1 by @DIV (2021-10-19 11:49 UTC)

<p>Currently in the Volumes module there are seven preset Display configurations:  <strong>CT-bone</strong>, <strong>CT-air</strong>, …, <strong>DTI</strong>.  It would be nice to allow users to define their own preset Display configuration(s).</p>
<p>I independently figured out a way to do this ‘manually’ for the Volume Rendering presets (cf. <a href="https://discourse.slicer.org/t/create-volume-rendering-presets/16339" class="inline-onebox">Create volume rendering presets</a>) — although I couldn’t find a convenient way to create relevant thumbnails for those user-defined presets.</p>

---

## Post #2 by @lassoan (2021-10-20 02:58 UTC)

<p>See how to do this in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#register-custom-volume-rendering-presets">documentation</a> and complete example of how you can do it in an extension in SlicerHeart:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerHeart/SlicerHeart/blob/1db36272742111a0fc3513a3a2a66cea38f68060/ValveAnnulusAnalysis/HeartValveLib/HeartValves.py#L329-L353">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/1db36272742111a0fc3513a3a2a66cea38f68060/ValveAnnulusAnalysis/HeartValveLib/HeartValves.py#L329-L353" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/1db36272742111a0fc3513a3a2a66cea38f68060/ValveAnnulusAnalysis/HeartValveLib/HeartValves.py#L329-L353" target="_blank" rel="noopener">SlicerHeart/SlicerHeart/blob/1db36272742111a0fc3513a3a2a66cea38f68060/ValveAnnulusAnalysis/HeartValveLib/HeartValves.py#L329-L353</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="329" style="counter-reset: li-counter 328 ;">
          <li>def registerCustomVrPresets(usPresetsScenePath):</li>
          <li>  """</li>
          <li>  Set volume rendering presets from Resources/VrPresets/US-VrPresets.mrml</li>
          <li>  """</li>
          <li>  import os</li>
          <li>
          </li>
<li>  if not os.path.isfile(usPresetsScenePath):</li>
          <li>    logging.warning('Volume rendering presets are not found at {0}'.format(usPresetsScenePath))</li>
          <li>    return</li>
          <li>
          </li>
<li>  # Read scene</li>
          <li>  usPresetsScene = slicer.vtkMRMLScene()</li>
          <li>  vrPropNode = slicer.vtkMRMLVolumePropertyNode()</li>
          <li>  usPresetsScene.RegisterNodeClass(vrPropNode)</li>
          <li>  usPresetsScene.SetURL(usPresetsScenePath)</li>
          <li>  usPresetsScene.Connect()</li>
          <li>
          </li>
<li>  # Add presets to volume rendering logic</li>
          <li>  vrLogic = slicer.modules.volumerendering.logic()</li>
          <li>  presetsScene = vrLogic.GetPresetsScene()</li>
      </ol>
    </code>
  </pre>

  This file has been truncated. <a href="https://github.com/SlicerHeart/SlicerHeart/blob/1db36272742111a0fc3513a3a2a66cea38f68060/ValveAnnulusAnalysis/HeartValveLib/HeartValves.py#L329-L353" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
