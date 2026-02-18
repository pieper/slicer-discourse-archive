# How to render two volumes in the 3D scene at the same time?

**Topic ID**: 1680
**Date**: 2017-12-18
**URL**: https://discourse.slicer.org/t/how-to-render-two-volumes-in-the-3d-scene-at-the-same-time/1680

---

## Post #1 by @wpgao (2017-12-18 06:13 UTC)

<p>Hi everybody,</p>
<p>Is there anyway to render two volumes (for example, CT and MR volumes) in the 3D scene at the same time using volume rendering? Thanks!</p>

---

## Post #2 by @timeanddoctor (2017-12-18 06:47 UTC)

<p>in my opinion there are still no module could achieve that goal</p>

---

## Post #3 by @pieper (2017-12-18 12:32 UTC)

<p>Right - currently only one volume at a time can be volume rendered, but there are some new developments underway that should support multiple volume rendering in the future.</p>

---

## Post #4 by @lassoan (2017-12-18 13:52 UTC)

<p>Here is the pull request of multi-volume rendering in VTK:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/3699">
  <header class="source">
      <img src="https://gitlab.kitware.com/uploads/-/system/appearance/favicon/1/KitwareMarkIcon.png" class="site-icon" width="32" height="32">

      <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/3699" target="_blank" rel="noopener">GitLab</a>
  </header>

  <article class="onebox-body">
    <img src="https://gitlab.kitware.com/uploads/-/system/project/avatar/13/vtk_logo-main1.png" class="thumbnail onebox-avatar" width="146" height="146">

<h3><a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/3699" target="_blank" rel="noopener">Support overlapping volumes through multiple inputs in GPUVolumeMapper (!3699)...</a></h3>

  <p>When multiple inputs are rendered through the same mapper, it is possible to composite the overlapping areas correctly. Inputs are connected directly to the mapper and its parameters...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It’ll probably take a few months (depending on how urgently a specific project needs this) to get it integrated into Slicer.</p>
<p>Note that multi-volume rendering is only useful in very specific cases, i.e., when displayedstructures just barely overlap. In general, you still need to segment your volumes before visualization, so don’t expect any radical change in processing &amp; visualization workflow - just more colorful images and structures with smoother-looking boundaries.</p>

---

## Post #5 by @muratmaga (2017-12-18 19:50 UTC)

<p>Just to clarify. If you don’t need them to be superimposed in the same rendering window, you can choose switch to dual 3D layout, assign each volume to a different viewport, adjust their volume properties and finally link cameras.</p>
<p>That way you can see both MR and CT in 3D scene at the same time, just not as superimposed volumes.</p>

---

## Post #6 by @wpgao (2018-04-21 09:58 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="1680">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>e properties and</p>
</blockquote>
</aside>
<p>it’s a good idea, thanks!</p>

---

## Post #7 by @lassoan (2018-04-21 13:33 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> is working on adding rendering of multiple volumes. In the latest nightly, you can already show multiple volumes using 3D volume rendering (raycasting). The limitation is that only non-overlapping volumes are displayed correctly.</p>
<p>Soon <a class="mention" href="/u/cpinter">@cpinter</a> will integrate his latest enhancements that allow correct rendering of overlapping volumes (using VTK’s multi-volume GPU renderer).</p>

---

## Post #8 by @cpinter (2018-04-21 14:01 UTC)

<p>Indeed. Just to keep expectations in bay, VTK’s multi-volume renderer has issues, such as lack of shading support and significantly lower performance than the current GPU renderer. I’ll follow up with VTK developers about these and see if something can be done in reasonable time. This should be available in Slicer core sometime next week.</p>
<p><a class="mention" href="/u/wpgao">@wpgao</a> Since the integration of multi-volume support in volume rendering that happened this week, it is now possible to do what <a class="mention" href="/u/muratmaga">@muratmaga</a> suggested. You can show multiple volumes and turn on only one view for each.</p>

---
