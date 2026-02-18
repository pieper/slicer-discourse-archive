# SimpleITK install error on mac

**Topic ID**: 9829
**Date**: 2020-01-15
**URL**: https://discourse.slicer.org/t/simpleitk-install-error-on-mac/9829

---

## Post #1 by @pieper (2020-01-15 20:32 UTC)

<p>I’m getting this error currently.  I tried deleting all SimpleITK directories and rebuilding but I hit the same thing.  When I have a chance I’ll try a completely clean build tree, but for now I’ll turn of SimpleITK in my build.</p>
<pre><code class="lang-auto">[ 81%] **Completed 'SimpleITK'**

[100%] Built target SimpleITK

[ 97%] **Performing install step for 'SimpleITK'**

-- SimpleITK: Removing 'install' log files

-- SimpleITK: SimpleITK_WORKING_DIR: /Users/pieper/slicer/latest/sbrew/SimpleITK-build/SimpleITK-build/Wrapping/Python

-- SimpleITK: /Users/pieper/slicer/latest/sbrew/python-install/bin/PythonSlicer;Packaging/setup.py;install

-- SimpleITK: Errors detected - See below.

running install

running bdist_egg

running egg_info

writing SimpleITK.egg-info/PKG-INFO

writing dependency_links to SimpleITK.egg-info/dependency_links.txt

writing top-level names to SimpleITK.egg-info/top_level.txt

reading manifest file 'SimpleITK.egg-info/SOURCES.txt'

writing manifest file 'SimpleITK.egg-info/SOURCES.txt'

installing library code to build/bdist.macosx-10.15-x86_64/egg

running install_lib

running build_py

running build_ext

copying /Users/pieper/slicer/latest/sbrew/SimpleITK-build/SimpleITK-build/Wrapping/Python/_SimpleITK.so -&gt; build/lib.macosx-10.15-x86_64-3.6/SimpleITK/_SimpleITK.cpython-36m-darwin.so

creating build/bdist.macosx-10.15-x86_64/egg

creating build/bdist.macosx-10.15-x86_64/egg/SimpleITK

copying build/lib.macosx-10.15-x86_64-3.6/SimpleITK/SimpleITK.py -&gt; build/bdist.macosx-10.15-x86_64/egg/SimpleITK

copying build/lib.macosx-10.15-x86_64-3.6/SimpleITK/__init__.py -&gt; build/bdist.macosx-10.15-x86_64/egg/SimpleITK

copying build/lib.macosx-10.15-x86_64-3.6/SimpleITK/_SimpleITK.cpython-36m-darwin.so -&gt; build/bdist.macosx-10.15-x86_64/egg/SimpleITK

byte-compiling build/bdist.macosx-10.15-x86_64/egg/SimpleITK/SimpleITK.py to SimpleITK.cpython-36.pyc

byte-compiling build/bdist.macosx-10.15-x86_64/egg/SimpleITK/__init__.py to __init__.cpython-36.pyc

creating stub loader for SimpleITK/_SimpleITK.cpython-36m-darwin.so

byte-compiling build/bdist.macosx-10.15-x86_64/egg/SimpleITK/_SimpleITK.py to _SimpleITK.cpython-36.pyc

installing package data to build/bdist.macosx-10.15-x86_64/egg

running install_data

copying /Users/pieper/slicer/latest/sbrew/SimpleITK/LICENSE -&gt; build/bdist.macosx-10.15-x86_64/egg/

copying /Users/pieper/slicer/latest/sbrew/SimpleITK/NOTICE -&gt; build/bdist.macosx-10.15-x86_64/egg/

copying /Users/pieper/slicer/latest/sbrew/SimpleITK/Readme.md -&gt; build/bdist.macosx-10.15-x86_64/egg/

copying /Users/pieper/slicer/latest/sbrew/SimpleITK-build/SimpleITK-build/ITK-5.1-NOTICE -&gt; build/bdist.macosx-10.15-x86_64/egg/

copying /Users/pieper/slicer/latest/sbrew/SimpleITK-build/SimpleITK-build/ITK-5.1-README.md -&gt; build/bdist.macosx-10.15-x86_64/egg/

creating build/bdist.macosx-10.15-x86_64/egg/EGG-INFO

copying SimpleITK.egg-info/PKG-INFO -&gt; build/bdist.macosx-10.15-x86_64/egg/EGG-INFO

copying SimpleITK.egg-info/SOURCES.txt -&gt; build/bdist.macosx-10.15-x86_64/egg/EGG-INFO

copying SimpleITK.egg-info/dependency_links.txt -&gt; build/bdist.macosx-10.15-x86_64/egg/EGG-INFO

copying SimpleITK.egg-info/top_level.txt -&gt; build/bdist.macosx-10.15-x86_64/egg/EGG-INFO

writing build/bdist.macosx-10.15-x86_64/egg/EGG-INFO/native_libs.txt

creating 'dist/SimpleITK-1.3.0.dev527-py3.6-macosx-10.15-x86_64.egg' and adding 'build/bdist.macosx-10.15-x86_64/egg' to it

removing 'build/bdist.macosx-10.15-x86_64/egg' (and everything under it)

Processing SimpleITK-1.3.0.dev527-py3.6-macosx-10.15-x86_64.egg

removing '/Users/pieper/slicer/latest/sbrew/python-install/lib/python3.6/site-packages/SimpleITK-1.3.0.dev527-py3.6-macosx-10.15-x86_64.egg' (and everything under it)

creating /Users/pieper/slicer/latest/sbrew/python-install/lib/python3.6/site-packages/SimpleITK-1.3.0.dev527-py3.6-macosx-10.15-x86_64.egg

Extracting SimpleITK-1.3.0.dev527-py3.6-macosx-10.15-x86_64.egg to /Users/pieper/slicer/latest/sbrew/python-install/lib/python3.6/site-packages

SimpleITK 1.3.0.dev527 is already the active version in easy-install.pth

Installed /Users/pieper/slicer/latest/sbrew/python-install/lib/python3.6/site-packages/SimpleITK-1.3.0.dev527-py3.6-macosx-10.15-x86_64.egg

Processing dependencies for SimpleITK==1.3.0.dev527

Searching for SimpleITK==1.3.0.dev527

Reading https://pypi.org/simple/SimpleITK/

zip_safe flag not set; analyzing archive contents...

SimpleITK.__pycache__.SimpleITK.cpython-36: module references __file__

SimpleITK.__pycache__._SimpleITK.cpython-36: module references __file__

No local packages or working download links found for SimpleITK==1.3.0.dev527

error: Could not find suitable distribution for Requirement.parse('SimpleITK==1.3.0.dev527')

CMake Error at /Users/pieper/slicer/latest/Slicer/CMake/ExternalProjectForNonCMakeProject.cmake:104 (message):

SimpleITK: install step failed with exit code '1'.

Outputs also captured in

/Users/pieper/slicer/latest/sbrew/SimpleITK_install_step_output.txt and

/Users/pieper/slicer/latest/sbrew/SimpleITK_install_step_error.txt.

Setting env. variable EP_EXECUTE_DISABLE_CAPTURE_OUTPUTS to 1 allows to

disable file capture.

Call Stack (most recent call first):

/Users/pieper/slicer/latest/sbrew/SimpleITK_install_step.cmake:3 (ExternalProject_Execute)

make[3]: *** [SimpleITK-prefix/src/SimpleITK-stamp/SimpleITK-install] Error 1

make[2]: *** [CMakeFiles/SimpleITK.dir/all] Error 2

make[1]: *** [CMakeFiles/SimpleITK.dir/rule] Error 2

make: *** [SimpleITK] Error 2

rock:sbrew pieper$
</code></pre>

---

## Post #2 by @lassoan (2020-01-15 21:06 UTC)

<p>There is a good chance that you could not properly clean your python site packages folders manually and that’s why it cannot find SimpleITK, so it would help if you could test with a clean build.</p>
<p>Clean build looks successful on the dashboard (<a href="http://slicer.cdash.org/index.php?project=SlicerPreview">http://slicer.cdash.org/index.php?project=SlicerPreview</a>) but sitkUtils test fail.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> Are you going to have time to look into this SimpleITK Mac issue? If not then maybe we should revert the ITK/SimpleITK update for now until someone has time to investigate.</p>

---

## Post #3 by @jamesobutler (2020-01-16 00:34 UTC)

<p>Sorry I don’t have access to a Mac right now to debug these Mac specific issues.</p>

---

## Post #4 by @pieper (2020-01-16 15:39 UTC)

<p>Deleting all SimpleITK and all [pP]ython* directories in the superbuild tree worked.</p>
<p>When I try to run a the MRHead through the MedianImageFilter I get this error in my local build, but the same operation work in the preview build of 2020-01-08.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd679a02c6d804b1f1ea1d4bffae325c40a1f591.png" alt="image" data-base62-sha1="vADu9EV7i9qKvCkuhtEN14bdmb7" width="483" height="285"></p>

---

## Post #5 by @lassoan (2020-01-16 16:30 UTC)

<p><a class="mention" href="/u/blowekamp">@blowekamp</a> do you have any clue what could have changed in ITK and SimpleITK to cause this problem? See change log <a href="https://github.com/Slicer/Slicer/commit/15fda09332c42bf185958ffbc14c9c18b7715a5a">here</a>.</p>

---

## Post #6 by @blowekamp (2020-01-16 18:05 UTC)

<p>Hello,</p>
<p>This error looks likely to be caused by the OSX peculiarities to  <code>dynamic_cast</code> requirements to have the symbol be from the same compilation unit. The old OSX SDKs don’t have this behavior, so that is likely the difference between Steve’s and the preview build. This is not an issue for SimpleITK’s binary distribution but is a problem with it integrated into Slicer with all the duplicate ITK symbols from different libraries floating around.</p>
<p>I suspect that it was this commit which changed the behavior is Slicer:<br>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/SimpleITK/SimpleITK/commit/ddde6bf0d262877ed3d822d160463f47d952c088" target="_blank" rel="nofollow noopener">github.com/SimpleITK/SimpleITK</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SimpleITK/SimpleITK/commit/ddde6bf0d262877ed3d822d160463f47d952c088" target="_blank" rel="nofollow noopener">Disable the explicit template instantiating by default</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2019-11-22" data-time="17:09:11" data-timezone="UTC">05:09PM - 22 Nov 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/blowekamp" target="_blank" rel="nofollow noopener">
          <img alt="blowekamp" src="https://avatars1.githubusercontent.com/u/321061?v=4" class="onebox-avatar-inline" width="20" height="20">
          blowekamp
        </a>
        
      </div>

      <div class="lines" title="changed 1 files with 5 additions and 2 deletions">
        <a href="https://github.com/SimpleITK/SimpleITK/commit/ddde6bf0d262877ed3d822d160463f47d952c088" target="_blank" rel="nofollow noopener">
          <span class="added">+5</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">But continue to use is by default with MSVC to avoid a linking error
likely due to memory limitation.</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Two things which may help the situation are:</p>
<ul>
<li>set <code>SimpleITK_EXPLICIT_INSTANTIATION=ON</code> for OSX in the Superbuild.</li>
<li>Using setting SimpleITK to use static libraries. This will ensure all SimpleITK’s symbols are consistent, but would likely ensure dynamic_cast failures if the C++ API was used.</li>
</ul>

---

## Post #7 by @lassoan (2020-01-16 18:34 UTC)

<p><a class="mention" href="/u/blowekamp">@blowekamp</a> thanks a lot for the quick and helpful response.</p>
<aside class="quote no-group" data-username="blowekamp" data-post="6" data-topic="9829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/blowekamp/48/1386_2.png" class="avatar"> blowekamp:</div>
<blockquote>
<p>This is not an issue for SimpleITK’s binary distribution but is a problem with it integrated into Slicer with all the duplicate ITK symbols from different libraries floating around</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a> worked on removing all ITK symbol duplications in Slicer binaries for several years. It is terrible to hear that there are still problems around this.</p>
<aside class="quote no-group" data-username="blowekamp" data-post="6" data-topic="9829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/blowekamp/48/1386_2.png" class="avatar"> blowekamp:</div>
<blockquote>
<ul>
<li>set <code>SimpleITK_EXPLICIT_INSTANTIATION=ON</code> for OSX in the Superbuild.</li>
<li>Using setting SimpleITK to use static libraries. This will ensure all SimpleITK’s symbols are consistent, but would likely ensure dynamic_cast failures if the C++ API was used.</li>
</ul>
</blockquote>
</aside>
<p>We use the plain ITK API for C++ API. Can we just enable SimpleITK_EXPLICIT_INSTANTIATION or there would be other consequences?</p>

---

## Post #8 by @blowekamp (2020-01-16 18:48 UTC)

<p>The logic in the above commit in SimpleITK may need to be updated to automatically turn on SimpleITK_EXPLICIT_INSTANTIATION when shared libraries are enabled. I’ll have to do some testing.</p>
<p>It would be best if Slicer always explicitly enabled the above flag, as that is the way which has been working for Slicer.</p>

---

## Post #9 by @lassoan (2020-01-16 19:14 UTC)

<aside class="quote no-group" data-username="blowekamp" data-post="8" data-topic="9829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/blowekamp/48/1386_2.png" class="avatar"> blowekamp:</div>
<blockquote>
<p>It would be best if Slicer always explicitly enabled the above flag, as that is the way which has been working for Slicer.</p>
</blockquote>
</aside>
<p>Thank you, I’ll enable this option then and we’ll see in tomorrow’s build if it indeed fixes the issue.</p>

---

## Post #10 by @blowekamp (2020-01-16 19:26 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="9829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Thank you, I’ll enable this option then and we’ll see in tomorrow’s build if it indeed fixes the issue.</p>
</blockquote>
</aside>
<p>But Steve said:</p>
<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="9829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>When I try to run a the MRHead through the MedianImageFilter I get this error in my local build, but the same operation work in the preview build of 2020-01-08.</p>
</blockquote>
</aside>
<p>So it’s OK with the preview builds, but not local builds compiled against a newer OSX SDK.</p>

---

## Post #11 by @pieper (2020-01-16 19:34 UTC)

<p>Confirmed, running this and rebuilding fixed the problem.</p>
<pre><code class="lang-auto">(cd SimpleITK-build/; cmake -D SimpleITK_EXPLICIT_INSTANTIATION:BOOL=ON .)
</code></pre>
<p>Any downsides to just adding that to the superbuild script?</p>

---

## Post #12 by @lassoan (2020-01-16 21:47 UTC)

<p>I’ve added SimpleITK_EXPLICIT_INSTANTIATION:BOOL=ON to the superbuild script (<a href="https://github.com/Slicer/Slicer/commit/506754f1becd5df717464e320c154142ccd701cb">https://github.com/Slicer/Slicer/commit/506754f1becd5df717464e320c154142ccd701cb</a><br>
).</p>

---
