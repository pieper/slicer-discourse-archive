# Problem to build Slicer?!

**Topic ID**: 7177
**Date**: 2019-06-15
**URL**: https://discourse.slicer.org/t/problem-to-build-slicer/7177

---

## Post #1 by @shahrokh (2019-06-15 15:07 UTC)

<p>Hi Dears 3DSlicer developers</p>
<p>I want to build Slicer as mentioned in the site of <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions</a>.<br>
I do the following steps:</p>
<pre><code>(base) [sn@localhost ~]$ uname --all
Linux localhost.localdomain 4.8.6-300.fc25.x86_64 #1 SMP Tue Nov 1 12:36:38 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
(base) [sn@localhost ~]$ sudo dnf list git-core svn libX11-devel libXt-devel mesa-libGL-devel mesa-libGLU-devel cmake tcl-devel python-devel qt-devel qt-webkit-devel
[sudo] password for sn: 
Last metadata expiration check: 1:17:27 ago on Sat Jun 15 17:51:12 2019.
Installed Packages
cmake.x86_64                                                       3.6.2-6.fc25                                                @fedora
git-core.x86_64                                                    2.9.3-1.fc25                                                anaconda
libX11-devel.i686                                                  1.6.5-1.fc25                                                @updates 
libX11-devel.x86_64                                                1.6.5-1.fc25                                                @updates 
libXt-devel.x86_64                                                 1.1.5-3.fc24                                                @fedora  
mesa-libGL-devel.x86_64                                            17.0.5-3.fc25                                               @updates 
mesa-libGLU-devel.x86_64                                           9.0.0-10.fc24                                               @fedora  
python-devel.x86_64                                                2.7.13-2.fc25                                               @updates 
qt-devel.x86_64                                                    1:4.8.7-18.fc25                                             @fedora  
tcl-devel.x86_64                                                   1:8.6.6-1.fc25                                              @fedora  
Available Packages
cmake.i686                                                         3.9.1-1.fc25                                                updates  
cmake.x86_64                                                       3.9.1-1.fc25                                                updates  
git-core.x86_64                                                    2.9.5-3.fc25                                                updates  
libXt-devel.i686                                                   1.1.5-3.fc24                                                fedora   
mesa-libGL-devel.i686                                              17.0.5-3.fc25                                               updates  
mesa-libGLU-devel.i686                                             9.0.0-10.fc24                                               fedora   
python-devel.i686                                                  2.7.13-3.fc25                                               updates  
python-devel.x86_64                                                2.7.13-3.fc25                                               updates  
qt-devel.i686                                                      1:4.8.7-18.fc25                                             fedora   
tcl-devel.i686                                                     1:8.6.6-1.fc25                                              fedora   
(base) [sn@localhost ~]$ sudo dnf groupinstall "Development Tools"
...
Last metadata expiration check: 1:19:38 ago on Sat Jun 15 17:51:12 2019.
Group 'Development Tools' is already installed, skipping.
Dependencies resolved.
Nothing to do.
Complete!
(base) [sn@localhost ~]$ 
</code></pre>
<p>So I have installed the packages mentioned in the site. Also, I check Qt installed usig qtdiag:</p>
<pre><code>(base) [sn@localhost Slicer-SuperBuild-Debug]$ qtdiag 
Qt 5.9.7 (x86_64-little_endian-lp64 shared (dynamic) release build; by GCC 7.3.0) on "xcb" 
OS: Fedora 25 (Workstation Edition) [linux version 4.8.6-300.fc25.x86_64]
...
</code></pre>
<p>I think that I installed Qt (5.9.7) correctly. At now, I enter the following commands:</p>
<pre><code>(base) [sn@localhost ~]$ git clone https://github.com/Slicer/Slicer.git
...
(base) [sn@localhost ~]$ mkdir Slicer-SuperBuild-Debug
(base) [sn@localhost ~]$ cd Slicer-SuperBuild-Debug/
(base) [sn@localhost Slicer-SuperBuild-Debug]$ /home/sn/cmake3.15.0-rc1/cmake-3.15.0-rc1-Linux-x86_64/bin/cmake  ../Slicer
(base) [sn@localhost Slicer-SuperBuild-Debug]$ make -j5
...
-- Up-to-date: /home/sn/Slicer-SuperBuild-Debug/python-install/lib/python3.6/zipapp.py
-- Up-to-date: /home/sn/Slicer-SuperBuild-Debug/python-install/lib/python3.6/zipfile.py
Generating grammar tables from /home/sn/Slicer-SuperBuild-Debug/python-install/lib/python3.6/lib2to3/Grammar.txt
Writing grammar tables to /home/sn/Slicer-SuperBuild-Debug/python-install/lib/python3.6/lib2to3/Grammar3.6.7.final.0.pickle
Generating grammar tables from /home/sn/Slicer-SuperBuild-Debug/python-install/lib/python3.6/lib2to3/PatternGrammar.txt
Writing grammar tables to /home/sn/Slicer-SuperBuild-Debug/python-install/lib/python3.6/lib2to3/PatternGrammar3.6.7.final.0.pickle
[ 38%] Performing configure_python_launcher step for 'python'
-- Copying '/home/sn/Slicer/Base/QTCore/Resources/Certs/Slicer.crt' to '/home/sn/Slicer-SuperBuild-Debug/Slicer-build/share/Slicer-4.11/Slicer.crt'
[ 38%] Completed 'python'
[ 39%] Built target python
Makefile:94: recipe for target 'all' failed
make: *** [all] Error 2
(base) [sn@localhost Slicer-SuperBuild-Debug]$ 
</code></pre>
<p>Why do I get this error?<br>
Please guide me.<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #2 by @pieper (2019-06-15 15:32 UTC)

<p>Hi -</p>
<p>It looks like you cut the actual error message out of the build log.  Run make again without the -j5 and it will stop on the actual error.</p>
<p>HTH</p>

---

## Post #3 by @shahrokh (2019-06-16 05:24 UTC)

<p>Hi<br>
Thanks for your guidance. I did as you said.</p>
<pre><code>(base) [sn@localhost ~]$ mkdir Slicer-SuperBuild-Debug
(base) [sn@localhost ~]$ cd Slicer-SuperBuild-Debug/
(base) [sn@localhost Slicer-SuperBuild-Debug]$ /home/sn/cmake3.15.0-rc1/cmake-3.15.0-rc1-Linux-x86_64/bin/cmake  ../Slicer
...
(base) [sn@localhost Slicer-SuperBuild-Debug]$ make
...
- Looking for CMake command CONFIGURE_PACKAGE_CONFIG_FILE
-- Looking for CMake command CONFIGURE_PACKAGE_CONFIG_FILE - found
-- Looking for CMake command WRITE_BASIC_PACKAGE_VERSION_FILE
-- Looking for CMake command WRITE_BASIC_PACKAGE_VERSION_FILE - found
-- Configuring done
-- Generating done
-- Build files have been written to: /home/sn/Slicer-SuperBuild-Debug/DCMTK-build
[ 47%] Performing build step for 'DCMTK'
[  2%] Built target ofstd
[  2%] Linking CXX executable ../../bin/ofstd_tests
../../lib/libofstd.so.3.6.3: undefined reference to `ucnv_close_57'
../../lib/libofstd.so.3.6.3: undefined reference to `ucnv_setToUCallBack_57'
../../lib/libofstd.so.3.6.3: undefined reference to `ucnv_getFromUCallBack_57'
../../lib/libofstd.so.3.6.3: undefined reference to `ucnv_open_57'
../../lib/libofstd.so.3.6.3: undefined reference to `ucnv_convertEx_57'
../../lib/libofstd.so.3.6.3: undefined reference to `u_errorName_57'
../../lib/libofstd.so.3.6.3: undefined reference to `UCNV_FROM_U_CALLBACK_STOP_57'
../../lib/libofstd.so.3.6.3: undefined reference to `UCNV_FROM_U_CALLBACK_SKIP_57'
../../lib/libofstd.so.3.6.3: undefined reference to `ucnv_getName_57'
../../lib/libofstd.so.3.6.3: undefined reference to `UCNV_TO_U_CALLBACK_STOP_57'
../../lib/libofstd.so.3.6.3: undefined reference to `ucnv_setFromUCallBack_57'
../../lib/libofstd.so.3.6.3: undefined reference to `UCNV_TO_U_CALLBACK_SKIP_57'
collect2: error: ld returned 1 exit status
ofstd/tests/CMakeFiles/ofstd_tests.dir/build.make:431: recipe for target 'bin/ofstd_tests' failed
make[5]: *** [bin/ofstd_tests] Error 1
CMakeFiles/Makefile2:353: recipe for target 'ofstd/tests/CMakeFiles/ofstd_tests.dir/all' failed
make[4]: *** [ofstd/tests/CMakeFiles/ofstd_tests.dir/all] Error 2
Makefile:140: recipe for target 'all' failed
make[3]: *** [all] Error 2
CMakeFiles/DCMTK.dir/build.make:113: recipe for target 'DCMTK-prefix/src/DCMTK-stamp/DCMTK-build' failed
make[2]: *** [DCMTK-prefix/src/DCMTK-stamp/DCMTK-build] Error 2
CMakeFiles/Makefile2:862: recipe for target 'CMakeFiles/DCMTK.dir/all' failed
make[1]: *** [CMakeFiles/DCMTK.dir/all] Error 2
Makefile:94: recipe for target 'all' failed
make: *** [all] Error 2
(base) [sn@localhost Slicer-SuperBuild-Debug]$ 
</code></pre>
<p>Please guide me.<br>
Shahrokh</p>

---

## Post #4 by @pieper (2019-06-16 19:49 UTC)

<p>Hmm, thanks for the extra information.  It looks like something in the way DCMTK is using <a href="http://userguide.icu-project.org/icufaq" rel="nofollow noopener">ICU</a>.  Maybe you need to install that too.  If that works we can update the wiki to indicate it’s a requirement.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/DCMTK/blob/patched-DCMTK-3.6.3_20180621/ofstd/libsrc/ofchrenc.cc#L56" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/DCMTK/blob/patched-DCMTK-3.6.3_20180621/ofstd/libsrc/ofchrenc.cc#L56" target="_blank" rel="nofollow noopener">commontk/DCMTK/blob/patched-DCMTK-3.6.3_20180621/ofstd/libsrc/ofchrenc.cc#L56</a></h4>
<pre class="onebox"><code class="lang-cc"><ol class="start lines" start="46" style="counter-reset: li-counter 45 ;">
<li>const unsigned int OFCharacterEncoding::CPC_OEM    = CP_OEMCP;</li>
<li>const unsigned int OFCharacterEncoding::CPC_ASCII  = 20127;</li>
<li>const unsigned int OFCharacterEncoding::CPC_Latin1 = 28591;</li>
<li>const unsigned int OFCharacterEncoding::CPC_UTF8   = CP_UTF8;</li>
<li>#endif</li>
<li>
</li>
<li>/*------------------*</li>
<li> *  implementation  *</li>
<li> *------------------*/</li>
<li>
</li>
<li class="selected">#ifdef DCMTK_ENABLE_CHARSET_CONVERSION</li>
<li>#if DCMTK_ENABLE_CHARSET_CONVERSION == DCMTK_CHARSET_CONVERSION_ICU</li>
<li>#include &lt;unicode/ucnv.h&gt;</li>
<li>#include &lt;unicode/ucnv_err.h&gt;</li>
<li>
</li>
<li>#define CONVERSION_BUFFER_SIZE 1024</li>
<li>
</li>
<li>class OFCharacterEncoding::Implementation</li>
<li>{</li>
<li>
</li>
<li>  public:</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
