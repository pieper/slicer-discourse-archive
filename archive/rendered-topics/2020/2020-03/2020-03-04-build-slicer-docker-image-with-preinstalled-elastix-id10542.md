# Build Slicer docker image with preinstalled elastix

**Topic ID**: 10542
**Date**: 2020-03-04
**URL**: https://discourse.slicer.org/t/build-slicer-docker-image-with-preinstalled-elastix/10542

---

## Post #1 by @Alex_Vergara (2020-03-04 14:11 UTC)

<p>The title says it all. I want a docker image of slicer with elastix extension preinstalled. My current <code>Dockerfile</code> is the following:</p>
<pre><code class="lang-auto"># start from base with centos &amp; qt5
FROM slicer/buildenv-qt5-centos7:latest

WORKDIR /usr/src

# get basics for the gui
RUN yum install Xvfb Xorg mesa-dri-drivers libGLEW -y

# get slicer nighly version
RUN git clone -b master https://github.com/Slicer/Slicer.git

# create slicer-build and environment
RUN mkdir /usr/src/Slicer-build &amp;&amp; \
    cd /usr/src/Slicer-build &amp;&amp; \
    # build slicer
    cmake \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DQt5_DIR:PATH=${Qt5_DIR} \
    -DSlicer_USE_SimpleITK:BOOL=OFF \
    -DSlicer_USE_QtTesting:BOOL=OFF \
    /usr/src/Slicer &amp;&amp; \
    # build dependencies
    make -j 32

# create environment variables
ENV PATH="${PATH}:/usr/src/Slicer-build/python-install/bin"
ENV PYTHONPATH="${PYTHONPATH}:/usr/src/Slicer-build/python-install/bin/PythonSlicer"
ENV SLICER=/usr/src/Slicer

# Create ExtensionsIndex
RUN git clone git://github.com/Slicer/ExtensionsIndex.git &amp;&amp; \
    mkdir ExtensionsIndex-build &amp;&amp; cd ExtensionsIndex-build &amp;&amp; \
    cmake -DSlicer_DIR:PATH=/usr/src/Slicer-build/Slicer-build -DSlicer_EXTENSION_DESCRIPTION_DIR:PATH=../ExtensionsIndex \
    -DCMAKE_BUILD_TYPE:STRING=Release ${SLICER}/Extensions/CMake &amp;&amp; \
    make -j 32

# Install Elastix
RUN PythonSlicer -c "import sys;print(sys.path)"
RUN PythonSlicer -m pip install --upgrade pip
RUN PythonSlicer -m pip install 2to3 lmfit
RUN 2to3 -w /usr/src/Slicer-build/python-install/lib/python3.6/site-packages/uncertainties

# start running container
CMD bash
</code></pre>
<p>But this raises an 18GB image!! All extensions are built!! The worst is: no extension is installed! They are all built and able to be installed, but not actually installed.</p>
<p>When I try to use it, it says slicer has no module app.</p>
<p>What is wrong here??</p>

---

## Post #2 by @Alex_Vergara (2020-03-04 14:37 UTC)

<p>I have tried building an image from slicer-base, but it is also unsuccessful. The Dockerfile is:</p>
<pre><code class="lang-auto"># start from base with slicer-base
FROM slicer/slicer-base

WORKDIR /usr/src/Slicer

# get basics for the gui
RUN yum install Xvfb Xorg mesa-dri-drivers libGLEW -y

# create slicer package
RUN ../Slicer-build/BuildSlicer.sh &amp;&amp; \
     package=$(head -n1 /usr/src/Slicer-build/Slicer-build/PACKAGE_FILE.txt) &amp;&amp; \
     echo "package [${package}]" &amp;&amp; \
     mkdir -p /Slicer-package  &amp;&amp; \
     mv ${package} /Slicer-package/

# create environment variables
ENV PATH="${PATH}:/Slicer-package/"
ENV PYTHONPATH="${PYTHONPATH}:/usr/src/Slicer-build/python-install/bin/PythonSlicer"
ENV SLICER=/usr/src/Slicer

# Install Elastix
RUN PythonSlicer -c "import sys;print(sys.path)"
RUN PythonSlicer -m pip install --upgrade pip
RUN PythonSlicer -m pip install 2to3 lmfit
RUN 2to3 -w /usr/src/Slicer-build/python-install/lib/python3.6/site-packages/uncertainties
RUN (echo "import slicer" ; echo "emm = slicer.app.extensionsManagerModel()"; echo "md = emm.retrieveExtensionMetadataByName('SlicerElastix')"; echo "emm.dow$
RUN PythonSlicer InstallElastix.py

# start running container
CMD bash
</code></pre>
<p>This fails in the BuildSlicer.sh</p>
<pre><code class="lang-auto">Step 4/14 : RUN ../Slicer-build/BuildSlicer.sh &amp;&amp;      package=$(head -n1 /usr/src/Slicer-build/Slicer-build/PACKAGE_FILE.txt) &amp;&amp;      echo "package [${package}]" &amp;&amp;      mkdir -p /Slicer-package  &amp;&amp;      mv ${package} /Slicer-package/
 ---&gt; Running in 8bb2e3f6bf82
+ set -o pipefail
+ set -o
allexport      	off
braceexpand    	on
emacs          	off
errexit        	on
errtrace       	off
functrace      	off
hashall        	on
histexpand     	off
history        	off
ignoreeof      	off
interactive-comments	on
keyword        	off
monitor        	off
noclobber      	off
noexec         	off
noglob         	off
nolog          	off
notify         	off
nounset        	off
onecmd         	off
physical       	off
pipefail       	on
posix          	off
privileged     	off
verbose        	off
vi             	off
xtrace         	on
+ cd /usr/src/Slicer-build
+ /usr/bin/cmake -E make_directory /usr/src/Slicer
+ /usr/bin/cmake -E make_directory /usr/src/Slicer-build/Slicer-build
+ /usr/bin/cmake -E make_directory /usr/src/Slicer-build/Slicer-prefix
+ /usr/bin/cmake -E make_directory /usr/src/Slicer-build/Slicer-prefix/tmp
+ /usr/bin/cmake -E make_directory /usr/src/Slicer-build/Slicer-prefix/src/Slicer-stamp
+ /usr/bin/cmake -E make_directory /usr/src/Slicer-build/Slicer-prefix/src
+ /usr/bin/cmake -E touch /usr/src/Slicer-build/Slicer-prefix/src/Slicer-stamp/Slicer-mkdir
+ cd /usr/src/Slicer-build/Slicer-prefix/src
+ /usr/bin/cmake -E echo_append
+ /usr/bin/cmake -E touch /usr/src/Slicer-build/Slicer-prefix/src/Slicer-stamp/Slicer-download
+ cd /usr/src/Slicer
+ /usr/bin/cmake -E echo_append
+ /usr/bin/cmake -E touch /usr/src/Slicer-build/Slicer-prefix/src/Slicer-stamp/Slicer-update
+ cd /usr/src/Slicer-build
+ /usr/bin/cmake -E echo_append
+ /usr/bin/cmake -E touch /usr/src/Slicer-build/Slicer-prefix/src/Slicer-stamp/Slicer-patch
+ cd /usr/src/Slicer-build/Slicer-build
+ /usr/bin/cmake -C/usr/src/Slicer-build/Slicer-prefix/tmp/Slicer-cache-Release.cmake -GNinja /usr/src/Slicer
loading initial cache file /usr/src/Slicer-build/Slicer-prefix/tmp/Slicer-cache-Release.cmake
CMake Error: The source directory "/usr/src/Slicer" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.
+ exit 1
The command '/bin/sh -c ../Slicer-build/BuildSlicer.sh &amp;&amp;      package=$(head -n1 /usr/src/Slicer-build/Slicer-build/PACKAGE_FILE.txt) &amp;&amp;      echo "package [${package}]" &amp;&amp;      mkdir -p /Slicer-package  &amp;&amp;      mv ${package} /Slicer-package/' returned a non-zero code: 1
</code></pre>

---

## Post #3 by @Alex_Vergara (2020-03-04 14:54 UTC)

<p>Somehow I see the slicer-base image to be empty, is this normal? Where it is Slicer installed here?</p>
<pre><code class="lang-auto">E15TY:~ alexvergaragil$ docker run -it slicer/slicer-base  /bin/bash
[root@01a14648b5d2 Slicer-build]# ls /usr/src/
cmake-3.13.4-Centos5-x86_64  debug  kernels  Slicer-build
[root@01a14648b5d2 Slicer-build]# ls Slicer-
Slicer-build/  Slicer-prefix/
[root@01a14648b5d2 Slicer-build]# ls Slicer-build/
share
[root@01a14648b5d2 Slicer-build]# ls Slicer-prefix/
src  tmp
[root@01a14648b5d2 Slicer-build]# ls Slicer-prefix/src/
Slicer-stamp
[root@01a14648b5d2 Slicer-build]# ls Slicer-prefix/src/Slicer-stamp/
[root@01a14648b5d2 Slicer-build]# ls Slicer-build/share/
Slicer-4.11
[root@01a14648b5d2 Slicer-build]# ls Slicer-build/share/Slicer-4.11/
Slicer.crt
[root@01a14648b5d2 Slicer-build]#
</code></pre>

---

## Post #4 by @Sam_Horvath (2020-03-04 16:31 UTC)

<p>for the version from slicer/buildenv:</p>
<p>Building the Extensions Index does not install the extensions.  You will still need to manually install by setting module paths</p>
<p>Can you post the error where slicer fails to start?</p>

---

## Post #5 by @Alex_Vergara (2020-03-04 17:00 UTC)

<p>Please remember this is a docker container, I can’t start slicer there. Also the slicer-base image is supposed to have a prebuilt image of Slicer, I just need to add the elastix extension by default. I can trigger the instalation in Slicer by:</p>
<pre><code class="lang-python">import slicer
emm = slicer.app.extensionsManagerModel()
md = emm.retrieveExtensionMetadataByName('SlicerElastix')
emm.downloadAndInstallExtension(md['extension_id'])
</code></pre>
<p>but in the docker environment this fails with the error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "installElastix.py", line 2, in &lt;module&gt;
    emm = slicer.app.extensionsManagerModel()
AttributeError: module 'slicer' has no attribute 'app'
vtkDebugLeaks has found no leaks.
</code></pre>

---

## Post #6 by @Alex_Vergara (2020-03-04 17:16 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="4" data-topic="10542">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>slicer/buildenv</p>
</blockquote>
</aside>
<p>Also</p>
<pre><code class="lang-auto">E15TY:~ alexvergaragil$ docker run -it slicer/buildenv  /bin/bash
Unable to find image 'slicer/buildenv:latest' locally
docker: Error response from daemon: pull access denied for slicer/buildenv, repository does not exist or may require 'docker login': denied: requested access to the resource is denied.
See 'docker run --help'.
</code></pre>

---

## Post #7 by @Sam_Horvath (2020-03-04 17:44 UTC)

<ol>
<li>
<p>Sorry slicer/buildenv should have been slicer/buildenv-qt5-centos7:latest</p>
</li>
<li>
<p>slicer/slicer-base does not contain a slicer build, it is used for CircleCI builds and so contains everything except Slicer</p>
</li>
<li>
<p>We currently do not have a supported full Slicer docker image.  There is a very out of date one available under slicer/slicer-build</p>
</li>
</ol>
<p>I am looking into the best way to get this working for you  (<a class="mention" href="/u/jcfr">@jcfr</a> )</p>

---

## Post #8 by @jcfr (2020-03-04 21:59 UTC)

<p>The Dockerfile that would be responsible to create a docker image useful for runtime could simply download the nightly build and extract it.</p>
<p>It could be based of the work of <a class="mention" href="/u/ihnorton">@ihnorton</a>. See <a href="https://github.com/ihnorton/dockerfiles/blob/master/slicer2binder/Dockerfile">https://github.com/ihnorton/dockerfiles/blob/master/slicer2binder/Dockerfile</a></p>
<p>Once we have such a base image, anyone could easily create derived image with whatever extension they would like.</p>

---

## Post #9 by @Alex_Vergara (2020-03-05 10:19 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="8" data-topic="10542">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>It could be based of the work of <a class="mention" href="/u/ihnorton">@ihnorton</a>. See</p>
</blockquote>
</aside>
<p>Thanks for pointing this to me, however I still got some problems:</p>
<p>My Dockerfile so far:</p>
<pre><code class="lang-auto">
# start from base with slicer-base
FROM slicer/slicer-base

RUN mkdir /usr/src/Slicer &amp;&amp; cd /usr/src/Slicer

WORKDIR /usr/src/Slicer

################################################################################
# Download and unpack Slicer
RUN pip install pip beautifulsoup4 2to3 -U
RUN git clone https://gist.github.com/f49c5062695562370a76222dada47e47.git &amp;&amp; \
    mv f49c5062695562370a76222dada47e47/updateSlicer.py ./updateSlicer.py
RUN python3 updateSlicer.py /usr/src/Slicer

# Create evioronment variables
ENV PATH="${PATH}:/usr/src/Slicer/bin"
ENV PYTHONPATH="${PYTHONPATH}:/usr/src/Slicer/bin/PythonSlicer"
ENV SLICER=/usr/src/Slicer

# Install Elastix
RUN PythonSlicer -c "import sys;print(sys.path)"  &amp;&amp; \
    PythonSlicer -m pip install --upgrade pip lmfit
RUN 2to3 -w /usr/src/Slicer/lib/Python/lib/python3.6/site-packages/uncertainties
RUN (echo "import slicer"; echo "emm = slicer.app.extensionsManagerModel()"; echo "md = emm.retrieveExtensionMetadataByName('SlicerElastix')"; echo "emm.down$
RUN PythonSlicer installElastix.py

# start running container
CMD bash
</code></pre>
<p>this is failing at:</p>
<pre><code class="lang-auto">Step 12/14 : RUN (echo "import slicer"; echo "emm = slicer.app.extensionsManagerModel()"; echo "md = emm.retrieveExtensionMetadataByName('SlicerElastix')"; echo "emm.downloadAndInstallExtension(md['extension_id'])" ) &gt;&gt; installElastix.py
 ---&gt; Running in 5d79f9d8ac46
Removing intermediate container 5d79f9d8ac46
 ---&gt; cbd1129c5580
Step 13/14 : RUN PythonSlicer installElastix.py
 ---&gt; Running in 10b10c6e2546
No module named 'logic'
Traceback (most recent call last):
  File "installElastix.py", line 2, in &lt;module&gt;
    emm = slicer.app.extensionsManagerModel()
AttributeError: module 'slicer' has no attribute 'app'
vtkDebugLeaks has found no leaks.
The command '/bin/sh -c PythonSlicer installElastix.py' returned a non-zero code: 1
</code></pre>
<p>What is it wrong here? The failing script is this one:</p>
<pre><code class="lang-auto">RUN (echo "import slicer"; \
     echo "emm = slicer.app.extensionsManagerModel()"; \
     echo "md = emm.retrieveExtensionMetadataByName('SlicerElastix')"; \
     echo "emm.downloadAndInstallExtension(md['extension_id'])" ) &gt;&gt; installElastix.py
</code></pre>

---

## Post #10 by @Alex_Vergara (2020-03-05 11:22 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="8" data-topic="10542">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>The Dockerfile that would be responsible to create a docker image useful for runtime could simply download the nightly build and extract it.</p>
</blockquote>
</aside>
<p>I have tried this approach and in the test it will fail with</p>
<pre><code class="lang-auto">CMake Error at CMakeLists.txt:17 (find_package):
  By not providing "FindSlicer.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "Slicer", but
  CMake did not find one.

  Could not find a package configuration file provided by "Slicer" with any
  of the following names:

    SlicerConfig.cmake
    slicer-config.cmake

  Add the installation prefix of "Slicer" to CMAKE_PREFIX_PATH or set
  "Slicer_DIR" to a directory containing one of the above files.  If "Slicer"
  provides a separate development package or SDK, be sure it has been
  installed.
</code></pre>
<p>The CMakeList.txt in my extension is:</p>
<pre><code class="lang-auto">cmake_minimum_required(VERSION 3.5)

project(Dosimetry4D)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "http://gitlab.com/opendose/opendose4d")
set(EXTENSION_CATEGORY "Dosimetry")
set(EXTENSION_CONTRIBUTORS "Alex Vergara Gil (INSERM) and Janick Rueegger (KSA)")
set(EXTENSION_DESCRIPTION "This extension contains the entire dosimetry workflow for a multipoint study")
set(EXTENSION_ICONURL "https://opendose.org/themes/default/images/opendose_favicon.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/Dosimetry/Screenshots/1.png")
set(EXTENSION_DEPENDS SlicerElastix) # Specified as a space separated string, a list or 'NA' if any

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(Dosimetry4D)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})

#-----------------------------------------------------------------------------
option(ENABLE_TESTS "Enable tests" OFF)
if (${ENABLE_TESTS})
    enable_testing()
endif()
</code></pre>
<p>but my extension is just a python module, Is there a way to avoid the <code>find_package(Slicer REQUIRED)</code> line??</p>

---

## Post #11 by @lassoan (2020-03-05 13:27 UTC)

<p>You need to pass <code>-DSlicer_DIR:PATH=... </code> to CMake when you configure Dosimetry4D (or the extension manager index builder project).</p>

---

## Post #12 by @Alex_Vergara (2020-03-05 13:29 UTC)

<p>I have done that, but that path does not contain any cmake file in the nightly build. You can use <code>docker run -it unnmdnwb3/slicer3d-nightly:0.8.0  /bin/bash</code> to test this approach. It contains a slicer-base image with a preinstalled slicer-nightly. the Slicer_DIR is /usr/src/Slicer</p>

---

## Post #13 by @lassoan (2020-03-05 13:36 UTC)

<p>I see. An install tree is not sufficient for build&amp;test. As a workaround, you could create a script that runs Pytjon selftests manually. You can find the full command-line of each test on CDash.</p>

---

## Post #14 by @Alex_Vergara (2020-03-05 13:39 UTC)

<p>Actually I only require the <a href="https://github.com/Slicer/Slicer/blob/master/CMake/SlicerMacroBuildScriptedModule.cmake" rel="nofollow noopener">slicerMacroBuildScriptedModule</a> macro definition to run the tests. This file does not depend on any slicer header, but is the one who builds the python module.<br>
Are the command lines like this one?</p>
<pre><code class="lang-auto">/usr/src/Slicer-build/Slicer-build/Slicer "--no-splash" "--testing" "--no-main-window" "--additional-module-paths" "/builds/dosimetry4d-build/lib/Slicer-4.11/qt-scripted-modules" "/builds/dosimetry4d-build/lib/Slicer-4.11/cli-modules" "/builds/dosimetry4d-build/lib/Slicer-4.11/qt-loadable-modules" "--python-code" "import slicer.testing; slicer.testing.runUnitTest(['/builds/dosimetry4d-build/Dosimetry4D/Logic', '/builds/opendose/opendose4d/Dosimetry4D/Logic'], 'Dosimetry4DTest')"
</code></pre>

---

## Post #15 by @lassoan (2020-03-05 14:00 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="14" data-topic="10542">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Are the command lines like this one?</p>
</blockquote>
</aside>
<p>Yes.</p>
<p>It would be nice to properly build and test your extension. It would increase the test coverage (it would test building) and you never know when you’ll need to add a loadable or CLI module to your extension.</p>

---

## Post #16 by @Alex_Vergara (2020-03-05 14:03 UTC)

<p>I can perform normal test without elastix, but that will truncate half the functionality of my extension. Is it possible to have a build sequence that leaves me with a built Slicer+Elastix by default?</p>

---

## Post #17 by @jcfr (2020-03-05 14:13 UTC)

<p>Are you still trying to do the following:</p>
<blockquote>
<p>want a docker image of slicer with elastix extension preinstalled</p>
</blockquote>
<p>If yes, there is no need to base your image of <code>slicer/slicer-base</code>. Using a centos7 base should be sufficient.</p>
<p>Also, what would you like to do with this docker image ?</p>

---

## Post #18 by @Alex_Vergara (2020-03-05 14:17 UTC)

<p>I want to test my extension wich depends on elastix</p>

---

## Post #19 by @Alex_Vergara (2020-03-05 14:21 UTC)

<p>I have tried to run manually the tests and this happens</p>
<pre><code class="lang-auto">$ /usr/src/Slicer/bin/PythonSlicer -c "import slicer.testing; slicer.testing.runUnitTest(['$CI_BUILDS_DIR/dosimetry4d-build/Dosimetry4D/Logic', '$CI_BUILDS_DIR/opendose/opendose4d/Dosimetry4D/Logic'], 'Dosimetry4DTest')"
Dosimetry4DTest (unittest.loader._FailedTest) ... ERROR

======================================================================
ERROR: Dosimetry4DTest (unittest.loader._FailedTest)
----------------------------------------------------------------------
ImportError: Failed to import test module: Dosimetry4DTest
Traceback (most recent call last):
  File "/usr/src/Slicer/lib/Python/lib/python3.6/unittest/loader.py", line 153, in loadTestsFromName
    module = __import__(module_name)
  File "/builds/dosimetry4d-build/Dosimetry4D/Logic/Dosimetry4DTest.py", line 3, in &lt;module&gt;
    from slicer.ScriptedLoadableModule import ScriptedLoadableModuleTest
  File "/usr/src/Slicer/bin/Python/slicer/ScriptedLoadableModule.py", line 4, in &lt;module&gt;
    import qt, ctk, slicer
  File "/usr/src/Slicer/bin/Python/qt/__init__.py", line 19, in &lt;module&gt;
    from PythonQt.private import QObject
ModuleNotFoundError: No module named 'PythonQt'


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/usr/src/Slicer/bin/Python/slicer/testing.py", line 26, in runUnitTest
    exitFailure()
  File "/usr/src/Slicer/bin/Python/slicer/testing.py", line 11, in exitFailure
    raise Exception(message)
Exception
No module named 'logic'
-------------------------------------------
path: ['/builds/dosimetry4d-build/Dosimetry4D/Logic', '/builds/opendose/opendose4d/Dosimetry4D/Logic']
testname: Dosimetry4DTest
-------------------------------------------
vtkDebugLeaks has found no leaks.
</code></pre>
<p>I think preinstalled slicer leads to even more errors than building it</p>

---

## Post #20 by @Alex_Vergara (2020-03-06 14:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="10542">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be nice to properly build and test your extension.</p>
</blockquote>
</aside>
<p>I have succeeded to make a Full Test using BrainsFit, not optimal but good enough solution. The Full Test in graphical mode (Reload and test) will use elastix if it is installed.<br>
The module is complete, I am just waiting for testers answers. Next steps will be:</p>
<ol>
<li>Write the article (shall be presented in ECMP2020 or EANM2020)</li>
<li>Open the source (as soon as the abstract is accepted)</li>
<li>integrating in Slicer as scripted module (I will need your help in this point). The module shall be accesible by the time the article is published.</li>
</ol>

---

## Post #21 by @ROSENty (2021-12-30 08:33 UTC)

<p>could you tell me how to install extension(such as SlicerRT) in docker container(from docker images<a href="https://github.com/Slicer/SlicerDocker" rel="noopener nofollow ugc">https://github.com/Slicer/SlicerDocker</a>) manually?</p>

---

## Post #22 by @lassoan (2021-12-30 17:59 UTC)

<p>The question is answered here:</p>
<aside class="quote" data-post="12" data-topic="13925">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/installing-extension-inside-a-dockerfile/13925/12">Installing extension inside a Dockerfile</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Showing GUI or not is your choice, but you need to set up a display server to run the full application. It does not mean that you need to display a GUI at the host. 
The slicer-notebook docker image that I linked above installs SlicerJupyter. Replace that by SlicerElastix and you are good.
  </blockquote>
</aside>


---
