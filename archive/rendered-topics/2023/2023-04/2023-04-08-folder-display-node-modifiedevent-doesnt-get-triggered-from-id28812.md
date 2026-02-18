# Folder display node ModifiedEvent doesn't get triggered from parent

**Topic ID**: 28812
**Date**: 2023-04-08
**URL**: https://discourse.slicer.org/t/folder-display-node-modifiedevent-doesnt-get-triggered-from-parent/28812

---

## Post #1 by @danpak94 (2023-04-08 19:20 UTC)

<p>Hello,</p>
<p>I was trying to implement a callback for my folder display node, but it seems like it’s not triggering ModifiedEvent when I change the display of the parent folder.</p>
<p>For example, let’s say I have the following subject hierarchy:</p>
<p>FolderA<br>
|---- FolderB<br>
|---- Segmentation</p>
<pre><code class="lang-auto">shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
folderDisplayNode = shNode.GetItemDataNode(shNode.GetItemByName("FolderB"))
segmentationNode = shNode.GetItemDataNode(shNode.GetItemByName("Segmentation"))

def test_callback(caller, event):
    print('in here!', caller.GetName())

test = slicer.util.VTKObservationMixin()
test.addObserver(folderDisplayNode, vtk.vtkCommand.ModifiedEvent, test_callback)
test.addObserver(segmentationNode.GetDisplayNode(), vtk.vtkCommand.ModifiedEvent, test_callback)
</code></pre>
<p>When I change FolderA visibility, it triggers only Segmentation display node’s ModifiedEvent. I would expect it to trigger the FolderB display ModifiedEvent as well. Could you please point me to how I can fix this issue?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2023-04-11 05:07 UTC)

<p>A node’s modified event is only invoked if the node is modified. You can observe the node’s <code>DisplayModified</code> event if you want to get notified about any display node changes:</p>
<pre><code class="lang-python">test.addObserver(segmentationNode, slicer.vtkMRMLDisplayableNode.DisplayModifiedEvent, test_callback)
</code></pre>

---

## Post #3 by @danpak94 (2023-04-11 11:11 UTC)

<p>Hello,</p>
<p>My problem was actually more associated with <code>folderDisplayNode</code>, which is a <code>vtkMRMLDisplayNode</code>, not a <code>vtkMRMLDisplayabableNode</code>. I just added this line (<code>test.addObserver(segmentationNode.GetDisplayNode(), vtk.vtkCommand.ModifiedEvent, test_callback</code>) to demonstrate that changing the <strong>parent</strong> folder visibility seems to call <code>segmentationNode.DisplayNode()</code>'s  <code>ModifiedEvent</code>, but not <code>folderDisplayNode</code>’s <code>ModifiedEvent</code>.</p>
<p>I would appreciate any pointers as to why this might be happening / how I can solve the issue.</p>
<p>Thank you.</p>

---

## Post #4 by @lassoan (2023-04-11 19:21 UTC)

<aside class="quote no-group" data-username="danpak94" data-post="3" data-topic="28812">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/danpak94/48/18310_2.png" class="avatar"> danpak94:</div>
<blockquote>
<p>to demonstrate that changing the <strong>parent</strong> folder visibility seems to call <code>segmentationNode.DisplayNode()</code>'s <code>ModifiedEvent</code>, but not <code>folderDisplayNode</code>’s <code>ModifiedEvent</code>.</p>
</blockquote>
</aside>
<p>Toggling visibility of the folder actually calls <code>folderDisplayNode</code>’s <code>ModifiedEvent</code>. To test, you can create a new folder, click the eye icon so that a display node gets created for it automatically, run the code snippet below, and toggle the eye icon of the folder to see the message printed:</p>
<pre data-code-wrap="python"><code class="lang-python">shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
folderDisplayNode = shNode.GetItemDataNode(shNode.GetItemByName('NewFolder'))
if not folderDisplayNode or not folderDisplayNode.IsA('vtkMRMLFolderDisplayNode'):
    raise RuntimeError("This folder has no display node")

def test_callback(caller, event):
    print('in here!', caller.GetName())

test = slicer.util.VTKObservationMixin()
test.addObserver(folderDisplayNode, vtk.vtkCommand.ModifiedEvent, test_callback)
</code></pre>

---

## Post #5 by @danpak94 (2023-04-12 01:59 UTC)

<p>Yes, that works when I have a single folder, but I’m wondering about when there’s a folder inside another folder.</p>
<p>ParentFolder<br>
|---- NewFolder</p>
<p>The callback is triggered when I toggle NewFolder, but not when I toggle ParentFolder.</p>

---

## Post #6 by @lassoan (2023-04-12 11:32 UTC)

<aside class="quote no-group" data-username="danpak94" data-post="5" data-topic="28812">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/danpak94/48/18310_2.png" class="avatar"> danpak94:</div>
<blockquote>
<p>The callback is triggered when I toggle NewFolder, but not when I toggle ParentFolder.</p>
</blockquote>
</aside>
<p>That’s correct. A node invokes Modified event if the node is modified. A node does not invoke Modified event if a different node is modified.</p>
<p>Some nodes invoke custom modified events when certain properties change or some properties in related nodes change.</p>
<p>What is your overall goal?</p>

---

## Post #7 by @danpak94 (2023-04-12 16:41 UTC)

<p>If this behavior is expected, then how come the following happens?</p>
<p>ParentFolder<br>
|---- SegmentationNode</p>
<p><code>test.addObserver(SegmentationNode.GetDisplayNode(), vtk.vtkCommand.ModifiedEvent, test_callback)</code></p>
<p>Toggling ParentFolder calls test_callback.</p>
<p>My overall goal:<br>
I want to update my visibility checkbox based on the “final” visibility of the NewFolder, since NewFolder is only visible when both ParentFolder and NewFolder are visible.</p>

---

## Post #8 by @lassoan (2023-04-12 22:41 UTC)

<p>It looks like the folder display node explicitly invokes a <code>Modified</code> event on all display nodes of all its displayable node children:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/fd7b4f3cceba976aabeb2e1cdda9ecc685fc0c64/Libs/MRML/Core/vtkMRMLFolderDisplayNode.cxx#L198-L225">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/fd7b4f3cceba976aabeb2e1cdda9ecc685fc0c64/Libs/MRML/Core/vtkMRMLFolderDisplayNode.cxx#L198-L225" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/fd7b4f3cceba976aabeb2e1cdda9ecc685fc0c64/Libs/MRML/Core/vtkMRMLFolderDisplayNode.cxx#L198-L225" target="_blank" rel="noopener">Slicer/Slicer/blob/fd7b4f3cceba976aabeb2e1cdda9ecc685fc0c64/Libs/MRML/Core/vtkMRMLFolderDisplayNode.cxx#L198-L225</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="198" style="counter-reset: li-counter 197 ;">
          <li>std::vector&lt;vtkIdType&gt; childItemIDs;</li>
          <li>shNode-&gt;GetItemChildren(folderItemId, childItemIDs, true);</li>
          <li>
          </li>
<li>bool batchProcessing = (childItemIDs.size() &gt; 10);</li>
          <li>if (batchProcessing)</li>
          <li>  {</li>
          <li>  this-&gt;GetScene()-&gt;StartState(vtkMRMLScene::BatchProcessState);</li>
          <li>  }</li>
          <li>
          </li>
<li>std::vector&lt;vtkIdType&gt;::iterator childIt;</li>
          <li>for (childIt=childItemIDs.begin(); childIt!=childItemIDs.end(); ++childIt)</li>
          <li>  {</li>
          <li>  vtkMRMLDisplayableNode* childDisplayableNode = vtkMRMLDisplayableNode::SafeDownCast(</li>
          <li>    shNode-&gt;GetItemDataNode(*childIt) );</li>
          <li>  if (!childDisplayableNode)</li>
          <li>    {</li>
          <li>    continue;</li>
          <li>    }</li>
          <li>  // Trigger display update for display node of child nodes that allow overriding</li>
          <li>  for (int i=0; i&lt;childDisplayableNode-&gt;GetNumberOfDisplayNodes(); ++i)</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/fd7b4f3cceba976aabeb2e1cdda9ecc685fc0c64/Libs/MRML/Core/vtkMRMLFolderDisplayNode.cxx#L198-L225" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The folder display node is not a displayable node, so it does not get a Modified event invokation. The code could be reorganized so that each folder display node just notifies its immediate children and then let the children folders notify their children. Do you want to give it a try to implement it?</p>
<p>Displaying branches that are under a “closed eye” branch in a different style (e.g., dark gray text, maybe a different icon) would be great. We’ve been thinking about implementing something like this just did not have the time. Do you plan to contribute this feature to Slicer core? Let us know how we can help.</p>

---

## Post #9 by @danpak94 (2023-04-13 17:42 UTC)

<p>This could be interesting for me to try, but I’ve only worked with python scripting for slicer, so I’m not very familiar with compiling it, etc. Is this something that I can get help with?</p>

---

## Post #10 by @lassoan (2023-04-13 19:08 UTC)

<p>C++/Python is not a big difference, but the key question is how much you are familiar (or ready to learn) about Qt and a little about Slicer core.</p>
<p>If you decide to give it a try then the first step is to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html">build Slicer from source</a>.</p>

---
