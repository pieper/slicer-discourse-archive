# New Module doesn't appear in Module Navigation Interface

**Topic ID**: 958
**Date**: 2017-08-28
**URL**: https://discourse.slicer.org/t/new-module-doesnt-appear-in-module-navigation-interface/958

---

## Post #1 by @shenziheng (2017-08-28 04:21 UTC)

<p>Hello,<br>
I write a loadable module by ExtentenWizard, and then build it using cmake and visualstudio2013.<br>
After that,I add additional path to 3Dslcier.(Application Setting Dialog -&gt; Module -&gt; Add additional module path), Restart Slcier!<br>
But my custom module doesn’t appear in Module Navigation Interface.<br>
My custom module path is D:\Slicer4D\Slicer-build\lib\Slicer-4.7\qt-loadable-modules, I am sure it’s OK.<br>
I’ll appreciate it If someone can help me with the puzzle.<br>
Ziheng Shen.</p>

---

## Post #2 by @shenziheng (2017-08-28 07:24 UTC)

<p>I have solved the problem.</p>

---

## Post #3 by @lassoan (2017-08-28 15:59 UTC)

<p>What was the problem?</p>

---

## Post #4 by @shenziheng (2017-08-30 13:29 UTC)

<p>I should add the filepath of ‘lib’, not ‘Debug’.</p>

---

## Post #5 by @lassoan (2017-08-30 16:24 UTC)

<p>I guess you mean you instead of this path:</p>
<pre><code>D:\Slicer4D\Slicer-build\lib\Slicer-4.7\qt-loadable-modules
</code></pre>
<p>you had to use this:</p>
<pre><code>D:\Slicer4D\Slicer-build\lib\Slicer-4.7\qt-loadable-modules\Debug</code></pre>

---

## Post #6 by @jcfr (2017-08-30 22:40 UTC)

<p>The solution is to fix <a href="https://issues.slicer.org/view.php?id=4183">https://issues.slicer.org/view.php?id=4183</a></p>
<p>Now that CTKAppLauncherLib is a dependency of Slicer, it should be fairly straightforward.  The, updating the additional module path and restarting Slicer should allow to have all required path added the settings.</p>

---
