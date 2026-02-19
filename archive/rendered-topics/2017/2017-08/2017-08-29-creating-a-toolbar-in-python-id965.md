---
topic_id: 965
title: "Creating A Toolbar In Python"
date: 2017-08-29
url: https://discourse.slicer.org/t/965
---

# Creating a toolbar in Python

**Topic ID**: 965
**Date**: 2017-08-29
**URL**: https://discourse.slicer.org/t/creating-a-toolbar-in-python/965

---

## Post #1 by @moselhy (2017-08-29 13:58 UTC)

<p>Hello,</p>
<p>I was wondering whether it would be possible to create a toolbar widget using Python, without the need of C++. Similar to this layout:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2a74998c8e9f52475960695b1a41f13d53af532.png" data-download-href="/uploads/short-url/puroTtCdviwLWshUiapU2QMSVZU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2a74998c8e9f52475960695b1a41f13d53af532.png" alt="image" data-base62-sha1="puroTtCdviwLWshUiapU2QMSVZU" width="690" height="26" data-dominant-color="F0EFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">913×35 4.65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2017-08-29 15:18 UTC)

<p>You can create a toolbar in Python the same way as in C++:</p>
<ul>
<li><a href="https://github.com/SlicerRt/Sequences/blob/00d4b4d98f340cd45f48ec00661ae717720d40f5/SequenceBrowser/qSlicerSequenceBrowserModule.cxx#L69-L72">create QToolBar</a></li>
<li><a href="http://doc.qt.io/qt-4.8/qtoolbar.html#addWidget">add actions or widgets into it</a></li>
<li><a href="https://github.com/SlicerRt/Sequences/blob/00d4b4d98f340cd45f48ec00661ae717720d40f5/SequenceBrowser/qSlicerSequenceBrowserModule.cxx#L89">add it to the main window</a></li>
</ul>

---
