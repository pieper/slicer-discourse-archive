---
topic_id: 10501
title: "Slicer Is Duplicating Files On Upload"
date: 2020-03-02
url: https://discourse.slicer.org/t/10501
---

# Slicer is duplicating files on upload

**Topic ID**: 10501
**Date**: 2020-03-02
**URL**: https://discourse.slicer.org/t/slicer-is-duplicating-files-on-upload/10501

---

## Post #1 by @fullerkj (2020-03-02 16:45 UTC)

<p>Hello!<br>
When I upload a directory into Slicer, I am having a problem where my files (segmentation, transform, etc) are being duplicated on upload.  I’m not quite sure what is causing these files to duplicate.  I have attached a picture below showing what I think I’m importing vs. what is showing up when I import this directory:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b233f52ec3674111a64174baebeb92f2b96b2be4.png" data-download-href="/uploads/short-url/pqsj8CBEnwlfPLk2DzS3RUF1byQ.png?dl=1" title="Selection_034" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b233f52ec3674111a64174baebeb92f2b96b2be4_2_690x304.png" alt="Selection_034" data-base62-sha1="pqsj8CBEnwlfPLk2DzS3RUF1byQ" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b233f52ec3674111a64174baebeb92f2b96b2be4_2_690x304.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b233f52ec3674111a64174baebeb92f2b96b2be4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b233f52ec3674111a64174baebeb92f2b96b2be4.png 2x" data-dominant-color="EEEDEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Selection_034</span><span class="informations">947×418 52.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5382717ff327c4ac309724d430a3875bf34a13a7.png" data-download-href="/uploads/short-url/bUL6qrGTAIfQTXpybYnJrYvJ01x.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5382717ff327c4ac309724d430a3875bf34a13a7_2_377x500.png" alt="image" data-base62-sha1="bUL6qrGTAIfQTXpybYnJrYvJ01x" width="377" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5382717ff327c4ac309724d430a3875bf34a13a7_2_377x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5382717ff327c4ac309724d430a3875bf34a13a7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5382717ff327c4ac309724d430a3875bf34a13a7.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">483×640 48.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If anyone has any ideas regarding what is causing this problem, or what I might be doing wrong when saving or uploading these files I would be most grateful!</p>

---

## Post #2 by @lassoan (2020-03-02 17:53 UTC)

<p>Most likely, you have a scene (.mrml) file selected among the files, which loads all the nodes anyway. I would recommend to just load the .mrml file. You can also save the scene in a single file, by clicking the “package” icon in the save data dialog.</p>

---
