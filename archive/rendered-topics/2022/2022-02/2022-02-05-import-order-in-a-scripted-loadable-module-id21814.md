# Import order in a scripted loadable module

**Topic ID**: 21814
**Date**: 2022-02-05
**URL**: https://discourse.slicer.org/t/import-order-in-a-scripted-loadable-module/21814

---

## Post #1 by @CsatiZoltan (2022-02-05 18:23 UTC)

<h3><a name="p-73579-problem-1" class="anchor" href="#p-73579-problem-1" aria-label="Heading link"></a>Problem</h3>
<p>What is the order of the module loading in a scripted loadable module? I realized that I cannot access the <code>slicer</code> module in a class attribute. For example, the code</p>
<pre data-code-wrap="python"><code class="lang-python">class materWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
    pointSet = qt.Signal(slicer.vtkMRMLMarkupsFiducialNode)
    ...
    def __init__(self, parent=None):
        ScriptedLoadableModuleWidget.__init__(self, parent)
        ...

    def setup(self):
        ScriptedLoadableModuleWidget.setup(self)
        ...
</code></pre>
<p>fails on the line where the class attribute is defined with the following error:</p>
<pre data-code-wrap="python"><code class="lang-python">AttributeError: module 'slicer' has no attribute 'vtkMRMLMarkupsFiducialNode'
</code></pre>
<p>On the other hand, if I make <code>pointSet</code> an instance variable (by putting it into <code>__init__</code> for instance), it works. Note that <code>import slicer</code> is already present at the top of the file. I must be missing something in the Python import logic… How could I use the <code>slicer</code> module in a class attribute?</p>
<hr>
<h3><a name="p-73579-background-information-2" class="anchor" href="#p-73579-background-information-2" aria-label="Heading link"></a>Background information</h3>
<p>I want to emit a Qt signal once a specific MRML event has been triggered:</p>
<pre data-code-wrap="python"><code class="lang-python">mrml_event = slicer.vtkMRMLMarkupsFiducialNode.PointPositionDefinedEvent

def onPointSet(observer, eventid):
    self.pointSet.emit(observer)

id = self.markup_node.AddObserver(mrml_event, onPointSet)

@qt.Slot(slicer.vtkMRMLMarkupsFiducialNode)
def test_slot(markup_node):
    print(markup_node.GetName())

self.pointSet.connect(test_slot)
</code></pre>
<p>Why do I complicate my life by connecting a Qt signal to an MRML event callback? Because I want to connect multiple slots to the same event. In this case, when a control point is added to the Markups node, I want to perform multiple tasks:</p>
<ul>
<li>change the color of a button (widget-related)</li>
<li>execute a computation (logic-raleted)</li>
<li>… (features that will come in the future)</li>
</ul>
<p>The signal-slot mechanism allows me to completely separate the logic from the GUI.<br>
A PyQt signal must be a defined as a class attribute, that’s why this problem with <code>pointSet</code> came up.</p>

---

## Post #2 by @ungi (2022-02-06 14:36 UTC)

<p>Hi, that’s not the right way to connect MRML events to Qt functions. MRML nodes are VTK-based objects, so they don’t have Qt signals. Typically, you would add a VTK-style observer function to your module widget class. That observes events from your Markups node. The observer function is in your module widget class, so it has direct access to Qt objects. It can update button colors directly using code like self.ui.myButton.setStyleSheet(…).</p>
<p>There are probably lots of examples if you search in the source code of other modules. E.g. look at this example module: <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Examples/CampTutorial2/CampTutorial2.py" rel="noopener nofollow ugc">https://github.com/PerkLab/PerkLabBootcamp/blob/master/Examples/CampTutorial2/CampTutorial2.py</a><br>
This module is just an example for a tutorial, it doesn’t do exactly what you need. It updates a MRML node (sphere model) when a Markups node is modified. But it’s a good example for how to observe a Markups node.</p>

---

## Post #3 by @CsatiZoltan (2022-02-06 16:59 UTC)

<p>Hi <a class="mention" href="/u/ungi">@ungi</a> . I considered that design choice too. However, it requires that the observation (<code>AddObserver</code>) is defined in the widget class. But I want my application to work without the GUI too, meaning that I must allocate the Markups node in the logic class. That class does not know about the widget class. That is why I included an intermediate step (VTK event → Qt event → perform action): this way the VTK event on the Markups node can be observed by methods (slots) of both the widget class and the logic class.</p>

---

## Post #4 by @lassoan (2022-02-06 17:49 UTC)

<p>When a module class is instantiated, it is still the module discovery phase (the application scans what modules are available, builds a dependency tree, determines in which order the modules will be initialized). Slicer application or other modules are not available yet. If you want to do something at application startup then you can connect a method to the application’s <code>startupCompleted()</code> signal:</p>
<blockquote>
<p>Create logic object on startupCompleted() signal and store it in the module class. This is only necessary if only one logic instance is allowed in the application. For example, this is the case when the logic observes the scene and reacts to changes, modifies nodes automatically</p>
</blockquote>
<p>(source: <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">PerkLab bootcamp, Slicer programming tutorial</a>, slide 11)</p>
<p>See the scripted module template for an example of using this signal:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/4d756f0ef57832d654df7a8dc1a8b10e38b8fba9/Utilities/Templates/Modules/Scripted/TemplateKey.py#L35">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/4d756f0ef57832d654df7a8dc1a8b10e38b8fba9/Utilities/Templates/Modules/Scripted/TemplateKey.py#L35" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4d756f0ef57832d654df7a8dc1a8b10e38b8fba9/Utilities/Templates/Modules/Scripted/TemplateKey.py#L35" target="_blank" rel="noopener">Slicer/Slicer/blob/4d756f0ef57832d654df7a8dc1a8b10e38b8fba9/Utilities/Templates/Modules/Scripted/TemplateKey.py#L35</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="25" style="counter-reset: li-counter 24 ;">
          <li>This is an example of scripted loadable module bundled in an extension.</li>
          <li>See more information in &lt;a href="https://github.com/organization/projectname#TemplateKey"&gt;module documentation&lt;/a&gt;.</li>
          <li>"""</li>
          <li>    # TODO: replace with organization, grant and thanks</li>
          <li>    self.parent.acknowledgementText = """</li>
          <li>This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc., Andras Lasso, PerkLab,</li>
          <li>and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.</li>
          <li>"""</li>
          <li></li>
          <li>    # Additional initialization step after application startup is complete</li>
          <li class="selected">    slicer.app.connect("startupCompleted()", registerSampleData)</li>
          <li></li>
          <li>#</li>
          <li># Register sample data sets in Sample Data module</li>
          <li>#</li>
          <li></li>
          <li>def registerSampleData():</li>
          <li>  """</li>
          <li>  Add data sets to Sample Data module.</li>
          <li>  """</li>
          <li>  # It is always recommended to provide sample data for users to make it easy to try the module,</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @CsatiZoltan (2022-02-06 18:55 UTC)

<p>Thank you, this was very valuable!<br>
I read the bootcamp tutorials before, but skipped the details that I did not understand then; time to reread them with my current, deeper, understanding…<br>
I found <a href="https://apidocs.slicer.org/master/classqSlicerApplication.html#a97b2b5f43e708bfc9d874871a7e3260f" rel="noopener nofollow ugc"><code>startupCompleted</code></a> in the API docs. One question though: how could I know that <code>slicer.app.startupCompleted()</code> is the Python wrapper of the corresponding C++ method <code>qSlicerApplication::startupCompleted()</code>? I found it by trial and error. Is there a systematic way to discover it (the debugger doesn’t work for me and I don’t have autocompletion for the <code>slicer</code> module in my IDE)?</p>

---

## Post #6 by @lassoan (2022-02-06 19:05 UTC)

<aside class="quote no-group" data-username="CsatiZoltan" data-post="5" data-topic="21814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/csatizoltan/48/13807_2.png" class="avatar"> CsatiZoltan:</div>
<blockquote>
<p>how could I know that <code>slicer.app.startupCompleted()</code> is the Python wrapper of the corresponding C++ method <code>qSlicerApplication::startupCompleted()</code> ?</p>
</blockquote>
</aside>
<p>You can find <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#doxygen-style-documentation">here</a> a set of rules how C++ classes, methods, properties are accessible in Python.</p>
<p>As with most APIs, probably the most effective ways of learning examples, tutorials, and trial and error. API documentation is sometimes useful, too. If none of these help then you can get all the answers from the source code or by asking here.</p>
<aside class="quote no-group" data-username="CsatiZoltan" data-post="5" data-topic="21814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/csatizoltan/48/13807_2.png" class="avatar"> CsatiZoltan:</div>
<blockquote>
<p>the debugger doesn’t work for me and I don’t have autocompletion for the <code>slicer</code> module in my IDE</p>
</blockquote>
</aside>
<p>Multiple debuggers can be used. Feel free to create a new topic if you have trouble setting up a Python debugger.</p>

---
