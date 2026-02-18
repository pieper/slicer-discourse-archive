# Using 3D Slicer as library/ Framework in Paraview based application

**Topic ID**: 19988
**Date**: 2021-10-04
**URL**: https://discourse.slicer.org/t/using-3d-slicer-as-library-framework-in-paraview-based-application/19988

---

## Post #1 by @phtran.dev (2021-10-04 11:57 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
I am a new user to VTK/ Paraview/ 3D Slicer. I know that  Paraview  supports for remote rendering and web application. However, it’s general framework for Visualization. And 3D Slicer has specific features for Medical visualization. I wonder how can I develop a application in python (or c++) using Paraview framework (using pvpython) and import python libraries from 3D Slicer. Example visualize preset, segmentation, filter …</p>

---

## Post #2 by @lassoan (2021-10-04 13:23 UTC)

<p>You can already build we applications based on Slicer, the same way as ParaView. The ParaView team is ahead in that they implemented a couple of complete examples and they also implemented a few simple custom web widgets to modify some properties.</p>
<p>To access the full application GUI and all features you need to connect to a running application instance. You can send commands and request data using a REST API (implemented in <a href="https://github.com/pieper/SlicerWeb">SlicerWeb extension</a>) or Jupyter notebook protocol (implemented in <a href="https://github.com/Slicer/SlicerJupyter">SlicerJupyter extension</a>). For remote rendering of views or the full application GUI in a web browser (in a separate page or anywhere within a webpage), you can use VNC protocol (see this <a href="https://mybinder.org/v2/gh/Slicer/SlicerNotebooks/master?filepath=SlicerWeb.ipynb">example using Binder</a>).</p>
<p>To view data created by Slicer in a web application without a Slicer server, you can use vtk.js and itk.js components - see the two examples below.</p>
<p>Knee atlas rendering:</p>
<iframe width="480" height="373" frameborder="0" marginheight="0" marginwidth="0" src="https://kitware.github.io/vtk-js/examples/OBJViewer/OBJViewer.html?fileURL=https://dl.dropboxusercontent.com/s/1ymrrdpy563w6jv/knee.zip">
</iframe>
<details>
<summary>
Click here to see the text to write in your post to show this viewer</summary>
<pre><code class="lang-auto">&lt;iframe width="480" height="373" frameborder="0" scrolling="no" marginheight="0"
 marginwidth="0" id="kitware-obj-viewer"
 title="Object viewer"
 src="https://kitware.github.io/vtk-js/examples/OBJViewer/OBJViewer.html?fileURL=https://dl.dropboxusercontent.com/s/1ymrrdpy563w6jv/knee.zip"&gt;
&lt;/iframe&gt;
</code></pre>
</details>
<p>Volume rendering of one of the sample data sets:</p>
<iframe width="480" height="373" frameborder="0" marginheight="0" marginwidth="0" src="https://kitware.github.io/vtk-js/examples/VolumeViewer/VolumeViewer.html?fileURL=https://data.kitware.com/api/v1/item/59e12e988d777f31ac6455c5/download">
</iframe>
<details>
<summary>
Click here to see the text to write in your post to show this viewer</summary>
<pre><code class="lang-auto">&lt;iframe width="480" height="373" frameborder="0" scrolling="no" marginheight="0"
 marginwidth="0" id="kitware-vol-viewer"
 title="Volume viewer"
 src="https://kitware.github.io/vtk-js/examples/VolumeViewer/VolumeViewer.html?fileURL=https://data.kitware.com/api/v1/item/59e12e988d777f31ac6455c5/download"&gt;
&lt;/iframe&gt;
</code></pre>
</details>
<p>While you already have all the API that allows you to do everything what you could possibly want without modifying anything in Slicer, there is of course still a lot that we could do to make it easier to write web applications based on Slicer, such as providing example applications, example server configurations, docker images, simple reusable custom widgets for common visualization tasks. There is interest in these topics, so if you are willing to spend some time with these then you can get help.</p>
<p>About ParaView integration. Since there is very little common between general engineering visualization and medical image computing (other than low-level infrastructure, such as VTK), I don’t think there are plans for bringing the applications closer together. However, we work with <a href="https://viewer.ohif.org/">OHIF</a> and <a href="https://kheops.online/">Kheops</a> developers in making Slicer available from these web applications in various ways (local application launching, using Slicer web services, using identity-aware proxies to stream Slicer GUI, etc.).</p>

---
