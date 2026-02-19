---
topic_id: 25268
title: "Import External Python Classes To Your Module Script"
date: 2022-09-14
url: https://discourse.slicer.org/t/25268
---

# Import External Python classes to your module script

**Topic ID**: 25268
**Date**: 2022-09-14
**URL**: https://discourse.slicer.org/t/import-external-python-classes-to-your-module-script/25268

---

## Post #1 by @Louis-Franz (2022-09-14 15:40 UTC)

<p>Hi, I have created a scripted Slicer module, within my logic class I am calling a separate python file/class. However, when loading the extension Slicer tries to add the separate file as a module, but i don’t want to have it as an extra module. If any one could assist that would be great.</p>

---

## Post #2 by @lassoan (2022-09-14 15:42 UTC)

<p>All the .py files in a folder that is listed among “additional module paths” are expected to be Slicer modules. You can put all additional .py files in regular Python modules within the Slicer module folder as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-include-python-modules-in-an-extension">here</a>.</p>

---

## Post #3 by @Louis-Franz (2022-09-14 15:56 UTC)

<p>Ahh great, thanks for the help!</p>

---
