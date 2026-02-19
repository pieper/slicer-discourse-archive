---
topic_id: 8400
title: "Easiest Way To Create A Very Simple Set Of Widgets"
date: 2019-09-12
url: https://discourse.slicer.org/t/8400
---

# Easiest way to create a very simple set of widgets?

**Topic ID**: 8400
**Date**: 2019-09-12
**URL**: https://discourse.slicer.org/t/easiest-way-to-create-a-very-simple-set-of-widgets/8400

---

## Post #1 by @Christine_Choirat (2019-09-12 12:58 UTC)

<p>Dear All:</p>
<p>What would the the easiest way to create a very simple GUI, basically a couple of buttons, each button being associated with a user-defined Python function?  In other words, is there any way to use snippets such as <a href="https://pythonprogramminglanguage.com/pyqt5-hello-world/" class="inline-onebox" rel="noopener nofollow ugc">PyQt5 hello world example, Python GUI - Python</a> from the Slicer’s Python interpreter?</p>
<p>With the dev version, I’m running into: “Reason: Incompatible library version: QtWidgets.so requires version 5.13.0 or later, but QtWidgets provides version 5.10.0.”</p>
<p>Thank you!<br>
Christine</p>

---

## Post #2 by @pieper (2019-09-12 13:35 UTC)

<p>Hi Christine -</p>
<p>Slicer provides everything you need for this - it comes with python and Qt already installed.</p>
<p>Here’s an example of what you can do at the python prompt in Slicer:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; b = qt.QPushButton("click me")
&gt;&gt;&gt; b.connect('clicked()', lambda : print('clicked!'))
True
&gt;&gt;&gt; b.show()
</code></pre>
<p>There’s a lot more of course, but here’s the starting point:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Start_Here" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Start_Here</a></p>
<p>Let us know if you don’t find what you need.</p>
<p>-Steve</p>

---

## Post #3 by @lassoan (2019-09-12 13:45 UTC)

<p>There are some more Slicer module development tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials" rel="nofollow noopener">here</a> that reflect recent developments (e.g., use Qt Designer to create module GUI).</p>

---

## Post #4 by @pieper (2019-09-12 13:59 UTC)

<p>Yes, the Perk lab tutorials are great too - I updated the Start Here wiki page to point there as well.</p>

---

## Post #5 by @Christine_Choirat (2019-09-13 14:48 UTC)

<p>Dear Steve and Andras:</p>
<p>Thank you so much, these are exactly the pointers I was looking for.  To put things into context, I had students over summer working on an image segmentation project (not under my direct supervision, so I am somehow familiar with the project, but not aware of all the technical aspects): <a href="https://github.com/EricaMoreira/SlicerSemSeg" rel="nofollow noopener">https://github.com/EricaMoreira/SlicerSemSeg</a>.</p>
<p>My sense was that a (Slicer-based) very simple GUI could be built to wrap Step 6 --&gt; Step 20 of their project and make the user experience more pleasant.  I need some time to go through the resources that you suggested, but my sense is that it shouldn’t take too much effort!</p>
<p>Thanks again for your help!<br>
Christine</p>

---

## Post #6 by @lassoan (2019-09-13 15:09 UTC)

<p>Your results look very nice and it should not be hard to package everything nicely in a Slicer extension so that you don’t need any manual installation/configuration. If you need any help with this then feel free to post specific questions as new topics.</p>

---
