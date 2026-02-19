---
topic_id: 13291
title: "Impossibility To Test For Coverage In Extensions"
date: 2020-09-02
url: https://discourse.slicer.org/t/13291
---

# Impossibility to test for coverage in extensions

**Topic ID**: 13291
**Date**: 2020-09-02
**URL**: https://discourse.slicer.org/t/impossibility-to-test-for-coverage-in-extensions/13291

---

## Post #1 by @Alex_Vergara (2020-09-02 09:13 UTC)

<p>I am trying to test the coverage in my extension. This is easily performed by<br>
<code>pytest --cov-report term --cov=Dosimetry4D</code></p>
<p>However this results in</p>
<pre><code class="lang-auto">$ pytest --cov-report term --cov=Dosimetry4D
Failed to import the site module
Traceback (most recent call last):
  File "/usr/src/Slicer-build/python-install/lib/python3.6/site.py", line 553, in &lt;module&gt;
    main()
  File "/usr/src/Slicer-build/python-install/lib/python3.6/site.py", line 539, in main
    known_paths = addusersitepackages(known_paths)
  File "/usr/src/Slicer-build/python-install/lib/python3.6/site.py", line 282, in addusersitepackages
    user_site = getusersitepackages()
  File "/usr/src/Slicer-build/python-install/lib/python3.6/site.py", line 258, in getusersitepackages
    user_base = getuserbase() # this will also set USER_BASE
  File "/usr/src/Slicer-build/python-install/lib/python3.6/site.py", line 248, in getuserbase
    USER_BASE = get_config_var('userbase')
  File "/usr/src/Slicer-build/python-install/lib/python3.6/sysconfig.py", line 601, in get_config_var
    return get_config_vars().get(name)
  File "/usr/src/Slicer-build/python-install/lib/python3.6/sysconfig.py", line 550, in get_config_vars
    _init_posix(_CONFIG_VARS)
  File "/usr/src/Slicer-build/python-install/lib/python3.6/sysconfig.py", line 421, in _init_posix
    _temp = __import__(name, globals(), locals(), ['build_time_vars'], 0)
ModuleNotFoundError: No module named '_sysconfigdata_m_linux_x86_64-linux-gnu'
ERROR: Job failed: exit code 1
FATAL: exit code 1 
</code></pre>
<p>I have found <a href="https://bugzilla.redhat.com/show_bug.cgi?id=1409177" rel="nofollow noopener">this topic</a> addressing the same issue with python 3.6. This bug is not critical but it is annoying and eventually will raise another bug.</p>
<p>Maybe this is the starting point for you to consider to move to python 3.8. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @lassoan (2020-09-02 12:24 UTC)

<p>For me, attempt to start gdb fails with the same error. From the bug report you referenced, it is not clear for me if this is solved in Python 3.8, but I’m not an experienced Linux user. It would be great if you could investigate this further, for example try to build Slicer with Python 3.8 and see if the problem is fixed.</p>

---

## Post #3 by @Alex_Vergara (2020-09-02 13:50 UTC)

<p>I tried using python 3.8.5, however the build fails at this point</p>
<pre><code class="lang-auto">CMake Error at cmake/libpython/CMakeLists.txt:442 (add_executable):
  Cannot find source file:

    /usr/src/Slicer-build/Python-3.8.5/Parser/bitset.c

  Tried extensions .c .C .c++ .cc .cpp .cxx .cu .m .M .mm .h .hh .h++ .hm
  .hpp .hxx .in .txx


CMake Error at /usr/src/Slicer-build/python-build/CMakeBuild/extensions/extension_ctypes-src/CMakeLists.txt:1 (add_library):
  Cannot find source file:

    /usr/src/Slicer-build/Python-3.8.5/Modules/_ctypes/libffi/src/closures.c

  Tried extensions .c .C .c++ .cc .cpp .cxx .cu .m .M .mm .h .hh .h++ .hm
  .hpp .hxx .in .txx


CMake Error at cmake/libpython/CMakeLists.txt:398 (add_executable):
  Cannot find source file:

    /usr/src/Slicer-build/Python-3.8.5/Modules/zipimport.c

  Tried extensions .c .C .c++ .cc .cpp .cxx .cu .m .M .mm .h .hh .h++ .hm
  .hpp .hxx .in .txx


CMake Error at /usr/src/Slicer-build/python-build/CMakeBuild/extensions/extension_ctypes-src/CMakeLists.txt:1 (add_library):
  No SOURCES given to target: extension_ctypes


CMake Error at cmake/libpython/CMakeLists.txt:398 (add_executable):
  No SOURCES given to target: _freeze_importlib


CMake Error at cmake/libpython/CMakeLists.txt:442 (add_executable):
  No SOURCES given to target: pgen


CMake Error at cmake/libpython/CMakeLists.txt:469 (add_library):
  No SOURCES given to target: libpython-shared
Call Stack (most recent call first):
  cmake/libpython/CMakeLists.txt:505 (add_libpython)


-- Build files have been written to: /usr/src/Slicer-build/python-build
make[2]: *** [python-prefix/src/python-stamp/python-configure] Error 1
make[1]: *** [CMakeFiles/python.dir/all] Error 2
make: *** [all] Error 2
</code></pre>
<p>I am trying with the freezed 3.6.12 final version as it is the same 3.6 brand with a frozen final version</p>

---

## Post #4 by @jcfr (2020-09-02 14:08 UTC)

<p>To support building Slicer against the CPython 3.7 or 3.8, we would need help to finalize this pull request</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/pull/267" target="_blank" rel="noopener">github.com/python-cmake-buildsystem/python-cmake-buildsystem</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/pull/267" target="_blank" rel="noopener">Upgrade to Python 3.8.3</a>
    </h4>

    <div class="branches">
      <code>python-cmake-buildsystem:master</code> ← <code>dand-oss:upgrade-py383</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-05-14" data-time="12:23:16" data-timezone="UTC">12:23PM - 14 May 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/dand-oss" target="_blank" rel="noopener">
          <img alt="dand-oss" src="https://avatars1.githubusercontent.com/u/1530152?v=4" class="onebox-avatar-inline" width="20" height="20">
          dand-oss
        </a>
      </div>

      <div class="lines" title="39 commits changed 17 files with 1396 additions and 1081 deletions">
        <a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/pull/267/files" target="_blank" rel="noopener">
          <span class="added">+1396</span>
          <span class="removed">-1081</span>
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

## Post #5 by @Alex_Vergara (2020-09-02 14:19 UTC)

<p>In the meanwhile, I am testing Slicer with python 3.6.12 and so far the build is ok, when I tested it I will propose a PR to upgrade to 3.6.12 which is harmless and less traumatic.</p>

---

## Post #6 by @Alex_Vergara (2020-09-03 10:23 UTC)

<p>The version with python 3.6.12 is running ok in ubuntu and docker. But the issue remains</p>
<pre><code class="lang-auto">$ pytest --cov-report term --cov=Dosimetry4D
Failed to import the site module
Traceback (most recent call last):
  File "/usr/src/Slicer-build/python-install/lib/python3.6/site.py", line 553, in &lt;module&gt;
    main()
  File "/usr/src/Slicer-build/python-install/lib/python3.6/site.py", line 539, in main
    known_paths = addusersitepackages(known_paths)
  File "/usr/src/Slicer-build/python-install/lib/python3.6/site.py", line 282, in addusersitepackages
    user_site = getusersitepackages()
  File "/usr/src/Slicer-build/python-install/lib/python3.6/site.py", line 258, in getusersitepackages
    user_base = getuserbase() # this will also set USER_BASE
  File "/usr/src/Slicer-build/python-install/lib/python3.6/site.py", line 248, in getuserbase
    USER_BASE = get_config_var('userbase')
  File "/usr/src/Slicer-build/python-install/lib/python3.6/sysconfig.py", line 601, in get_config_var
    return get_config_vars().get(name)
  File "/usr/src/Slicer-build/python-install/lib/python3.6/sysconfig.py", line 550, in get_config_vars
    _init_posix(_CONFIG_VARS)
  File "/usr/src/Slicer-build/python-install/lib/python3.6/sysconfig.py", line 421, in _init_posix
    _temp = __import__(name, globals(), locals(), ['build_time_vars'], 0)
ModuleNotFoundError: No module named '_sysconfigdata_m_linux_x86_64-linux-gnu'
ERROR: Job failed: exit code 1
</code></pre>
<p>I will skip coverage for now.<br>
You can use the docker image at: bishopwolf/slicer3d-nightly:0.4.1</p>

---

## Post #7 by @lassoan (2020-09-03 12:41 UTC)

<p>Thanks for the update. Does gdb work for you with Slicer (for example, can you launch Slicer using gdb)?</p>

---

## Post #8 by @Alex_Vergara (2020-09-04 10:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="13291">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does gdb work for you with Slicer (for example, can you launch Slicer using gdb)?</p>
</blockquote>
</aside>
<p>Unfortunately not, but the change from 3.6.7 to 3.6.12 is not supposed to add anything new, just bug corrections.</p>
<p>I have detected if you run ccmake for Slicer build that you have a WITH_COVERAGE variable</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf1ed4c38a4cfbfa69e6239f80e8bb4e9606f143.png" alt="image" data-base62-sha1="tygThNV7evzGDSjXTbTf0eNOFqj" width="385" height="228"></p>
<p>what is this supposed to do?</p>

---
