# find cli-modules path

**Topic ID**: 29999
**Date**: 2023-06-13
**URL**: https://discourse.slicer.org/t/find-cli-modules-path/29999

---

## Post #1 by @Kening_Zhang (2023-06-13 02:54 UTC)

<p>FiberTractMeasurementsCLI = “/Applications/Slicer.app/Contents/Extensions-31382/SlicerDMRI/lib/Slicer-5.2/cli-modules/FiberTractMeasurements”<br>
This is the path I need to use in the later code, but for other users, the path changes depends on the version of the Slicer they installed. So I use a command:<br>
FiberTractMeasurementsCLI = glob.glob(“<strong>/SlicerDMRI/lib/</strong>/cli-modules/FiberTractMeasurements”, recursive=True)[0]   to search the path in the computer, but it takes too long time to find. I wonder if there are any command in Slicer which can find the path of the module installed.<br>
By the way, the module is contained in DMRI.<br>
Best wishes,<br>
Joshua</p>

---

## Post #2 by @pieper (2023-06-13 11:41 UTC)

<p>I don’t have DMRI installed on this machine, but since the module you are running is a CLI, you should be able to do something like this:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.modules.modelmaker.path
'/Applications/Slicer-5.2.1.app/Contents/lib/Slicer-5.2/cli-modules/ModelMaker'
</code></pre>
<p>Replace modelmaker with fibertractmeasurements.</p>

---
