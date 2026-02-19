---
topic_id: 16992
title: "Pythonqt Properties Shadowing Methods"
date: 2021-04-08
url: https://discourse.slicer.org/t/16992
---

# PythonQt properties shadowing methods

**Topic ID**: 16992
**Date**: 2021-04-08
**URL**: https://discourse.slicer.org/t/pythonqt-properties-shadowing-methods/16992

---

## Post #1 by @fbordignon (2021-04-08 01:38 UTC)

<p>Hi all, I’ve noticed a strange behavior that I could not understand if it is a bug or intended.<br>
It seems to me that a property can sometimes shadow methods from qt objects. Example:</p>
<blockquote>
<p>qgw = qt.QGraphicsWidget()</p>
</blockquote>
<p><code>qgw.layout</code> is None</p>
<blockquote>
<p>qgw.setLayout(qt.QGraphicsLayout())</p>
</blockquote>
<p>This runs ok with no errors, and even emit the signal <code>layoutChanged</code><br>
but <code>qgw.layout</code> continues to be None</p>
<p>if I try to</p>
<blockquote>
<p>qgw.layout = qt.QGraphicsLayout()</p>
</blockquote>
<p>I get an error:</p>
<pre><code>Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: Property 'layout' of type 'QGraphicsLayout*' does not accept an object of type QGraphicsLayout (QGraphicsLayout (C++ object at: 0x000002187FBE0B90))
</code></pre>
<p>Which I can understand, because setting an object to a pointer variable can only result in a error. But the layout() method is not accessible, which is also understandable from the python point of view.</p>
<p>That is not the case for QWidget, which I can access the layout via layout() slot. Can you help me to understand what is happening? I know it may be more related to PythonQt than Slicer, but I wanted to use QGraphicsWidget with another lib. Thanks</p>

---

## Post #2 by @lassoan (2021-04-08 16:02 UTC)

<p>For reference, discussions on github:</p>
<ul>
<li><a href="https://github.com/MeVisLab/pythonqt/issues/42" class="inline-onebox">Properties shadowing methods · Issue #42 · MeVisLab/pythonqt · GitHub</a></li>
<li><a href="https://github.com/pyqtgraph/pyqtgraph/issues/1699" class="inline-onebox">PythonQt support · Issue #1699 · pyqtgraph/pyqtgraph · GitHub</a></li>
</ul>
<p>There are hundreds of graphing libraries for Python. pyqtgraph may make sense if you already use the same Qt wrapping as it does, but otherwise bringing in an entire new set of Qt is probably not worth it.</p>

---

## Post #3 by @fbordignon (2021-04-08 16:48 UTC)

<p>Thanks Andras, your input is always greatly appreciated. We’ve managed to use matplotlib inside slicer to improve plotting capabilities, but we need a lib that allow us to plot things more dynamically and interactively. Also we have another project outside slicer that we built based on pyqtgraph that we would like to include into slicer.</p>
<p>I’ve managed to install PySide2 in Slicer and run pyqtgraph with it, but as expected the python wrapped qt objects are not compatible with pyqhtonqt wrapped ones. i.e. I cannot add a PySide2.QtCore.QWidget to a PythonQt.QtGui.QLayout. This way I can only use pyqtgraph as a separate window. A wrapper of some kind comes to mind to make pythonqt accept a pyside2 widget, but I don’t know how to start looking into it.</p>

---

## Post #4 by @pieper (2021-04-08 19:05 UTC)

<p>It sounds like you are into a potential dangerzone here by mixing PythonQt with PySide2, but if it’s working and matches your use case, I guess we can’t stop you ; )</p>
<p>If you just need a workaround, you should be able to get the pixel data from any of your widgets as numpy arrays that you can then display in the “other” qt.</p>
<p>For example in <a href="https://github.com/pieper/SlicerWeb/blob/master/WebServer/WebServer.py#L1310-L1314">SlicerWeb</a> I do:</p>
<pre><code class="lang-auto">    slicer.qMRMLUtils().qImageToVtkImageData(timeImage, vtkTimeImage)
</code></pre>
<p>then I get a numpy array from the vtkImageData.  It should be a very fast operation, even if it is a “creative” (hacky) workaround.</p>

---

## Post #5 by @fbordignon (2021-04-08 21:00 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a> that is a nice workaround to know as well.</p>
<p>I’ve come up with this other hack so far:</p>
<blockquote>
<p>from PySide2.QtWidgets import QVBoxLayout<br>
import shiboken2<br>
pysidelayout = shiboken2.wrapInstance(hash(self.layout), QVBoxLayout)<br>
import numpy as np<br>
from pyqtgraph.Qt import QtGui, QtCore<br>
import pyqtgraph as pg<br>
cw = pg.GraphicsLayoutWidget()<br>
pysidelayout.addWidget(cw)</p>
</blockquote>
<p>This way I can wrap a pythonqt qt object with shiboken and use it as it were a pyside2 object. Events are working, nicely and I got to add a pyside2 widget to a slicer layout. I will report if I find any issues, so far so good.</p>
<p>The other way around is still a mystery (pyside2 → pythonqt).</p>

---

## Post #6 by @fbordignon (2021-04-27 02:11 UTC)

<p>Reporting back on the hack of the post above. It works at first when creating and displaying a widget from pyside2. But when the parent widget gets destroyed, Slicer crashes. I’ve tried to remove my widget from the Slicer layout before the destruction of the PythonQt object with no success. I am guessing that the events are processed at the C++ level before getting passed to python for me to get a chance to remove the widget.</p>
<p>There are two options for me to go further with this madness:<br>
1 - Figure why some  functions are missing from PythonQt<br>
2 - Subclass QLayout in C++ for it not to take ownership of its widgets so that I can manage them from python. i.e. create widget with pyside, add to this unmanaged layout and destroy the widget myself via python when the layout is no more.</p>

---

## Post #7 by @fbordignon (2021-08-27 20:43 UTC)

<p>Hello everyone. Turns out the crashes were stackoverflows and I sort of fixed the issue with some checks on PythonQt. see <a href="https://github.com/commontk/PythonQt/pull/81" class="inline-onebox" rel="noopener nofollow ugc">ENH: added sanity checks for compatibility with pyqtgraph by fbordignon · Pull Request #81 · commontk/PythonQt · GitHub</a><br>
Now I have pretty plots with pyqtgraph 0.11.1:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/706386e7d36d8a5b4f8e9532adf2fc1d8c3eb228.png" data-download-href="/uploads/short-url/g2eI9Tfpc5ybWzDtYKPdMbZh4zS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/706386e7d36d8a5b4f8e9532adf2fc1d8c3eb228_2_517x279.png" alt="image" data-base62-sha1="g2eI9Tfpc5ybWzDtYKPdMbZh4zS" width="517" height="279" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/706386e7d36d8a5b4f8e9532adf2fc1d8c3eb228_2_517x279.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/706386e7d36d8a5b4f8e9532adf2fc1d8c3eb228_2_775x418.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/706386e7d36d8a5b4f8e9532adf2fc1d8c3eb228_2_1034x558.png 2x" data-dominant-color="262524"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1900×1026 69.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @pieper (2021-08-27 22:33 UTC)

<p>Hey, that’s nice! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>
<p>Will you have sample code for people to try?</p>

---

## Post #9 by @fbordignon (2021-08-30 13:14 UTC)

<p>For this example, the user needs to have the <a href="https://github.com/Slicer/Slicer/pull/5822" rel="noopener nofollow ugc">python3.dll fix</a>, alternatively one can temporarily <a href="https://sourceforge.net/projects/winpython/files/WinPython_3.6/3.6.7.0/WinPython64-3.6.7.0Zero.exe/download" rel="noopener nofollow ugc">download and install WinPython 3.6.7</a> and copy python3.dll from <code>winpython/python-3.6.7.amd64/python3.dll</code> to <code>Slicer/bin/python3.dll</code><br>
Slicer can crash if one does not have PythonQt compiled with <a href="https://github.com/commontk/PythonQt/pull/81" rel="noopener nofollow ugc">this fix</a>. It works without it, but Slicer can become unstable.</p>
<p>Working example based on <a href="https://github.com/pyqtgraph/pyqtgraph/blob/master/examples/Plotting.py" rel="noopener nofollow ugc">plotting example of pyqtgraph</a>:</p>
<pre><code class="lang-python"># Copy and paste this on Slicer's python terminal
pip_install('pyside2==5.15.1') # must be important to match pyside2 version to slicer's qt version
pip_install('pyqtgraph')

import textwrap
from PySide2.QtWidgets import QVBoxLayout
import shiboken2
import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

# Custom layout base class
class BaseLayout:
    TAG = "EmptyScreen"
    UID = 1010
    LAYOUT = textwrap.dedent(
        f"""
        &lt;layout type="vertical"&gt;
            &lt;item&gt;
                &lt;{TAG}&gt;&lt;/{TAG}&gt;
            &lt;/item&gt;
        &lt;/layout&gt;
    """
    )
    @classmethod
    def register(cls):
        viewFactory = slicer.qSlicerSingletonViewFactory()
        viewFactory.setTagName(cls.TAG)
        if slicer.app.layoutManager() is not None:
            slicer.app.layoutManager().registerViewFactory(viewFactory)
        container = cls.build(viewFactory)
        layoutManager = slicer.app.layoutManager()
        layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(cls.UID, cls.LAYOUT)
        return container
    @classmethod
    def build(cls, factory):
        viewWidget = qt.QWidget()
        viewWidget.setAutoFillBackground(True)
        factory.setWidget(viewWidget)
        viewLayout = qt.QVBoxLayout()
        viewWidget.setLayout(viewLayout)
        return viewWidget
    @classmethod
    def show(cls):
        slicer.app.layoutManager().setLayout(cls.UID)

#my plot layout class
class PlotLayout(BaseLayout):
    TAG = "MyPlotWidget"
    UID = 1019
    LAYOUT = textwrap.dedent(f"""
        &lt;layout type="vertical"&gt;
            &lt;item&gt;
                &lt;{TAG}&gt;&lt;/{TAG}&gt;
            &lt;/item&gt;
        &lt;/layout&gt;
    """)

lw = PlotLayout.register().layout()
PlotLayout.show()

# wrap pythonQt instance with shiboken2 (pyside2)
pysidelayout = shiboken2.wrapInstance(hash(lw), QVBoxLayout)

pg.mkQApp()

# start of pyqtgraph plotting example https://github.com/pyqtgraph/pyqtgraph/blob/master/examples/Plotting.py
win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
pysidelayout.addWidget(win)

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

p1 = win.addPlot(title="Basic array plotting", y=np.random.normal(size=100))

p2 = win.addPlot(title="Multiple curves")
p2.plot(np.random.normal(size=100), pen=(255,0,0), name="Red curve")
p2.plot(np.random.normal(size=110)+5, pen=(0,255,0), name="Green curve")
p2.plot(np.random.normal(size=120)+10, pen=(0,0,255), name="Blue curve")

p3 = win.addPlot(title="Drawing with points")
p3.plot(np.random.normal(size=100), pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')

win.nextRow()

p4 = win.addPlot(title="Parametric, grid enabled")
x = np.cos(np.linspace(0, 2*np.pi, 1000))
y = np.sin(np.linspace(0, 4*np.pi, 1000))
p4.plot(x, y)
p4.showGrid(x=True, y=True)

p5 = win.addPlot(title="Scatter plot, axis labels, log scale")
x = np.random.normal(size=1000) * 1e-5
y = x*1000 + 0.005 * np.random.normal(size=1000)
y -= y.min()-1.0
mask = x &gt; 1e-15
x = x[mask]
y = y[mask]
p5.plot(x, y, pen=None, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 50))
p5.setLabel('left', "Y Axis", units='A')
p5.setLabel('bottom', "Y Axis", units='s')
p5.setLogMode(x=True, y=False)

p6 = win.addPlot(title="Updating plot")
curve = p6.plot(pen='y')
data = np.random.normal(size=(10,1000))
ptr = 0

def update():
    global curve, data, ptr, p6
    curve.setData(data[ptr%10])
    if ptr == 0:
        p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
    ptr += 1

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)


win.nextRow()

p7 = win.addPlot(title="Filled plot, axis disabled")
y = np.sin(np.linspace(0, 10, 1000)) + np.random.normal(size=1000, scale=0.1)
p7.plot(y, fillLevel=-0.3, brush=(50,50,200,100))
p7.showAxis('bottom', False)


x2 = np.linspace(-100, 100, 1000)
data2 = np.sin(x2) / x2
p8 = win.addPlot(title="Region Selection")
p8.plot(data2, pen=(255,255,255,200))
lr = pg.LinearRegionItem([400,700])
lr.setZValue(-10)
p8.addItem(lr)

p9 = win.addPlot(title="Zoom on selected region")
p9.plot(data2)

def updatePlot():
    p9.setXRange(*lr.getRegion(), padding=0)

def updateRegion():
    lr.setRegion(p9.getViewBox().viewRange()[0])

lr.sigRegionChanged.connect(updatePlot)
p9.sigXRangeChanged.connect(updateRegion)
updatePlot()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a402884270034660f227ec6aa37fcca44ae5c5b8.png" data-download-href="/uploads/short-url/noTJi3uriYdM9gu4H7406ELkZRu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a402884270034660f227ec6aa37fcca44ae5c5b8_2_690x401.png" alt="image" data-base62-sha1="noTJi3uriYdM9gu4H7406ELkZRu" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a402884270034660f227ec6aa37fcca44ae5c5b8_2_690x401.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a402884270034660f227ec6aa37fcca44ae5c5b8_2_1035x601.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a402884270034660f227ec6aa37fcca44ae5c5b8_2_1380x802.png 2x" data-dominant-color="202020"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1858×1080 370 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @pieper (2021-08-30 14:20 UTC)

<p>Wow, that’s very cool <img src="https://emoji.discourse-cdn.com/twitter/eyes.png?v=10" title=":eyes:" class="emoji" alt=":eyes:"></p>
<p>Do you think this is a stable setup?  It looks like all the events and timers work and there are no other special hacks?  If so that would allow people to mix other PySide2 based code in Slicer (e.g. <a href="https://www.pythonguis.com/widgets/">these widgets</a>) or share widgets with <a>napari</a>.</p>

---

## Post #11 by @fbordignon (2021-08-30 16:40 UTC)

<p>Hey <a class="mention" href="/u/pieper">@pieper</a> thanks. We are gonna try to use code we have from another proprietary Pyside2 project inside Slicer in production, hoping that it is stable enough. I will report if we find issues.</p>
<p>I was surprised by the compatibility, TBH I was expecting more of a struggle. But it seems that PythonQt and pyside2/shiboken2 are built with the assumption that objects can be created by C++ and/or Python so they need to keep references updated, i.e. if pyside2 creates objects and adds a child to a PythonQt object, it is more or less like C++ is adding it. Note that this is an impression based on things working and a comprehension of the code tending to zero.</p>
<p>I expect a bit more work now to keep track of the ownership of the objects. Anyways, maybe we can start a new thread to test this.</p>

---

## Post #12 by @pieper (2021-08-30 18:27 UTC)

<p>Very nice - I hope it works well in your project!  I agree with your logic so, fingers crossed, it should hold up in practice.</p>

---

## Post #13 by @fbordignon (2022-06-24 14:10 UTC)

<p>Hi, I am using this fix for 10 months now. We’ve released 4 stable versions of our custom app to final users without any problems reported regarding this issue. I figure because it is a simple solution, we could merge it and see if someone else is interested. Thanks.</p>

---

## Post #14 by @fbordignon (2025-04-22 15:59 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> FUP to the weekly dev meeting. This was not integrated into pythonqt <a href="https://github.com/MeVisLab/pythonqt/pull/72" class="inline-onebox" rel="noopener nofollow ugc">ENH: checks to prevent infinite recursion by fbordignon · Pull Request #72 · MeVisLab/pythonqt · GitHub</a><br>
I don’t know how to respond. I see that the checks may be causing some overhead but I don’t know if it is degrading performance, probably not.<br>
It is likely that the wrapping is what is causing the problem:</p>
<pre><code class="lang-auto">pysidelayout = shiboken2.wrapInstance(hash(lw), QVBoxLayout)
</code></pre>
<p>Maybe explicitly setting the parent of the layout can workaround the problem. It has been some time that I have looked into it.</p>

---

## Post #15 by @fbordignon (2025-04-22 16:02 UTC)

<p>Well, I’ve tested on Slicer 5.8 now and the example above is working just changing pyside2 to 5.15.2! See: <a href="https://youtu.be/ehle4uiHByw" rel="noopener nofollow ugc">https://youtu.be/ehle4uiHByw</a></p>
<pre data-code-wrap="python"><code class="lang-python"># Copy and paste this on Slicer's python terminal
pip_install('pyside2==5.15.2') # must be important to match pyside2 version to slicer's qt version
pip_install('pyqtgraph')

import textwrap
from PySide2.QtWidgets import QVBoxLayout
import shiboken2
import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

# Custom layout base class
class BaseLayout:
    TAG = "EmptyScreen"
    UID = 1010
    LAYOUT = textwrap.dedent(
        f"""
        &lt;layout type="vertical"&gt;
            &lt;item&gt;
                &lt;{TAG}&gt;&lt;/{TAG}&gt;
            &lt;/item&gt;
        &lt;/layout&gt;
    """
    )
    @classmethod
    def register(cls):
        viewFactory = slicer.qSlicerSingletonViewFactory()
        viewFactory.setTagName(cls.TAG)
        if slicer.app.layoutManager() is not None:
            slicer.app.layoutManager().registerViewFactory(viewFactory)
        container = cls.build(viewFactory)
        layoutManager = slicer.app.layoutManager()
        layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(cls.UID, cls.LAYOUT)
        return container
    @classmethod
    def build(cls, factory):
        viewWidget = qt.QWidget()
        viewWidget.setAutoFillBackground(True)
        factory.setWidget(viewWidget)
        viewLayout = qt.QVBoxLayout()
        viewWidget.setLayout(viewLayout)
        return viewWidget
    @classmethod
    def show(cls):
        slicer.app.layoutManager().setLayout(cls.UID)

#my plot layout class
class PlotLayout(BaseLayout):
    TAG = "MyPlotWidget"
    UID = 1019
    LAYOUT = textwrap.dedent(f"""
        &lt;layout type="vertical"&gt;
            &lt;item&gt;
                &lt;{TAG}&gt;&lt;/{TAG}&gt;
            &lt;/item&gt;
        &lt;/layout&gt;
    """)

lw = PlotLayout.register().layout()
PlotLayout.show()

# wrap pythonQt instance with shiboken2 (pyside2)
pysidelayout = shiboken2.wrapInstance(hash(lw), QVBoxLayout)

pg.mkQApp()

# start of pyqtgraph plotting example https://github.com/pyqtgraph/pyqtgraph/blob/master/examples/Plotting.py
win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
pysidelayout.addWidget(win)

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

p1 = win.addPlot(title="Basic array plotting", y=np.random.normal(size=100))

p2 = win.addPlot(title="Multiple curves")
p2.plot(np.random.normal(size=100), pen=(255,0,0), name="Red curve")
p2.plot(np.random.normal(size=110)+5, pen=(0,255,0), name="Green curve")
p2.plot(np.random.normal(size=120)+10, pen=(0,0,255), name="Blue curve")

p3 = win.addPlot(title="Drawing with points")
p3.plot(np.random.normal(size=100), pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')

win.nextRow()

p4 = win.addPlot(title="Parametric, grid enabled")
x = np.cos(np.linspace(0, 2*np.pi, 1000))
y = np.sin(np.linspace(0, 4*np.pi, 1000))
p4.plot(x, y)
p4.showGrid(x=True, y=True)

p5 = win.addPlot(title="Scatter plot, axis labels, log scale")
x = np.random.normal(size=1000) * 1e-5
y = x*1000 + 0.005 * np.random.normal(size=1000)
y -= y.min()-1.0
mask = x &gt; 1e-15
x = x[mask]
y = y[mask]
p5.plot(x, y, pen=None, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 50))
p5.setLabel('left', "Y Axis", units='A')
p5.setLabel('bottom', "Y Axis", units='s')
p5.setLogMode(x=True, y=False)

p6 = win.addPlot(title="Updating plot")
curve = p6.plot(pen='y')
data = np.random.normal(size=(10,1000))
ptr = 0

def update():
    global curve, data, ptr, p6
    curve.setData(data[ptr%10])
    if ptr == 0:
        p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
    ptr += 1

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)


win.nextRow()

p7 = win.addPlot(title="Filled plot, axis disabled")
y = np.sin(np.linspace(0, 10, 1000)) + np.random.normal(size=1000, scale=0.1)
p7.plot(y, fillLevel=-0.3, brush=(50,50,200,100))
p7.showAxis('bottom', False)


x2 = np.linspace(-100, 100, 1000)
data2 = np.sin(x2) / x2
p8 = win.addPlot(title="Region Selection")
p8.plot(data2, pen=(255,255,255,200))
lr = pg.LinearRegionItem([400,700])
lr.setZValue(-10)
p8.addItem(lr)

p9 = win.addPlot(title="Zoom on selected region")
p9.plot(data2)

def updatePlot():
    p9.setXRange(*lr.getRegion(), padding=0)

def updateRegion():
    lr.setRegion(p9.getViewBox().viewRange()[0])

lr.sigRegionChanged.connect(updatePlot)
p9.sigXRangeChanged.connect(updateRegion)
updatePlot()
</code></pre>

---

## Post #16 by @pieper (2025-04-22 21:24 UTC)

<p>Alas, that crashed for me on mac with 5.8.1.  The Qt version is 5.15.8, so I tried switching to that but it turns out there’s no pyside2 for that.</p>

---
