# Run a loadable module from python console

**Topic ID**: 3427
**Date**: 2018-07-09
**URL**: https://discourse.slicer.org/t/run-a-loadable-module-from-python-console/3427

---

## Post #1 by @Sanjeev_Grampurohit (2018-07-09 13:49 UTC)

<p>I want to be able to run the <strong>tractographyinteractiveseeding</strong> module from the python console. It is a loadable module which I think is why slicer.cli.run(, ) doesn’t seem to work. How do I run this module? Also, given a module, how do I know what all parameters to pass as arguments for the function?</p>

---

## Post #2 by @lassoan (2018-07-09 17:32 UTC)

<p><code>slicer.cli.run()</code> is for CLI (command-line interface) modules. Loadable modules usually observes MRML nodes, so the most common way of accessing functions from scripts is to modify MRML nodes in the scene. For triggering actions, you can call the methods of the module’s logic class.</p>
<aside class="quote no-group" data-username="Sanjeev_Grampurohit" data-post="1" data-topic="3427">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/db5fbb/48.png" class="avatar"> Sanjeev_Grampurohit:</div>
<blockquote>
<p>How do I run this module?</p>
</blockquote>
</aside>
<p>You cannot “run” a loadable module, as it already, continuously runs (observes the scene, reacts to changes in the scene or user actions on the GUI, etc). What function you would like to activate?</p>
<aside class="quote no-group" data-username="Sanjeev_Grampurohit" data-post="1" data-topic="3427">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/db5fbb/48.png" class="avatar"> Sanjeev_Grampurohit:</div>
<blockquote>
<p>given a module, how do I know what all parameters to pass as arguments for the function?</p>
</blockquote>
</aside>
<p>See <a href="http://apidocs.slicer.org/master/annotated.html">Slicer API documentation</a>, or use Python <code>help</code> function, or check source code of the module (documentation is typically in .h header files).</p>

---

## Post #3 by @Zhiy (2019-11-13 20:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="3427">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>accessing functions from scripts is to modify MRML nodes in the scene. For triggering actions, you can call the methods of the module’s logic class.</p>
</blockquote>
</aside>
<p>Can you make it concrete by taking an example?</p>
<p>How could I access a function in loadable modules in bash file?</p>

---

## Post #4 by @Zhiy (2019-11-13 20:30 UTC)

<p>In particular, the function I want to access take strings as arguments. I run into errors to pass the parameter.</p>

---

## Post #5 by @lassoan (2019-11-14 01:30 UTC)

<p>Let us know which specific method you have trouble with.</p>

---

## Post #6 by @Saima (2023-08-15 03:26 UTC)

<p>is it possible to run a scripted module from command line.</p>
<p>regards,<br>
Saima</p>

---
