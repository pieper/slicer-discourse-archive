# Macro XML to python

**Topic ID**: 15803
**Date**: 2021-02-03
**URL**: https://discourse.slicer.org/t/macro-xml-to-python/15803

---

## Post #1 by @aldoSanchez (2021-02-03 01:10 UTC)

<p>Hi, I’m recording some macros and I want to know if there’s any way that I can convert the XLM code to python code for Slicer.<br>
Thanks</p>

---

## Post #2 by @jcfr (2021-02-03 20:22 UTC)

<p>There are currently no way of recording macro as python script. As described below, there is a way to record python code but this would be very similar to the generated XML and challenging to maintain.</p>
<p><strong>Question</strong>: What are you trying to achieve ? By understanding this, we may be able to better answer your question.</p>
<p>For now, I instead suggest to write <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/SelfTestModule">self test</a> by hand.</p>
<p>There are a lot of python snippets available <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">here</a>, and the extension wizard will create a skeleton of module including the relevant infrastructure to run the test.</p>
<h3><a name="p-54034-enabling-macro-recording-1" class="anchor" href="#p-54034-enabling-macro-recording-1" aria-label="Heading link"></a>Enabling macro recording</h3>
<p>Answers in this post assumes you are talking about using <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/QtTesting">QtTesting</a> functionality that can be enabled through the settings:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f713798341e9e2d4d146b129c41af929913f87a3.png" data-download-href="/uploads/short-url/zfJESZ6LEramVnky4VyKSveA1WP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f713798341e9e2d4d146b129c41af929913f87a3.png" alt="image" data-base62-sha1="zfJESZ6LEramVnky4VyKSveA1WP" width="442" height="280"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">442×280 25.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-54034-qttesting-and-python-2" class="anchor" href="#p-54034-qttesting-and-python-2" aria-label="Heading link"></a>QtTesting and python</h3>
<p>All of that said, we could look into generating python code similar to what is done in Paraview (see <a href="https://www.paraview.org/ParaView/index.php/Testing_Guide#Python_based_testing">here</a>). The code would be similar to the one posted below:</p>
<pre data-code-wrap="python"><code class="lang-python">import QtTesting
import QtTestingImage
object1 = 'MainWindow/menubar/menuFile'
QtTesting.playCommand(object1, 'activate', 'actionFileLoadServerState')
object2 = 'MainWindow/ServerStartupBrowser/connect'
QtTesting.playCommand(object2, 'activate', )
object3 = 'MainWindow/FileLoadServerStateDialog'
QtTesting.playCommand(object3, 'filesSelected', '$PARAVIEW_DATA_ROOT/Data/LoadStateMultiView.pvsm')
snapshotWidget = 'MainWindow/1pqRenderWindowManager0/SplitterFrame/MultiViewSplitter/0/Viewport'
QtTestingImage.compareImage(snapshotWidget, 'LoadStateMultiView.png', 200, 200);
</code></pre>

---

## Post #3 by @lassoan (2021-02-03 20:37 UTC)

<p>Recording GUI events (button clicks, etc.) has very limited use (only for testing, and even there it is quite fragile). Meaningful workflow automation Python scripts should operate at lower level, by changing properties of MRML nodes and calling module logic functions.</p>
<p>I’ve recently implemented a simple Python script that observes all MRML node changes and generate a list of node property modifications (by comparing MRML node PrintSelf results before and after the node modification). This can be used to generate a runnable, user-editable Python script. This is similar to what Paraview can do. However, this turned out not to be very useful, because it is too low level (for a single user action you get a bunch of node property modification events, but you don’t know why the node ended up being modified like that).</p>
<p>What we would really need is an intermediate level, where a user action is translated to a few high-level method calls. I’m not sure what is the easiest way to achieve this. Maybe we could add a specially formatted log message whenever a logic method is called (and macro recording is enabled), and these could be easily converted to runnable Python code.</p>

---

## Post #4 by @pll_llq (2021-02-03 21:19 UTC)

<p>Having a log of what logic methods are called would be really great. Module logic is not always intuitive and having the system to give some clue on where to look for the methods that replicate the actions that the user has just done via the UI would really speed up the creation of simple automations.</p>

---

## Post #5 by @aldoSanchez (2021-02-04 02:05 UTC)

<p>hi i want to do this <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eb4065295926830df20068ad2f71e6c2b8ae1c5.png" alt="image" data-base62-sha1="6F9FdoR1MQ9fXJDMVakRg6PyuH3" width="438" height="204"><br>
open 2 files at the same time and select a freeSurferLabels<br>
just this by python code</p>

---

## Post #6 by @aldoSanchez (2021-02-04 03:56 UTC)

<p>larssoan could you please show me this script<br>
-implemented a simple Python script that observes all MRML node changes and generate a list of node property modifications (by comparing MRML node PrintSelf results before and after the node modification)</p>

---

## Post #7 by @aldoSanchez (2021-02-04 05:11 UTC)

<p>when i code this:</p>
<pre><code class="lang-python">import QtTesting
import QtTestingImage
</code></pre>
<p>a get this message :</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:/Users/aldot/AppData/Roaming/NA-MIC/Extensions-28257/Sandbox/lib/Slicer-4.10/qt-scripted-modules/UserStatistics.py", line 805, in &lt;module&gt;
    class IdleDetectionEventFilter(qt.QObject):
AttributeError: 'module' object has no attribute 'QObject'
</code></pre>

---

## Post #8 by @jcfr (2021-02-04 05:45 UTC)

<aside class="quote no-group" data-username="aldoSanchez" data-post="5" data-topic="15803">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/5f9b8f/48.png" class="avatar"> aldoSanchez:</div>
<blockquote>
<p>open 2 files at the same time and select a freeSurferLabels<br>
just this by python code</p>
</blockquote>
</aside>
<p>Assuming the <code>SlicerFreeSurfer</code> extension is installer, the follow will allow you to load files using python:</p>
<pre data-code-wrap="python"><code class="lang-python">slicer.util.loadVolume('/path/to/volume.nrrd', {'colorNodeID': 'vtkMRMLColorTableNodeFile'})
slicer.util.loadLabelVolume('/path/to/label.nrrd')
</code></pre>
<p>For list of properties that can be passed to <code>loadVolume</code> and <code>loadLabelVolume</code>, see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/volumes.html#reading-from-file">Developer Guide / Modules API / Volumes / Reading from file</a></p>

---

## Post #9 by @jcfr (2021-02-04 05:48 UTC)

<aside class="quote no-group quote-modified" data-username="aldoSanchez" data-post="7" data-topic="15803" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/5f9b8f/48.png" class="avatar"> aldoSanchez:</div>
<blockquote>
<p>when i code this:</p>
<pre><code class="lang-auto">import QtTesting
import QtTestingImage
[...]
</code></pre>
</blockquote>
</aside>
<p>This was an example of code used in Paraview, it is <strong>not</strong> supported in Slicer.</p>

---

## Post #10 by @aldoSanchez (2021-02-05 07:10 UTC)

<p>thanks, it works, not as I like to<br>
but I going to play a little to get the colors I want.<br>
i leave the code :</p>
<pre><code class="lang-python">slicer.util.loadVolume('C:/Users/aldot/Desktop/Seg30/Aldo 3/Done/IXI-aseg.mgz', {'colorNodeID': 'vtkMRMLColorTableNodeFileGenericColors.txt'})
</code></pre>
<p>i couldn’t use this one returns a falls state:</p>
<pre><code class="lang-python">slicer.util.loadLabelVolume('/path/to/label.nrrd')
slicer.util.loadLabelVolume('C:/Program Files/Slicer 4.10.2/share/FreeSurfer')
False
slicer.util.loadLabelVolume('C:/Program Files/Slicer 4.10.2/share/Slicer-4.10/ColorFiles/Inferno.txt')
False
</code></pre>

---

## Post #11 by @aldoSanchez (2021-02-05 07:14 UTC)

<pre><code class="lang-python">slicer.util.loadVolume('C:/Users/aldot/Desktop/Seg30/Aldo 3/Done/IXI134-aseg.mgz', {'colorNodeID': 'vtkMRMLColorTableNodeFile'})
</code></pre>
<p>this one for free surfer but because there are 3 diferent files i dont know what to do</p>

---

## Post #12 by @aldoSanchez (2021-02-05 17:42 UTC)

<p>now it works perfect thanks for the information.</p>
<pre><code class="lang-python">slicer.util.loadVolume('C:/Users/aldot/Desktop/Seg30/Aldo 3/Done/IXI-nu.mgz')
slicer.util.loadLabelVolume('C:/Users/aldot/Desktop/Seg30/Aldo 3/Done/IXI-aseg.mgz', {'colorNodeID': 'vtkMRMLColorTableNodeFile'})
</code></pre>

---
