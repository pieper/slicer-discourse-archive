# Problems installing lmfit python package

**Topic ID**: 9210
**Date**: 2019-11-19
**URL**: https://discourse.slicer.org/t/problems-installing-lmfit-python-package/9210

---

## Post #1 by @Alex_Vergara (2019-11-19 08:51 UTC)

<p>I have problems installing lmfit package. Initially, it installs fine with no errors but then when importing it in a script <a href="https://github.com/lmfit/lmfit-py/issues/605" rel="nofollow noopener">this happens</a>.</p>
<p>The developers said that while installing the setup.py converts the python2 code into python3, but this was not done for me. Can you try and see if there is any problem or it is just my system?</p>
<p>just</p>
<pre><code class="lang-python">slicer.util.pip_install("lmfit")  # this works
import lmfit  # This gives an error
</code></pre>

---

## Post #2 by @jamesobutler (2019-11-19 14:23 UTC)

<p>Using Python 3.6.7 (not the one in Slicer), then installing <code>lmfit</code> has no problems as associated with the dependency <code>uncertainties</code>.  There is problems installing it within Slicer though so I would say this is a Slicer or other local problem involving the install.</p>
<p>The failure to build the wheel for the uncertainties package can happen in the local version too, but it is a result of something incorrect in pip cache. Once, I removed an old cache at “C:\Users\JamesButler\AppData\Local\pip\cache\wheels” then <code>pip install uncertainties</code> began to compile correctly again within python 3.6.7 outside of Slicer.</p>

---

## Post #3 by @Alex_Vergara (2019-11-19 14:28 UTC)

<p>I had to manually uninstall uncertainties and reinstall it again using <code>SlicerPython -m pip</code> for it to work. But this breaks automatic installation of the package from within python modules.  Using just <code>slicer.util.pip_install</code> I didn’t achieve to make it work.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/696508b59578d5e27a09a75f16cd5d073c3fec82.png" data-download-href="/uploads/short-url/f2mB7K0SOFbDYxUYIK7BIciZxjI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/696508b59578d5e27a09a75f16cd5d073c3fec82_2_690x241.png" alt="image" data-base62-sha1="f2mB7K0SOFbDYxUYIK7BIciZxjI" width="690" height="241" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/696508b59578d5e27a09a75f16cd5d073c3fec82_2_690x241.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/696508b59578d5e27a09a75f16cd5d073c3fec82.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/696508b59578d5e27a09a75f16cd5d073c3fec82.png 2x" data-dominant-color="F0F6F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">926×324 48.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Alex_Vergara (2019-11-20 10:30 UTC)

<p>Doing Slicer upgrade, breaks again this package. is there a way to make it run properly? I even installed the 2to3 package and nothing worked out.</p>

---

## Post #5 by @Alex_Vergara (2019-11-20 14:38 UTC)

<p>I have found that the lib2to3 is a core Python3 library and shall be accesible from within the python interpreter as</p>
<pre><code class="lang-python">  from setuptools.lib2to3_ex import Mixin2to3
</code></pre>
<p>However, this simple line fails in Slicer with this error</p>
<pre><code class="lang-bash">    from setuptools.lib2to3_ex import Mixin2to3
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/setuptools/lib2to3_ex.py", line 12, in &lt;module&gt;
    from lib2to3.refactor import RefactoringTool, get_fixers_from_package
ModuleNotFoundError: No module named 'lib2to3.refactor'
</code></pre>
<p>It is not enough to install the <code>2to3</code> package, the library must be compiled inside python itself, when compiling python this must be added in order for this mechanism to work.</p>

---

## Post #6 by @jcfr (2019-11-20 15:02 UTC)

<p>It may be worth investing time in improving these two packages so that python wheels are made available:</p>
<ul>
<li><a href="https://pypi.org/project/lmfit/#files">https://pypi.org/project/lmfit/#files</a></li>
<li><a href="https://pypi.org/project/uncertainties/#files">https://pypi.org/project/uncertainties/#files</a></li>
</ul>
<p>To be very specific, it doesn’t look like any file from these libraries is “compiled” (there are no C/C++/fortran/… files)</p>
<p>That said, since there are no wheel for uncertainties package, the conversion from python2 to python3 code seems to happen for every install. See <a href="https://github.com/lebigot/uncertainties/blob/2fc16f3099bcf708f8f459d960b1e4e0f3c99ee5/setup.py#L359-L360">here</a></p>
<p>If anyone has time to invest to improve these packages, I would be happy to provide guidance and reference example of packages that are successfully packaged.</p>

---

## Post #7 by @Alex_Vergara (2019-11-20 15:19 UTC)

<p>The simple line in the console</p>
<pre><code class="lang-bash">/usr/bin/2to3- -w /Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.6/site-packages/uncertainties
</code></pre>
<p>Makes the packages to work, however I have not succeeded to make an automatic run inside a script. So far I do</p>
<pre><code class="lang-python">    pip_install('lmfit')
    
    # Correct uncertainties
    e2to3lib = Path(site.getsitepackages()[0]).parent
    sys.path.append(str(e2to3lib))

    e2to3 = shutil.which("2to3")
    if not e2to3:
        pip_install('2to3')
        if sys.platform.startswith('win'):
            e2to3 = Path(shutil.which("conda")).parent / '2to3.exe' # Windows
        else:
            e2to3 = Path(shutil.which("python3")).parent / '2to3-'  # MACOS
            if not e2to3.exists:
                e2to3 = Path(shutil.which("python3")).parent / '2to3'  # Linux
        
    uncertainties = Path(site.getsitepackages()[0]) / "uncertainties"
    try:
        print(subprocess.check_output([str(e2to3), "-w", str(uncertainties)],shell=True,stderr=subprocess.STDOUT, env=startupEnvironment()))
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    import lmfit
</code></pre>
<p>But this fails with this error:</p>
<pre><code class="lang-bash">subprocess.CalledProcessError: Command '['/usr/bin/2to3-', '-w', '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.6/site-packages/uncertainties']' returned non-zero exit status 2.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/Users/alexvergaragil/Documents/GIT/dosimetry4d/Dosimetry4D/Dosimetry4D.py", line 21, in &lt;module&gt;
    from Logic import Dosimetry4DLogic, Dosimetry4DTest, dicomutils, vtkmrmlutils, vtkmrmlutilsTest, testutils, xmlutils, xmlutilsTest, nodes, nodesTest, errors, config, logging, sentry, utils, export
  File "/Users/alexvergaragil/Documents/GIT/dosimetry4d/Dosimetry4D/Logic/__init__.py", line 1, in &lt;module&gt;
    from .Dosimetry4DLogic import *
  File "/Users/alexvergaragil/Documents/GIT/dosimetry4d/Dosimetry4D/Logic/Dosimetry4DLogic.py", line 32, in &lt;module&gt;
    from Logic.fit_values import fit_values
  File "/Users/alexvergaragil/Documents/GIT/dosimetry4d/Dosimetry4D/Logic/fit_values.py", line 41, in &lt;module&gt;
    raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
RuntimeError: command '['/usr/bin/2to3-', '-w', '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.6/site-packages/uncertainties']' return with error (code 2): b'At least one file or directory argument required.\nUse --help to show usage.\n'
</code></pre>

---

## Post #8 by @lebigot (2019-11-20 16:03 UTC)

<p>If creating a wheel is not too long for someone who has never done it, I could indeed use some pointers/guidance and see if I can do this for uncertainties.</p>

---

## Post #9 by @Alex_Vergara (2019-11-21 13:31 UTC)

<p>I am studying this <a href="https://github.com/Slicer/Slicer/blob/nightly-master/SuperBuild/External_python-scipy.cmake" rel="nofollow noopener">file</a>. But I can’t make it to execute automatically the <code>setup.py</code> from the <code>uncertainties</code> project. If I just clone everything the <code>lmfit</code> is installed but <code>uncertainties</code> still has python2 looking. Basically I need that in the configuration step Slicer executes the setup.py from the project before installing it.</p>
<p>Perhaps a similar solution by just adding the 2to3 package is enough, what do you think?</p>

---

## Post #10 by @Alex_Vergara (2019-11-21 14:02 UTC)

<p>Hello Eric!</p>
<p>I think you shall take a <a href="https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/" rel="nofollow noopener">look a this</a></p>

---

## Post #11 by @Alex_Vergara (2019-11-21 14:25 UTC)

<p>Apparently we were not the only ones who need this python wheel. A <a href="https://github.com/lebigot/uncertainties/pull/108" rel="nofollow noopener">PR</a> is ready for this.</p>

---

## Post #12 by @jcfr (2019-11-21 15:26 UTC)

<blockquote>
<p>I could indeed use some pointers/guidance and see if I can do this for uncertainties.</p>
</blockquote>
<p>If you would like to setup Continuous Integration to support distribution of wheels, you may want to look at what we did for this package: <a href="https://github.com/amueller/word_cloud" class="inline-onebox">GitHub - amueller/word_cloud: A little word cloud generator in Python</a></p>

---

## Post #13 by @Alex_Vergara (2019-11-22 11:10 UTC)

<p>Most of the old python2 packages implemented an automatic conversion for python3 in the setup itself, this is made using the 2to3 tool that shall be available in the system or in the bundled python. Something like this is inside those packages <code>setup.py</code> file:</p>
<pre><code class="lang-python">...
if sys.version_info &gt;= (3, ):
        import subprocess
        subprocess.check_call(["2to3", "-w", "."])
</code></pre>
<p>this routine will fail if there is no <code>2to3</code> executable. That is why I think bundling 2to3 package inside Slicer is very good to avoid all these issues.</p>

---

## Post #14 by @lassoan (2019-11-22 14:14 UTC)

<p>It could be nice to include this 2to3 tool in Slicer if somebody has time for it, as there is a chance that it could make some modules work.</p>
<p>However, I have quite bad experience with 2to3: it obfuscated the code (made changes in a way that are not reasonable or maintainable for a human) and caused errors at several places. I would avoid relying on packages that still use 2to3’s automatic conversion to provide a Python3-compatible version because it indicates that the maintainer does not have enough time to do essential development &amp; maintenance tasks.</p>

---

## Post #15 by @jcfr (2019-11-22 17:56 UTC)

<p>I agree with <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Ideally, the project should be updated to support python3.  Indeed, in early 2020, there will be no more release of python 2.7</p>
<p>If both python2 and python3 really need to be supported, leveraging package like <a href="https://pypi.org/project/six/">https://pypi.org/project/six/</a> can be helpful.</p>
<p>To help identify, part of the code that need to be updated. When working on transitioning Slicer code based, we used <a href="https://python-future.org/futurize.html">https://python-future.org/futurize.html</a></p>
<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Python_2_to_Python_3">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Python_2_to_Python_3</a></p>

---

## Post #16 by @Alex_Vergara (2019-11-23 07:21 UTC)

<p>I agree that Slicer shall not rely on 2to3 converted packages. But it shall be user’s decision to include his own packages, and this 2to3 tool makes some packages to work, as it is in this specific case. Therefore the tool would be a great addition and it is part of the setuptools library (already bundled) as optional package.It is just to tell cmake to compile it.</p>
<p>Specifically remove <a href="https://github.com/Slicer/Slicer/blob/nightly-master/CMake/SlicerBlockInstallPython.cmake#L41" rel="nofollow noopener">this line</a>.</p>

---

## Post #17 by @lassoan (2019-11-23 14:54 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="16" data-topic="9210">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Specifically remove <a href="https://github.com/Slicer/Slicer/blob/nightly-master/CMake/SlicerBlockInstallPython.cmake#L41">this line </a>.</p>
</blockquote>
</aside>
<p>Have you tried if removing that line fixes the problem?</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Do you know why lib2to3 is excluded?</p>
<aside class="quote no-group" data-username="Alex_Vergara" data-post="16" data-topic="9210">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Therefore the tool would be a great addition</p>
</blockquote>
</aside>
<p>Regardless if Slicer supports it or not, I would not recommend on relying on a package that still have not been properly ported to Python3, as it means that the maintainer could not find 1-2 days in the last 2-3 years to upgrade. This indicates that other aspects of the package might have been neglected, too, and there may not be enough resources to keep the package alive for long.</p>

---

## Post #18 by @Alex_Vergara (2019-11-26 10:14 UTC)

<p>Removing that line makes cmake to actually install 2to3 executable and it became available in Slicer. The lmfit is now a pure python3 package with wheels (<a href="https://github.com/lmfit/lmfit-py/issues/544" rel="nofollow noopener">see here the discussion</a>) and the uncertainties package is making a switch for python3 <a href="https://github.com/lebigot/uncertainties/pull/111" rel="nofollow noopener">see here</a> and started up by making wheels <a href="https://github.com/lebigot/uncertainties/issues/106" rel="nofollow noopener">see here</a></p>

---

## Post #19 by @jcfr (2019-11-26 13:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="9210">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you know why lib2to3 is excluded?</p>
</blockquote>
</aside>
<p>Features not explicitly required have been excluded.</p>
<p>If we ship the 2to3 executable, we would have to make sure a launcher is also configured for macOS.</p>
<p>Considering that python 2 will be officially retired in few  months, I would suggest to work with maintainers to migrate their code.</p>

---

## Post #20 by @jcfr (2020-07-14 14:45 UTC)

<p>To address issue <a href="https://github.com/Slicer/Slicer/issues/5042">#5042</a>, I just  submitted this pull request:</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/5043" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5043" target="_blank" rel="noopener">BUG: Package python library "lib2to3"</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jcfr:5042-package-python-lib2to3</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-07-14" data-time="14:44:20" data-timezone="UTC">02:44PM - 14 Jul 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5043/files" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #21 by @Alex_Vergara (2020-08-05 09:40 UTC)

<p>Finally, the uncertainties package have changed to python3 and switched to a wheel packaging. This change makes the package <code>lmfit</code> to install normally through pip_install. This thread can be closed for good <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
