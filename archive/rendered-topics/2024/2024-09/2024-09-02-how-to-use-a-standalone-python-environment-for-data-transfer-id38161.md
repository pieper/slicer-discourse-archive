---
topic_id: 38161
title: "How To Use A Standalone Python Environment For Data Transfer"
date: 2024-09-02
url: https://discourse.slicer.org/t/38161
---

# How to use a standalone python environment for data transfer with 3Dslicer

**Topic ID**: 38161
**Date**: 2024-09-02
**URL**: https://discourse.slicer.org/t/how-to-use-a-standalone-python-environment-for-data-transfer-with-3dslicer/38161

---

## Post #1 by @wenlin_x (2024-09-02 15:40 UTC)

<p>How to use a standalone python environment for data transfer with 3Dslicer</p>

---

## Post #2 by @lassoan (2024-09-02 15:48 UTC)

<p>You have several options. To give specific advice we would need to know more about what exactly you want to achieve, but for example you can:</p>
<ul>
<li>Use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html">Slicer’s web API</a> to upload/download data and trigger processing functionsin Slicer. If you develop in Python then <a href="https://pypi.org/project/slicerio/">slicerio</a>  Python package can be used.</li>
<li>Use <a href="https://github.com/openigtlink/SlicerOpenIGTLink">OpenIGTLink</a> for real-time continous streaming of data, such as ultrasound images, video, transforms, surface meshes. If you develop in Python then <a href="https://github.com/lassoan/pyigtl">pyigtl</a> Python package can be used.</li>
</ul>

---
