# Error while trying to install psutil package in nightly

**Topic ID**: 8902
**Date**: 2019-10-25
**URL**: https://discourse.slicer.org/t/error-while-trying-to-install-psutil-package-in-nightly/8902

---

## Post #1 by @Alex_Vergara (2019-10-25 13:58 UTC)

<p>The error is shown by doing this</p>
<pre><code class="lang-bash">&gt;&gt;&gt; slicer.util.pip_install('psutil')
Collecting psutil
  Using cached https://files.pythonhosted.org/packages/1c/ca/5b8c1fe032a458c2c4bcbe509d1401dca9dda35c7fc46b36bb81c2834740/psutil-5.6.3.tar.gz
Building wheels for collected packages: psutil
  Building wheel for psutil (setup.py): started
  Building wheel for psutil (setup.py): finished with status 'error'
  Complete output from command /Applications/Slicer.app/Contents/bin/./python-real -u -c "import setuptools, tokenize;__file__='/private/var/folders/px/rkhksnnj0g91sxn5bvbrwzrc0000gn/T/pip-install-unz_qt1e/psutil/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /private/var/folders/px/rkhksnnj0g91sxn5bvbrwzrc0000gn/T/pip-wheel-go9_rzxt --python-tag cp36:
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib.macosx-10.11-x86_64-3.6
  creating build/lib.macosx-10.11-x86_64-3.6/psutil
  copying psutil/_pswindows.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
  copying psutil/_common.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
  copying psutil/__init__.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
  copying psutil/_psosx.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
  copying psutil/_psbsd.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
  copying psutil/_psaix.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
  copying psutil/_pslinux.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
  copying psutil/_compat.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
  copying psutil/_psposix.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
  copying psutil/_pssunos.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
  creating build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_contracts.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_connections.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/runner.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_unicode.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_misc.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_posix.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_linux.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_sunos.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/__init__.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_aix.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_process.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_bsd.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_system.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_osx.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_memory_leaks.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/test_windows.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  copying psutil/tests/__main__.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
  running build_ext
  building 'psutil._psutil_osx' extension
  creating build/temp.macosx-10.11-x86_64-3.6
  creating build/temp.macosx-10.11-x86_64-3.6/psutil
  creating build/temp.macosx-10.11-x86_64-3.6/psutil/arch
  creating build/temp.macosx-10.11-x86_64-3.6/psutil/arch/osx
  /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc -pthread -Wall -g -fPIC -DPSUTIL_POSIX=1 -DPSUTIL_VERSION=563 -DPSUTIL_OSX=1 -I/Applications/Slicer.app/Contents/lib/Python/include/python3.6m -c psutil/_psutil_common.c -o build/temp.macosx-10.11-x86_64-3.6/psutil/_psutil_common.o
  psutil/_psutil_common.c:9:10: fatal error: 'Python.h' file not found
  #include &lt;Python.h&gt;
           ^~~~~~~~~~
  1 error generated.
  error: command '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc' failed with exit status 1

  ----------------------------------------
  Failed building wheel for psutil
  Running setup.py clean for psutil
Failed to build psutil
Installing collected packages: psutil
  Running setup.py install for psutil: started
    Running setup.py install for psutil: finished with status 'error'
    Complete output from command /Applications/Slicer.app/Contents/bin/./python-real -u -c "import setuptools, tokenize;__file__='/private/var/folders/px/rkhksnnj0g91sxn5bvbrwzrc0000gn/T/pip-install-unz_qt1e/psutil/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /private/var/folders/px/rkhksnnj0g91sxn5bvbrwzrc0000gn/T/pip-record-_4ag1w90/install-record.txt --single-version-externally-managed --compile:
    running install
    running build
    running build_py
    creating build
    creating build/lib.macosx-10.11-x86_64-3.6
    creating build/lib.macosx-10.11-x86_64-3.6/psutil
    copying psutil/_pswindows.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
    copying psutil/_common.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
    copying psutil/__init__.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
    copying psutil/_psosx.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
    copying psutil/_psbsd.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
    copying psutil/_psaix.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
    copying psutil/_pslinux.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
    copying psutil/_compat.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
    copying psutil/_psposix.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
    copying psutil/_pssunos.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil
    creating build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_contracts.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_connections.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/runner.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_unicode.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_misc.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_posix.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_linux.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_sunos.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/__init__.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_aix.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_process.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_bsd.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_system.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_osx.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_memory_leaks.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/test_windows.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    copying psutil/tests/__main__.py -&gt; build/lib.macosx-10.11-x86_64-3.6/psutil/tests
    running build_ext
    building 'psutil._psutil_osx' extension
    creating build/temp.macosx-10.11-x86_64-3.6
    creating build/temp.macosx-10.11-x86_64-3.6/psutil
    creating build/temp.macosx-10.11-x86_64-3.6/psutil/arch
    creating build/temp.macosx-10.11-x86_64-3.6/psutil/arch/osx
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc -pthread -Wall -g -fPIC -DPSUTIL_POSIX=1 -DPSUTIL_VERSION=563 -DPSUTIL_OSX=1 -I/Applications/Slicer.app/Contents/lib/Python/include/python3.6m -c psutil/_psutil_common.c -o build/temp.macosx-10.11-x86_64-3.6/psutil/_psutil_common.o
    psutil/_psutil_common.c:9:10: fatal error: 'Python.h' file not found
    #include &lt;Python.h&gt;
             ^~~~~~~~~~
    1 error generated.
    error: command '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc' failed with exit status 1

    ----------------------------------------
Command "/Applications/Slicer.app/Contents/bin/./python-real -u -c "import setuptools, tokenize;__file__='/private/var/folders/px/rkhksnnj0g91sxn5bvbrwzrc0000gn/T/pip-install-unz_qt1e/psutil/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /private/var/folders/px/rkhksnnj0g91sxn5bvbrwzrc0000gn/T/pip-record-_4ag1w90/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /private/var/folders/px/rkhksnnj0g91sxn5bvbrwzrc0000gn/T/pip-install-unz_qt1e/psutil/
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2057, in pip_install
    logProcessOutput(proc)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2010, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'psutil']' returned non-zero exit status 1.
&gt;&gt;&gt; 
</code></pre>
<p>Somehow the SlicerPython has not the required devel headers in the python environment. This may result in more packages not being able to install.</p>

---

## Post #2 by @Sam_Horvath (2019-10-28 16:20 UTC)

<p>I haven’t had time to look into this in depth, but this error is not occurring in the most recent windows installer.</p>

---

## Post #3 by @lassoan (2019-10-28 17:07 UTC)

<p>Do you only have problems with psutil or with other packages, too?<br>
Have you installed Python development packages that are needed for building python wheels?</p>

---

## Post #4 by @Alex_Vergara (2019-10-28 19:51 UTC)

<p>I just installed the Slicer nightly, then psutil is not installing, maybe a default installation of development packages is enough to solve this issue. But how to install them from Slicer itself? Is not like you have much options for the environment.</p>

---

## Post #5 by @lassoan (2019-10-28 21:12 UTC)

<p>Is it usual for Python to build packages on MacOS? Or does it happen only for psutil?</p>
<p>Can other Python distributions build psutil on your computer?</p>

---

## Post #6 by @Alex_Vergara (2019-10-28 21:18 UTC)

<p>psutil needs to be built in every distro and in every os, it is the same for some fancy packages that use cython capabilities in general (mostly all the really cool ones ;).</p>

---

## Post #7 by @lassoan (2019-10-28 21:48 UTC)

<p>psutil is not built from source on Windows (downloaded from <a href="https://files.pythonhosted.org/packages/86/91/f15a3aae2af13f008ed95e02292d1a2e84615ff42b7203357c1c0bbe0651/psutil-5.6.3-cp36-cp36m-win_amd64.whl">here</a>) but maybe binary is not available for some linux/Mac environments.</p>
<p>Can other Python distributions build psutil on your computer?</p>
<p>Do you have issues with building other Python packages from source on your computer, either in Slicer or other Python environments?</p>
<p>If the problem is only with psutil then I would consider it very low priority (as a medical image computing application should not need to use so low-level APIs), but if this is a more general issue then it may worth a closer look.</p>

---

## Post #8 by @pieper (2019-10-28 22:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="8902">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If the problem is only with psutil then I would consider it very low priority (as a medical image computing application should not need to use so low-level APIs), but if this is a more general issue then it may worth a closer look.</p>
</blockquote>
</aside>
<p>A couple things:</p>
<p>I see that psutil has a nice abstraction for getting free memory, and that could be useful when working with large data (e.g. before loading a huge dataset).  I’m not aware of other cross-platform options for that.<br>
<a href="https://psutil.readthedocs.io/en/latest/#memory" class="onebox" target="_blank" rel="noopener">https://psutil.readthedocs.io/en/latest/#memory</a></p>
<p>Also it would be good to define which python package “just work” on all platforms and what ones require specific installation steps.  I tried a python package the other day on mac and it failed to install due to a build issue even though I have a complete developer environment.</p>

---

## Post #9 by @jamesobutler (2019-10-28 22:54 UTC)

<p>Psutil has prebuilt wheels (available for Windows) hosted on pypi, however no wheels for Mac or Linux which is why the wheel is having to be built.</p>
<p>psutil-5.6.3-cp36-cp36m-win32.whl<br>
psutil-5.6.3-cp36-cp36m-win_amd64.whl<br>
[<a href="https://pypi.org/project/psutil/#files" rel="nofollow noopener">source</a>]</p>
<p>I would suggest looking into psutil to understand the requirements to build and see if others have problems. Just a quick look that others sometimes struggle to build psutil on mac. <a href="https://github.com/giampaolo/psutil/issues/1572" rel="nofollow noopener">https://github.com/giampaolo/psutil/issues/1572</a></p>

---
