# Pure python extension: Packaging w/o CMAKE/Visual Studio, etc?

**Topic ID**: 10169
**Date**: 2020-02-08
**URL**: https://discourse.slicer.org/t/pure-python-extension-packaging-w-o-cmake-visual-studio-etc/10169

---

## Post #1 by @stephan (2020-02-08 21:41 UTC)

<p>Hi everybody,</p>
<p>I have a rather simple extension module that was based on the Extension Wizard. So it’s pure python, nothing that need to be compiled. However, it seems that in order to package the extension into the .zip file that can then be installed “from file” through the extension manager, on needs to “compile” it using Visual Studio anyway? At least that’s how I understood <a href="https://discourse.slicer.org/t/extensions-how-to-create-package-file/6079">this thread</a>.<br>
I would prefer not to install Visual Studio and figure out how to compile the Slicer source in the first place if there is an easier way.<br>
Maybe there’s documentation what needs to go into that zip file for the extension manager to install it correctly? So I could simply create that zip file manually?</p>
<p>Thank you</p>
<p>Stephan</p>

---

## Post #2 by @pieper (2020-02-08 22:19 UTC)

<p>If you plan to submit this to the extension catalog then you don’t need to compile it yourself, the factory will do that.  The CMake infrastructure is mostly to be sure it gets packaged correctly.</p>
<p>If your goal is just to have easy installation instructions outside the extension manager, then you can just add the single python directory to the module paths in the application settings and it will be discovered when you restart slicer.</p>

---
