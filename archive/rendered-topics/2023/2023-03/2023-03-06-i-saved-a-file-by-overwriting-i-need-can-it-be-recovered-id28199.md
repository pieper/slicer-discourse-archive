---
topic_id: 28199
title: "I Saved A File By Overwriting I Need Can It Be Recovered"
date: 2023-03-06
url: https://discourse.slicer.org/t/28199
---

# I saved a file by overwriting I need, can it be recovered?

**Topic ID**: 28199
**Date**: 2023-03-06
**URL**: https://discourse.slicer.org/t/i-saved-a-file-by-overwriting-i-need-can-it-be-recovered/28199

---

## Post #1 by @MariaTeresa_Mirarchi (2023-03-06 20:49 UTC)

<p>Operating system:<br>
Slicer version:5.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2023-03-06 20:53 UTC)

<p>If you store your files in a dropbox, onedrive, box, etc. synchronized folder or use revision control system (git, svn, etc.) then you may can retrieve previous version of your files. Otherwise, if you simply save in a local folder then you need to set unique name for each file you want to preserve.</p>
<p>You can save your entire workspace in a single file if you click the “package” icon in the Save data window. You may find that it is easy to save many versions like this because you need to set a new name for a single file.</p>

---

## Post #3 by @MariaTeresa_Mirarchi (2023-03-07 23:35 UTC)

<p>thank you very much!<br>
another question .i unintentionally connected two segments. how do i unlink them again?</p>
<p>Mariateresa Mirarchi MD</p>

---

## Post #4 by @lassoan (2023-03-08 02:11 UTC)

<p>You can click the undo button in the Segment Editor to see if you still have the unlinked segments in the undo stack.</p>
<p>If you don’t then you can split segments using the Scissors effect very effectively in the 3D view:</p>
<ul>
<li>Select or create an empty segment</li>
<li>Set Operation → Fill inside</li>
<li>Choose Masking → Editable area → Inside (the segment you want to split)</li>
</ul>
<div class="youtube-onebox lazy-video-container" data-video-id="m4zTj8i4tCA" data-video-title='New "scissors" editing tool in 3D Slicer for 3D cropping' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=m4zTj8i4tCA" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/m4zTj8i4tCA/maxresdefault.jpg" title='New "scissors" editing tool in 3D Slicer for 3D cropping' width="" height="">
  </a>
</div>


---

## Post #5 by @MariaTeresa_Mirarchi (2023-03-08 09:15 UTC)

<p>Hallo!<br>
it is too bumpy to cut out. it is a metastasis in the liver which is attached to a vein.</p>
<p>when I open the vascular window, the metastasis window also opens.<br>
and also by mistake I made it the same color and change it.<br>
thank you you are precious</p>
<p>Mariateresa Mirarchi MD</p>

---
