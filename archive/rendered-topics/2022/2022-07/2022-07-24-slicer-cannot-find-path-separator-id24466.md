---
topic_id: 24466
title: "Slicer Cannot Find Path Separator"
date: 2022-07-24
url: https://discourse.slicer.org/t/24466
---

# slicer cannot find path separator

**Topic ID**: 24466
**Date**: 2022-07-24
**URL**: https://discourse.slicer.org/t/slicer-cannot-find-path-separator/24466

---

## Post #1 by @Xin_Chen (2022-07-24 15:52 UTC)

<p>Hello everyone<br>
I used Slicer 5.1.0 (Preview Release) on Win 10 (64 bit).<br>
Now, I want to open the extension Module from github. I succefully add the path of Module in Edit tab. However, when I execute the module, Slicer told me that :</p>
<pre><code class="lang-auto">ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'D:EEG_ToolBoxSemiology-Visualisation-Tool-masterrequirements.txt'
Traceback (most recent call last):
  File "D:/EEG_ToolBox/Semiology-Visualisation-Tool-master/slicer/SemiologyVisualisation.py", line 1423, in installRepository
    import mega_analysis
  File "D:\EEG_ToolBox\Semiology-Visualisation-Tool-master\mega_analysis\__init__.py", line 2, in &lt;module&gt;
    from .crosstab.gif_lobes_from_excel_sheets import gif_lobes_from_excel_sheets
  File "D:\EEG_ToolBox\Semiology-Visualisation-Tool-master\mega_analysis\crosstab\gif_lobes_from_excel_sheets.py", line 1, in &lt;module&gt;
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:/EEG_ToolBox/Semiology-Visualisation-Tool-master/slicer/SemiologyVisualisation.py", line 99, in setup
    self.logic.installRepository()
  File "D:/EEG_ToolBox/Semiology-Visualisation-Tool-master/slicer/SemiologyVisualisation.py", line 1429, in installRepository
    slicer.util.pip_install(
  File "E:\Program Files\slicer-PreRelease\Slicer 5.1.0-2022-07-22\bin\Python\slicer\util.py", line 3535, in pip_install
    _executePythonModule('pip', args)
  File "E:\Program Files\slicer-PreRelease\Slicer 5.1.0-2022-07-22\bin\Python\slicer\util.py", line 3498, in _executePythonModule
    logProcessOutput(proc)
  File "E:\Program Files\slicer-PreRelease\Slicer 5.1.0-2022-07-22\bin\Python\slicer\util.py", line 3467, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['E:/Program Files/slicer-PreRelease/Slicer 5.1.0-2022-07-22/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', '-r', 'D:EEG_ToolBoxSemiology-Visualisation-Tool-masterrequirements.txt']' returned non-zero exit status 1.
</code></pre>
<p>I know, the module need load ‘D:\EEG_ToolBox\Semiology-Visualisation-Tool-master\requirements.txt’, and this file existed in this path indeed.<br>
I don’t know why Slicer can’t recognize the path separator ('')?<br>
Could any one help me?</p>

---

## Post #2 by @lassoan (2022-07-24 15:56 UTC)

<p>It seems that the path was not specified correctly. See how to specify native Windows paths <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-type-file-paths-in-python">here</a>.</p>

---
