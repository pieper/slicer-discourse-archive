---
topic_id: 45803
title: "Auto3Dgm Landmark Placement On Invisible Parts Of Mesh"
date: 2026-01-16
url: https://discourse.slicer.org/t/45803
---

# Auto3dgm landmark placement on invisible parts of mesh 

**Topic ID**: 45803
**Date**: 2026-01-16
**URL**: https://discourse.slicer.org/t/auto3dgm-landmark-placement-on-invisible-parts-of-mesh/45803

---

## Post #1 by @raranda22 (2026-01-16 22:11 UTC)

<p>Hello Slicer Community,</p>
<p>I’m using Auto3dgm on segmented upper beaks from MarkMyBird database, but it appears landmarks are being placed on seemingly invisible parts of the segmented meshes!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce004b0ad5ff2acab82120c1f00088f2a7a74dd.jpeg" data-download-href="/uploads/short-url/A52hkKCXSaGKVwobqNBc1YS3bUp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce004b0ad5ff2acab82120c1f00088f2a7a74dd_2_517x234.jpeg" alt="image" data-base62-sha1="A52hkKCXSaGKVwobqNBc1YS3bUp" width="517" height="234" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce004b0ad5ff2acab82120c1f00088f2a7a74dd_2_517x234.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce004b0ad5ff2acab82120c1f00088f2a7a74dd_2_775x351.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce004b0ad5ff2acab82120c1f00088f2a7a74dd_2_1034x468.jpeg 2x" data-dominant-color="B3B3D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1810×823 98.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here are the original unsegmented meshes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17d4d18c855db5fb97880e90b71a8d616b90ca1f.jpeg" data-download-href="/uploads/short-url/3oOWuFlQ8pEdPKzmJdftP4jN5Uj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17d4d18c855db5fb97880e90b71a8d616b90ca1f_2_241x250.jpeg" alt="image" data-base62-sha1="3oOWuFlQ8pEdPKzmJdftP4jN5Uj" width="241" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17d4d18c855db5fb97880e90b71a8d616b90ca1f_2_241x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17d4d18c855db5fb97880e90b71a8d616b90ca1f_2_361x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17d4d18c855db5fb97880e90b71a8d616b90ca1f_2_482x500.jpeg 2x" data-dominant-color="B0B18A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">706×731 93.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b7c15a9353d2d0a9609a7982d91ecff58f2a16c.jpeg" data-download-href="/uploads/short-url/8ue1i0A7E2PmsdZru9ca0275ZCY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b7c15a9353d2d0a9609a7982d91ecff58f2a16c_2_345x207.jpeg" alt="image" data-base62-sha1="8ue1i0A7E2PmsdZru9ca0275ZCY" width="345" height="207" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b7c15a9353d2d0a9609a7982d91ecff58f2a16c_2_345x207.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b7c15a9353d2d0a9609a7982d91ecff58f2a16c_2_517x310.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b7c15a9353d2d0a9609a7982d91ecff58f2a16c_2_690x414.jpeg 2x" data-dominant-color="AAAB87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">928×558 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here’s how I segmented the meshes: I used Plane Cut tool in Dynamic Modeler, using a 2D plane placed vertically at approximately where the beak begins. I exported the desired segment as an .obj file. Interestingly, using either DeCAL or BUILDER module as part of ATLAS, they seem to respect the posterior boundary of the mesh (but they’re not without other issues with these meshes):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7a456c78d47136d7ab62b911ef20990d64c798d.jpeg" data-download-href="/uploads/short-url/qcztfmpFSsDWbVje5SDRP0U9T0V.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7a456c78d47136d7ab62b911ef20990d64c798d_2_244x250.jpeg" alt="image" data-base62-sha1="qcztfmpFSsDWbVje5SDRP0U9T0V" width="244" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7a456c78d47136d7ab62b911ef20990d64c798d_2_244x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7a456c78d47136d7ab62b911ef20990d64c798d_2_366x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7a456c78d47136d7ab62b911ef20990d64c798d_2_488x500.jpeg 2x" data-dominant-color="AFAF95"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">634×649 61.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any help would be greatly appreciated!</p>
<p>Best,</p>
<p>Ricardo Ely</p>

---

## Post #2 by @muratmaga (2026-01-16 23:10 UTC)

<p>I think that extension is abandoned, I don’t think anyone in the development team tracks this forum. You might try opening an issue on their github repo <a href="https://github.com/ToothAndClaw/SlicerAuto3dgm" class="inline-onebox" rel="noopener nofollow ugc">GitHub - ToothAndClaw/SlicerAuto3dgm: Repo for auto3dgm slicer extension</a> but they don’t appear to be responsive.</p>
<p>I think if you use Dynamic modeler to cut a model, it removes the vertices but not the points. We encountered. that in other application. I opened an issue, <a href="https://github.com/Slicer/Slicer/issues/8777" class="inline-onebox" rel="noopener nofollow ugc">Dynamic modeler ROI cut removes the polygons but not the vertices · Issue #8777 · Slicer/Slicer · GitHub</a></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> maybe it is time to implement that clean option.</p>

---

## Post #3 by @lassoan (2026-01-17 13:27 UTC)

<p>OK, I’ll add the clean option in the next few days.</p>

---

## Post #4 by @raranda22 (2026-01-17 18:05 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> That would be amazing, thank you!</p>

---

## Post #5 by @lassoan (2026-01-18 15:10 UTC)

<p>I’ve pushed a fix, it is under review.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/SlicerSurfaceToolbox/pull/85">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/85" target="_blank" rel="noopener">github.com/Slicer/SlicerSurfaceToolbox</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/85" target="_blank" rel="noopener">Remove orphan points from Dynamic Modeler ROI Cut and Plane Cut outputs</a>
      </h4>

    <div class="branches">
      <code>master</code> ← <code>lassoan:fix-vtkClipPolyData-output</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-01-18" data-time="15:06:40" data-timezone="UTC">03:06PM - 18 Jan 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 6 files with 53 additions and 5 deletions">
          <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/85/files" target="_blank" rel="noopener">
            <span class="added">+53</span>
            <span class="removed">-5</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Dynamic Modeler module's ROI Cut tool and Plane Cut tool use vtkClipPolyData, wh<span class="show-more-container"><a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/85" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ich can leave orphan points (points that are not used in any cells) in its output. The points are not exactly the same as the input points (coordinates are, but point IDs are not) and they are only preserved in certain cases (e.g., when clipped points are requested), therefore the orphan points are not reliable usable for anything and so they are not worth preserving. This is confirmed by testing the filter and also discussed at https://discourse.vtk.org/t/vtkclippolydata-has-different-behaviors-in-vtk-8-2-0-and-in-vtk-9-4-0/15626.

Since having orphan points in the output is unexpected and caused errors in subsequent processing, clean polydata filter is applied to the output to remove the orphan points.

fixes https://github.com/Slicer/Slicer/issues/8777</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2026-01-19 02:16 UTC)

<p>The fix is integrated. Slicer Preview Releases (downloaded tomorrow or later) will not have invisible orphan points in the outputs of ROI cut and Plane cut tools.</p>

---

## Post #7 by @raranda22 (2026-01-20 10:59 UTC)

<p>Thank you for implementing those fixes! I was just about to download the preview release for Windows, but it seems that version is from 01/15, while Linux and mac are 01/19? I run 3D Slicer on Windows.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4890d13b6a7d98323d515a341ace2f6d86bab8d.png" data-download-href="/uploads/short-url/ukaQY1oLCrVArVyacQBhPbVrJ13.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4890d13b6a7d98323d515a341ace2f6d86bab8d.png" alt="image" data-base62-sha1="ukaQY1oLCrVArVyacQBhPbVrJ13" width="690" height="336" data-dominant-color="F5F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">936×457 17.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @cpinter (2026-01-20 12:54 UTC)

<p>It seems the last build succeeded on all platforms. Click the package button in the Windows line and you can download the installer (apparently the download site hasn’t updated itself yet).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5834d500ee6cb9ea07791c0ec6e5cd0b2d4a719.png" data-download-href="/uploads/short-url/nCc5WvYvq6X0ooMWEVF1clIEgad.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5834d500ee6cb9ea07791c0ec6e5cd0b2d4a719_2_690x92.png" alt="image" data-base62-sha1="nCc5WvYvq6X0ooMWEVF1clIEgad" width="690" height="92" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5834d500ee6cb9ea07791c0ec6e5cd0b2d4a719_2_690x92.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5834d500ee6cb9ea07791c0ec6e5cd0b2d4a719_2_1035x138.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5834d500ee6cb9ea07791c0ec6e5cd0b2d4a719.png 2x" data-dominant-color="B9C2CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1335×179 22.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2026-01-20">
  <header class="source">
      <img src="https://slicer.cdash.org/favicon.ico" class="site-icon" alt="" width="32" height="32">

      <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2026-01-20" target="_blank" rel="noopener">slicer.cdash.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2026-01-20" target="_blank" rel="noopener">SlicerPreview</a></h3>

  <p>
            CDash is an open source, web-based software testing server. CDash aggregates, analyzes, and displays the
            results of software testing processes submitted from clients located around the world. CDash is a part of a
           ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please keep in mind that for such a recent preview you may need to wait a bit for all the extensions be available.</p>

---

## Post #9 by @lassoan (2026-01-20 18:29 UTC)

<p>The download page now shows 2026-01-20 for Slicer Preview Releases for all platforms. This version contains the fix.</p>

---

## Post #10 by @raranda22 (2026-01-21 15:55 UTC)

<p>Hello all,</p>
<p>Auto3dgm works now with the new fix. Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for taking the time to address this issue!</p>
<p>Best,</p>
<p>Ricardo Ely</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f41f4934448bb66b743ec08215dbd82f6f6602ec.jpeg" data-download-href="/uploads/short-url/yPBx1saSiuOixWKDHtLBwS6nJIE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f41f4934448bb66b743ec08215dbd82f6f6602ec.jpeg" alt="image" data-base62-sha1="yPBx1saSiuOixWKDHtLBwS6nJIE" width="421" height="496"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">421×496 41.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @muratmaga (2026-01-21 16:21 UTC)

<p>If you look at the clipped surface, I think you will see many point there? You might want to consider there having points in a completely arbitrary and flat surface makes biological sense in your geometric analysis.</p>

---

## Post #12 by @raranda22 (2026-01-21 16:33 UTC)

<p>I made sure to uncheck the option for capping a surface under the Plane Cut tool, forcing landmarks to fall on the surface mesh.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38cb24427c4159be05091c28bc5e527364c96120.jpeg" data-download-href="/uploads/short-url/86pXYiN520bUxyaFQ7eIHCBTykE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38cb24427c4159be05091c28bc5e527364c96120_2_395x500.jpeg" alt="image" data-base62-sha1="86pXYiN520bUxyaFQ7eIHCBTykE" width="395" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38cb24427c4159be05091c28bc5e527364c96120_2_395x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38cb24427c4159be05091c28bc5e527364c96120_2_592x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38cb24427c4159be05091c28bc5e527364c96120.jpeg 2x" data-dominant-color="A09397"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">665×840 88.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @raranda22 (2026-01-22 10:02 UTC)

<p>On second thought, regarding how much biological sense my procedure makes, while I made sure to leave the clipped surface uncapped, I’m now slightly concerned about landmarks falling on the clipped edges. I may be overthinking this too much, but the criteria for cutting the mesh along that specific plane is the part of the beak that is anterior to the nasals. The angle of the plane is determined by a PCA of the specimen’s landmarks themselves (for the most part). Any thoughts?</p>

---

## Post #14 by @muratmaga (2026-01-22 16:39 UTC)

<p>I don’t think you will be concerned on points falling on the clipped surface. The question is now  consistent and repeatable the clipping is.</p>

---
