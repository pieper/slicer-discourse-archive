# White sphere in center of 3d view

**Topic ID**: 9176
**Date**: 2019-11-16
**URL**: https://discourse.slicer.org/t/white-sphere-in-center-of-3d-view/9176

---

## Post #1 by @Amine (2019-11-16 07:48 UTC)

<p>slicer version 4.10.1 (issue only happens with slicelet)<br>
Hi, whenever i run this slicelet i get a white sphere at the center of the 3d view, it is small but interferes with small models, is there any way to get rid of it? (Ps: this issue is solved in nightly but i prefer keeping 4.10.1 for my project) , thanks for any inputs.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e48f8d9f04156f1d5dc793b7c2cde822ba08a904.png" alt="dot" data-base62-sha1="wBWqk7ZFlVPZLh56TlXrsASrVLS" width="480" height="386"></p>
<p>Slicelet :</p>
<pre><code>import qt
import __main__

mainWidget = qt.QWidget()
vlayout = qt.QVBoxLayout()
mainWidget.setLayout(vlayout)

layoutManager = slicer.qMRMLLayoutWidget()
layoutManager.setMRMLScene(slicer.mrmlScene)
 layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)
vlayout.addWidget(layoutManager)

mainWidget.show()

__main__.mainWidget = mainWidget
</code></pre>

---

## Post #2 by @lassoan (2019-11-16 14:39 UTC)

<p>We deliver fixes and improvements in preview releases and only fix selected high-priority issues in the latest stable release.</p>
<p>Since 4.10.1 is not the latest stable (that is 4.10.2), presence of a very small sphere is not a serious issue, we don’t plan to release a 4.10.x patch release, and the problem does not exist in latest preview release, it is unlikely that anyone could take the time to investigate this.</p>
<p>I would recommend to use latest stable or preview release.</p>

---
