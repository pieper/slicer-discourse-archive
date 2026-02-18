# Transform Matrix calculated by GetMatrixTransformBetweenNodes

**Topic ID**: 4069
**Date**: 2018-09-11
**URL**: https://discourse.slicer.org/t/transform-matrix-calculated-by-getmatrixtransformbetweennodes/4069

---

## Post #1 by @xxzhou (2018-09-11 15:42 UTC)

<p>Hi!</p>
<p>I am new for 3D Slicer, and when I want to use GetMatrixTransformBetweenNodes to calculate transform matrix from source to target, I found that the input “source”&amp;“target” are both vtkMRMLTransformNode.</p>
<p>However, I usually use<br>
source = getNode(’’)<br>
target = getNode(’’), which are vtkMRMLScalarVolumeNode.</p>
<p>I am wondering how to change vtkMRMLScalarVolumeNode to vtkMRMLTransformNode.<br>
Any inference is welcomed!</p>
<p>Thank you!</p>
<p>Best regards,<br>
xxzhou</p>

---

## Post #2 by @lassoan (2018-09-11 18:04 UTC)

<p>GetMatrixTransformBetweenNodes() needs parent transform nodes of your nodes, so you need to use source.GetParentTransformNode() and target.GetParentTransformNode(). See details in this related post: <a href="https://discourse.slicer.org/t/transformation-graph-for-quick-calculation-of-concatenated-transforms/326/5?u=lassoan">Transformation graph for quick calculation of concatenated transforms</a></p>

---

## Post #3 by @cpinter (2018-09-11 18:10 UTC)

<p><a class="mention" href="/u/xxzhou">@xxzhou</a> Please do not post the same question <a href="https://discourse.slicer.org/t/transformation-graph-for-quick-calculation-of-concatenated-transforms/326/10?u=cpinter">more than once</a>. You won’t have a higher chance for it to be answered. Thanks.</p>

---

## Post #4 by @xxzhou (2018-09-11 18:48 UTC)

<p>Hi, sorry for this problem! I will not do that again.<br>
Thank you for your remind!</p>

---

## Post #5 by @jcfr (2018-09-11 18:53 UTC)

<aside class="quote no-group" data-username="xxzhou" data-post="4" data-topic="4069">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/x/13edae/48.png" class="avatar"> xxzhou:</div>
<blockquote>
<p>sorry for this problem! I will not do that again.</p>
</blockquote>
</aside>
<p>Thanks for understanding.</p>
<p>As a side note, if you have idea how we could update the forum to better convey the idea of “one post → one question”. Do not hesitate to create a  new topic for discussing it.</p>

---

## Post #6 by @xxzhou (2018-09-11 18:56 UTC)

<p>Sure, thank you <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=6" title=":grin:" class="emoji" alt=":grin:"><br>
Appreciate 3D Slicer Forum that you provide very efficient help for us. I am working on the information you provide for me. Thanks a lot!<br>
If solved, I will come back to post it.</p>

---
