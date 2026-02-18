# Use of qt.Signal leads to a crash on exit

**Topic ID**: 8321
**Date**: 2019-09-06
**URL**: https://discourse.slicer.org/t/use-of-qt-signal-leads-to-a-crash-on-exit/8321

---

## Post #1 by @jcfr (2019-09-06 12:16 UTC)

<p>Recently, I have been investigating the source of a crash on exit.</p>
<p>To reproduce the crash:</p>
<pre><code class="lang-auto">./Slicer --no-main-window --testing
</code></pre>
<p>Notes:</p>
<ul>
<li>removing the connection to the <code>closed</code> signal object <a href="https://github.com/Slicer/Slicer/blob/45cf7d262fc07078fa94ece66520b0ac58f321d7/Modules/Scripted/DICOM/DICOM.py#L153" rel="nofollow noopener">here</a> in the DICOM module avoids the crash on exit from happening.</li>
<li>disconnecting the signal on exit (or just after setting the connection) does <strong>not</strong> prevent the crash from happening</li>
<li>starting the application with the main window prevents the crash on exit from happening</li>
<li>a possibly related thread on the PythonQt forum is this one: <a href="https://sourceforge.net/p/pythonqt/discussion/631393/thread/bbc98b8f/" rel="nofollow noopener"> Segmentation fault after emiting a signal</a>
</li>
<li>yesterday, we updated (see <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28485" rel="nofollow noopener">r28485</a>) to use the latest version of PythonQt thinking the issue would be addressed … but it is not.</li>
</ul>

---

## Post #2 by @jcfr (2019-09-06 12:25 UTC)

<p>Create a script <code>test.py</code> with the following content:</p>
<pre><code class="lang-python">class FooDetailsWidget(qt.QWidget):
  closed = qt.Signal() # Invoked when the dicom widget is closed using the close method
  def __init__(self):
    qt.QWidget.__init__(self)

class Foo(object):
  def __init__(self):
    self.detailsPopup = FooDetailsWidget()
    self.detailsPopup.closed.connect(self.onDetailsPopupClosed)
  def onDetailsPopupClosed(self):
    print("onDetailsPopupClosed")

d = Foo()
d.detailsPopup.closed.emit()

# In this case, disconnecting prevent the crash on exit from happening
# d.detailsPopup.closed.disconnect(d.onDetailsPopupClosed)
</code></pre>
<p>and running Slicer with the following allows to reproduce a crash on exit. But:</p>
<ul>
<li>the condition are not exactly the same</li>
<li>disconnecting the signal prevent the crash from happening whereas in the <code>DICOM</code> module it does <strong>not</strong>
</li>
<li>with/without <code>--no-main-window</code> lead to a crash</li>
</ul>
<pre><code class="lang-auto">./Slicer --disable-modules --no-main-window --testing --python-script /tmp/test.py
</code></pre>

---

## Post #3 by @fbordignon (2020-06-04 14:41 UTC)

<p>Hi jcfr, have you solved this? The pythonQt seems to not support calling emit() directly. Do you have a workaround? Thanks</p>

---

## Post #4 by @lassoan (2020-06-04 15:05 UTC)

<p>Would you like to emit another object’s <em>signal</em>? This was explicitly prohibited in Qt4 but to allow new syntax in Qt5 this cannot be prevented anymore. Still, it should not be done, as you would essentially lie about the internal state of the other object to all connected objects. Objects should always emit their own signals only. Objects can call other object’s <em>slots</em>.</p>

---

## Post #5 by @riep (2023-12-26 16:36 UTC)

<p>Dear all,<br>
I dig up this thread but I think it is worth having a solution to this issue.<br>
I am exactly in the same situation as <a class="mention" href="/u/jcfr">@jcfr</a> : I have a widget in python that emits signals and the moment I connect to these signal in another widget, I have this silent crash on exit, even if disconnection are properly implemented. I have tried several modifications without managing to find a good solution.<br>
<a class="mention" href="/u/jcfr">@jcfr</a> have you explored a bit further this issue ?<br>
Thanks for your input</p>

---

## Post #6 by @lassoan (2023-12-30 13:58 UTC)

<aside class="quote no-group" data-username="riep" data-post="5" data-topic="8321">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/riep/48/9933_2.png" class="avatar"> riep:</div>
<blockquote>
<p>have a widget in python that emits signals</p>
</blockquote>
</aside>
<p>Does the widget emit its own signal, or the tries to  make make another object emit a signal? Can you provide a minimal reproducible example script?</p>

---
