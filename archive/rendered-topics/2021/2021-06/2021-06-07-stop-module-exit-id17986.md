---
topic_id: 17986
title: "Stop Module Exit"
date: 2021-06-07
url: https://discourse.slicer.org/t/17986
---

# Stop module exit

**Topic ID**: 17986
**Date**: 2021-06-07
**URL**: https://discourse.slicer.org/t/stop-module-exit/17986

---

## Post #1 by @giovform (2021-06-07 02:39 UTC)

<p>Hello! Is there a way to stop a module from exiting, from inside its own exit() function? I would like to offer the user the option to cancel his exit from the module to allow him finish some operations that he may want to do before exiting.</p>
<p>For example, he clicks another module and gets a prompt: “Are you sure you want to exit the module?”</p>

---

## Post #2 by @lassoan (2021-06-07 03:58 UTC)

<p>A Python module should never call <code>exit()</code>. I would recommend to ask the developer to remove this call. If the developer does not respond to this then you can use the module in a separate process (for example, run it in a Python CLI module).</p>
<p>If you mean that you would like to write a module that closes the application gracefully (lets the user decide to actually quit or not) then you can use <code>slicer.util.mainWindow().close()</code>.</p>

---

## Post #3 by @giovform (2021-06-07 13:06 UTC)

<p>Hi Andras, I mean the <strong>exit(self)</strong> function that is called when you exit a module.</p>
<pre><code class="lang-auto">  def enter(self):
    self.interfaceFrame.enabled = False
    self.setupDialog()

  def exit(self):
    self.removeInteractorObservers()
</code></pre>
<p>The code above is from the Landmark Registration module, as an example.</p>
<p>A separate but important issue is that when I close Slicer, the <strong>dialog asking to save the scene</strong> appears <strong>before the call to</strong> <strong>exit(self)</strong> from the current module. Shouldn’t it be <strong>after</strong>? (the developer may want to do some changes on the scene within the current module <strong>exit(self)</strong>, before allowing saving the scene, and thus keep those changes)</p>

---

## Post #4 by @lassoan (2021-06-07 18:38 UTC)

<p>Once the method’s <code>exit</code> method is called, exiting the module is already in progress. You can always apply hacks, such as starting a timer in the <code>exit</code> method and switch back to the current module when the timer elapses, but the proper solution is to only display actions to the user that he is not allowed to perform. For example, you can hide the module selector toolbar.</p>
<aside class="quote no-group" data-username="giovform" data-post="3" data-topic="17986">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovform/48/4687_2.png" class="avatar"> giovform:</div>
<blockquote>
<p>A separate but important issue is that when I close Slicer, the <strong>dialog asking to save the scene</strong> appears <strong>before the call to</strong> <strong>exit(self)</strong> from the current module. Shouldn’t it be <strong>after</strong> ? (the developer may want to do some changes on the scene within the current module <strong>exit(self)</strong> , before allowing saving the scene, and thus keep those changes)</p>
</blockquote>
</aside>
<p>All persistent information must be stored in the scene. If there is really absolutely no other way than doing some last-minute node updates then you can find some hacks (e.g., <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#override-default-scene-save-dialog">override default scene save dialog</a> where you first do what you need and then call the default dialog), but I would not recommend to do this. Storing information in the scene is not required only because of scene saving but the application and all modules assume that information in the scene is up-to-date and you don’t withhold (or privately cache) anything essential.</p>

---
