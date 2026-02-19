---
topic_id: 18514
title: "Reloading Scripted Extension With Multiple Files"
date: 2021-07-05
url: https://discourse.slicer.org/t/18514
---

# Reloading scripted extension with multiple files

**Topic ID**: 18514
**Date**: 2021-07-05
**URL**: https://discourse.slicer.org/t/reloading-scripted-extension-with-multiple-files/18514

---

## Post #1 by @LorenzE (2021-07-05 11:49 UTC)

<p>I am trying to reload a scripted python extension with multiple .py files. Some of them are located in subfolders, see below for example.</p>
<p>extension_name/<br>
├── service/<br>
│   ├── logic.py<br>
│   └── gui.py<br>
└── extension_name.py</p>
<p>It seems that 3DSlicer only reloads the extension_name.py file. Is this the expected behavior when reloading extensions? Or do I need to specify explicitly which files should be reloaded additionally?</p>

---

## Post #2 by @LorenzE (2021-07-06 09:47 UTC)

<p>Duplicate of <a href="https://discourse.slicer.org/t/python-scripted-module-development-reload-feature-for-multiple-files/6363/2">Python scripted module development reload feature for multiple files - Development - 3D Slicer Community</a></p>

---
