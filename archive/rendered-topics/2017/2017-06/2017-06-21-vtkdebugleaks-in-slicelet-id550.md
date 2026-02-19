---
topic_id: 550
title: "Vtkdebugleaks In Slicelet"
date: 2017-06-21
url: https://discourse.slicer.org/t/550
---

# vtkDebugLeaks in slicelet

**Topic ID**: 550
**Date**: 2017-06-21
**URL**: https://discourse.slicer.org/t/vtkdebugleaks-in-slicelet/550

---

## Post #1 by @jks1995 (2017-06-21 21:28 UTC)

<p>When I close my slicelete I always get an error box that says “vtkDebugLeaks has detected LEAKS!” and it lists a bunch of node types that still have instances. I am programming in python and I am not sure the proper way to resolve this. It even happens if I just open and close the app immediately. What can I do?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2017-06-21 22:10 UTC)

<p>This page should help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement</a></p>

---

## Post #3 by @jks1995 (2017-06-22 14:27 UTC)

<p>Using the Unregister function on the slicer AboutToQuit method doesnt seem to work.  See code sample below.</p>
<p><code>slicer.app.connect('aboutToQuit()', self.removeNodes)</code></p>
<pre><code>def removeNodes(self):
        '''
        Remove nodes from scene to prevent vtk leaks.
        '''
        n = slicer.mrmlScene.GetNodesByClass('vtkMRMRLFiducialListNode')
        n.UnRegister(slicer.mrmlScene)</code></pre>

---

## Post #4 by @jks1995 (2017-06-22 14:55 UTC)

<p>Also trying:</p>
<pre><code>n = slicer.mrmlScene.GetNodesByClass('vtkMRMRLFiducialListNode')
for i in xrange(n.GetNumberOfItems()):
  volume_node = n.GetItemAsObject(i)
  slicer.mrmlScene.RemoveNode(volume_node)
  volume_node.UnRegister(slicer.mrmlScene)
</code></pre>
<p>This also didn’t work.</p>

---

## Post #5 by @lassoan (2017-06-22 15:04 UTC)

<p>You don’t need to remove nodes from the scene on application exit, Slicer will take care of that.</p>
<p>In order that mechanism to work correctly, when you add a node to the scene then you should delete your reference to that node immediately, to let the scene take full ownership of that node. The scene will know when to delete that node (for example, when the node is removed from the scene or the entire scene is deleted).</p>
<p>For example, as shown on the wiki page I linked:</p>
<pre><code>n = slicer.mrmlScene.CreateNodeByClass('vtkMRMLViewNode')
slicer.mrmlScene.AddNode(n)
n.UnRegister(slicer.mrmlScene)
</code></pre>
<p>The problem is that your code keeps a reference to a MRML node or some other VTK objects. It is usually very difficult to find source of memory leaks. One technique is to comment out parts of your code until the memory leak is gone. When the leak is gone then you will know that the part you commented out last causes the leak.</p>

---

## Post #6 by @jks1995 (2017-06-22 15:09 UTC)

<p>I am also having this issue before I add any nodes to slicer. I can launch the slicelete and close it immediately and still have a warning dialog pop up.</p>

---

## Post #7 by @lassoan (2017-06-22 15:36 UTC)

<p>What template did you use to create your slicelet?<br>
Is your code available on github so that we can have a look?</p>
<p>(Note: spelling of the slicer applet term is “slicelet” not “slicelete”)</p>

---

## Post #8 by @lassoan (2017-06-22 15:50 UTC)

<aside class="quote no-group" data-username="jks1995" data-post="4" data-topic="550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/90db22/48.png" class="avatar"> jks1995:</div>
<blockquote>
<p>This also didn’t work.</p>
</blockquote>
</aside>
<p>If you need help, we must understand your problem, and for that you always need to provide full error message and/or description of what you did, what you expected to happen, and what happened instead.</p>
<p>Note that (as described on the page that I linked) slicer.mrmlScene.GetNodesByClass creates a vtkCollection that must be unregistered immediately after you get the object in Python, otherwise the collection will not be destroyed and it will keep a reference to all the nodes inside it.</p>
<p>To remove all markup nodes from the scene (note that in Slicer4 there are no more fiducial list nodes):</p>
<pre><code>nodes = slicer.mrmlScene.GetNodesByClass('vtkMRMLMarkupsFiducialNode')
nodes.UnRegister(None)
for i in range(nodes.GetNumberOfItems()):
  node = nodes.GetItemAsObject(i)
  slicer.mrmlScene.RemoveNode(node)
</code></pre>

---

## Post #9 by @jamesobutler (2017-06-22 22:15 UTC)

<p>Here’s snippets of code from <a class="mention" href="/u/jks1995">@jks1995</a> regarding his issue.</p>
<p>Instantiating “Analysis” and “Acquisition” in ModuleEQ does not result in vtkdebug leaks even though <code>layout_widget.layoutManager()</code> is passed into them successfully as an argument and used in the destination file.</p>
<p>However, passing <code>layout_widget</code> as an argument into FileB, which is then added as a widget to layout, results in vtkdebug leaks upon closing of the slicelet.</p>
<pre><code>from FileB import FileB
from Analysis import Analysis
from Acquisition import Acquisition
from __main__ import qt, slicer

class ModuleEQ():
    def __init__(self):
        '''
        Instantiate all the major GUIs and their corresponding classes.
        '''
        layout_widget = slicer.qMRMLLayoutWidget()
        layout_widget.setMRMLScene(slicer.mrmlScene)

        layout_manager = layout_widget.layoutManager()

        acquisition = Acquisition(layout_manager)
        acquisition_gui = acquisition.getUI()

        analysis = Analysis(layout_manager)
        analysis_gui = analysis.getUI()

        file_b = FileB(layout_widget, acquisition, analysis)

if __name__ == "ModuleEQ":
    ModuleEQ()
</code></pre>
<p>Below is the second file where the layout_widget is passed into.<br>
<a href="http://FileB.py" rel="nofollow noopener">FileB.py</a>:</p>
<pre><code>def __init__(self, layout_widget, acquisition, analysis):
            self.layout_widget = layout_widget
            self.acquisition = acquisition
            self.analysis = analysis
            self.setUpUI()

def setUpUI(self):
            '''
            Set up the user interface using the UI file.
            '''
            ui_filepath = os.path.dirname(os.path.realpath(__file__)) + '/FileB.ui'
            ui_loader = qt.QUiLoader()
            f = qt.QFile(ui_filepath)
            f.open(qt.QFile.ReadOnly)
            self.ui = ui_loader.load(f)
            f.close()

            #add acquisition and analysis gui into FileB gui
            self.main_tabs = self.ui.findChild(qt.QTabWidget, 'main_tabs')
            self.main_tabs.insertTab(0, self.acquisition.getUI(), "Ultrasound Acquisition")
            self.main_tabs.insertTab(1, self.analysis.getUI(), "Image Analysis")

            #add slicer views to Qframe in FileB gui
            slicer_views_frame = self.ui.findChild(qt.QFrame, 'slicer_frame')
            slicer_views_frame.setLayout(qt.QVBoxLayout())
            slicer_views_frame.layout().addWidget(self.layout_widget)</code></pre>

---

## Post #10 by @jcfr (2017-06-24 21:23 UTC)

<p>Fwiw, instantiating a node using :</p>
<p>n = slicer.vtkMRMLViewNode()</p>
<p>Will avoid the use of UnRegister.</p>
<p>Hth<br>
Jc</p>

---

## Post #11 by @Ted_Chen (2018-01-23 03:08 UTC)

<p>I also encountered same problem with same mechanism. (use QUiLoader to load a ui and set central wiget to qMRMLLayoutWidget will get vtkDebugLeaks while closing application)</p>
<p>hello.ui</p>
<pre><code>&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;ui version="4.0"&gt;
 &lt;class&gt;MainWindow&lt;/class&gt;
 &lt;widget class="QMainWindow" name="MainWindow"&gt;
  &lt;property name="geometry"&gt;
   &lt;rect&gt;
    &lt;x&gt;0&lt;/x&gt;
    &lt;y&gt;0&lt;/y&gt;
    &lt;width&gt;800&lt;/width&gt;
    &lt;height&gt;600&lt;/height&gt;
   &lt;/rect&gt;
  &lt;/property&gt;
  &lt;property name="windowTitle"&gt;
   &lt;string&gt;MainWindow&lt;/string&gt;
  &lt;/property&gt;
  &lt;widget class="QWidget" name="centralwidget"/&gt;
  &lt;widget class="QMenuBar" name="menubar"&gt;
   &lt;property name="geometry"&gt;
    &lt;rect&gt;
     &lt;x&gt;0&lt;/x&gt;
     &lt;y&gt;0&lt;/y&gt;
     &lt;width&gt;800&lt;/width&gt;
     &lt;height&gt;21&lt;/height&gt;
    &lt;/rect&gt;
   &lt;/property&gt;
  &lt;/widget&gt;
  &lt;widget class="QStatusBar" name="statusbar"/&gt;
 &lt;/widget&gt;
 &lt;resources/&gt;
 &lt;connections/&gt;
&lt;/ui&gt;
</code></pre>
<p><a href="http://hello.py" class="onebox" target="_blank" rel="nofollow noopener">hello.py</a></p>
<pre><code># coding: utf-8
import slicer 
import qt

# Load UI file
uiloader = qt.QUiLoader()
file = qt.QFile("D:/project/slicer/Base/Python/hello.ui")
file.open(qt.QFile.ReadOnly)
dtcUI = uiloader.load(file)
file.close()

# set central widget
layoutMrml = slicer.qMRMLLayoutWidget()
layoutMrml.setMRMLScene(slicer.mrmlScene)

# this line will cause memory leak
dtcUI.setCentralWidget(layoutMrml)

dtcUI.show() 
</code></pre>
<p>I don’t know what and how to release the referenced vtk object ?</p>

---

## Post #12 by @lassoan (2018-01-23 05:04 UTC)

<p>I’m not sure what the issue is, but in production code you should probably disable memory leak checking (by turning off Slicer_USE_VTK_DEBUG_LEAKS CMake flag when configuring Slicer build). In the latest stable (Slicer-4.8.1), no memory leaks are reported; in nightly builds, some builds may have Slicer_USE_VTK_DEBUG_LEAKS option enabled.</p>

---

## Post #13 by @Ted_Chen (2018-01-23 05:43 UTC)

<p>Andras,</p>
<p>I am running the python script under self-compiled slicer (tag v4.8.1) and slicer will show me the vtkDebugLeaks message to me while closing.</p>
<p>According to your reply, do you mean the python code i showed should not necessary to release any vtk object?</p>

---

## Post #14 by @lassoan (2018-01-23 14:09 UTC)

<p>If memory leaks are reported then it means that you either have to release some resources (delete variables, set references to objects to None, etc.) or tune the order of object deletion.</p>
<p>Examples on Slicer’s <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets#Additional_steps_to_run_the_slicelet_without_a_main_window">slicelet page</a> work without memory leaks, you can start from those and see which of your change introduces the leak - then you know exactly where to look for the root cause of the issue.</p>
<p>You may also choose to keep the Slicer main window and hide all custom elements (toolbars, menu bars, etc.) that you don’t need.</p>

---

## Post #15 by @lassoan (2018-01-23 14:21 UTC)

<aside class="quote no-group" data-username="Ted_Chen" data-post="13" data-topic="550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ec9cab/48.png" class="avatar"> Ted_Chen:</div>
<blockquote>
<p>I am running the python script under self-compiled slicer</p>
</blockquote>
</aside>
<p>Disable Slicer_USE_VTK_DEBUG_LEAKS when you are configuring your Slicer build if you don’t want to see debug leaks report during development. Always disable Slicer_USE_VTK_DEBUG_LEAKS in software that is shipped to customers.</p>

---

## Post #16 by @Ted_Chen (2018-01-24 01:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Examples on Slicer’s slicelet page work without memory leaks, you can start from those and see which of your change introduces the leak - then you know exactly where to look for the root cause of the issue.</p>
</blockquote>
</aside>
<p>My first version is using that method to customize our own UI with no leaks but after we trasferring to use  QUiLoader to load Qt widgets and set slicer.mrmlScene to QMainWindow main widget, application will report leaks after closing.</p>
<p>I am wondering slicer.mrmlScene will also be referenced while we set main widget of QMainWindow to mrmlScene and it’s necessary to set main widget to None before closing app.</p>

---
