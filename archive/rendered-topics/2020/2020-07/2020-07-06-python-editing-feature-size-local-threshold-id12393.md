---
topic_id: 12393
title: "Python Editing Feature Size Local Threshold"
date: 2020-07-06
url: https://discourse.slicer.org/t/12393
---

# Python - Editing Feature Size Local Threshold

**Topic ID**: 12393
**Date**: 2020-07-06
**URL**: https://discourse.slicer.org/t/python-editing-feature-size-local-threshold/12393

---

## Post #1 by @vertebra (2020-07-06 13:15 UTC)

<p>In the local threshold code on GitHub, there is a function updateMRMLfromGUI:</p>
<p>def updateMRMLFromGUI(self):<br>
SegmentEditorThresholdEffect.updateMRMLFromGUI(self)</p>
<pre><code>minimumDiameterMm = self.minimumDiameterSpinBox.value
self.scriptedEffect.setParameter(MINIMUM_DIAMETER_MM_PARAMETER_NAME, minimumDiameterMm)

featureSizeMm = self.featureSizeSpinBox.value
self.scriptedEffect.setParameter(FEATURE_SIZE_MM_PARAMETER_NAME, featureSizeMm)

segmentationAlgorithm = self.segmentationAlgorithmSelector.currentText
self.scriptedEffect.setParameter(SEGMENTATION_ALGORITHM_PARAMETER_NAME, segmentationAlgorithm)
</code></pre>
<p>How would I edit this code to set the feature size to 6.000 mm? Do I just replace featureSizeMm with 6?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-07-06 13:33 UTC)

<p>You don’t need to change the source code of a Segment Editor effect if you just want to change effect parameters from a Python script. Instead, you simply call <code>effect.setParameter</code> method from outside. See complete examples in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---

## Post #3 by @vertebra (2020-07-06 13:37 UTC)

<p>So for local threshold effect, I would type in:<br>
localThresholdEffect.setFeatureSize(6)<br>
localThresholdEffect.setMinimumThreshold(250)<br>
localThresholdEffect.setMaximumThreshold(1000)</p>
<p>Our code just takes in a point on a vertebra and runs local threshold from that point. We have already coded the taking in a point.</p>

---

## Post #4 by @vertebrae (2020-07-06 15:25 UTC)

<p>Do we also need to include values for BACKGROUND_VALUE and LABEL_VALUE in the apply function?</p>

---

## Post #5 by @vertebrae (2020-07-06 15:51 UTC)

<p>Also SELECTED_ISLAND_VALUE and OUTSIDE_THRESHOLD_VALUE</p>

---

## Post #6 by @lassoan (2020-07-06 16:27 UTC)

<aside class="quote no-group" data-username="vertebrae" data-post="4" data-topic="12393" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/dec6dc/48.png" class="avatar"> vertebrae:</div>
<blockquote>
<p>Do we also need to include values for BACKGROUND_VALUE and LABEL_VALUE in the apply function?</p>
</blockquote>
</aside>
<p>You don’t need to do anything with BACKGROUND_VALUE, LABEL_VALUE, etc. - they are internal constants.</p>
<p>The <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/5b46d10fd6ca81e9b714fc92fd05f621bc041adf/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py#L336">only parameter for <code>apply</code> method is <code>ijkPoints</code></a> and the method uses scripted effect parameters:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/5b46d10fd6ca81e9b714fc92fd05f621bc041adf/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py#L173-L179">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/5b46d10fd6ca81e9b714fc92fd05f621bc041adf/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py#L173-L179" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/5b46d10fd6ca81e9b714fc92fd05f621bc041adf/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py#L173-L179" target="_blank" rel="noopener">lassoan/SlicerSegmentEditorExtraEffects/blob/5b46d10fd6ca81e9b714fc92fd05f621bc041adf/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py#L173-L179</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="173" style="counter-reset: li-counter 172 ;">
          <li>def setMRMLDefaults(self):</li>
          <li>  self.scriptedEffect.setParameterDefault(MINIMUM_DIAMETER_MM_PARAMETER_NAME, 3)</li>
          <li>  self.scriptedEffect.setParameterDefault(FEATURE_SIZE_MM_PARAMETER_NAME, 3)</li>
          <li>  self.scriptedEffect.setParameterDefault(SEGMENTATION_ALGORITHM_PARAMETER_NAME, SEGMENTATION_ALGORITHM_GROWCUT)</li>
          <li>  if slicer.app.majorVersion &gt;= 4 and slicer.app.minorVersion &gt;= 11:</li>
          <li>    self.scriptedEffect.setParameterDefault(HISTOGRAM_BRUSH_TYPE_PARAMETER_NAME, HISTOGRAM_BRUSH_TYPE_DRAW)</li>
          <li>  SegmentEditorThresholdEffect.setMRMLDefaults(self)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @vertebrae (2020-07-06 17:38 UTC)

<p>Thank you very much!</p>

---

## Post #8 by @vertebra (2020-07-06 18:30 UTC)

<p>Hello Andras!</p>
<p>We are in the testing stage of the entire code now. To confirm, we are running it line by line in the python interactor. The GitHub code uses an apply function(which appears to be synonymous with run the algorithm). The parameters for apply are self and ijkPoints.</p>
<p>Whenever we run the apply function:’</p>
<p>apply(ijkPoints)</p>
<p>It says apply() missing 1 required positional argument: ‘ijkPoints’</p>
<p>We have defined it already, so what do we do?</p>
<p>Thanks!</p>

---

## Post #9 by @lassoan (2020-07-06 18:37 UTC)

<p>You need to call apply like this: <code>effect.apply(ijkPoints)</code></p>

---

## Post #10 by @vertebra (2020-07-06 18:38 UTC)

<p>It says effect is not defined when I attempted this…</p>

---

## Post #11 by @vertebra (2020-07-06 18:42 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/873038c511c26b0591dacfb40e6744d16c58bf21.png" alt="Screen Shot 2020-07-06 at 2.42.25 PM" data-base62-sha1="jhVLVYXsVZ1u8sv5JAFxyg9L7ZD" width="549" height="84"></p>

---

## Post #12 by @lassoan (2020-07-06 18:49 UTC)

<p>You need to set an active effect first.</p>

---

## Post #14 by @lassoan (2020-07-06 19:00 UTC)

<p>Call <code>setActiveEffectByName</code>, as it is done in all the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">examples</a>.</p>

---

## Post #15 by @vertebra (2020-07-06 19:15 UTC)

<p>We set an active effect by name, but once again receive another error. It says:</p>
<p>Attribute Error: qSlicerSegmentEditorScriptEffect has no attribute named ‘apply’</p>
<p>This was after running effect.apply(ijkPoints)</p>
<p>We defined the function apply, what should we do?</p>

---

## Post #16 by @lassoan (2020-07-06 19:41 UTC)

<p>Indeed, in case of this effect, which is derived from  C++ effect, the syntax is slightly different, as <code>effect</code> refers to the C++ effect, and you need to call <code>effect.self()</code> to access the methods added in Python. So, a complete example:</p>
<pre><code class="lang-python">segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
segmentEditorWidget.setActiveEffectByName("Local Threshold")
effect = segmentEditorWidget.activeEffect()
ijkPoints = vtk.vtkPoints()
ijkPoints.InsertNextPoint(127,102,80)
effect.self().apply(ijkPoints)
</code></pre>

---

## Post #17 by @lassoan (2020-07-07 20:01 UTC)

<p>A post was merged into an existing topic: <a href="/t/python-module-logic-class/12415/8">Python Module Logic Class</a></p>

---

## Post #18 by @vertebra (2020-07-07 19:48 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I am sorry to bother you again. I copied all of the functions from the Local Threshold into the Python Interactor and created a segmentationNode around a pre-determined point. Then, I run this code:</p>
<p>segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor<br>
segmentEditorWidget.setActiveEffectByName(“Local Threshold”)<br>
effect.setParameter(“Minimum Threshold”, 265)<br>
effect.setParameter(“Maximum Threshold”, 1009)<br>
effect = segmentEditorWidget.activeEffect()<br>
ijkPoints = vtk.vtkPoints()<br>
ijkPoints.InsertNextPoint(world[0], world[1], world[2]) #<span class="hashtag">#world</span> has the coordinates of the point<br>
effect.self().apply(ijkPoints)</p>
<p>This gives me an error saying that “None Type” has no attribute self. I feel like we have the necessary elements to the code(many thanks to your GitHub resources), but I just cannot get the code to actually work when run. Thank you</p>

---

## Post #19 by @lassoan (2020-07-07 19:59 UTC)

<p>You can only select an effect if you selected a master volume and created a segment. See the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">examples</a>.</p>
<p>Also note that the order of operations need to be fixed (<code>effect = </code> comes first) and that <code>world</code> coordinate is physical (RAS) coordinate and not <code>IJK</code>. You need to convert to <code>RAS</code> to <code>IJK</code> before inserting the point coordinates into <code>ijkPoints</code>.</p>

---

## Post #20 by @vertebra (2020-07-08 13:08 UTC)

<p>Thank you! I found out how to convert the RAS coordinates to IJK coordinates, but we are still having trouble with the effect line:</p>
<p>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()<br>
slicer.mrmlScene.AddNode(segmentEditorNode)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setSegmentationNode(segmentationNode)<br>
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)</p>
<p>segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor<br>
<strong>segmentEditorWidget.setActiveEffectByName(“Local Threshold”)</strong><br>
effect = segmentEditorWidget.activeEffect()<br>
effect.self().apply(fidIJK)</p>
<p>The setActiveEffectByName line(and lines where we setParameters after it) still have errors regarding attributes and identifiers. Do you have any idea why <a class="mention" href="/u/lassoan">@lassoan</a>?</p>

---

## Post #21 by @lassoan (2020-07-08 13:11 UTC)

<p>Can you send the link to your module’s source code?</p>

---

## Post #22 by @vertebra (2020-07-08 13:23 UTC)

<p>This is the link to everything:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/kbehlmirusmed/VertebraSeg" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/67699725?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/kbehlmirusmed/VertebraSeg" target="_blank" rel="nofollow noopener">kbehlmirusmed/VertebraSeg</a></h3>

<p>Contribute to kbehlmirusmed/VertebraSeg development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Thank you so much!</p>

---

## Post #23 by @vertebra (2020-07-08 14:55 UTC)

<p>We figured it out <a class="mention" href="/u/lassoan">@lassoan</a>!</p>

---

## Post #24 by @vertebra (2020-07-08 15:21 UTC)

<p>When we use effect.setParameter(“Minimum Threshold”, 265) and then:</p>
<p>print(slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLSegmentEditorNode”))</p>
<p>It says that the parameter is still set at the default of 115 (Local Threshold.MinimumThreshold:115)</p>
<p>Are we missing a line of code <a class="mention" href="/u/lassoan">@lassoan</a>?</p>

---

## Post #25 by @vertebrae (2020-07-08 17:01 UTC)

<p>We have figured it out. Thanks!</p>

---

## Post #26 by @lassoan (2020-07-09 00:59 UTC)

<p>Please always write here what was the solution because it will help others who will find this page when they have a similar question.</p>

---

## Post #27 by @vertebra (2020-07-09 12:30 UTC)

<p>The solution is you write <code>effect.setParameter("MinimumThreshold", "265")</code> - no SPACE</p>

---
