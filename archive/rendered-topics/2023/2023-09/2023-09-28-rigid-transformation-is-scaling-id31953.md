---
topic_id: 31953
title: "Rigid Transformation Is Scaling"
date: 2023-09-28
url: https://discourse.slicer.org/t/31953
---

# Rigid Transformation is-- scaling?

**Topic ID**: 31953
**Date**: 2023-09-28
**URL**: https://discourse.slicer.org/t/rigid-transformation-is-scaling/31953

---

## Post #1 by @Beth_Bearce (2023-09-28 20:53 UTC)

<p>Hi there!</p>
<p>I have a bit of a workflow to extract the simplified shapes of fish spines from their whole skeletons, and then align them to one another. (I work on scoliosis &amp; spine morphology.) Here is what I typically do:</p>
<ol>
<li>Create a Markup list, manually add a series of fiducial landmarks to the narrowest central point of each vertebra (Using Markups).</li>
<li>Create a “Spine Tube” that approximates the width and shape of the spinal column. (Markups-to-Model using the Markup List as the Input &gt; Create Tube &gt; Set Radius = .35mm &gt; Global Moving Polynomial for smoothing). Repeat for each fish from various scans, export the models.</li>
<li>Use the Markup Lists from the fish that I am registering to create “Rigid” Transforms. (Registration&gt;Specialized&gt;Fiducial Registration, Align 2 spines by assigning one as fixed &amp; one as moving, Check “Rigid.”)</li>
<li>Align the Spine Tube Models by applying their corresponding markup transformations.</li>
</ol>
<p>The problem that I have with this, is that this transformation is scaling my models, even though I am only applying Rigid transforms-- as in, if I align one small fish using the markups from its 32 vertebrae, to a rather big fish that has 32 vertebrae, the small fish ends up just as long as the big one. But “rigid” is checked, so this Transformation shouldn’t scale. (It appears to re-scale the whole model proportionally-- the tube radius of the scaled model ends up looking a little larger, even though I created the tubes with the same radius initially.) Can anyone figure out where this is going wrong?</p>

---

## Post #2 by @mikebind (2023-09-28 22:05 UTC)

<p>That definitely sounds like a bug somewhere. You can check if the transform matrix is rigid using the Characterize Transform Matrix module of the Slicer Sandbox extension (<a href="https://github.com/PerkLab/SlicerSandbox#characterize-transform-matrix" class="inline-onebox" rel="noopener nofollow ugc">GitHub - PerkLab/SlicerSandbox: Collection of utilities that are not polished implementations but can be useful to users</a>; the extension is installable through the extension manager).  If the output transform matrix of Fiducial Registration with the “Rigid” box checked does not represent a rigid transformation, report back here, ideally with a simple data set which would allow others to reproduce the problem.</p>

---

## Post #3 by @muratmaga (2023-09-28 22:11 UTC)

<aside class="quote no-group" data-username="Beth_Bearce" data-post="1" data-topic="31953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/beth_bearce/48/18556_2.png" class="avatar"> Beth_Bearce:</div>
<blockquote>
<p>Registration&gt;Specialized&gt;Fiducial Registration</p>
</blockquote>
</aside>
<p>Install the SlicerIGT and retry with the <code>Fiducial Registration Wizard</code>. and see if you are seeing the scaling.</p>

---

## Post #4 by @mikebind (2023-09-28 22:27 UTC)

<p>I can reproduce this issue with a simple synthetic data set.  I created a fixed fiducial set by clicking randomly, cloned it, created a scaling transformation, applied it to the clone and hardened it, and Fiducial Registration between the two produced a scaling transformation output even though the “Rigid” option was selected, which is clearly an error.</p>

---

## Post #5 by @mikebind (2023-09-28 22:30 UTC)

<p>Fiducial Registration Wizard, on the other hand, produces a rigid transformation for the same data set.</p>

---

## Post #7 by @Beth_Bearce (2023-09-28 22:36 UTC)

<p>Thank you for trying this (&amp; also recapitulating the bug)! I will redo all the transforms with the Wizard.</p>

---

## Post #8 by @muratmaga (2023-09-28 22:40 UTC)

<p>awesome, if you can file a bug report for <code>Fiducial Transform</code> it will be great.<br>
cc <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #9 by @lassoan (2023-09-30 04:41 UTC)

<p>The issue was the ITK has been improved to be able to compute the scaling. I’ve pushed a fix, it will be in the Slicer Preview Release within a couple of days.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7255">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7255" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7255" target="_blank" rel="noopener">BUG: Fix Fiducial Registration module rigid transform changing scale</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:fix-fiducial-registration-rigid-mode-scaling</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-09-30" data-time="03:58:21" data-timezone="UTC">03:58AM - 30 Sep 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 72 additions and 106 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7255/files" target="_blank" rel="noopener">
            <span class="added">+72</span>
            <span class="removed">-106</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When Rigid transform type was selected in Fiducial Registration module, the resu<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7255" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">lting transform included scaling (scale factor != 1.0) as reported at https://discourse.slicer.org/t/rigid-transformation-is-scaling/31953

The problem occurred because ITK landmark initializer has been improved so that it can now compute scaling. Fixed this by using more specific transform types (rigid/similarity).

Since ITK now also supports "affine" transform initialization, this option is now exposed in the module as well.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
