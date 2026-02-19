---
topic_id: 20964
title: "3D Slicer Elastix Registration Method"
date: 2021-12-08
url: https://discourse.slicer.org/t/20964
---

# 3D Slicer Elastix registration method

**Topic ID**: 20964
**Date**: 2021-12-08
**URL**: https://discourse.slicer.org/t/3d-slicer-elastix-registration-method/20964

---

## Post #1 by @Vincebisca (2021-12-08 11:31 UTC)

<p>Hello,</p>
<p>I’m just having a very small interrogation: what is the registration method used in 3D Slicer’s Elastix extension? I saw that a common method of registration in the litterature is Mutual Information but I don’t know if it is the one applied in Elastix.<br>
Also, when using the presets “General(all)” and “CT/MR-based pseudo-CT (pelvis(prostate))” is the registration rigid or non-rigid?</p>
<p>Thank you for the information if you have it !</p>
<p>Vincent B.</p>

---

## Post #2 by @jamesobutler (2021-12-08 13:20 UTC)

<p>I took a look at <a href="https://github.com/lassoan/SlicerElastix/blob/master/README.md" class="inline-onebox" rel="noopener nofollow ugc">SlicerElastix/README.md at master · lassoan/SlicerElastix · GitHub</a> and indicates</p>
<blockquote>
<p>Select Preset: <code>generic (all)</code> performs deformable registration; <code>generic rigid (all)</code> performs rigid registration</p>
</blockquote>

---

## Post #3 by @Vincebisca (2021-12-08 13:27 UTC)

<p>Oh nice thank you, I found the git but missed this line. I guess that the other preset I mentionned is from the community so there won’t be extensive information. I assume it’s a deformable registration too.<br>
I’ll look more carefully to the GitHub to see if I manage to find out the precise method used in the Elastix registration for deformable applications.</p>
<p>Thank you !</p>

---

## Post #4 by @muratmaga (2021-12-08 16:54 UTC)

<p>They have a wiki and a link to their documentation which lists everything you are looking for:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SuperElastix/elastix/wiki/A-brief-history-of-time">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SuperElastix/elastix/wiki/A-brief-history-of-time" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/8176d6379229ef3a1324e9d7aaec0e43e5f7bcec3f00b0caa011dc0a0eb569ea/SuperElastix/elastix" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SuperElastix/elastix/wiki/A-brief-history-of-time" target="_blank" rel="noopener nofollow ugc">A brief history of time · SuperElastix/elastix Wiki</a></h3>

  <p>Official elastix repository. Contribute to SuperElastix/elastix development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>At a glance they do not seem to support deformable transformation beyond B-Spline and Thin-plate splines… But check their documents…</p>

---
