---
topic_id: 20224
title: "Display Model In 3D View Via A Python Module"
date: 2021-10-19
url: https://discourse.slicer.org/t/20224
---

# Display Model in 3D view via a Python module

**Topic ID**: 20224
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/display-model-in-3d-view-via-a-python-module/20224

---

## Post #1 by @Karthik (2021-10-19 09:42 UTC)

<p>Operating system: Ubuntu 20.04<br>
Slicer version: 4.11.20210226</p>
<p>I am writing a python module for 3D Slicer. I have a surface (vtkPolyData). I want to display this in the 3D view. I know how to do this with a volume, i.e. using sitkUtils.PushVolumeToSlicer. Is there something like PushModelToSlicer?</p>
<p>Also, is PushVolumeToSlicer the only way to display a volume object on the 3d view?</p>

---

## Post #2 by @simonoxen (2021-10-19 09:53 UTC)

<p>Hi, see the first example in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#models" rel="noopener nofollow ugc">script repository: models</a></p>
<pre><code class="lang-auto">slicer.modules.models.logic().AddModel(...)
</code></pre>
<p>Hope this helps</p>

---

## Post #3 by @lassoan (2021-10-19 12:04 UTC)

<p>2 posts were split to a new topic: <a href="/t/update-existing-volume-from-simpleitk-image/20239">Update existing volume from SimpleITK image</a></p>

---
