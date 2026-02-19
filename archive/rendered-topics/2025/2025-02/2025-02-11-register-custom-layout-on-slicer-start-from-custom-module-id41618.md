---
topic_id: 41618
title: "Register Custom Layout On Slicer Start From Custom Module"
date: 2025-02-11
url: https://discourse.slicer.org/t/41618
---

# Register custom layout on Slicer start from custom module

**Topic ID**: 41618
**Date**: 2025-02-11
**URL**: https://discourse.slicer.org/t/register-custom-layout-on-slicer-start-from-custom-module/41618

---

## Post #1 by @mikebind (2025-02-11 01:19 UTC)

<p>Hello, a module I have developed uses a few different custom layouts. Currently, these custom layouts are registered in the module widget’s setup() method.  However, when users save a scene using one of these layouts, close Slicer, and then reopen Slicer and reopen the saved scene, the custom layout is no longer available because the module widget’s setup() method has not yet run (because the user has not reopened the module in the new Slicer session yet).  To alleviate this issue, I tried moving the custom layout registration code into the module’s base class (I’m not sure what to call it, the one which derives from ScriptedLoadableModule and is the first class in the module file), but this give an error because <code>slicer.app.layoutManager</code> is currently <code>None</code> when that is run.  I’d like to keep the custom layout registration code in my module (rather than in slicerrc.py for example) to keep distribution of code to multple users simpler. Is there a way to ensure that the registration code runs after <code>slicer.app.layoutManager</code> is initialized but still before the user opens the custom module for the first time?</p>

---

## Post #2 by @cpinter (2025-02-11 10:01 UTC)

<p>I find it really strange that your module is not yet set up when the scene loading happens. I’d try connecting the function to the startup completed signal like this: <code>slicer.app.startupCompleted.connect(self.registerCustomLayouts)</code>. I normally have this connection in the <code>setup</code> function of my module, and it works like this (however, I do not open scenes directly from the shell). This probably won’t work for you because calling it directly from <code>setup</code> didn’t work, but maybe you can make this connection in the descriptor class or the constructor of your module widget. However, I think that it should not happen that the scene import occurs before loading every module, so there must be a reason for this.</p>

---

## Post #3 by @mikebind (2025-02-11 16:38 UTC)

<p>I think maybe I wasn’t clear in my question.  My module name is ContactLocator, and in my existing code, <code>registerCustomLayouts</code> is called from the <code>ContactLocatorWidget.setup()</code> method. The comments in the file (and my experience) suggests, that this code is not run until the user manually opens the module for the first time in each Slicer session.  Therefore, if the sequence of events is 1. Open Slicer, 2. Open saved scene, 3. Open ContactLocator, then even though the scene was saved with a custom layout, it is not restored on load because the new Slicer session doesn’t know about it yet, because the layouts have not been registered for this session yet, since that does not occur until step 3. If I coach users to open ContactLocator as step 2 and open the saved scene as step 3, the custom layouts are restored on load, but they often forget to do this, and it also isn’t possible to do this if Slicer is opened by double-clicking on an mrb file. So, I was trying to figure out a way to get the custom layouts to be registered when Slicer was opening, before scene loading occurs.</p>
<p>When I added a call to <code>registerCustomLayouts</code> to the <code>ContactLocator.init()</code> method, which does clearly run early in the process and before the ContactLocator GUI has been opened, it seems to run too early, because when that is run <code>slicer.app.layoutManager</code> is <code>None</code> at that point.</p>
<p>Your suggestion of registering something to run at startup completion sounds like it could work though, I will give that a try by adding that to the descriptor class and report back if that doesn’t work.</p>
<p>Reporting back, it worked!  Thanks so much for the help <a class="mention" href="/u/cpinter">@cpinter</a> !!</p>

---

## Post #4 by @cpinter (2025-02-12 12:19 UTC)

<p>Yes, makes sense. Indeed, <code>setup</code> is only called when the user switches to the module. I’m glad the <code>startupCompleted</code> approach worked!</p>

---
