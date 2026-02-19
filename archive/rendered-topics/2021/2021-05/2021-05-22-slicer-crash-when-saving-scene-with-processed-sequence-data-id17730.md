---
topic_id: 17730
title: "Slicer Crash When Saving Scene With Processed Sequence Data"
date: 2021-05-22
url: https://discourse.slicer.org/t/17730
---

# Slicer crash when saving scene with processed Sequence data

**Topic ID**: 17730
**Date**: 2021-05-22
**URL**: https://discourse.slicer.org/t/slicer-crash-when-saving-scene-with-processed-sequence-data/17730

---

## Post #1 by @mikebind (2021-05-22 07:02 UTC)

<p>Hello, I am having a reproducible crash of Slicer when I try to save a scene.  I have a sequence of 3D volumes and have done several processing steps on them, and have saved that progress in an mrb file.  Then I do a bit more processing, and then when I try to save the scene, Slicer crashes.  A _BundleSaveTemp directory is created and it contains in incomplete MRML file (no XML closing MRML tag, and no closing tag for a vtkMRMLScriptedModuleNodeUserStatistics ScriptedModule).  I believe there is likely also a lot more missing which would appear after that, because if I just remove that last  ScriptedModule section and manually add the <code>&lt;/MRML&gt;</code> tag and then try to load that mrml file, I get many errors which say <code>ResolveUnresolvedItems: Unable to find data node with ID (nullptr)</code>.  I can consistently reproduce this crash by following the same steps, but I’m not sure what the best approach to troubleshooting would be.  There is nothing at the end of the error logs (the last message logged is before I click save; for example,  <code>[DEBUG][Qt] 21.05.2021 16:41:05 [] (unknown:0) - Switch to module:  "Data"</code>), so there’s nothing helpful there.</p>
<p>Is the fact that the MRML scene file is truncated a good hint?  Is the problem likely related to the UserStatistics module (which I make no use of at this point, if I look at it the “Enabled” checkbox is unchecked) because that is where the .mrml file cuts off?</p>
<p>Other suggestions about how to troubleshoot crashes?  I’m using a custom module that is doing a lot of node management on Sequences, and I feel like sometimes the code manages to get the SubjectHierarchy confused, but I don’t really understand how it happens, and it doesn’t seem consistent. This is the first time I have ever run into not being able to save a scene to an mrb file.</p>

---

## Post #2 by @pieper (2021-05-22 22:48 UTC)

<p>Probably the best way to approach this is to do start with a workflow that doesn’t crash and incrementally add features until you can isolate what leads to the corruption.  As you say, it’s probably the node references or subject hierarchy getting out of sync.  The fact that you have the half-written mrml file indicates that one of the storage nodes crashed during the save process.</p>
<p>You could also do a debug build from source and use the debugger to identify where the crash is happening in C++.  There’s a chance this would isolate the error, but probably the actual bug is somewhere else and the mrml scene is already in a corrupt state by the time you want to save.</p>

---

## Post #3 by @mikebind (2021-05-25 18:14 UTC)

<p>I am making progress on this problem, and it occurs earlier than I thought.  I wonder if I am creating derived Sequences in the wrong way.  Currently, I have been creating them via</p>
<pre><code>seq = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSequenceNode')
</code></pre>
<p>which is the way I create all sorts of other classes of MRML nodes, but I see that the following error message appears when I open the Save Data dialog after creating a Sequence node in this way:</p>
<pre><code>void __cdecl qSlicerSaveDataDialogPrivate::populateNode(class vtkMRMLNode *)  failed: 
storage node not found for node  vtkMRMLSequenceNode2 . The node will not be shown in the 
save data dialog.
</code></pre>
<p>Calling <code>seq.CreateDefaultStorageNode()</code> or <code>seq.CreateDefaultSequenceStorageNode()</code> doesn’t seem to help; I get the same error after running them.</p>
<p>Checking an existing Sequence (that I didn’t create), I see that the storage node is of type <code>vtkMRMLVolumeSequenceStorageNode</code>, which got me looking through the Slicer source code for the Sequences module, where I see a storage node being set up in a function called <code>AddSequence()</code>, but maybe that’s for loading a Sequence from a file?  I also see a function called <code>AddSynchronizedNode()</code> which looks like maybe I should be using that for creating the sequences I want instead of <code>mrmlScene.AddNewNodeByClass()</code>?  It looks like it can handle a null sequence argument.</p>
<p>Taking a step back, I have a volume sequence with an associated sequence browser.  My goal is to end up with a new volume sequence associated with the same browser, where the volumes in the new sequence are derived by processing the volumes in the existing volume sequence.  What is the correct way to do this in general?  My approach so far has been to create a new Sequence, fill it, and then use <code>browserNode.AddSynchronizedSequenceNode()</code> to add the new Sequence to the existing browser. I assumed I needed to do this because I thought an empty or partially filled sequence would not be able to be added to the browser node (because how would you handle browsing through one sequence with 14 items and another with 3 items?), but perhaps I am incorrect?</p>

---

## Post #4 by @mikebind (2021-05-27 18:37 UTC)

<p>Found the step that leads to the crash.  Here is a minimal example using SampleData which reproduces the crash:</p>
<pre><code>import SampleData    
sequenceNode = SampleData.downloadSample('CTCardioSeq')
sequenceBrowserNode = slicer.modules.sequences.logic().GetFirstBrowserNodeForSequenceNode(sequenceNode)
newSeq = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSequenceNode')
# this is the change that causes the crash:
sequenceBrowserNode.SetSaveChanges(newSeq,True) 
sceneSaveFilename = slicer.app.temporaryPath + "/saved-scene-crashes.mrb" 
# crash occurs while executing this line:
slicer.util.saveScene(sceneSaveFilename)
</code></pre>
<p>This seems like a bug. I am later going to fill the sequences I create using <code>SetDataNodeAtValue()</code>, and I wasn’t sure whether I needed to set save changes to True in order for those additions to be recorded in the sequence (and I figured it couldn’t hurt even if it wasn’t necessary), which is why I had set “Save Changes” to True for these sequences.  I’ll try not setting it that way.</p>

---

## Post #5 by @mikebind (2021-06-02 19:05 UTC)

<p>Just noticed that my crash example code is missing the line</p>
<pre><code>sequenceBrowserNode.AddSynchronizedSequenceNode(newSeq)
</code></pre>
<p>With this line included, there is no crash.  So, the issue in that case is probably related to setting SaveChanges on a sequence which isn’t actually associated with the browser node.  This still seems like a bug, but maybe a less severe one.</p>

---

## Post #6 by @lassoan (2021-06-04 21:08 UTC)

<p>Thank you, the detailed instructions for reproducing the problem were very helpful.</p>
<p>The crash was caused by the sequence browser getting into an inconsistent state due to incorrect use of the API (invoking operation on a browser node for an unrelated sequence node). The issue is fixed by checking the inputs and displaying meaningful error message if they are invalid.</p>
<aside class="onebox githubissue">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5671" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5671" target="_blank" rel="noopener">Crash saving sequence browser node if SetSaveChanges is set on a non-synchronized sequence node</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-06-02" data-time="18:48:17" data-timezone="UTC">06:48PM - 02 Jun 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-06-03" data-time="01:56:48" data-timezone="UTC">01:56AM - 03 Jun 21 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/mikebind" target="_blank" rel="noopener">
          <img alt="mikebind" src="https://avatars.githubusercontent.com/u/3981795?v=4" class="onebox-avatar-inline" width="20" height="20">
          mikebind
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Reproducible Slicer crash using sample data when the following code snippet is r<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">un in the interactor.

## Steps to reproduce
```
import SampleData    
sequenceNode = SampleData.downloadSample('CTCardioSeq')
sequenceBrowserNode = slicer.modules.sequences.logic().GetFirstBrowserNodeForSequenceNode(sequenceNode)
newSeq = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSequenceNode')
# this is the change that causes the crash:
sequenceBrowserNode.SetSaveChanges(newSeq,True) 
sceneSaveFilename = slicer.app.temporaryPath + "/saved-scene-crashes.mrb" 
# crash occurs while executing this line:
slicer.util.saveScene(sceneSaveFilename)
```
Running the above code leads to a reproducible Slicer crash when saving the scene.  If the following line is added before the `SetSaveChanges` line, then there is no crash. 

```
sequenceBrowserNode.AddSynchronizedSequenceNode(newSeq)
```

## Expected behavior
I would have expected an error to be raised when trying to SetSaveChanges on a sequence which is not associated with the browser.  

## Environment
- Slicer version: Slicer-4.13.0-2021-05-29  (same thing happens on 4.11.20210226)
- Operating system: Windows 10</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
