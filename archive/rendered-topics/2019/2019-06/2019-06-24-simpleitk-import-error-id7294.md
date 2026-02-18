# SimpleITK import error

**Topic ID**: 7294
**Date**: 2019-06-24
**URL**: https://discourse.slicer.org/t/simpleitk-import-error/7294

---

## Post #1 by @Fernando (2019-06-24 15:31 UTC)

<p>Hi all,</p>
<p>I’ve been getting this error for a while on mac. This is from the latest nightly. Please let me know if you’d like me to report it on the issue tracker.</p>
<pre><code class="lang-auto">Python 3.6.7 (default, Jun 23 2019, 23:06:42) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
&gt;&gt;&gt; import SimpleITK
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK/SimpleITK.py", line 18, in swig_import_helper
    return importlib.import_module(mname)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "&lt;frozen importlib._bootstrap&gt;", line 994, in _gcd_import
  File "&lt;frozen importlib._bootstrap&gt;", line 971, in _find_and_load
  File "&lt;frozen importlib._bootstrap&gt;", line 955, in _find_and_load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 658, in _load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 571, in module_from_spec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 922, in create_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
ImportError: dlopen(/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK/_SimpleITK.cpython-36m-darwin.so, 1): Library not loaded: /Volumes/Dashboards/Preview/Slicer-0-build/ITK-build/lib/libITKIOBruker-5.0.1.dylib
  Referenced from: /Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK/_SimpleITK.cpython-36m-darwin.so
  Reason: image not found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK/__init__.py", line 1, in &lt;module&gt;
    from .SimpleITK import *
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK/SimpleITK.py", line 21, in &lt;module&gt;
    _SimpleITK = swig_import_helper()
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK/SimpleITK.py", line 20, in swig_import_helper
    return importlib.import_module('_SimpleITK')
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
ModuleNotFoundError: No module named '_SimpleITK'
&gt;&gt;&gt; 
</code></pre>

---

## Post #2 by @pieper (2019-06-25 22:44 UTC)

<p>Hi <a class="mention" href="/u/fernando">@Fernando</a> -</p>
<p>I can replicate your issue on mac with the nightly.  The key message seems to be missing <code>libITKIOBruker-5.0.1.dylib</code>.</p>
<p><a class="mention" href="/u/blowekamp">@blowekamp</a> is coming to project week and hopefully we can look through this together.  It seems it’s something to do with the way SimpleITK interacts with remote ITK modules with image IO functions.</p>

---

## Post #3 by @blowekamp (2019-06-26 12:40 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="7294">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I can replicate your issue on mac with the nightly. The key message seems to be missing <code>libITKIOBruker-5.0.1.dylib</code> .</p>
</blockquote>
</aside>
<p>This indicate that when when the SimpleITK library is being loaded the linker can not find the <code>libITKIOBruker-5.0.1.dylib</code> dependency. The things to check are:</p>
<ul>
<li>Does <code>libITKIOBruker-5.0.1.dylib</code> exist in the proper place in the Mac Bundle?</li>
<li>Run <code>otool -L</code> on <code>_SimpleITK.so</code> to verify that it has been fixed up correctly.</li>
</ul>
<p>Unfortunately, I seem to be having trouble getting to <a href="http://www.slicer.org" rel="noopener nofollow ugc">www.slicer.org</a> right now to download the latest nightly. I’ll be at project week on Thursday.</p>

---

## Post #4 by @pieper (2019-06-26 14:20 UTC)

<p>Thanks <a class="mention" href="/u/blowekamp">@blowekamp</a> - <a href="http://slicer.org" rel="nofollow noopener">slicer.org</a> seems to be working now for me if you want to have a look.</p>
<p>When we looked before it seems the Bruker reader is not being included or fixed up, maybe as part of the SimpleITK build step.  Do you know if that’s something that’s changed recently?  It works in Slicer 4.10.2 but that’s an older ITK.  We can look at it when you are at Project Week.</p>

---

## Post #5 by @blowekamp (2019-06-26 15:14 UTC)

<p>I was able to download both the nightly and the release versions.</p>
<p>The suffix on the SimpleITK library has changed a bit:</p>
<pre><code class="lang-auto">$ find Slicer-4.1* -name _SimpleITK\*
Slicer-4.10.2.app/Contents/lib/Python/lib/python2.7/site-packages/SimpleITK/_SimpleITK.so
Slicer-4.11.0-2019-06-24.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK/_SimpleITK.cpython-36m-darwin.so
</code></pre>
<p>And the SimpleITK library is not being fixed up at all:</p>
<pre><code class="lang-auto"> $otool -L  Slicer-4.11.0-2019-06-24.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK/_SimpleITK.cpython-36m-darwin.so

Slicer-4.11.0-2019-06-24.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK/_SimpleITK.cpython-36m-darwin.so:
	/Volumes/Dashboards/Preview/Slicer-0-build/ITK-build/lib/libITKIOBruker-5.0.1.dylib (compatibility version 1.0.0, current version 1.0.0)
	/Volumes/Dashboards/Preview/Slicer-0-build/ITK-build/lib/libITKIODCMTK-5.0.1.dylib (compatibility version 1.0.0, current version 1.0.0)
	/Volumes/Dashboards/Preview/Slicer-0-build/ITK-build/lib/libITKIOHDF5-5.0.1.dylib (compatibility version 1.0.0, current version 1.0.0)
	/Volumes/Dashboards/Preview/Slicer-0-build/ITK-build/lib/libITKIOJPEG2000-5.0.1.dylib (compatibility version 1.0.0, current version 1.0.0)
	/Volumes/Dashboards/Preview/Slicer-0-build/ITK-build/lib/libITKIOLSM-5.0.1.dylib (compatibility version 1.0.0, current version 1.0.0)

</code></pre>

---

## Post #6 by @pieper (2019-06-26 15:31 UTC)

<p>Ah - I guess it’s a python3 related change?</p>

---

## Post #7 by @blowekamp (2019-06-26 15:34 UTC)

<p>Here is a PR which should fix it:<br>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/1160" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
      <a href="https://github.com/blowekamp" target="_blank" rel="nofollow noopener">
    <img alt="blowekamp" src="https://avatars1.githubusercontent.com/u/321061?v=4" class="thumbnail onebox-avatar" width="90" height="90">
  </a>

<h4>
  <a href="https://github.com/Slicer/Slicer/pull/1160" target="_blank" rel="nofollow noopener">BUG: Fix regex matching for SimpleITK Python library fixup</a>
</h4>

<div class="date">
  by <a href="https://github.com/blowekamp" target="_blank" rel="nofollow noopener">blowekamp</a>
  on <a href="https://github.com/Slicer/Slicer/pull/1160" target="_blank" rel="nofollow noopener">03:32PM - 26 Jun 19 UTC</a>
</div>

<div class="github-commit-stats">
  <strong>1 commits</strong>
  changed <strong>1 files</strong>
  with <strong>1 additions</strong>
  and <strong>1 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>I don’t have a Mac setup for Slicer development, so I could test it. This certainly looks like the cause of the SimpleITK library not being fixed up.</p>

---

## Post #8 by @jcfr (2019-06-27 06:15 UTC)

<p>Thanks <a class="mention" href="/u/blowekamp">@blowekamp</a> for the fix <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>
<p>It has been integrated in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28347" rel="nofollow noopener">r28347</a></p>

---

## Post #9 by @fedorov (2019-06-28 11:32 UTC)

<p>Unfortunately, the problem persists in today’s nightly.</p>

---

## Post #10 by @fedorov (2019-06-28 18:28 UTC)

<p>This PR from <a class="mention" href="/u/blowekamp">@blowekamp</a> should hopefully fix the problem in the next nightly: <a href="https://github.com/Slicer/Slicer/pull/1161" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1161</a>.</p>
<p>Meanwhile, <a class="mention" href="/u/jcfr">@jcfr</a> had the idea to install SimpleITK using pip. I first removed the SimpleITK local package:</p>
<pre><code class="lang-bash">$ rm -rf ./lib/Python/lib/python3.6/site-packages/SimpleITK*
</code></pre>
<p>And then did <code>slicer.util.pip_install("SimpleITK")</code>, but after restarting Slicer, I got a crash, <a href="https://gist.github.com/fedorov/9eb533309770c61cd6d612104c20c64b" rel="nofollow noopener">here’s the stack trace</a>.</p>

---

## Post #11 by @jamesobutler (2019-06-28 19:23 UTC)

<p>I think SimpleITK from pip install is v1.2.0 which is built using ITK v4.13 even though it is ITKv5 compatible. Probably not the best since Slicer is using ITKv5</p>
<p>Check with</p>
<pre><code class="lang-python">import SimpleITK as sitk
sitk.Version().ITKVersionString()
</code></pre>

---

## Post #12 by @fedorov (2019-06-28 19:29 UTC)

<p>Yes, indeed SimpleITK from pip is 4.13.</p>
<p>I thought I asked a question along those lines to JC at the project week, and I thought the response was that packages installed via pip are installed into separate directory, along with their dependencies, so they would not conflict with any packages already installed. I guess I misunderstood the answer. I thought SimpleITK will use ITK it will bring along, and will not conflict with Slicer ITK 5.</p>

---

## Post #13 by @jamesobutler (2019-06-28 19:36 UTC)

<p>I did the following using SlicerPython directly instead of within Slicer and didn’t have any crashing on open.</p>
<pre><code class="lang-auto">./SlicerPython.exe -m pip uninstall SimpleITK
Uninstalling SimpleITK-1.2.0rc2.dev413:
  Would remove:
    c:\users\jamesbutler\appdata\local\na-mic\slicer 4.11.0-2019-06-23\lib\python\lib\site-packages\simpleitk
    c:\users\jamesbutler\appdata\local\na-mic\slicer 4.11.0-2019-06-23\lib\python\lib\site-packages\simpleitk-1.2.0rc2.dev413-py3.6.egg-info
Proceed (y / n)? 
  Successfully uninstalled SimpleITK-1.2.0rc2.dev413
./SlicerPython.exe -m pip install SimpleITK
Collecting SimpleITK
  Using cached https://files.pythonhosted.org/packages/ff/b3/2c79f38d113eb3912703261979c88ec1f640488d6d9fac391de42052e8cb/SimpleITK-1.2.0-cp36-cp36m-win_amd64.whl
Installing collected packages: SimpleITK
Successfully installed SimpleITK-1.2.0
</code></pre>
<p>There was this warning on open though.</p>
<pre><code class="lang-auto">WARNING: In C:\d\VS14-Win64-pkg\SimpleITK-build\ITK\Modules\Core\Common\src\itkObjectFactoryBase.cxx, line 664
Possible incompatible factory load:
Running itk version :
itk version 4.13.1
Loaded factory version:
itk version 5.0.0
Loading factory:
C:/Users/JamesButler/AppData/Local/NA-MIC/Slicer 4.11.0-2019-06-23/bin/../lib/Slicer-4.11/ITKFactories\MRMLIDIOPlugin.dll
</code></pre>

---

## Post #14 by @fedorov (2019-06-28 19:40 UTC)

<p>What happens when you do <code>import SimpleITK</code> in the Slicer python console? I get a crash.</p>
<p>It is also interesting that somehow I am not getting the warning that you mentioned…</p>

---

## Post #15 by @jamesobutler (2019-06-28 19:48 UTC)

<p>I get the output warning (separate window) after importing SimpleITK. Here’s the output I get. No crashing.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import SimpleITK as sitk
&gt;&gt;&gt; sitk.Version().VersionString()
'1.2.0'
&gt;&gt;&gt; sitk.Version().ITKVersionString()
'4.13'
</code></pre>

---

## Post #16 by @fedorov (2019-06-28 19:52 UTC)

<p>Hmmm… I am on Mac, and installed from this nightly package: Slicer-4.11.0-2019-06-27-macosx-amd64. Is this what you have?</p>

---

## Post #17 by @jamesobutler (2019-06-28 20:11 UTC)

<p>I’m on Windows. I tried again with Slicer-4.11.0-2019-06-27-win-amd64 and didn’t have issues.</p>

---

## Post #18 by @fedorov (2019-06-28 20:13 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> thanks a lot for your efforts, I appreciate it!</p>
<p>I will wait for the nightly package, hopefully it works tomorrow.</p>

---

## Post #19 by @lassoan (2019-06-28 22:33 UTC)

<p>As I understood from <a class="mention" href="/u/jcfr">@jcfr</a>, ITK Puthon is built statically, so there is no version conflict except the IO factory. Unfortunately, ABI incompatibility in the IO factory can break everything.</p>
<p>I guess SimpleITK will upgrade to the latest stable ITK version (5.x) at some point, which may happen more quickly if we ask for it.</p>

---

## Post #20 by @fedorov (2019-06-30 14:49 UTC)

<p>Unfortunately, as of r28349 the problem is still there.</p>

---

## Post #21 by @jcfr (2019-06-30 17:47 UTC)

<p>This should now be fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28350" rel="nofollow noopener">r28350</a></p>
<p>In a nutshell, regular expression can not be used as globbing expression.</p>

---

## Post #22 by @Fernando (2019-07-01 14:49 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="21" data-topic="7294">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>This should now be fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28350" rel="noopener nofollow ugc">r28350</a></p>
</blockquote>
</aside>
<p>It is, thanks <a class="mention" href="/u/jcfr">@jcfr</a>!</p>

---

## Post #23 by @HodaGH (2021-03-01 20:44 UTC)

<p>Hi,</p>
<p>I’m trying to use SimpleElastix within Anaconda while using Slicer (to do my registration). I feel like my problem is related to this issue here.</p>
<p>So it seems that SimpleElastix is not included in the SimpleITK of Slicer because when I import SimpleITK as sitk I get this error:</p>
<pre><code class="lang-auto">Module 'SimpleITK' has no attribute 'ElastixImageFilter'
</code></pre>
<p>How can I tell anaconda which version to use?</p>
<p>Similar to the solution here I changed  <code>_SimpleITK.so</code>  to <code>_SimpleITK*.so</code>  in my build directory for SimpleElastix installation and then did sudo python setup.py install again but it still looks for  <code>_SimpleITK.so</code>.</p>
<p>Do you have any recommendations?</p>
<p>Thanks very much.</p>

---

## Post #24 by @lassoan (2021-03-01 21:08 UTC)

<p>You can use <a href="https://github.com/lassoan/SlicerElastix">SlicerElastix</a> extension and to get Elastix binaries that are compatible with Slicer’s SimpleITK version that you can use from Python. Command-line interface may not be as convenient as Python, but it comes with nice perks, such as being able to run the registration in the background and stop it any time without impacting the application.</p>

---

## Post #25 by @HodaGH (2021-03-02 01:46 UTC)

<p>Sorry I’m a beginner so I have the SlicerElastix installed on my computer but should I import something? (I tried importing SlicerElastix but didn’t work)<br>
I also tried slicer.util.pip_install(‘SimpleElastix’) but this is the error I get (my computer is mac 10.14):</p>
<p>ERROR: Could not find a version that satisfies the requirement SimpleElastix (from versions: 0.9.1.macosx-10.11-intel, 0.10.0.post224.macosx-10.6-x86_64)<br>
ERROR: No matching distribution found for SimpleElastix</p>
<p>when I write my code in the jupyter notebook I import SimpleITK as sitk. Here’s the code:</p>
<pre><code class="lang-python">import SimpleITK as sitk

# Concatenate the ND images into one (N+1)D image
MRI_nodes = ['image1.hdr', ..., 'imageN.hdr']
vectorOfImages = sitk.VectorOfImage()

for volumenode in MRI_nodes:
    sitk_images = sitkUtils.PullVolumeFromSlicer(volumenode)
    vectorOfImages.push_back(sitk_images)
image = sitk.JoinSeries(vectorOfImages)
# Register
elastixImageFilter = sitk.ElastixImageFilter() 
elastixImageFilter.SetFixedImage(image)
elastixImageFilter.SetMovingImage(image)
elastixImageFilter.SetParameterMap(sitk.GetDefaultParameterMap('groupwise'))
elastixImageFilter.Execute()
</code></pre>
<p>**elastixImageFilter = sitk.ElastixImageFilter() → this is what gives me the error and when I use the tab after sitk. I don’t see ElastixImageFilter in the menu</p>

---

## Post #26 by @lassoan (2021-03-02 04:59 UTC)

<aside class="quote no-group" data-username="HodaGH" data-post="25" data-topic="7294">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>Sorry I’m a beginner so I have the SlicerElastix installed on my computer but should I import something? (I tried importing SlicerElastix but didn’t work)</p>
</blockquote>
</aside>
<p><a href="https://github.com/moselhy/SlicerSequenceRegistration/blob/master/SequenceRegistration/SequenceRegistration.py">Sequence registration module</a> is a good example of how to run the Elastix command-line executables from Python. These executables are not Python modules, they are command-line applications.</p>
<aside class="quote no-group" data-username="HodaGH" data-post="25" data-topic="7294">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>ERROR: Could not find a version that satisfies the requirement SimpleElastix</p>
</blockquote>
</aside>
<p>See above. SlicerElastix extension provides you Elastix command-line applications, not the Python package.</p>
<p>If you absolutely want to run Elastix via SimpleElastix then you may need to do it in an external Python environment. For example, you install anaconda, create a virtual Python environment,  in that environment you install SimpleElastix, and then from Slicer you run the registration script in that environment.</p>

---
