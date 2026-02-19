---
topic_id: 11990
title: "Best Way To Delete Nodes"
date: 2020-06-11
url: https://discourse.slicer.org/t/11990
---

# Best way to delete nodes

**Topic ID**: 11990
**Date**: 2020-06-11
**URL**: https://discourse.slicer.org/t/best-way-to-delete-nodes/11990

---

## Post #1 by @siaeleni (2020-06-11 15:27 UTC)

<p>Hi,</p>
<p>I apply some filters to my data (eg.BinaryMorphologicalOpeningImageFilter) and at the end I remove all unnecessary nodes from the scene (label maps/segmentation nodes) that were created in the meantime. Right after applying the filtering, I remove all nodes through the following function:</p>
<blockquote>
<p>def RemoveNodeFromScene(node):<br>
if slicer.mrmlScene:<br>
slicer.mrmlScene.RemoveNode(node)</p>
</blockquote>
<p>The first time that runs the filtering works fine, but the second time that I use the filtering, I have realized that the “Data module” stucks, and I cannot handle the visibility of the nodes from there anymore.</p>
<p>I have realized that RemoveNodeFromScene affects the Data module.<br>
Why does it happened and how can I solve that issue?</p>
<p>Thanks,<br>
Eleni</p>

---

## Post #2 by @pieper (2020-06-11 15:43 UTC)

<p>Hi Eleni -</p>
<p>Thanks for reporting <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>That sounds like a bug in the Data module at some level.  Can you provide a simple test script that replicates the problem and file an issue on the Slicer project on github?</p>
<p>-Steve</p>

---

## Post #3 by @siaeleni (2020-06-11 16:18 UTC)

<p>Hi Steve,</p>
<p>Sure, here is the file, I tried to replicate it by running the following at Python Interactor by using 4.11 version in case that is useful and here is happening from the first time that I run it.<br>
</p><aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="15" height="15">
      <a href="https://www.dropbox.com/s/35lsuegpymhx94n/sample.txt?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-txt-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/35lsuegpymhx94n/sample.txt?dl=0" target="_blank" rel="nofollow noopener">sample.txt</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I will file the issue on GitHub too.</p>
<p>Thanks,<br>
Eleni</p>

---

## Post #4 by @lassoan (2020-06-11 16:41 UTC)

<p>You did everything well, except that at the end you deleted the entire subject hierarchy by calling <code>RemoveNodeFromScene(shNode)</code>. Subject hierarchy node is a singleton, it is created automatically, and should not be deleted. Nevertheless, it would be nicer if deleting the subject hierarchy would result in recreating it from scratch instead of making the GUI stuck in an inconsistent state.</p>
<p>One more comment: if you delete a data node, make sure you delete all associated nodes that you created along with it (display nodes, color nodes, storage node).</p>

---
