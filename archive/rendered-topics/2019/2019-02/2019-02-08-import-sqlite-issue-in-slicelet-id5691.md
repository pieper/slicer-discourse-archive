# Import sqlite issue in Slicelet

**Topic ID**: 5691
**Date**: 2019-02-08
**URL**: https://discourse.slicer.org/t/import-sqlite-issue-in-slicelet/5691

---

## Post #1 by @Ehouarn (2019-02-08 14:51 UTC)

<p>Hi Slicer community,</p>
<p>I am pretty new in Slicer extensions development,<br>
I try to create a complete graphic interface based on Slicelet concept to interface an existing software.<br>
This software have a lot of dependencies, an among other, dependency to sqlite3, for patient database management.<br>
when i try to import sqlite from the slicelet, i have an import error (that does not appear when launch the soft outside Slicer):<br>
Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages/sqlite/<strong>init</strong>.py", line 1, in :<br>
ImportError: No module named _sqlite</p>
<p>It seems that sqlite is embedded in Slicer, as i see the package: lib/Python/lib/python2.7/site-packages/sqlite<br>
I tried to install the libsqlite3-dev package, change PYTHONPATH in a lot of ways, with no success.</p>
<p>I did not find any publication on this issue in the web,<br>
do i miss something in my configuration, installation or link between Slicer and my software?</p>
<p>Configuration:<br>
Ubuntu 16.0<br>
Slicer 4.8.1 from Slicer web site<br>
Python 2.7<br>
sqlite 3.11</p>
<p>Thanks in advance for your help,<br>
Ehouarn</p>

---

## Post #2 by @pieper (2019-02-08 19:19 UTC)

<p>That’s odd, yes.  I can <code>import sqlite3</code> on mac but not on windows or linux.  Perhaps it’s a packaging thing related to the leading underscore.  You may want to have a look at the packaging scripts to see if you can fix it (or maybe manually copy things around) but also be aware that there’s going to be a transition to Python 3, within a few weeks I’m told, so things might change at that point.</p>

---

## Post #3 by @Ehouarn (2019-02-12 13:08 UTC)

<p>Hi Steve,</p>
<p>Thanks for the quick response,<br>
The mac version own sqlite3.so file in lib/Python/lib/python2.7/lib-dynload, and not the linux one, the problem come from this point i think.</p>
<p>Sqlite is found after copy the lib, but i am running in trouble with the USC2 vs UCS4 encoding.<br>
I noticed at least one thread on the forum on that subject, i will have a look in the way i can launch SlicerPython directly.</p>
<p>Ehouarn</p>

---

## Post #4 by @Alex_Vergara (2019-12-11 15:31 UTC)

<p>I can confirm the issue remains on Slicer nightly</p>
<p><code>import sqlite3</code> works on mac but not on windows nor linux, does anyone have found a solution?</p>

---

## Post #5 by @lassoan (2019-12-11 16:47 UTC)

<p>Probably sqlite support has to be explicitly enabled when Slicer builds Python. Could you try if adding SQLite include and library paths to External_python.cmake solves the issue?</p>
<pre><code class="lang-nohighlight">  USE_SYSTEM_SQLITE3=ON|OFF     (defaults to ON)
    If set to OFF, no attempt to detect SQLITE3 libraries will be done.
    Associated python extensions are: SQLITE3
    Following CMake variables can manually be set: SQLITE3_INCLUDE_PATH, SQLITE3_LIBRARY
</code></pre>
<p>(from (slicer-build-dir)/python/README.rst)</p>

---

## Post #6 by @Alex_Vergara (2019-12-13 10:20 UTC)

<p>In Linux the problem is solved by installing <code>libsqlite-dev</code> (Ubuntu) before building the whole Slicer, I see no solution for windows (perhaps bundling <a href="https://www.sqlitetutorial.net/download-install-sqlite/" rel="nofollow noopener">this sqlite version</a> is enough).</p>
<p>The point is that Slicer shall always have sqlite3 capabilities, even when it is not installed. It should be possible to install sqlite libraries after building Slicer and it shall work. Even better is to have already bundled an own sqlite3 library, so your already bundled python does not depend on system if it is not installed.</p>

---

## Post #7 by @Alex_Vergara (2019-12-19 14:28 UTC)

<p>Is there any perspective on this topic?</p>

---

## Post #8 by @lassoan (2019-12-19 14:36 UTC)

<p>I agree that it would be useful to build Python with sqlite support.</p>
<p>Could you add sqlite build to Slicer superbuild (similarly to how it is done for curl, jsoncpp, libarchive, rapidjson, teem, zlib, etc.)?</p>
<p>On linux we could pick it from from some dev packages, but it would be better to build on our own because it is needed on Windows anyway and this way we could guarantee that the same sqlite features are enabled on all platforms.</p>

---

## Post #9 by @Alex_Vergara (2019-12-19 15:25 UTC)

<p>This is a little hard to do, LOL. I have tried and I must invoke curl to download the <a href="https://www.sqlite.org/src/tarball/sqlite.tar.gz" rel="nofollow noopener">sqlite sources</a> or <a href="https://www.sqlite.org/src/zip/sqlite.zip" rel="nofollow noopener">these for windows</a>. Then invoke zlib to extract the sources and create the respective folders inside the Superbuild. Finally invoke cmake on them:</p>
<p>This for linux/mac</p>
<pre><code class="lang-auto">    tar xzf sqlite.tar.gz    ;#  Unpack the source tree into "sqlite"
    mkdir bld                ;#  Build will occur in a sibling directory
    cd bld                   ;#  Change to the build directory
    ../sqlite/configure      ;#  Run the configure script
    make                     ;#  Run the makefile.
    make sqlite3.c           ;#  Build the "amalgamation" source file
    make test                ;#  Run some tests (requires Tcl)
</code></pre>
<p>And this for windows:</p>
<pre><code class="lang-auto">    mkdir bld
    cd bld
    nmake /f Makefile.msc TOP=..\sqlite
    nmake /f Makefile.msc sqlite3.c TOP=..\sqlite
    nmake /f Makefile.msc sqlite3.dll TOP=..\sqlite
    nmake /f Makefile.msc sqlite3.exe TOP=..\sqlite
    nmake /f Makefile.msc test TOP=..\sqlite
</code></pre>
<p>In the case of windows I must also invoke nmake, which is the VisualStudio that it is used inside Slicer compilation. I am no Windows expert.</p>

---

## Post #10 by @jcfr (2019-12-19 15:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="5691">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>to build on our own because it is needed on Windows anyway and this way we could guarantee that the same sqlite features are enabled on all platforms.</p>
</blockquote>
</aside>
<p>That is the way to go. <a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> if you would like to help maintain it, here is what could be done:</p>
<ul>
<li>fork <a href="https://github.com/mackyle/sqlite" class="inline-onebox">GitHub - mackyle/sqlite: Unofficial git mirror of SQLite sources (see link for build instructions)</a> into GitHub Slicer organization</li>
<li>add <code>welcome</code> branch similar to <a href="https://github.com/Slicer/VTK/tree/welcome">this one</a>
<ul>
<li>the README file would document how to update the version of sqlite</li>
</ul>
</li>
<li>create a branch called <code>slicer-3.30.1-2019-10-10-350f1fc</code>  where you would add a <code>CMakeLists.txt</code> allowing to build the amalgamated</li>
</ul>

---

## Post #11 by @Alex_Vergara (2019-12-19 17:11 UTC)

<p>Is not that easy, that repository is not cmake compliant</p>
<pre><code class="lang-auto">PhaseScriptExecution CMake\ Rules /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/Slicer.build/Debug/sqlite.build/Script-06CD2C3DA9D14B5E981BB91D.sh
    cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/Slicer
    /bin/sh -c /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/Slicer.build/Debug/sqlite.build/Script-06CD2C3DA9D14B5E981BB91D.sh

echo "Creating directories for 'sqlite'"
Creating directories for 'sqlite'
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E make_directory /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E make_directory /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E make_directory /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E make_directory /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/tmp
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E make_directory /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src/sqlite-stamp/Debug
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E make_directory /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E make_directory /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src/sqlite-stamp
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E touch /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src/sqlite-stamp/Debug/sqlite-mkdir
echo "Performing download step (git clone) for 'sqlite'"
Performing download step (git clone) for 'sqlite'
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -P /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/tmp/sqlite-gitclone.cmake
Clonage dans 'sqlite'...
Note : basculement sur 'version-3.30.1'.

Vous êtes dans l'état « HEAD détachée ». Vous pouvez visiter, faire des modifications
expérimentales et les valider. Il vous suffit de faire un autre basculement pour
abandonner les commits que vous faites dans cet état sans impacter les autres branches

Si vous voulez créer une nouvelle branche pour conserver les commits que vous créez,
il vous suffit d'utiliser l'option -c de la commande switch comme ceci :

  git switch -c &lt;nom-de-la-nouvelle-branche&gt;

Ou annuler cette opération avec :

  git switch -

Désactivez ce conseil en renseignant la variable de configuration advice.detachedHead à false

HEAD est maintenant sur 350f1fc6f Version 3.30.1
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -E touch /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src/sqlite-stamp/Debug/sqlite-download
echo "Performing update step for 'sqlite'"
Performing update step for 'sqlite'
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -P /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/tmp/sqlite-gitupdate.cmake
echo "No patch step for 'sqlite'"
No patch step for 'sqlite'
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E echo_append
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E touch /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src/sqlite-stamp/Debug/sqlite-patch
echo "Performing configure step for 'sqlite'"
Performing configure step for 'sqlite'
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -GXcode -C/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/tmp/sqlite-cache-Debug.cmake /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite
loading initial cache file /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/tmp/sqlite-cache-Debug.cmake
CMake Error: The source directory "/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.
make: *** [/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src/sqlite-stamp/Debug/sqlite-configure] Error 1
Command /bin/sh failed with exit code 2
</code></pre>

---

## Post #12 by @lassoan (2019-12-19 17:13 UTC)

<p>That’s why Jc recommended to fork the repository and add a CMakeLists.txt file there. I think this repository may be usable as is: <a href="https://github.com/azadkuh/sqlite-amalgamation">https://github.com/azadkuh/sqlite-amalgamation</a> (already CMake-ified sqlite).</p>

---

## Post #13 by @Alex_Vergara (2019-12-19 17:19 UTC)

<p>Indeed, success in the first try</p>
<pre><code class="lang-auto">
Showing Recent Messages

Prepare build
note: Using legacy build system


Build target ZERO_CHECK of project Slicer with configuration Debug

PhaseScriptExecution CMake\ Rules /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/Slicer.build/Debug/ZERO_CHECK.build/Script-E0568E519E264736B9DC7D4B.sh
    cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/Slicer
    /bin/sh -c /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/Slicer.build/Debug/ZERO_CHECK.build/Script-E0568E519E264736B9DC7D4B.sh

echo ""

make -f /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/CMakeScripts/ReRunCMake.make
make[1]: `/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/CMakeFiles/cmake.check_cache' is up to date.


Build target sqlite of project Slicer with configuration Debug

PhaseScriptExecution CMake\ Rules /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/Slicer.build/Debug/sqlite.build/Script-582CB80BE60D49A6859460AE.sh
    cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/Slicer
    /bin/sh -c /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/Slicer.build/Debug/sqlite.build/Script-582CB80BE60D49A6859460AE.sh

echo "Performing download step (git clone) for 'sqlite'"
Performing download step (git clone) for 'sqlite'
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -P /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/tmp/sqlite-gitclone.cmake
Clonage dans 'sqlite'...
Note : basculement sur '3.30.1'.

Vous êtes dans l'état « HEAD détachée ». Vous pouvez visiter, faire des modifications
expérimentales et les valider. Il vous suffit de faire un autre basculement pour
abandonner les commits que vous faites dans cet état sans impacter les autres branches

Si vous voulez créer une nouvelle branche pour conserver les commits que vous créez,
il vous suffit d'utiliser l'option -c de la commande switch comme ceci :

  git switch -c &lt;nom-de-la-nouvelle-branche&gt;

Ou annuler cette opération avec :

  git switch -

Désactivez ce conseil en renseignant la variable de configuration advice.detachedHead à false

HEAD est maintenant sur 180e629 update to 3030001 (3.30.1)
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -E touch /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src/sqlite-stamp/Debug/sqlite-download
echo "Performing update step for 'sqlite'"
Performing update step for 'sqlite'
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -P /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/tmp/sqlite-gitupdate.cmake
echo "No patch step for 'sqlite'"
No patch step for 'sqlite'
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E echo_append
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E touch /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src/sqlite-stamp/Debug/sqlite-patch
echo "Performing configure step for 'sqlite'"
Performing configure step for 'sqlite'
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -GXcode -C/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/tmp/sqlite-cache-Debug.cmake /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite
loading initial cache file /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/tmp/sqlite-cache-Debug.cmake
-- The C compiler identification is AppleClang 11.0.0.11000033
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -E touch /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src/sqlite-stamp/Debug/sqlite-configure
echo "Performing build step for 'sqlite'"
Performing build step for 'sqlite'
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake --build . --config Debug
User defaults from command line:
    HideShellScriptEnvironment = YES

Build settings from command line:
    TOOLCHAINS = com.apple.dt.toolchain.XcodeDefault

Prepare build
note: Using legacy build system
=== BUILD AGGREGATE TARGET ZERO_CHECK OF PROJECT sqlite3 WITH CONFIGURATION Debug ===

Check dependencies

Write auxiliary files
write-file /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/ZERO_CHECK.build/Script-0ABDB98C97844771B6FC8110.sh
chmod 0755 /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/ZERO_CHECK.build/Script-0ABDB98C97844771B6FC8110.sh

PhaseScriptExecution CMake\ Rules /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/ZERO_CHECK.build/Script-0ABDB98C97844771B6FC8110.sh
    cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite
    /bin/sh -c /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/ZERO_CHECK.build/Script-0ABDB98C97844771B6FC8110.sh
echo ""

make -f /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/CMakeScripts/ReRunCMake.make
make[2]: `/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/CMakeFiles/cmake.check_cache' is up to date.

=== BUILD TARGET sqlite3 OF PROJECT sqlite3 WITH CONFIGURATION Debug ===

Check dependencies

Write auxiliary files
/bin/mkdir -p /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/sqlite3.build/Objects-normal/x86_64
write-file /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/sqlite3.build/Objects-normal/x86_64/sqlite3.LinkFileList

CompileC /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/sqlite3.build/Objects-normal/x86_64/sqlite3.o sqlite3.c normal x86_64 c com.apple.compilers.llvm.clang.1_0.compiler
    cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -x c -target x86_64-apple-macos10.15 -fmessage-length=0 -fdiagnostics-show-note-include-stack -fmacro-backtrace-limit=0 -Wno-trigraphs -fpascal-strings -O0 -Wno-missing-field-initializers -Wno-missing-prototypes -Wno-return-type -Wno-missing-braces -Wparentheses -Wswitch -Wno-unused-function -Wno-unused-label -Wno-unused-parameter -Wno-unused-variable -Wunused-value -Wno-empty-body -Wno-uninitialized -Wno-unknown-pragmas -Wno-shadow -Wno-four-char-constants -Wno-conversion -Wno-constant-conversion -Wno-int-conversion -Wno-bool-conversion -Wno-enum-conversion -Wno-float-conversion -Wno-non-literal-null-conversion -Wno-objc-literal-conversion -Wno-shorten-64-to-32 -Wpointer-sign -Wno-newline-eof -DCMAKE_INTDIR=\"Debug\" -DSQLITE_ENABLE_JSON1 -DSQLITE_DQS=0 -DSQLITE_DEFAULT_MEMSTATUS=0 -DSQLITE_LIKE_DOESNT_MATCH_BLOBS -DSQLITE_MAX_EXPR_DEPTH=0 -DSQLITE_OMIT_DECLTYPE -DSQLITE_OMIT_DEPRECATED -DSQLITE_USE_ALLOCA -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk -fasm-blocks -fstrict-aliasing -Wdeprecated-declarations -g -Wno-sign-conversion -Wno-infinite-recursion -Wno-comma -Wno-block-capture-autoreleasing -Wno-strict-prototypes -Wno-semicolon-before-method-body -I/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/Debug/include -I/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/sqlite3.build/DerivedSources-normal/x86_64 -I/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/sqlite3.build/DerivedSources/x86_64 -I/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/sqlite3.build/DerivedSources -Wmost -Wno-four-char-constants -Wno-unknown-pragmas -F/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/Debug -Wall -Wextra -pedantic -MMD -MT dependencies -MF /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/sqlite3.build/Objects-normal/x86_64/sqlite3.d --serialize-diagnostics /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/sqlite3.build/Objects-normal/x86_64/sqlite3.dia -c /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite/sqlite3.c -o /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/sqlite3.build/Objects-normal/x86_64/sqlite3.o
/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite/sqlite3.c:98251:57: warning: unused parameter 'pParse' [-Wunused-parameter]
SQLITE_PRIVATE void sqlite3ExprSetHeightAndFlags(Parse *pParse, Expr *p){
                                                        ^
/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite/sqlite3.c:127390:10: warning: unused parameter 'pParse' [-Wunused-parameter]
  Parse *pParse,      /* Parser context */
         ^
/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite/sqlite3.c:127391:12: warning: unused parameter 'pTabList' [-Wunused-parameter]
  SrcList *pTabList,  /* List of tables */
           ^
/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite/sqlite3.c:127392:13: warning: unused parameter 'pEList' [-Wunused-parameter]
  ExprList *pEList    /* Expressions defining the result set */
            ^
4 warnings generated.

Libtool /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/Debug/libsqlite3.a normal x86_64
    cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/libtool -static -arch_only x86_64 -D -syslibroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk -L/Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/Debug -filelist /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/sqlite3.build/Objects-normal/x86_64/sqlite3.LinkFileList -o /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/Debug/libsqlite3.a

=== BUILD AGGREGATE TARGET ALL_BUILD OF PROJECT sqlite3 WITH CONFIGURATION Debug ===

Check dependencies

Write auxiliary files
write-file /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/ALL_BUILD.build/Script-50FF3BD8C0F94E6898D13121.sh
chmod 0755 /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/ALL_BUILD.build/Script-50FF3BD8C0F94E6898D13121.sh

PhaseScriptExecution CMake\ Rules /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/ALL_BUILD.build/Script-50FF3BD8C0F94E6898D13121.sh
    cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite
    /bin/sh -c /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build/sqlite3.build/Debug/ALL_BUILD.build/Script-50FF3BD8C0F94E6898D13121.sh
echo ""

echo Build\ all\ projects
Build all projects

** BUILD SUCCEEDED **

cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -E touch /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src/sqlite-stamp/Debug/sqlite-build
echo "No install step for 'sqlite'"
No install step for 'sqlite'
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -E echo_append
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-build &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -E touch /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src/sqlite-stamp/Debug/sqlite-install
echo "Generate version-sqlite.txt and license-sqlite.txt"
Generate version-sqlite.txt and license-sqlite.txt
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -P /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/CMakeFiles/sqlite-generate-project-description.cmake
cd /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite &amp;&amp; /usr/local/Cellar/cmake/3.16.1/bin/cmake -E touch /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src/sqlite-stamp/Debug/sqlite-generate_project_description
echo "Completed 'sqlite'"
Completed 'sqlite'
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E make_directory /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/CMakeFiles/Debug
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E touch /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/CMakeFiles/Debug/sqlite-complete
/usr/local/Cellar/cmake/3.16.1/bin/cmake -E touch /Volumes/BIGLC_SHARE/Alex_Save/GIT/build/slicer/sqlite-prefix/src/sqlite-stamp/Debug/sqlite-done



Build succeeded    19/12/2019 18:18    22.7 seconds
</code></pre>
<pre><code class="lang-auto">remote: Permission to Slicer/Slicer.git denied to BishopWolf.
fatal: impossible d'accéder à 'https://github.com/Slicer/Slicer/' : The requested URL returned error: 403
</code></pre>
<p>I am trying to push into a new branch sqlite</p>

---

## Post #14 by @Alex_Vergara (2019-12-20 08:22 UTC)

<p>I can’t push the changes, The site gave me permission errors to push into a new branch, where do I have to push the changes?</p>
<pre><code class="lang-auto">remote: Permission to Slicer/Slicer.git denied to BishopWolf.
fatal: impossible d'accéder à 'https://github.com/Slicer/Slicer/' : The requested URL returned error: 403
</code></pre>

---

## Post #15 by @Alex_Vergara (2019-12-20 10:50 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/lassoan">@lassoan</a>: here it is the patch to enable sqlite3 support. I can’t push it to the git since I don’t have permissions</p>
<pre><code class="lang-auto">diff --git a/CMake/SlicerInitializeOSXVariables.cmake b/CMake/SlicerInitializeOSXVariables.cmake
index 5b7300fd7..9bb27fc30 100644
--- a/CMake/SlicerInitializeOSXVariables.cmake
+++ b/CMake/SlicerInitializeOSXVariables.cmake
@@ -67,7 +67,7 @@ if(APPLE)
   set(required_deployment_target "10.11")
 
   if(CMAKE_OSX_DEPLOYMENT_TARGET VERSION_LESS ${required_deployment_target})
-    message(FATAL_ERROR "CMAKE_OSX_DEPLOYMENT_TARGET must be ${required_deployment_target} or greater.")
+    message(FATAL_ERROR "CMAKE_OSX_DEPLOYMENT_TARGET ${CMAKE_OSX_DEPLOYMENT_TARGET} must be ${required_deployment_target} or greater.")
   endif()
 
   if(NOT "${CMAKE_OSX_SYSROOT}" STREQUAL "")
diff --git a/SuperBuild.cmake b/SuperBuild.cmake
index 62888538b..7d24b7df4 100644
--- a/SuperBuild.cmake
+++ b/SuperBuild.cmake
@@ -97,6 +97,7 @@ set(Slicer_DEPENDENCIES
   CTK
   LibArchive
   RapidJSON
+  sqlite
   )
 
 set(CURL_ENABLE_SSL ${Slicer_USE_PYTHONQT_WITH_OPENSSL})
diff --git a/SuperBuild/External_python.cmake b/SuperBuild/External_python.cmake
index 0b8ad8bc4..44992518f 100644
--- a/SuperBuild/External_python.cmake
+++ b/SuperBuild/External_python.cmake
@@ -10,6 +10,7 @@ if(NOT Slicer_USE_SYSTEM_python)
     bzip2
     CTKAPPLAUNCHER
     zlib
+    sqlite
     )
 endif()
 if(Slicer_USE_PYTHONQT_WITH_TCL)
@@ -165,6 +166,8 @@ if((NOT DEFINED PYTHON_INCLUDE_DIR
       -DBZIP2_LIBRARIES:FILEPATH=${BZIP2_LIBRARIES}
       -DZLIB_INCLUDE_DIR:PATH=${ZLIB_INCLUDE_DIR}
       -DZLIB_LIBRARY:FILEPATH=${ZLIB_LIBRARY}
+      -DSQLITE3_LIBRARY:FILEPATH=${sqlite_LIBRARY}
+      -DSQLITE3_INCLUDE_PATH:PATH=${sqlite_DIR}
       -DENABLE_TKINTER:BOOL=${Slicer_USE_PYTHONQT_WITH_TCL}
       -DENABLE_SSL:BOOL=${PYTHON_ENABLE_SSL}
       -DPatch_EXECUTABLE:FILEPATH=${Patch_EXECUTABLE}
diff --git a/SuperBuild/External_sqlite.cmake b/SuperBuild/External_sqlite.cmake
new file mode 100644
index 000000000..fbd8478a5
--- /dev/null
+++ b/SuperBuild/External_sqlite.cmake
@@ -0,0 +1,78 @@
+
+set( proj sqlite )
+
+# Set dependency list
+set(${proj}_DEPENDENCIES "")
+
+# Include dependent projects if any
+ExternalProject_Include_Dependencies(${proj} PROJECT_VAR proj DEPENDS_VAR ${proj}_DEPENDENCIES)
+
+if(Slicer_USE_SYSTEM_${proj})
+  unset(${proj}_DIR CACHE)
+  find_package(${proj} REQUIRED)
+endif()
+
+# Sanity checks
+if(DEFINED ${proj}_DIR AND NOT EXISTS ${${proj}_DIR})
+  message(FATAL_ERROR "${proj}_DIR variable is defined but corresponds to nonexistent directory")
+endif()
+
+if(NOT DEFINED ${proj}_DIR AND NOT Slicer_USE_SYSTEM_${proj})
+
+  ExternalProject_SetIfNotDefined(
+    Slicer_${proj}_GIT_REPOSITORY
+    "${EP_GIT_PROTOCOL}://github.com/azadkuh/sqlite-amalgamation.git"
+    QUIET
+    )
+
+  ExternalProject_SetIfNotDefined(
+    Slicer_${proj}_GIT_TAG
+    "3.30.1"
+    QUIET
+    )
+
+  set(EP_SOURCE_DIR ${CMAKE_BINARY_DIR}/${proj})
+  set(EP_BINARY_DIR ${CMAKE_BINARY_DIR}/${proj}-build)
+
+  ExternalProject_Add(${proj}
+    ${${proj}_EP_ARGS}
+    GIT_REPOSITORY "${Slicer_${proj}_GIT_REPOSITORY}"
+    GIT_TAG "${Slicer_${proj}_GIT_TAG}"
+    SOURCE_DIR ${EP_SOURCE_DIR}
+    BINARY_DIR ${EP_BINARY_DIR}
+    CMAKE_CACHE_ARGS
+      -DCMAKE_CXX_COMPILER:FILEPATH=${CMAKE_CXX_COMPILER}
+      -DCMAKE_CXX_FLAGS:STRING=${ep_common_cxx_flags}
+      -DCMAKE_C_COMPILER:FILEPATH=${CMAKE_C_COMPILER}
+      -DCMAKE_C_FLAGS:STRING=${ep_common_c_flags} # Unused
+      -DCMAKE_CXX_STANDARD:STRING=${CMAKE_CXX_STANDARD}
+      -DCMAKE_CXX_STANDARD_REQUIRED:BOOL=${CMAKE_CXX_STANDARD_REQUIRED}
+      -DCMAKE_CXX_EXTENSIONS:BOOL=${CMAKE_CXX_EXTENSIONS}
+      -DSQLITE_BUILD_DOC:BOOL=OFF
+      -DSQLITE_BUILD_EXAMPLES:BOOL=OFF
+      -DSQLITE_BUILD_TESTS:BOOL=OFF
+      -DLIBRARY_INSTALL_DIR:PATH=${Slicer_INSTALL_LIB_DIR}
+      -DRUNTIME_INSTALL_DIR:PATH=${Slicer_INSTALL_LIB_DIR}
+      -DARCHIVE_INSTALL_DIR:PATH=${Slicer_INSTALL_LIB_DIR}
+      -DINCLUDE_INSTALL_DIR:PATH=${Slicer_INSTALL_INCLUDE_DIR}
+    INSTALL_COMMAND ""
+    DEPENDS
+      ${${proj}_DEPENDENCIES}
+    )
+
+  ExternalProject_GenerateProjectDescription_Step(${proj})
+
+  set(${proj}_DIR ${EP_BINARY_DIR})
+  set(${proj}_SOURCE_DIR ${EP_SOURCE_DIR})
+  set(${proj}_LIBRARY ${${proj}_DIR})
+
+else()
+  ExternalProject_Add_Empty(${proj} DEPENDS ${${proj}_DEPENDENCIES})
+endif()
+
+mark_as_superbuild(
+  VARS
+    ${proj}_LIBRARY:PATH
+    ${proj}_DIR:PATH
+  LABELS "FIND_PACKAGE"
+  )
</code></pre>
<p>This was tested on mac and linux, I am not possible to test on windows. SlicerPython is built successfully with internal sqlite3 support.</p>

---

## Post #16 by @lassoan (2019-12-20 12:16 UTC)

<p>This is awesome, thank you. Please fork Slicer/Slicer repository, push to your fork, and create a pull request to Slicer/Slicer (standard <a href="https://guides.github.com/introduction/flow/">github flow process</a>). We can then review and test your changes, provide feedback, and merge. I’ll test on Windows.</p>

---

## Post #17 by @Alex_Vergara (2019-12-20 12:32 UTC)

<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/1293" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/1293" target="_blank" rel="nofollow noopener">Sqlite3</a>
    </h4>

    <div class="branches">
      <code>Slicer:nightly-master</code> ← <code>BishopWolf:sqlite3</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2019-12-20" data-time="12:31:57" data-timezone="UTC">12:31PM - 20 Dec 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/BishopWolf" target="_blank" rel="nofollow noopener">
          <img alt="BishopWolf" src="https://avatars3.githubusercontent.com/u/11816952?v=4" class="onebox-avatar-inline" width="20" height="20">
          BishopWolf
        </a>
      </div>

      <div class="lines" title="3 commits changed 4 files with 83 additions and 1 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/1293/files" target="_blank" rel="nofollow noopener">
          <span class="added">+83</span>
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

## Post #18 by @Alex_Vergara (2019-12-26 13:13 UTC)

<p>Successfully tested in <a href="https://github.com/Slicer/Slicer/pull/1293" rel="nofollow noopener">Mac and Windows</a> so far. We need a linux tester!!</p>

---

## Post #19 by @pieper (2019-12-27 17:30 UTC)

<p>Here’s a diff that makes the build work on linux (it’s a throwaway virtual machine so I can’t push from it).  This fix follows the pattern for curl and other C libraries so it seems to be the right thing.</p>
<pre><code class="lang-auto">~/Slicer$ git diff
diff --git a/SuperBuild/External_sqlite.cmake b/SuperBuild/External_sqlite.cmake
index d54e6adf8..e8b698827 100644
--- a/SuperBuild/External_sqlite.cmake
+++ b/SuperBuild/External_sqlite.cmake
@@ -36,6 +36,11 @@ if(NOT DEFINED ${proj}_DIR AND NOT Slicer_USE_SYSTEM_${proj})
   set(EP_BINARY_DIR ${CMAKE_BINARY_DIR}/${proj}-build)
   set(EP_INSTALL_DIR ${CMAKE_BINARY_DIR}/${proj}-install)
 
+  set(${proj}_CMAKE_C_FLAGS ${ep_common_c_flags})
+  if(CMAKE_SIZEOF_VOID_P EQUAL 8) # 64-bit
+    set(${proj}_CMAKE_C_FLAGS "${ep_common_c_flags} -fPIC")
+  endif()
+
   ExternalProject_Add(${proj}
     ${${proj}_EP_ARGS}
     GIT_REPOSITORY "${Slicer_${proj}_GIT_REPOSITORY}"
@@ -47,7 +52,7 @@ if(NOT DEFINED ${proj}_DIR AND NOT Slicer_USE_SYSTEM_${proj})
       -DCMAKE_CXX_COMPILER:FILEPATH=${CMAKE_CXX_COMPILER}
       -DCMAKE_CXX_FLAGS:STRING=${ep_common_cxx_flags}
       -DCMAKE_C_COMPILER:FILEPATH=${CMAKE_C_COMPILER}
-      -DCMAKE_C_FLAGS:STRING=${ep_common_c_flags} # Unused
+      -DCMAKE_C_FLAGS:STRING=${${proj}_CMAKE_C_FLAGS}
       -DCMAKE_CXX_STANDARD:STRING=${CMAKE_CXX_STANDARD}
       -DCMAKE_CXX_STANDARD_REQUIRED:BOOL=${CMAKE_CXX_STANDARD_REQUIRED}
       -DCMAKE_CXX_EXTENSIONS:BOOL=${CMAKE_CXX_EXTENSIONS}
</code></pre>
<p>With the fix I get this:</p>
<pre><code class="lang-auto">pieper@slicer-build-1:~/Slicer$ ../Slicer-superbuild/python-install/bin/PythonSlicer 
Python 3.6.7 (default, Dec 11 2019, 15:28:01) 
[GCC 7.4.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import sqlite3
&gt;&gt;&gt; 
</code></pre>
<p>Without it, here’s the build error on <code>Ubuntu 18.04.3</code>.</p>
<pre><code class="lang-auto">[ 32%] Linking C shared library ../../../lib/python3.6/lib-dynload/_sqlite3.so
/usr/bin/ld: /home/pieper/Slicer-superbuild/sqlite-install/lib/libsqlite3.a(sqlite3.c.o): relocation R_X86_64_PC32 against symbol `sqlite3_mutex_enter' can not be used when making a shared object; recompile with -fPIC
/usr/bin/ld: final link failed: Bad value
collect2: error: ld returned 1 exit status
CMakeBuild/extensions/extension_sqlite3/CMakeFiles/extension_sqlite3.dir/build.make:204: recipe for target 'lib/python3.6/lib-dynload/_sqlite3.so' failed
make[5]: *** [lib/python3.6/lib-dynload/_sqlite3.so] Error 1
CMakeFiles/Makefile2:4389: recipe for target 'CMakeBuild/extensions/extension_sqlite3/CMakeFiles/extension_sqlite3.dir/all' failed
make[4]: *** [CMakeBuild/extensions/extension_sqlite3/CMakeFiles/extension_sqlite3.dir/all] Error 2
Makefile:140: recipe for target 'all' failed
make[3]: *** [all] Error 2
CMakeFiles/python.dir/build.make:117: recipe for target 'python-prefix/src/python-stamp/python-build' failed
make[2]: *** [python-prefix/src/python-stamp/python-build] Error 2
CMakeFiles/Makefile2:1073: recipe for target 'CMakeFiles/python.dir/all' failed
make[1]: *** [CMakeFiles/python.dir/all] Error 2
Makefile:94: recipe for target 'all' failed
make: *** [all] Error 2
</code></pre>

---

## Post #20 by @lassoan (2019-12-30 20:02 UTC)

<p>It seems that there is a build error on Linux caused by this change: <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1787103">http://slicer.cdash.org/viewBuildError.php?buildid=1787103</a></p>
<p>Could someone have a look and suggest a fix?</p>

---

## Post #21 by @Alex_Vergara (2019-12-31 03:55 UTC)

<p>Did you merged the <a href="https://github.com/Slicer/Slicer/commit/4001545375eeed0fa7b15cb76b4510f9b00f4e20" rel="nofollow noopener">last commits</a> that I pushed before the final merge solving this issue?</p>

---

## Post #22 by @lassoan (2019-12-31 04:03 UTC)

<p>I’ve included that commit - see <a href="https://github.com/Slicer/Slicer/commit/15bc3838623449df79e32ecd5303062000868feb">https://github.com/Slicer/Slicer/commit/15bc3838623449df79e32ecd5303062000868feb</a>.</p>
<p>It was quite complicated because you kept force-pushing a long list of complicated commits and merge-commits, while I kept cleaning them up and squashing and rebasing on latest master. It is possible that something got lost in the process.</p>

---

## Post #23 by @Alex_Vergara (2019-12-31 04:07 UTC)

<p>I wonder why the comparison still <a href="https://github.com/Slicer/Slicer/compare/nightly-master...BishopWolf:sqlite3?expand=1" rel="nofollow noopener">show differences</a> regarding these changes? I expected these differences to refer no change at all.</p>
<p>Anyways, the error says</p>
<pre><code class="lang-auto">ninja: error: '/.../Slicer-0-build/sqlite-install/lib/libsqlite3.a', needed by 'lib/python3.6/lib-dynload/_sqlite3.so', missing and no known rule to make it
</code></pre>
<p>which is quite odd, it worked in the other tests and in other systems.</p>

---
