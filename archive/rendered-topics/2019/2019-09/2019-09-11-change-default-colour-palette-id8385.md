---
topic_id: 8385
title: "Change Default Colour Palette"
date: 2019-09-11
url: https://discourse.slicer.org/t/8385
---

# Change default colour palette

**Topic ID**: 8385
**Date**: 2019-09-11
**URL**: https://discourse.slicer.org/t/change-default-colour-palette/8385

---

## Post #1 by @Jonathan_Lesage (2019-09-11 16:17 UTC)

<p>Hi All,</p>
<p>I am hoping to change the default colourmap that is applied to all loaded volumes from Grey to a custom map I’ve added to the list by putting a file in the colors directory. Is this something simple to do? Alternatively, I would like to know how to run a script which automatically runs when a new volume is added.</p>
<p>Thanks,</p>
<ul>
<li>Jon</li>
</ul>

---

## Post #2 by @pieper (2019-09-11 19:20 UTC)

<p>You could do this yes.  You could observe the scene for new nodes and then change the volume’s display node.  Search these pages for <code>slicerrc.py</code>, <code>NodeAddedEvent</code>, and <code>DisplayNode</code> to get the idea.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository</a></p>

---

## Post #3 by @keri (2022-08-02 16:21 UTC)

<p>Since then did anything change? I mean is there a default diplay node (for volumes, for models) where I could simply change color node once and do not observe the scene?</p>

---

## Post #4 by @lassoan (2022-08-03 06:30 UTC)

<p>You can change the default color, color node, etc. in a display node and set in the scene as default node to make it the default for all newly loaded nodes.</p>
<p>For DICOM volumes, the default colormap may be overridden depending on the image modality:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/38e026f75f78320a2cb579b5fa96f0917ab4f02c/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L480-L485">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/38e026f75f78320a2cb579b5fa96f0917ab4f02c/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L480-L485" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/38e026f75f78320a2cb579b5fa96f0917ab4f02c/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L480-L485" target="_blank" rel="noopener">Slicer/Slicer/blob/38e026f75f78320a2cb579b5fa96f0917ab4f02c/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L480-L485</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="480" style="counter-reset: li-counter 479 ;">
          <li># initialize color lookup table</li>
          <li>modality = self.mapSOPClassUIDToModality(sopClassUID)</li>
          <li>if modality == "PT":</li>
          <li>    displayNode = volumeNode.GetDisplayNode()</li>
          <li>    if displayNode:</li>
          <li>        displayNode.SetAndObserveColorNodeID(slicer.modules.colors.logic().GetPETColorNodeID(slicer.vtkMRMLPETProceduralColorNode.PETheat))</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
