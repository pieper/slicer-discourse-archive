---
topic_id: 25049
title: "Setting Up Unix Ubuntu Local Paths"
date: 2022-09-02
url: https://discourse.slicer.org/t/25049
---

# Setting Up Unix (Ubuntu) Local Paths?

**Topic ID**: 25049
**Date**: 2022-09-02
**URL**: https://discourse.slicer.org/t/setting-up-unix-ubuntu-local-paths/25049

---

## Post #1 by @Matt_Park (2022-09-02 03:31 UTC)

<p>I am trying to use the Cervical Vertebra Tools extension on 5.03 r30893/7ea0f43 and am getting a “setup local paths variables” error. Searching has not found a good link.</p>
<p>Ubuntu 20.04</p>
<p>I get the following errors:</p>
<pre><code class="lang-auto">VisSimCommonLogic: initializing global variables:
 Defaults paths: 
      VisSimTools folder: /home/xyx/VisSimTools
      Output folder     : /home/xyz/VisSimTools/outputs
      elastix binaries are found in /home/matt/Downloads/Slicer-5.0.3-linux-amd64/NA-MIC/Extensions-30893/SlicerElastix/lib/Slicer-5.0/elastix
      Spine Extension is selected
      Models or contents are wrong, trying to download ...
      Downloading VisSim Tools  ... 
      Downloading VisSimTools others ...
     Extracting to user home 
      Error: can not download and extract VisSimTools ...
"There is no item named '/home/xyz/' in the archive"
setup local paths variables.........................
removeOtputsFolderContents ........................ 
STOPPED: error in input or during the segmentation
unsupported operand type(s) for &gt;&gt;: 'builtin_function_or_method' and 'PythonQtStdOutRedirect'. Did you mean "print(&lt;message&gt;, file=&lt;output_stream&gt;)"?
</code></pre>
<p>Thanks,<br>
Matt</p>

---

## Post #2 by @pieper (2022-09-02 12:15 UTC)

<p>Others <a href="https://discourse.slicer.org/t/help-over-vissimtools/8203">have asked about that extension</a> on this forum and I don’t see that they got any answers.  Try contacting the developers <a href="https://github.com/MedicalImageAnalysisTutorials/SlicerCervicalSpine">on github</a> for suggestions.</p>

---
