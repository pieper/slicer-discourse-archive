---
topic_id: 12280
title: "All Module View Doesnt Fit On The Screen"
date: 2020-06-29
url: https://discourse.slicer.org/t/12280
---

# All module view doesn't fit on the screen

**Topic ID**: 12280
**Date**: 2020-06-29
**URL**: https://discourse.slicer.org/t/all-module-view-doesnt-fit-on-the-screen/12280

---

## Post #1 by @muratmaga (2020-06-29 18:30 UTC)

<p>When I expand the Modules to show all modules, it occupies my entire screen, but it is not a full list, nor I can expand or scroll. This is on a laptop with 4K screen. I suspect it is something to do with the scaling<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9b9494795ed578482451826545b711c527ed16b.png" data-download-href="/uploads/short-url/xlCdVfDEU7QEsFITapYAi0XWHur.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9b9494795ed578482451826545b711c527ed16b_2_517x291.png" alt="image" data-base62-sha1="xlCdVfDEU7QEsFITapYAi0XWHur" width="517" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9b9494795ed578482451826545b711c527ed16b_2_517x291.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9b9494795ed578482451826545b711c527ed16b_2_775x436.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9b9494795ed578482451826545b711c527ed16b_2_1034x582.png 2x" data-dominant-color="3D3D3E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3840×2160 263 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2020-06-29 18:51 UTC)

<p>I wonder if we should just remove that menu.  Do you ever find it useful?</p>

---

## Post #3 by @rkikinis (2020-06-29 19:10 UTC)

<p>Alernately, a scroll  bar might do the trick. Sometimes browsing is helpful to me, if I don’t remember the exact name of the module.</p>

---

## Post #4 by @muratmaga (2020-06-29 19:18 UTC)

<p>Same as Ron. I do use it for modules that I occasionally use and can’t remember their full name or where they are located.</p>

---

## Post #5 by @pieper (2020-06-29 19:27 UTC)

<p>Try this in the python console - if you like it we can make it the default.</p>
<pre><code class="lang-auto">a = findChildren(mainWindow(), text="All Modules")[0]
a.menu().setStyleSheet("QMenu { menu-scrollable: 1; }")
</code></pre>

---

## Post #6 by @muratmaga (2020-06-29 19:42 UTC)

<p>Definitely better +1 for making default.</p>

---

## Post #7 by @pieper (2020-06-29 20:46 UTC)

<p>Agreed.  Not anticipating objections I went ahead and committed the change.</p>

---

## Post #8 by @lassoan (2020-06-29 21:00 UTC)

<p>I’ve run into this issue, too. Setting it scrollable makes the menu nicer but it is still not very usable (it takes about 10 seconds to get to the end of the list, which is way too long).</p>
<p>I’ll add a module finder dialog, which allows quick search&amp;filter of a module. It solves the other common complaints that users don’t know where the module shows up in the categorized module list; or users don’t know the module type (CLI, Loadable, Scripted, …).</p>

---

## Post #9 by @lassoan (2020-06-30 12:08 UTC)

<p>Here is a quick preview of a new work-in-progress module selector:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="tmWcFrn7U9U" data-video-title="ModuleFinder01" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=tmWcFrn7U9U" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/tmWcFrn7U9U/maxresdefault.jpg" title="ModuleFinder01" width="" height="">
  </a>
</div>

<ul>
<li>It can select a module using the same number of clicks as the the Ctrl/Cmd-F combobox (type characters, press arrow-down key N times, then press Enter to go to that module)</li>
<li>Built-in modules can be hidden, so it is easy to find modules installed by extensions</li>
<li>Module category is shown (e.g., <code>Cleaner</code> module is available in <code>Surface models-&gt;Advanced</code> category)</li>
<li>Developer information can be optionally displayed: module type (CLI, C++ loadable, scripted loadable), location, dependencies</li>
</ul>
<p>It could be added as an “All modules” menu item (replacing the submenu by a popup) or replace the current Ctrl/Cmd-F combobox. Replacing the combobox would be probably better, to reduce redundancy (the combobox and this finder works very similarly) and to make the module finder easily accessible (single-click on the main interface, familiar shortcut).</p>

---

## Post #10 by @pieper (2020-06-30 12:39 UTC)

<p>Wow, cool!  I think it would be great to replace the Ctrl/Cmd-F combobox with this dialog.</p>

---

## Post #11 by @lassoan (2020-07-01 00:07 UTC)

<p>The implementation is ready (see <a href="https://github.com/Slicer/Slicer/pull/5024">pull request</a>). I find that the new module selector works really well: it makes it much easier to browse and find modules and it does not require more clicks than the combobox that it replaced. Since “All modules” submenu is not needed anymore, the module selector is simplified, too.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="bhPbT0pu2K8" data-video-title="ModuleFinder02" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=bhPbT0pu2K8" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/bhPbT0pu2K8/maxresdefault.jpg" title="ModuleFinder02" width="" height="">
  </a>
</div>


---

## Post #12 by @lassoan (2020-07-03 13:06 UTC)

<p>This is now available in the Preview Release:</p>
<aside class="quote quote-modified" data-post="1" data-topic="12356">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-finder-for-selecting-modules/12356">New module finder for selecting modules</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    As more modules have been added to Slicer, it has become harder browse and select modules (see <a href="https://discourse.slicer.org/t/all-module-view-doesnt-fit-on-the-screen/12280/9">[1]</a>). To address this, we added a new module finder window. The finder can be displayed by clicking “Search” icon in the module toolbar or using Ctrl/Cmd + F keyboard shortcut. 

  <a href="https://www.youtube.com/watch?v=_ctPDxv8rGg" target="_blank" rel="noopener">
    [New module finder in 3D Slicer]
  </a>


Features: 

It can select a module using the same number of clicks as the the Ctrl/Cmd-F combobox (type characters, press arrow-down key N times, then press Enter to go to that modu…
  </blockquote>
</aside>


---
