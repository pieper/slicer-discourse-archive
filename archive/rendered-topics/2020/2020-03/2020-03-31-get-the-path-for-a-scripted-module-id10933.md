---
topic_id: 10933
title: "Get The Path For A Scripted Module"
date: 2020-03-31
url: https://discourse.slicer.org/t/10933
---

# Get the path for a scripted module

**Topic ID**: 10933
**Date**: 2020-03-31
**URL**: https://discourse.slicer.org/t/get-the-path-for-a-scripted-module/10933

---

## Post #1 by @ZiyunLiang (2020-03-31 08:16 UTC)

<p>Hi all,<br>
I load a scripted module to Slier by adding the module path to ‘Edit / Application settings’.<br>
I want to access the path of this module in my .py file because I want to load other files to Slicer in that path without stating again. Does anyone know how to get the path of my already loaded module in python console?<br>
Thanks!</p>

---

## Post #2 by @lassoan (2020-03-31 15:25 UTC)

<p>You can use <code>scriptPath = os.path.dirname(os.path.abspath(__file__))</code> anywhere in the file. In the widget class, there is a convenience method to get full path to a resource file: <code>self.resourcePath('UI/mycustomfile.txt')</code>.</p>
<p>To add these additional files to the extension’s installation package, you need to store the files in the module’s <code>Resources</code> subfolder and add the files to <code>MODULE_PYTHON_RESOURCES</code> list in <code>CMakeLists.txt</code>.</p>

---
