---
topic_id: 4595
title: "Discussion About Default Display And Storage Nodes"
date: 2018-10-30
url: https://discourse.slicer.org/t/4595
---

# Discussion about default display and storage nodes

**Topic ID**: 4595
**Date**: 2018-10-30
**URL**: https://discourse.slicer.org/t/discussion-about-default-display-and-storage-nodes/4595

---

## Post #1 by @cpinter (2018-10-30 18:15 UTC)

<p>Thread for continuing discussion in <a href="https://github.com/Slicer/Slicer/pull/1029">PR1029</a>:</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>:<br>
Should we simply disable the creation of node using node constructor from both C++ and python ? That would be consistent with the new behavior we are promoting.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>:<br>
There are probably valid use cases for instantiating nodes directly, so probably we should not disable it.</p>
<p><a class="mention" href="/u/pieper">@pieper</a>:<br>
Yes, instantiating a node and adding it to the scene seems like the logical pattern (it’s in lots of examples). But when you are using the utility method to create default display nodes then you should expect them to have the proper SetAndObserve* behavior and that depends on the scene being valid.</p>
<p>On the other hand, now that I look at it it’s odd that CreateDefaultStorageNode doesn’t call SetAndObserveStorageNodeID.</p>
<p>We could deprecate (or leave) the current methods and introduce CreateAndObserveDefault{Display,Storage}Node methods.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a>:<br>
It is indeed strange that there is no observation set in CreateDefaultStorageNode. Considering that CreateDefaultDisplayNodes does set the observation, I think this is an inconsistency that we should fix, so at least the two functions with the similar names do the same things. I know there might be issues in some places, but I’d rather add the observation in the CreateDefaultStorageNode functions to make them work the same way.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>:<br>
This morning we also talked about adding a  <code>vtkMRMLScene::Reset(vtkMRMLNode*)</code>  that would allow to reset a node with the expected default properties.</p>
<p>Either way, I am wondering if we should we also replace the calls to  <code>vtkNew&lt;vtkMRMLNAME&gt;</code>  with the equivalent call using  <code>AddNewNodeByClass</code>  or by adding a call to the (to be added) <code>vtkMRMLScene::Reset(vtkMRMLNode*)</code>  function ?</p>

---
