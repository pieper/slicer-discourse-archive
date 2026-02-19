---
topic_id: 21857
title: "Cannot Pull Activebrowsernode From Qmrmlsequencebrowsertoolb"
date: 2022-02-08
url: https://discourse.slicer.org/t/21857
---

# Cannot pull activeBrowserNode from qMRMLSequenceBrowserToolBar in Python

**Topic ID**: 21857
**Date**: 2022-02-08
**URL**: https://discourse.slicer.org/t/cannot-pull-activebrowsernode-from-qmrmlsequencebrowsertoolbar-in-python/21857

---

## Post #1 by @nathanbmnt (2022-02-08 20:00 UTC)

<p>Hello,<br>
I have a Python program where I want to get the active browser node of a qMRMLSequenceBrowserToolBar. However this variable is inaccessible from Python. Any ideas on how to get this variable?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/733ea4718045df8fcd12b89c35544d2f814510e4.png" data-download-href="/uploads/short-url/grv7qfyJsZPXHCz3Zy73ivTLBhq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/733ea4718045df8fcd12b89c35544d2f814510e4.png" alt="image" data-base62-sha1="grv7qfyJsZPXHCz3Zy73ivTLBhq" width="690" height="67" data-dominant-color="FBEFF3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">701×69 3.23 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<a href="https://apidocs.slicer.org/master/qMRMLSequenceBrowserToolBar_8h_source.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/master/qMRMLSequenceBrowserToolBar_8h_source.html</a></p>

---

## Post #2 by @lassoan (2022-02-08 20:09 UTC)

<p>Good catch. This method was not marked for Python wrapping. I’ve <a href="https://github.com/Slicer/Slicer/commit/fab4ec043672efc3434ae29fea498979b9ae7b17">added it now</a>, so the method will be available in Python from tomorrow in the Slicer Preview Release.</p>
<p>Until then, you can get the active browser node by connecting to function to the <code>activeBrowserNodeChanged(vtkMRMLNode* activeBrowserNode)</code> signal.</p>

---
