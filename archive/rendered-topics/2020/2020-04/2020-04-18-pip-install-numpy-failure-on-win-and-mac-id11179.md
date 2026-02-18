# Pip install numpy failure on Win and MAC

**Topic ID**: 11179
**Date**: 2020-04-18
**URL**: https://discourse.slicer.org/t/pip-install-numpy-failure-on-win-and-mac/11179

---

## Post #1 by @tbillah (2020-04-18 21:17 UTC)

<p><code>Slicer-4.10.2</code></p>
<p>I tried to install <code>numpy</code> in another directory:</p>
<blockquote>
<p>.\PythonSlicer.exe -m pip install numpy --target \my\dir\</p>
</blockquote>
<p>After installation, the following error is observed:</p>
<pre data-code-wrap="python"><code class="lang-python">.\PythonSlicer.exe
Python 2.7.13 (default, May 16 2019, 14:27:45) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import sys
# ensure the new numpy is imported
&gt;&gt;&gt; sys.path[0]=r'\my\dir\'
&gt;&gt;&gt; import numpy as np
</code></pre>
<pre data-code-wrap="bash"><code class="lang-bash">Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "C:\Users\AppData\Roaming\NA-MIC\Extensions-28257\DiffusionQC\Lib\site-packages\numpy\__init__.py", line 142, in &lt;module&gt;
    from . import core
  File "C:\Users\AppData\Roaming\NA-MIC\Extensions-28257\DiffusionQC\Lib\site-packages\numpy\core\__init__.py", line 71, in &lt;module&gt;
    raise ImportError(msg)
ImportError:

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the multiarray numpy extension module failed.  Most
likely you are trying to import a failed build of numpy.
Here is how to proceed:
- If you're working with a numpy git repository, try `git clean -xdf`
  (removes all files not under version control) and rebuild numpy.
- If you are simply trying to use the numpy version that you have installed:
  your installation is broken - please reinstall numpy.
- If you have already reinstalled and that did not fix the problem, then:
  1. Check that you are using the Python you expect (you're using C:\Users\tashr\Downloads\Slicer-dqc\bin\python-real.exe),
     and that you have no directories in your PATH or PYTHONPATH that can
     interfere with the Python and numpy versions you're trying to use.
  2. If (1) looks fine, you can open a new issue at
     https://github.com/numpy/numpy/issues.  Please include details on:
     - how you installed Python
     - how you installed numpy
     - your operating system
     - whether or not you have multiple versions of Python installed
     - if you built from source, your compiler versions and ideally a build log

     Note: this error has many possible causes, so please don't comment on
     an existing issue about this - open a new one instead.

Original error was: DLL load failed: The specified module could not be found.
</code></pre>
<h1><a name="p-38805-additional-information-1" class="anchor" href="#p-38805-additional-information-1" aria-label="Heading link"></a>Additional information</h1>
<ul>
<li>
<p>The error does not appear to happen on Linux.</p>
</li>
<li>
<p>As <a class="mention" href="/u/lassoan">@lassoan</a> noted, I tried the same with <code>Slicer-4.11</code>, which runs Python 3 and the error didn’t occur with that. However, if there is a quick solution/suggestion to solve this, I would love to follow that.</p>
</li>
<li>
<p>The fix is necessary to fix SlicerDiffusionQC extension. <a href="http://slicer.cdash.org/testDetails.php?test=9889818&amp;build=1887395" rel="noopener nofollow ugc">Here</a> is the error log from the dashboard.</p>
</li>
</ul>

---

## Post #2 by @lassoan (2020-04-18 21:43 UTC)

<p>Slicer-4.10 will only be supported for a few more weeks, so I would suggest to test everything with latest Slicer-4.11 and let us know if you find any issues.</p>

---

## Post #3 by @jamesobutler (2020-04-19 00:51 UTC)

<p>I don’t believe numpy not being installed is your problem as this is included standard in Slicer.</p>
<p>There were other traceback errors for your specific extension such as</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Volumes/Dashboards/Stable/S-4102-E-b/DiffusionQC-build/lib/Slicer-4.10/qt-scripted-modules/GradQC.py", line 5, in &lt;module&gt;
    from gradqclib.slicerUserInteraction import slicerGUI
  File "/Volumes/Dashboards/Stable/S-4102-E-b/DiffusionQC-build/lib/Slicer-4.10/qt-scripted-modules/gradqclib/slicerUserInteraction.py", line 6, in &lt;module&gt;
    from diffusionqclib.dwi_attributes import dwi_attributes
ImportError: No module named diffusionqclib.dwi_attributes
loadSourceAsModule - Failed to load file "/Volumes/Dashboards/Stable/S-4102-E-b/DiffusionQC-build/lib/Slicer-4.10/qt-scripted-modules/GradQC.py"  as module "GradQC" !
Fail to instantiate module  "GradQC"
</code></pre>

---

## Post #4 by @tbillah (2020-04-19 01:07 UTC)

<blockquote>
<p>I don’t believe numpy not being installed is your problem as this is included standard in Slicer.</p>
</blockquote>
<p>I don’t think I said that.</p>
<blockquote>
<p>There were other traceback errors for your specific extension such as</p>
</blockquote>
<p>I am aware of them. You may see <a href="https://github.com/pnlbwh/SlicerDiffusionQC/issues/39" class="inline-onebox" rel="noopener nofollow ugc">[Win/MAC] PYTHONPATH does not appear to be set · Issue #39 · pnlbwh/SlicerDiffusionQC · GitHub</a> to know more about it. But that should not concern us since I gave an independent way of reproducing the issue.</p>

---

## Post #5 by @jamesobutler (2020-04-19 01:08 UTC)

<p>What is your motivation of installing numpy in another directory if it is already installed in regular slicer?</p>

---

## Post #6 by @tbillah (2020-04-19 01:14 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, in my experience, popular software continues supporting an old version for a while even after releasing a new one (think about python 2 and 3). While stable Slicer-4.11 release is not available, I am a little surprised to hear that Slicer leadership has already decided to discontinue supporting current stable version 4.10.</p>
<p>Where I work, we have invested significant effort to transition from 4.8 to 4.10. I think it will be hard for us to invest the same in the near future for another transition. So, it would be good to see continued support for 4.10.</p>
<p>cc <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #7 by @jamesobutler (2020-04-19 01:21 UTC)

<p>Slicer 4.10 is nearly 1.5 years old (based on originally release in Fall 2018). Since the newest version of Slicer will be released here soon, I don’t want you to waste your time developing for 4.10 when the new stable release will be out in weeks. Once it is out all responses to things regarding issues with 4.10 or earlier will earn a reply of “use the latest stable” and see how that works.</p>
<p>Python 2 is now for real EOL as of Jan 1st, so no one should continue developing with it. Even the latest numpy versions no longer support Python 2. Support was dropped for Numpy 1.17.</p>
<p>I would recommend to update software as soon as a new stable release is out or even before a new release. Keeping up with the latest development is important.</p>

---

## Post #8 by @lassoan (2020-04-19 02:26 UTC)

<p>I know that transition to new software version is always painful, but you just cannot avoid it. <a href="https://en.wikipedia.org/wiki/Software_rot">Software rot</a> is very real and happens quite quickly nowadays.</p>
<p>We try to reduce the pain by sweetening it by providing tons of new features and improvements. We also keep most things backward compatible within a major version; only release a major version with significant breaking changes once in every 5 years, and providing a migration guide.</p>
<p>I cannot spend time investigating problems in Slicer-4.10 that have been already fixed in the latest version, but you might be able to convince others to help you out. You are guaranteed to get help if you are willing to pay for commercial support (by Kitware or other companies). However, if you have money to spend on this then putting it towards transition to 4.11 (soon to be released as Slicer5) is probably a better investment.</p>

---

## Post #9 by @jamesobutler (2020-04-19 02:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="11179">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, if you have money to spend on this then putting it towards transition to 4.11 (soon to be released as Slicer5) is probably a better investment.</p>
</blockquote>
</aside>
<p>Totally agree with that. The migration guide is available at <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_backward_incompatible_changes" rel="noopener nofollow ugc">this link</a>. I will say that I often, in my own personal time and not getting paid, will try to fix issues with extensions that are having failing tests built with the Slicer preview version. If I do see an extension that is greatly out of date I won’t provide a fix. However if it is something minor based on recent updates in Slicer, I will provide fixes. You will potentially receive support from some community developers (me) if the code doesn’t fall so far behind. Here to help!</p>

---

## Post #10 by @pieper (2020-04-19 13:08 UTC)

<p>Very good discussion - I agree we need to keep moving ahead but I also feel the pain of responding to little backwards incompatibilities.  We can learn a lot from the python 2 to 3 transition, which took decades partly because it introduced a fair number of small, seemingly arbitrary changes, and people resisted it.  I hope we can avoid that kind of shift again, but the 4.10 to 4.11/5 shift in Slicer is where it hits home.</p>
<p>These changes are particularly painful for people using systems they don’t control, like centrally administered compute clusters with old OS installations and no support for virtualization or containers.  These must eventually go away so that users can have more control over their environments.</p>
<p>In any case, help people use 4.10 if we can, but using it as a platform for further development is not advised.</p>

---
