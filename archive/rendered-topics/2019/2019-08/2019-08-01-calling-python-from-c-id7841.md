# Calling Python from C++

**Topic ID**: 7841
**Date**: 2019-08-01
**URL**: https://discourse.slicer.org/t/calling-python-from-c/7841

---

## Post #1 by @rprueckl (2019-08-01 18:18 UTC)

<p>Hi, as the title suggests, the question is whether there is a possibility to call a scripted python module from C++, and if yes, how to do that.</p>

---

## Post #2 by @lassoan (2019-08-01 18:33 UTC)

<p>In general, infrastructure is implemented in C++ (it is a bit more work but code is usually more robust, easier to maintain, and has better performance), which is easily accessible from both Python and C++.</p>
<p>If you want to call Python from C++ then it means that infrastructure-like code is implemented in Python, which is not desirable.</p>
<p>If you are sure that you must call Python from C++ then you can use a Python scripted CLI module with a C++ interface (the same way as you would <a href="https://github.com/Slicer/Slicer/blob/dc72547a0252053ec751924fdb75ef36e0c1718d/Modules/Loadable/CropVolume/Logic/vtkSlicerCropVolumeLogic.cxx#L577-L581" rel="nofollow noopener">run any other CLI module from C++</a>) or you can run arbitrary Python code using <a href="https://github.com/Slicer/Slicer/blob/dc72547a0252053ec751924fdb75ef36e0c1718d/Modules/Loadable/Segmentations/qSlicerSegmentationsModule.cxx#L198-L200" rel="nofollow noopener"><code>evalScript</code></a>.</p>

---

## Post #3 by @rprueckl (2019-08-01 19:18 UTC)

<p>Yes, that’s clear. The question was regarding a Python scripted CLI (e.g. Surface Toolkit) that I want to use in my workflow. I tried it with pattern I used for calling CLI modules, but somehow I got null pointers… I will try again…</p>

---

## Post #4 by @lassoan (2019-08-01 21:12 UTC)

<p>Currently, surface toolkit is a Python scripted module, not a CLI. We left it like this, because it exposes very simple features (few lines of code each). The module is currently being reworked. What Surface toolbox feature would you like to use in your module?</p>

---

## Post #5 by @rprueckl (2019-08-02 07:27 UTC)

<p>Sure, wrong terminology on my side.<br>
I find the ‘Connectivity’ tool very handy. I saw in the source code that there was a suggestion to consider a certain minimum size for the individual parts, which I also would find very useful.</p>

---

## Post #6 by @rprueckl (2019-08-02 13:33 UTC)

<p>Sorry, I’m stuck with this one. Is there a difference between a Python scripted CLI module and a Python scripted module?</p>
<p>For calling the SurfaceToolbox this is what I have:</p>
<pre><code class="lang-auto">qSlicerScriptedLoadableModule* scrModule = static_cast&lt;qSlicerScriptedLoadableModule*&gt;(qSlicerCoreApplication::application()-&gt;moduleManager()-&gt;module("SurfaceToolbox"));
qSlicerScriptedLoadableModuleWidget *scrWidget = static_cast&lt;qSlicerScriptedLoadableModuleWidget*&gt;(scrModule-&gt;widgetRepresentation());
vtkSlicerScriptedLoadableModuleLogic* moduleLogic = vtkSlicerScriptedLoadableModuleLogic::SafeDownCast(scrModule-&gt;logic());

// create scripted module node
d-&gt;scrNode = vtkMRMLScriptedModuleNode::SafeDownCast(scene-&gt;CreateNodeByClass("vtkMRMLScriptedModuleNode"));
d-&gt;scrNode-&gt;Register(d);

// Add node to the scene
scene-&gt;AddNode(d-&gt;scrNode);

// set node to widget
scrWidget-&gt;setEditedNode(d-&gt;scrNode);

// set parameters
d-&gt;scrNode-&gt;SetParameter("connectivity", "true");
</code></pre>
<p>I do not know how to execute the logic, as there is no <code>Apply</code> method. Moreover, I don’t know how to specify the input and output models.</p>

---

## Post #7 by @rprueckl (2019-08-06 11:34 UTC)

<p>Considering the comments from <a href="https://discourse.slicer.org/t/updated-sample-code-for-calling-cli-via-c/7840/4">here</a>, I reduced the code as follows, but still the question remains: can I execute the scripted module based on the following code? How would I do that?</p>
<pre><code class="lang-auto">// get module and its widget
qSlicerScriptedLoadableModule* scrModule = static_cast&lt;qSlicerScriptedLoadableModule*&gt;(qSlicerCoreApplication::application()-&gt;moduleManager()-&gt;module("SurfaceToolbox"));
vtkSlicerScriptedLoadableModuleLogic* moduleLogic = vtkSlicerScriptedLoadableModuleLogic::SafeDownCast(scrModule-&gt;logic());

// create scripted module node
vtkMRMLScriptedModuleNode* scrNode = vtkMRMLScriptedModuleNode::SafeDownCast(scene-&gt;CreateNodeByClass("vtkMRMLScriptedModuleNode"));
scene-&gt;AddNode(scrNode);

// set parameters
scrNode-&gt;SetParameter("connectivity", "true");

// TBD: set input/output nodes
// TBD: start execution
</code></pre>

---

## Post #8 by @lassoan (2019-08-07 04:45 UTC)

<p>You can use Python scripted modules using <code>evalScript</code>. For example:</p>
<pre><code>PythonQt::init();
PythonQtObjectPtr context = PythonQt::self()-&gt;getMainModule();
context.evalScript(QString("import SampleData; SampleData.SampleDataLogic().downloadMRHead()"));</code></pre>

---

## Post #9 by @Zhiy (2020-06-26 14:29 UTC)

<p>Hi, I am trying to call a Python script (python3.7) that runs scipy functions in Slicer C++ module. Can I do this?</p>

---

## Post #10 by @lassoan (2020-06-26 15:14 UTC)

<p>There are several options for calling Python from C++ (one of them is shown in my comment above, using <code>evalScript</code>) and it is done at many places in Slicer. However, C++ modules provide low-level infrastructure, so it would not make sense for a C++ module to depend on Python.</p>
<p>If you want to implement some performance-critical processing in C++ but other features are in Python then I would recommend to:</p>
<ul>
<li>create a hidden C++ loadable module that just implements performance-critical processing in its logic classes: these classes are all Python-wrapped and so can be used from either C++ of Python modules</li>
<li>create Python-scripted module that uses your C++ module’s logic and any Python packages (scipy, etc.)</li>
</ul>
<p>Also note that VTK, ITK, and other libraries bundled with Slicer already provide many features of scipy, so you may remove the need to call Python from C++ by using those libraries instead.</p>

---
