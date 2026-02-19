---
topic_id: 12795
title: "Slicer Crashes When Setting Master Sequence Node To Sequence"
date: 2020-07-30
url: https://discourse.slicer.org/t/12795
---

# Slicer crashes when setting master Sequence Node to SequenceBrowserNode

**Topic ID**: 12795
**Date**: 2020-07-30
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-setting-master-sequence-node-to-sequencebrowsernode/12795

---

## Post #1 by @dloopz (2020-07-30 18:33 UTC)

<p>Operating system: Ubuntu Debian 18.04 (KDE neon 5.19)<br>
Slicer version: 4.11.0-2020-06-05<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi everyone,</p>
<p>I’m having some troubles managing sequences (create them and remove them completely) from python scripts for background nodes (ie ScalarVolumeNodes) and label nodes (ie LabelMapVolumeNodes). My problem is that I can create and delete everything once (sequence node for both background and label, sequence browser node, and both proxys). Buth when I attempt to create a sequence again after its removal, slicer crashes in this line:</p>
<p><code>SeqBrowNode.SetAndObserveMasterSequenceNodeID(SeqNode.GetID())</code></p>
<p>The way I manage a sequence creation is like this:</p>
<pre><code>SeqBrowN = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSequenceBrowserNode')
SeqBrowN.SetName('SOME_SEQBROWN_NAME')

SeqN = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSequenceNode')
SeqN.SetName('SOME_SEQN_NAME')

for frame_i in range(frames):
      NodeForSequence = slicer.mrmlScene.GetNodeByID('SOME_PREFIX' + str(frame_i))
      SeqN.SetDataNodeAtValue(NodeForSequence,str(frame_i))

SeqBrowN.SetAndObserveMasterSequenceNodeID(SeqN.GetID()) # Here I get the crash
sequencesModule.widgetRepresentation().setActiveBrowserNode(SeqBrowN)
</code></pre>
<p>The way I manage removal:</p>
<pre><code>for seq_i in range(self.getNumberOfMySequences()):

    # Build background name
    name_i = str(seq_i + 1) + self.getBackgName()

    # Custom background SequenceNodes
    backgSeqNode = slicer.mrmlScene.GetNodesByClassByName('vtkMRMLSequenceNode',name_i).GetItemAsObject(0)
    while ( backgSeqNode != None ):
      backgSeqNode.RemoveAllObservers()
      slicer.mrmlScene.RemoveNode(backgSeqNode)
      backgSeqNode = slicer.mrmlScene.GetNodesByClassByName('vtkMRMLSequenceNode',name_i).GetItemAsObject(0)
    
    # Custom background ScalarVolumeNodes (proxys)
    backgProxyNode = slicer.mrmlScene.GetNodesByClassByName('vtkMRMLScalarVolumeNode',name_i).GetItemAsObject(0) 
    while ( backgProxyNode != None ):
      slicer.mrmlScene.RemoveNode(backgProxyNode)
      backgProxyNode = slicer.mrmlScene.GetNodesByClassByName('vtkMRMLScalarVolumeNode',name_i).GetItemAsObject(0)
    
  # Custom background SeqBrowNode
  name_SeqBrow = self.getBackgName()
  backgSeqBrowNode = slicer.mrmlScene.GetNodesByClassByName('vtkMRMLSequenceBrowserNode',name_SeqBrow).GetItemAsObject(0)
  while ( backgSeqBrowNode != None ):
    backgSeqBrowNode.RemoveAllObservers()  
    slicer.mrmlScene.RemoveNode(backgSeqBrowNode)
    backgSeqBrowNode = slicer.mrmlScene.GetNodesByClassByName('vtkMRMLSequenceBrowserNode',name_SeqBrow).GetItemAsObject(0)
</code></pre>
<p>I think I’m not removing correctly or maybe the synchronization is the problem. Any suggestion or similar code to look for and learn?</p>
<p>Thanks!!<br>
Lucca</p>

---

## Post #2 by @lassoan (2020-07-30 19:27 UTC)

<p>In the first example there does not seem to be anything wrong, so the issue is most likely the content of <code>NodeForSequence</code>. Can you send a code snippet that I can use as is to reproduce the crash? Or at least a link to your source code repository so that I can see the full context of the code.</p>
<p>To delete nodes, just call <code>slicer.mrmlScene.RemoveNode()</code>. No need for removing observers manually. Remove browser node first, then proxy nodes and sequence nodes.</p>

---

## Post #3 by @dloopz (2020-07-31 15:31 UTC)

<p>Hi Andras,</p>
<p>First, thank you very much for your reply. I checked the <code>NodeForSequence</code> and they were correct (ScalarVolumeNodes). I could solved this by setting a ‘NodeAboutToBeRemoved’ callback on sequenceNodes and using <code>RemoveSynchronizedSequenceNode</code>’ s method of sequenceBrowserNode with its master SequenceNode that was about to be deleted. This stops slicer’s crashes and doesn’t give warnings. However, I don’t understand why it works.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12795">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Can you send a code snippet that I can use as is to reproduce the crash? Or at least a link to your source code repository so that I can see the full context of the code.</p>
</blockquote>
</aside>
<p>I’m not sure how to encapsulate a snippet of code to reproduce as is, but I can try to make a reduced version. Meanwhile, <a href="https://gitlab.com/Curiale/cardiac/-/blob/master/CardIAcSegmentationModule/CardIAcSegmentationModule.py" rel="noopener nofollow ugc">here is the full code</a>. Is relatively large, but functions mentioned are:</p>
<ul>
<li><code>def createCardIAcSequence(self):</code> (line 1466)</li>
<li><code>def deleteCardIAcSeqNodes(self,delete_only_shortSeq = False):</code> (line 1549)</li>
</ul>
<p>Thanks again</p>

---
