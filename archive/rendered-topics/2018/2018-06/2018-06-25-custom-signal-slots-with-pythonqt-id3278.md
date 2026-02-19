---
topic_id: 3278
title: "Custom Signal Slots With Pythonqt"
date: 2018-06-25
url: https://discourse.slicer.org/t/3278
---

# Custom Signal/Slots with PythonQt

**Topic ID**: 3278
**Date**: 2018-06-25
**URL**: https://discourse.slicer.org/t/custom-signal-slots-with-pythonqt/3278

---

## Post #1 by @mcfly3001 (2018-06-25 13:38 UTC)

<p>Hi all,</p>
<p>the signal/slot system of Qt is a very helpful mechanism for implementing callbacks. I was wondering if I can create my own signals and slots with PythonQt but had no success so far.<br>
In other projects where I use e.g. pySide I can subclass from “QObject” and then define my custom signals which then can be connected to my callbacks. When searching in PythonQt threads I found a similar code snippet here:</p>
<p><a href="https://sourceforge.net/p/pythonqt/discussion/631393/thread/bbc98b8f/" class="onebox" target="_blank" rel="nofollow noopener">https://sourceforge.net/p/pythonqt/discussion/631393/thread/bbc98b8f/</a></p>
<p>Unfortunately I am not able to get a PythonQt.QtCore.QObject object in the Python version of Slicer. Is this some wanted restriction?<br>
If this is not possible, is there a similar mechansim available? As an example: I have an IGTL connection which receives data. Based on the data I want to update some UI elements. The connection class and the Widget class are two separate classes though. I am trying to keep the logic separated from the UI.</p>
<p>Thanks for any help!</p>

---

## Post #2 by @jcfr (2018-06-25 23:54 UTC)

<aside class="quote no-group" data-username="mcfly3001" data-post="1" data-topic="3278">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>Unfortunately I am not able to get a PythonQt.QtCore.QObject object in the Python version of Slicer. Is this some wanted restriction?</p>
</blockquote>
</aside>
<p>In addition of being available in the <code>PythonQt.QtXXX</code> namespace, for convenience, all qt objects are also imported in the <code>qt</code> namespace.</p>
<p>Any of these currently work:</p>
<pre><code class="lang-auto">import qt
qt.Signal("QVariant")
</code></pre>
<p>or</p>
<pre><code class="lang-auto">import PythonQt
PythonQt.QtCore.Signal("QVariant")
</code></pre>
<p>That said, <code>QObject</code> is not available. We should probably update the version of PythonQt bundled in Slicer. It is currently based on <a href="https://sourceforge.net/p/pythonqt/code/455/">r455</a>. More details here: <a href="https://github.com/commontk/PythonQt" class="inline-onebox">GitHub - commontk/PythonQt: CMake-ified version of PythonQt</a></p>

---

## Post #3 by @pieper (2018-06-26 07:05 UTC)

<p>It would be good to know if PythonQt supports creating signals directly and if it does we can add it to Slicer.  There are limits compared with PySide, but it gets better over time.  Did you look at the <a href="http://pythonqt.sourceforge.net">PythonQt page</a> and check with the folks there?</p>

---

## Post #4 by @mcfly3001 (2018-06-26 08:30 UTC)

<p>Thanks for your suggestions. I reviewed the PythonQt page which says:</p>
<blockquote>
<p>QObject.emit to emit Qt signals from Python is not yet implemented but PythonQt allows to just emit a signal by calling it like a normal slot</p>
</blockquote>
<p>So I will now try to create a signal and emit it directly as jcfr suggested. Just to be sure, would something like this work then?</p>
<pre data-code-wrap="python"><code class="lang-python"> import qt
 
 class ReceiverClass:
 
     new_parameters_received = qt.Signal("QVariant")
 
     def _on_reveive(self, params):
         new_parameters_received.emit(params)

 class UserInterface:
     
    def __init__(self, receiver):
       receiver.new_parameters_received.connect(self._on_new_params)

    def _on_new_params(self, data):
        self._bt_foo.setText(data[0])
        ....
</code></pre>
<p>Thanks again!</p>

---

## Post #5 by @mcfly3001 (2018-06-28 12:33 UTC)

<p>Hi again,</p>
<p>I did some more tests and still have some problems using the signal-slot concept via Qt. To beginn with I forgot to mention that I was using the stable release of Slicer. Therefore, there was no qt.Signal or qt.Slot object available, only a qt.SIGNAL which would not work.</p>
<p>After updating to a nightly release version of Slicer, the qt.Signal and qt.Slot classes were available. I was still not able though to connect a simple signal with a slot. Everytime I try to connect, the whole application just crashes, e.g.:</p>
<pre><code class="lang-python">import qt

test_sig = qt.Signal("QVariant")

@qt.Slot("QVariant")
def test_slot(data):
    print(data)

test_sig.connect(test_slot)
test_sig.emit("Foo")
</code></pre>
<p>Other similar tries (e.g. without qt.Slot decorator) lead to a crash or a non-working connection. In the end I just tried to wrap the signal-slot connection into a class which derives from QWidget (since QObject is not available). This seems to solve the issue. The signal is connected and also correctly triggered.</p>
<p>It still though does not feel right to subclass from QWidget for every class that needs signal-slot feature. Therefore I might use an alternative solution, e.g. the PySignals module. Or are there any better proposals for me?</p>
<p>Thanks!</p>

---

## Post #6 by @ihnorton (2018-06-28 14:54 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="3278">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>That said, <code>QObject</code> is not available. We should probably update the version of PythonQt bundled in Slicer. It is currently based on <a href="https://sourceforge.net/p/pythonqt/code/455/">r455</a>.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a> I looked through the commits after r455, and didn’t see anything that was obviously related… I wonder if something from CTK is shadowing/removing QObject, because it is <a href="https://github.com/commontk/PythonQt/blob/patched-8/generated_cpp_56/com_trolltech_qt_core/com_trolltech_qt_core_init.cpp#L109">registered</a> the same way as many other classes which <em>are</em> available under <code>PythonQt.QtCore</code> in the repl (e.g. <code>QMimeData</code>).</p>

---

## Post #7 by @PaoloZaffino (2020-05-25 12:23 UTC)

<p>Hi all,<br>
I’m interested in emitting a signal and, if some object is registered on this “channel”, in receiving it.<br>
Any idea about which qt tool can I use?<br>
I also read <a href="https://discourse.slicer.org/t/use-of-qt-signal-leads-to-a-crash-on-exit/8321">this</a> and I got a crash too.</p>
<p>Thanks a lot.<br>
Paolo</p>

---

## Post #8 by @lassoan (2020-05-25 12:57 UTC)

<p>We have signal/slot mechanism in Qt and observer mechanism in VTK, and you can implement custom plugin or callback mechanisms. These are all available to be used from both C++ and Python.</p>
<p>Probably the most universal way (that is available from all Slicer classes) is to observe/invoke custom modified events on a MRML node.</p>

---

## Post #9 by @PaoloZaffino (2020-05-25 19:04 UTC)

<p>Thanks Andras,<br>
I used the observe/invoke mechanism of MRML node.</p>
<p>Paolo</p>

---
