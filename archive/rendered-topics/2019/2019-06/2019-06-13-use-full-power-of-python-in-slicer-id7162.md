# Use full power of Python in Slicer

**Topic ID**: 7162
**Date**: 2019-06-13
**URL**: https://discourse.slicer.org/t/use-full-power-of-python-in-slicer/7162

---

## Post #1 by @lassoan (2019-06-13 16:23 UTC)

<p>Until recently, Slicer used a custom Python build that was not binary compatible with third-party Python packages. Now, in latest Slicer Preview release, any Python packages can be installed and used in Slicer (except those that in direct conflict with version of libraries that are bundled with Slicer).</p>
<p>Example: do curve fitting using scipy</p>
<ol>
<li>Install scipy by typing in Slicer’s Python console:</li>
</ol>
<p><code>pip_install('scipy')</code></p>
<ol start="2">
<li>Try a simple curve fitting example:</li>
</ol>
<pre><code class="lang-auto">import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# Define the data to be fit with some noise:
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise

# Fit for the parameters a, b, c of the function func:
popt, pcov = curve_fit(func, xdata, ydata)

# Plot results
plotNodes = {}
plot([xdata, ydata, func(xdata, *popt)], xColumnIndex = 0, nodes = plotNodes)
plotNodes['chart'].SetTitle('Curve fit demo')
plotNodes['series'][0].SetName('noisy')
plotNodes['series'][1].SetName('fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c91195b3027899cfb491615286b5e90e864d816.png" data-download-href="/uploads/short-url/k3vIAmU4o9k0SBrLNkUFnBsBuCO.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c91195b3027899cfb491615286b5e90e864d816_2_690x475.png" alt="image" data-base62-sha1="k3vIAmU4o9k0SBrLNkUFnBsBuCO" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c91195b3027899cfb491615286b5e90e864d816_2_690x475.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c91195b3027899cfb491615286b5e90e864d816_2_1035x712.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c91195b3027899cfb491615286b5e90e864d816.png 2x" data-dominant-color="F3F5F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1205×830 73 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This feature will be heavily utilized in the upcoming <a href="http://www.slicerigt.org/wp/cars-2019-tutorial/">Slicer tutorial “Deep learning and computer vision for real-time procedure annotation”</a> at CARS conference next week, where tensorflow, keras, scikit-learn pacakges are used in Slicer for classification of images streamed in real-time.</p>
<p>Any questions, comments, suggestions are welcome.</p>

---

## Post #2 by @Alex_Vergara (2019-06-14 10:08 UTC)

<p>It would be really nice if you allow plotly, matplotlib, (whatever), graphs to be displayed and saved inside a plot Node (Feature request?)</p>

---

## Post #3 by @lassoan (2019-06-14 18:07 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="2" data-topic="7162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>It would be really nice if you allow plotly, matplotlib, (whatever), graphs to be displayed and saved inside a plot Node</p>
</blockquote>
</aside>
<p>There are hundreds of plotting libraries in Python, they offer amazing amount of functionality but at the same time this entire area in Python is a huge mess. I would not venture into choosing a handful of them and trying to make them integrate into Slicer’s GUI. There can be some implementation difficulties, too, as these packages often include interactive GUI components that may conflict with Slicer’s GUI components. For example, matplotlib’s Qt GUI is probably incompatible with Slicer’s Qt version (it should still be possible to use matplotlib’s "agg’ backend and display the plot as a rendered image).</p>
<p>For now, I would keep relying on Slicer’s very sophisticated 2D and 3D visualization capabilities and somewhat less sophisticated interactive 2D plotting (which is very fast and directly can visualize plots from Slicer’s VTK-based data storage objects). We could improve plotting API in Slicer to make it a bit more user friendly (<code>slicer.util.plot()</code> is an attempt towards that - see the example above).</p>
<p>If somebody wanted to experiment with third-party plotting then that would be great. It would be interesting to learn about the experiences. If results are very promising then maybe some helper/adapter functions could be added to Slicer that would help using some plotting packages.</p>

---

## Post #4 by @ungi (2019-06-15 02:07 UTC)

<p>Matplotlib doesn’t work in Slicer, not even with ‘agg’ backend. I’ve just tried it today. But I agree with Andras, it would be impossible to choose which Python GUI tools to support in Slicer. A convenient workaround is to save data (e.g. numpy.save) and load it (e.g. numpy.load) in a standard Jupyter notebook that has visualization scripts with Matplotlib, etc.</p>

---

## Post #5 by @lassoan (2019-06-15 04:48 UTC)

<p>I’ve just tried interactive plotting using matplotlib and it works fine for me on Windows. I just had to switch to WXAgg backend.</p>
<p>Setup:</p>
<pre><code class="lang-python">pip_install("matplotlib wxPython")
</code></pre>
<p>Example interactive plot using matplotlib:</p>
<pre><code class="lang-python"># Get a volume from SampleData and compute its histogram
import SampleData
import numpy as np
volumeNode = SampleData.SampleDataLogic().downloadMRHead()
histogram = np.histogram(arrayFromVolume(volumeNode), bins=50)

# Set matplotlib to use WXAgg backend
import matplotlib
matplotlib.use('WXAgg')

# Show a plot using matplotlib
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(histogram[1][1:], histogram[0].astype(float))
ax.grid(True)
ax.set_ylim((0, 4e5))
plt.show(block=False)
</code></pre>
<p>For reference, to create a similar plot using Slicer’s plotting infrastructure:</p>
<pre><code class="lang-python">chartNode = plot(histogram, xColumnIndex = 1)
chartNode.SetYAxisRangeAuto(False)
chartNode.SetYAxisRange(0, 4e5)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7e295728729990f9c3c1e841f573c16b01d2e26.png" data-download-href="/uploads/short-url/uNO6NvyJAwv5O8KUKO1qUI1YCAC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d7e295728729990f9c3c1e841f573c16b01d2e26_2_690x438.png" alt="image" data-base62-sha1="uNO6NvyJAwv5O8KUKO1qUI1YCAC" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d7e295728729990f9c3c1e841f573c16b01d2e26_2_690x438.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d7e295728729990f9c3c1e841f573c16b01d2e26_2_1035x657.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d7e295728729990f9c3c1e841f573c16b01d2e26_2_1380x876.png 2x" data-dominant-color="CCCDCC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1434 599 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @ungi (2019-06-15 05:04 UTC)

<p>Thanks! This is good to know. Especially in Slicer Jupyter notebooks. When batch processing lots of data in Slicer in Jupyter notebooks, it will be good that the notebooks can archive matplotlib graphs to report on results!<br>
For single graphs like in your example, I agree that Slicer plots are much more practical to use.</p>

---

## Post #7 by @pieper (2019-06-15 17:00 UTC)

<p>FWIW, unfortunately on mac with today’s nightly the pip install works and reports no errors, but when running the example script it crashes with the trace pasted below.</p>
<pre><code class="lang-auto">Thread 0 Crashed:: Dispatch queue: com.apple.main-thread
0   libpython3.6m.dylib           	0x000000010624b134 PyUnicode_InternInPlace + 116
1   libpython3.6m.dylib           	0x000000010626c3cc PyUnicode_InternFromString + 60
2   libpython3.6m.dylib           	0x000000010621eaa0 PyObject_GetAttrString + 48
3   libpython3.6m.dylib           	0x00000001061dd088 PyObject_CallMethod + 120
4   libCTKScriptingPythonWidgets.0.1.dylib	0x00000001016f0ed0 ctkPythonConsolePrivate::push(QString const&amp;) + 144
5   libCTKScriptingPythonWidgets.0.1.dylib	0x00000001016f1f22 ctkPythonConsole::executeCommand(QString const&amp;) + 18
6   libCTKWidgets.0.1.dylib       	0x0000000101722243 ctkConsolePrivate::internalExecuteCommand() + 563
7   libCTKWidgets.0.1.dylib       	0x0000000101721aa8 ctkConsolePrivate::keyPressEvent(QKeyEvent*) + 2120
8   org.qt-project.QtWidgets      	0x0000000106d7ec90 QWidget::event(QEvent*) + 5104
9   org.qt-project.QtWidgets      	0x0000000106e31c8d QFrame::event(QEvent*) + 45
10  org.qt-project.QtWidgets      	0x0000000106e3b78c QAbstractScrollArea::event(QEvent*) + 364
11  org.qt-project.QtWidgets      	0x0000000106f22127 QTextEdit::event(QEvent*) + 407
12  org.qt-project.QtWidgets      	0x0000000106d458cd QApplicationPrivate::notify_helper(QObject*, QEvent*) + 301
13  org.qt-project.QtWidgets      	0x0000000106d46ddd QApplication::notify(QObject*, QEvent*) + 797
14  libqSlicerBaseQTGUI.dylib     	0x00000001010bf3d6 qSlicerApplication::notify(QObject*, QEvent*) + 22
15  org.qt-project.QtCore         	0x000000010d9d9c84 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 164
16  org.qt-project.QtWidgets      	0x0000000106d9daf7 0x106d35000 + 428791
17  org.qt-project.QtWidgets      	0x0000000106d458cd QApplicationPrivate::notify_helper(QObject*, QEvent*) + 301
18  org.qt-project.QtWidgets      	0x0000000106d46c47 QApplication::notify(QObject*, QEvent*) + 391
19  libqSlicerBaseQTGUI.dylib     	0x00000001010bf3d6 qSlicerApplication::notify(QObject*, QEvent*) + 22
20  org.qt-project.QtCore         	0x000000010d9d9c84 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 164
21  org.qt-project.QtGui          	0x000000010d2fa2ee QGuiApplicationPrivate::processKeyEvent(QWindowSystemInterfacePrivate::KeyEvent*) + 174
22  org.qt-project.QtGui          	0x000000010d2e095b QWindowSystemInterface::sendWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 155
23  org.qt-project.QtGui          	0x000000010d2dc3bc QWindowSystemInterface::flushWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 572
24  libqcocoa.dylib               	0x0000000116f63aa3 0x116f41000 + 141987
25  libqcocoa.dylib               	0x0000000116f63be8 0x116f41000 + 142312
26  com.apple.AppKit              	0x00007fff4b533b9f -[NSWindow(NSEventRouting) _reallySendEvent:isDelayedEvent:] + 6840
27  com.apple.AppKit              	0x00007fff4b531e9f -[NSWindow(NSEventRouting) sendEvent:] + 478
28  libqcocoa.dylib               	0x0000000116f68217 0x116f41000 + 160279
29  com.apple.AppKit              	0x00007fff4b3d2101 -[NSApplication(NSEvent) sendEvent:] + 2953
30  libqcocoa.dylib               	0x0000000116f6e669 0x116f41000 + 185961
31  com.apple.AppKit              	0x00007fff4b3bfee8 -[NSApplication run] + 755
32  libwx_osx_cocoau_core-3.0.0.4.0.dylib	0x000000012bf72edf wxApp::CallOnInit() + 143
33  _core.cpython-36m-darwin.so   	0x000000012b417724 wxPyApp::_BootstrapApp() + 532
34  _core.cpython-36m-darwin.so   	0x000000012b41b604 meth_wxPyApp__BootstrapApp(_object*, _object*) + 100
35  libpython3.6m.dylib           	0x000000010621c00c _PyCFunction_FastCallDict + 172
36  libpython3.6m.dylib           	0x000000010629ac0f call_function + 479
37  libpython3.6m.dylib           	0x0000000106297632 _PyEval_EvalFrameDefault + 25826
38  libpython3.6m.dylib           	0x000000010629bb19 _PyEval_EvalCodeWithName + 3641
39  libpython3.6m.dylib           	0x000000010629c652 _PyFunction_FastCallDict + 802
40  libpython3.6m.dylib           	0x00000001061dc8a8 _PyObject_FastCallDict + 360
41  libpython3.6m.dylib           	0x00000001061dc9c5 _PyObject_Call_Prepend + 149
42  libpython3.6m.dylib           	0x00000001061dc5f6 PyObject_Call + 102
43  libpython3.6m.dylib           	0x0000000106233d7e slot_tp_init + 158
44  libpython3.6m.dylib           	0x000000010622feb9 type_call + 313
45  libpython3.6m.dylib           	0x00000001061dc875 _PyObject_FastCallDict + 309
46  libpython3.6m.dylib           	0x000000010629ab09 call_function + 217
47  libpython3.6m.dylib           	0x0000000106297632 _PyEval_EvalFrameDefault + 25826
48  libpython3.6m.dylib           	0x000000010629bb19 _PyEval_EvalCodeWithName + 3641
49  libpython3.6m.dylib           	0x000000010629c652 _PyFunction_FastCallDict + 802
50  libpython3.6m.dylib           	0x00000001061dc8a8 _PyObject_FastCallDict + 360
51  libpython3.6m.dylib           	0x00000001061dc9c5 _PyObject_Call_Prepend + 149
52  libpython3.6m.dylib           	0x00000001061dc5f6 PyObject_Call + 102
53  libpython3.6m.dylib           	0x0000000106297933 _PyEval_EvalFrameDefault + 26595
54  libpython3.6m.dylib           	0x000000010629bb19 _PyEval_EvalCodeWithName + 3641
55  libpython3.6m.dylib           	0x00000001062910fb PyEval_EvalCodeEx + 107
56  libpython3.6m.dylib           	0x000000010620233d function_call + 381
57  libpython3.6m.dylib           	0x00000001061dc5f6 PyObject_Call + 102
58  libpython3.6m.dylib           	0x0000000106297933 _PyEval_EvalFrameDefault + 26595
59  libpython3.6m.dylib           	0x000000010629bb19 _PyEval_EvalCodeWithName + 3641
60  libpython3.6m.dylib           	0x000000010629c316 fast_function + 742
61  libpython3.6m.dylib           	0x000000010629abe9 call_function + 441
62  libpython3.6m.dylib           	0x0000000106297632 _PyEval_EvalFrameDefault + 25826
63  libpython3.6m.dylib           	0x000000010629bb19 _PyEval_EvalCodeWithName + 3641
64  libpython3.6m.dylib           	0x0000000106291084 PyEval_EvalCode + 100
65  libpython3.6m.dylib           	0x000000010628e7e0 builtin_exec + 528
66  libpython3.6m.dylib           	0x000000010621c00c _PyCFunction_FastCallDict + 172
67  libpython3.6m.dylib           	0x000000010629ac0f call_function + 479
68  libpython3.6m.dylib           	0x0000000106297632 _PyEval_EvalFrameDefault + 25826
69  libpython3.6m.dylib           	0x000000010629c26e fast_function + 574
70  libpython3.6m.dylib           	0x000000010629abe9 call_function + 441
71  libpython3.6m.dylib           	0x0000000106297632 _PyEval_EvalFrameDefault + 25826
72  libpython3.6m.dylib           	0x000000010629bb19 _PyEval_EvalCodeWithName + 3641
73  libpython3.6m.dylib           	0x000000010629c316 fast_function + 742
74  libpython3.6m.dylib           	0x000000010629abe9 call_function + 441
75  libpython3.6m.dylib           	0x0000000106297632 _PyEval_EvalFrameDefault + 25826
76  libpython3.6m.dylib           	0x000000010629c6ec _PyFunction_FastCallDict + 956
77  libpython3.6m.dylib           	0x00000001061dc8a8 _PyObject_FastCallDict + 360
78  libpython3.6m.dylib           	0x00000001061dc9c5 _PyObject_Call_Prepend + 149
79  libpython3.6m.dylib           	0x00000001061dc875 _PyObject_FastCallDict + 309
80  libpython3.6m.dylib           	0x00000001061dd1d4 callmethod + 180
81  libpython3.6m.dylib           	0x00000001061dd0c4 PyObject_CallMethod + 180
82  libCTKScriptingPythonWidgets.0.1.dylib	0x00000001016f0ed0 ctkPythonConsolePrivate::push(QString const&amp;) + 144
83  libCTKScriptingPythonWidgets.0.1.dylib	0x00000001016f1f22 ctkPythonConsole::executeCommand(QString const&amp;) + 18
84  libCTKWidgets.0.1.dylib       	0x0000000101722243 ctkConsolePrivate::internalExecuteCommand() + 563
85  libCTKWidgets.0.1.dylib       	0x0000000101724afb ctkConsolePrivate::pasteText(QString const&amp;) + 459
86  libCTKWidgets.0.1.dylib       	0x0000000101724893 ctkConsolePrivate::insertFromMimeData(QMimeData const*) + 115
87  libCTKWidgets.0.1.dylib       	0x00000001017213b9 ctkConsolePrivate::keyPressEvent(QKeyEvent*) + 345
88  org.qt-project.QtWidgets      	0x0000000106d7ec90 QWidget::event(QEvent*) + 5104
89  org.qt-project.QtWidgets      	0x0000000106e31c8d QFrame::event(QEvent*) + 45
90  org.qt-project.QtWidgets      	0x0000000106e3b78c QAbstractScrollArea::event(QEvent*) + 364
91  org.qt-project.QtWidgets      	0x0000000106f22127 QTextEdit::event(QEvent*) + 407
92  org.qt-project.QtWidgets      	0x0000000106d458cd QApplicationPrivate::notify_helper(QObject*, QEvent*) + 301
93  org.qt-project.QtWidgets      	0x0000000106d46ddd QApplication::notify(QObject*, QEvent*) + 797
94  libqSlicerBaseQTGUI.dylib     	0x00000001010bf3d6 qSlicerApplication::notify(QObject*, QEvent*) + 22
95  org.qt-project.QtCore         	0x000000010d9d9c84 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 164
96  org.qt-project.QtWidgets      	0x0000000106d9daf7 0x106d35000 + 428791
97  org.qt-project.QtWidgets      	0x0000000106d458cd QApplicationPrivate::notify_helper(QObject*, QEvent*) + 301
98  org.qt-project.QtWidgets      	0x0000000106d46c47 QApplication::notify(QObject*, QEvent*) + 391
99  libqSlicerBaseQTGUI.dylib     	0x00000001010bf3d6 qSlicerApplication::notify(QObject*, QEvent*) + 22
100 org.qt-project.QtCore         	0x000000010d9d9c84 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 164
101 org.qt-project.QtGui          	0x000000010d2fa2ee QGuiApplicationPrivate::processKeyEvent(QWindowSystemInterfacePrivate::KeyEvent*) + 174
102 org.qt-project.QtGui          	0x000000010d2e095b QWindowSystemInterface::sendWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 155
103 org.qt-project.QtGui          	0x000000010d2dc3bc QWindowSystemInterface::flushWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 572
104 libqcocoa.dylib               	0x0000000116f63aa3 0x116f41000 + 141987
105 libqcocoa.dylib               	0x0000000116f63be8 0x116f41000 + 142312
106 com.apple.AppKit              	0x00007fff4b533b9f -[NSWindow(NSEventRouting) _reallySendEvent:isDelayedEvent:] + 6840
107 com.apple.AppKit              	0x00007fff4b531e9f -[NSWindow(NSEventRouting) sendEvent:] + 478
108 libqcocoa.dylib               	0x0000000116f68217 0x116f41000 + 160279
109 libqcocoa.dylib               	0x0000000116f6f1d0 0x116f41000 + 188880
110 com.apple.AppKit              	0x00007fff4b713f99 -[NSMenu _performKeyEquivalentWithDelegate:] + 142
111 com.apple.AppKit              	0x00007fff4b714169 -[NSMenu _performKeyEquivalentWithDelegate:] + 606
112 com.apple.AppKit              	0x00007fff4b713b2b -[NSMenu performKeyEquivalent:] + 68
113 com.apple.AppKit              	0x00007fff4bb99517 routeKeyEquivalent + 860
114 com.apple.AppKit              	0x00007fff4b3d19a0 -[NSApplication(NSEvent) sendEvent:] + 1064
115 libqcocoa.dylib               	0x0000000116f6e669 0x116f41000 + 185961
116 com.apple.AppKit              	0x00007fff4b3bfee8 -[NSApplication run] + 755
117 libqcocoa.dylib               	0x0000000116f6ae0d 0x116f41000 + 171533
118 org.qt-project.QtCore         	0x000000010d9d5641 QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 417
119 org.qt-project.QtCore         	0x000000010d9da358 QCoreApplication::exec() + 392
120                               	0x0000000100d42cec main + 540
121 libdyld.dylib                 	0x00007fff7a2613d5 start + 1

</code></pre>

---

## Post #8 by @lassoan (2019-06-15 17:49 UTC)

<p>Which call caused the crash? You may try <code>plot.show()</code> (without <code>block=False</code>). There are 15-20 backends, I would expect that at least a few of them works on Mac, too.</p>

---

## Post #9 by @pieper (2019-06-16 19:31 UTC)

<p>The wx version dies on this line:</p>
<pre><code class="lang-auto">fig, ax = plt.subplots()
</code></pre>
<p>But using Agg directly works on the mac as shown in the example below.</p>
<p>(For context, this example is only slightly updated from something I put on the <a href="https://www.slicer.org/wiki/Slicer3:Python#Matplotlib_plotting_functionality">Slicer3 wiki page almost 10 years ago</a> when we first started playing with python packages in Slicer).</p>
<pre><code class="lang-auto">import matplotlib
matplotlib.use ( 'Agg' )
from pylab import *

t1 = arange(0.0, 5.0, 0.1)
t2 = arange(0.0, 5.0, 0.02)
t3 = arange(0.0, 2.0, 0.01) 

subplot(211)
plot(t1, cos(2*pi*t1)*exp(-t1), 'bo', t2, cos(2*pi*t2)*exp(-t2), 'k')
grid(True)
title('A tale of 2 subplots')
ylabel('Damped')

subplot(212)
plot(t3, cos(2*pi*t3), 'r--')
grid(True)
xlabel('time (s)')
ylabel('Undamped')
savefig ( 'MatplotlibExample.png' )

import Slicer
r = vtk.vtkPNGReader()
v = vtk.vtkImageViewer()
r.SetFileName( 'MatplotlibExample.png' )

v.SetColorWindow(255)
v.SetColorLevel(128)
v.SetInputConnection(r.GetOutputPort())
v.Render()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/926a7f715da74a3eb67c3ab3263afb25a579e8b7.png" data-download-href="/uploads/short-url/kTfSDpsF2fvnwZuqO0sZuGOjmcL.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/926a7f715da74a3eb67c3ab3263afb25a579e8b7_2_629x500.png" alt="image" data-base62-sha1="kTfSDpsF2fvnwZuqO0sZuGOjmcL" width="629" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/926a7f715da74a3eb67c3ab3263afb25a579e8b7_2_629x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/926a7f715da74a3eb67c3ab3263afb25a579e8b7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/926a7f715da74a3eb67c3ab3263afb25a579e8b7.png 2x" data-dominant-color="EEEDEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">642×510 42.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @Jan_Alexander (2021-02-24 10:47 UTC)

<p>When I try to install <em>wxpython</em>  by using</p>
<pre><code class="lang-auto">pip_install('wxpython')
</code></pre>
<p>I get following error:</p>
<pre><code class="lang-auto">configure: error: in `/tmp/pip-install-6tksvgas/wxpython_713cfb256f5442bfa5b03be8be257a56/build/wxbld/gtk3':
    configure: error: no acceptable C compiler found in $PATH
    See `config.log' for more details
    Error running configure
    ERROR: failed building wxWidgets
</code></pre>
<p>What I have tried:</p>
<p>Adapt dockerfile to try to include needed packages while building the docker:</p>
<pre><code class="lang-auto">RUN /home/sliceruser/Slicer/bin/PythonSlicer -m pip install matplotlib SimpleITK
RUN /home/sliceruser/Slicer/bin/PythonSlicer -m pip install -U \
-f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/debian-8 \
wxPython
</code></pre>
<p>I am stuck. For me, It would be very useful to be able to use matplotlib next to the Slicer visualization in the same notebook.</p>
<p>Regards,<br>
Jan</p>

---

## Post #11 by @jamesobutler (2021-02-24 13:09 UTC)

<p>It appears <code>wxPython</code> has <a href="https://pypi.org/project/wxPython/#files" rel="noopener nofollow ugc">wheels</a> available for macOS and Windows. Are you using either of these platforms?</p>
<p>If not, your system would have to build the python package from source which means you would have to have all the build dependencies. This is often problematic for users.</p>

---

## Post #12 by @Jan_Alexander (2021-02-25 08:10 UTC)

<p>I am trying to accomplish this in the slicer notebook <a href="https://hub.docker.com/r/lassoan/slicer-notebook" rel="noopener nofollow ugc">docker</a>.</p>
<p>This docker image is debian linux based. This is why I try to install from <code>https://extras.wxpython.org/wxPython4/extras/linux/gtk3/debian-8</code></p>
<p>Is there a better way?</p>
<p>Jan</p>

---

## Post #13 by @lassoan (2021-02-25 18:51 UTC)

<p>wxWidgets matplotlib backend is not usable from notebooks and it blocks the application’s event loop. You can try to use matplotlib with a notebook-friendly backend; or use other web-native visualization packages that can be used interactively in notebooks.</p>

---

## Post #14 by @Jan_Alexander (2021-03-01 11:12 UTC)

<p>Thank you, I was able to get it working eventually with</p>
<p><code>slicernb.MatplotlibDisplay(matplotlib.pyplot)</code></p>

---

## Post #15 by @Xiaojie_Guo (2024-12-13 03:44 UTC)

<p>Hi, <a class="mention" href="/u/lassoan">@lassoan</a>. Recently, I have become interested in the PythonSlicer project. I have built Slicer-5.6.2 on Win10. What interests me is how to build PythonSlicer.exe in the Slicer project. The project is generated by CMake and opened using Visual Studio. I searched for PythonSlicer as a keyword but couldn’t find this project. It seems that there is not a project called PythonSlicer, but there are some projects related to Python. I don’t know what they mean. So my question is how do I find the project which built the PythonSlicer.exe? I want to learn how to build PythonSlicer. So I can use a similar method in my project.</p>

---

## Post #16 by @lassoan (2024-12-13 04:56 UTC)

<p><code>PythonSlicer</code> is a launcher: a small application that sets up the runtime environment (mostly for loading dynamic libraries from various folders) and launches the Python interpreter (<code>Python-real</code>). The launcher is prebuilt, because Qt libraries needs to be linked statically in the launcher, which requires commercial license. The launcher executable is created by downloading and renaming the prebuilt launcher application.</p>

---

## Post #17 by @Xiaojie_Guo (2024-12-13 06:00 UTC)

<p>Thanks. I found that’s CTKAPPLauncher, right?</p>

---
