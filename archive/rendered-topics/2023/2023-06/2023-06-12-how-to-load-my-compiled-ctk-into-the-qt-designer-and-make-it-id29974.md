---
topic_id: 29974
title: "How To Load My Compiled Ctk Into The Qt Designer And Make It"
date: 2023-06-12
url: https://discourse.slicer.org/t/29974
---

# How to load my compiled CTK into the QT designer and make it a drag and drop control？

**Topic ID**: 29974
**Date**: 2023-06-12
**URL**: https://discourse.slicer.org/t/how-to-load-my-compiled-ctk-into-the-qt-designer-and-make-it-a-drag-and-drop-control/29974

---

## Post #1 by @ma1282029525 (2023-06-12 01:59 UTC)

<p>I have compiled a ctk library myself and added CTKWidgetsPlugins.dll to qt D: QT 5.15.2 msvc2019_ 64 plugins designer directory, but it prompts me that I cannot load the library and cannot find the specified module</p>

---

## Post #2 by @jamesobutler (2023-06-12 02:47 UTC)

<p>If you start Slicer (can be one you downloaded from <a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a>), you can run <code>slicer.util.startQtDesigner()</code> which will start Qt Designer and CTK related widgets will be available to drag and drop into a UI.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html?highlight=Designer#slicer.util.startQtDesigner" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html?highlight=Designer#slicer.util.startQtDesigner</a></p>

---

## Post #3 by @ma1282029525 (2023-06-20 03:05 UTC)

<p>Can I load these additional plugins into my own qt creator environment</p>

---
