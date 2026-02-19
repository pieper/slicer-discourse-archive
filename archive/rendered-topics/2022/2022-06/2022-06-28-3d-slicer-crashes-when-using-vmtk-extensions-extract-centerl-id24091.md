---
topic_id: 24091
title: "3D Slicer Crashes When Using Vmtk Extensions Extract Centerl"
date: 2022-06-28
url: https://discourse.slicer.org/t/24091
---

# 3D slicer crashes when using VMTK extension's extract centerline in Slicer-5.2

**Topic ID**: 24091
**Date**: 2022-06-28
**URL**: https://discourse.slicer.org/t/3d-slicer-crashes-when-using-vmtk-extensions-extract-centerline-in-slicer-5-2/24091

---

## Post #1 by @gfurnari (2022-06-28 21:49 UTC)

<p>Hi everyone,<br>
when i try to compute centerline model using extractcenterline module, both by code or manually, the software crashes everytime. I’m using 4.13.0 version for windows (i tried 5.1 version for macOS bu the problem is the same). Is there any solutions or any alternative way to compute the centerline model?<br>
(using 4.11 version the problem doesn’t show but i need to use the sandbox extension for other purposes but it is not available for this version, if i don’t get it wrong)</p>
<p>Thank you very much for your help!!</p>

---

## Post #2 by @lassoan (2022-06-28 23:27 UTC)

<p>Could you share the input model or segmentation file? (upload to dropbox/onedrive/google drive and post here the link)</p>

---

## Post #3 by @gfurnari (2022-06-29 07:45 UTC)

<p>Thank you for your quick reply <a class="mention" href="/u/lassoan">@lassoan</a>! Here’s the link:</p>
<p><a href="https://drive.google.com/drive/folders/11qqPEbOhiqVK-OjjeUgLzUT9ASrSrP_u?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/11qqPEbOhiqVK-OjjeUgLzUT9ASrSrP_u?usp=sharing</a></p>
<p>Inside the folder you can find both the vtk model and the segmentation model (i tried to compute the centerline with both).<br>
Thank you again.</p>

---

## Post #4 by @gfurnari (2022-06-30 21:43 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, i saw you tried to get access to the folder i put my models, i hope i allowed you to.</p>
<p>I wanted to ask an other question: is it possible to extract the tree curve from the network model instead of the centerline curve?<br>
Thank you very much!</p>

---

## Post #5 by @lassoan (2022-06-30 22:34 UTC)

<p>I’ve spent several hours investigating this issue. It is due to that if VMTK cannot find the path to an endpoint then it creates a line with a single-point. This was accepted in VTK-8.x but in VTK-9.x they changed the behavior so that it crashes the application. I’m working on a solution at both VTK and VMTK levels, but it is not easy, it’ll probably take a couple of days.</p>
<p>Until then, you can avoid the crash by moving the centerline endpoints to where the vessels are a bit thicker to ensure that they are accessible from the input point.</p>

---

## Post #6 by @gfurnari (2022-06-30 22:52 UTC)

<p>Ok, no problems.<br>
I really appreciate it!</p>

---

## Post #7 by @lassoan (2022-07-01 02:53 UTC)

<p>I’ve created an issue to track the resolution of this issue in VMTK’s bugtracker:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/vmtk/issues/430">
  <header class="source">

      <a href="https://github.com/vmtk/vmtk/issues/430" target="_blank" rel="noopener">github.com/vmtk/vmtk</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/vmtk/issues/430" target="_blank" rel="noopener">Centerline extraction crashes with VTK9</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-07-01" data-time="02:51:20" data-timezone="UTC">02:51AM - 01 Jul 22 UTC</span>
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
    <p class="github-body-container">Users reported centerline extraction crash in Slicer-5.1:
https://discourse.sli<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">cer.org/t/3d-slicer-crashes-when-computing-extractcenterline/24091/4</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @gfurnari (2022-07-01 07:54 UTC)

<p>Ok perfect, thank you.</p>
<p>while i wait for the solution, do you know if it would be possible to compute the tree curve centerline  using the network model as input?</p>

---

## Post #9 by @ruili (2024-01-23 14:01 UTC)

<p>Hello! I am using slicer 5.2.2 and am still experiencing this issue. I am wondering if this issue should have been fixed in slicer 5.2.2, or do I need to update anything?</p>

---

## Post #10 by @lassoan (2024-01-23 14:23 UTC)

<p>The problem is fixed in the current Slicer release. We will not provide further patch releases for Slicer-5.2, so if something does not work or you want to benefit from the lots of new features added since Slicer-5.2 then you need to upgrade to the current Slicer version.</p>

---

## Post #11 by @ruili (2024-01-23 14:25 UTC)

<p>I see. Thanks for the clarification!</p>

---
