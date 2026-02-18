# Slicer Local Threshold Scripted Effect Error

**Topic ID**: 12463
**Date**: 2020-07-09
**URL**: https://discourse.slicer.org/t/slicer-local-threshold-scripted-effect-error/12463

---

## Post #1 by @vertebra (2020-07-09 16:48 UTC)

<p>When we run our code in the Python interactor, our code enters an infinite error sequence pointing to line 75 in SegmentEditorEffect.py</p>
<p>This line reads: r,g,b = segmentationNode.GetSegmentation().GetSegment(segmentID).GetColor()</p>
<p>The error says that segmentID is the issue</p>
<p>In our code, we create our segment:</p>
<p>segmentationNode.AddSegmentFromClosedSurfaceRepresentation(lumbarSeed.GetOutput(), “Lumbar-” + str(x+1), [random(), random(), random()], str(x+1))</p>
<p>Do you have any idea for the issue? What do we change to repair this bug? <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #2 by @Sunderlandkyl (2020-07-09 17:11 UTC)

<p>Did you call segmentEditorNode.SetSelectedSegmentID()?</p>
<p>If you can upload your code somewhere, I can take a look at the error.</p>

---

## Post #3 by @vertebra (2020-07-09 17:20 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>
<p>Thank you so much!</p>
<p>This is our code(we also have the local threshold functions, but the link is just the “run” code)</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/kbehlmirusmed/VertebraSeg/blob/master/VertebraSeg.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/kbehlmirusmed/VertebraSeg/blob/master/VertebraSeg.py" target="_blank" rel="nofollow noopener">kbehlmirusmed/VertebraSeg/blob/master/VertebraSeg.py</a></h4>
<pre><code class="lang-py">class VertebraSeg(SegmentEditorThresholdEffect):

  #Load master volume
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadCTACardio() ##slicer.mrmlScene

  delayDisplay("Please mark a point on each of the five lumbar")

  for x in range(2):
#x=0
  print('Next Point in Loop')
  print(x)
  fidList = slicer.util.getNode('F')    
  segmentationNode = slicer.vtkMRMLSegmentationNode()
  segmentationNode.SetName('VertebraL' + str(x+1))
  slicer.mrmlScene.AddNode(segmentationNode)
  segmentationNode.CreateDefaultDisplayNodes() # only needed for display
  segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
  fidRAS = [0,0,0]
  fidList.GetNthFiducialPosition(x, fidRAS)
</code></pre>

  This file has been truncated. <a href="https://github.com/kbehlmirusmed/VertebraSeg/blob/master/VertebraSeg.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>The print statements are just for cross referencing purposes</p>

---

## Post #4 by @Sunderlandkyl (2020-07-09 18:52 UTC)

<p>I’ve fixed the bug that was causing the error message <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/commit/584e02c9fcdc62285ff2e2332bd7308a6b7ceeeb" rel="nofollow noopener">in this commit</a>.</p>
<p>You should still select the segment that you would like to edit by calling segmentationNode.SetSelectedSegmentID(segmentID) to ensure that the correct segment is modified. This should also have the side effect of preventing the errors.</p>

---

## Post #5 by @vertebra (2020-07-09 19:32 UTC)

<p>Thank you so much Kyle!</p>
<p>One last question: when we run it, for some reason even though we set the segmentationNode, it does not switch to the newly created segmentationNode on Slicer. The segment editor says that we are still in the original Segmentation(always called “Segmentation”). Do you know why it wouldn’t switch to VertebraL1?c <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---

## Post #6 by @Sunderlandkyl (2020-07-09 20:20 UTC)

<p>You have two different segment editor widgets in your code.</p>
<p>You create one and assign the segmentation here:<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/kbehlmirusmed/VertebraSeg/blob/cf64dcfe6ebb8fd40d3b80af394852b6c04d3572/VertebraSeg.py#L34-L40" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/kbehlmirusmed/VertebraSeg/blob/cf64dcfe6ebb8fd40d3b80af394852b6c04d3572/VertebraSeg.py#L34-L40" target="_blank" rel="nofollow noopener">kbehlmirusmed/VertebraSeg/blob/cf64dcfe6ebb8fd40d3b80af394852b6c04d3572/VertebraSeg.py#L34-L40</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="34" style="counter-reset: li-counter 33 ;">
<li>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()</li>
<li>segmentEditorWidget.setMRMLScene(slicer.mrmlScene)</li>
<li>segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()</li>
<li>slicer.mrmlScene.AddNode(segmentEditorNode)</li>
<li>segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)</li>
<li>segmentEditorWidget.setSegmentationNode(segmentationNode)</li>
<li>segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>And then you get the widget from the module here:<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/kbehlmirusmed/VertebraSeg/blob/cf64dcfe6ebb8fd40d3b80af394852b6c04d3572/VertebraSeg.py#L41-L43" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/kbehlmirusmed/VertebraSeg/blob/cf64dcfe6ebb8fd40d3b80af394852b6c04d3572/VertebraSeg.py#L41-L43" target="_blank" rel="nofollow noopener">kbehlmirusmed/VertebraSeg/blob/cf64dcfe6ebb8fd40d3b80af394852b6c04d3572/VertebraSeg.py#L41-L43</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="41" style="counter-reset: li-counter 40 ;">
<li>segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor</li>
<li>segmentEditorWidget.setActiveEffectByName("Local Threshold")</li>
<li>effect = segmentEditorWidget.activeEffect() ##open segment editor tab</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Probably you need to delete the first one from the code, and only use the widget from the Segment Editor module.</p>

---

## Post #7 by @vertebra (2020-07-10 12:34 UTC)

<p>Thank you <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>
<p>One last question…</p>
<p>Is there a way to open up the segment editor module from the python interactor?</p>
<p>Thank you!</p>

---

## Post #8 by @vertebrae (2020-07-10 15:32 UTC)

<p>Does anyone have a response to this? We looked in some class references and did not find anything that worked. <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #9 by @Sunderlandkyl (2020-07-10 15:49 UTC)

<blockquote>
<p>slicer.util.selectModule(‘SegmentEditor’)</p>
</blockquote>

---
