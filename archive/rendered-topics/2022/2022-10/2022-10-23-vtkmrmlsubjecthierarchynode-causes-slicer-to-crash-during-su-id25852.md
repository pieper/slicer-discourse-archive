---
topic_id: 25852
title: "Vtkmrmlsubjecthierarchynode Causes Slicer To Crash During Su"
date: 2022-10-23
url: https://discourse.slicer.org/t/25852
---

# vtkMRMLSubjectHierarchyNode causes Slicer to crash during surgical plan

**Topic ID**: 25852
**Date**: 2022-10-23
**URL**: https://discourse.slicer.org/t/vtkmrmlsubjecthierarchynode-causes-slicer-to-crash-during-surgical-plan/25852

---

## Post #1 by @mau_igna_06 (2022-10-23 23:30 UTC)

<p>Hi. Thank you for the hardwork on Slicer development!</p>
<p>I have developed a very nice feature I would like to integrate to the main branch of <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerIGT/SlicerBoneReconstructionPlanner: 3D Slicer module for planning mandible reconstruction surgery using fibula flap</a></p>
<p>This module handles tens of objects in a handful of folders that are created and deleted during the workflow. Till now it was stable enough. But now it is not, one folder with lots of items and subfolders is not visible on the subject hierarchie till I press right click on some folder visibility button, then it appears but Slicer shows the processing mouse cursor animation and then it crashes (sometimes). Other times it crashes when I start processing but not reliably (this involves creation and deletion of folders).</p>
<p>Hope you can help.</p>
<p>Mauro</p>

---

## Post #2 by @lassoan (2022-10-24 02:23 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="25852">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Till now it was stable enough. But now it is not</p>
</blockquote>
</aside>
<p>Which Slicer versions do you mean by “till now” and “now”?</p>
<p>To investigate, we need to be able to reproduce the issue. Ideally, a script that we can copy-paste into the Python console.</p>

---

## Post #3 by @mau_igna_06 (2022-10-25 13:42 UTC)

<p>Hi</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="25852">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Which Slicer versions do you mean by “till now” and “now”?</p>
</blockquote>
</aside>
<p>I mean today’s preview release by “now” and “till now”.</p>
<blockquote>
<p>To investigate, we need to be able to reproduce the issue. Ideally, a script that we can copy-paste into the Python console.</p>
</blockquote>
<p>On a virtual surgical plan, BRP creates the hierarchy below when clicking the “Update fibula planes over the fibula line, bone pieces and transform them to the mandible” button:</p>
<pre><code class="lang-auto">BoneReconstructionPlanner/
  Mandible reconstruction/
    LotsOfNodesAndSubfolders 
 Inverse mandible reconstruction/  &lt;-- this folder visibility is set to hidden while creating it
    LotsOfNodesAndSubfolders
</code></pre>
<p>There are two problems with the image below:</p>
<ul>
<li>
<ol>
<li>The “Inverse mandible reconstruction” folder doesn’t appear on the qMRMLSubjectHierarchyTreeView although it has been created.</li>
</ol>
</li>
<li>
<ol start="2">
<li>The orange mandible that appears over the fibula on the lower 3D view is inside the “Inverse mandible reconstruction” folder (and it should be hidden because its parent folder is hidden)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be7a190b017f4afcff91988babca20ab057bdb4e.jpeg" data-download-href="/uploads/short-url/rb2johaYNyrPA620ojX0UcZF9Se.jpeg?dl=1" title="Screenshot from 2022-10-25 10-03-55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be7a190b017f4afcff91988babca20ab057bdb4e_2_690x388.jpeg" alt="Screenshot from 2022-10-25 10-03-55" data-base62-sha1="rb2johaYNyrPA620ojX0UcZF9Se" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be7a190b017f4afcff91988babca20ab057bdb4e_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be7a190b017f4afcff91988babca20ab057bdb4e_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be7a190b017f4afcff91988babca20ab057bdb4e_2_1380x776.jpeg 2x" data-dominant-color="9F9EB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-10-25 10-03-55</span><span class="informations">1920×1080 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
</li>
</ul>
<p>When I click the eye icon on qMRMLSubjectHierarchyTreeView of “Mandible reconstruction” the “Inverse mandible reconstruction” folder appears:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07d54d79ef6b893631c26f5e483eb93dc8e21a88.jpeg" data-download-href="/uploads/short-url/17il9aDrv6p7PzwHOmN0ZlrjCxW.jpeg?dl=1" title="Screenshot from 2022-10-25 10-04-14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07d54d79ef6b893631c26f5e483eb93dc8e21a88_2_690x388.jpeg" alt="Screenshot from 2022-10-25 10-04-14" data-base62-sha1="17il9aDrv6p7PzwHOmN0ZlrjCxW" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07d54d79ef6b893631c26f5e483eb93dc8e21a88_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07d54d79ef6b893631c26f5e483eb93dc8e21a88_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07d54d79ef6b893631c26f5e483eb93dc8e21a88_2_1380x776.jpeg 2x" data-dominant-color="A0A0B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-10-25 10-04-14</span><span class="informations">1920×1080 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I click on the eye icon of the “Inverse mandible reconstruction” folder (once or twice) Slicer crashes.</p>
<hr>
<p>Here is a Slicer scene where you can quickly make Slicer crash:<br>
<a href="https://1drv.ms/u/s!AgpRvclrLSCegWlpmdL1L8s9BXrg?e=1btqGb" class="onebox" target="_blank" rel="noopener nofollow ugc">https://1drv.ms/u/s!AgpRvclrLSCegWlpmdL1L8s9BXrg?e=1btqGb</a></p>
<p>You need to install BoneReconstructionPlanner extension, then in “application settings”-&gt;“modules” replace the BRP folder path by the module path inside <a>this branch of BRP</a>, load the scene I provided, switch to BoneReconstructionPlanner module and do the button-clicks I explained at the beginning.</p>
<p>Thank you, hope you can help</p>

---

## Post #4 by @mau_igna_06 (2022-10-26 18:35 UTC)

<p>The solution was simple though, just replace the last line of this:</p>
<pre><code class="lang-auto">      inverseMandibleReconstructionFolder = shNode.CreateFolderItem(parentItemID,"Inverse mandible reconstruction")
      pluginHandler = slicer.qSlicerSubjectHierarchyPluginHandler().instance()
      folderPlugin = pluginHandler.pluginByName("Folder")
      folderPlugin.setDisplayVisibility(inverseMandibleReconstructionFolder, 0)
</code></pre>
<p>by this:</p>
<pre><code class="lang-auto">      qt.QTimer.singleShot(0, lambda: folderPlugin.setDisplayVisibility(inverseMandibleReconstructionFolder, 0))
</code></pre>
<p>May be it should be clarified <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#manipulate-subject-hierarchy-item">here</a> that you should use a timer if you are not on the python console (for more context see <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/commit/b58d3f961c5e32c2ed764b6c83a8943661697418#diff-35cef951fd2ef7675f25d45a8e5933c707de10ecb4835702b2b1b4c587fc87d8L231">this link</a>).</p>

---

## Post #5 by @mau_igna_06 (2022-10-26 22:09 UTC)

<p>There is a useful bug:</p>
<blockquote>
<p>If you delete and create a folder with the same name Slicer remembers if it was visible or not before you would have deleted it</p>
</blockquote>
<p>This is useful for BRP because you can select on the treeview if you want to see the folder of “Mandible reconstruction” or “Inverse mandible reconstruction” and then after updating the virtual surgical plan it doesn’t autotoggle back to “Mandible reconstruction” folder</p>

---

## Post #6 by @lassoan (2022-10-27 03:56 UTC)

<p>It should be safe to call <code>folderPlugin.setDisplayVisibility(inverseMandibleReconstructionFolder, 0)</code> right after creating the folder. I could not reproduce any issue with calling this method immediately.</p>
<p>Would you be able to come up with a minimal example that demonstrates how calling <code>setDisplayVisibility</code> immediately causes any issue?</p>

---
