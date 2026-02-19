---
topic_id: 22980
title: "How To Add The Subject Hierarchy Tree To A Custom Extension"
date: 2022-04-15
url: https://discourse.slicer.org/t/22980
---

# How to add the Subject hierarchy tree to a custom extension

**Topic ID**: 22980
**Date**: 2022-04-15
**URL**: https://discourse.slicer.org/t/how-to-add-the-subject-hierarchy-tree-to-a-custom-extension/22980

---

## Post #1 by @koeglfryderyk (2022-04-15 21:18 UTC)

<p>I wanted to have the subject hierarchy as part of my custom extension.</p>
<p>To do this, I added the <code>qMRMLSubjectHierarchyTreeView</code> to my .ui file.</p>
<p>It now appears in my custom extension but it is empty (a scene is loaded and in the data module the tree is there):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/443831ac72f89866276be0846b5b71e52afbdcfd.png" data-download-href="/uploads/short-url/9JuRvZp0C8VQqwPsVzNDS1R8qrr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/443831ac72f89866276be0846b5b71e52afbdcfd_2_345x164.png" alt="image" data-base62-sha1="9JuRvZp0C8VQqwPsVzNDS1R8qrr" width="345" height="164" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/443831ac72f89866276be0846b5b71e52afbdcfd_2_345x164.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/443831ac72f89866276be0846b5b71e52afbdcfd_2_517x246.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/443831ac72f89866276be0846b5b71e52afbdcfd_2_690x328.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1144×544 5.93 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What do I have to do to make all the folders, volumes etc appear here?</p>

---

## Post #2 by @lassoan (2022-04-16 00:25 UTC)

<p>You need to set the scene into the widget.</p>

---

## Post #3 by @koeglfryderyk (2022-04-16 15:07 UTC)

<p>Thanks, that worked. Just wanted to comment with the line of code if in the future anyone will have the same problem:</p>
<p>(I added this line of code to setup() in the widget class of my extension:<br>
<code>self.ui.SubjectHierarchyTreeView.setMRMLScene(slicer.mrmlScene)</code></p>

---
