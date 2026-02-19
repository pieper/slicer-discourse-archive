---
topic_id: 35634
title: "New Module To Manually Align 3D Views"
date: 2024-04-20
url: https://discourse.slicer.org/t/35634
---

# New module to manually align 3D views

**Topic ID**: 35634
**Date**: 2024-04-20
**URL**: https://discourse.slicer.org/t/new-module-to-manually-align-3d-views/35634

---

## Post #1 by @muratmaga (2024-04-20 16:07 UTC)

<p>We have added a new module called <code>QuickAlign</code> to SlicerMorph. QuickAlign allows you manually orient two different 3D objects (can be both volume and model nodes), and create a synced view between them. This was initially prototyped at the <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/RenderingSupportForMultipleViews/">39th PW</a></p>
<p>We find it useful to visualize and compare scans that are acquired in different orientations without need to modify their orientation through transforms module or registration.</p>
<p>Comments/suggestions are welcome.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3bded8dc35c842598c96f4a7184fea1bc180e57.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/281570c34bd0efde36dd4802954a661bcedf2040.jpeg">
  </div><p></p>

---

## Post #2 by @mau_igna_06 (2024-04-20 16:58 UTC)

<p>Nice… I’m wondering if it would be useful to optionally output the transform that would achieve the visual synchronization</p>

---

## Post #3 by @muratmaga (2024-04-20 17:47 UTC)

<p>We thought about it, but these transforms are relative. For example if manipulate the orientation of object 1 and then object 2, they will be aligned in the viewer, but the transforms will not be of something that’s directly of use to you.</p>
<p>Nevertheless, if you start the sync view, and go to the Data module, transforms are there.</p>

---

## Post #4 by @mau_igna_06 (2024-04-20 19:09 UTC)

<p>This can be used as a manual eyeballing registration method (I just tested it) but there will be the need to add a “Pause/Resume Sync” button between “Start Sync” and “End Sync” to be able to iterate an improve the resulting transform.</p>
<p>Example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd0edb81f93e4bd1a4aa958c54df7fd8c4faa3d7.jpeg" data-download-href="/uploads/short-url/qYu4zUEGLyaa6YUiIiC00YxKQET.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd0edb81f93e4bd1a4aa958c54df7fd8c4faa3d7_2_690x389.jpeg" alt="image" data-base62-sha1="qYu4zUEGLyaa6YUiIiC00YxKQET" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd0edb81f93e4bd1a4aa958c54df7fd8c4faa3d7_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd0edb81f93e4bd1a4aa958c54df7fd8c4faa3d7_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd0edb81f93e4bd1a4aa958c54df7fd8c4faa3d7_2_1380x778.jpeg 2x" data-dominant-color="9A9CB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1083 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Note: the random transform is very different to the identity</p>
<p>This module would be useful on a surgical planning workflow for mandible reconstruction with iliac crest bone where you need to move a segment of the iliac crest to fill the salvaged mandible empty space</p>
<p>Another useful feature would be to allow interpolated opacity between the two objects (in only one 3D view) controlled by a slider</p>
<p>Hope it makes sense</p>

---

## Post #5 by @coco (2024-06-22 06:53 UTC)

<p>This is fastalign now in slicermorph I guess</p>

---

## Post #6 by @muratmaga (2024-06-22 13:40 UTC)

<p>This is called quickAlign not fastAlign.</p>

---

## Post #7 by @mau_igna_06 (2024-06-22 21:44 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="4" data-topic="35634">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>This can be used as a manual eyeballing registration method (I just tested it) but there will be the need to add a “Pause/Resume Sync” button between “Start Sync” and “End Sync” to be able to iterate an improve the resulting transform.</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a>,</p>
<p>Was that implemented? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @muratmaga (2024-06-22 21:49 UTC)

<p>No, we didnt implement that. For our applications, we dont need to be that precise and i am yet to encounter a situation where i feel like i have to iterate.</p>
<p>But if you think this will be a useful feature and have time to work on it, feel free to send a PR pause functionality add.</p>

---

## Post #9 by @coco (2024-06-23 07:15 UTC)

<p>Thanks, I could not find it in 5.6.1, nor install the module via the “install extensions”. is it in the latest version ?</p>

---

## Post #10 by @muratmaga (2024-06-23 15:12 UTC)

<p>Yes. Always use the latest stable since extensions are not updated for older ones.</p>

---
