# Workflow that brings together a few modules as tabs in a unifying parent module.

**Topic ID**: 5314
**Date**: 2019-01-08
**URL**: https://discourse.slicer.org/t/workflow-that-brings-together-a-few-modules-as-tabs-in-a-unifying-parent-module/5314

---

## Post #1 by @NormandRbert (2019-01-08 20:54 UTC)

<p>Creating a workflow that brings together a few existing and new custom modules as tabs in a unifying parent module. I am wondering if anyone has used this approach. Sensible? Bad idea? I have inherited code to do this but I am concerned about the design of it.  I would like to see a “best” practice example if one exists.</p>

---

## Post #2 by @lassoan (2019-01-08 21:00 UTC)

<p>Typically you would not reuse entire module widgets to build your workflow interface, because each module widget is expected to be a singleton. Instead, you build it from high-level widgets.</p>
<p>Modules widgets that are implemented well are already built up from high-level reusable widgets. If you come across a module that you would like to use and not implemented like this then let us know and we’ll see if reusable widgets can be easily exposed.</p>

---

## Post #3 by @NormandRobert (2019-01-08 21:08 UTC)

<p>Andras can you pick one or more python module which you think embodies these best practices? Thanks</p>

---

## Post #4 by @adamrankin (2019-01-08 21:09 UTC)

<p>As <a class="mention" href="/u/lassoan">@lassoan</a> said, reusable widgets are the best approach. If they are not available and the authors don’t have the bandwidth to support you, you could try your idea (others have).</p>
<p>I recommend you investigate the <a href="http://www.commontk.org/index.php/Documentation/ctkWorkflowWidget" rel="nofollow noopener">ctkWorkflowWidget</a> as this is what it was designed for.</p>
<p>I personally like this approach for clinician workflows, as it limits the decisions they have to make/content they have to learn. They can always override your workflow by going to a desired module (unless you’ve hidden the module navigator widget).</p>

---

## Post #5 by @NormandRobert (2019-01-08 21:20 UTC)

<p>I was also interested in doing this to create a clinical workflow.</p>

---

## Post #6 by @jcfr (2019-01-08 22:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="5314">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>because each module widget is expected to be a singleton</p>
</blockquote>
</aside>
<p>That said, if complete UI of modules need to be composed together. One could use, the function <code>createNewWidgetRepresentation()</code></p>
<p>For example:</p>
<pre data-code-wrap="python"><code class="lang-python">w = slicer.modules.gaussianblurimagefilter.createNewWidgetRepresentation()
w.show()

w = slicer.modules.segmenteditor.createNewWidgetRepresentation()
w.show()
</code></pre>

---

## Post #7 by @NormandRobert (2019-01-08 23:02 UTC)

<p>I was not going to go there <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"> but the solution I inherited (below) has some similarity to what you suggested and then I noticed that “my” version caused the UI creation code to be called twice, realized it was ugly causing me to start this thread. Looking into your variation which uses “show”. Also thinking that since I am authoring the tabbed modules I should consider Andras’ advice by making those “more” re-usable.  Thank you</p>
<h1>Triggers UI creation</h1>
<pre><code>igtConnection = slicer.modules.igtconnection.createNewWidgetRepresentation()
self.igtConnectionModule = IGTConnection.IGTConnectionWidget(igtConnection)
self.tabWidget.addTab(self.qWidget1, "IGT Connection")
# Triggers UI creation again bad?
self.igtConnectionModule.setup(qFormLayout1)</code></pre>

---

## Post #8 by @NormandRbert (2019-01-09 21:30 UTC)

<p>Been thinking about what you wrote. Imagine a module called SandBox, a template generated with the python script found in the Slicer 3D source tree. It produces the classes  SandBox, SandBoxWidget, SandBoxLogic, SandBoxTest.</p>
<p>So do you recommend that I create a new class say SandBoxWidgetUI with mostly GUI stuff and use it in another  module like this?<br>
import SandBox<br>
sdb=SandBox.SandBoxWidgetUI()</p>
<p>It seems that the names SandBox, SandBoxWidget, SandBoxLogic, SandBoxTest are special and Slicer looks for these functions and makes them available via slicer.modules… unlike my new SandBoxWidgetUI class. I could alternatively reorganize the existing SandBoxWidget() class to make it more useful from another module but that seems less flexible as I would inherit other bits like a constructor I might not need.</p>

---

## Post #9 by @lassoan (2019-01-09 22:54 UTC)

<p>For complex GUI, you can use Qt designer to create a .ui file and instantiate the widget from that.</p>

---

## Post #10 by @pieper (2019-01-10 13:24 UTC)

<p>I like the idea of having a “UI” class be part of the auto-generated module code.  It would encourage best practices.  It would mean updating the templates.</p>

---

## Post #11 by @lassoan (2019-01-10 14:17 UTC)

<p>I haven’t thought about promoting using .ui files to the general public, but I agree that it could work well.</p>
<p>To make Qt designer (with all custom ctk, qMRML, Slicer widgets) available without requiring users to install a compatible version of Qt, we would need to bundle Qt designer binaries in the installation package. It should be no problem, as it requires only a few extra files of a total size of 6 MB (designer.exe, Qt5Designer.dll, and Qt5DesignerComponents.dll; Qt designer plugins are already included). <a class="mention" href="/u/jcfr">@jcfr</a> what do you think?</p>
<p>In addition to bundling designer executable, we should add an “Edit .ui file” button to the Reload&amp;Test section and add an ExtensionWizard template.</p>

---

## Post #12 by @jcfr (2019-01-10 14:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="5314">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>what do you think?</p>
</blockquote>
</aside>
<p>That seems reasonable.</p>
<p>Additional libraries would have to be listed <a href="https://github.com/Slicer/Slicer/blob/53be7ad66d1d6c5655352b5a028c2f22348c1842/CMake/SlicerBlockInstallQt.cmake#L82-L90">here</a> and designer executable could be installed using approach done for <a href="https://github.com/Slicer/Slicer/blob/53be7ad66d1d6c5655352b5a028c2f22348c1842/CMake/SlicerBlockInstallQt.cmake#L94-L96">QtWebEngineProcess</a>.</p>
<p>And if build system not already take care of fixing up the executable … we may have to do something specific.</p>

---

## Post #13 by @pieper (2019-01-10 15:05 UTC)

<p>Wow, bundling Qt Designer with Slicer is a fascinating idea. That could be convenient for everyone, but I also imaging there’s a category of people who might contribute to the ui who wouldn’t think of doing it in C++ or Python but would like using the designer.</p>
<p>I suppose the logical next step would be including all of Qt Creator?  We need to draw the line somewhere but this could be an optional install or developer extension.</p>

---

## Post #14 by @lassoan (2019-01-10 17:37 UTC)

<p>I’ve tried to update the current scripted module template to use a .ui file to generate GUI and it worked really well. It reduced and simplified the code a lot.</p>
<p>Reload works nicely: to update the GUI, it is enough to save the .ui file in Qt Designer and click Reload in Slicer.</p>
<p>Widget variables can be automatically exposed as <code>self.ui.myWidget</code> (similarly how variables are accessible in C++ by generating a skeleton file).</p>
<p>I’ve submitted a pull request so that you can have a look: <a href="https://github.com/Slicer/Slicer/pull/1072/files#diff-c12bcbe4f4bab89847136fc032496bd4R36" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1072/files#diff-c12bcbe4f4bab89847136fc032496bd4R36</a></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> It works so nicely that I think it would worth the time adding designer to the package. Could you have a look? If it’s very easy then it might make sense to include it in 4.10.1.</p>

---

## Post #15 by @jamesobutler (2019-01-10 18:12 UTC)

<p>My group has been using Qt Designer for generating UI files and using them in our Slicer python code using <code>slicer.util.loadUI()</code> for well over a year now. Qt Designer definitely helps with quick prototyping of GUIs and we generally prefer this unless the widget is something extremely simple. For beginners, coding QLayout policies and such is really intimidating and difficult to understand without playing around with something like Qt Designer.</p>

---

## Post #16 by @NormandRbert (2019-01-10 19:12 UTC)

<p>I think it is also valuable to maintain the simple template that can be generated via the python script which Jean-Christophe Fillion-Robin et Steve Pieper wrote some years ago. I also think that said script should be in some bin directory associated with slicer binary as well so you don’t have to download the source to get it. It gives you a quick path to writing a “hello world” module.</p>

---

## Post #17 by @lassoan (2019-01-10 19:16 UTC)

<aside class="quote no-group" data-username="NormandRbert" data-post="16" data-topic="5314">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/normandrbert/48/2975_2.png" class="avatar"> NormandRbert:</div>
<blockquote>
<p>I think it is also valuable to maintain the simple template</p>
</blockquote>
</aside>
<p>We’ll maintain both scripted module templates (the current one where GUI is created by scripting, and the new one where GUI is loaded from .ui file). ExtensionWizard module can generate modules from these templates.</p>

---

## Post #18 by @jcfr (2019-01-13 19:43 UTC)

<p>Following <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27706" rel="nofollow noopener">r27706</a>, Qt designer is expected to be packages on the three platform.</p>
<p>On Linux and Windows, it should be started using <code>./Slicer --designer</code>, on macOS, it should be directly started.</p>

---

## Post #19 by @jcfr (2019-01-13 19:44 UTC)

<p>Thinking more about it, we will have to generate a dedicated launcher (similarly to what is done for Python) because we must set variables like <code>QT_PLUGIN_PATH</code> also on macOS</p>

---

## Post #20 by @lassoan (2019-01-13 20:19 UTC)

<p>If module UI file is found then a new button “Edit UI” appears in Reload&amp;Test section of scripted modules. That button relies on a slicer.util function that uses Slicer --designer to launch the designer. So, it would be great if this would work on all platforms.</p>
<p>Currently, the button is only shown for non-installed Slicer. Now that designer is bundled with installed Slicer, too, the button should be shown for installed Slicer as well. <a class="mention" href="/u/jcfr">@jcfr</a> please make the change (I’m traveling).</p>

---

## Post #21 by @jcfr (2019-01-13 20:21 UTC)

<p>Agreed. The next set of commits should enable that.</p>

---

## Post #22 by @jcfr (2019-01-13 22:07 UTC)

<p>In addition of supporting <code>Slicer --designer</code> where the Slicer launcher is available, the cross-platform approach to start Qt designer is to run <code>SlicerDesigner</code> executable found in the <code>bin</code> directory.</p>
<p>It was needed to configure a launcher because on macOS it is not possible to run <code>./Slicer --designer</code> from an install tree.</p>
<p>Based on tomorrow nightly build, we may have to tweak the packaging of designer on Windows and macOS. After this is tested, we will initiate the 4.10.1 release process.</p>

---

## Post #23 by @adamrankin (2019-01-16 19:48 UTC)

<p>Just an FYI to all, I have recently stumbled upon <a href="https://issues.slicer.org/view.php?id=4670" rel="nofollow noopener">this</a> issue.</p>
<p>I will work on a fix, but until then, the <code>slicer.util.loadUI()</code> approach can’t load re-usable widgets from extensions.</p>

---

## Post #24 by @NormandRobert (2019-01-16 22:20 UTC)

<p>Looking at someone else’s code and noticed that they use ScriptedLoadableModuleWidget.setup(self). If one starts from the python generated module template this function is not called and the template instead has code to produce a reload button reload and test button and connections and a method to reload modules.</p>

---

## Post #25 by @pieper (2019-01-16 23:03 UTC)

<p>The older templates included the developer section, but now they use the superclass:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/4b38acadf6878ef37092443b63ab4f5b12f37c8d/Utilities/Templates/Modules/Scripted/TemplateKey.py#L42" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4b38acadf6878ef37092443b63ab4f5b12f37c8d/Utilities/Templates/Modules/Scripted/TemplateKey.py#L42" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/4b38acadf6878ef37092443b63ab4f5b12f37c8d/Utilities/Templates/Modules/Scripted/TemplateKey.py#L42</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="32" style="counter-reset: li-counter 31 ;">
<li>#</li>
<li># TemplateKeyWidget</li>
<li>#</li>
<li>
</li>
<li>class TemplateKeyWidget(ScriptedLoadableModuleWidget):</li>
<li>"""Uses ScriptedLoadableModuleWidget base class, available at:</li>
<li>https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py</li>
<li>"""</li>
<li>
</li>
<li>def setup(self):</li>
<li class="selected">  ScriptedLoadableModuleWidget.setup(self)</li>
<li>
</li>
<li>  # Instantiate and connect widgets ...</li>
<li>
</li>
<li>  #</li>
<li>  # Parameters Area</li>
<li>  #</li>
<li>  parametersCollapsibleButton = ctk.ctkCollapsibleButton()</li>
<li>  parametersCollapsibleButton.text = "Parameters"</li>
<li>  self.layout.addWidget(parametersCollapsibleButton)</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Is that not working?</p>

---

## Post #26 by @NormandRbert (2019-01-17 00:36 UTC)

<p>I ran the script more than a year ago. Could be my fault. Will check.</p>

---

## Post #27 by @NormandRobert (2019-01-18 23:17 UTC)

<p>Yep I was using a template I generated too long ago…</p>

---

## Post #28 by @NormandRbert (2019-01-28 22:24 UTC)

<p>I have thinking about UI reuse a bit more (as opposed to logic reuse).  Do you all agree that it is just a case of putting all the UI stuff in a new class… let’s call it ModuleNameWidgetUI with some constructor expecting a layout whereby said class is also designed so that MRML node(s) can be “passed in” and for each MRML “passed in” the node selection widget is not created and the “passed in” value is used instead?</p>

---

## Post #29 by @lassoan (2019-01-29 00:58 UTC)

<p>The current design is that each module offers a number of reusable widgets. The module widget is built up a couple of these widgets. This results in much simpler design and more clean interfaces than trying to make a large monolithic module widget highly configurable with lots of options.</p>
<p>Some module widgets may contain sections that are not available directly as reusable widgets (we did not have the extra time to do that or did not think that there would be a strong need for it). If you want to reuse such sections in your module then the solution is to factor out those parts as a separate widget - as it has been done several times in the past.</p>

---
