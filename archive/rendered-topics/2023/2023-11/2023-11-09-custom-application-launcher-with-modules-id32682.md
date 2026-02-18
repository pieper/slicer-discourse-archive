# Custom application launcher with modules

**Topic ID**: 32682
**Date**: 2023-11-09
**URL**: https://discourse.slicer.org/t/custom-application-launcher-with-modules/32682

---

## Post #1 by @1116 (2023-11-09 00:08 UTC)

<p>Hello, I am trying to create an application launcher with custom modules.<br>
I want the modules loaded in slicer already when the custom application is installed by launcher.</p>
<p>I found a similar topic [<a href="https://discourse.slicer.org/t/customized-application-launchers/564" class="inline-onebox">Customized application launchers</a>] and there is an option for custom installers that can be built without modifying anything in Slicer source code, just by tuning CMake options.</p>
<p>As I understood :</p>
<ol>
<li>the base slicer and all modules should be built already in the released version separately.</li>
<li>a .cmake file should be created or modified when building <code>PACKAGE</code> project in the CMakePredefinedTargets folder.</li>
</ol>
<p>Could you let me know which .cmake file should be modified and can I get any examples of it?</p>
<p>This is my file list for cmake build .<br>
The S dir is slicer source code and the left dirs are modules<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e307cd36d8890332643399df9068e4d2fe2320e7.png" alt="image" data-base62-sha1="wop6f1gwenX03oj6grkY6MkMvhd" width="247" height="472"></p>

---
