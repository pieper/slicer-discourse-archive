# How to split 4D volumes to individual 3D volumes?

**Topic ID**: 2707
**Date**: 2018-04-24
**URL**: https://discourse.slicer.org/t/how-to-split-4d-volumes-to-individual-3d-volumes/2707

---

## Post #1 by @xuec (2018-04-24 07:14 UTC)

<p>Thank you.In addition to that, do you perhaps know how to split 4D image data to several 3D? I found a way to do it manually by saving it in GUI, but I have too many files to handle it manually. Any hints please? Thank you</p>

---

## Post #2 by @lassoan (2018-04-24 13:07 UTC)

<p>You can write separate volumes to a zip file with this code snippet:</p>
<pre><code>sequenceNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLSequenceNode')
storageNode = slicer.vtkMRMLSequenceStorageNode()
storageNode.SetFileName('c:/tmp/volumes.mrb')
storageNode.WriteData(sequenceNode)
</code></pre>
<p>The .mrb file is actually a .zip file. You may need to change the extension to .zip to open it using an archive manager.</p>

---

## Post #3 by @xuec (2018-04-26 02:47 UTC)

<p>Thank you again for your response. how can I open the volumes.mrb, I tried to rename it to .zip files but I cannot open it using standard winrar/winzip.<br>
In addition, to my understanding, this will save the files, but will it be able to split the 4D data to 3D data directly? Thank you.</p>

---

## Post #4 by @xuec (2018-04-26 02:50 UTC)

<p>by the way, I usually used MultiVolumeExplorer module to select the frame and then save it one by one manually, however, I think this is too time consuming, hence I am just wondering if there is another good way to just split the 4D data to some 3D data. Thank you. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #5 by @lassoan (2018-04-26 13:49 UTC)

<aside class="quote no-group quote-post-not-found" data-username="xuec" data-post="6" data-topic="2647">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/x/e274bd/48.png" class="avatar"><a href="https://discourse.slicer.org/t/is-there-any-ways-to-save-transformation-matrix-using-command-line/2647/6">is there any ways to save transformation matrix using command line?</a></div>
<blockquote>
<p>I tried to rename it to .zip files but I cannot open it using standard winrar/winzip</p>
</blockquote>
</aside>
<p>.mrb file is zip file, so if you cannot open it then it may mean that you’ve tried to rename some other file (maybe a .nrrd file).</p>
<p>Have you installed Sequences module? Did you have your volume loaded as MultiVolume or as Sequence node? If you had it as MultiVolume, then load it as volume Sequence instead, as explained here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences#Convert_MultiVolume_node_to_Sequence_node" class="inline-onebox">Documentation/Nightly/Extensions/Sequences - Slicer Wiki</a>.</p>

---

## Post #6 by @xuec (2018-04-27 06:53 UTC)

<p>Indeed, I load it as volume instead of volume sequence, now It works like charm. Thank you so much!</p>

---
