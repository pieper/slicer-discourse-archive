---
topic_id: 2114
title: "Plus Mff What Is The Next Where I Should Post The Problem Gi"
date: 2018-02-19
url: https://discourse.slicer.org/t/2114
---

# PLUS/MFF What is the next? where I should post the problem? github/here forum?

**Topic ID**: 2114
**Date**: 2018-02-19
**URL**: https://discourse.slicer.org/t/plus-mff-what-is-the-next-where-i-should-post-the-problem-github-here-forum/2114

---

## Post #1 by @timeanddoctor (2018-02-19 13:06 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/9566f7c9999c24ede6f58356e42bb2a4dbbb4050.png" data-download-href="/uploads/short-url/ljFKyg50RqIhZaNPnkoBkUYXYB2.png?dl=1" title="" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/9566f7c9999c24ede6f58356e42bb2a4dbbb4050_2_690x374.png" alt="" data-base62-sha1="ljFKyg50RqIhZaNPnkoBkUYXYB2" role="presentation" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/9566f7c9999c24ede6f58356e42bb2a4dbbb4050_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/9566f7c9999c24ede6f58356e42bb2a4dbbb4050_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/9566f7c9999c24ede6f58356e42bb2a4dbbb4050.png 2x" data-dominant-color="C1BFC3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">1324×718 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
After active in openIGT I connected my MMF succecssfully, but I don’t know how to display in 3d slicer. Just like the picture problem.<br>
Best,<br>
Li Zhenzhu</p>

---

## Post #2 by @jamesobutler (2018-02-19 15:59 UTC)

<p>You can refer to <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ProcedureStreamingToSlicer.html" rel="noopener nofollow ugc">ProcedureStreamingToSlicer</a>.</p>
<p>Use the OpenIGTLinkIF module within Slicer 4.8.1, add a connector, you’re using the default port 18944 so you don’t need to update that within the module, and then set the status to active. Your live stream will appear as a new volume in the slice views.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37a8c15f9f8a34d32b9684ab7a936cb303a0b8e1.png" data-download-href="/uploads/short-url/7WnOGLBlFYBJUdztqmlwPTkkx7H.png?dl=1" title="plus-to-slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37a8c15f9f8a34d32b9684ab7a936cb303a0b8e1_2_690x373.png" alt="plus-to-slicer" data-base62-sha1="7WnOGLBlFYBJUdztqmlwPTkkx7H" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37a8c15f9f8a34d32b9684ab7a936cb303a0b8e1_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37a8c15f9f8a34d32b9684ab7a936cb303a0b8e1_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37a8c15f9f8a34d32b9684ab7a936cb303a0b8e1_2_1380x746.png 2x" data-dominant-color="6B6A72"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">plus-to-slicer</span><span class="informations">1920×1040 54.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2018-02-20 01:19 UTC)

<p>To learn how to use Slicer with live image and tracking data, calibrate tools, set up visualization, etc. I would suggest to complete all <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a>.</p>

---

## Post #4 by @timeanddoctor (2018-02-20 08:09 UTC)

<p>Thanks,<br>
I completed the turorials as Lassoan offered, and I have found my problem is I forgeted clicking the “centre key”.<br>
Bests,<br>
Li</p>

---

## Post #5 by @timeanddoctor (2018-02-20 08:24 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85e826175706f65da435dc0c0fa5bb65fd8e829e.png" data-download-href="/uploads/short-url/j6ASyYqb1OEF3jAk4mwyMuhO8Ee.png?dl=1" title="" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85e826175706f65da435dc0c0fa5bb65fd8e829e_2_392x500.png" alt="" data-base62-sha1="j6ASyYqb1OEF3jAk4mwyMuhO8Ee" role="presentation" width="392" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85e826175706f65da435dc0c0fa5bb65fd8e829e_2_392x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85e826175706f65da435dc0c0fa5bb65fd8e829e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85e826175706f65da435dc0c0fa5bb65fd8e829e.png 2x" data-dominant-color="D5C6C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">441×562 89.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
what I mean is load the video as a Coronal sequence not Axical.</p>

---

## Post #6 by @lassoan (2018-02-20 14:00 UTC)

<p>The fourth row of a homogeneous transformation matrix must be kept <code>0 0 0 1</code>. To swap axes, you need to swap columns of the matrix.</p>

---
