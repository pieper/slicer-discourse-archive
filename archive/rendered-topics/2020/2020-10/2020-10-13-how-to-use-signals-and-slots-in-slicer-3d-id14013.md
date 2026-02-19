---
topic_id: 14013
title: "How To Use Signals And Slots In Slicer 3D"
date: 2020-10-13
url: https://discourse.slicer.org/t/14013
---

# How to use signals and slots in Slicer 3d?

**Topic ID**: 14013
**Date**: 2020-10-13
**URL**: https://discourse.slicer.org/t/how-to-use-signals-and-slots-in-slicer-3d/14013

---

## Post #1 by @Chintha_Siva_Prasad (2020-10-13 14:28 UTC)

<p>I am familiar with pyqt.  I want to use signals and slots mechanism in my slicer python script. For some reason when I am connecting the signal to the slot, slicer is exiting abnormally.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea5135400ea87fde32dacc513d5090c6ec905fdc.png" alt="Screenshot from 2020-10-13 19-57-03" data-base62-sha1="xqRIm9GyuQOtqKdDJBKl1w3cBrK" width="543" height="109"><br>
How to  use signals and slots in slicer pythonqt?</p>

---

## Post #2 by @jamesobutler (2020-10-13 14:54 UTC)

<p>A previous post of mine mentioned some about basics of using Qt signals and slots with python.</p><aside class="quote" data-post="6" data-topic="13801">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/dynamically-updating-ui/13801/6">Dynamically Updating UI</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Doing some like a=qt.QPushButton() is already the python interface that you can use in Slicer to interact with Qt which is C++ based. Slicer uses <a href="https://mevislab.github.io/pythonqt/" rel="noopener nofollow ugc">PythonQt</a> and not <a href="https://riverbankcomputing.com/software/pyqt/intro" rel="noopener nofollow ugc">PyQt</a>. They are similar in syntax, but with different licensing. 
How are you currently connecting the button press to updating the label? 
I generally connect actions using the newer style of 
a=qt.QPushButton()
a.clicked.connect(slotName)
  </blockquote>
</aside>

<p><strong>Essentially the syntax is something like {object}.{signal_name}.connect({slot_name}).</strong></p>
<p>So something that is based on QProgressBar will have <a href="https://doc.qt.io/qt-5/qprogressbar.html#signals" rel="noopener nofollow ugc">these signals</a> such as valueChanged. Therefore</p>
<pre data-code-wrap="python"><code class="lang-python">def printMyNewValue(value):
  print("The progress bar value is now: {}".format(value))

import qt
progress_bar = qt.QProgressBar()
progress_bar.setMaximum(10)
progress_bar.valueChanged.connect(printMyNewValue)
progress_bar.setValue(4)  # will then print "The progress bar value is now: 4"
</code></pre>

---

## Post #3 by @Chintha_Siva_Prasad (2020-10-14 14:20 UTC)

<p>I want to create a new signal and then connect it to a slot. I don’t want to use the pre-defined signals of widgets.</p>

---

## Post #4 by @Chintha_Siva_Prasad (2020-10-14 14:23 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea5135400ea87fde32dacc513d5090c6ec905fdc.png" alt="Screenshot from 2020-10-13 19-57-03" data-base62-sha1="xqRIm9GyuQOtqKdDJBKl1w3cBrK" width="543" height="109"></p>
<p>When I am executing the above code slicer is exiting abnormally. How can I create a new signal in slicer that works fine?</p>

---

## Post #5 by @lassoan (2020-10-15 04:43 UTC)

<p>This example works for me:</p>
<pre data-code-wrap="python"><code class="lang-python">class C(qt.QObject):
    received = qt.Signal(object)
    def __init__(self):
        super(C, self).__init__(None)
    def process(self, msg):
        self.received.emit(msg)

class D(qt.QObject):
    def __init__(self, sender):
        super(D, self).__init__(None)
        sender.received.connect(self.process)
    def process(self, msg):
        print("Processed this: "+repr(msg))

c = C()
d = D(c)
m = {'h': {'t': 's'}, 'c': {'e': 'i'}}

c.process(m)
</code></pre>
<p>(taken from these discussions: <a href="https://discourse.slicer.org/t/custom-signal-slots-with-pythonqt/3278/6" class="inline-onebox">Custom Signal/Slots with PythonQt - #6 by ihnorton</a> and <a href="https://sourceforge.net/p/pythonqt/discussion/631393/thread/bbc98b8f/" class="inline-onebox">PythonQt / Discussion / Help: Segmentation fault after emiting a signal</a>)</p>
<p>However, normally there is no need to create Qt-based Python classes and define new signals and slots, as you can communicate via MRML nodes and VTK event observations:</p>
<aside class="quote" data-post="8" data-topic="3278">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/custom-signal-slots-with-pythonqt/3278/8">Custom Signal/Slots with PythonQt</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    We have signal/slot mechanism in Qt and observer mechanism in VTK, and you can implement custom plugin or callback mechanisms. These are all available to be used from both C++ and Python. 
Probably the most universal way (that is available from all Slicer classes) is to observe/invoke custom modified events on a MRML node.
  </blockquote>
</aside>

<p>What is your use case? What would you like to achieve with the custom signals/slots?</p>

---

## Post #6 by @Chintha_Siva_Prasad (2020-10-18 15:18 UTC)

<p>I want to change the progress of a progressbar from another thread.<br>
i want to create a signal(int) and connect it to progressBar.setValue(int).<br>
But when I am connecting it is exiting…</p>

---
