# Reloading a loadable module

**Topic ID**: 14212
**Date**: 2020-10-23
**URL**: https://discourse.slicer.org/t/reloading-a-loadable-module/14212

---

## Post #1 by @Anish_Basnet (2020-10-23 12:22 UTC)

<p>Hello everyone,<br>
I’d like to know if a C++ loadable module can be loaded new without restarting the 3D slicer. I’d like to do it by clicking a PushButton in my moduleWidgetGUI.</p>

---

## Post #2 by @pieper (2020-10-23 12:33 UTC)

<p>No, we don’t support reloading C++ modules.  It would be possible in theory, but since we are usually reloading modules to fix bugs, the chances of memory corruption would probably outweigh the benefits.</p>
<p>My suggestion is to put your GUI in python for rapid development and debugging and put your C++ code into a CLI module.  Then you can rebuild and re-run the CLI without exiting Slicer.  Plus that makes the C++ logic easier to test and reuse.</p>

---

## Post #3 by @lassoan (2020-10-23 14:03 UTC)

<p>Reloading modules could be useful for quickly fixing errors found during monkey testing. However, we usually not develop C++ loadable modules this way, but we are a bit more disciplined, because C++ modules are usually infrastructure modules (that others modules rely on and therefore has to be very stable), and errors in C++ code can be easily catastrophic (make the application crash).</p>
<p>So, instead of quick iterations of randomly testing and reloading, usually we test a large part of the module using unit tests - without launching and manually operating Slicer. Application-level testing of various use cases are done using Python scripted self-tests. All these tests are also added to the list of automatic tests that are performed after each build to detect any regressions more quickly.</p>
<p>We of course still do random testing and there are a few tricks to make it more efficient. For example, we often load only an extension or a subproject in Visual Studio, so when you build, you don’t need to wait for build-check of the entire application (which can take tens of seconds) and we add a line to the .slicerrc.py file to automatically load a test scene when the application starts - saving a couple of clicks at each debugging session.</p>

---

## Post #4 by @Anish_Basnet (2020-10-28 09:08 UTC)

<p>Hello, Andras and <a class="mention" href="/u/pieper">@pieper</a> ! Thank you for the reply! I think I asked the question in a wrong way. I do not want to rebuild slicer. I’d like to restart a module with the already built Slicer. I do not want to make any changes to the C++ loadable module. All I want to do is restart the module with the same functionality (with the help of a PushButton), without making any changes and rebuilding the slicer.</p>
<p>Is it possible with some kind of extensions that already exists??</p>
<p>Best regards,<br>
Anish</p>

---

## Post #5 by @pieper (2020-10-28 13:30 UTC)

<p>In this case, all you should need to do is close the scene and the module will reset, right?</p>

---

## Post #6 by @Anish_Basnet (2020-11-05 09:37 UTC)

<p>Hello <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
I am now able to provide the functionality by removing the model Nodes and the Markup Nodes by getting them from the scene inside a qt slot and adding the new model Nodes and Markups Node inside the qt slot.</p>

---
