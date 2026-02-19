---
topic_id: 5368
title: "Collapse Expand Widget Buttons Using Python"
date: 2019-01-15
url: https://discourse.slicer.org/t/5368
---

# Collapse/Expand Widget Buttons using Python

**Topic ID**: 5368
**Date**: 2019-01-15
**URL**: https://discourse.slicer.org/t/collapse-expand-widget-buttons-using-python/5368

---

## Post #1 by @brynpitt (2019-01-15 04:03 UTC)

<p>Hello all,</p>
<p>I am developing a new module using the Scripted Module template. I would like to be able collapse/expand the collapsible buttons in the Widget using Python. Specifically, I would like to have some of the buttons collapsed using a python script at startup (using the --python-script option when starting Slicer).</p>
<p>I can find the ctkCollapsibleButton instance, eg (using Slicer Radiomics module as an example):</p>
<blockquote>
<p>slicer.modules.SlicerRadiomicsWidget.layout.itemAt(0).widget()</p>
</blockquote>
<p>According to CTK documentation, the ctkCollapsibleButton should have a method <em>setCollapsed()</em> ; however, I get an error saying the method does not exist:</p>
<blockquote>
<p>slicer.modules.SlicerRadiomicsWidget.layout.itemAt(0).widget().setCollapsed(True)</p>
<p>Traceback (most recent call last):<br>
File "&lt;console&gt;", line 1, in &lt;module&gt;<br>
AttributeError: ctkCollapsibleButton has no attribute named ‘setCollapsed’</p>
</blockquote>
<p>I would appreciate if anyone could tell me how I can collapse/expand the buttons in the widget.</p>
<p>Edit: I am using Slicer 4.10.0.</p>
<p>Thanks in advance,<br>
ebp</p>

---

## Post #2 by @lassoan (2019-01-15 06:09 UTC)

<p>Qt object properties are get/set as attributes in Python:</p>
<pre><code>slicer.modules.SlicerRadiomicsWidget.layout.itemAt(0).widget().collapsed = True
</code></pre>
<p>Note that such low-level hijacking of a module’s GUI would be extremely fragile (if a new item is added to the GUI, references like the one above would be broken). Instead, it would be a much better approach to make the widget customizable (for example, add a method to show/hide some details) or move creation of a widget to a method that you can call from outside of the module to generate a widget section. You can make whatever change you would like in the module and then send a pull request to the module’s maintainer.</p>
<p>What would you like to do?<br>
Why would you need to collapse a section?<br>
Don’t you want a more streamlined user interface (have all the GUI that you need for your workflow in a single module)?</p>

---

## Post #3 by @brynpitt (2019-01-15 17:55 UTC)

<p>Hi Andras,</p>
<p>Thank you for the information. I certainly agree that the sample code I showed is poorly implemented. I just copied/pasted from the Python Interactor while I was experimenting around with the GUI. I have to admit that I am not very familiar with Qt; however, and at the moment, I am not certain how to reference the collapsible buttons more generally. Regardless, the line of code I posted would certainly not be the final implementation.</p>
<p>To answer your other questions, the module is intended to be used as part of a surgeon video console, which is split across multiple screens (the main window is full screen on one monitor, the module GUI is floating on another). The module is large, and it has several sections that need to be used in sequential order. I would like the module to launch with certain sections collapsed because those sections are never used immediately upon launching the module.</p>
<p>I hope that clarifies things. I’m certain there is room to improve the GUI design (I’ve never made a GUI before), so if you have any tips or resources, I would be glad to hear them. If you are interested, I could probably share more specific information with you privately.</p>
<p>Thanks again for your help,<br>
Bryn</p>

---

## Post #4 by @lassoan (2019-01-16 04:46 UTC)

<p>We implemented several 3D Slicer based applications that are used by surgeons and various other specialists for interventional guidance (using overhead monitors, projectors, touchscreens, and augmented reality displays). Due to the huge amount of pre-built software componentsin 3D Slicer, SlicerIGT, and other extensions, it is typically feasible to build an initial application prototype within a week or so and then you can do quick iterations based on user feedback to get practically usable system in a few month. A couple of examples are listed here: <a href="http://www.slicerigt.org/wp/examples/" rel="nofollow noopener">http://www.slicerigt.org/wp/examples/</a></p>
<p>We would be happy to share how we implemented these, but we would need to know much more about what you plan to do:<br>
Do you use real-time imaging (ultrasound, fluoroscopy, MRI, etc.)?<br>
Do you use tool navigation (surgical navigation systems or optical or electromagnetic trackers)?<br>
How surgeons interact with the system (touchscreen, LeapMotion, IMU, tracked tools, …)?<br>
What information do you need to display on how many screens?<br>
Do you need any spatial or temporal calibration?</p>
<p>The most efficient could be if you can attend one of the <a href="https://na-mic.github.io/ProjectWeek/" rel="nofollow noopener">Slicer project weeks</a> where you can probably build a first prototype with help from Slicer experts and other participants who have developed similar systems. You can also explore examples, <a href="http://www.slicerigt.org" rel="nofollow noopener">tutorials</a>, <a href="https://github.com/SlicerIGT" rel="nofollow noopener">source code of existing systems</a>, and of courseyou can also keep posting specific questions on the forum.</p>

---
