# Scalar Color Mapping has too many control points

**Topic ID**: 31741
**Date**: 2023-09-15
**URL**: https://discourse.slicer.org/t/scalar-color-mapping-has-too-many-control-points/31741

---

## Post #1 by @muratmaga (2023-09-15 16:32 UTC)

<p>In the latest stable on Linux, when I enable volume rendering in one of my 16 bit scans (without using a preset), too many control points on the scalar color map is created.</p>
<p>This makes it too tedious to reorganize colors. Is used to be 4-5 points as I recall. Is there a reason why it has increased so much.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/867712af53a97ce1bf26045c11a6f28e235b80eb.jpeg" data-download-href="/uploads/short-url/jbx5OkQsflGEDvAIU3lXR8uI9v5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/867712af53a97ce1bf26045c11a6f28e235b80eb_2_327x500.jpeg" alt="image" data-base62-sha1="jbx5OkQsflGEDvAIU3lXR8uI9v5" width="327" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/867712af53a97ce1bf26045c11a6f28e235b80eb_2_327x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/867712af53a97ce1bf26045c11a6f28e235b80eb_2_490x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/867712af53a97ce1bf26045c11a6f28e235b80eb_2_654x1000.jpeg 2x" data-dominant-color="D8D9DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">823×1256 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-09-15 18:00 UTC)

<p>The change was necessary to ensure that the volume’s color map is copied to volume rendering color transfer function with acceptable accuracy. We had to find a balance between sufficient color reproduction and the ability to manually edit the color mapping, that’s why the number of control points are limited to 24. See detailed description here:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/35e5586bdb6749376864522b20a2dfda5dab33fc">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/35e5586bdb6749376864522b20a2dfda5dab33fc" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/35e5586bdb6749376864522b20a2dfda5dab33fc" target="_blank" rel="noopener">BUG: Fix color synchronization inaccuarcy in volume rendering module</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-06-27" data-time="18:04:41" data-timezone="UTC">06:04PM - 27 Jun 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 2 files with 88 additions and 61 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/35e5586bdb6749376864522b20a2dfda5dab33fc" target="_blank" rel="noopener">
          <span class="added">+88</span>
          <span class="removed">-61</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When a color node with few color table entries (such as fMRI) was used for showi<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/35e5586bdb6749376864522b20a2dfda5dab33fc" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ng a volume, the "Synchronize with Volumes module" button in volume rendering module very inaccurately copied the color entries to the color transfer function. The problem was that only every 64th color table entry was copied. Fixed the issue by copying up to 24 color entries (evenly sampled in the lookup table) of the table into the transfer function. This number is large enough to accurately represent a color table, but not too high so that users can still edit the color transfer manually.

Also fixed synchronization of continuous color mapping. All control points of continuous color maps are copied, so these are copied in full fidelity.

Fixes the problem reported at https://discourse.slicer.org/t/the-colormap-in-volume-rendering-is-wrong-when-using-fmri-lookup-table-in-volume/30186</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>What could be improved is to change the trivial 256-entry color tables (vtkMRMLColorTableNode) to procedural color nodes (vtkMRMLProceduralColorNode), which define a color transfer function by a few control points. For example, the 256 table items of the gray color node could be replaced by a color transfer function that contains 2 control points. Control points of procedural color nodes are copied to volume rendering transfer functions and they remain easily editable there, because these color maps are typically defined by just a few control points.</p>

---

## Post #3 by @muratmaga (2023-09-15 18:12 UTC)

<p>The issue is there is no easy way of removing multiple control points quickly. It requires a lot of mouse clicks to remove them one by one.</p>
<p>For these smooth colors (e.g. gray), only the 3-4 control points would suffice (in fact right at the same control point spots at where the ramp for opacity map is.</p>

---

## Post #4 by @lassoan (2023-09-15 18:25 UTC)

<p>It is really easy to delete control points: click on one and keep hitting Delete key until all unnedded control points are gone. It takes about 10 seconds to delete all the 24 control points.</p>
<p>Indeed, most of the color maps are “smooth” and can be described by 2 to 5 control points. As I described above, they could be replaced by color transfer functions, but someone would need to reverse-engineer them: determine what control points and color space choice reproduce the original table values.</p>

---

## Post #5 by @muratmaga (2023-09-15 18:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="31741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It is really easy to delete control points: click on one and keep hitting Delete key until all unnedded control points are gone. It takes about 10 seconds to delete all the 24 control points.</p>
</blockquote>
</aside>
<p>Thats a lot of clicks, and the main problem it is not a one-time thing, you have to do it again and again for every new transfer function you are creating.</p>
<p>As a comprise could be possible to do a right-mouse click option that says “remove all control points”. Because it would be way faster to add 3-4 points on where you want them to be than to remove 20 one by one.</p>

---

## Post #6 by @lassoan (2023-09-15 19:11 UTC)

<p>Making removing all control points easier might be an acceptable workaround for some use cases and for some color maps. However, it would be better to address the root cause of the issue: use the minimum necessary number of control points to define a color map. That would allow convenient editing without losing any information.</p>
<p>Are you only interested in the gray colormap?</p>

---

## Post #7 by @muratmaga (2023-09-15 19:20 UTC)

<p>Most often for microCT we start with gray and then adjust colors.</p>

---

## Post #8 by @lassoan (2023-09-15 21:44 UTC)

<p>Aren’t the uCT… presets good enough as a starting point? If you can detect a micro-CT automatically then you can write a Subject Hierarchy plugin that sets up volume rendering using a uCT preset by default.</p>

---

## Post #9 by @muratmaga (2023-09-15 22:42 UTC)

<p>Those can be good enough starting points for mineralized tissue scans, but ultimately there is wide range of intensities based on voltage, filter and (if used) contrast solution.</p>

---

## Post #10 by @lassoan (2023-09-16 19:15 UTC)

<p>It seems that the goal is not to copy the window-level preset but to make it easier to create good volume rendering transfer functions. To achieve this, we could add more volume rendering presets, and maybe we could also develop a new feature: applying window/level used in n the slice view to shift/scale the volume rendering transfer functions.</p>

---
