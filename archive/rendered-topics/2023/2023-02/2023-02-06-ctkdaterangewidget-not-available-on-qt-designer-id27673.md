---
topic_id: 27673
title: "Ctkdaterangewidget Not Available On Qt Designer"
date: 2023-02-06
url: https://discourse.slicer.org/t/27673
---

# ctkDateRangeWidget not available on Qt Designer

**Topic ID**: 27673
**Date**: 2023-02-06
**URL**: https://discourse.slicer.org/t/ctkdaterangewidget-not-available-on-qt-designer/27673

---

## Post #1 by @Gabriel_WK (2023-02-06 19:13 UTC)

<p>When editing a custom extension UI on Qt Designer using the “Edit UI” button in the Developer Section, ctkDateRangeWidget is not available. It’s still available through python with <code>ctk.ctkDateRangeWidget()</code>. Is there a way to import ctkDateRangeWidget and directly add it to the .ui file?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0612c52499de4d0e12f6bef7a7cc0e95459100b.png" data-download-href="/uploads/short-url/yiuMH01HRfsueRl02viJl3CXxzB.png?dl=1" title="Captura de tela_20230206_154713" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0612c52499de4d0e12f6bef7a7cc0e95459100b.png" alt="Captura de tela_20230206_154713" data-base62-sha1="yiuMH01HRfsueRl02viJl3CXxzB" width="232" height="500" data-dominant-color="F0F0F0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de tela_20230206_154713</span><span class="informations">343×738 24.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-02-06 21:40 UTC)

<p>ctkDateRangeWidget just does not have a designer plugin. To fix it, two files has to be added to CTK (in CTK\Libs\Widgets\Plugins) and add the class to CMakeLists.txt and ctkWidgetsPlugins.h. It would be great if you could submit a pull request with this change to <a href="https://github.com/commontk/CTK">CTK</a>. You may not even need to build it, we can test it before we merge the pull request.</p>
<p>In the meantime, as a workaround, you can add a frame in Qt designer and then put the ctkDateRangeWidget in the frame in your Python code.</p>

---
