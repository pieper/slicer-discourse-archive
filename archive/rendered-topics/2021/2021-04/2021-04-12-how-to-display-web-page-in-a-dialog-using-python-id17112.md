---
topic_id: 17112
title: "How To Display Web Page In A Dialog Using Python"
date: 2021-04-12
url: https://discourse.slicer.org/t/17112
---

# How to display web page in a dialog using Python?

**Topic ID**: 17112
**Date**: 2021-04-12
**URL**: https://discourse.slicer.org/t/how-to-display-web-page-in-a-dialog-using-python/17112

---

## Post #1 by @spycolyf (2021-04-12 17:34 UTC)

<p>Good afternoon <a class="mention" href="/u/pieper">@pieper</a>  <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I am working on issue, Help Link Button <a href="https://github.com/KitwareMedical/SlicerQReads/issues/65" rel="noopener nofollow ugc">#65</a>. I would like to launch a help webpage when the user pushes the “Help” button. This seems fairly simple I know, but I finally have a little time to start learning. Is this something I can do in qreads.py? How do I associate launching my URL with the button?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2021-04-12 17:50 UTC)

<p>You can open a link in the default web browser like this:</p>
<pre><code>qt.QDesktopServices.openUrl(qt.QUrl('http://www.slicer.org'))
</code></pre>
<p>You can show a webpage embedded in the module GUI (or in a popup window within Slicer) like this:</p>
<pre><code class="lang-python">webWidget = slicer.qSlicerWebWidget()
webWidget.url = qt.QUrl('http://www.slicer.org')
webWidget.show()

# Manually reposition the widget
slicerGeometry = slicer.util.mainWindow().geometry
webWidget.size = qt.QSize(300, 300)
webWidget.pos = qt.QPoint(slicerGeometry.x() + 20, slicerGeometry.y() + 50)
</code></pre>

---

## Post #3 by @spycolyf (2021-04-15 21:11 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I’m trying to use my HelpButton to launch a web page. HelpButton is defined in my qreads.ui file.</p>
<p>I’m getting this error after pushing the help button.<br>
“TypeError: showSlicerQREADSHelp() takes 0 positional arguments but 1 was given”</p>
<p>Here is my code…</p>
<pre><code class="lang-python">  self.ui.HelpButton.connect("clicked()", self.logic.showSlicerQREADSHelp)
  .
  .
  .

def showSlicerQREADSHelp():
    webWidget = slicer.qSlicerWebWidget()
    webWidget.url = qt.QUrl('http://www.google.com')
    webWidget.show()

    # Manually reposition the widget
    slicerGeometry = slicer.util.mainWindow().geometry
    webWidget.size = qt.QSize(300, 300)
    webWidget.pos = qt.QPoint(slicerGeometry.x() + 20, slicerGeometry.y() + 50)
</code></pre>

---

## Post #4 by @lassoan (2021-04-15 21:15 UTC)

<p>You need to add <code>self</code> as the first argument to all non-static methods in a class.</p>

---

## Post #5 by @spycolyf (2021-04-15 21:43 UTC)

<p>I did that and after pushed the Help button, Slicer flashed up something, paused and then aborted.</p>

---

## Post #6 by @jamesobutler (2021-04-15 21:56 UTC)

<p>Your local variable <code>webWidget</code> is getting destroyed at the end of the method. You can instead define a <code>self.web_widget = None</code> in the <code>__init__</code> method of your class and then use it in your <code>showSlicerQREADSHelp</code> and then your window should be persistent.</p>

---

## Post #7 by @spycolyf (2021-04-16 00:17 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a><br>
,<br>
Thank you so much. Took me a while to experiment until I understood scope, but I finally got it.</p>
<p>I’m getting there thanks to all of the help…</p>
<pre><code class="lang-python">def setup(self):

  # Create Web Widget for HelpButton press event
  self.helpButtonWebWidget = None
  .
  .
  .
  self.ui.HelpButton.connect("clicked()", self.showSlicerQREADSHelp)
  .
  . 
  .
  def showSlicerQREADSHelp(self):
    # Create the SlicerQREADS Help webpage object
    self.helpButtonWebWidget = slicer.qSlicerWebWidget()
    self.helpButtonWebWidget.url = qt.QUrl('http://www.google.com')
    self.helpButtonWebWidget.show()
</code></pre>

---

## Post #8 by @jcfr (2021-04-16 00:54 UTC)

<p>Few comments:</p>
<ul>
<li>
<p>Instead of using the name <code>helpButtonWebWidget</code>, consider using <code>helpWebWidget</code>, the fact a button is used to display it is not relevant.</p>
</li>
<li>
<p>consider using properly formatted docstring for the function:</p>
<pre><code class="lang-python">def showSlicerQREADSHelp(self):
  """Display the help website of the application using a non-modal dialog
  """
  [...]
</code></pre>
</li>
<li>
<p>to ensure the existing widget is updated if the user click multiple time on the button, consider doing something like this:</p>
<pre><code class="lang-auto">def showSlicerQREADSHelp(self):
  """Display the help website of the application using a non-modal dialog
  """
  if self.helpButtonWebWidget is None:
    self.helpButtonWebWidget = slicer.qSlicerWebWidget()
    self.helpButtonWebWidget.url = qt.QUrl('http://www.google.com')
  self.helpButtonWebWidget.show()
</code></pre>
</li>
<li>
<p>To reference code block in discourse, consider using the backtick. For example, here is a screenshot of how I edited your last comment:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d99e49f5a638d6a526e1215ef104c6b45707420.png" alt="image" data-base62-sha1="b4utJuLpVbq07ZLBKb2RcqpnfMI" width="584" height="390"></p>
</li>
</ul>

---

## Post #9 by @spycolyf (2021-04-16 02:06 UTC)

<p>OK. Thanks JC. I want to follow the Slicer coding standards. Thanks for sharing.</p>

---

## Post #10 by @spycolyf (2021-04-16 02:09 UTC)

<ol>
<li>
<p>How do I show that ruler <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87501d3841b9d13f6cf2306572b0951b236cf8e6.png" alt="Ruler" data-base62-sha1="jj26l6bR7pPK12UTdw6P92W3Wce" width="48" height="48">  which is displayed at the bottom of the images? And then how do I set the sizes and colors?</p>
</li>
<li>
<p>How you set the button icons? Are you placing them<br>
in resources somehow outside of QT?</p>
</li>
</ol>
<p>Thanks.</p>

---
