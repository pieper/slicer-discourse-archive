---
topic_id: 20046
title: "How To Get Parameters Of Segment Editor Effects"
date: 2021-10-07
url: https://discourse.slicer.org/t/20046
---

# How to get parameters of Segment Editor effects

**Topic ID**: 20046
**Date**: 2021-10-07
**URL**: https://discourse.slicer.org/t/how-to-get-parameters-of-segment-editor-effects/20046

---

## Post #1 by @Saima (2021-10-07 05:52 UTC)

<p>Hi Andras,<br>
How to get the parameter list for the segment editor modules</p>
<p>for example I need parameter list for wrap solidify. How can I get it.<br>
Regards,<br>
Saima Safdar</p>

---

## Post #2 by @lassoan (2021-10-07 05:57 UTC)

<p>You can find list of Segment Editor effect parameters for built-in effects here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html" class="inline-onebox">Segment editor — 3D Slicer documentation</a></p>
<p>Usually extension developers do not write this kind of documentation but you can read the list of parameters directly from the source code, see for example here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/blob/a9512a05f4203f4ae75211a9efde2bcab8bb549e/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py#L903-L962">
  <header class="source">

      <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/blob/a9512a05f4203f4ae75211a9efde2bcab8bb549e/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py#L903-L962" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/blob/a9512a05f4203f4ae75211a9efde2bcab8bb549e/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py#L903-L962" target="_blank" rel="noopener">sebastianandress/Slicer-SurfaceWrapSolidify/blob/a9512a05f4203f4ae75211a9efde2bcab8bb549e/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py#L903-L962</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="903" style="counter-reset: li-counter 902 ;">
          <li>ARG_DEFAULTS = {}</li>
          <li>ARG_OPTIONS = {}</li>
          <li>
          </li>
<li>ARG_REGION = 'region'</li>
          <li>REGION_OUTER_SURFACE = 'outerSurface'</li>
          <li>REGION_LARGEST_CAVITY = 'largestCavity'</li>
          <li>REGION_SEGMENT = 'segment'</li>
          <li>ARG_OPTIONS[ARG_REGION] = [REGION_OUTER_SURFACE, REGION_LARGEST_CAVITY, REGION_SEGMENT]</li>
          <li>ARG_DEFAULTS[ARG_REGION] = REGION_OUTER_SURFACE</li>
          <li>
          </li>
<li>ARG_REGION_SEGMENT_ID = 'regionSegmentID'</li>
          <li>ARG_DEFAULTS[ARG_REGION_SEGMENT_ID] = ''</li>
          <li>
          </li>
<li>ARG_CARVE_HOLES_IN_OUTER_SURFACE = 'carveHolesInOuterSurface'</li>
          <li>ARG_DEFAULTS[ARG_CARVE_HOLES_IN_OUTER_SURFACE] = False</li>
          <li>
          </li>
<li>ARG_CARVE_HOLES_IN_OUTER_SURFACE_DIAMETER = 'carveHolesInOuterSurfaceDiameter'</li>
          <li>ARG_DEFAULTS[ARG_CARVE_HOLES_IN_OUTER_SURFACE_DIAMETER] = 10.0</li>
          <li>
          </li>
<li>ARG_SPLIT_CAVITIES = 'splitCavities'</li>
      </ol>
    </code>
  </pre>

  This file has been truncated. <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/blob/a9512a05f4203f4ae75211a9efde2bcab8bb549e/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py#L903-L962" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Saima (2021-10-07 06:49 UTC)

<p>Hi Andras,<br>
could you help me with this.<br>
I am running the wrapsolidify using script. At the end I want models for the segments. but I get another segmentation node as a result.</p>
<pre><code>segmentEditorWidget.setActiveEffectByName("Wrap Solidify")
effect = segmentEditorWidget.activeEffect()

segmentEditorWidget.setCurrentSegmentID(segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('Bone'))
effect.setParameter("ARG_OUTPUT_TYPE", "OUTPUT_MODEL")
effect.setParameter("ARG_REGION", "region")
effect.setParameter("REGION_OUTER_SURFACE", "outerSurface")
effect.setParameter("ARG_CARVE_HOLES_IN_OUTER_SURFACE", True)
effect.setParameter("ARG_CARVE_HOLES_IN_OUTER_SURFACE_DIAMETER", 10)
effect.self().onApply()
</code></pre>
<p>I am not getting the model output file. for the current segment. any help. Am I applying it correctly.</p>
<p>Thank you</p>

---

## Post #4 by @Saima (2021-10-07 11:48 UTC)

<aside class="quote no-group" data-username="Saima" data-post="3" data-topic="20046">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>Hi Andras,<br>
could you help me with this.<br>
I am running the wrapsolidify using script. At the end I want models for the segments. but I get another segmentation node as a result.</p>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Wrap Solidify")
effect = segmentEditorWidget.activeEffect()

segmentEditorWidget.setCurrentSegmentID(segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('Bone'))
effect.setParameter("ARG_OUTPUT_TYPE", "OUTPUT_MODEL")
effect.setParameter("ARG_REGION", "region")
effect.setParameter("REGION_OUTER_SURFACE", "outerSurface")
effect.setParameter("ARG_CARVE_HOLES_IN_OUTER_SURFACE", True)
effect.setParameter("ARG_CARVE_HOLES_IN_OUTER_SURFACE_DIAMETER", 10)
effect.self().onApply()
</code></pre>
<p>I am not getting the model output file. for the current segment. any help. Am I applying it correctly.</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
could you help me with this.<br>
I am running the wrapsolidify using script. At the end I want models for the segments. but I get another segmentation node as a result.</p>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Wrap Solidify")
effect = segmentEditorWidget.activeEffect()

segmentEditorWidget.setCurrentSegmentID(segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('Bone'))
effect.setParameter("ARG_OUTPUT_TYPE", "OUTPUT_MODEL")
effect.setParameter("ARG_REGION", "region")
effect.setParameter("REGION_OUTER_SURFACE", "outerSurface")
effect.setParameter("ARG_CARVE_HOLES_IN_OUTER_SURFACE", True)
effect.setParameter("ARG_CARVE_HOLES_IN_OUTER_SURFACE_DIAMETER", 10)
effect.self().onApply()
</code></pre>
<p>I am not getting the model output file. for the current segment. any help. Am I applying it correctly.</p>

---

## Post #5 by @lassoan (2021-10-07 12:20 UTC)

<p>You need to use the variable’s value in the string literal, not the variable’s name. For example, replace <code>"ARG_OUTPUT_TYPE" </code> by <code>"outputType" </code>.</p>

---

## Post #6 by @Saima (2021-10-07 12:29 UTC)

<pre><code> effect.setParameter("region", "outerSurface")
    effect.setParameter("regionSegmentID", segmentName)
    #effect.setParameter("REGION_OUTER_SURFACE", "outerSurface")
    #effect.setParameter("REGION_LARGEST_CAVITY", "largestCavity")
    effect.setParameter("carveHolesInOuterSurface", True)
    effect.setParameter("carveHolesInOuterSurfaceDiameter", 10)
    effect.setParameter("outputType", "model")
    #effect.setParameter("ARG_OUTPUT_MODEL_NODE", model1)
    effect.self().onApply()
</code></pre>
<p>Like this I am getting the model.</p>
<p>I am using split island by filter but i do not understand why it is running two times although my script contains only one time but it is creating a new segmentation node again.<br>
is it because i am using this line</p>
<pre><code>segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone)
</code></pre>
<p>regards,<br>
Saima Safdar</p>

---

## Post #7 by @lassoan (2021-10-07 12:47 UTC)

<p>It seems that everything works as expected, it may be just not clear for you yet how things work internally. For this, you can attach a Python debugger and go through all the Python code step by step very easily. If you want to dig into C++ code as well then you can either just read the source code; or build Slicer and step through the code using Visual Studio’s debugger. See instructions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/index.html">here</a>.</p>

---

## Post #8 by @Saima (2021-10-07 15:19 UTC)

<p>Hi Andras,<br>
I do not understand the following</p>
<p>Processing started<br>
QLayout::addChildLayout: layout “” already has a parent<br>
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 10 1<br>
72 islands created (12083 ignored)<br>
72 islands created (0 ignored)<br>
Processing completed in 422.18 seconds<br>
Processing started<br>
QLayout::addChildLayout: layout “” already has a parent<br>
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 10 1<br>
72 islands created (12083 ignored)<br>
72 islands created (0 ignored)<br>
QString qSlicerSegmentEditorAbstractEffect::parameter(QString) : Parameter named  “regionSegmentID”  cannot be found for effect  “Wrap Solidify”<br>
Processing completed in 825.04 seconds</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #9 by @lassoan (2021-10-07 17:59 UTC)

<p>You can put a breakpoint where “islands created” is logged and see what has called that method.</p>
<p>By the way, 825 second for Wrap Solidify is extreme. Probably you want to clean up the input segmentation a bit (a small smoothing may suffice) to get reasonable computation time.</p>

---
