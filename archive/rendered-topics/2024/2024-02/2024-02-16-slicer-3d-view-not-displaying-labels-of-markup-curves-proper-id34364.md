# Slicer 3D view not displaying labels of markup curves properly

**Topic ID**: 34364
**Date**: 2024-02-16
**URL**: https://discourse.slicer.org/t/slicer-3d-view-not-displaying-labels-of-markup-curves-properly/34364

---

## Post #1 by @ruili (2024-02-16 14:38 UTC)

<p>Hello,</p>
<p>I am writing to report what seems to be a bug with the labelling of centerline curves or markup curves in general in the 3D view. The details of this bug can be found in a previous discussion <a href="https://discourse.slicer.org/t/vmtk-extract-centerline-with-python-console/31596/14">here</a>. But to summarise, there are two main problems:</p>
<ol>
<li>When generating centerline curves using the ‘ExtractCenterline’ module from VMTK, if your 3D view is zoomed and does not show the full segmentation structure, only those curves that are included in your current view will be labelled in the 3D view.</li>
<li>Even when the curves are labelled initially, if you save the curves either as a .mrk.json file or the whole scene in a mrml or mrb file, when reloading it, no markup curve will be labelled in the 3D view.</li>
</ol>
<p>To replicate the first problem, you may use <a href="https://drive.google.com/file/d/1eTTquFSzlJC8Ioq7qHEl590RjKiD5uNs/view?usp=sharing" rel="noopener nofollow ugc">this</a> scene with a segmentation and re-run the ExtractCenterline module. To replicate the second problem, you may use the same file or just draw any mark up curve in slicer and try saving and reloading it.</p>
<p>I will appreciate it very much if anyone can help me check if this is indeed a bug and fix it if it is!</p>

---

## Post #2 by @ruili (2024-03-29 10:51 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> <a class="mention" href="/u/mikebind">@mikebind</a> Hi! This request of mine seems to have been largely ignored, but I will still appreciate some help with it from the experts, as it is very annoying to have extracted and saved the curves and to be unable to see their labels in the 3D view when loading them later.</p>

---

## Post #3 by @chir.set (2024-03-29 11:40 UTC)

<p>I noticed that too, like in the picture below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97fbe63f650ede3a254485e90f53dbb77d74a1b1.png" data-download-href="/uploads/short-url/lGvMYQKpeYriMvAAjq5pt4Eu23v.png?dl=1" title="Copie d'écran_20240329_122009" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97fbe63f650ede3a254485e90f53dbb77d74a1b1_2_303x500.png" alt="Copie d'écran_20240329_122009" data-base62-sha1="lGvMYQKpeYriMvAAjq5pt4Eu23v" width="303" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97fbe63f650ede3a254485e90f53dbb77d74a1b1_2_303x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97fbe63f650ede3a254485e90f53dbb77d74a1b1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97fbe63f650ede3a254485e90f53dbb77d74a1b1.png 2x" data-dominant-color="131612"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Copie d'écran_20240329_122009</span><span class="informations">339×559 59.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I don’t think it would be considered a bug by core developers, i.e, it’s doubtful they would spend time tracking the root cause.</p>
<p>There are other glitches. For example, with a double 3D view layout, if I apply a volume rendering then display the ROI, the resizing handles appear in the slice views, but would next disappear in the green and yellow views when the mouse cursor is over them. They persist in the red view only. I did not report it since there are other ways to resize the ROI and it does not result in an unusable workspace.</p>
<p>So I think thet one has to accept the kind of unexpected observation you described as it is; or convince some core developer to look into it.</p>

---

## Post #4 by @lassoan (2024-03-29 13:11 UTC)

<p>Sorry for the slow response, we just have not had the chance to get to this. There is indeed something wrong with the initialization of the property label when all the control points are hidden.</p>
<p>A workaround until we fix the issue is to show and hide a control point; or enable occluded visibility.</p>
<p>Since the problem is 100% reproducible I expect that we can fix it very quickly.</p>

---

## Post #5 by @lassoan (2024-03-29 14:09 UTC)

<p>Unfortunately, the problem is not so simple. It is actually a feature that a curve label is not displayed if none of the curve points are visible in the current 3D view. The check if the curve points are visible is done by checking if there is any control point that is not occluded. Occlusion check is expensive and so it is only done if a control point is visible, otherwise the previous result of the occlusion check will be used. This is not a good choice, as the curve may become visible or occluded while none of the control points are shown. If we turn off the occlusion check then the curve label would be always visible, which would mean all curve names would always be visible in all 3D views, regardles if the curve is occluded or not.</p>
<p>For now, you can force display of the property label by enabling occluded visibility or show one control point.</p>
<p>I’ve added an issue to make determination of curve visibility better:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7665">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7665" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7665" target="_blank" rel="noopener">Curve title is not visible in 3D if all control points are hidden</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-03-29" data-time="14:06:00" data-timezone="UTC">02:06PM - 29 Mar 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

A curve's properties label is not displayed if none of the curve p<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">oints are visible in the current 3D view. However, someone may want to show just a curve without any control points (e.g., because it is a curve with many control points and the control points would clutter the view).

https://discourse.slicer.org/t/slicer-3d-view-not-displaying-labels-of-markup-curves-properly/34364/3

## Steps to reproduce

- Create a curve =&gt; properties label is visible in 3D view, showing the node's name
- Hide all control points
- Save scene, close scene, load the saved scene =&gt; properties label is not visible =&gt; ERROR: the label should be visible

## Environment
- Slicer version: Slicer-5.7.0-2024-03-28
- Operating system: Windows</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @ruili (2024-04-26 16:16 UTC)

<p>Thank you for checking this!</p>
<blockquote>
<p>you can force display of the property label by enabling occluded visibility</p>
</blockquote>
<p>Can I please ask where I can change this setting? The other option to show one control point for each curve might be too troublesome for me, as I have many curves to load.</p>

---
