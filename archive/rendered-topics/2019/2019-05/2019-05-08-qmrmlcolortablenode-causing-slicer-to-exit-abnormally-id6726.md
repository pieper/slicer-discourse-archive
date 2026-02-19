---
topic_id: 6726
title: "Qmrmlcolortablenode Causing Slicer To Exit Abnormally"
date: 2019-05-08
url: https://discourse.slicer.org/t/6726
---

# qMRMLColorTableNode causing Slicer to exit abnormally

**Topic ID**: 6726
**Date**: 2019-05-08
**URL**: https://discourse.slicer.org/t/qmrmlcolortablenode-causing-slicer-to-exit-abnormally/6726

---

## Post #1 by @jamesobutler (2019-05-08 00:48 UTC)

<p>I have been having problems using qMRMLColorTableComboBox and I can’t seem to figure it out.  I’m using Slicer 4.10.1 and after creating the object and manipulating it as shown below, then upon closing the Slicer main window it will result in an exit abnormally message.  Am I manipulating this in an incorrect way?  Does an exit abnormally message usually indicate a specific issue with MRML widgets?</p>
<pre><code class="lang-python">class ColorTableTest():
  def __init__(self):
    self.combobox = slicer.qMRMLColorTableComboBox()
    self.combobox.setMRMLScene(slicer.mrmlScene)

class_instance = ColorTableTest()
class_instance.combobox.setCurrentNodeID("vtkMRMLColorTableNodeGrey")
</code></pre>
<pre><code class="lang-auto">Python console user input: class ColorTableTest():
Python console user input:   def __init__(self):
Python console user input:     self.combobox = slicer.qMRMLColorTableComboBox()
Python console user input:     self.combobox.setMRMLScene(slicer.mrmlScene)
Python console user input: class_instance = ColorTableTest()
This function is deprecated. Use currentNodeID() instead
qMRMLNodeFactory::baseName failed: class name vtkMRMLColorTableNode not found
This function is deprecated. Use currentNodeID() instead
qMRMLNodeFactory::baseName failed: class name vtkMRMLColorTableNode not found
qMRMLNodeFactory::baseName failed: class name vtkMRMLColorTableNode not found
This function is deprecated. Use currentNodeID() instead
This function is deprecated. Use currentNodeID() instead
qMRMLNodeFactory::baseName failed: class name vtkMRMLColorTableNode not found
This function is deprecated. Use currentNodeID() instead
qMRMLNodeFactory::baseName failed: class name vtkMRMLColorTableNode not found
qMRMLNodeFactory::baseName failed: class name vtkMRMLColorTableNode not found
This function is deprecated. Use currentNodeID() instead
This function is deprecated. Use currentNodeID() instead
qMRMLNodeFactory::baseName failed: class name vtkMRMLColorTableNode not found
This function is deprecated. Use currentNodeID() instead
qMRMLNodeFactory::baseName failed: class name vtkMRMLColorTableNode not found
qMRMLNodeFactory::baseName failed: class name vtkMRMLColorTableNode not found
This function is deprecated. Use currentNodeID() instead
Python console user input: class_instance.combobox.setCurrentNodeID("vtkMRMLColorTableNodeGrey")
Switch to module:  ""
Switch to module:  ""
error: [C:/S4.10R/Slicer-build/bin/Release/SlicerApp-real.exe] exit abnormally - Report the problem.
</code></pre>

---

## Post #2 by @lassoan (2019-05-08 01:19 UTC)

<p>It is due to trying to update a widget (triggered by removing of nodes) when the GUI of the application has been already partially destroyed. You should be able to fix this by destroying the combobox or at least set its scene to None when your module widget is destroyed.</p>
<p>To avoid the deprecation warnings, use <code>class_instance.combobox.currentNodeID = "vtkMRMLColorTableNodeGrey"</code> instead of <code>setCurrentNodeID()</code>.</p>

---

## Post #3 by @jamesobutler (2019-05-08 03:24 UTC)

<p>What’s the correct signal that I should be using?</p>
<p>Would I set it up as</p>
<pre><code class="lang-python">self.combobox.destroyed.connect( #method that clears scene or destroys object)
</code></pre>
<p>or is this too late and needs some signal before it gets destroyed?<br>
I’ve tried the above and it seems to still exit abnormally.</p>

---

## Post #4 by @lassoan (2019-05-08 04:39 UTC)

<p>Set scene to None in the destructor of the module widget class.</p>

---

## Post #5 by @jamesobutler (2019-05-08 14:22 UTC)

<p>In my test above adding the following seemed to prevent it from exiting abnormally (setting the scene to None was still causing exit abnormally with this test).</p>
<pre><code class="lang-python">class ColorTableTest():
  def __init__(self):
    self.combobox = slicer.qMRMLColorTableComboBox()
    self.combobox.setMRMLScene(slicer.mrmlScene)
  def __del__(self):
    self.combobox.delete()
</code></pre>
<p>However, in my real application, I’m still struggling to prevent the exit abnormally even with defining the destructor with this code in multiple areas too.  Would I need to build a Slicer debug version and connect to process to nail this down further?</p>
<p>I’m able to use <code>slicer.qSlicerScalarVolumeDisplayWidget()</code> which includes a qMRMLColorTableComboBox and doesn’t cause an exit abnormally.</p>
<p>I attempted to try making a qMRMLNodeComboBox into a qMRMLColorTableComboBox, but I was also struggling to get this working as well.</p>

---

## Post #6 by @lassoan (2019-05-08 15:45 UTC)

<p>Colors module logic destructor removes default color nodes from the scene. This happens very late and causes all these troubles. Color module should not pollute the scene with default color nodes anyway, so changing this should make the shutdown more robust. We’ve been planning to do this, but has not found a ND the time yet. It would be a backward-incompatible change, a good fit for current master branch, where we have many of those already.</p>
<p>To debug this, you certainly need a debug-mode build of Slicer.</p>

---

## Post #7 by @jcfr (2019-05-08 17:41 UTC)

<p>In scripted module, you could override the <code>cleanup</code> method of the widget.</p>
<p><a href="https://github.com/Slicer/Slicer/blob/10bf184d585f7526b8083043da671b0970043a16/Base/Python/slicer/ScriptedLoadableModule.py#L99-L106" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/10bf184d585f7526b8083043da671b0970043a16/Base/Python/slicer/ScriptedLoadableModule.py#L99-L106</a></p>
<blockquote>
<p>What’s the correct signal that I should be using?</p>
</blockquote>
<p>You could also directly observe the signal <code>qSlicerModuleManager::moduleAboutToBeUnloaded(QString)</code>, if module name being unloaded is <code>YourModuleName</code>, you would perform the cleanup and disconnect the signal.</p>

---

## Post #8 by @jamesobutler (2019-05-08 19:25 UTC)

<p>Thanks for the ideas!</p>
<p>I think I have found a solution that will work for my code.</p>
<p>Doing <code>slicer.app.aboutToQuit.connect(self.myCleanup)</code> appears to handle the <code>delete()</code> calls for the qMRMLColorTableComboBox widgets in an early enough time to prevent the exit abnormally.</p>

---
