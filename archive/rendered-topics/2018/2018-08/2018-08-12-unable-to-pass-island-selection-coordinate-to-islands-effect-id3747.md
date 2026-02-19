---
topic_id: 3747
title: "Unable To Pass Island Selection Coordinate To Islands Effect"
date: 2018-08-12
url: https://discourse.slicer.org/t/3747
---

# Unable to pass island selection coordinate to Islands effect by python script

**Topic ID**: 3747
**Date**: 2018-08-12
**URL**: https://discourse.slicer.org/t/unable-to-pass-island-selection-coordinate-to-islands-effect-by-python-script/3747

---

## Post #1 by @devakumar (2018-08-12 21:53 UTC)

<p>Dear Development team, I appreciate your work on the segment editor effects.</p>
<p>I am trying to select an island from the selected segmentation by python script. I am using the following code.</p>
<pre><code class="lang-auto">    # Keep the selected island
    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    print 'Island effect name', effect
    #operationName = 'KEEP_LARGEST_ISLAND'
    operationName = 'KEEP_SELECTED_ISLAND'
    minSize = 1000
    effect.setParameter("Operation",operationName)
    effect.setParameter("MinimumSize", minSize);
    effect.self().onApply()
</code></pre>
<p>I don’t know how to set the parameter to pass the coordinate for island selection. Could you please help me. <code>KEEP_LARGEST_ISLAND</code> operation works fine as it doesn’t require a coordinate to be passed.</p>
<p>Regards<br>
Devakumar<br>
Department of Nuclear Medicine<br>
Christian Medical College,<br>
Vellore-632004<br>
India</p>

---

## Post #2 by @Andinet_Enquobahrie (2018-08-13 12:13 UTC)

<p>Take a look at it the processInteractionEvents method in the Islands Effect python script.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorIslandsEffect.py#L210-L317" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorIslandsEffect.py#L210-L317" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorIslandsEffect.py#L210-L317</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="210" style="counter-reset: li-counter 209 ;">
<li>def processInteractionEvents(self, callerInteractor, eventId, viewWidget):</li>
<li>  import vtkSegmentationCorePython as vtkSegmentationCore</li>
<li>
</li>
<li>  abortEvent = False</li>
<li>
</li>
<li>  # Only allow in modes where segment selection is needed</li>
<li>  if not self.currentOperationRequiresSegmentSelection():</li>
<li>    return False</li>
<li>
</li>
<li>  # Only allow for slice views</li>
<li>  if viewWidget.className() != "qMRMLSliceWidget":</li>
<li>    return abortEvent</li>
<li>
</li>
<li>  if eventId != vtk.vtkCommand.LeftButtonPressEvent:</li>
<li>    return abortEvent</li>
<li>
</li>
<li>  abortEvent = True</li>
<li>
</li>
<li>  # Generate merged labelmap of all visible segments</li>
<li>  segmentationNode = self.scriptedEffect.parameterSetNode().GetSegmentationNode()</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorIslandsEffect.py#L210-L317" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I am not sure if there is easy easy way to do this. You will need to do a bit more coding to get this working (get the pixel position of the selected island, instantiate a flood fill filter based on the pixel value of the selected island, and update the islands effect default modifier labelmap using the flood fill filter results)</p>
<p>Hope this helps<br>
-Andinet</p>

---

## Post #3 by @mikebind (2019-04-05 22:25 UTC)

<p>I want to do something very similar to this.  I would like to use another segment’s binary label map as seed points for selecting islands to keep. I am prepared to extract and modify the relevant parts of the code <a href="https://discourse.slicer.org/u/Andinet_Enquobahrie">Andinet_Enquobahrie</a> linked above, but I have not been able to figure out how to get a list of IJK points from a binary label map.</p>
<p>Specifically, I know if I have a vtkSegment called seg in python, I can get its label map via <code>labelMap = seg.GetRepresentation('Binary labelmap').</code></p>
<p>And I see that I can find a select a segment from seed points using a flood filter like this:<br>
<code>floodFillingFilter = vtk.vtkImageThresholdConnectivity()</code><br>
<code>floodFillingFilter.SetInputData(inputLabelImage)</code><br>
<code>seedPoints = vtk.vtkPoints()</code><br>
<code>origin = inputLabelImage.GetOrigin()</code><br>
<code>spacing = inputLabelImage.GetSpacing()</code><br>
<code>seedPoints.InsertNextPoint(origin[0]+ijk[0]*spacing[0], origin[1]+ijk[1]*spacing[1], origin[2]+ijk[2]*spacing[2])</code><br>
<code>floodFillingFilter.SetSeedPoints(seedPoints)</code><br>
<code>floodFillingFilter.ThresholdBetween(pixelValue, pixelValue)</code></p>
<p>But I don’t know how to get IJK seed points from the labelmap.  Any suggestions?</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2019-04-06 12:51 UTC)

<p>You can use <code>numpy.where</code> function to get a list of ijk indices, then convert them to RAS, and from there convert to ijk indices of segmentation’s internal labelmap.</p>
<p>However, if the goal is to keep only islands that intersect with other segments then Grow from seeds effect should do a much better job. Use the segment that you want to process as <em>mask segment</em> (set “Editable area: Segment …” and then hide that segment to not use it as seed) and the other (one or more) segments will be used as seeds (if they overlap with a region in the mas segment then that region in the mask segment will retained in the output).</p>

---

## Post #5 by @mikebind (2019-04-06 17:03 UTC)

<p>Thanks Andras, I’ll try that approach instead. Much appreciated!</p>

---

## Post #6 by @mikebind (2019-04-15 16:12 UTC)

<p>I appreciate the suggestion, but the “Grow from seeds” effect says that it ignores masking settings, and indeed, when I tried this approach the resulting segment spilled outside the masking segment. Do you have another suggestion?</p>

---

## Post #7 by @lassoan (2019-04-15 16:48 UTC)

<p>In recent Slicer versions, a Grow from seeds effect takes masking settings into account.</p>

---

## Post #8 by @mikebind (2019-04-15 16:55 UTC)

<p>Thanks, I’ll update.</p>

---
