# Script to load specific modules

**Topic ID**: 8224
**Date**: 2019-08-29
**URL**: https://discourse.slicer.org/t/script-to-load-specific-modules/8224

---

## Post #1 by @Todd_G (2019-08-29 13:55 UTC)

<p>I remember posted somewhere on here (yes i searched, but cant seem to find the correct key words) an example code for the application start up script that basically made slicer a very light version. Would anyone have the link to that specific thread?<br>
thank you</p>

---

## Post #2 by @Sam_Horvath (2019-08-29 15:08 UTC)

<p>This, perhaps?</p>
<aside class="quote quote-modified" data-post="2" data-topic="7383">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-4-11-slice-view-widget-interactions-intersections-issue-in-slicelet/7383/2">Slicer 4.11 Slice view widget interactions, intersections issue in slicelet</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Slicer has evolved a lot since the concepts of no-main-window-slicelets. Initialization of the main window has become more complicated (due to hi-DPI screens, OpenGL context initialization overrides, interaction widgets, etc.) and it is expected to get even more complex in the future (with multi-monitor support, multi-touch, pen, and Mac trackpad support, etc.). It should be still possible to mimic initialization steps of the Slicer main window in a generic widget in a Python script, but it woul…
  </blockquote>
</aside>


---

## Post #3 by @Todd_G (2019-08-29 15:12 UTC)

<p>Yes thank you!!!<br>
slicelet that is the term i couldnt remember.<br>
Much appreciated.</p>

---
