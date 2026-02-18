# invoking python CLI module from command line

**Topic ID**: 3369
**Date**: 2018-07-03
**URL**: https://discourse.slicer.org/t/invoking-python-cli-module-from-command-line/3369

---

## Post #1 by @tjbertram (2018-07-03 19:03 UTC)

<p>Operating system: macOS 10.13.2 (High Sierra)<br>
Slicer version: 4.8.1<br>
Expected behavior: able to invoke python CLI module from command line<br>
Actual behavior: not able to invoke python CLI module from command line</p>
<p>Greetings - I am trying to create a python CLI module, following the specification given in<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel/Python" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel/Python</a></p>
<p>I have created the file myPythonCLImodule.py, which includes the XML and Execute() method as specified at the URL above. I have also created the directory and added the path to the settings as specified in the instruction (also in the URL above):<br>
“To create a working Python CLI module, just create a directory, put your .py file there and add the directory path to the path list in Application settings - Module settings.”</p>
<p>I then try to invoke this python CLI module from the command line, as follows<br>
./Slicer myPythonCLImodule<br>
but nothing happens.</p>
<p>My question is: How do I invoke a python CLI module from the command line?</p>
<p>I assume that one does not need to rebuild Slicer, or run Slicer from the slicer/superbuild directory, in order to run a python CLI module - is this correct?</p>
<p>I should also point out, just for reference, that the following command line is working just fine for me:<br>
./Slicer --no-main-window  --python-script /tmp/test.py<br>
This is not my problem. My problem is how to invoke my own python CLI module from the command line.</p>
<p>Thanks in advance for any assistance you can provide.</p>

---

## Post #2 by @pieper (2018-07-03 22:30 UTC)

<p>Hi -</p>
<p>Thanks for pointing that out - the documentation on that wiki page was vague.  It says Slicer3 but didn’t indicate that things are different in Slicer 4.  I added a big warning at the top with a pointer to this example with a python CLI that works with the current Slicer 4.9 (Nightly Preview) version:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics/tree/master/SlicerRadiomicsCLI">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/tree/master/SlicerRadiomicsCLI" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/AIM-Harvard/SlicerRadiomics/tree/master/SlicerRadiomicsCLI" target="_blank" rel="noopener">SlicerRadiomics/SlicerRadiomicsCLI at master · AIM-Harvard/SlicerRadiomics</a></h3>

  <p><a href="https://github.com/AIM-Harvard/SlicerRadiomics/tree/master/SlicerRadiomicsCLI" target="_blank" rel="noopener">master/SlicerRadiomicsCLI</a></p>

  <p><span class="label1">A Slicer extension to provide a GUI around pyradiomics</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
