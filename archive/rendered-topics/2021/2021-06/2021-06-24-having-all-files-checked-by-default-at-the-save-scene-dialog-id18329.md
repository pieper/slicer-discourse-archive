---
topic_id: 18329
title: "Having All Files Checked By Default At The Save Scene Dialog"
date: 2021-06-24
url: https://discourse.slicer.org/t/18329
---

# Having all files checked by default at the Save Scene dialog

**Topic ID**: 18329
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/having-all-files-checked-by-default-at-the-save-scene-dialog/18329

---

## Post #1 by @giovform (2021-06-24 17:26 UTC)

<p>Is there a way to set the select files checked by default at the Save Scene dialog? I tried this code bellow, but no sucess:</p>
<pre><code class="lang-auto">saveDataDialog.children()[6].model().setHeaderData(0, qt.Qt.Horizontal, qt.Qt.Checked, qt.Qt.CheckStateRole)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f485a111292faeecb0b9b99b8cb0a541487a5ed7.png" data-download-href="/uploads/short-url/yT8NIJXwPT6OBt4vziSdVzOMr9Z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f485a111292faeecb0b9b99b8cb0a541487a5ed7.png" alt="image" data-base62-sha1="yT8NIJXwPT6OBt4vziSdVzOMr9Z" width="690" height="459" data-dominant-color="333131"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">726×483 18.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2021-06-24 17:32 UTC)

<p>Better to use <a href="https://apidocs.slicer.org/master/classvtkMRMLStorableNode.html#ac92434ba2f9859a6f72bec0be170ad70">this method</a> to mark the nodes so that the widget will select them for saving.</p>

---

## Post #3 by @giovform (2021-06-24 18:19 UTC)

<p>But if I always wanted to have this option checked, regardless, because it has caused some confusion with users altering the directory thinking it would modify for all the project files.</p>

---

## Post #4 by @pieper (2021-06-24 19:50 UTC)

<p>I see.  If you always want to save everything maybe MRB is a better option (click the package icon).  Or if you are doing a bit of customizing anyway and don’t want the MRB you could add a save dialog with just a single directory browser.</p>

---
