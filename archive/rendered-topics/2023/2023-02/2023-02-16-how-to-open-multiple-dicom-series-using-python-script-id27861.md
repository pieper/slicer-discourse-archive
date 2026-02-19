---
topic_id: 27861
title: "How To Open Multiple Dicom Series Using Python Script"
date: 2023-02-16
url: https://discourse.slicer.org/t/27861
---

# How to open multiple DICOM series using python script

**Topic ID**: 27861
**Date**: 2023-02-16
**URL**: https://discourse.slicer.org/t/how-to-open-multiple-dicom-series-using-python-script/27861

---

## Post #1 by @anhhtmsc (2023-02-16 11:56 UTC)

<p>Hello everyone,<br>
I want to use the WebServer module of 3D Slicer to make a WADO Server. I can load DICOM files into the scene from a folder. I need to open multiple DICOM series simultaneously, then control the volumes to return a slice corresponding to a request. How can I do this?<br>
Thank you, everyone!</p>

---

## Post #2 by @pieper (2023-02-16 14:53 UTC)

<p>The WebServer already has a basic WADO mode (enough to support the OHIF viewer anyway, but not fully standards compliant).  Code contributions to improve this mode would be welcome!</p>
<p>For full flexibility, it might be more efficient to use the <code>exec</code> API to run python code in Slicer to do all your dicom operations.  There are lots of ways to accomplish what you describe so please post any example code you develop and let us know if you run into roadblocks.</p>

---

## Post #3 by @anhhtmsc (2023-02-17 09:58 UTC)

<p>For now, I can load multiple volumes, and get the arrays from them to return a slice corresponding to a request. (I need the array to return slices for different directions - axial, sagittal, coronal). For example:</p>
<pre><code class="lang-auto">volumeNode1 = slicer.util.loadVolume("path_to_series_1", {"singleFile": False, "show": False})
volumeArray1 = slicer.util.arrayFromVolume(volumeNode1)
</code></pre>
<p>With a volume loaded, I can render a 3D image for a volume with the following code, but I don’t know how to render multiple 3D images in different threeDView for different volumes. Can I do this or it’s only possible to render a 3D image for only one volume with one Slicer instance?</p>
<pre><code class="lang-auto">volRenLogic = slicer.modules.volumerendering.logic()
volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode1)
</code></pre>
<p>Thank you very much for your response!</p>

---

## Post #4 by @pieper (2023-02-17 15:09 UTC)

<p>You have pretty much full control through the python api in terms of which volumes to show in which 3D views or even create new views of arbitrary size.  Maybe the best is to browse the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#volumes">script repository</a> to get a sense of what’s possible and let us know if you get stuck.</p>

---
