---
topic_id: 25795
title: "Skull Stripping Using Hdbrainextraction"
date: 2022-10-20
url: https://discourse.slicer.org/t/25795
---

# SKULL STRIPPING USING "HDBrainExtraction"

**Topic ID**: 25795
**Date**: 2022-10-20
**URL**: https://discourse.slicer.org/t/skull-stripping-using-hdbrainextraction/25795

---

## Post #1 by @D.Prasad (2022-10-20 05:25 UTC)

<p>Operating system: windows 11<br>
Slicer version: 5.0.3 r30893/7eaof43<br>
Expected behavior:  skull stripping<br>
Actual behavior:</p>
<p>Failed to compute results.</p>
<pre><code class="lang-auto">Command '['C:/Users/admin/AppData/Local/NA-MIC/Slicer 5.0.3/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'git+https://github.com/MIC-DKFZ/batchgenerators#egg=batchgenerators']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "C:/Users/admin/AppData/Local/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/HDBrainExtraction/lib/Slicer-5.0/qt-scripted-modules/HDBrainExtractionTool.py", line 227, in onApplyButton
    self.logic.setupPythonRequirements()
  File "C:/Users/admin/AppData/Local/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/HDBrainExtraction/lib/Slicer-5.0/qt-scripted-modules/HDBrainExtractionTool.py", line 301, in setupPythonRequirements
    slicer.util.pip_install('git+https://github.com/MIC-DKFZ/batchgenerators#egg=batchgenerators')
  File "C:\Users\admin\AppData\Local\NA-MIC\Slicer 5.0.3\bin\Python\slicer\util.py", line 3527, in pip_install
    _executePythonModule('pip', args)
  File "C:\Users\admin\AppData\Local\NA-MIC\Slicer 5.0.3\bin\Python\slicer\util.py", line 3490, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\admin\AppData\Local\NA-MIC\Slicer 5.0.3\bin\Python\slicer\util.py", line 3459, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/admin/AppData/Local/NA-MIC/Slicer 5.0.3/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'git+https://github.com/MIC-DKFZ/batchgenerators#egg=batchgenerators']' returned non-zero exit status 1.
</code></pre>
<p>plz do help me what to do.</p>

---

## Post #2 by @jcfr (2022-10-20 06:16 UTC)

<p>Could you try to locally edit the file</p>
<blockquote>
<p><code>C:/Users/admin/AppData/Local/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/HDBrainExtraction/lib/Slicer-5.0/qt-scripted-modules/HDBrainExtractionTool.py</code></p>
</blockquote>
<p>by editing line 301 implementing the following change:</p>
<pre data-code-wrap="diff"><code class="lang-diff">-slicer.util.pip_install('git+https://github.com/MIC-DKFZ/batchgenerators#egg=batchgenerators')
+slicer.util.pip_install("batchgenerators")
</code></pre>
<p>For reference, here is also link to the corresponding source file. See <a href="https://github.com/lassoan/SlicerHDBrainExtraction/blob/c308995da9ded06c0833f8c3681e8202005db99d/HDBrainExtractionTool/HDBrainExtractionTool.py#L301">HDBrainExtractionTool/HDBrainExtractionTool.py#L301</a></p>
<p>I suspect the problem is due to the fact you may not have <code>git</code> installed.</p>

---
