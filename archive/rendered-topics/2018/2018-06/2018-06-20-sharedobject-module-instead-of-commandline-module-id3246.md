---
topic_id: 3246
title: "Sharedobject Module Instead Of Commandline Module"
date: 2018-06-20
url: https://discourse.slicer.org/t/3246
---

# SharedObject Module instead of CommandLine Module

**Topic ID**: 3246
**Date**: 2018-06-20
**URL**: https://discourse.slicer.org/t/sharedobject-module-instead-of-commandline-module/3246

---

## Post #1 by @chaddy1004 (2018-06-20 18:00 UTC)

<p>Hello,</p>
<p>I have a cli module that I am tying to incorporate into Slicer, and it works fine on my machine, but it doesnt work that well on</p>
<p>The Log message output when it works is the following:</p>
<pre><code>Found CommandLine Module, target is  C:/s_build/SlicerGmmRegPackage/4449f7e-win-amd64- 
SlicerGmmReg-giteee0568-2018-05-25/lib/Slicer-4.9/cli-modules/GmmRegistration.exe
ModuleType: CommandLineModule
GmmRegistration command line:
</code></pre>
<p>The Log message output when it does not work is the following:</p>
<pre><code>Found SharedObject Module
ModuleType: SharedObjectModule
GmmRegistration command line: 
</code></pre>
<p>I am not sure what Shared Object is and why it is not finding the proper commandline module. I am not sure if this is the only reason why my module isn’t working on a different machine, but this difference is the biggest difference.</p>
<p>Thank you!</p>

---

## Post #2 by @Michael_Hardisty (2018-06-20 18:27 UTC)

<p>Hi Chad,</p>
<p>I suspect that the error is related to dependent shared objects (*.dll files on windows and *.so files on linux) not being present on the new machine that were present on the machine used for development.  With my knowledge of this project, i suspect this issue arose from cublas64_80 not being present.  This should be fixable by installing cuda.</p>
<p>When do you see this error?</p>
<p>You could try to resolve other dependencies using dependency walker in windows <a href="http://www.dependencywalker.com/" rel="nofollow noopener">http://www.dependencywalker.com/</a> or ldd in ubuntu</p>
<p>Michael</p>

---
