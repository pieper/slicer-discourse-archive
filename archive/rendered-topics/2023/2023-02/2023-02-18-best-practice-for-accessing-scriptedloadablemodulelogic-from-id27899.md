---
topic_id: 27899
title: "Best Practice For Accessing Scriptedloadablemodulelogic From"
date: 2023-02-18
url: https://discourse.slicer.org/t/27899
---

# Best practice for accessing ScriptedLoadableModuleLogic from Module?

**Topic ID**: 27899
**Date**: 2023-02-18
**URL**: https://discourse.slicer.org/t/best-practice-for-accessing-scriptedloadablemodulelogic-from-module/27899

---

## Post #1 by @p_t (2023-02-18 04:55 UTC)

<p>Operating system: Windows 10<br>
Slicer version:5.2.1</p>
<p>I have created my own ScriptedLoadableModule. It has a Module, Widget and Logic. In the documentation I see that the Module is supposed to create the Widget and Logic (<a href="https://www.slicer.org/w/img_auth.php/7/79/SlicerModulesProgrammingBeyondBasics.pdf" rel="noopener nofollow ugc">https://www.slicer.org/w/img_auth.php/7/79/SlicerModulesProgrammingBeyondBasics.pdf</a>). But I don’t think I’ve ever seen that in examples. In most cases the Module doesn’t interact with the Widget at all, both seem to get created automatically. Normally I’ve seen the Widget create the Logic, for example in the template: <a href="https://github.com/Slicer/Slicer/blob/main/Extensions/Testing/ScriptedLoadableExtensionTemplate/ScriptedLoadableModuleTemplate/ScriptedLoadableModuleTemplate.py" class="inline-onebox" rel="noopener nofollow ugc">Slicer/ScriptedLoadableModuleTemplate.py at main · Slicer/Slicer · GitHub</a>. Is the Module really supposed to create both? Is there an example of that? (or maybe that’s how it happens under the hood)</p>
<p>My issue is I have implemented onURLReceived like in the DICOM module <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOM/DICOM.py" class="inline-onebox" rel="noopener nofollow ugc">Slicer/DICOM.py at main · Slicer/Slicer · GitHub</a>, which is in the Module (I think because Widget may not have been loaded by the time URL event is triggered?). But I need to access the Logic instance to respond to the URL event (I want to access Logic instance to get parameter node which will be shared with Widget). If I create the Logic instance in the Module how do I give it to the Widget, since most of the time the Widget seems to create the Logic? I could create 2 instances of Logic and since they will share a singleton parameter node it would probably all work out but doesn’t feel right.</p>
<p>I can only find this one example using the URL event but maybe there are other examples that show how a Module can access a parameter node/Logic instance, that would be helpful.</p>

---

## Post #2 by @jamesobutler (2023-02-18 14:49 UTC)

<p>For a scripted loadable module, the module class will automatically create the widget based on the class name (MyModule, MyModuleWidget). You don’t need to add any code to the base Module class for this.</p>
<p>As mentioned on one of the slides “Current limitation: Scripted module logic is not created automatically, it has to be instantiated in the Widget class.” So as seen in the template the logic is instantiated in the widget class. (<code>self.logic = MyModuleLogic()</code>)</p>
<p>If there are issues during startup loading order, they can usually be mitigated by utilizing the startupCompleted signal. See linked thread:</p>
<aside class="quote quote-modified" data-post="4" data-topic="21814">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/import-order-in-a-scripted-loadable-module/21814/4">Import order in a scripted loadable module</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    When a module class is instantiated, it is still the module discovery phase (the application scans what modules are available, builds a dependency tree, determines in which order the modules will be initialized). Slicer application or other modules are not available yet. If you want to do something at application startup then you can connect a method to the application’s startupCompleted() signal: 

Create logic object on startupCompleted() signal and store it in the module class. This is only n…
  </blockquote>
</aside>


---

## Post #3 by @p_t (2023-02-20 14:30 UTC)

<p>Thanks for the reply James. So I understand that you are suggesting I create the Logic in the Module. But if I do that how do I pass that same Logic instance to the Widget? Since the Widget creation is automatic I don’t have access to the constructor or, as far as I can tell, the Widget instance. But I would need that if I was to pass along the Logic instance.</p>
<p>Perhaps the following thead title would be more complete: Best practice for accessing the same ScriptedLoadableModuleLogic instance from Module and Widget?</p>

---

## Post #4 by @jamesobutler (2023-02-20 19:57 UTC)

<p>An instance of the logic class is created from the init of the widget class. Typically there is nothing else in the “MyModule” class other than the info setting the title, category, contributors, etc. When you are creating a module, the custom code that you add is typically part of the Widget or Logic classes. So far I’m not aware of any typical usage that attempts to use a logic class from within a Module class. It is typically only used in Widget or Logic classes.</p>
<pre><code class="lang-python">class MyModule(ScriptedLoadableModule):
    """Uses ScriptedLoadableModule base class, available at:
    https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "ScriptedLoadableModuleTemplate"  # TODO make this more human readable by adding spaces
        self.parent.categories = ["Examples"]
        self.parent.dependencies = []
        self.parent.contributors = ["John Doe (AnyWare Corp.)"]  # replace with "Firstname Lastname (Organization)"
        self.parent.helpText = """
This is an example of scripted loadable module bundled in an extension.
It performs a simple thresholding on the input volume and optionally captures a screenshot.
"""
        self.parent.helpText += self.getDefaultModuleDocumentationLink()
        self.parent.acknowledgementText = """
This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.
and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
"""  # replace with organization, grant and thanks.

class MyModuleWidget(ScriptedLoadableModuleWidget):
  def __init__(self, parent=None):
    ScriptedLoadableModuleWidget.__init__(self, parent)
    self.logic = MyModuleLogic()

class MyModuleLogic(ScriptedLoadableModuleLogic):
...
</code></pre>

---
