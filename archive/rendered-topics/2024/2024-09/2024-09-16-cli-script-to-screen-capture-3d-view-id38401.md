# CLI script to screen capture 3D View

**Topic ID**: 38401
**Date**: 2024-09-16
**URL**: https://discourse.slicer.org/t/cli-script-to-screen-capture-3d-view/38401

---

## Post #1 by @Jithendra (2024-09-16 18:47 UTC)

<p>Could some one share the solution for creating 3d views of volume and segmentation using cli commands.</p>
<p>I tried one example to execute the <a href="https://github.com/jzeyl/3D-Slicer-Scripts/blob/master/command%20line_loopfolders_volumerendering.py" rel="noopener nofollow ugc">command line_loopfolders_volumerendering.py</a> using</p>
<pre><code class="lang-auto">/Applications/Slicer.app/Contents/MacOS/Slicer --no-splash --no-main-window --python-script "/Users/3D-Slicer-Scripts/command line_loopfolders_volumerendering.py"  -f /Users/data/in
</code></pre>
<p>and got <code>AttributeError: 'NoneType' object has no attribute 'threeDWidget'</code></p>
<p>Environment - Slicer 5.6.2, macOS 14.5</p>
<p>It seems to run fine without <code>--no-main-window</code> but i wanted to run this as command line script.</p>

---

## Post #2 by @Jithendra (2024-09-16 18:54 UTC)

<p>It seems to error out with layoutManager</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0)
</code></pre>

---

## Post #3 by @lassoan (2024-09-16 23:12 UTC)

<p>Layout manager is provided by the application main window. If you don’t have a main window then you don’t have a layout manager. You can fix the error by removing <code>--no-main-window</code>.</p>
<p>If you need a full example, check out the <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/e37d719f14a8d72692287d132547995672d3aba2/MONAIAuto3DSeg/MONAIAuto3DSeg.py#L1612-L1684">script</a> that generates this <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/releases/tag/ModelsTestResults">Auto3DSeg segmentation model catalog page</a>.</p>

---

## Post #4 by @Jithendra (2024-09-17 06:06 UTC)

<p>Thank you for providing the script. I successfully ran the segmentation process. Is it possible to generate 3D view images using a batch CLI command with <code>screencapture</code>? I understand that <code>screencapture</code> requires the layout manager to generate images, which typically needs the main window. Since this is not feasible with batch CLI commands running in a Unix terminal, is there an alternative workaround for this?</p>

---

## Post #5 by @lassoan (2024-09-17 14:58 UTC)

<p>You can do everything with commands on the terminal. You can pass Python commands as command-line arguments or you can put all the commands in a .py file and execute that from the command-line. If popping up of a GUI window is bothering you then you can use a <a href="https://github.com/pieper/SlicerDockers">dockerized version of Slicer</a>.</p>

---

## Post #6 by @Jithendra (2024-09-19 11:34 UTC)

<p>Thank you for providing the docker reference. I managed to get it working as suggested and generated screen captured images and video of it.</p>

---
