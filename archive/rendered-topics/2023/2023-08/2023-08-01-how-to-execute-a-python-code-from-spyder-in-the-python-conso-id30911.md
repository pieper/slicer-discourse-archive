# How to execute a python code from spyder in the python console that is inside Slicer?

**Topic ID**: 30911
**Date**: 2023-08-01
**URL**: https://discourse.slicer.org/t/how-to-execute-a-python-code-from-spyder-in-the-python-console-that-is-inside-slicer/30911

---

## Post #1 by @HBM (2023-08-01 15:27 UTC)

<p>I have written my own image registration code in Spyder and want to run it in 3D slicer to see if my code works. How do I do this?</p>

---

## Post #2 by @lassoan (2023-08-02 04:26 UTC)

<p>Spyder does not know how to instantiate all the application classes that you may need to use in your Slicer scripts. Instead, you can start the Slicer application, which can execute your script. You can to Slicer’s Python environment using remote Python debugging from VS Code, PyCharm, etc. as described here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerRt/SlicerDebuggingTools#python-debugger">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerRt/SlicerDebuggingTools#python-debugger" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/ee9baab79a0d0b9a81146061dfdda5630f68f1026a5d0981c47a75055591af56/SlicerRt/SlicerDebuggingTools" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerRt/SlicerDebuggingTools#python-debugger" target="_blank" rel="noopener">GitHub - SlicerRt/SlicerDebuggingTools: Extension for 3D Slicer containing...</a></h3>

  <p>Extension for 3D Slicer containing various tools for module development and debugging - GitHub - SlicerRt/SlicerDebuggingTools: Extension for 3D Slicer containing various tools for module developme...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
