---
topic_id: 17172
title: "Module Qt Designer Check Box"
date: 2021-04-19
url: https://discourse.slicer.org/t/17172
---

# Module Qt Designer Check Box

**Topic ID**: 17172
**Date**: 2021-04-19
**URL**: https://discourse.slicer.org/t/module-qt-designer-check-box/17172

---

## Post #1 by @Gabriel (2021-04-19 13:55 UTC)

<p>I am creating a module and have used Qt Designer to add in a checkbox.<br>
For now I have just added a print function to test the checkbox, later I want it to carry out a function when clicked on.</p>
<p>In the main PY file, under the “(modulename)widget” class. I have added the following code under<br>
def setup(self):<br>
self.ui.EnableFolderGrab.connect(‘clicked(bool)’, self.onEnableFolderGrabButton)</p>
<p>Then i have created another function in the same class.</p>
<p>def onButtonGrabber(self):<br>
print(“Hello this check box button is working”)</p>
<p>However this function runs (printing the text) every time I click the check box (whether checking or unchecking). When I’d only like it to print (activate the function) when the check box is clicked on, not when it is clicked off. Any help would be much appreciated.<br>
If there is a part of the Slicer Wiki that goes through this you could direct me to that would be great. I’ve gone through the documentation pdf and i believe most developer sections on the wiki but can’t find information regarding this area.</p>
<p>Many Thanks</p>

---

## Post #2 by @jamesobutler (2021-04-19 14:32 UTC)

<p>Qt documentation will likely be the most helpful source when figuring out what signals are available for a QWidget object. You can see QCheckBox signals at <a href="https://doc.qt.io/qt-5/qcheckbox.html#signals" class="inline-onebox" rel="noopener nofollow ugc">QCheckBox Class | Qt Widgets 5.15.3</a>. QCheckBox also inherits from QAbstractButton which is why the <code>clicked()</code> signal is available as well <a href="https://doc.qt.io/qt-5/qabstractbutton.html#signals" class="inline-onebox" rel="noopener nofollow ugc">QAbstractButton Class | Qt Widgets 5.15.3</a>.</p>
<p>Based on what is available there isn’t a signal specifically for when it is checked versus unchecked, so you will have to handle it within your slot <code>onButtonGrabber</code>.</p>
<p>In the example below I use the signal <code>stateChanged</code> from the QCheckBox class which is a little more detailed in that it provides the <a href="https://doc.qt.io/qt-5/qt.html#CheckState-enum" rel="noopener nofollow ugc">Qt CheckState</a> (checked, unchecked, partially checked) rather than just a simple boolean as provided by the <code>clicked</code> signal.</p>
<pre><code class="lang-python">def setup(self):
  self.ui.EnableFolderGrab.stateChanged.connect(self.onButtonGrabber)

def onButtonGrabber(self, checkState):
  if checkState == qt.Qt.Checked:
    print("This checkbox was checked")
  elif checkState == qt.Qt.Unchecked:
    print("This checkbox was unchecked")
</code></pre>

---

## Post #3 by @Gabriel (2021-04-19 16:13 UTC)

<p>Thank you very much, have been reading the links you’ve shared since your post and implemented the code and it works great!</p>
<p>(I think) I understand what you have done, but do you have a couple of Questions if you don’t mind.</p>
<ol>
<li>
<p>Does including   <code>.stateChanged</code> inside of<br>
<code> def setup(self):</code><br>
<code> self.ui.EnableFolderGrab.stateChanged.connect(self.onButtonGrabber)</code></p>
<p>introduce that branch of code, like an <code>import</code>, and allow the ability to use <code>checkState</code> later on (in <code>def onButtonGrabber</code>?</p>
</li>
<li>
<p>How do you know to use <code>qt.Qt.</code>inside of<br>
<code>if checkState == qt.Qt.Checked:</code></p>
</li>
</ol>
<p>I understand both of these are needed and have played around with removing them to view the errors that causes.</p>
<p>P.S. For the original post I accidentally copied over code from a different button, hence the mix match between variable names. That’s a lesson to me on proper commenting and having unique and proper variable names.<br>
Also tried to copy you in using code separated text and will use hyperlinks too if needed!</p>

---

## Post #4 by @jamesobutler (2021-04-19 18:57 UTC)

<ol>
<li>
<p>Signals such as <code>stateChanged</code> send the <code>state</code> which is an <code>int</code> as an input to the slot (<code>onButtonGrabber</code>). It is <code>int</code> type because CheckState is an <code>int</code> enum where <code>qt.Qt.Checked</code> returns the value of 2. The documentation will tell you if there is an input it is passing to the slot or not. It will also tell you the type.</p>
</li>
<li>
<p><code>qt.Qt</code>. as in <code>qt.Qt.Checked</code> is referencing the <a href="https://doc.qt.io/qt-5/qt.html" rel="noopener nofollow ugc">Qt namespace</a> which is where the Qt CheckState is defined as linked in my above post. I think it is the syntax <code>qt.Qt</code> just based on how <a href="https://github.com/MeVisLab/pythonqt" rel="noopener nofollow ugc">PythonQt</a>  python bindings are generated. There isn’t really documentation saying to access the Qt namespace you can do <code>qt.Qt</code>, so just something to observe in examples or ask about on the forum as you have done.</p>
</li>
</ol>

---
