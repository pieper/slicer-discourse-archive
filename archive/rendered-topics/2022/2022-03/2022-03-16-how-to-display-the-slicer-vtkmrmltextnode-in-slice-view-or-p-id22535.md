# How to display the `slicer.vtkMRMLTextNode` in slice view or pyhon interactor?

**Topic ID**: 22535
**Date**: 2022-03-16
**URL**: https://discourse.slicer.org/t/how-to-display-the-slicer-vtkmrmltextnode-in-slice-view-or-pyhon-interactor/22535

---

## Post #1 by @jumbojing (2022-03-16 10:08 UTC)

<p>How to display or print the <code>slicer.vtkMRMLTextNode's Text</code> in slice view or pyhon interactor?</p>

---

## Post #2 by @mikebind (2022-03-16 15:22 UTC)

<p>Here is the documentation for the vtkMRMLTextNode class: <a href="https://apidocs.slicer.org/master/classvtkMRMLTextNode.html" class="inline-onebox">Slicer: vtkMRMLTextNode Class Reference</a></p>
<pre><code class="lang-auto">textNodeName = 'My Text Node'
textNode = slicer.util.getNode(textNodeName)
print(textNode.GetText())
</code></pre>

---

## Post #3 by @jumbojing (2022-03-16 20:41 UTC)

<p>Thanks, but how to export/import the node?<br>
I want to edit it in external editor.</p>

---

## Post #4 by @lassoan (2022-03-16 21:18 UTC)

<aside class="quote no-group" data-username="jumbojing" data-post="3" data-topic="22535">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<p>Thanks, but how to export/import the node?</p>
</blockquote>
</aside>
<p>Do you mean that you did not actually want to view the text? Or you mean that what <a class="mention" href="/u/mikebind">@mikebind</a> described works well and now you would like to write this text to file?</p>
<p>Please describe your end goal because if we give solutions to your low-level tasks that may not lead to solving your high-level task in an optimal way.</p>

---

## Post #5 by @jumbojing (2022-03-16 22:28 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f253bd36f119d55d6fc1aa32e247fe70331ea8f7.png" alt="image" data-base62-sha1="yzIXoSttk2x58fCxEt9j0gPl3sr" width="369" height="68"><br>
I want to save this Node, but get “false”</p>

---

## Post #6 by @mikebind (2022-03-16 22:38 UTC)

<p>Text nodes with very short text (&lt;250 characters) default to saving in the MRML scene file rather than in their own files, meaning that they do not get storage nodes by default.  I think it is the lack of storage node which leads to <code>saveNode</code> failing. You can force a text node to have a storage node like this</p>
<pre><code class="lang-auto">tx = getNode('Text')
tx.SetForceCreateStorageNode(1)
# Now this will work
saveNode(tx, r"text333.txt")
</code></pre>

---

## Post #7 by @jumbojing (2022-03-16 22:40 UTC)

<p>and howto import this txt file?</p>

---

## Post #8 by @mikebind (2022-03-16 22:43 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.loadText">https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.loadText</a></p>

---

## Post #9 by @jumbojing (2022-03-16 22:54 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/534a9fda6c780d8d5d9623641555c1951866cec5.png" data-download-href="/uploads/short-url/bSPvKGfeZ1lSi8woAdu3XhUeWvH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/534a9fda6c780d8d5d9623641555c1951866cec5_2_690x78.png" alt="image" data-base62-sha1="bSPvKGfeZ1lSi8woAdu3XhUeWvH" width="690" height="78" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/534a9fda6c780d8d5d9623641555c1951866cec5_2_690x78.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/534a9fda6c780d8d5d9623641555c1951866cec5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/534a9fda6c780d8d5d9623641555c1951866cec5.png 2x" data-dominant-color="D9F7FE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">871×99 10.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
谢谢老师, 太棒了. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
