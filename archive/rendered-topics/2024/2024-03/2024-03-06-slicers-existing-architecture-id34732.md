---
topic_id: 34732
title: "Slicers Existing Architecture"
date: 2024-03-06
url: https://discourse.slicer.org/t/34732
---

# Slicer's existing architecture

**Topic ID**: 34732
**Date**: 2024-03-06
**URL**: https://discourse.slicer.org/t/slicers-existing-architecture/34732

---

## Post #1 by @MJamal (2024-03-06 04:35 UTC)

<p>Is it possible to port slicer’s existing architecture from single-threaded to multi-threaded?</p>

---

## Post #2 by @muratmaga (2024-03-06 04:41 UTC)

<p>Most modules and tools in slicer is already multi-threaded.</p>

---

## Post #3 by @jcfr (2024-03-06 15:50 UTC)

<p>For reference, both VTK and ITK filters are indeed written by leveraging classes like <code>vtkThreadedImageAlgorithm</code> or <code>itk::MultiThreaderBase</code></p>
<p>For example, the new SurfaceNets feature heavily relies on the threading capabilities. See <a href="https://discourse.slicer.org/t/new-surface-model-generation-method-surfacenets/32430" class="inline-onebox">New surface model generation method: SurfaceNets</a></p>

---

## Post #4 by @MJamal (2024-03-07 04:31 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/jcfr">@jcfr</a> Thank you for your inputs. I appreciate you bringing the references to my attention. However, based on the description of <code>itk::MultiThreaderBase</code>, this class appears to focus on parallelizing image operations.</p>
<p>My current focus is on parallelizing operations on <code>vtkMRMLScene</code> , specifically the <code>SaveSceneToSlicerDataBundleDirectory()</code> function.</p>

---

## Post #5 by @jamesobutler (2024-03-07 12:09 UTC)

<p>There are plans to ultimately switch to Zlib-ng for some performance improvements. See this former thread that might be related to your topic.</p>
<aside class="quote" data-post="3" data-topic="33290">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/parallel-zip-library-for-slicer/33290/3">Parallel zip library for Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    As a drop-in replacement, we have  plan to  switch zlib with zlib-ng. See <a href="https://github.com/Slicer/Slicer/pull/6708" class="inline-onebox" rel="noopener nofollow ugc">COMP: Switch to modern maintained zlib-ng fork of zlib by jamesobutler · Pull Request #6708 · Slicer/Slicer · GitHub</a> 
Instead of transitioning to fastzip (currently unmaintained), we will likely add support for <a href="https://github.com/facebook/zstd" class="inline-onebox" rel="noopener nofollow ugc">GitHub - facebook/zstd: Zstandard - Fast real-time compression algorithm</a>
  </blockquote>
</aside>


---

## Post #6 by @pieper (2024-03-07 13:39 UTC)

<p><a class="mention" href="/u/mjamal">@MJamal</a> do you know specifically which bottlenecks you are trying to address?  As <a class="mention" href="/u/jamesobutler">@jamesobutler</a> points out, a lot of the time for loading/saving bit volume datasets if the compression time, which can be avoided with a switch.  You probably want to do some profiling to see where time is really being spent before trying to optimize.</p>
<p>For the case where there are a lot of non-volume files in the scene it could make sense to load/save them in parallel.</p>
<p>I did <a href="https://github.com/SlicerDMRI/SlicerDMRI/compare/master...pieper:SlicerDMRI:parallel-load">an experiment</a>  loading vtk files in parallel that you can look at for reference.  It does work, but would need to be generalized to save and load and work on more node types to be generally useful.  A lot of the performance implications depend on whether the files are local or remote, how big they are, how much processing is needed for each file type, etc.</p>

---

## Post #7 by @MJamal (2024-03-14 04:30 UTC)

<p>I need some time to discuss the bottlenecks here. I’ll also look into the references provided above and update you soon. Thanks <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---
