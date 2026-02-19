---
topic_id: 12563
title: "Viewing Side By Side"
date: 2020-07-15
url: https://discourse.slicer.org/t/12563
---

# Viewing Side by Side

**Topic ID**: 12563
**Date**: 2020-07-15
**URL**: https://discourse.slicer.org/t/viewing-side-by-side/12563

---

## Post #1 by @vertebrae (2020-07-15 18:52 UTC)

<p>Is there python code to switch the viewing panes? Before I do my segmentation, I need to set the code to display only the Coronal and Sagittal view before the segmentation and then display the 3D view along with the coronal and sagittal view after the segmentation has been complete. Does anyone know how to do this in python?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #2 by @lassoan (2020-07-16 03:10 UTC)

<p>You can find examples for all commonly used functions in the script repository. For example, custom layout creation is described here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout</a></p>

---

## Post #3 by @vertebrae (2020-07-16 13:39 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thank you for helping us with this project. We have one more question. When we use layout 29 (sidebyside), we get the axial and sagittal view. When we used the custom layout sidebyside code from the github to try to get the coronal and sagittal view, we get an error. We copied the code below into our module and created a custom layout ID but this did not work. How can we integrate the github sidebyside code into our module?</p>

---

## Post #4 by @lassoan (2020-07-16 13:44 UTC)

<p>Can you send a github repository link to the line that fails?</p>

---

## Post #5 by @vertebra (2020-07-16 13:46 UTC)

<p>It says invalid syntax when initializing the sideBySideView:</p>
<p>sideBySideView =<br>
“&lt;layout type=“horizontal”&gt;”<br>
"  "<br>
"   &lt;view class=“vtkMRMLSliceNode” singletontag=“Red”&gt;"<br>
"    &lt;property name=“orientation” action=“default”&gt;Sagittal"<br>
"    &lt;property name=“viewlabel” action=“default”&gt;R"<br>
"    &lt;property name=“viewcolor” action=“default”&gt;#F34A33"<br>
"   "<br>
"  "<br>
"  "<br>
"   &lt;view class=“vtkMRMLSliceNode” singletontag=“Yellow”&gt;"<br>
"    &lt;property name=“orientation” action=“default”&gt;Coronal"<br>
"    &lt;property name=“viewlabel” action=“default”&gt;Y"<br>
"    &lt;property name=“viewcolor” action=“default”&gt;#EDD54C"<br>
"   "<br>
"  "<br>
“”</p>
<p>Also, should we put this in the enter function, so it runs when we enter the module?</p>

---

## Post #6 by @cpinter (2020-07-16 14:18 UTC)

<p>You have to ad the closing tags as well: <code>&lt;/layout&gt;</code> at the end, and <code>&lt;/view&gt;</code> and <code>&lt;/property&gt;</code> to the end of the corresponding lines.</p>
<p>I added my custom layouts in the .slicerrc.py file, for example:</p>
<pre><code class="lang-auto">resizableFourUpLayout = ("&lt;layout type=\"vertical\" split=\"true\"&gt;&lt;item&gt;&lt;layout type=\"horizontal\" split=\"true\"&gt;&lt;item&gt;&lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Red\"&gt;&lt;property name=\"orientation\" action=\"default\"&gt;Axial&lt;/property&gt;&lt;property name=\"viewlabel\" action=\"default\"&gt;R&lt;/property&gt;&lt;property name=\"viewcolor\" action=\"default\"&gt;#F34A33&lt;/property&gt;&lt;/view&gt;&lt;/item&gt;&lt;item&gt;&lt;view class=\"vtkMRMLViewNode\" singletontag=\"1\"&gt;&lt;property name=\"viewlabel\" action=\"default\"&gt;1&lt;/property&gt;&lt;/view&gt;&lt;/item&gt;&lt;/layout&gt;&lt;/item&gt;&lt;item&gt;&lt;layout type=\"horizontal\"&gt;&lt;item&gt;&lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Yellow\"&gt;&lt;property name=\"orientation\" action=\"default\"&gt;Sagittal&lt;/property&gt;&lt;property name=\"viewlabel\" action=\"default\"&gt;Y&lt;/property&gt;&lt;property name=\"viewcolor\" action=\"default\"&gt;#EDD54C&lt;/property&gt;&lt;/view&gt;&lt;/item&gt;&lt;item&gt;&lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Green\"&gt;&lt;property name=\"orientation\" action=\"default\"&gt;Coronal&lt;/property&gt;&lt;property name=\"viewlabel\" action=\"default\"&gt;G&lt;/property&gt;&lt;property name=\"viewcolor\" action=\"default\"&gt;#6EB04B&lt;/property&gt;&lt;/view&gt;&lt;/item&gt;&lt;/layout&gt;&lt;/item&gt;&lt;/layout&gt;")
layoutLogic = slicer.app.layoutManager().layoutLogic()
layoutLogic.GetLayoutNode().AddLayoutDescription(520, resizableFourUpLayout)
# slicer.app.layoutManager().setLayout(520) # Uncomment if set on startup
</code></pre>

---

## Post #7 by @vertebra (2020-07-16 14:27 UTC)

<p>Thanks! When we run that <a class="mention" href="/u/cpinter">@cpinter</a> we still get an error on this line:</p>
<p>self.setParameterNode(self.logic.getParameterNode())</p>
<p>The error is: ‘NoneType’ object has no attribute ‘getParameterNode’</p>
<p>Do you have any ideas?</p>

---

## Post #8 by @cpinter (2020-07-16 15:14 UTC)

<p>Without seeing the context (i.e. the surrounding code), it is impossible to tell from one line what is the problem. In general this error means that the variable has not been set properly. Is it possible you want to run this line outside a module class? It would help if we saw some more code.</p>

---

## Post #9 by @vertebra (2020-07-16 15:30 UTC)

<p>Thanks, it works now!</p>

---
