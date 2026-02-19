---
topic_id: 30228
title: "How To Script Into Code Data Loading 3D Model Generation And"
date: 2023-06-26
url: https://discourse.slicer.org/t/30228
---

# How to script into code data loading, 3D model generation and screen capture tasks

**Topic ID**: 30228
**Date**: 2023-06-26
**URL**: https://discourse.slicer.org/t/how-to-script-into-code-data-loading-3d-model-generation-and-screen-capture-tasks/30228

---

## Post #1 by @jhlegarreta (2023-06-26 02:16 UTC)

<p>Hi,<br>
I’d like to be able to automate some tasks in 3D Slicer by calling its Python API from the command line:</p>
<ul>
<li>Loading structural (e.g. an T1w MRI) and segmentation files for a given subject.</li>
<li>Making the data displayed at a given orientation/view (e.g. axial) at a specified slice/location/position (index).</li>
<li>Potentially creating a 3D model/contour out of a segmentation, and display it in an orthogonal view</li>
<li>Removing the default annotation labels (without requiring to restart 3D Slicer).</li>
<li>Capturing a screenshot of a view (e.g. axial) at an arbitrary size and resolution.</li>
<li>Setting the background of the view (whether a 3D or e.g. axial) to white or transparent (or black in the case of the 3D view).</li>
</ul>
<p>So far I have found a way to capture the 3D or the orthogonal views using Python:</p>
<pre><code class="lang-auto">view = slicer.app.layoutManager().threeDWidget(0).threeDView()
renderWindow = view.renderWindow()
renderWindow.SetAlphaBitPlanes(1)
wti = vtk.vtkWindowToImageFilter()
wti.SetInputBufferTypeToRGBA()
wti.SetInput(renderWindow)
wti.Update()
vtk_data = wti.GetOutput()

writer = vtk.vtkPNGWriter()

writer.SetWriteToMemory(False)

writer.SetInputData(vtk_data)

filename = "/my_path/slicer_screenshot.png"
writer.SetFileName(filename)
writer.Write()
</code></pre>
<p>However, the above</p>
<ul>
<li>Does not remove the annotation labels. According to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#hide-slice-view-annotations" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>, I need to execute the below to remove the labels, and this is only effective when restarting Slicer, which is inconvenient:</li>
</ul>
<pre><code class="lang-auto"># Disable slice annotations immediately
sliceAnnotations = slicer.modules.DataProbeInstance.infoWidget.sliceAnnotations
sliceAnnotations.sliceViewAnnotationsEnabled=False
sliceAnnotations.updateSliceViewFromGUI()
# Disable slice annotations persistently (after Slicer restarts)
settings = qt.QSettings()
settings.setValue("DataProbe/sliceViewAnnotations.enabled", 0)
</code></pre>
<ul>
<li>The size of the captured screenshot has the size of the view/window (i.e it is a small window if I am in a 3D+orthogonal layout, a bigger one if I am on a single view layout, etc.). Can this be made arbitrarily big programmatically? If not, can the layout be maximized to a given view programmatically?</li>
</ul>
<p>Can pointers or snippets be provided for the rest of the tasks in the bullet list as well, please?</p>
<p>Thanks for developing and maintaining this tool</p>

---
