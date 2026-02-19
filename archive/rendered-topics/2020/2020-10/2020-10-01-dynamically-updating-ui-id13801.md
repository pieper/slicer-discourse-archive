---
topic_id: 13801
title: "Dynamically Updating Ui"
date: 2020-10-01
url: https://discourse.slicer.org/t/13801
---

# Dynamically Updating UI

**Topic ID**: 13801
**Date**: 2020-10-01
**URL**: https://discourse.slicer.org/t/dynamically-updating-ui/13801

---

## Post #1 by @jrl (2020-10-01 16:40 UTC)

<p>In general, is there an efficient way to dynamically update the UI? I want to allow the user to enter in a value in a text field (QLineEdit), hit a button, and update a separate field (I’m using QLabel) in the UI to reflect that change (in addition to performing some other logic which I have yet to implement). However, I noticed sometimes there is lagging. If I merely print this new value to the python interactor, it basically occurs instantly. However, updating the UI takes more than 10 seconds sometimes.</p>

---

## Post #2 by @smrolfe (2020-10-01 16:51 UTC)

<p>This shouldn’t take so long, can you post your code here?</p>

---

## Post #3 by @jrl (2020-10-01 17:07 UTC)

<p>Excuse me if any of this is bad practice as I am still learning how to create a module. Here is the portion of the code for this UI update:</p>
<p>widget = slicer.util.loadUI(“filepath”)<br>
self.layout.addWidget(widget)<br>
self.ui = slicer.util.childWidgetVariables(widget)</p>
<p>And then in the function that is tied to the button:<br>
newValue = self.ui.newField.text<br>
self.ui.oldValue.setText(newValue)<br>
self.ui.newField.setText("") (to clear the new field once the user hits the button)</p>
<p>Also not sure if this is relevant and maybe this is affecting the performance, but I created multiple .ui files to use in my module for organizational purposes. Should I only be using 1 or does it not matter?</p>

---

## Post #4 by @smrolfe (2020-10-01 18:27 UTC)

<p>I don’t see anything that would cause the label to not update, so it could be the structure. You can see how it should work with a simple example:</p>
<pre><code>def onToggle():
  str = input.text
  label.setText(str)
  input.setText("Input")

menu = ctk.ctkCollapsibleButton()
menuLayout = qt.QFormLayout(menu)
input = qt.QLineEdit('Input')
label = qt.QLabel("UI Label ")
b=qt.QPushButton('Toggle') 
b.connect('clicked()',onToggle)

menuLayout.addWidget(input)
menuLayout.addWidget(label)
menuLayout.addWidget(b)
menu.show()</code></pre>

---

## Post #5 by @jrl (2020-10-01 19:00 UTC)

<p>Would you recommend that I use pyqt? I’ve seen several tutorials reference it, but the original tutorial I used didn’t utilize it so I didn’t either.</p>

---

## Post #6 by @jamesobutler (2020-10-01 20:55 UTC)

<p>Doing some like <code>a=qt.QPushButton()</code> is already the python interface that you can use in Slicer to interact with Qt which is C++ based. Slicer uses <a href="https://mevislab.github.io/pythonqt/" rel="noopener nofollow ugc">PythonQt</a> and not <a href="https://riverbankcomputing.com/software/pyqt/intro" rel="noopener nofollow ugc">PyQt</a>. They are similar in syntax, but with different licensing.</p>
<p>How are you currently connecting the button press to updating the label?<br>
I generally connect actions using the newer style of</p>
<pre><code class="lang-auto">a=qt.QPushButton()
a.clicked.connect(slotName)
</code></pre>

---

## Post #7 by @jrl (2020-10-02 07:36 UTC)

<p>I’ve read conflicting information on the best practice, but I’ve used the Qt Designer to create my widgets and then reference them within the python file.</p>
<p>As far as the button press, I was using a tutorial on laplace transformations from the Slicer site as a reference which had used a button in the following code</p>
<p>laplaceButton.connect(‘clicked(bool)’, self.onApply)</p>
<p>However, I can’t seem to find the documentation for “connect” for QPushButton. Would you mind pointing me towards the API/documentation for QPushButton, specifically the part that mentions using “clicked” and “connect”? I’ve searched and can’t find it that references those two.</p>

---

## Post #8 by @cpinter (2020-10-02 07:47 UTC)

<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://d33sqmjvzgs8hq.cloudfront.net/wp-content/themes/oneqt/assets/images/favicon.ico.gzip" class="site-icon" width="16" height="16">
      <a href="https://doc.qt.io/qt-5/qabstractbutton.html#clicked" target="_blank" rel="noopener">doc.qt.io</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://doc.qt.io/qt-5/qabstractbutton.html#clicked" target="_blank" rel="noopener">QAbstractButton Class | Qt Widgets 5.15.1</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://d33sqmjvzgs8hq.cloudfront.net/wp-content/themes/oneqt/assets/images/favicon.ico.gzip" class="site-icon" width="16" height="16">
      <a href="https://doc.qt.io/qt-5/qobject.html#connect-2" target="_blank" rel="noopener">doc.qt.io</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://doc.qt.io/qt-5/qobject.html#connect-2" target="_blank" rel="noopener">QObject Class | Qt Core 5.15.1</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #9 by @jrl (2020-10-02 15:06 UTC)

<p>Aren’t those C++? I’m looking for python.</p>

---

## Post #10 by @jamesobutler (2020-10-02 15:47 UTC)

<p>The documentation on how they perform are the same. Are you instead looking for python syntax? If so you can use pyqt documentation as a basis since it is similar to pythonqt but not exactly the same.</p>

---

## Post #11 by @jrl (2020-10-03 07:26 UTC)

<p>Right, I was looking for python syntax. But thank you. I’ll do that then.</p>

---
