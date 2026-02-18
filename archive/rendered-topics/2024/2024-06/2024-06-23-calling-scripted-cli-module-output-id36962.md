# Calling scripted cli module Output

**Topic ID**: 36962
**Date**: 2024-06-23
**URL**: https://discourse.slicer.org/t/calling-scripted-cli-module-output/36962

---

## Post #1 by @fqzhice (2024-06-23 05:45 UTC)

<p>I create a scripted cli module according to SlicerPythonCLIExample, and set print in .py file.</p>
<pre><code class="lang-auto">#!/usr/bin/env python-real  `
import os  
print("call vessel segment!")`
</code></pre>
<p>Then in a cpp file , it is called as below:</p>
<pre><code class="lang-auto">PythonQt::init();
PythonQtObjectPtr context = PythonQt::self()-&gt;getMainModule();
context.evalScript(QString(
    "slicer.cli.run(slicer.modules.ctaseg, None, None)\n"
));
</code></pre>
<p>But there is no output string in console window. just</p>
<pre><code class="lang-auto">Found CommandLine Module, target is C:/PilotImage/Release/Slicer-build/lib/Slicer-5.4/cli-modules/Release/CTASeg.py
ModuleType: CommandLineModule
No input data assigned to "Input Volume"
</code></pre>
<p>Does this script run correctly？ or the input volume is necessary</p>
<p>Thanks</p>

---

## Post #2 by @fqzhice (2024-06-23 06:55 UTC)

<p>Later</p>
<pre><code>vtkMRMLNode* dummyNode = qSlicerApplication::application()-&gt;mrmlScene()-&gt;GetFirstNodeByClass("vtkMRMLScalarVolumeNode");

PythonQt::init();
PythonQtObjectPtr context = PythonQt::self()-&gt;getMainModule();
context.evalScript(QString(
    "param={}\n"
    "param['inputVolume']=%1\n"
    "slicer.cli.runSync(slicer.modules.ctaseg, None, parameters=param)\n"
).arg(dummyNode-&gt;GetID()));
</code></pre>
<p>it says name ‘vtkMRMLScalarVolumeNode1’ is not defined</p>

---

## Post #3 by @lassoan (2024-06-23 22:22 UTC)

<p>Process output is logged into the application log and also available in the CLI module node.</p>
<p>If you develop in C++ then you can use the C++ API (no need to call out to Python).</p>

---

## Post #4 by @fqzhice (2024-06-24 01:20 UTC)

<p>I try to call the custom AI-module in python script.<br>
Now I cant find the generated result image, so i set an print to check if it works. it seems fails .<br>
I try to find in log later.<br>
Thanks</p>

---

## Post #5 by @lassoan (2024-06-24 02:04 UTC)

<p>We have many modules that segment images by using xuatom AI models. I would recommend to start from a similar module.</p>
<p>Does the segmentation tool use nn-unet, monai, or just pyrorch directly?</p>

---

## Post #6 by @fqzhice (2024-06-24 08:50 UTC)

<p>The module is developped  by other guy and i was required to make an integration. Maybe is  some unet module.<br>
I just call “slicer.util.launchConsoleProcess” to implement it</p>
<p>Thanks very much</p>

---

## Post #7 by @lassoan (2024-06-24 10:53 UTC)

<p>If it is nnunet then I would recommend to use <a href="https://github.com/gaudot/SlicerDentalSegmentator" class="inline-onebox">GitHub - gaudot/SlicerDentalSegmentator: 3D Slicer extension for fully-automatic segmentation of CT and CBCT dental volumes.</a> extension as an example, and if anything else then the <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg" class="inline-onebox">GitHub - lassoan/SlicerMONAIAuto3DSeg: Extension for 3D Slicer for running MONAI Auto3DSeg models</a> extension.</p>

---
