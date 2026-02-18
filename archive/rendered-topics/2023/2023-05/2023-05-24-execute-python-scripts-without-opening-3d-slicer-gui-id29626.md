# Execute python scripts without opening 3D-slicer GUI

**Topic ID**: 29626
**Date**: 2023-05-24
**URL**: https://discourse.slicer.org/t/execute-python-scripts-without-opening-3d-slicer-gui/29626

---

## Post #1 by @dhanushkannan (2023-05-24 10:48 UTC)

<p>Hi all,<br>
I have scripted a python code which segments skull from the input DICOM data. When I try to execute the script from CLI using the following command</p>
<pre><code class="lang-auto">Slicer.exe --python-script "app.py" --no-splash --no-main-window
</code></pre>
<p>the 3d-slicer GUI keeps opening. I need to execute the script without opening GUI.</p>
<p>Thanks in advance. Anyone please help me with it</p>

---

## Post #2 by @lassoan (2023-05-24 12:20 UTC)

<p>Does the full Slicer GUI appear? What Slicer version are you using? Does it do the same if you specify full path for Slicer.exe and app.py?</p>

---

## Post #3 by @dhanushkannan (2023-05-24 12:40 UTC)

<p>I have scripted a python code which segments skull from the input DICOM data. When I try to execute the script from CLI using the following command</p>
<pre><code class="lang-auto">Slicer.exe --python-script "app.py" --no-splash --no-main-window
</code></pre>
<p>the code does not gets executed and the result is not obtained.</p>
<p>If the script is executed using the following command</p>
<pre><code class="lang-auto">Slicer.exe --python-script "app.py"
</code></pre>
<p>the result is generated but, the GUI appears.</p>
<p><strong>I need to execute the script without opening GUI.</strong></p>

---

## Post #4 by @dhanushkannan (2023-05-24 12:41 UTC)

<p>yes, the full Slicer GUI appears.<br>
My Slicer version is 5.2.2</p>

---

## Post #5 by @lassoan (2023-05-24 13:18 UTC)

<p>Everything works perfectly for me with Slicer-5.2.2 on Windows. If I create an <code>app.py</code> file with this content:</p>
<pre><code class="lang-python">import slicer
slicer.util.messageBox('test')
</code></pre>
<p>And run this command:</p>
<pre><code>"c:\Users\andra\appdata\Local\NA-MIC\Slicer 5.2.2\Slicer.exe" --no-splash --no-main-window --python-script "c:\Users\andra\appdata\Local\NA-MIC\Slicer 5.2.2\test.py"
</code></pre>
<p>then all I get is a popup window, displayed by app.py executed by Slicer. The Slicer main window is not displayed.</p>

---

## Post #6 by @dhanushkannan (2023-05-25 06:04 UTC)

<p>The messageBox appears while executing the code. But the other lines of code are not executed.</p>
<p>I have developed a python script which segments skull from dicom data.</p>

---

## Post #7 by @lassoan (2023-05-26 13:30 UTC)

<p>I’m not sure what “other lines” you are referring to. If you provide an example script that is not executed the way you expect then we can investigate.</p>
<p>Note that <code>Slicer.exe</code> launcher is a GUI application, therefore it cannot print anything to the console. Maybe you think that some code lines are not sure executed because you don’t see the output in the console? See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/tips.html#console-output-on-windows">here</a> how you can see the console output on Windows.</p>

---
