---
topic_id: 3550
title: "Convert Label Map Volume Into A Scalarvolumenode"
date: 2018-07-21
url: https://discourse.slicer.org/t/3550
---

# Convert label map volume into a scalarvolumenode

**Topic ID**: 3550
**Date**: 2018-07-21
**URL**: https://discourse.slicer.org/t/convert-label-map-volume-into-a-scalarvolumenode/3550

---

## Post #1 by @Laura (2018-07-21 11:41 UTC)

<p>Good morning,</p>
<p>To convert my label map volume into a scalarvolumenode after correction on Segment editor and “export” the label map, I have some difficulties…<br>
I am able to convert this updated label map into a numpy array (called ‘a’) but then, I don’t succeed in converting it into a vtkMRMLScalarVolumeNode : do you know how can I do this ?<br>
Maybe I have committed some errors before by exporting my label map with my segmentation…</p>
<p>This is my code :</p>
<blockquote>
<p>seg = slicer.util.getNode(‘CorrectionSegmentationFoie’)<br>
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’,‘LabelFoiefinal’)</p>
<p>foiesegfin = slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(seg, labelmapVolumeNode)<br>
a = slicer.util.array(‘LabelFoiefinal’)<br>
volumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLScalarVolumeNode’,“VolumeFoieSegmente”)<br>
foieseg = slicer.util.updateVolumeFromArray(volumeNode, a)</p>
</blockquote>
<p>Thanks a lot in advance !<br>
Laura</p>
<p>P.S : Do you know how to force in my python script to check the “sphere brush” in my 'Segment editor" module and force also my “MasterVolume” to be the label map that I have created from my previous uncorrected volume ?</p>

---

## Post #2 by @Fernando (2018-07-22 11:02 UTC)

<p>Hi Laura,</p>
<aside class="quote no-group" data-username="Laura" data-post="1" data-topic="3550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/a4c791/48.png" class="avatar"> Laura:</div>
<blockquote>
<p>I don’t succeed in converting it into a vtkMRMLScalarVolumeNode : do you know how can I do this ?</p>
</blockquote>
</aside>
<p>You can try <a href="https://apidocs.slicer.org/v4.8/classvtkSlicerVolumesLogic.html#a2f8a3951a503ea98d40f223094ac6f75" rel="noopener nofollow ugc">CreateScalarVolumeFromVolume </a>.</p>

---

## Post #3 by @Laura (2018-07-22 13:32 UTC)

<p>Hey !</p>
<p>Thanks for this idea, I have tried so much but not this one !<br>
Unfortunately, when I write this on my python script :</p>
<blockquote>
<pre><code>seg = slicer.util.getNode('CorrectionSegmentationFoie')
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode','LabelFoiefinal')
slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(seg, labelmapVolumeNode)
outputvolumenode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", 'FoieSegmenteApresCorrection')
sef = slicer.modules.volumes.logic().CreateScalarVolumeFromVolume(slicer.mrmlScene,labelmapVolumeNode, outputvolumenode)
</code></pre>
</blockquote>
<p>My 3D Slicer crashes without saying nothing… Just crashes and asks me if I want to reload Slicer without any explanation…<br>
Do I made a mistake ?<br>
Thanks a lot in advance and enjoy your weekend !<br>
Laura</p>

---

## Post #4 by @cpinter (2018-07-22 15:13 UTC)

<p>I don’t see any problems with your code after a quick look. A few things to check:</p>
<ol>
<li>What does the log say? You can find it in About menu / Report a problem window</li>
<li>If you show labelmapVolumeNode in the slice view or in 3D volume rendering do you see anything?</li>
<li>If you enter the lines one by one which one causes the crash?</li>
</ol>

---

## Post #5 by @Fernando (2018-07-22 16:44 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="3550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<ol>
<li>If you enter the lines one by one which one causes the crash?</li>
</ol>
</blockquote>
</aside>
<p>I just tried her code and Slicer crashed after running the last command. The last line of my log is not suspicious:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 22.07.2018 17:42:34 [] (unknown:0) - Python console user input: outputvolumenode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", 'FoieSegmenteApresCorrection')
</code></pre>
<p>Also, the label map looks fine.</p>

---

## Post #6 by @Fernando (2018-07-22 16:52 UTC)

<aside class="quote no-group quote-modified" data-username="Laura" data-post="3" data-topic="3550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/a4c791/48.png" class="avatar"> Laura:</div>
<blockquote>
<blockquote>
<pre><code class="lang-auto">sef = slicer.modules.volumes.logic().CreateScalarVolumeFromVolume(slicer.mrmlScene,labelmapVolumeNode, outputvolumenode)
</code></pre>
</blockquote>
</blockquote>
</aside>
<p>Try swapping the arguments:</p>
<pre><code class="lang-auto">sef = slicer.modules.volumes.logic().CreateScalarVolumeFromVolume(slicer.mrmlScene, outputvolumenode, labelmapVolumeNode)
</code></pre>
<p>According to the <a href="https://apidocs.slicer.org/v4.8/classvtkSlicerVolumesLogic.html#a2f8a3951a503ea98d40f223094ac6f75" rel="noopener nofollow ugc">docs</a>, the second argument is your output and the third is the input.</p>
<p>But of course Slicer shouldn’t just crash <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @cpinter (2018-07-22 19:41 UTC)

<p>Thanks, Fernando!<br>
Does this function crash with any data? If so, then it should be an easy fix. Otherwise I can fix it if you give me the labelmap that you get after exporting.</p>

---

## Post #8 by @Fernando (2018-07-22 19:53 UTC)

<p>Anything should work. I just thresholded MRHead in the Segment Editor, renamed the segmentation node and pasted the code.</p>

---

## Post #9 by @cpinter (2018-07-22 20:19 UTC)

<p>I fixed the crash, I’ll integrate it in a minute so it shouldn’t crash in tomorrow’s version.</p>
<p>There is also something to fix in VTK too, though, because DeepCopy shouldn’t crash if you give it null pointer, which is what happens here (so my fix in Slicer is only a superficial fix). This is where it starts (and I made sure it doesn’t get this far):<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Volumes/Logic/vtkSlicerVolumesLogic.cxx#L998" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Volumes/Logic/vtkSlicerVolumesLogic.cxx#L998" target="_blank">Slicer/Slicer/blob/master/Modules/Loadable/Volumes/Logic/vtkSlicerVolumesLogic.cxx#L998</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="988" style="counter-reset: li-counter 987 ;">
<li>  }</li>
<li>
</li>
<li>// Associate labelmap with the source volume</li>
<li>if (inputVolume-&gt;GetID())</li>
<li>  {</li>
<li>  outputVolume-&gt;SetNodeReferenceID("AssociatedNodeID", inputVolume-&gt;GetID());</li>
<li>  }</li>
<li>
</li>
<li>// Copy and set image data of the input volume to the label volume</li>
<li>vtkNew&lt;vtkImageData&gt; imageData;</li>
<li class="selected">imageData-&gt;DeepCopy(inputVolume-&gt;GetImageData());</li>
<li>outputVolume-&gt;SetAndObserveImageData(imageData.GetPointer());</li>
<li>
</li>
<li>vtkNew&lt;vtkMatrix4x4&gt; ijkToRas;</li>
<li>inputVolume-&gt;GetIJKToRASMatrix(ijkToRas.GetPointer());</li>
<li>outputVolume-&gt;SetIJKToRASMatrix(ijkToRas.GetPointer());</li>
<li>
</li>
<li>outputVolume-&gt;SetAndObserveTransformNodeID(inputVolume-&gt;GetTransformNodeID());</li>
<li>
</li>
<li>// Create a display node if the output node does not have one</li>
<li>outputVolume-&gt;CreateDefaultDisplayNodes();</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Then vtkImageData and vtkDataSet handles the null properly, but then in vtkDataObject this call causes the crash ultimately:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Kitware/VTK/blob/master/Common/DataModel/vtkDataObject.cxx#L550" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/VTK/blob/master/Common/DataModel/vtkDataObject.cxx#L550" target="_blank">Kitware/VTK/blob/master/Common/DataModel/vtkDataObject.cxx#L550</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="540" style="counter-reset: li-counter 539 ;">
<li>    fd-&gt;ShallowCopy(src-&gt;FieldData);</li>
<li>    this-&gt;SetFieldData(fd);</li>
<li>    fd-&gt;FastDelete();</li>
<li>  }</li>
<li>}</li>
<li>}</li>
<li>
</li>
<li>//----------------------------------------------------------------------------</li>
<li>void vtkDataObject::DeepCopy(vtkDataObject *src)</li>
<li>{</li>
<li class="selected">vtkFieldData *srcFieldData = src-&gt;GetFieldData();</li>
<li>
</li>
<li>this-&gt;InternalDataObjectCopy(src);</li>
<li>
</li>
<li>if (srcFieldData)</li>
<li>{</li>
<li>  vtkFieldData *newFieldData = vtkFieldData::New();</li>
<li>  newFieldData-&gt;DeepCopy(srcFieldData);</li>
<li>  this-&gt;SetFieldData(newFieldData);</li>
<li>  newFieldData-&gt;FastDelete();</li>
<li>}</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Optimally this should be fixed in VTK.</p>
<p>To answer the original question, I think Fernando’s suggestion is the solution, which is to swap the arguments.</p>

---

## Post #10 by @lassoan (2018-07-22 20:32 UTC)

<p>Unfortunately, DeepCopy has no return value and VTK does not use exceptions, so there is not really a clean way to handle invalid DeepCopy input. Maybe VTK could log an error and return when the input is NULL instead of crashing? There is a chance that the error would be missed, but probably it is still better than crashing.</p>

---

## Post #11 by @cpinter (2018-07-22 20:35 UTC)

<p>In the DeepCopy functions of vtkImageData and vtkDataSet the null argument was simply handled with an if statement. Indeed, no error was logged. I think adding it would be a nice solution, but then to make it consistent we’d need to change potentially a hundred VTK classes.<br>
Maybe the easiest would be to just fix this one in vtkDataObject.</p>

---

## Post #12 by @cpinter (2018-07-22 20:36 UTC)

<p>By the way, <a class="mention" href="/u/laura">@Laura</a>, swapping the arguments was the solution to your problem, I could confirm. So the last line should be</p>
<pre><code>sef = slicer.modules.volumes.logic().CreateScalarVolumeFromVolume(slicer.mrmlScene, outputvolumenode, labelmapVolumeNode)</code></pre>

---

## Post #13 by @Laura (2018-07-23 06:19 UTC)

<p>Good morning,</p>
<aside class="quote no-group" data-username="cpinter" data-post="12" data-topic="3550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>sef = slicer.modules.volumes.logic().CreateScalarVolumeFromVolume(slicer.mrmlScene, outputvolumenode, labelmapVolumeNode)</p>
</blockquote>
</aside>
<p>Thank you so so much to everybody, this works perfectly !!!<br>
Have a good day<br>
Laura</p>

---

## Post #14 by @Laura (2018-07-23 12:13 UTC)

<p>Another little question <a class="mention" href="/u/cpinter">@cpinter</a> and <a class="mention" href="/u/fernando">@Fernando</a> :  do you know how to force in my python script to check the “sphere brush” in my 'Segment editor" module and force also my “MasterVolume” to be the label map that I have created from my previous uncorrected volume ?</p>
<p>Thanks again for everything !</p>
<p>Laura</p>

---

## Post #15 by @cpinter (2018-07-23 13:32 UTC)

<p>Hi Laura,</p>
<p>You can find information about driving Segment Editor from python here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>
<p>I think if you set the reference volume using the function called SetReferenceImageGeometryParameterFromVolumeNode in the segmentation node, then it should be selected when you enter Segment Editor. Please note that you need to set this as soon as you have both nodes in the scene, and definitely before you enter Segment Editor.</p>

---

## Post #16 by @lassoan (2018-07-23 19:00 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="15" data-topic="3550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I think if you set the reference volume using the function called SetReferenceImageGeometryParameterFromVolumeNode in the segmentation node, then it should be selected when you enter Segment Editor.</p>
</blockquote>
</aside>
<p>You can also explicitly call <code>segmentEditorWidget.setMasterVolumeNode(...)</code> as it is done in almost all segmentation scripting examples.</p>
<aside class="quote no-group" data-username="Laura" data-post="14" data-topic="3550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/a4c791/48.png" class="avatar"> Laura:</div>
<blockquote>
<p>check the “sphere brush”</p>
</blockquote>
</aside>
<p>It is a parameter effect, which you can modify by calling <code>effect.SetParameter(…)</code> as shown in examples, or modifying the segment editor node directly: <code>getNode('SegmentEditor').SetAttribute('BrushSphere','1')</code></p>

---

## Post #17 by @cpinter (2018-07-23 19:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="3550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can also explicitly call <code>segmentEditorWidget.setMasterVolumeNode(...)</code></p>
</blockquote>
</aside>
<p>That’s right, you’re already using the Segment Editor widget from script anyway, so this will make it simpler.</p>

---

## Post #18 by @Laura (2018-07-24 07:33 UTC)

<p>Thanks a lot for your super help !<br>
I succeed for the brush but I am still looking for the ‘setMasterVolumeNode’ because, when I write :</p>
<blockquote>
<p>editorWidget = slicer.modules.segmenteditor.createNewWidgetRepresentation()<br>
editorWidget.setMRMLScene(slicer.app.mrmlScene())<br>
slicer.util.getNode(‘SegmentEditor’).SetAttribute(‘BrushSphere’,‘1’)<br>
editorWidget.setMasterVolumeNode(inputVolCor)<br>
editorWidget.show()</p>
</blockquote>
<p>I have this error caused by my last line :</p>
<blockquote>
<p>AttributeError: qSlicerScriptedLoadableModuleWidget has no attribute named ‘setMasterVolumeNode’</p>
</blockquote>
<p>But I am looking for a solution !<br>
Thanks again !<br>
Laura</p>

---

## Post #19 by @lassoan (2018-07-24 17:23 UTC)

<aside class="quote no-group" data-username="Laura" data-post="18" data-topic="3550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/a4c791/48.png" class="avatar"> Laura:</div>
<blockquote>
<p>editorWidget = slicer.modules.segmenteditor.createNewWidgetRepresentation()</p>
</blockquote>
</aside>
<p>This line does not seem to be correct. You should not instantiate a new module widget.<br>
You either create a new segment editor widget (as is shown in most examples; I would recommend this):</p>
<pre><code>editorWidget = slicer.qMRMLSegmentEditorWidget()
</code></pre>
<p>or access the existing module widget of the SegmentEditor module:</p>
<pre><code>slicer.util.selectModule("SegmentEditor")
editorWidget=slicer.modules.segmenteditor.widgetRepresentation().self().editor
</code></pre>

---

## Post #20 by @Laura (2018-07-25 07:58 UTC)

<p>Good morning,</p>
<p>I agree with you but this is the only way I found to create a popup of Segment Editor :</p>
<ul>
<li>for your first solution :</li>
</ul>
<blockquote>
<p>editorWidget = slicer.qMRMLSegmentEditorWidget()</p>
</blockquote>
<p>No segment editor popup appears even when I use the script in most examples with the line ‘.show()’ and I would like to paint and erase as I need so this is not convenient for what I do</p>
<ul>
<li>for your second solution :</li>
</ul>
<blockquote>
<p>slicer.util.selectModule(“SegmentEditor”)<br>
editorWidget=slicer.modules.segmenteditor.widgetRepresentation().self().editor</p>
</blockquote>
<p>The Segment Editor Widget appears of course but not in a popup so I haven’t my extension wizard background so this is not convenient neither <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>That’s why I have found this one :</p>
<blockquote>
<pre><code>editorWidget = slicer.modules.segmenteditor.createNewWidgetRepresentation()
</code></pre>
</blockquote>

---

## Post #21 by @lassoan (2018-07-25 12:42 UTC)

<aside class="quote no-group" data-username="Laura" data-post="20" data-topic="3550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/a4c791/48.png" class="avatar"> Laura:</div>
<blockquote>
<p>No segment editor popup appears even when I use the script in most examples with the line ‘.show()’</p>
</blockquote>
</aside>
<p>Probably you don’t see the widget because the widget gets deleted automatically when the variable gets out of scope. You can address this by storing <code>editorWidget</code> variable in a class member variable or adding the widget to a layout. A good example is the Segment Editor module itself: copy-paste, rename, and modify Segment Editor module to fit your needs.</p>

---
