---
topic_id: 26965
title: "How To Export Model As Smaller File"
date: 2022-12-28
url: https://discourse.slicer.org/t/26965
---

# How to export model as smaller file?

**Topic ID**: 26965
**Date**: 2022-12-28
**URL**: https://discourse.slicer.org/t/how-to-export-model-as-smaller-file/26965

---

## Post #1 by @studyskin (2022-12-28 23:46 UTC)

<p>hi, im new to slicer and computers in general but i am trying to make a model of a nasua narica skull for 3d printing from files i got from morphosource, i can load up and create the model fine but when i export the file is huge and my laptop cant handle it (i have a predator helios 300), is there a way to make it smaller in slicer? like a way to reduce the voxel count? i have tried simplifying using the segment editor but it smoothes the model too much and creates holes and still the file is huge, thank you to anyone who can help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2022-12-28 23:51 UTC)

<p>You can reduce the pollution count of your model using Surface Toolbox module. I would recommend using the “Uniform remesh” option, but you can also try “Decimation”. Usually you can reduce the mesh size by a factor of 10-20 without losing relevant details.</p>

---

## Post #3 by @studyskin (2022-12-29 13:50 UTC)

<p>Thank you for your reply! When I try to deciminate a message comes up saying ‘failed to compute output model: ‘none type’ object has no attribute’is_all_triangles’ do you know what I’m doing wrong?</p>

---

## Post #4 by @lassoan (2022-12-29 13:57 UTC)

<p>Did you get this error when you tried uniform remeshing or decimation?<br>
What Slicer version do you use?<br>
On what operating system?<br>
Can you share the model that you are trying to decimate (upload to dropbox/onedrive/google drive and post the link here)?</p>

---

## Post #5 by @studyskin (2022-12-29 14:20 UTC)

<p>im using slicer 5.2.1 and windows 10, it happened when i tried to uniform remesh, it also now wont let me select the model? but i imagine thats something simple, heres links to the file and a video trying to show what i mean about selecting, thank you so much for helping me i really appreciate it</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1-yQZbNmV5j9Hk86ukE00EWkCagDsn4K7/view?usp=share_link">
  <header class="source">

      <a href="https://drive.google.com/file/d/1-yQZbNmV5j9Hk86ukE00EWkCagDsn4K7/view?usp=share_link" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1-yQZbNmV5j9Hk86ukE00EWkCagDsn4K7/view?usp=share_link" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1-yQZbNmV5j9Hk86ukE00EWkCagDsn4K7/view?usp=share_link" target="_blank" rel="noopener nofollow ugc">IMG_9027.MOV</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1e-dpiaIXGsJwcZB9LxagRmeu01JzBkuf/view?usp=share_link">
  <header class="source">

      <a href="https://drive.google.com/file/d/1e-dpiaIXGsJwcZB9LxagRmeu01JzBkuf/view?usp=share_link" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1e-dpiaIXGsJwcZB9LxagRmeu01JzBkuf/view?usp=share_link" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1e-dpiaIXGsJwcZB9LxagRmeu01JzBkuf/view?usp=share_link" target="_blank" rel="noopener nofollow ugc">2022-12-29-Scene.mrml</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p><a href="https://drive.google.com/drive/folders/1NysVWBosONIxftgLPQdkdu_nC0Oc6B7w?usp=share_link" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1NysVWBosONIxftgLPQdkdu_nC0Oc6B7w?usp=share_link</a></p>

---

## Post #6 by @lassoan (2022-12-29 15:40 UTC)

<p>You need to select an input <em>model</em> for the remeshing/decimation.</p>
<p>You can export the segmentation to a model using the right-click menu in the in the Data module.</p>

---

## Post #7 by @studyskin (2022-12-29 16:08 UTC)

<p>Thank you! Like I said I’m very new to this haha</p>

---

## Post #8 by @lassoan (2022-12-29 16:20 UTC)

<p>No problem at all. We would like to make the software easily usable for newcomers, so such quesrions/feedbacks are useful for us.</p>
<p>Let us know if you managed to make everything work and maybe post a screenshot of the final result. Your segmentation in the video looked very nice.</p>

---
