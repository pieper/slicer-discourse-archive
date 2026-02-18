# ModuleNotFoundError: No module named 'vmtk'

**Topic ID**: 15962
**Date**: 2021-02-12
**URL**: https://discourse.slicer.org/t/modulenotfounderror-no-module-named-vmtk/15962

---

## Post #1 by @Carlos_Alberto_Bulan (2021-02-12 01:46 UTC)

<p>Hello all,<br>
First of all, I would like to thank you for developing Slicer, I am a new user and it seems to be a powerful framework.<br>
I have a Python project, PP, for image processing relaying on VTK, SimpleITK &amp; VMTK.<br>
I would like to develop a Slicer extension module, SEM, encapsulating some scripts from PP.<br>
I was able to implement the modules widget, and now I have to code the SEM Logic, which consists of calls to function on scripts on PP.</p>
<p>I have a symbolic link to my PP folder in the SEM folder. This allows me to import my PP scripts.<br>
I am having troubles importing scripts from PP which depends on VMTK, for example, let’s say that I want to import “PP/scriptA.py” into my SEM module code</p>
<pre><code class="lang-python"># start SEM_sm.py-----------------------------
import PP.scriptA
# module content...
# end SEM_sm.py------------------------------

# start scriptA.py --------------------------------
import vmtk.vmtkscripts
# script content...
# end scriptA.py ---------------------------------
</code></pre>
<p>Loading the module in Slicer 4.11.20200930 r29402 / 002be18, which has the SlicerVMTK extension results in the following error.<br>
ModuleNotFoundError: No module named ‘vmtk’</p>
<p>I assume that in order to use any vmtk functionality I needed to install the SlicerVMTK extension, but I am starting to think that maybe that is not the way to use vmtk from my SEM extension.</p>
<p>Could someone point me in the right direction?<br>
Thanks,<br>
Carlos</p>

---
