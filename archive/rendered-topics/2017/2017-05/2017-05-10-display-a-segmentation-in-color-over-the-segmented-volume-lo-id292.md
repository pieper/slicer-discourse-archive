---
topic_id: 292
title: "Display A Segmentation In Color Over The Segmented Volume Lo"
date: 2017-05-10
url: https://discourse.slicer.org/t/292
---

# Display a segmentation in color over the segmented volume - loadable module

**Topic ID**: 292
**Date**: 2017-05-10
**URL**: https://discourse.slicer.org/t/display-a-segmentation-in-color-over-the-segmented-volume-loadable-module/292

---

## Post #1 by @sandra (2017-05-10 15:30 UTC)

<p>Operating system: MAC<br>
Slicer version: 4.6.2</p>
<p>Hi everyone,</p>
<p>I am currently writting my own loadable module and I would need to segment a volume (for example by thresholding it) and display the segmentation in color over the segmented volume, as it is done in the “Segmentations” module (“Segment Editor”, the threshold effect).</p>
<p>To do so, I read the code of this loadable module (mostly qSlicerSegmentEditorAbstractEffect.cxx and <a href="http://SegmentEditorThresholdEffect.py" rel="nofollow noopener">SegmentEditorThresholdEffect.py</a>) and I managed to extract some of the things I would need but I’m missing things and I’m a bit lost in the two files mentionned.<br>
Thanks for any answer that could help me understand how to do this.</p>
<p>Here is what I have for the moment:</p>
<p>///////////////////////////////////////////////////////////////////////////</p>
<p>vtkMRMLScalarVolumeNode* volumeNode = … ;<br>
vtkImageData* image = … ;</p>
<p>vtkNew thresholdFilter;<br>
thresholdFilter-&gt;SetInValue(255);<br>
thresholdFilter-&gt;SetOutValue(0);<br>
thresholdFilter-&gt;SetInputData(image);<br>
thresholdFilter-&gt;ThresholdBetween(min,max);</p>
<p>qSlicerLayoutManager* layoutManager = qSlicerApplication::application()-&gt;layoutManager();<br>
foreach (QString sliceViewName, layoutManager-&gt;sliceViewNames())<br>
{<br>
qMRMLSliceWidget* sliceWidget = layoutManager-&gt;sliceWidget(sliceViewName);</p>
<pre><code>    vtkNew&lt;vtkLookupTable&gt; lookupTable;
    vtkNew&lt;vtkImageMapToRGBA&gt; colorMapper;
    vtkNew&lt;vtkImageMapper&gt; mapper;
    vtkNew&lt;vtkActor2D&gt; actor;

    lookupTable-&gt;SetRampToLinear();
    lookupTable-&gt;SetNumberOfTableValues(2);
    lookupTable-&gt;SetTableRange(0,255);
    lookupTable-&gt;SetTableValue(0,0,0,0,0);
    lookupTable-&gt;SetTableValue(1,0.5,0.7,0.5,0.8);

    colorMapper-&gt;SetOutputFormatToRGBA();
    colorMapper-&gt;SetLookupTable(lookupTable.GetPointer());

    actor-&gt;VisibilityOn();
    actor-&gt;SetMapper(mapper.GetPointer());

    mapper-&gt;SetColorWindow(255);
    mapper-&gt;SetColorLevel(128);

    colorMapper-&gt;SetInputConnection(thresholdFilter-&gt;GetOutputPort());

    mapper-&gt;SetInputConnection(colorMapper-&gt;GetOutputPort());
   
    vtkRenderWindow* renderWindow = sliceWidget-&gt;sliceView()-&gt;renderWindow();
    vtkRenderer* renderer = vtkRenderer::SafeDownCast(renderWindow-&gt;GetRenderers()-&gt;GetItemAsObject(0));
    renderer-&gt;AddActor2D(actor.GetPointer());
   
    sliceWidget-&gt;sliceView()-&gt;scheduleRender();
}

vtkSlicerApplicationLogic* slicerAppLogic = this-&gt;module()-&gt;appLogic();
vtkMRMLSelectionNode* selectionNode = slicerAppLogic-&gt;GetSelectionNode();
selectionNode-&gt;SetReferenceActiveVolumeID(volumeNode-&gt;GetID());
slicerAppLogic-&gt;PropagateVolumeSelection();
</code></pre>
<p>/////////////////////////////////////////////////////////////////////////////////////////////////</p>
<p>Regards,</p>
<p>Sandra.</p>

---

## Post #2 by @lassoan (2017-05-10 17:08 UTC)

<p>Probably the simplest is to create a segment editor widget, set its inputs (scene, input volume, segmentation), activate an effect, set parameters, and apply the effect.</p>
<p>Here is an example in Python (the same works in C++ with some trivial changes in syntax):</p>
<pre><code># Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
# To show segment editor widget (useful for debugging): segmentEditorWidget.show()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Run segmentation
segmentEditorWidget.setActiveEffectByName("Grow from seeds")
effect = segmentEditorWidget.activeEffect()
# You can change parameters by calling: effect.setParameter("MyParameterName", someValue)
# Most effect don't have onPreview, you can just call onApply
effect.self().onPreview()
effect.self().onApply()

# Clean up and show results
################################################

# Clean up
slicer.mrmlScene.RemoveNode(segmentEditorNode)

# Make segmentation results nicely visible in 3D
segmentationDisplayNode = segmentationNode.GetDisplayNode()
segmentationDisplayNode.SetSegmentVisibility(backgroundSegmentId, False)
</code></pre>
<p>You can find some more examples here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---

## Post #3 by @Davide_Punzo (2017-05-10 18:01 UTC)

<p>Hi Sandra, I do something like that here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/Widgets/qSlicerAstroVolumeModuleWidget.cxx#L1551-L1556" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/Widgets/qSlicerAstroVolumeModuleWidget.cxx#L1551-L1556" target="_blank" rel="nofollow noopener">Punzo/SlicerAstro/blob/master/AstroVolume/Widgets/qSlicerAstroVolumeModuleWidget.cxx#L1551-L1556</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="1551" style="counter-reset: li-counter 1550 ;">
<li>{</li>
<li>vtkMRMLVolumeRenderingDisplayNode *volumeOneRenderingDisplay =</li>
<li>  vtkMRMLVolumeRenderingDisplayNode::SafeDownCast</li>
<li>    (this-&gt;mrmlScene()-&gt;GetNodeByID(volumeOne-&gt;GetNthDisplayNodeID(i)));</li>
<li>if (volumeOneRenderingDisplay)</li>
<li>  {</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Specifically:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/Widgets/qSlicerAstroVolumeModuleWidget.cxx#L1727-L1875" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/Widgets/qSlicerAstroVolumeModuleWidget.cxx#L1727-L1875" target="_blank" rel="nofollow noopener">Punzo/SlicerAstro/blob/master/AstroVolume/Widgets/qSlicerAstroVolumeModuleWidget.cxx#L1727-L1875</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="1727" style="counter-reset: li-counter 1726 ;">
<li>SegmentOneID += "_3RMS";</li>
<li>vtkSegment *SegmentOne = currentSegmentationNode-&gt;GetSegmentation()-&gt;GetSegment(SegmentOneID);</li>
<li>if(!SegmentOne)</li>
<li>  {</li>
<li>  SegmentOneID = currentSegmentationNode-&gt;GetSegmentation()-&gt;AddEmptySegment(SegmentOneID, SegmentOneID);</li>
<li>
</li>
<li>  vtkNew&lt;vtkImageThreshold&gt; imageThreshold;</li>
<li>  imageThreshold-&gt;SetInputData(volumeOne-&gt;GetImageData());</li>
<li>  double min, max;</li>
<li>  min = StringToDouble(volumeOne-&gt;GetAttribute("SlicerAstro.3DDisplayThreshold")) * 3.;</li>
<li>  max = StringToDouble(volumeOne-&gt;GetAttribute("SlicerAstro.DATAMAX"));</li>
<li>  imageThreshold-&gt;ThresholdBetween(min, max);</li>
<li>  imageThreshold-&gt;SetInValue(1);</li>
<li>  imageThreshold-&gt;SetOutValue(0);</li>
<li>  imageThreshold-&gt;SetOutputScalarType(VTK_SHORT);</li>
<li>  imageThreshold-&gt;Update();</li>
<li>  vtkNew&lt;vtkOrientedImageData&gt; modifierLabelmap;</li>
<li>  modifierLabelmap-&gt;DeepCopy(imageThreshold-&gt;GetOutput());</li>
<li>  vtkNew&lt;vtkMatrix4x4&gt; IJKToRASMatrix;</li>
<li>  volumeOne-&gt;GetIJKToRASMatrix(IJKToRASMatrix.GetPointer());</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/Widgets/qSlicerAstroVolumeModuleWidget.cxx#L1727-L1875" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I guess it is possible to clean, by removing the initialization of the segment editor node (and just creating a segmentation node). However,  in my case I inizialize the segment editor, and, then, I use the segmentation node create from the segmentation editor. This because I want that the segments that I create by thresholding the volumes will appear in the Segmentation editor module immediatly, so the user has already everything settled for modifying the selection done by thresholding.</p>

---

## Post #4 by @sandra (2017-05-10 19:08 UTC)

<p>Thank you very much both for your answers !</p>
<p>I would need to do my own segmentation after (and not use an already existing one like thresholding or growing from seeds in slicer) so I guess with your solution Andras it might not be possible ? or I would need to create my own effect in order to activate it ?</p>
<p>I believe I won’t have this issue with your solution Davide, so I’ll try to work from the code you gave me and come back to you if necessary.</p>
<p>Thank you,<br>
Regards,<br>
Sandra.</p>

---

## Post #5 by @lassoan (2017-05-10 19:20 UTC)

<p>If there is already an effect that does what you need then follow this example: <a href="https://subversion.assembla.com/svn/slicerrt/trunk/SlicerRt/samples/PythonScripts/SegmentGrowCut/SegmentGrowCutSimple.py">https://subversion.assembla.com/svn/slicerrt/trunk/SlicerRt/samples/PythonScripts/SegmentGrowCut/SegmentGrowCutSimple.py</a></p>
<p>If you want to do segmentation by using VTK, ITK, etc. classes then follow this example:<br>
<a href="https://subversion.assembla.com/svn/slicerrt/trunk/SlicerRt/samples/PythonScripts/SegmentGrowCut/SegmentGrowCut.py" class="onebox" target="_blank">https://subversion.assembla.com/svn/slicerrt/trunk/SlicerRt/samples/PythonScripts/SegmentGrowCut/SegmentGrowCut.py</a><br>
If it works well and you want to use it using a graphical user interface, share it with others, etc. then put it into a Segment editor effect (use the Extension wizard in Slicer to create a new scriptededitoreffect module). See example of extending Segment editor with new effects in this extension: <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects">https://github.com/lassoan/SlicerSegmentEditorExtraEffects</a></p>

---

## Post #6 by @sandra (2017-05-11 07:40 UTC)

<p>Thank you, it seems to be what I needed, I’ll look into it and come back to you if I have more questions</p>

---

## Post #7 by @sandra (2017-05-11 13:40 UTC)

<p>Davide, with your solution, would it be possible to display two segments of the same volume with two different colors ? I think that’s what you did with your SegmentTwo and SegmentThree both done on volumeTwo but if I follow your example only the first segment is displayed.</p>

---

## Post #8 by @lassoan (2017-05-11 14:36 UTC)

<p>You can set the color of any segments independently. You can also have as many segments in the segmentation as you want and show them as the same time. If you need overlapping segments, set masking option <code>Overwrite other segments</code> to <code>None</code>.</p>

---

## Post #9 by @sandra (2017-05-11 14:53 UTC)

<p>I’ve already tried adding this line at the end:<br>
SegmentationDisplayNode-&gt;SetSegmentOverrideColor(SegmentTwoID, 0.7, 0.5, 0.5);<br>
And I get only the first segment displayed with the new color (0.7,0.5,0.5)</p>
<p>And even without trying to modify the color of any segment, I only get the first segment displayed</p>

---

## Post #10 by @lassoan (2017-05-11 18:35 UTC)

<p>Add your segment to the scene and check if all segments shows up in the Segmentations module. If you still have problems then save the segmentation node to file and share it with us so that we can have a look (upload to Dropbox or OneDrive and attach the link).</p>

---

## Post #11 by @sandra (2017-05-12 08:27 UTC)

<p>Indeed I had only one segment showing up in the Segmentations module,  I found my error (the two segments ended havind the same ID so I only got one segment).</p>
<p>Thank you very much for your help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #12 by @Davide_Punzo (2017-05-15 20:48 UTC)

<p>sorry I didn’t see your messages. Glad that you managed it!</p>

---

## Post #13 by @qiqi5210 (2022-05-06 11:50 UTC)

<p>Dr. Lassoan,<br>
Hello.Recently, I have been writing modules in C + +, and I have also studied a lot about the call of segmenteditor. I want to know how to apply effects in C + +, such as threshold apply.<br>
Best wishes to you.Thank you in advance.</p>

---
