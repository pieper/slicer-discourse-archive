# How to use Segment Editor effects from python script?

**Topic ID**: 20815
**Date**: 2021-11-28
**URL**: https://discourse.slicer.org/t/how-to-use-segment-editor-effects-from-python-script/20815

---

## Post #1 by @utkgl (2021-11-28 12:54 UTC)

<p>Hi!<br>
I am trying to automatize some series of lung segmentation steps on 3D Slicer with using python scripts.<br>
Currently I can resample my file using;</p>
<pre><code class="lang-auto">volumeNode = slicer.util.loadVolume(file)
emptyVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", "output volume")
slicer.util.mainWindow().moduleSelector().selectModule('ResampleScalarVolume')
              
params = {}
params["InputVolume"] = volumeNode
params["OutputVolume"] = emptyVolumeNode
params["outputPixelSpacing"] = (2,2,2)
              
resampleModule = slicer.modules.resamplescalarvolume
cliNode = slicer.cli.runSync(resampleModule,None,params)
</code></pre>
<p>Or add empty segmentations using;</p>
<pre><code class="lang-auto">slicer.util.mainWindow().moduleSelector().selectModule('Segmentations')
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes()
segmentationNode. SetReferenceImageGeometryParameterFromVolumeNode(emptyVolumeNode)
leftSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("left lung")
rightSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("right lung")
tracheaSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("trachea")	
</code></pre>
<p>Also in Segment Editor, the “Smoothing” section I can use the smoothing tool like this;</p>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Smoothing") 
effect = segmentEditorWidget.activeEffect() 
effect.setParameter("SmoothingMethod", "CLOSING") 
effect.setParameter("KernelSizeMm", 12) 
effect.self().onApply()

</code></pre>
<p>However I am struggling to use “Threshold” and “Grow from seeds” parts. In Threshold part I want it to click the “Use for masking” button and in the Grow from seeds part I want it to first click “Initialize” then “Apply” button.</p>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Threshold")
 effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","-1024")
effect.setParameter("MaximumThreshold","-500")
effect.self().onApply()
</code></pre>
<p>For example this code sets correct threshold values but clicks “apply” instead of “use for masking” button.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d782b8be473b062afd86b19f82c510f20787542.jpeg" data-download-href="/uploads/short-url/mt2qq0cQNAs2pciDt8gZ7KiARNg.jpeg?dl=1" title="grow from seeds" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d782b8be473b062afd86b19f82c510f20787542_2_690x330.jpeg" alt="grow from seeds" data-base62-sha1="mt2qq0cQNAs2pciDt8gZ7KiARNg" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d782b8be473b062afd86b19f82c510f20787542_2_690x330.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d782b8be473b062afd86b19f82c510f20787542_2_1035x495.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d782b8be473b062afd86b19f82c510f20787542_2_1380x660.jpeg 2x" data-dominant-color="4D4C53"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grow from seeds</span><span class="informations">1779×851 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7675e36d7ca93b0ea9aa0ed2b77062a17cee6008.png" data-download-href="/uploads/short-url/gTWUNXrTCw5UtHsFq7H0lXW1TzW.png?dl=1" title="threshold" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7675e36d7ca93b0ea9aa0ed2b77062a17cee6008_2_477x500.png" alt="threshold" data-base62-sha1="gTWUNXrTCw5UtHsFq7H0lXW1TzW" width="477" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7675e36d7ca93b0ea9aa0ed2b77062a17cee6008_2_477x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7675e36d7ca93b0ea9aa0ed2b77062a17cee6008.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7675e36d7ca93b0ea9aa0ed2b77062a17cee6008.png 2x" data-dominant-color="E5E4E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">threshold</span><span class="informations">520×544 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I researched the script repository but wasn’t able to find anything. I would appreciate any help. Thanks!</p>
<p>Yusuf Utku Gül</p>

---

## Post #2 by @chir.set (2021-11-28 13:34 UTC)

<p>If UI simulation is an acceptable solution for you, you can get some insight <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/6aeec24352244ed2bd9313605c981f8bff1a7215/FiducialCenterlineExtraction/FiducialCenterlineExtraction.py#L736" rel="noopener nofollow ugc">here</a>. Basically, you can dig through the effect UI and locate the widgets unexposed by the effect’s API, and interact next by the widget’s API.</p>

---

## Post #3 by @utkgl (2021-11-28 20:20 UTC)

<p>Thank you for the response, I am looking into it right now.</p>

---

## Post #4 by @qiqi5210 (2021-11-29 00:51 UTC)

<p>The initialization button for seed growth can be set as follows:</p>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Grow form seeds")
effect = segmentEditorWidget.activeEffect()
effect.self().onPreview()
</code></pre>

---

## Post #5 by @lassoan (2021-11-30 00:10 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="2" data-topic="20815">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>If UI simulation is an acceptable solution for you</p>
</blockquote>
</aside>
<p>Simulating button clicks would make the code very fragile. All the necessary API should be available to run effects without simulating GUI events, but if it turns out that anything is missing then we can expose more functions.</p>
<p>There are full examples of how to perform Thresholding and Grow from seeds from Python scripts in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#how-to-run-segment-editor-effects-from-a-script">script repository</a>.</p>
<p>There are also some nice modules that do this, using a simple, wizard-like interface, for example the LungCTAnalyzer extension by <a class="mention" href="/u/rbumm">@rbumm</a>, which can automatically segment lungs and trachea from a few clicks that the user is guided through:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="fpLxm7uAvZQ" data-video-title="Automated lung CT segmentation and analysis for COVID-19 assessment" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=fpLxm7uAvZQ" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/fpLxm7uAvZQ/maxresdefault.jpg" title="Automated lung CT segmentation and analysis for COVID-19 assessment" width="" height="">
  </a>
</div>

<p>Source code: <a href="https://github.com/rbumm/SlicerLungCTAnalyzer" class="inline-onebox">GitHub - rbumm/SlicerLungCTAnalyzer: This is a 3D Slicer extension for segmentation and spatial reconstruction of infiltrated, collapsed, and emphysematous areas in lung CT.</a></p>

---
