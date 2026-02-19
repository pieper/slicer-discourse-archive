---
topic_id: 23588
title: "Optimizing Performance Of Events When Clearing Nodes"
date: 2022-05-25
url: https://discourse.slicer.org/t/23588
---

# Optimizing performance of events when clearing nodes

**Topic ID**: 23588
**Date**: 2022-05-25
**URL**: https://discourse.slicer.org/t/optimizing-performance-of-events-when-clearing-nodes/23588

---

## Post #1 by @jamesobutler (2022-05-25 16:06 UTC)

<p>I often have about 100 hundred volumes loaded into the scene with corresponding segmentations for each of those volumes. When clearing nodes I’ve observed varying performance based on how many times the current selection in a qMRMLNodeComboBox keeps updating. This is because when a qMRMLNodeComboBox’s current selection is removed from the scene, it selects the last available index in the model and processes that update change to the widgets involved. This additional processing can add up if I happen to be clearing nodes where the current node selection in the combobox is the one being removed.</p>
<p>A specific example is the volume node comboboxes part of slice viewers. If I I’m removing a set of volumes nodes in the scene where the order corresponds to the current selection, then it can result in a flashing effect as the current selection is removed, the last index is selected, the new volume is shown in the slice viewer, then the new selection is removed, the last index is selected again, a new volume is shown in the slice viewer, etc… This additional processing happens as well for all other node comboboxes such as the Master Volume node combobox in the Segment Editor module.</p>
<p>Has there been discussions in the past about how best to handle unnecessary updates like this? I know it is standard behavior for a QComboBox to select the last index when the current selection is removed, but this increases processing if there are events tied to the index being changed. If a volume node is selected in various qMRMLNodeComboBoxes across various modules, then when that volume is removed it will trigger updates across all of those modules that I might not care to process. Maybe I want a “None” type selection when the current selection is removed.</p>

---

## Post #2 by @jamesobutler (2022-05-25 16:55 UTC)

<p>Things that I have played around with is when batch removing a set of volumes in the scene I call <code>blockSignals(True)</code> on the qMRMLNodeComboBoxes in the slice viewers and in the SegmentEditor module and then at the end call <code>blockSignals(False)</code> to reset the state and then call a single update for the selection I want at the end of the remove node process.</p>
<p>This is a targeted approach, but doesn’t find all the places that might be processing updates with new volume selections during the batch removal of volume nodes.</p>
<p>I’m calling the individual <code>slicer.mrmlScene.RemoveNode(volumeNode)</code>, but maybe there could be a <code>RemoveNodes</code> method available to use that would process the list, but only trigger a single update for each of the relevant qMRMLNodeComboBoxes.</p>

---

## Post #3 by @mau_igna_06 (2022-05-25 17:21 UTC)

<p>Could use your approach finding all mrmlNodeComboBoxes with mainWindow().findChildren(…) ?</p>

---

## Post #4 by @lassoan (2022-05-25 17:36 UTC)

<p>Do you switch the scene into batch processing state when you remove the nodes?</p>
<pre><code class="lang-auto">scene-&gt;StartState(vtkMRMLScene::BatchProcessState);
...
(many changes in the scene)
...
scene-&gt;EndState(vtkMRMLScene::BatchProcessState);
</code></pre>

---

## Post #5 by @jamesobutler (2022-05-25 17:54 UTC)

<p>I did not know about the <code>vtkMRMLScene::BatchProcessState</code> so I have not been using that. I just tried putting it around my batch clearing of volume and segmentation nodes method and can confirm I see it working by not processing slice view updates, but my profiling is still indicating multiple calls of <code>masterVolumeNodeChanged</code> coming from Segment Editor stuff that is cumulatively about 25% of the time to clear.</p>
<p>What does this BatchProcessState specifically prevent? Just visual changes in the slice views? Or other mrml objects such as qMRMLNodeComboBoxes in various modules from triggering multiple times during batch processing.</p>

---

## Post #6 by @pieper (2022-05-25 18:02 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> definitely try the batch process mode, it was designed exactly for the use case you describe.  Not just comboboxes but other updates like views are deferred until after the bulk operation is done.</p>

---

## Post #7 by @lassoan (2022-05-25 18:07 UTC)

<p>Every module, logic, widget, etc. can decide how to utilize scene state information. The idea is that while the scene is in batch processing state, software components can ignore scene changes and do a full update when batch processing is finished.</p>
<p>It seems that the Segment Editor could do some more optimization based on the scene state. There are a number of places where such optimizations are done (see for example qSlicerMarkupsModuleWidget) that you can use as examples.</p>

---

## Post #8 by @jamesobutler (2022-05-25 18:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="23588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It seems that the Segment Editor could do some more optimization based on the scene state. There are a number of places where such optimizations are done (see for example qSlicerMarkupsModuleWidget) that you can use as examples.</p>
</blockquote>
</aside>
<p>Thanks for pointing this out. I will try some changes to add the check for batch processing in some more places and will issue a PR if I’m successful.</p>

---

## Post #9 by @jamesobutler (2022-05-25 21:45 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Is there a method for making sure the widgets get updated at the end of batch processing? When trying it out with the Markups module (qSlicerMarkupsModuleWidget) as the currently selected module I’m observing that the qMRMLSubjectHierarchyTreeView isn’t updated when the batch processing state is ended. Is this normal behavior or a bug? I would have expected that when BatchProcessingState is ended that the markups table would show the node for “First” and “Fourth”.</p>
<pre data-code-wrap="python"><code class="lang-python">first=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "First")
second=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "Second")
third=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "Third")
slicer.mrmlScene.StartState(slicer.mrmlScene.BatchProcessState)

for node in [third, second]:
  slicer.mrmlScene.RemoveNode(node)

slicer.mrmlScene.EndState(slicer.mrmlScene.BatchProcessState)
fourth=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "Fourth")

</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1912791279d990898fabd4c1ba4db1e28679f37.png" data-download-href="/uploads/short-url/rCn8VyfnJGqTds57KzSS8MhxArl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1912791279d990898fabd4c1ba4db1e28679f37_2_690x366.png" alt="image" data-base62-sha1="rCn8VyfnJGqTds57KzSS8MhxArl" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1912791279d990898fabd4c1ba4db1e28679f37_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1912791279d990898fabd4c1ba4db1e28679f37_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1912791279d990898fabd4c1ba4db1e28679f37_2_1380x732.png 2x" data-dominant-color="8F8F96"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1020 74.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @jamesobutler (2022-05-25 22:29 UTC)

<p>The code above where the qMRMLSubjectHierarchyTreeView isn’t updated upon ending the BatchProcessingState produces the following errors.</p>
<pre><code class="lang-auto">[DEBUG][Qt] 25.05.2022 18:24:45 [] (unknown:0) - Python console user input: slicer.mrmlScene.EndState(slicer.mrmlScene.BatchProcessState)
[ERROR][VTK] 25.05.2022 18:24:45 [vtkMRMLSubjectHierarchyNode (0000028BAFF77F30)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2114) - GetItemDataNode: Failed to find subject hierarchy item by ID 8
[ERROR][VTK] 25.05.2022 18:24:45 [vtkMRMLSubjectHierarchyNode (0000028BAFF77F30)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2827) - GetItemParent: Failed to find subject hierarchy item by ID 8
[ERROR][VTK] 25.05.2022 18:24:45 [vtkMRMLSubjectHierarchyNode (0000028BAFF77F30)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2114) - GetItemDataNode: Failed to find subject hierarchy item by ID 9
[ERROR][VTK] 25.05.2022 18:24:45 [vtkMRMLSubjectHierarchyNode (0000028BAFF77F30)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2827) - GetItemParent: Failed to find subject hierarchy item by ID 9
</code></pre>
<p>Looks like I’m possibly running into known issues as written up in <a href="https://github.com/Slicer/Slicer/issues/6006" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/issues/6006</a> and <a href="https://github.com/Slicer/Slicer/issues/4650" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/issues/4650</a>.</p>
<p>Using the workaround mentioned in <a href="https://github.com/Slicer/Slicer/issues/6006" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/issues/6006</a>, I can get the subject hierarchy in the Markups module to refresh.</p>
<blockquote>
<p>Force subject hierarchy tree rebuild by temporarily switching to scene import mode:</p>
<pre data-code-wrap="python"><code class="lang-python">slicer.mrmlScene.StartState(slicer.vtkMRMLScene.ImportState)
slicer.mrmlScene.EndState(slicer.vtkMRMLScene.ImportState)
</code></pre>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c67e244b21c8c0a47be0d32802f6cbe49e783b84.png" data-download-href="/uploads/short-url/sjWNojt9fM8BoCyDEhRCtFiTMy0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c67e244b21c8c0a47be0d32802f6cbe49e783b84.png" alt="image" data-base62-sha1="sjWNojt9fM8BoCyDEhRCtFiTMy0" width="690" height="366" data-dominant-color="8F8F96"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1020 71.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @lassoan (2022-05-26 03:10 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="9" data-topic="23588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Is there a method for making sure the widgets get updated at the end of batch processing?</p>
</blockquote>
</aside>
<p>All the classes that may ignore updates in batch processing mode must observe the scene and do a full update when batch processing is finished.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="9" data-topic="23588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I’m observing that the qMRMLSubjectHierarchyTreeView isn’t updated when the batch processing state is ended</p>
</blockquote>
</aside>
<p>Unfortunately, the Subject Hierarchy scene model and widget were not developed with having batch processing mode in mind. It was a huge hole in the design and implementation. The code was later fixed up, so most of the major issues are fixed, but since it was just an afterthought and the implementation is quite complex, there may be still a few errors.</p>

---

## Post #12 by @jamesobutler (2022-05-26 15:30 UTC)

<p>Is setting the BatchProcessState encouraged to be used as global state where you turn it on, go do a bunch of things, and then turn it off (see <code>functionThatDoesAllThings</code>)? Or should it be turned on/off only around the individual action (see <code>function1</code>)? The latter requires more sprinkling of the Start/End state methods.</p>
<p>In the case below when running <code>functionThatDoesAllThings</code> I would expect <code>function2</code> actions to be skipped over, but it seems as though the batch process state would have been ended at the end of <code>function1</code>. In my own code I was setting the state like in <code>functionThatDoesAllThings</code>, but seems like in some SubjectHierarchy related code it does it like <code>function1</code>.</p>
<pre><code class="lang-python">def function1():
    slicer.mrmlScene.StartState(slicer.mrmlScene.BatchProcessState)
    # do some things here
    slicer.mrmlScene.EndState(slicer.mrmlScene.BatchProcessState)

def function2():
    if slicer.mrmlScene.IsBatchProcessing():
        return
    # do some things here

def functionThatDoesAllThings():
    slicer.mrmlScene.StartState(slicer.mrmlScene.BatchProcessState)
    function1()
    function2()
    function1()
    slicer.mrmlScene.EndState(slicer.mrmlScene.BatchProcessState)
</code></pre>

---

## Post #13 by @pieper (2022-05-26 16:12 UTC)

<p><code>vtkMRMLScene::StartState</code> is actually pushing on a stack, so the final <code>EndState</code> call should invoke the event as long as the starts and ends are paired.</p>

---

## Post #14 by @jamesobutler (2022-05-26 16:19 UTC)

<p>Ah, yes I see that. Seems like I can use it around smaller methods or even in methods that do lots of subtasks.</p>
<pre><code class="lang-auto">def function1():
    slicer.mrmlScene.StartState(slicer.mrmlScene.BatchProcessState)
    print("Function 1 actions")
    slicer.mrmlScene.EndState(slicer.mrmlScene.BatchProcessState)

def function2():
    if slicer.mrmlScene.IsBatchProcessing():
        return
    print("Function 2 actions")
    # do some things here

def functionThatDoesAllThings():
    slicer.mrmlScene.StartState(slicer.mrmlScene.BatchProcessState)
    function1()
    function2()
    function1()
    slicer.mrmlScene.EndState(slicer.mrmlScene.BatchProcessState)
</code></pre>
<pre><code class="lang-auto">&gt;&gt;&gt; functionThatDoesAllThings()
Function 1 actions
Function 1 actions
</code></pre>

---

## Post #15 by @jamesobutler (2022-05-26 16:20 UTC)

<p>Reviewing the other mrml states:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/80869f11bc507ddf60449014c3c11878cd4d9068/Libs/MRML/Core/vtkMRMLScene.h#L591-L600">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/80869f11bc507ddf60449014c3c11878cd4d9068/Libs/MRML/Core/vtkMRMLScene.h#L591-L600" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/80869f11bc507ddf60449014c3c11878cd4d9068/Libs/MRML/Core/vtkMRMLScene.h#L591-L600" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/80869f11bc507ddf60449014c3c11878cd4d9068/Libs/MRML/Core/vtkMRMLScene.h#L591-L600</a></h4>



    <pre class="onebox">      <code class="lang-h">
        <ol class="start lines" start="591" style="counter-reset: li-counter 590 ;">
            <li>enum StateType</li>
            <li>  {</li>
            <li>  BatchProcessState = 0x0001,</li>
            <li>  CloseState = 0x0002 | BatchProcessState,</li>
            <li>  ImportState = 0x0004 | BatchProcessState,</li>
            <li>  RestoreState = 0x0008 | BatchProcessState,</li>
            <li>  SaveState = 0x0010,</li>
            <li>  UndoState = 0x0020,</li>
            <li>  RedoState = 0x0040,</li>
            <li>  };</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It seems like some of my actions of batch processing nodes to be removed from the scene or added to the scene isn’t quite like CloseState and ImportState which appear to have been desired with clearing and importing a mrml scene. I’m doing some batch actions outside of mrml file use. It seems like in some places in the code there are checks for <code>isClosing()</code> and <code>isImporting()</code> which wouldn’t return true if Starting/Ending the BatchProcess state directly.</p>

---

## Post #16 by @jamesobutler (2022-05-26 17:06 UTC)

<aside class="quote quote-modified" data-post="10" data-topic="23588">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/optimizing-performance-of-events-when-clearing-nodes/23588/10">Optimizing performance of events when clearing nodes</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    The code above where the qMRMLSubjectHierarchyTreeView isn’t updated upon ending the BatchProcessingState produces the following errors. 
[DEBUG][Qt] 25.05.2022 18:24:45 [] (unknown:0) - Python console user input: slicer.mrmlScene.EndState(slicer.mrmlScene.BatchProcessState)
[ERROR][VTK] 25.05.2022 18:24:45 [vtkMRMLSubjectHierarchyNode (0000028BAFF77F30)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2114) - GetItemDataNode: Failed to find subject hierarchy item by ID 8
[ERROR][VTK]…
  </blockquote>
</aside>

<p>^ I’ve issued the following PR with an attempt to fix this update issue of the subject hierarchy view.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6394">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6394" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6394" target="_blank" rel="noopener nofollow ugc">BUG: Fix subject hierarchy table showing nodes removed during batch processing</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jamesobutler:batch-processing-fixes</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-05-26" data-time="17:04:49" data-timezone="UTC">05:04PM - 26 May 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="1 commits changed 3 files with 2 additions and 60 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6394/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+2</span>
            <span class="removed">-60</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Originally reported at https://discourse.slicer.org/t/optimizing-performance-of-<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6394" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">events-when-clearing-nodes/23588/9.

Code to replicate original issue
```python
slicer.util.selectModule("Data")
first = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "First")
second = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "Second")
third = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "Third")
slicer.mrmlScene.StartState(slicer.mrmlScene.BatchProcessState)

for node in [third, second]:
  slicer.mrmlScene.RemoveNode(node)

slicer.mrmlScene.EndState(slicer.mrmlScene.BatchProcessState)
fourth = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "Fourth")

```
After running the above code:

| Slicer 5.1.0-2022-05-24 | This PR |
|----------|---------|
|![image](https://user-images.githubusercontent.com/15837524/170538309-2f3b580c-3b5a-48ac-b93b-4741fd046653.png)|![image](https://user-images.githubusercontent.com/15837524/170538404-fb846e94-86da-4b85-a594-704025df1115.png)|

I have removed `updateFromSubjectHierarchy` because of it's single usage in Slicer core being removed. This could be reverted if it is desired even though it is code not being used by core. `onMRMLSceneEndBatchProcess` was switched to using the full `rebuildFromSubjectHierarchy` as when removing nodes during batch processing it was not removing them from the widget when batch processing state was ended.

When using Slicer 5.1.0-2022-05-24 and the subject hierarchy widget not updating it would produce many errors of the following when the batch processing state was ended:
```
[DEBUG][Qt] 26.05.2022 13:03:25 [] (unknown:0) - Python console user input: slicer.mrmlScene.EndState(slicer.mrmlScene.BatchProcessState)
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2114) - GetItemDataNode: Failed to find subject hierarchy item by ID 8
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2827) - GetItemParent: Failed to find subject hierarchy item by ID 8
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2114) - GetItemDataNode: Failed to find subject hierarchy item by ID 9
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2827) - GetItemParent: Failed to find subject hierarchy item by ID 9
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2114) - GetItemDataNode: Failed to find subject hierarchy item by ID 8
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2827) - GetItemParent: Failed to find subject hierarchy item by ID 8
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2114) - GetItemDataNode: Failed to find subject hierarchy item by ID 8
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2827) - GetItemParent: Failed to find subject hierarchy item by ID 8
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2114) - GetItemDataNode: Failed to find subject hierarchy item by ID 8
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2827) - GetItemParent: Failed to find subject hierarchy item by ID 8
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2114) - GetItemDataNode: Failed to find subject hierarchy item by ID 8
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2827) - GetItemParent: Failed to find subject hierarchy item by ID 8
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2114) - GetItemDataNode: Failed to find subject hierarchy item by ID 9
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2827) - GetItemParent: Failed to find subject hierarchy item by ID 9
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2114) - GetItemDataNode: Failed to find subject hierarchy item by ID 9
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2827) - GetItemParent: Failed to find subject hierarchy item by ID 9
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2114) - GetItemDataNode: Failed to find subject hierarchy item by ID 9
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2827) - GetItemParent: Failed to find subject hierarchy item by ID 9
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2114) - GetItemDataNode: Failed to find subject hierarchy item by ID 9
[ERROR][VTK] 26.05.2022 13:03:25 [vtkMRMLSubjectHierarchyNode (000002CDB734A7B0)] (D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2827) - GetItemParent: Failed to find subject hierarchy item by ID 9
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #17 by @jamesobutler (2022-05-26 21:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="23588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It seems that the Segment Editor could do some more optimization based on the scene state. There are a number of places where such optimizations are done (see for example qSlicerMarkupsModuleWidget) that you can use as examples.</p>
</blockquote>
</aside>
<p>I’ve posted the following PR that addresses this issue of some unnecessary SegmentEditor signaling occurring during batch removing a bunch of volume nodes.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6395">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6395" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6395" target="_blank" rel="noopener nofollow ugc">ENH: Optimize processing Segment Editor updates during Batch Processing</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jamesobutler:batch-processing-segment-editor</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-05-26" data-time="21:56:44" data-timezone="UTC">09:56PM - 26 May 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 35 additions and 1 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6395/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+35</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Originally discussed in https://discourse.slicer.org/t/optimizing-performance-of<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6395" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">-events-when-clearing-nodes/23588/5. A `masterVolumeNodeChanged` call in SegmentEditor was 25% of the time when clearing a set of volume nodes from the scene in some custom code that I have.

For example when removing volume nodes, this can trigger a change of the current Master Volume node specification in the Segment Editor module if the current volume node is removed from the scene. When this happens over and over during batch processing there was frequent updating of the master volume node for SegmentEditor logic which can be an expensive operation, especially the masterVolumeNodeChanged call for SegmentEditorThresholdEffect.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #18 by @lassoan (2022-05-27 01:45 UTC)

<p>Thank you for all your work on this. I’ve already reviewed one of your pull request and will have a look at the others, too.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="23588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>100 hundred volumes loaded into the scene with corresponding segmentations for each of those volumes.</p>
</blockquote>
</aside>
<p>We haven’t had any use case in mind that would involve having hundreds of volumes and segmentations in the scene. Having a large number of nodes would cause performance and GUI usability issues at many other places, too. Can you tell a bit more about your application? Why do you have so many volumes?</p>
<p>Have you considered storing them in sequences (just pulling into the main scene those that you actually need) or merging these nodes into fewer nodes (e.g., reconstruct volumes from them, or put them into a single textured model node, or dynamically loading them into the scene when they are actually needed, …)?</p>

---

## Post #19 by @jamesobutler (2022-05-27 02:22 UTC)

<p>Typically it represents volumes for a single timepoint of a cohort of mice. Where there is 25-50 mice in a cohort. Typically there is a 3D B-Mode ultrasound as a reference background for some other supporting mode (think like Color Flow, Shear Wave Elastography, M-Mode, etc).</p>
<p>You could load in a few volumes for a certain number of mice to keep the number of nodes down, but most of the researchers just load in all the data for that timepoint that they need to segment.</p>
<p>We have some custom stuff to improve workflows where we identify related volumes based on our metadata to appropriately pair volumes. So we don’t have a lot of combo boxes with 100s of selections to choose from. A primary volume with a subject hierarchy is used to organize nodes so we can show the relevant nodes when needed.</p>

---
