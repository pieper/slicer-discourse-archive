---
topic_id: 34992
title: "Deforming With Niftyreg Is Different Than Deforming In Slice"
date: 2024-03-20
url: https://discourse.slicer.org/t/34992
---

# Deforming with NiftyReg is different than deforming in Slicer

**Topic ID**: 34992
**Date**: 2024-03-20
**URL**: https://discourse.slicer.org/t/deforming-with-niftyreg-is-different-than-deforming-in-slicer/34992

---

## Post #1 by @koeglfryderyk (2024-03-20 16:02 UTC)

<p>I’m integrating <a href="http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg_documentation" rel="noopener nofollow ugc">NiftyReg</a> into an extension. (one of the goals is to get the computed transformation/deformation into Slicer)</p>
<p>I registered two images with <a href="http://cmictig.cs.ucl.ac.uk/wiki/index.php/Reg_f3d" rel="noopener nofollow ugc">reg_f3d</a> and saved the control point grid (to later get the deformation).</p>
<pre><code class="lang-auto">reg_f3d -ref fixed.nii -flo moving.nii -res warped.nii -cpp controlPointGrid.nii
</code></pre>
<p><br>
<br>
I then used <a href="http://cmictig.cs.ucl.ac.uk/wiki/index.php/Reg_transform" rel="noopener nofollow ugc">reg_transform</a> to get the displacement field as a .nii</p>
<pre><code class="lang-auto">reg_transform -ref fixed.nii -disp controlPointGrid.nii displacement.nii
</code></pre>
<p><br>
<br>
I then loaded the displacement.nii into Slicer as a Transform. I got the following warning, but I’m not sure if it is relevant:</p>
<blockquote>
<p>Warning: Loading /Desktop/volumes/niftyreg/displacement.nii - NIFTI file may not contain valid displacement field, the transform may be incorrect. Intent code is expected to be ‘1006’ (displacement vector), but the file contained: ‘1007’. Filename: ‘/Desktop/volumes/niftyreg/displacement.nii’.</p>
</blockquote>
<p><br>
<br>
Then I applied the transformation in Slicer to the moving image, but the result was very different (‘clearly wrong’) from the moving image transformed by NiftyReg.<br>
First screenshot is a 50/50 overlay of the NiftyReg warped image (purple) over the fixed image (green)<br>
First screenshot is a 50/50 overlay of the Slicer transformed image (purple) over the fixed image (green)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa987aa9b0413b6e73cd877af3dfc560aa8b4e68.jpeg" data-download-href="/uploads/short-url/ol9R0OTUEiyegu04Vz6SgKqwRba.jpeg?dl=1" title="Screenshot from 2024-03-20 16-58-02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa987aa9b0413b6e73cd877af3dfc560aa8b4e68_2_690x445.jpeg" alt="Screenshot from 2024-03-20 16-58-02" data-base62-sha1="ol9R0OTUEiyegu04Vz6SgKqwRba" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa987aa9b0413b6e73cd877af3dfc560aa8b4e68_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa987aa9b0413b6e73cd877af3dfc560aa8b4e68_2_1035x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa987aa9b0413b6e73cd877af3dfc560aa8b4e68_2_1380x890.jpeg 2x" data-dominant-color="373841"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-03-20 16-58-02</span><span class="informations">1904×1230 93 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61ce865427002982e47ac135f1df173847dfe250.jpeg" data-download-href="/uploads/short-url/dXeN5Ide9PwFbluAkI16gBl34I0.jpeg?dl=1" title="Screenshot from 2024-03-20 16-58-43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61ce865427002982e47ac135f1df173847dfe250_2_690x445.jpeg" alt="Screenshot from 2024-03-20 16-58-43" data-base62-sha1="dXeN5Ide9PwFbluAkI16gBl34I0" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61ce865427002982e47ac135f1df173847dfe250_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61ce865427002982e47ac135f1df173847dfe250_2_1035x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61ce865427002982e47ac135f1df173847dfe250_2_1380x890.jpeg 2x" data-dominant-color="373841"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-03-20 16-58-43</span><span class="informations">1904×1230 97.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><br>
<br>
I’m not sure if the displacement field is somehow encoded differently/incorrectly or if I’m missing some steps in between. (the author of NiftyReg mentioned that “Note that the transformation are encoded from the reference to the floating space and all is stored in physical space (mm) rather than voxel space.” - not sure if this is relevant here)</p>
<p><br>
<br>
Here’s a <a href="https://www.dropbox.com/scl/fo/wi3u01njtyzokhzehi7jg/h?rlkey=0obw9hopx99jtefbyaphn09nl&amp;dl=0" rel="noopener nofollow ugc">link to all the volumes</a></p>

---

## Post #2 by @lassoan (2024-03-20 22:58 UTC)

<p>Due to using a wrong intent code, the ITK reader does not know that the vectors store spatial displacement and therefore the vectors are not converted to the correct coordinate system.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITK/commit/d007ee8e78ab367d10a4fc116fceb4ba07604174">
  <header class="source">

      <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/d007ee8e78ab367d10a4fc116fceb4ba07604174" target="_blank" rel="noopener">github.com/InsightSoftwareConsortium/ITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/d007ee8e78ab367d10a4fc116fceb4ba07604174" target="_blank" rel="noopener">BUG: Fix read/write of displacement field in NIFTI file format</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-01-26" data-time="01:45:10" data-timezone="UTC">01:45AM - 26 Jan 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 3 files with 177 additions and 9 deletions">
        <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/d007ee8e78ab367d10a4fc116fceb4ba07604174" target="_blank" rel="noopener">
          <span class="added">+177</span>
          <span class="removed">-9</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">NIFTI image containing displacement field (intent = 1006) was incorrectly read a<span class="show-more-container"><a href="https://github.com/InsightSoftwareConsortium/ITK/commit/d007ee8e78ab367d10a4fc116fceb4ba07604174" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">s scalar volume (all 3 vector components were set to the same value).

Fixed by reading NIFTI displacement vector files similarly to general-purpose vector images. For displacement vector files,
vector components are converted between NIFTI file's RAS coordinate system and ITK's LPS coordinate system,
unless this conversion is explicitly disabled by setting ConvertRASDisplacementVectors to false.

An ITK vector image can be written as NIFTI displacement vector file by setting "intent_code"="1006" in the metadata dictionary of the image.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>VoxelMorph had a <a href="https://github.com/voxelmorph/voxelmorph/issues/438">similar issue</a>. If niftyreg developers cannot fix the problem quickly then you can patch the nifti file similarly to how it is described in the voxelmorph issue.</p>

---

## Post #3 by @koeglfryderyk (2024-03-21 07:57 UTC)

<p>The problem was a bit simpler - the displacement field from NiftiReg already had the correct shape, I only had to change the intent code</p>

---

## Post #4 by @lassoan (2024-03-22 01:23 UTC)

<aside class="quote no-group" data-username="koeglfryderyk" data-post="3" data-topic="34992">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p>I only had to change the intent code</p>
</blockquote>
</aside>
<p>Great! Please report the issue to NiftyReg maintainers and copy the link to the issue here for future reference. Thank you!</p>

---
