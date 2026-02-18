# Embedding Segment Editor in Layout Crashes Slicer 5 Upon Reload

**Topic ID**: 26075
**Date**: 2022-11-04
**URL**: https://discourse.slicer.org/t/embedding-segment-editor-in-layout-crashes-slicer-5-upon-reload/26075

---

## Post #1 by @rbumm (2022-11-04 15:15 UTC)

<p>The scripted <a href="https://github.com/acil-bwh/SlicerCIP/blob/develop/Scripted/CIP_Calibration/CIP_Calibration.py">SlicerCIP “Calibration” module</a> implements a reduced Slicer “Segment Editor” in its layout to define “Air” and “Blood” regions in lung CT.</p>
<p>The startup works fine, but a script “Reload” in development mode causes a crash as soon as paint drops are placed in the mentioned regions (Slicer 5.0.3 stable and Slicer 5.1).</p>
<p>I do not see the error, thank you for any ideas.</p>

---

## Post #2 by @cpinter (2022-11-04 15:36 UTC)

<p>After a quick readthrough I also haven’t found the potential problem, but in case others don’t have time soon to join the conversation, one suggestion I’d have is to start commenting out parts of the code and narrow down the reason for the crash that way. I mean for example comment out all the segment editor related things and verify there is no crash. Fine, then you start adding back in the code piece by piece, and see which line reintroduces the crash. Maybe not a big help but this is what occurs to me now…</p>

---

## Post #3 by @rbumm (2022-11-04 15:58 UTC)

<p>Thank you <a class="mention" href="/u/cpinter">@cpinter</a> - I tried that in many different combinations this afternoon but the crash only happens if I include <a href="https://github.com/acil-bwh/SlicerCIP/blob/7add81177be11da09ec05da592930a7292d717a3/Scripted/CIP_Calibration/CIP_Calibration.py#L122">this line</a> .<br>
Also tried to implement</p>
<pre><code class="lang-auto">       if self.segmentEditorNode: 
            slicer.mrmlScene.RemoveNode(self.segmentEditorNode)
            self.segmentEditorNode = None
        if self.segmentEditorWidget:
            self.segmentEditorWidget.setActiveEffect(None)
            self.segmentEditorWidget = None
</code></pre>
<p>in the <a href="https://github.com/acil-bwh/SlicerCIP/blob/7add81177be11da09ec05da592930a7292d717a3/Scripted/CIP_Calibration/CIP_Calibration.py#L331">cleanup function</a>.<br>
I´m just maintaining the code but it would be great to understand and fix this as in the current state the module seems to be single-use only.</p>

---

## Post #4 by @cpinter (2022-11-04 16:05 UTC)

<p>This line looks suspicious:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/acil-bwh/SlicerCIP/blob/7add81177be11da09ec05da592930a7292d717a3/Scripted/CIP_Calibration/CIP_Calibration.py#L255">
  <header class="source">

      <a href="https://github.com/acil-bwh/SlicerCIP/blob/7add81177be11da09ec05da592930a7292d717a3/Scripted/CIP_Calibration/CIP_Calibration.py#L255" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/acil-bwh/SlicerCIP/blob/7add81177be11da09ec05da592930a7292d717a3/Scripted/CIP_Calibration/CIP_Calibration.py#L255" target="_blank" rel="noopener">acil-bwh/SlicerCIP/blob/7add81177be11da09ec05da592930a7292d717a3/Scripted/CIP_Calibration/CIP_Calibration.py#L255</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="245" style="counter-reset: li-counter 244 ;">
          <li>self.segmentEditorAreaCollapsibleButton = ctk.ctkCollapsibleButton()</li>
          <li>self.segmentEditorAreaCollapsibleButton.text = "Segment editor"</li>
          <li>self.layout.addWidget(self.segmentEditorAreaCollapsibleButton, SlicerUtil.ALIGNMENT_VERTICAL_TOP)</li>
          <li>self.segmentEditorLayout = qt.QFormLayout(self.segmentEditorAreaCollapsibleButton)</li>
          <li></li>
          <li>self.segmentEditorWidget = qSlicerSegmentationsModuleWidgetsPythonQt.qMRMLSegmentEditorWidget()</li>
          <li>self.segmentEditorWidget.setMaximumNumberOfUndoStates(10)</li>
          <li>self.segmentEditorWidget.setMRMLScene(slicer.mrmlScene)</li>
          <li>self.segmentEditorWidget.unorderedEffectsVisible = False</li>
          <li>self.segmentEditorWidget.setEffectNameOrder(['Paint', 'Draw', 'Erase', 'Scissors'])</li>
          <li class="selected">self.segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")</li>
          <li>self.segmentEditorNode.SetSingletonTag("CIP_Calibration")</li>
          <li>self.segmentEditorWidget.setMRMLSegmentEditorNode(self.segmentEditorNode)</li>
          <li>self.segmentEditorWidget.setMasterVolumeNodeSelectorVisible(False)</li>
          <li>self.segmentEditorWidget.setSegmentationNodeSelectorVisible(False)</li>
          <li>self.segmentEditorWidget.setSwitchToSegmentationsButtonVisible(False)</li>
          <li>self.segmentEditorWidget.findChild( 'ctkMenuButton', 'Show3DButton' ).hide()</li>
          <li>self.segmentEditorWidget.findChild( 'QPushButton', 'AddSegmentButton' ).hide()</li>
          <li>self.segmentEditorWidget.findChild( 'QPushButton', 'RemoveSegmentButton' ).hide()</li>
          <li>self.segmentEditorWidget.show()</li>
          <li>self.segmentEditorLayout.addWidget(self.segmentEditorWidget)       </li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It is generally a bad idea to store node pointers as member variables. In modules, nodes should be kept track of using references: set node reference from parameter node when creating / selecting on UI, get as referenced node from parameter node when accessing. I know you didn’t implement the module but changing this could fix the crash.</p>
<aside class="quote no-group" data-username="rbumm" data-post="3" data-topic="26075">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>seems to be single-use only</p>
</blockquote>
</aside>
<p>Not sure I understand. The Reload button is supposed to be used while you develop the module, to update the code of the module so you can test it as you go with the implementation. What do you use it for?</p>

---

## Post #5 by @rbumm (2022-11-04 16:44 UTC)

<p>Will try that, thank you.</p>
<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="26075">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>The Reload button is supposed to be used while you develop the module</p>
</blockquote>
</aside>
<p>absolutely, I am aware of that. Probably best to implement a “Reset” button to clear the segmentation.<br>
But this will probably not solve the crash tendency during writing this portion of code, so it would be good to find the reason.</p>

---

## Post #6 by @lassoan (2022-11-05 20:52 UTC)

<p>This is definitely incorrect:</p>
<pre><code class="lang-python">self.segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
self.segmentEditorNode.SetSingletonTag("CIP_Calibration")
</code></pre>
<p>The problem is that after reload you’ll end up with having multiple singleton nodes in the scene with the same singleton tag, which may have unforeseeable consequences, even a crash. The correct usage would be to first try to get the singleton node from the scene and if it does not exist then add it, as it is done here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/62cb2f3d2e38f791f84069c8e5e93e7fdfa72158/Modules/Scripted/SegmentEditor/SegmentEditor.py#L79-L85">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/62cb2f3d2e38f791f84069c8e5e93e7fdfa72158/Modules/Scripted/SegmentEditor/SegmentEditor.py#L79-L85" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/62cb2f3d2e38f791f84069c8e5e93e7fdfa72158/Modules/Scripted/SegmentEditor/SegmentEditor.py#L79-L85" target="_blank" rel="noopener">Slicer/Slicer/blob/62cb2f3d2e38f791f84069c8e5e93e7fdfa72158/Modules/Scripted/SegmentEditor/SegmentEditor.py#L79-L85</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="79" style="counter-reset: li-counter 78 ;">
          <li>segmentEditorSingletonTag = "SegmentEditor"</li>
          <li>segmentEditorNode = slicer.mrmlScene.GetSingletonNode(segmentEditorSingletonTag, "vtkMRMLSegmentEditorNode")</li>
          <li>if segmentEditorNode is None:</li>
          <li>    segmentEditorNode = slicer.mrmlScene.CreateNodeByClass("vtkMRMLSegmentEditorNode")</li>
          <li>    segmentEditorNode.UnRegister(None)</li>
          <li>    segmentEditorNode.SetSingletonTag(segmentEditorSingletonTag)</li>
          <li>    segmentEditorNode = slicer.mrmlScene.AddNode(segmentEditorNode)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Nevertheless, we should implement safeguards against the incorrect API use (e.g., prevent changing the singleton tag to a tag that already exists in the scene), and see if we can add some extra checks to prevent the crash.</p>

---

## Post #7 by @rbumm (2022-11-05 21:44 UTC)

<p>Good catch <a class="mention" href="/u/lassoan">@lassoan</a>. This, in combination with not deleting the SingletonNode in cleanup(), solved it.<br>
See <a href="https://github.com/acil-bwh/SlicerCIP/commit/a6f71e19b399547a542a8f3eb276835ebc42844f">a6f71e1</a></p>

---

## Post #8 by @lassoan (2022-11-06 04:14 UTC)

<p>Thank you <a class="mention" href="/u/rbumm">@rbumm</a>, your fix looks good. I’ve pushed a <a href="https://github.com/Slicer/Slicer/commit/c66b8a1c84b6bb7e0fd7b57905efae2857245b4f">commit</a> with an additional null-pointer check in Slicer core that avoids this crash, even if the Slicer API is misused.</p>

---

## Post #9 by @cpinter (2022-11-06 16:23 UTC)

<p>Nice, simpler than what I suggested. Still, I consider storing node pointers in member variables in Python a big risk, but a quick fix is better than no fix. Thanks <a class="mention" href="/u/lassoan">@lassoan</a></p>

---
