---
topic_id: 32149
title: "Execute Python Scripts Not In A General Linux Terminal"
date: 2023-10-11
url: https://discourse.slicer.org/t/32149
---

# Execute python scripts not in a general linux terminal

**Topic ID**: 32149
**Date**: 2023-10-11
**URL**: https://discourse.slicer.org/t/execute-python-scripts-not-in-a-general-linux-terminal/32149

---

## Post #1 by @Liang_Ma (2023-10-11 04:28 UTC)

<p>Hi, there.<br>
I am able to run a python script inside 3D slicer Python consle, by following the suggestion from <a href="https://discourse.slicer.org/t/running-python-script-in-slicer-in-linux/29124/3">here</a>:</p>
<p>I am now trying to run the same script in a normal Linux terminal, however, since slicer is a package that does not exist outside of the 3D slicer install environment, always some errors are reported.</p>
<p>I also tried doing such: ./Slicer --no-splash --no-main-window --python-script “MY_PYTHON” – this works somehow but still report some warning like below:</p>
<pre><code class="lang-auto">qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added
Error ImageIO factory did not return an ImageIOBase: MRMLIDImageIO
</code></pre>
<p>Is there a way that I can run the Python script in a nominal Linux terminal?</p>

---

## Post #2 by @Liang_Ma (2023-10-11 10:27 UTC)

<p>I don’t know why --but I can not modify my post now… actually just found the title is wrong-- it should be “Execute Python scripts in a generic Linux terminal”</p>

---
