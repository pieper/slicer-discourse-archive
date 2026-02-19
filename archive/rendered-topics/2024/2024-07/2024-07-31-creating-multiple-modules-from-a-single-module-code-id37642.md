---
topic_id: 37642
title: "Creating Multiple Modules From A Single Module Code"
date: 2024-07-31
url: https://discourse.slicer.org/t/37642
---

# Creating Multiple Modules from a Single Module Code

**Topic ID**: 37642
**Date**: 2024-07-31
**URL**: https://discourse.slicer.org/t/creating-multiple-modules-from-a-single-module-code/37642

---

## Post #1 by @park (2024-07-31 19:13 UTC)

<p>Hello,</p>
<p>I have created a module that works well, and I would like to replicate this task multiple times, (with multiple GUI) creating modules named module1, module2, module3, and so on. The number of replications may vary each time. Is there a method I can use for this?</p>

---

## Post #2 by @mikebind (2024-07-31 19:41 UTC)

<p>Stock Slicer is set up to show one module’s GUI interface at a time; however, you can take full control of the GUI and structure it however you want.  You could have one module which has a complex GUI which is able to change to look like multiple modules (though to Slicer it could just remain the current module in the usual Slicer interface). You might look at tabbed layouts in Qt (this could be a simple way to have it look and function like multiple variations of a module, each variation on one tab).  If you need or want more flexibility that that allows, take a look at <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">“Slicer Custom Apps”</a>.</p>
<p>I don’t know exactly what you are trying to do, but, based on what you have shared so far, I think I would start by trying to put the functionality you need into a single module and using tabs to simulate the multiple replications that you need simultaneously. If you are thinking that you need multiple different modules because you need different versions of things that regular modules only have one of, like a parameter node, it will still be easier to manage whatever you need within a single module than to try to dynamically load multiple modules simultaneously in the Slicer framework.</p>

---
