---
topic_id: 9946
title: "About The Qtimer And Qtextbrower"
date: 2020-01-25
url: https://discourse.slicer.org/t/9946
---

# About the Qtimer and QTextBrower

**Topic ID**: 9946
**Date**: 2020-01-25
**URL**: https://discourse.slicer.org/t/about-the-qtimer-and-qtextbrower/9946

---

## Post #1 by @timeanddoctor (2020-01-25 17:29 UTC)

<p>I want to update the text in slicer extension by Qtimer and QTextBrower, but nothing happon after run the main(). The code as follows:</p>
<pre><code>self.text= qt.QTextBrowser()  
parametersFormLayout2D.addRow("received:", self.text)

def main(self):
  qt.QTimer.singleShot(100, self.Reader)



def Reader(self):
  try:
    self.data += 1
    if self.data:
      print ('recv:',self.data)
      self.text.insertPlainText(self.data)
   except Exception as ex: 
    print (ex)</code></pre>

---

## Post #2 by @lassoan (2020-01-25 17:57 UTC)

<p>Can you give a full example? It is not clear from your snippets how you use <code>self</code>.</p>

---

## Post #3 by @timeanddoctor (2020-01-26 04:35 UTC)

<p>The problem is  qt.QTimer.singleShot().<br>
I changed to</p>
<p>self.timer = qt.QTimer()<br>
self.timer.setInterval(20)<br>
self.timer.connect(‘timeout()’, self.Reader)</p>
<p>But another problem is there is a slowly runing</p>

---

## Post #4 by @lassoan (2020-01-26 04:50 UTC)

<p>What are you trying to achieve? Displaying real-time data that you receive via OpenIGTLink?</p>

---

## Post #5 by @timeanddoctor (2020-01-26 10:40 UTC)

<p>I try to connecte my single chip computer and display in slicer.<br>
Can I use the Qthread in slicer to deal with the slow-problem? And is there any example for that?</p>

---

## Post #6 by @lassoan (2020-01-26 12:04 UTC)

<p>You need to make sure that communication does not block the main thread for too long.</p>
<p>If you use serial (USB, RS-232,…) communication then you can use this work-in-progress <a href="https://github.com/pzaffino/SlicerArduinoController">Arduino extension</a> for simple single-threaded serial communication implementation or <a href="https://www.plustoolkit.org">Plus toolkit</a> for multi-threaded, networked configuration (communicate with many Arduinos, potentially connected to other computers - not directly to the one that runs Slicer).</p>

---
