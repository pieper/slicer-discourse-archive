---
topic_id: 33341
title: "Roi Markup Is Not Filled With Color In Coronal View In Slice"
date: 2023-12-11
url: https://discourse.slicer.org/t/33341
---

# ROI markup is not filled with color in coronal view in Slicer 5.6.0

**Topic ID**: 33341
**Date**: 2023-12-11
**URL**: https://discourse.slicer.org/t/roi-markup-is-not-filled-with-color-in-coronal-view-in-slicer-5-6-0/33341

---

## Post #1 by @Maya_Kiperwas_Gal (2023-12-11 15:52 UTC)

<p>Problem report for Slicer 5.6.0 win-amd64: ROI markup is not filled with color in coronal view</p>
<p>5.6.0 (revision 32390 / 0a13b9c) win-amd64 - installed release<br>
Windows /  Professional / (Build 19045, Code Page 65001) - 64-bit</p>

---

## Post #2 by @pieper (2023-12-11 16:28 UTC)

<p>Thanks for the report.  That is odd.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ad6018b830648be25aca2217556311538f7d269.jpeg" data-download-href="/uploads/short-url/1xRhojKSdglQrTG0iSTQy0vQdCN.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad6018b830648be25aca2217556311538f7d269_2_689x341.jpeg" alt="image" data-base62-sha1="1xRhojKSdglQrTG0iSTQy0vQdCN" width="689" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad6018b830648be25aca2217556311538f7d269_2_689x341.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad6018b830648be25aca2217556311538f7d269_2_1033x511.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ad6018b830648be25aca2217556311538f7d269.jpeg 2x" data-dominant-color="51524B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1148×568 66.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @shai-ikko (2024-09-12 08:00 UTC)

<p>I’m seeing the same thing here, Linux (Ubuntu 20.04), on both 5.6.2 and 5.4.0. I’ve only recently started to play with ROIs.</p>
<p>I was under the impression that it didn’t start this way, so I tried moving aside <code>.config/slicer.org/Slicer.ini</code> and removing <code>.slicerrc.py</code> (just to be on the safe side, as it was only comments anyway), but it didn’t change anything.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd0af014c751cd45ab3cc4d42188adaad7e1ba02.jpeg" data-download-href="/uploads/short-url/tfTjzbZoliNOXvyG68IHKKHmg6e.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd0af014c751cd45ab3cc4d42188adaad7e1ba02_2_690x423.jpeg" alt="image" data-base62-sha1="tfTjzbZoliNOXvyG68IHKKHmg6e" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd0af014c751cd45ab3cc4d42188adaad7e1ba02_2_690x423.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd0af014c751cd45ab3cc4d42188adaad7e1ba02_2_1035x634.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd0af014c751cd45ab3cc4d42188adaad7e1ba02_2_1380x846.jpeg 2x" data-dominant-color="594649"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1488×914 84.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve also tried to see if this was related to the slice view being Green or the fact that it’s coronal – by switching the viewers’ slice orientations – and it is, indeed, the coronal.</p>
<p>(I’m wondering if this could somehow be related to locale or timezone, <a class="mention" href="/u/maya_kiperwas_gal">@Maya_Kiperwas_Gal</a> seems to be in Israel like me; starting the app with <code>LANG=en_US LANGUAGE=en_US LC_ALL=en_US TZ=UTC</code> didn’t change anything either)</p>

---

## Post #4 by @pieper (2024-09-12 13:47 UTC)

<p>It’s not timezone related since it happens to me too in the US.  It seems to just be a bug that someone will need to investigate.</p>

---

## Post #5 by @lassoan (2024-09-12 14:45 UTC)

<p>Please test with the latest Slicer Preview Release, too.</p>

---

## Post #6 by @jamesobutler (2024-09-12 15:01 UTC)

<p>Latest Slicer preview (as of <a href="https://github.com/Slicer/Slicer/commit/d803d347e0dbd0ea825ddd4afa551deb7676e9d5" rel="noopener nofollow ugc">d803d34</a>):</p>
<pre data-code-wrap="python"><code class="lang-python">slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)
roi_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
roi_node.SetSize([100, 100, 100])
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f59bb51faed4f624e5df7a0ac6259ee545cc246e.png" data-download-href="/uploads/short-url/z2KA5tYUICqYoA780iC7uIPgxEa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f59bb51faed4f624e5df7a0ac6259ee545cc246e_2_690x370.png" alt="image" data-base62-sha1="z2KA5tYUICqYoA780iC7uIPgxEa" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f59bb51faed4f624e5df7a0ac6259ee545cc246e_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f59bb51faed4f624e5df7a0ac6259ee545cc246e_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f59bb51faed4f624e5df7a0ac6259ee545cc246e_2_1380x740.png 2x" data-dominant-color="9A989B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1032 83.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @shai-ikko (2024-09-18 14:58 UTC)

<p>Right, I somehow misread the December messages. Sorry.</p>

---

## Post #8 by @shai-ikko (2024-09-18 15:08 UTC)

<p>I don’t see this reported as an issue on Github – will reporting it there help, or is it just noise?</p>

---

## Post #9 by @pieper (2024-09-18 16:07 UTC)

<p>I think and issue on github makes sense.  I just tested and it’s still an issue on my local build.</p>

---

## Post #10 by @jamesobutler (2024-09-18 16:38 UTC)

<p>I’ve added this to the Slicer issue tracker:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7944">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7944" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7944" target="_blank" rel="noopener nofollow ugc">Markups ROI not shown with fill opacity for Coronal slice orientation</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-09-18" data-time="16:38:21" data-timezone="UTC">04:38PM - 18 Sep 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

As originally reported at https://discourse.slicer.org/t/roi-marku<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">p-is-not-filled-with-color-in-coronal-view-in-slicer-5-6-0/33341:

A Markups ROI object with a visible 2D fill opacity shows that there an issue with the display of that fill when the slice orientation is "Coronal". 

## Steps to reproduce
```python
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)
roi_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
roi_node.SetSize([100, 100, 100])
```
![image](https://github.com/user-attachments/assets/a73761e2-9e34-4eef-a4e6-168fc309b9d1)


## Environment
- Slicer version: Slicer-5.7.0-2024-09-17 (as of https://github.com/Slicer/Slicer/commit/114731d5f71167f1a2da81ed2494c8201d6a1654)
- Operating system: Windows, an issue on Linux and likely on macOS as well</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @mikebind (2024-09-18 16:47 UTC)

<p>I did a little checking, and if you rotate the ROI, it appears that 2 of the 6 faces of the ROI show as unfilled.  The appearance of unfilled ROI shapes is not limited to the coronal/green slice, and rotates with the ROI, and can therefore show up in any of the slice views. Just FYI for anyone who might start taking a look at debugging this.</p>

---

## Post #12 by @shai-ikko (2024-11-04 09:20 UTC)

<p>This has been fixed; the fix is already included in the latest preview release.</p>
<p>Thanks a lot to everyone involved!</p>

---
