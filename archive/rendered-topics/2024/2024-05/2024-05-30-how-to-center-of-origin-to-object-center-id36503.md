---
topic_id: 36503
title: "How To Center Of Origin To Object Center"
date: 2024-05-30
url: https://discourse.slicer.org/t/36503
---

# How to Center of Origin to Object Center

**Topic ID**: 36503
**Date**: 2024-05-30
**URL**: https://discourse.slicer.org/t/how-to-center-of-origin-to-object-center/36503

---

## Post #1 by @manjula (2024-05-30 18:49 UTC)

<p>Hi all,</p>
<p>I am working on full workflow for Orthognathic surgery through the 3D Slicer only and planning to make a tutorial. One last piece of puzzle i want to work out is the how to make the maxilla or the mandible to move around the object center. (not this way <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>)</p>
<p>Is there a way to without closing the entire scene and reloading the stl  files separately to center the transformation origin to the center of the object ? this will make Orthognathic surgery workflow very easy.</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1r5S9AguEYa6muIjFAp4AYOyRpXDR86pL/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1r5S9AguEYa6muIjFAp4AYOyRpXDR86pL/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1r5S9AguEYa6muIjFAp4AYOyRpXDR86pL/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1r5S9AguEYa6muIjFAp4AYOyRpXDR86pL/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Recording 2024-05-30 235552.mp4</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1-oSK8-RRMno2TqcBwLgHG9jb9tbmrl8Q/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1-oSK8-RRMno2TqcBwLgHG9jb9tbmrl8Q/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1-oSK8-RRMno2TqcBwLgHG9jb9tbmrl8Q/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1-oSK8-RRMno2TqcBwLgHG9jb9tbmrl8Q/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Recording 2024-05-31 001400.mp4</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thank you</p>

---

## Post #2 by @Sunderlandkyl (2024-05-30 20:02 UTC)

<p>You can specify the center of transformation in Python using vtkMRMLTransformNode::SetCenterOfTransformation().</p>
<p>You can also update the center of transformation from the GUI, see this video starting @ 0:18: <a href="https://youtu.be/ielxgJS-6SI?si=QXfVpDDE-5fBx48p&amp;t=18" rel="noopener nofollow ugc">https://youtu.be/ielxgJS-6SI?si=QXfVpDDE-5fBx48p&amp;t=18</a>.</p>

---
