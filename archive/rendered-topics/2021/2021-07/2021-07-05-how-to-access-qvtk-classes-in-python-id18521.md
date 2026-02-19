---
topic_id: 18521
title: "How To Access Qvtk Classes In Python"
date: 2021-07-05
url: https://discourse.slicer.org/t/18521
---

# How to access QVTK... classes in Python

**Topic ID**: 18521
**Date**: 2021-07-05
**URL**: https://discourse.slicer.org/t/how-to-access-qvtk-classes-in-python/18521

---

## Post #1 by @MarineC (2021-07-05 15:41 UTC)

<p>Hi everyone !</p>
<p>I need to use a VTK function called QVTKOpenGLStereoWidget in Python.<br>
I saw a vtk example where they did this way :</p>
<pre><code class="lang-auto">from PyQt4 import QtGui
from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
</code></pre>
<p>And then use it like this :</p>
<pre><code class="lang-auto">class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.frame = QtGui.QFrame()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
</code></pre>
<p>However, after looking at some topics, it seems Slicer uses PythonQt and not PyQt.<br>
So in order to access my class, can I just remplace PyQt4 to PythonQt and qt4 with qt5, or do I need to do differently ?</p>
<p>Thanks for the help !</p>
<p>Marine</p>

---

## Post #2 by @cpinter (2021-07-06 14:16 UTC)

<p>Normally you can access any VTK class in the main <code>vtk</code> module. Like <code>vtk.vtkCollection()</code>. However, this particular module seems not to be Python wrapped. I’d use the <code>vtkQWidgetWidget</code> class from the same module but also could not figure out how, so I added a C++ function using it directly that I then call form Python.</p>

---

## Post #3 by @MarineC (2021-07-06 15:00 UTC)

<p>OK thanks for the infos I’ll do that ! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
