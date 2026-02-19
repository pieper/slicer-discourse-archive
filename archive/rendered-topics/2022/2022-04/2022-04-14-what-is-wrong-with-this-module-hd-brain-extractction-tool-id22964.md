---
topic_id: 22964
title: "What Is Wrong With This Module Hd Brain Extractction Tool"
date: 2022-04-14
url: https://discourse.slicer.org/t/22964
---

# What is wrong with this module HD Brain Extractction Tool

**Topic ID**: 22964
**Date**: 2022-04-14
**URL**: https://discourse.slicer.org/t/what-is-wrong-with-this-module-hd-brain-extractction-tool/22964

---

## Post #1 by @slicer365 (2022-04-14 13:33 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc50ef930d4eb88028117bab4e2e6bf5145e5015.png" data-download-href="/uploads/short-url/A05J3Lk5UqAauhi66mqSaIG8ZEh.png?dl=1" title="1649943074(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc50ef930d4eb88028117bab4e2e6bf5145e5015_2_517x287.png" alt="1649943074(1)" data-base62-sha1="A05J3Lk5UqAauhi66mqSaIG8ZEh" width="517" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc50ef930d4eb88028117bab4e2e6bf5145e5015_2_517x287.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc50ef930d4eb88028117bab4e2e6bf5145e5015_2_775x430.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc50ef930d4eb88028117bab4e2e6bf5145e5015_2_1034x574.png 2x" data-dominant-color="C4C2C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1649943074(1)</span><span class="informations">1266×704 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Traceback (most recent call last):<br>
File “D:\MedSofts\Slicer\Slicer 4.13.0-2022-03-25\bin\Python\slicer\util.py”, line 2766, in tryWithErrorDisplay<br>
yield<br>
File “D:/MedSofts/Slicer/Slicer 4.13.0-2022-03-25/NA-MIC/Extensions-30741/HDBrainExtraction/lib/Slicer-4.13/qt-scripted-modules/HDBrainExtractionTool.py”, line 227, in onApplyButton<br>
self.logic.setupPythonRequirements()<br>
File “D:/MedSofts/Slicer/Slicer 4.13.0-2022-03-25/NA-MIC/Extensions-30741/HDBrainExtraction/lib/Slicer-4.13/qt-scripted-modules/HDBrainExtractionTool.py”, line 301, in setupPythonRequirements<br>
slicer.util.pip_install(‘git+https://github.com/MIC-DKFZ/batchgenerators#egg=batchgenerators’)<br>
File “D:\MedSofts\Slicer\Slicer 4.13.0-2022-03-25\bin\Python\slicer\util.py”, line 3333, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “D:\MedSofts\Slicer\Slicer 4.13.0-2022-03-25\bin\Python\slicer\util.py”, line 3307, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “D:\MedSofts\Slicer\Slicer 4.13.0-2022-03-25\bin\Python\slicer\util.py”, line 3276, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘D:/MedSofts/Slicer/Slicer 4.13.0-2022-03-25/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘git+https://github.com/MIC-DKFZ/batchgenerators#egg=batchgenerators’]’ returned non-zero exit status 1.</p>

---

## Post #2 by @lassoan (2022-04-14 23:19 UTC)

<p>Please check the application log for the root cause of the error. If you don’t find the error message there then you can open a Windows command prompt and type the install command there:</p>
<pre data-code-wrap="txt"><code class="lang-nohighlight">"D:/MedSofts/Slicer/Slicer 4.13.0-2022-03-25/bin/PythonSlicer.EXE" 
-m pip install git+https://github.com/MIC-DKFZ/batchgenerators#egg=batchgenerators
</code></pre>

---
