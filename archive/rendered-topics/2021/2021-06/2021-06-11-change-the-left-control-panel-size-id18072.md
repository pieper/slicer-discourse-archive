---
topic_id: 18072
title: "Change The Left Control Panel Size"
date: 2021-06-11
url: https://discourse.slicer.org/t/18072
---

# Change the left control panel size

**Topic ID**: 18072
**Date**: 2021-06-11
**URL**: https://discourse.slicer.org/t/change-the-left-control-panel-size/18072

---

## Post #1 by @full_stack_master (2021-06-11 04:38 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e8284c5c0597c9867a5bbec1d7106cd6b5ac35a.png" data-download-href="/uploads/short-url/4lTXssbztpdgTFXku3NlR03p1Oi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e8284c5c0597c9867a5bbec1d7106cd6b5ac35a_2_690x494.png" alt="image" data-base62-sha1="4lTXssbztpdgTFXku3NlR03p1Oi" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e8284c5c0597c9867a5bbec1d7106cd6b5ac35a_2_690x494.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e8284c5c0597c9867a5bbec1d7106cd6b5ac35a_2_1035x741.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e8284c5c0597c9867a5bbec1d7106cd6b5ac35a.png 2x" data-dominant-color="A7A6B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1224×877 37.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I want to reduce the left control panel size in code<br>
can you help me</p>

---

## Post #2 by @lassoan (2021-06-11 20:42 UTC)

<p>The module panel is sized automatically based on constraints defined by the widgets that are displayed in it. You can set a maximum width for the module panel (see below), but it will break the layout (widgets will “stick out” from it) if you reduce it beyond the feasible size.</p>
<pre data-code-wrap="python"><code class="lang-python">mainWindow = slicer.util.mainWindow()
modulePanelDockWidget = mainWindow.findChildren('QDockWidget','PanelDockWidget')[0]
modulePanelDockWidget.setMaximumWidth(500)
</code></pre>
<p>If you want to make the module panel more compressible without breaking layouts, you can change the font size or screen scaling. See more information here:</p>
<aside class="quote quote-modified" data-post="6" data-topic="11394">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/4-11-module-panel-is-too-wide-and-wont-resize/11394/6">4.11 Module panel is too wide and won't resize</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can scale the text/button sizes of Slicer many ways: 

Reduce font size in Slicer in menu: Edit / Application settings / Appearance / Font and size
Reduce the font scaling by running set QT_SCALE_FACTOR=0.5 in the command console and then starting Slicer in that console (you can make this permanent by adding this to your environment variables or creating a .bat file that sets this and then starts Slicer)
You can adjust text scaling settings on your computer
Drag-and-drop the module panel to …
  </blockquote>
</aside>


---
