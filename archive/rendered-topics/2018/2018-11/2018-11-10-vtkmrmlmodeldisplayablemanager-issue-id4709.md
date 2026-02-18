# vtkMRMLModelDisplayableManager issue

**Topic ID**: 4709
**Date**: 2018-11-10
**URL**: https://discourse.slicer.org/t/vtkmrmlmodeldisplayablemanager-issue/4709

---

## Post #1 by @smrolfe (2018-11-10 00:23 UTC)

<p>Hello,<br>
I would like to identify the picked display node after a fiducial is placed using the markups module. While attempting this, I came across what seems to be a bug in the vtkMRMLModelDisplayableManager.</p>
<p>The Pick function attempts to set the picked display node using the internal function FindPickedDisplayNodeFromMesh. The mesh is obtained via:<br>
this-&gt;Internal-&gt;CellPicker-&gt;GetDataSet().</p>
<p>However, no mesh is returned. The picked cell id is set correctly using:<br>
this-&gt;Internal-&gt;CellPicker-&gt;GetCellId()</p>
<p>I have also tried:<br>
this-&gt;Internal-&gt;FindFirstPickedDisplayNodeFromPickerProp3Ds();</p>
<p>to identify the picked display node. Is this a known issue with the vtkMRMLModelDisplayableManager? I would appreciate any advice or suggestions.<br>
Thanks,<br>
Sara</p>

---

## Post #2 by @pieper (2018-11-26 15:34 UTC)

<p>Hi <a class="mention" href="/u/smrolfe">@smrolfe</a> -</p>
<p>Sorry for the slow reply on this - I had a chance to step through the <code>vtkMRMLModelDisplayableManager::Pick</code> code and things seem to be working for me with a small example.</p>
<p>If this is still an issue for you let’s try to write a small test script that can replicate what you are seeing.</p>
<p>Best,<br>
Steve</p>

---

## Post #3 by @smrolfe (2018-11-26 22:34 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,<br>
Thanks for your reply, I’ll write a test script and then post an update.<br>
Best,<br>
Sara</p>

---

## Post #4 by @smrolfe (2018-11-30 20:52 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> -<br>
Here’s a few lines of code that I expected to return the volume node when a fiducial is placed on a 3D rendered volume:</p>
<pre><code class="lang-auto">fidList = getNode('F')
fidIndex = 0
volumeID = fidList.GetNthFiducialAssociatedNodeID(fidIndex)
volumeNode = getNode(volumeID)
</code></pre>
<p>This code is from an old Slicer thread archived here:<br>
<a href="http://massmail.spl.harvard.edu/public-archives/slicer-devel/2014/015761.html" class="onebox" target="_blank" rel="nofollow noopener">http://massmail.spl.harvard.edu/public-archives/slicer-devel/2014/015761.html</a></p>
<p>When I use this method, I do not get any node associated with the fiducial. Is this something that was changed from a previous version of Slicer? I traced the issue back to the vtkMRMLDisplayableManager, which is using:<br>
this-&gt;Internal-&gt;FindPickedDisplayNodeFromMesh(mesh, pickPoint);</p>
<p>to get the associated node. Since there is no mesh when only volume data is loaded, this is setting the associated node to null. I tried subbing the function FindFirstPickedDisplayNodeFromPickerProp3Ds, but this was not working for volume data either.</p>
<p>Could you let me know if you have any suggestions?</p>

---

## Post #5 by @pieper (2018-12-01 20:53 UTC)

<p>Hi <a class="mention" href="/u/smrolfe">@smrolfe</a> -</p>
<p>Thanks for the extra info - I see now you’d like to get the volume node but currently the code only only adds an associated node in the case of clicking on a model.</p>
<p>I <a href="https://github.com/Slicer/Slicer/commit/f1b55fc99e948629e8a048c619d685a25ac0ba4d" rel="nofollow noopener">just added a fix</a> so that the nodeID is set for either model or volume nodes.</p>
<p>So now, if I do this:</p>
<ol>
<li>download the MRHead from SampleData</li>
<li>make it visible in the VolumeRendering module</li>
<li>place a fiducial on it</li>
</ol>
<p>Then this code prints out <code>"MRHead"</code>.</p>
<pre><code class="lang-auto">fidList = getNode('F')
fidIndex = 0
volumeID = fidList.GetNthFiducialAssociatedNodeID(fidIndex)
volumeNode = getNode(volumeID)
print(volumeNode.GetName())
</code></pre>
<p>Let me know how it goes for you.</p>
<p>Cheers,<br>
-Steve</p>

---
