# Python interactor new features [load script, recent scripts]

**Topic ID**: 25859
**Date**: 2022-10-24
**URL**: https://discourse.slicer.org/t/python-interactor-new-features-load-script-recent-scripts/25859

---

## Post #1 by @mrrezaie (2022-10-24 11:11 UTC)

<p>Hi,</p>
<p>The Python interactor is not user-friendly at all and it would be great if it has a section in GUI for choosing and loading a script (.py file) as well as a history of recently loaded scripts (e.g. right-click on the Python interaction window and choosing “load script” or select from “recent scripts”; or add these options in File&gt;).</p>
<p>The following topic is a solution but is not user-friendly.<br>
<a href="https://discourse.slicer.org/t/load-python-script-from-harddisk-in-slicers-s-python-interactor/17399">Load python script from harddisk in Slicers´s Python Interactor? - Support - 3D Slicer Community</a></p>
<p>Thank you in advance.</p>

---

## Post #2 by @pieper (2022-10-24 12:10 UTC)

<p>+1 for improving the python console.  I’d also like to see it save/restore history and support searching history (like Ctrl-R in bash).  In fact why not let you search through the histories of all sessions.  Also tab-completion of file paths would be great.  Combining traditional command line features with some nice menus and dialogs could make things a lot easier.</p>
<p>I’ve thought about working on these features from time to time, but always find that workarounds like <code>exec(open(path).read())</code> that are good enough once you know them.</p>

---

## Post #3 by @lassoan (2022-10-25 04:59 UTC)

<p>I’ve made some improvements in the past few days (will be available in the Slicer Preview Release from Wednesday):</p>
<ul>
<li>Instead of <code>exec(open(path).read())</code> you can hit <kbd>Ctrl</kbd>-<kbd>r</kbd>. Last path is remembered, so you can rerun a script using <kbd>Ctrl</kbd>-<kbd>r</kbd>, <kbd>Enter</kbd>. This feature also somewhat serves a history of recently loaded scripts (the displayed native file selector can show recent files in the current folder, favorite folders, etc.)</li>
<li>If you copy-paste code into an empty line then instead of line-by-line execution, the code is run at once (fixing the annoying indentation errors due to presence of empty lines).</li>
</ul>
<p>Command history is preserved in the application log, so you can always look up all commands of the last 10 or so sessions. It would be very easy to save the command history and reload them when Slicer is restarted. However, I don’t feel a motivation to implement it, because if I want to re-run some code many times then I usually put it into a Jupyter notebook (Slicer can run as a Jupyter kernel) or I put it into a scripted loadable module template (if I want to do interactive debugging in a Python IDE). If you want to rerun a set of scripts then it is also very easy to drop a few buttons on a scripted loadable module template and make those scripts run at the click of a button. You can also assign keyboard shortcuts to loading specific Python files and run them.</p>

---

## Post #4 by @lassoan (2023-03-21 02:19 UTC)



---
