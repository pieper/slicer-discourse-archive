# Data node display nodes not maintained when creating a sequence

**Topic ID**: 28146
**Date**: 2023-03-02
**URL**: https://discourse.slicer.org/t/data-node-display-nodes-not-maintained-when-creating-a-sequence/28146

---

## Post #1 by @jamesobutler (2023-03-02 21:10 UTC)

<p>I’ve been having some issues creating a sequence where the display nodes of the given data nodes that I’m adding are not being maintained. I have a set of loaded 2D images where I have customized each of their display volumes with their appropriate colormap, window/level min/max and lower/upper threshold. However when I select one of my volumes to add as a data node to my sequence node I observe that all my display customizations have been lost.</p>
<p>Am I using sequences incorrectly? Or is the expectation to set up the display for each data node after it has been added to the sequence?</p>
<p>Below is some sample code of loading 2 MRHead volumes and customizing one of them, but when selecting the SequenceNode to show in the slice viewers I observe that the display customizations I did at the beginning were lost. I also observe this when selecting the SequenceNode in the Volumes module and playing the sequence as I don’t see the lower threshold value changing.</p>
<pre><code class="lang-python"># Load sample volume
import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
mrHead = sampleDataLogic.downloadMRHead()
mrHead2 = sampleDataLogic.downloadMRHead()
mrHead2.GetDisplayNode().SetAndObserveColorNodeID("vtkMRMLColorTableNodeRed")
mrHead2.GetDisplayNode().ApplyThresholdOn()
mrHead2.GetDisplayNode().SetLowerThreshold(79)

sequence_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode", "MySequenceNode")
sequence_node.SetDataNodeAtValue(mrHead, "0")
frame_vol_0 = sequence_node.GetNthDataNode(0)
frame_vol_0.GetDisplayNode()
sequence_node.SetDataNodeAtValue(mrHead2, "1")
frame_vol_1 = sequence_node.GetNthDataNode(1)
frame_vol_1.GetDisplayNode()

browser_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceBrowserNode", "MyBrowserNode")
browser_node.AddSynchronizedSequenceNode(sequence_node)
</code></pre>

---

## Post #2 by @mikebind (2023-03-02 22:14 UTC)

<p>I think what is probably happening here is that display nodes are not “attached” to the scalar volume node as it is added into the sequence.  Instead, browsing through the sequence node only copies the image data stored in the sequence into the scalar volume proxy node associated with the sequence.  That proxy node is then displayed with the display node associated with the proxy node rather than with the display node associated with the scalar volume at the point when it was added to the sequence.  I think you can probably create a sequence of display nodes and set the scalar volume proxy node to observe the proxy display node associated with the sequence of display nodes you want to run through.  That way, when you step through the sequence browser, both the scalar volume node and the display node associated with it would be updated with the next value in each sequence.  I’ve never done this for display nodes, but this is the way it works for transform nodes.  For example, if you have a sequence of transforms to apply to a sequence of images, both need to be synchronized under the same sequence browser node, and the image proxy volume needs to have as its parent transform the proxy node of the transform sequence.</p>

---

## Post #3 by @jamesobutler (2023-03-02 23:18 UTC)

<p>From reading about the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html#basic-mrml-node-types" rel="noopener nofollow ugc">Basic MRML node types</a>, it seems like Sequence nodes only store a list of “Data nodes”. A “Data node” is a Volume/Model/Segmentation/Markups/Transform/Text/Table, however a display node is a separate category of MRML node.</p>
<p>I have a situation of a sequence of volume nodes where I have percentage based calculated Window/Levels and Threshold values for each of the volumes nodes. It seems like currently I would have to apply the same Window/Level and Threshold for each index in the sequence.</p>

---

## Post #4 by @pieper (2023-03-02 23:40 UTC)

<p>Another option is just to listen for events from the sequence browser node and update the volume display with your custom properties.  This is basically what is done in <a href="https://github.com/pieper/SlicerAnimator/blob/master/Animator/Animator.py">the Animator</a>.</p>

---

## Post #5 by @lassoan (2023-03-03 05:25 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="28146">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>is the expectation to set up the display for each data node after it has been added to the sequence?</p>
</blockquote>
</aside>
<p>Yes. It is up to you how you want to display the sequence. Probably a new display node is created by default but if you want you can copy the display node content of one of the source data nodes. You can also put the display node into a sequence - if you want display properties to change in time, too.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="28146">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>From reading about the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html#basic-mrml-node-types">Basic MRML node types</a>, it seems like Sequence nodes only store a list of “Data nodes”.</p>
</blockquote>
</aside>
<p>There is no such limitation. The beauty of the sequences infrastructure that it can work with any node type (not just data nodes but display nodes, transforms, views, etc.). The only requirement is that the class must implement copy content method.</p>
<aside class="quote no-group" data-username="mikebind" data-post="2" data-topic="28146">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I’ve never done this for display nodes, but this is the way it works for transform nodes</p>
</blockquote>
</aside>
<p>Yes, it works well. You can select a display node as proxy node, start recording, modify display settings, stop recording, and then you can click play to see all your display changes.</p>

---

## Post #6 by @jamesobutler (2023-03-03 15:23 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="28146">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There is no such limitation. The beauty of the sequences infrastructure that it can work with any node type (not just data nodes but display nodes, transforms, views, etc.). The only requirement is that the class must implement copy content method.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I guess I was confused by the term “data node” mentioned in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html#sequences" rel="noopener nofollow ugc">sequences documentation</a> and how the term “data node” appears to exclude Display/Storage/View/Plot/SubjectHierarchy nodes as described in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html#basic-mrml-node-types" rel="noopener nofollow ugc">Basic MRML node types</a>.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="28146">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can also put the display node into a sequence - if you want display properties to change in time, too.</p>
</blockquote>
</aside>
<p>Below is my attempt at putting the display node into a sequence. However I’m observing that the sequence is not observing the change appropriately. I am doing this in code because I can’t seem to find a GUI method for setting up a display sequence.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc08168e051c2f7e962a30a8c4d8af957239465e.png" alt="image" data-base62-sha1="qPp5LZ86MCrAI0ZcZQcxo5l7sce" width="634" height="316"></p>
<pre data-code-wrap="python"><code class="lang-python"># Load sample volume
import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
mrHead = sampleDataLogic.downloadMRHead()
mrHead2 = sampleDataLogic.downloadMRHead()
mrHead2.GetDisplayNode().SetAndObserveColorNodeID("vtkMRMLColorTableNodeRed")
mrHead2.GetDisplayNode().ApplyThresholdOn()
mrHead2.GetDisplayNode().SetLowerThreshold(79)

sequence_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode", "MySequenceNode")
sequence_node.SetDataNodeAtValue(mrHead, "0")
sequence_node.SetDataNodeAtValue(mrHead2, "1")

sequence_display_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode", "MySequenceDisplayNode")
sequence_display_node.SetDataNodeAtValue(mrHead.GetDisplayNode(), "0")
sequence_display_node.SetDataNodeAtValue(mrHead2.GetDisplayNode(), "1")

browser_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceBrowserNode", "MyBrowserNode")
browser_node.AddSynchronizedSequenceNode(sequence_node)
browser_node.AddSynchronizedSequenceNode(sequence_display_node)
volume_proxy_node = browser_node.GetProxyNode(sequence_node)
display_proxy_node = browser_node.GetProxyNode(sequence_display_node)
volume_proxy_node.SetAndObserveDisplayNodeID(display_proxy_node.GetID())

slicer.modules.sequences.toolBar().setActiveBrowserNode(browser_node)
</code></pre>

---

## Post #7 by @jamesobutler (2023-03-03 17:59 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="6" data-topic="28146">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>However I’m observing that the sequence is not observing the change appropriately.</p>
</blockquote>
</aside>
<p>I was wrong here. Things are working appropriately. I confused myself by not doing <code>slicer.util.setSliceViewerLayers(background=volume_proxy_node)</code> at the end of the code snippet I provided in my last comment so I wasn’t actually looking at the volume node I was thinking. I had set the browser node to be active, but I hadn’t shown it yet in the slice views.</p>

---

## Post #8 by @jamesobutler (2023-03-03 18:36 UTC)

<p>Actually I’m wrong again. The colormap is updating appropriately for each index, but the Window/Level and Threshold properties are not appropriately changing in the sequence.</p>
<p>After the <code>SetDataNodeAtValue</code> call for a vtkMRMLScalarVolumeDisplayNode, I can confirm that Color node is copied over, but not window/level and not threshold. As seen by the output below produced by the included code in this comment.</p>
<p>Index 0 color node correct: True<br>
Index 0 window/level min correct: False<br>
Index 0 window/level max correct: False<br>
Index 0 LowerThreshold correct: False<br>
Index 0 UpperThreshold correct: False<br>
Index 1 color node correct: True<br>
Index 1 window/level min correct: False<br>
Index 1 window/level max correct: False<br>
Index 1 LowerThreshold correct: False<br>
Index 1 UpperThreshold correct: False</p>
<pre><code class="lang-python"># Load sample volume
import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
mrHead = sampleDataLogic.downloadMRHead()
mrHead.GetDisplayNode().ApplyThresholdOn()
mrHead.GetDisplayNode().SetAutoWindowLevel(False)
mrHead.GetDisplayNode().SetWindowLevelMinMax(10, 120)
min, max = mrHead.GetImageData().GetScalarRange()
mrHead.GetDisplayNode().SetThreshold(0, max)

mrHead2 = sampleDataLogic.downloadMRHead()
mrHead2.GetDisplayNode().SetAndObserveColorNodeID("vtkMRMLColorTableNodeRed")
mrHead2.GetDisplayNode().ApplyThresholdOn()
min, max = mrHead2.GetImageData().GetScalarRange()
mrHead2.GetDisplayNode().SetThreshold(79, max)
mrHead2.GetDisplayNode().ApplyThresholdOn()
mrHead2.GetDisplayNode().SetAutoWindowLevel(False)
mrHead2.GetDisplayNode().SetWindowLevelMinMax(20, 100)

sequence_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode", "MySequenceNode")
sequence_node.SetDataNodeAtValue(mrHead, "0")
sequence_node.SetDataNodeAtValue(mrHead2, "1")

sequence_display_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode", "MySequenceDisplayNode")
sequence_display_node.SetDataNodeAtValue(mrHead.GetDisplayNode(), "0")
sequence_display_node.SetDataNodeAtValue(mrHead2.GetDisplayNode(), "1")
a = sequence_display_node.GetDataNodeAtValue("0")
print(f"Index 0 color node correct: {a.GetColorNodeID() == mrHead.GetDisplayNode().GetColorNodeID()}")
print(f"Index 0 window/level min correct: {a.GetWindowLevelMin() == mrHead.GetDisplayNode().GetWindowLevelMin()}")
print(f"Index 0 window/level max correct: {a.GetWindowLevelMax() == mrHead.GetDisplayNode().GetWindowLevelMax()}")
print(f"Index 0 LowerThreshold correct: {a.GetLowerThreshold() == mrHead.GetDisplayNode().GetLowerThreshold()}")
print(f"Index 0 UpperThreshold correct: {a.GetUpperThreshold() == mrHead.GetDisplayNode().GetUpperThreshold()}")
b = sequence_display_node.GetDataNodeAtValue("1")
print(f"Index 1 color node correct: {b.GetColorNodeID() == mrHead2.GetDisplayNode().GetColorNodeID()}")
print(f"Index 1 window/level min correct: {b.GetWindowLevelMin() == mrHead2.GetDisplayNode().GetWindowLevelMin()}")
print(f"Index 1 window/level max correct: {b.GetWindowLevelMax() == mrHead2.GetDisplayNode().GetWindowLevelMax()}")
print(f"Index 1 LowerThreshold correct: {b.GetLowerThreshold() == mrHead2.GetDisplayNode().GetLowerThreshold()}")
print(f"Index 1 UpperThreshold correct: {b.GetUpperThreshold() == mrHead2.GetDisplayNode().GetUpperThreshold()}")
</code></pre>

---

## Post #9 by @lassoan (2023-03-03 19:02 UTC)

<p>It seems that when <a href="https://github.com/Slicer/Slicer/commit/f88c110430ac818329b2806dbe3e42eeb9e0b503">sequence support was added to most nodes in Slicer core</a> then <code>vtkMRMLScalarVolumeDisplayNode</code> was accidentally missed. This is why <code>vtkMRMLScalarVolumeDisplayNode</code> nodes do not show up in the proxy node selector in the Sequences module.</p>
<p>The fix is to implement <code>CopyContent</code> method. It would be great if you could work on it.</p>

---

## Post #10 by @jamesobutler (2023-03-03 19:41 UTC)

<p>Yes I can look into adding that.</p>
<p>In addition to creating a sequence node of pure vtkMRMLScalarVolumeDisplayNodes, should adding vtkMRMLScalarVolumeNodes as data nodes to a sequence also include copying over their display node if present?</p>

---

## Post #11 by @lassoan (2023-03-03 19:51 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="10" data-topic="28146">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>should adding vtkMRMLScalarVolumeNodes as data nodes to a sequence also include copying over their display node if present?</p>
</blockquote>
</aside>
<p>I don’t recall experiencing issues myself or reported by users about how display node is initialized now, but I assume that things can be always improved.</p>

---

## Post #12 by @ungi (2023-03-04 14:33 UTC)

<p>Recording scalar volume node changes in a sequence is not obviously a reason for automatically recording its display node changes. If I understand your suggestion correctly. E.g. I work with ultrasound sequences. They are replayed often for manual annotations by different users. Each user has different color map preferences and window/level preferences when they work on annotations. If you change the current default behavior, then the display properties recorded during ultrasound recording will be forced on the annotator person by default. We would need to implement a special module that applies the display node set up by the annotator. Or we need to implement a special module that removes display nodes from the recorded nodes during recording.<br>
It seems more intuitive for me to keep the current behavior, when you need to explicitly add the display node to the sequence browser if you want to record display changes too.</p>

---

## Post #13 by @jamesobutler (2023-03-04 21:21 UTC)

<aside class="quote no-group" data-username="ungi" data-post="12" data-topic="28146">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar"> ungi:</div>
<blockquote>
<p>Each user has different color map preferences and window/level preferences when they work on annotations.</p>
</blockquote>
</aside>
<p>In this case are users setting a global colormap and window/level that are applied to all frames in the sequence?</p>
<p>In my case, I have optical luminescent images where it is common for different Window/Levels to be used for each frame in the optical sequence. It was confusing for me to add a single frame which had a set of display settings and then upon adding it to a sequence those settings were lost and things reverted back to some default. I was expecting the “state” of the volume node to remain the same when added to a sequence and that includes both the image data and other supporting nodes like the display node.</p>

---

## Post #14 by @ungi (2023-03-04 21:29 UTC)

<p>Yes, ultrasound sequences are always viewed with the same window/level (and other display) parameters across the whole sequence. So the same tissues always appear similar, regardless of other brighter or darker areas that may appear in subsequent frames around the tissue. It would be quite confusing if we removed the ultrasound from the patient and we saw a medium gray image (looks like tissue) instead of a black frame (air with no tissue echoes).<br>
I always liked this feature of Slicer to detach volumes nodes from their display nodes, so we can use, record, and replay them separately or together based on what the use case demands.</p>

---

## Post #15 by @jamesobutler (2023-03-04 22:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="28146" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It seems that when <a href="https://github.com/Slicer/Slicer/commit/f88c110430ac818329b2806dbe3e42eeb9e0b503" rel="noopener nofollow ugc">sequence support was added to most nodes in Slicer core </a> then <code>vtkMRMLScalarVolumeDisplayNode</code> was accidentally missed. This is why <code>vtkMRMLScalarVolumeDisplayNode</code> nodes do not show up in the proxy node selector in the Sequences module.</p>
<p>The fix is to implement <code>CopyContent</code> method. It would be great if you could work on it.</p>
</blockquote>
</aside>
<p>I have issued the following PR to solve the issue of adding a vtkMRMLScalarVolumeDisplayNode to a sequence and it not copying the Window/Level and Threshold states.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6857">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6857" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6857" target="_blank" rel="noopener nofollow ugc">ENH: Add support of shallow and deep copy to scalar volume display node</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jamesobutler:scalar-display-node-copy-content</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-03-04" data-time="22:14:41" data-timezone="UTC">10:14PM - 04 Mar 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="2 commits changed 4 files with 144 additions and 12 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6857/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+144</span>
            <span class="removed">-12</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This is a followup to https://github.com/Slicer/Slicer/commit/f88c110430ac818329<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6857" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">b2806dbe3e42eeb9e0b503.

See https://discourse.slicer.org/t/data-node-display-nodes-not-maintained-when-creating-a-sequence/28146/9?u=jamesobutler

Here's the script I was using for testing.

```python
# Load sample volume
import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
mrHead = sampleDataLogic.downloadMRHead()
mrHead.GetDisplayNode().ApplyThresholdOn()
mrHead.GetDisplayNode().SetAutoWindowLevel(False)
mrHead.GetDisplayNode().SetWindowLevelMinMax(10, 120)
min, max = mrHead.GetImageData().GetScalarRange()
mrHead.GetDisplayNode().SetThreshold(0, max)

mrHead2 = sampleDataLogic.downloadMRHead()
mrHead2.GetDisplayNode().SetAndObserveColorNodeID("vtkMRMLColorTableNodeRed")
mrHead2.GetDisplayNode().ApplyThresholdOn()
min, max = mrHead2.GetImageData().GetScalarRange()
mrHead2.GetDisplayNode().SetThreshold(79, max)
mrHead2.GetDisplayNode().ApplyThresholdOn()
mrHead2.GetDisplayNode().SetAutoWindowLevel(False)
mrHead2.GetDisplayNode().SetWindowLevelMinMax(20, 100)

sequence_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode", "MySequenceNode")
sequence_node.SetDataNodeAtValue(mrHead, "0")
sequence_node.SetDataNodeAtValue(mrHead2, "1")

sequence_display_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode", "MySequenceDisplayNode")
sequence_display_node.SetDataNodeAtValue(mrHead.GetDisplayNode(), "0")
sequence_display_node.SetDataNodeAtValue(mrHead2.GetDisplayNode(), "1")

browser_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceBrowserNode", "MyBrowserNode")
browser_node.AddSynchronizedSequenceNode(sequence_node)
browser_node.AddSynchronizedSequenceNode(sequence_display_node)
volume_proxy_node = browser_node.GetProxyNode(sequence_node)
display_proxy_node = browser_node.GetProxyNode(sequence_display_node)
volume_proxy_node.SetAndObserveDisplayNodeID(display_proxy_node.GetID())

slicer.modules.sequences.toolBar().setActiveBrowserNode(browser_node)
slicer.util.setSliceViewerLayers(background=volume_proxy_node)
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
