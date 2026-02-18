# Update volume node

**Topic ID**: 7590
**Date**: 2019-07-15
**URL**: https://discourse.slicer.org/t/update-volume-node/7590

---

## Post #1 by @rbahegne (2019-07-15 14:12 UTC)

<p>Hello,</p>
<p>I want to display data as i receive them. So i created a volume node and each time i receive data i do a SetAndObserveImageData with the new data. Like this :</p>
<blockquote>
<p>m_streamNode-&gt;StartModify();<br>
m_streamNode-&gt;SetAndObserveImageData(imageData);<br>
m_streamNode-&gt;SetOrigin(originToRAS);<br>
m_streamNode-&gt;SetSpacing(pixelSpacingX,pixelSpacingY,scliceThickness);<br>
m_streamNode-&gt;SetIToRASDirection(rowToRAS[0],rowToRAS[1],rowToRAS[2]);<br>
m_streamNode-&gt;SetJToRASDirection(colToRAS[0],colToRAS[1],colToRAS[2]);<br>
m_streamNode-&gt;SetKToRASDirection(scliceToRAS[0],scliceToRAS[1],scliceToRAS[2]);<br>
m_streamNode-&gt;Modified();<br>
m_streamNode-&gt;CreateDefaultDisplayNodes();<br>
m_streamNode-&gt;CreateDefaultStorageNode();<br>
m_streamNode-&gt;UpdateScene(this-&gt;GetMRMLScene());<br>
this-&gt;UpdateFromMRMLScene();</p>
</blockquote>
<p>It kind of works but to have the display updated i need to hide and show the node, or to zoom on the window or click anything to have the window updated.</p>
<p>I searched and tried several kind of update command on the scene, node or displayNode. I did not manage to have it auto updated for now.</p>
<p>Is this possible ? Am I doing it the right way ?</p>

---

## Post #2 by @pieper (2019-07-15 14:32 UTC)

<p>Looks like you never call <code>EndModify</code> to match up with your <code>StartModifify</code> (these are used to make bulk changes to several nodes with only a single event)</p>

---

## Post #3 by @rbahegne (2019-07-16 13:03 UTC)

<p>Ok, in fact my main problem was a thread problem. I receive image data via websocket running in a separate tread and that was this tread tryng to update the node. And the node hierachy is managed i guess by the main thread. The solution in a simple signal/slot and make sure that the operation on the node are made by the main thread.</p>
<p>I had various not predictable behaviours and this kind of error/warning :</p>
<blockquote>
<p>HasItemAttribute: Failed to find subject hierarchy item by ID 94424278946520<br>
Input port 0 of algorithm vtkImageMapToWindowLevelColors(0x55914d195a70) has 0 connections but is not optional.<br>
Input port 0 of algorithm vtkImageThreshold(0x55914d19d860) has 0 connections but is not optional.<br>
QObject::startTimer: Timers cannot be started from another thread<br>
QObject::killTimer: Timers cannot be stopped from another thread<br>
Cannot make QOpenGLContext current in a different thread</p>
</blockquote>
<p>One last question, it work without StartModify and EndModify, so what is the purpose of thoses functions ?</p>

---

## Post #4 by @pieper (2019-07-16 20:28 UTC)

<aside class="quote no-group" data-username="rbahegne" data-post="3" data-topic="7590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbahegne/48/4837_2.png" class="avatar"> rbahegne:</div>
<blockquote>
<p>One last question, it work without StartModify and EndModify, so what is the purpose of thoses functions ?</p>
</blockquote>
</aside>
<p>They are only for efficiency - should work the same without them.</p>

---
