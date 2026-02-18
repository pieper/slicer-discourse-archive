# Is there any way to disable right-click context menu between Module Panel and Views?

**Topic ID**: 39440
**Date**: 2024-09-29
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-disable-right-click-context-menu-between-module-panel-and-views/39440

---

## Post #1 by @apparrilla (2024-09-29 22:17 UTC)

<p>I want to disable this mouse right-click qAction:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a67b19acb2b5031b4a249bf0489c860871e506a.png" data-download-href="/uploads/short-url/8kFR54Rr0zepAJfzQjNH42cCyFA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a67b19acb2b5031b4a249bf0489c860871e506a_2_628x500.png" alt="image" data-base62-sha1="8kFR54Rr0zepAJfzQjNH42cCyFA" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a67b19acb2b5031b4a249bf0489c860871e506a_2_628x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a67b19acb2b5031b4a249bf0489c860871e506a_2_942x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a67b19acb2b5031b4a249bf0489c860871e506a_2_1256x1000.png 2x" data-dominant-color="1F1E1C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1948×1549 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I´ve tried:</p>
<blockquote>
<p>pluginHandler = slicer.qSlicerSubjectHierarchyPluginHandler.instance()<br>
pluginLogic = pluginHandler.pluginLogic()<br>
pluginLogic.allowedViewContextMenuActionNames = <span class="chcklst-box fa fa-square-o fa-fw"></span></p>
</blockquote>
<p>It doesn´t work for me.</p>
<p>Thanks in advance!!!</p>

---

## Post #2 by @lassoan (2024-09-30 02:58 UTC)

<p>This is a standard Qt main window feature. You may search/ask on Qt forums about how to customize it, for example <a href="https://qtcentre.org/threads/31498-QToolBar-How-do-you-suppress-the-right-click-menu-that-allows-hiding-the-toolbar">here</a>.</p>

---

## Post #3 by @apparrilla (2024-10-01 21:19 UTC)

<p>This works for me…</p>
<pre><code class="lang-auto">slicer.util.mainWindow().setContextMenuPolicy(qt.Qt.NoContextMenu)
</code></pre>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a></p>

---
