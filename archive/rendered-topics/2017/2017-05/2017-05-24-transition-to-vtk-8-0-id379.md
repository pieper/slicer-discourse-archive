# Transition to VTK 8.0

**Topic ID**: 379
**Date**: 2017-05-24
**URL**: https://discourse.slicer.org/t/transition-to-vtk-8-0/379

---

## Post #1 by @jcfr (2017-05-24 19:44 UTC)

<p>Hi All,</p>
<p>Just to let you know we are working on updating the version of VTK used in Slicer to use the latest VTK version. As soon as a branch is ready for testing, I will follow up here.</p>
<p>It will include the follow steps:</p>
<ul>
<li>
<p>create branch for testing VTK build</p>
</li>
<li>
<p>document breaking change on <a href="https://www.slicer.org/wiki/Documentation/Labs/VTK7">https://www.slicer.org/wiki/Documentation/Labs/VTK7</a> (we will probably create a VTK8 page)</p>
</li>
<li>
<p>transition MacOSX build from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#Software">factory.kitware</a> (MacOSX 10.6.8) to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#factory.kitware">factory-south.kitware</a> (MacOSX 10.11.6). Deployment target for Slicer official package will be changed from <code>10.6</code> to <code>10.7</code> (the minimum required by newer VTK)</p>
</li>
<li>
<p>transition Linux build from Ubuntu 10.04 VM running on <code>factory-south.kitware</code> to docker based build running on <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#overload.kitware_and_metroplex.kitware">metroplex.kitware</a> dashboard. (It will most likely use <a href="https://github.com/dockcross/dockcross#readme">dockcross/manylinux-x64</a> (or similar image)</p>
</li>
</ul>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://blog.kitware.com/wp-content/uploads/2017/04/xExternalFavicon.png.pagespeed.ic.BxFzGTIFZT.png" class="site-icon" width="64" height="64">
      <a href="https://blog.kitware.com/vtk-8-0-0-rc1-ready-for-testing/" target="_blank" title="07:16PM - 24 May 2017">Kitware Blog – 24 May 17</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/386;"><img src="https://blog.kitware.com/wp-content/uploads/2016/01/VTKLogo.jpg" class="thumbnail" width="690" height="386"></div>

<h3><a href="https://blog.kitware.com/vtk-8-0-0-rc1-ready-for-testing/" target="_blank">VTK 8.0.0-rc1 ready for testing - Kitware Blog</a></h3>

<p>The VTK maintenance team is happy to announce that VTK 8.0 has entered the release candidate stage! You can find the source, data and documentation ... Read More</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2017-05-24 20:24 UTC)

<p>It would give more time for testing and extension developers for updating if we temporarily make Slicer and extensions compatible with both VTK7 and VTK8 with (using <span class="hashtag">#ifdefs</span>, similarly how we did it for VTK5-&gt;VTK6 transition).</p>

---

## Post #3 by @fedorov (2017-05-24 21:08 UTC)

<p>“This also means, beginning version 8.0.0, VTK requires a C++11 capable compiler to compile”</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> can you please comment whether C++11 will be enabled for VTK compiled with Slicer?</p>

---

## Post #4 by @jcfr (2017-05-24 21:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="379">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>compatible with both VTK7 and VTK8 with (using <span class="hashtag-raw">#ifdefs</span>, similarly how we did it for VTK5-&gt;VTK6 transition).</p>
</blockquote>
</aside>
<p>Look like we will have a CMake option to choose one or the other.</p>
<aside class="quote no-group" data-username="fedorov" data-post="3" data-topic="379">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>can you please comment whether C++11 will be enabled for VTK compiled with Slicer?</p>
</blockquote>
</aside>
<p>Will comment later. Depending on what require c++11, we may add this requirement at a later time and patch Slicer/VTK fork.</p>

---

## Post #5 by @jcfr (2017-09-22 19:24 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="379">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Will comment later. Depending on what require c++11, we may add this requirement at a later time and patch Slicer/VTK fork.</p>
</blockquote>
</aside>
<p>Here is an update:</p>
<ul>
<li>
<p>when building Slicer against Qt4, VTK 7.1 is used and C++98 is selected</p>
</li>
<li>
<p>when building Slicer against Qt5, VTK 8 is used and C++11 is selected</p>
</li>
</ul>

---

## Post #6 by @ihnorton (2017-11-04 15:16 UTC)

<p>Regarding</p>
<aside class="quote" data-post="3" data-topic="1356">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/load-dsi-studio-trk-gz-or-trackvis-trk-tracks-in-slicer/1356/3">Load DSI Studio (*.trk.gz) or TrackVis (*.trk) tracks in Slicer</a> <a class="badge-category__wrapper " href="/c/community/slicerdmri/16"><span data-category-id="16" style="--category-badge-color: #AB9364; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="The SlicerDMRI extension provides diffusion MRI tools including tensor estimation, tractography, and quantification."><span class="badge-category__name">SlicerDMRI</span></span></a>
  </div>
  <blockquote>
    <a class="mention" href="/u/jcfr">@jcfr</a> When do we plan to switch to c++11? I have trouble building Cleaver on Linux and Mac without c++11, too.
  </blockquote>
</aside>

<p>Actually, it wouldn’t be completely crazy to go straight to C++14…</p>
<ul>
<li>
<p>Windows: in the past, Visual Studio was always lagging, but we will be requiring MSVC19 (Visual Studio 2015) anyway, <a href="http://en.cppreference.com/w/cpp/compiler_support">which supports</a> everything in C++14.</p>
</li>
<li>
<p>Mac: Clang has supported everything in C++14 for more than two major releases.</p>
</li>
<li>
<p>Linux is the wildcard, because of old clusters. However, they are not any worse off than will be with C++11 – they have to use devtoolset or the equivalent anyway.</p>
</li>
</ul>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #7 by @lassoan (2017-11-04 16:26 UTC)

<p>I would try to be as close to VTK as possible and switch to c++14 shortly after VTK switches.</p>

---

## Post #8 by @lassoan (2017-11-04 20:20 UTC)

<p>I’m wondering if we should create a Slicer 4.8.1 patch release based on the latest trunk version (maybe excluding a few risky changes, if there were any), just before we switch to VTK8. There have been a couple of fixes and improvements that would be good to have in the stable version.</p>

---

## Post #9 by @jcfr (2017-12-12 23:48 UTC)

<p>Hi Slicers,</p>
<p>To streamline the maintenance, support for <code>Slicer_VTK_VERSION_MAJOR=8</code> has been removed in  <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26710">r26710</a></p>
<h3>What does this mean for existing build tree ?</h3>
<p>Three cases:</p>
<ul>
<li>
<p><strong>Qt4</strong>: if you are building against Qt4: <strong>no action required.</strong></p>
</li>
<li>
<p><strong>Qt5</strong>: if you have done a clean build since November 15 (when <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26634">r26634</a> was integrated), you are all set.</p>
</li>
<li>
<p><strong>Qt5</strong>: if you have NOT done a clean build, now is the time to do so. Otherwise, you will get an error message like ``.</p>
</li>
</ul>

---
