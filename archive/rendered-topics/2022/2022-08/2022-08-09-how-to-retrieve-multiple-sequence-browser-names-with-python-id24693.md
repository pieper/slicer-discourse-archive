# How to retrieve multiple Sequence browser names with python

**Topic ID**: 24693
**Date**: 2022-08-09
**URL**: https://discourse.slicer.org/t/how-to-retrieve-multiple-sequence-browser-names-with-python/24693

---

## Post #1 by @minhtan16 (2022-08-09 12:41 UTC)

<p>Hi everyone,</p>
<p>I’m looking to retrieve every sequence browser names using python. Considering I have multiple sequence browser :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65e30550dd18fe4bd6a0072e49c3c4ac38bd994b.png" alt="image" data-base62-sha1="exkC5dHtDfBLPEJZbYIGBINJjiX" width="624" height="334"><br>
I would like to retrieve an array containing : SequenceBrowser_1, SequenceBrowser_2, etc<br>
I’m not sure which API to use.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @mau_igna_06 (2022-08-09 12:51 UTC)

<p>Hi. You should use<br>
<code>nodes = slicer.util.getNodesByClass("vtkMRMLSequenceBrowserNode")</code></p>
<p>Please let me know if that works</p>
<p>Mauro</p>

---

## Post #3 by @minhtan16 (2022-08-09 12:54 UTC)

<p>Hi thank you for the quick reply, this works!</p>

---

## Post #4 by @minhtan16 (2022-08-09 13:44 UTC)

<p>I’ve been looking into the api of vtkMRMLSequenceBrowserNode,<br>
I’m now trying to retrieve the sequence nodes associated with the sequence browser.<br>
E.g:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8161507e43ee8f4178a1828c90878d695546581.png" alt="image" data-base62-sha1="nYXwBhlf0CgJmEXREu8oebWhKr7" width="627" height="387"><br>
I want to retrieve ThorasicSeq_1_Scans and ThorasicSeq_1_Tracker, do you know a way to do it?</p>
<p>I’m able to retrieve ThorasicSeq_1_Scans by using GetMasterSequenceNode but how do I retrieve every sequence nodes of the current SequenceBrowser?</p>
<p>Here’s the information that I have when printing the sequence browser:<br>
vtkMRMLSequenceBrowserNode (000001D310DB9640)<br>
ID: vtkMRMLSequenceBrowserNode1<br>
ClassName: vtkMRMLSequenceBrowserNode<br>
Name: SequenceBrowser_1<br>
Debug: false<br>
MTime: 253532<br>
Description: (none)<br>
SingletonTag: (none)<br>
HideFromEditors: false<br>
Selectable: true<br>
Selected: false<br>
UndoEnabled: false<br>
Node references:<br>
dataNodeRef0: vtkMRMLScalarVolumeNode1<br>
dataNodeRef1: vtkMRMLLinearTransformNode4<br>
rootNodeRef0: (none)<br>
rootNodeRef1: (none)<br>
sequenceNodeRef0: vtkMRMLSequenceNode1<br>
sequenceNodeRef1: vtkMRMLSequenceNode2<br>
Playback active: false<br>
Playback rate (fps): 10<br>
Playback item skipping enabled: true<br>
Playback looped: true<br>
Selected item number: 95<br>
Recording active: false<br>
Recording on master modified only: false<br>
Recording sampling mode: limitedToPlaybackFrameRate<br>
Index display mode: [indexValue]<br>
Index display format: %.2f<br>
Sequence nodes:<br>
Sequence: ThoracicSeq_1__Scans, Proxy: (none), Playback: 1, Recording: 1, OverwriteProxyName: 0, SaveChanges: 0<br>
Sequence: ThoracicSeq_1__Tracker-ThoracicSeq_1__Tracker-Seq, Proxy: (none), Playback: 1, Recording: 1, OverwriteProxyName: 0, SaveChanges: 0</p>

---

## Post #5 by @Sunderlandkyl (2022-08-09 14:57 UTC)

<p>The function is GetSynchronizedSequenceNodes.<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLSequenceBrowserNode.html#a525422c88a8860cf701631c3a68768cb" rel="noopener nofollow ugc">Slicer: vtkMRMLSequenceBrowserNode Class Reference</a></p>
<pre><code class="lang-python">collection = vtk.vtkCollection()
sequenceBrowserNode.GetSynchronizedSequenceNodes(collection, True)
for i in range(collection.GetNumberOfItems()):
   sequenceNode = collection.GetItemAsObject(i)
</code></pre>

---

## Post #6 by @minhtan16 (2022-08-09 15:25 UTC)

<p>Thank you! This works!</p>

---
