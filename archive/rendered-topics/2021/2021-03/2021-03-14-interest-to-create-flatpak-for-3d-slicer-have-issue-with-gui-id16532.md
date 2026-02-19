---
topic_id: 16532
title: "Interest To Create Flatpak For 3D Slicer Have Issue With Gui"
date: 2021-03-14
url: https://discourse.slicer.org/t/16532
---

# Interest to create Flatpak for 3D Slicer, have issue with GUISupportQtOpenGL not found

**Topic ID**: 16532
**Date**: 2021-03-14
**URL**: https://discourse.slicer.org/t/interest-to-create-flatpak-for-3d-slicer-have-issue-with-guisupportqtopengl-not-found/16532

---

## Post #1 by @Andythe_great (2021-03-14 14:06 UTC)

<p>Hello,</p>
<p>I want to create Flatpak for 3D Slicer.<br>
Flatpak is a packaging and distributing desktop software on Linux.<br>
<a href="https://www.flatpak.org/" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.flatpak.org/</a></p>
<p>I would like it to be submit to Flathub, an app store for Flatpak apps. Many Linux distros supported Flatpak. So I think it would be beneficial to package large software like 3D Slicer into Flatpak, it will make installing 3D Slicer quick and easy.<br>
<a href="https://flathub.org/home" class="onebox" target="_blank" rel="noopener nofollow ugc">https://flathub.org/home</a></p>
<p>This is what I have been working on so far.</p><aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/kevinsmia1939/org.slicer.Slicer" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:400/400;"><img src="https://avatars.githubusercontent.com/u/11407922?s=400&amp;amp;v=4" class="thumbnail" width="400" height="400"></div>

<h3><a href="https://github.com/kevinsmia1939/org.slicer.Slicer" target="_blank" rel="noopener nofollow ugc">kevinsmia1939/org.slicer.Slicer</a></h3>


  <p><span class="label1">Contribute to kevinsmia1939/org.slicer.Slicer development by creating an account on GitHub.</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I build VTK 9.0.1 with the following flags,</p>
<pre><code class="lang-auto">&gt; - -DVTK_BUILD_ALL_MODULES=OFF 
&gt; - -DBUILD_SHARED_LIBS=YES
&gt; - -DOpenGL_GL_PREFERENCE=GLVND
&gt; - -DVTK_WRAP_JAVA=OFF
&gt; - -DVTK_WRAP_PYTHON=YES
&gt; - -DCMAKE_BUILD_TYPE=Release
&gt; - -DVTK_PYTHON_VERSION:STRING=3
&gt; - -DVTK_GROUP_ENABLE_Qt=YES
&gt; - -DVTK_GROUP_ENABLE_Views=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_GUISupportQt=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_RenderingContextOpenGL2=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_RenderingFreeTypeFontConfig=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_RenderingQt=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_GUISupportQtSQL=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_FiltersExtraction=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_FiltersFlowPaths=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_FiltersGeometry=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_FiltersParallel=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_IOExport=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_IOImage=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_IOLegacy=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_IOPLY=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_IOXML=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_ImagingMath=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_ImagingMorphological=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_ImagingStatistics=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_ImagingStencil=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_InteractionImage=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_RenderingVolumeOpenGL2=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_TestingRendering=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_ViewsQt=YES
&gt; - -DVTK_MODULE_ENABLE_VTK_zlib=YES

And Slicer with this,
&gt;   - -DCMAKE_BUILD_TYPE:STRING=Release
&gt;   - -DSlicer_SUPERBUILD:BOOL=OFF

When building 3D Slicer, I got this error.
&gt; -- Setting C++ standard
&gt; -- Setting C++ standard - C++11
&gt; -- The C compiler identification is GNU 10.2.0
&gt; -- The CXX compiler identification is GNU 10.2.0
&gt; -- Detecting C compiler ABI info
&gt; -- Detecting C compiler ABI info - done
&gt; -- Check for working C compiler: /usr/bin/cc - skipped
&gt; -- Detecting C compile features
&gt; -- Detecting C compile features - done
&gt; -- Detecting CXX compiler ABI info
&gt; -- Detecting CXX compiler ABI info - done
&gt; -- Check for working CXX compiler: /usr/bin/c++ - skipped
&gt; -- Detecting CXX compile features
&gt; -- Detecting CXX compile features - done
&gt; -- Checking if --no-as-needed linker flag is required
&gt; -- Checking if --no-as-needed linker flag is required - yes
&gt; -- Check if the system is big endian
&gt; -- Searching 16 bit integer
&gt; -- Looking for sys/types.h
&gt; -- Looking for sys/types.h - found
&gt; -- Looking for stdint.h
&gt; -- Looking for stdint.h - found
&gt; -- Looking for stddef.h
&gt; -- Looking for stddef.h - found
&gt; -- Check size of unsigned short
&gt; -- Check size of unsigned short - done
&gt; -- Searching 16 bit integer - Using unsigned short
&gt; -- Check if the system is big endian - little endian
&gt; -- Could NOT find Subversion (missing: Subversion_SVN_EXECUTABLE) 
&gt; -- Found Git: /usr/bin/git  
&gt; -- Found Patch: /usr/bin/patch  
&gt; -- Configuring Slicer organization domain [www.na-mic.org]
&gt; -- Configuring Slicer organization name [NA-MIC]
&gt; -- Configuring Slicer default home module [Welcome]
&gt; -- Configuring Slicer default favorite modules [Data, Volumes, Models, Transforms, Markups, SegmentEditor]
&gt; -- Configuring Slicer text of disclaimer at startup [Thank you for using %1!&lt;br&gt;&lt;br&gt;This software is not intended for clinical use.]
&gt; -- Configuring Slicer release type [Experimental]
&gt; CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:94 (message):
&gt;   Skipping repository info extraction: directory [/run/build/Slicer] is not a
&gt;   GIT or SVN checkout
&gt; Call Stack (most recent call first):
&gt;   CMake/SlicerVersion.cmake:55 (SlicerMacroExtractRepositoryInfo)
&gt;   CMakeLists.txt:183 (include)
&gt; This warning is for project developers.  Use -Wno-dev to suppress it.
&gt; 
&gt; -- Configuring Slicer version [4.11.20210226-0000-00-00]
&gt; -- Configuring Slicer revision [0]
&gt; CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:94 (message):
&gt;   Skipping repository info extraction: directory [/run/build/Slicer] is not a
&gt;   GIT or SVN checkout
&gt; Call Stack (most recent call first):
&gt;   CMake/SlicerVersion.cmake:99 (SlicerMacroExtractRepositoryInfo)
&gt;   CMakeLists.txt:183 (include)
&gt; This warning is for project developers.  Use -Wno-dev to suppress it.
&gt; 
&gt; -- Checking to see if CXX compiler accepts flag -fdiagnostics-show-option
&gt; -- Checking to see if CXX compiler accepts flag -fdiagnostics-show-option - yes
&gt; -- Checking to see if CXX compiler accepts flag -Wl,--no-undefined
&gt; -- Checking to see if CXX compiler accepts flag -Wl,--no-undefined - yes
&gt; -- Checking to see if CXX compiler accepts flag -fstack-protector-all
&gt; -- Checking to see if CXX compiler accepts flag -fstack-protector-all - yes
&gt; -- Configuring VTK
&gt; --   Slicer_VTK_RENDERING_BACKEND is OpenGL2
&gt; --   Slicer_VTK_SMP_IMPLEMENTATION_TYPE is Sequential
&gt; --   Slicer_VTK_VERSION_MAJOR is 8
&gt; -- Looking for pthread.h
&gt; -- Looking for pthread.h - found
&gt; -- Performing Test CMAKE_HAVE_LIBC_PTHREAD
&gt; -- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
&gt; -- Looking for pthread_create in pthreads
&gt; -- Looking for pthread_create in pthreads - not found
&gt; -- Looking for pthread_create in pthread
&gt; -- Looking for pthread_create in pthread - found
&gt; -- Found Threads: TRUE  
&gt; -- Configuring Slicer with Qt 5.15.2 (using modules: Core, Widgets, Multimedia, Network, OpenGL, PrintSupport, UiTools, Xml, XmlPatterns, Svg, Sql, WebEngine, WebEngineWidgets, WebChannel, Script, Test, )
&gt; -- Setting QT_PLUGINS_DIR: /usr/lib/plugins
&gt; -- Setting QT_BINARY_DIR: /usr/lib/bin
&gt; -- 
&gt; -- Forcing Slicer_USE_SYSTEM_QT to ON (Qt5_DIR [/usr/lib/x86_64-linux-gnu/cmake/Qt5] associated with a system location: /usr/lib/)
&gt; -- 
&gt; -- Setting ExternalData_OBJECT_STORES to '/run/build/Slicer/_flatpak_build/ExternalData/Objects'
&gt; -- Configuring Slicer for [linux-amd64]
&gt; -- Using system QT
&gt; -- Found X11: /usr/include   
&gt; -- Looking for XOpenDisplay in /usr/lib/x86_64-linux-gnu/libX11.so;/usr/lib/x86_64-linux-gnu/libXext.so
&gt; -- Looking for XOpenDisplay in /usr/lib/x86_64-linux-gnu/libX11.so;/usr/lib/x86_64-linux-gnu/libXext.so - found
&gt; -- Looking for gethostbyname
&gt; -- Looking for gethostbyname - found
&gt; -- Looking for connect
&gt; -- Looking for connect - found
&gt; -- Looking for remove
&gt; -- Looking for remove - found
&gt; -- Looking for shmat
&gt; -- Looking for shmat - found
&gt; -- Looking for IceConnectionNumber in ICE
&gt; -- Looking for IceConnectionNumber in ICE - found
&gt; -- Found OpenGL: /usr/lib/x86_64-linux-gnu/libOpenGL.so  found components: OpenGL GLX 
&gt; -- Found Python3: /usr/bin/python3.8 (found suitable version "3.8.7", minimum required is "3.8") found components: Interpreter Development.Module Development.Embed 
&gt; -- Found FontConfig: /usr/lib/x86_64-linux-gnu/libfontconfig.so  
&gt; CMake Error at CMakeLists.txt:813 (find_package):
&gt;   Found package configuration file:
&gt; 
&gt;     /app/lib/cmake/vtk-9.0/vtk-config.cmake
&gt; 
&gt;   but it set VTK_FOUND to FALSE so package "VTK" is considered to be NOT
&gt;   FOUND.  Reason given by package:
&gt; 
&gt;   Could not find the VTK package with the following required components:
&gt;   GUISupportQtOpenGL.
&gt; 
&gt; 
&gt; 
&gt; -- Configuring incomplete, errors occurred!
</code></pre>
<p>It does not found GUISupportQtOpenGL. I assume that there are patch that were applied to when superbuild is enable to VTK that fix the issue?<br>
For Flatpak, superbuild are difficult to package, since superbuild will try to download packages, it will fail because Flathub does not allow that.</p>
<p>Are there patch file (.patch) that I can use? I can manually patch it.</p>
<p>Relate? <a href="https://github.com/Slicer/Slicer/issues/5339" class="inline-onebox" rel="noopener nofollow ugc">GUISupportQtOpenGL is deprecated in VTK9 · Issue #5339 · Slicer/Slicer · GitHub</a></p>
<p>Thanks<br>
Andy</p>

---

## Post #2 by @lassoan (2021-03-14 14:58 UTC)

<p>Thank you for working on this, it will be awesome.</p>
<p>Why don’t you use Slicer’s superbuild to take care of downloading and building all dependencies?</p>

---

## Post #3 by @Andythe_great (2021-03-14 16:28 UTC)

<p>Flathub (Flatpak store) does not allow network connection while building for the package to be reproducible. I can only download all package before hand.</p>

---

## Post #4 by @lassoan (2021-03-14 17:28 UTC)

<p>OK, then we need to download git repositories of all projects in advance and then pass their path to Slicer so that it uses those instead of downloading them. It may be enough to just specify Slicer_…_GIT_REPOSITORY CMake variable to point to the local git repository for each project (VTK, ITK, … all 40 projects in the SuperBuild subfolder; and for the few projects listed in SuperBuild.cmake) and build Slicer normally.</p>

---

## Post #5 by @Andythe_great (2021-03-14 17:52 UTC)

<p>I think that might work, will this be in the next 3D Slicer version?</p>
<p>I actually try to Flatpak Telesculptor too, but fail to build because superbuild method that need network. I need to hack around but unsuccessful.</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Kitware/TeleSculptor/issues/425" target="_blank" rel="noopener nofollow ugc">github.com/Kitware/TeleSculptor</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Kitware/TeleSculptor/issues/425" target="_blank" rel="noopener nofollow ugc">Build fail: Target "TeleSculptor" links to target "kwiver::kwiver_adapter" but the target was not found.</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-09" data-time="07:15:59" data-timezone="UTC">07:15AM - 09 Mar 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/kevinsmia1939" target="_blank" rel="noopener nofollow ugc">
          <img alt="kevinsmia1939" src="https://avatars.githubusercontent.com/u/11407922?v=4" class="onebox-avatar-inline" width="20" height="20">
          kevinsmia1939
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Hello,
I am trying to build Telesculptor for Linux Flatpak.
I got the error below.
I build Kwiver 1.5.1 with cmake with the flags,
...</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @Andythe_great (2021-03-14 18:13 UTC)

<p>Just successfully Flatpak Paraview, Paraview is easy because it does not use superbuild, pretty much self contain.</p>
<p>I do have graphical glitch in Paraview, this happen to Tomviz as well. Do you havesome clue?<br>
                        <a href="https://imgur.com/dJMnmEM" target="_blank" rel="noopener nofollow ugc" class="onebox">
              <img src="https://i.imgur.com/dJMnmEM.png" title="imgur.com" alt="Imgur" width="690" height="374">
            </a>

<br>
left flatpak, right tomviz binary<br>
                        <a href="https://imgur.com/UJSTa09" target="_blank" rel="noopener nofollow ugc" class="onebox">
              <img src="https://i.imgur.com/UJSTa09.png" title="Imgur: The magic of the Internet" alt="Imgur" width="690" height="388">
            </a>

</p>

---

## Post #7 by @lassoan (2021-03-15 04:52 UTC)

<p>Slicer superbuild does not need network connection if you download the git repositories in advance.</p>
<p>The rendering error is probably an issue in VTK (or maybe due to an error in your graphics driver). Report it to ParaView developers.</p>

---

## Post #8 by @Andythe_great (2021-03-15 08:03 UTC)

<p>Where must I put the pre-download dependencies? Must it be unpack or kept as archive?</p>

---

## Post #9 by @RafaelPalomar (2021-03-16 14:34 UTC)

<p>I agree with <a class="mention" href="/u/lassoan">@lassoan</a>. This can be really good for Linux users!</p>
<p>It might make sense to try to break the superbuild for this (<code>Slicer_SUPERBUILD=OFF</code>). I don’t know much about flatpacks, but if they provide a sandboxed environment, maybe the Slicer app launcher could be disabled in favor of the sandboxed environment.</p>

---

## Post #10 by @lassoan (2021-03-16 16:02 UTC)

<p>I would not recommend to deviate too much from the standard build and runtime environment, because even if somebody finds the time to implement the changes once, it will be very hard to maintain it.</p>
<p>The main problem of requiring network access during superbuild can be resolved by downloading the git repositories in advance and passing them as build options. This does not require any change in Slicer. I would expect that we’ll need to figure out something for bundled Python packages, too (is it OK to download pre-built wheels?).</p>

---

## Post #11 by @Andythe_great (2021-03-17 16:33 UTC)

<p>It is ok to download prebuild wheels as well.<br>
Could you clarify where must the pre-download deps be? Must it be archive or unpack? What should their archive or folder name be?</p>

---

## Post #12 by @jcfr (2021-03-17 20:08 UTC)

<p>To move forward, the following need to be done:</p>
<ol>
<li>support local download git repository</li>
<li>support download the applauncher</li>
<li>support local download and use of python wheels</li>
<li>update remaining external project to support passing local directory</li>
<li>support local download of remote dependencies download using <code>Slicer_Remote_Add</code>. (see <a href="https://github.com/Slicer/Slicer/blob/master/SuperBuild.cmake#L200">here</a>)</li>
<li>configure Slicer with relevant variables</li>
</ol>
<p>For (1) and (2), scripts are provided below.</p>
<p>For (3):</p>
<ul>
<li>list of dependencies are already described in external projects file of the form <code>External_python-*-requirements.cmake</code>
</li>
<li>
<a class="mention" href="/u/jamesobutler">@jamesobutler</a> created a script that provides a good base to support extracting these. (see <a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Scripts/python_package_updater.py">Utilities/Scripts/python_package_updater.py</a>)</li>
</ul>
<p>For (4), these external files need to be updated to allow passing local file path:</p>
<pre><code class="lang-auto">External_python.cmake
External_OpenSSL.cmake
External_PCRE.cmake
External_tbb.cmake
External_Swig.cmake
External_CTKResEdit.cmake  # Only used on windows
</code></pre>
<p>For (5), it should be easy to instrument the relevant CMake functions.</p>
<h2>(1) download git repositories</h2>
<p><em><strong>Note:</strong>  this is a partial list, we will likely have to update the build system to be more exhaustive</em></p>
<p>I suggest the following:</p>
<ul>
<li>Checkout dependencies  in local directory (script below should help)</li>
<li>Then, configure Slicer passing the following variables:</li>
</ul>
<pre><code class="lang-auto">-DSlicer_zlib_GIT_REPOSITORY=file:///tmp/zlib
-DSlicer_curl_GIT_REPOSITORY=file:///tmp/curl
-DSlicer_CTKAppLauncherLib_GIT_REPOSITORY=file:///tmp/CTKAppLauncherLib
-DSlicer_bzip2_GIT_REPOSITORY=file:///tmp/bzip2
-DSlicer_LZMA_GIT_REPOSITORY=file:///tmp/LZMA
-DSlicer_sqlite_GIT_REPOSITORY=file:///tmp/sqlite
-DSlicer_python_GIT_REPOSITORY=file:///tmp/python
-DSlicer_VTK_GIT_REPOSITORY=file:///tmp/VTK
-DSlicer_teem_GIT_REPOSITORY=file:///tmp/teem
-DSlicer_DCMTK_GIT_REPOSITORY=file:///tmp/DCMTK
-DSlicer_ITK_GIT_REPOSITORY=file:///tmp/ITK
-DSlicer_CTK_GIT_REPOSITORY=file:///tmp/CTK
-DSlicer_LibArchive_GIT_REPOSITORY=file:///tmp/LibArchive
-DSlicer_RapidJSON_GIT_REPOSITORY=file:///tmp/RapidJSON
-DSlicer_SimpleITK_GIT_REPOSITORY=file:///tmp/SimpleITK
-DSlicer_JsonCpp_GIT_REPOSITORY=file:///tmp/JsonCpp
-DSlicer_ParameterSerializer_GIT_REPOSITORY=file:///tmp/ParameterSerializer
-DSlicer_SlicerExecutionModel_GIT_REPOSITORY=file:///tmp/SlicerExecutionModel
-DSlicer_qRestAPI_GIT_REPOSITORY=file:///tmp/qRestAPI
</code></pre>
<p>Here is a short script to help download dependencies:</p>
<pre><code class="lang-bash">#!/bin/bash

set -eo pipefail

# See https://discourse.slicer.org/t/interest-to-create-flatpak-for-3d-slicer-have-issue-with-guisupportqtopengl-not-found/16532

PROG=$(basename $0)

SLICER_DEPENDENCIES_DIR=/tmp

#
# Dependencies associated with Slicer d234b7ee9 from 2021.03.17
# See https://github.com/Slicer/Slicer/commit/d234b7ee9dd6f7ab7ed7d141c08db05f9e20a3d9
#

slicer_git_dependencies_file=${SLICER_DEPENDENCIES_DIR}/slicer_git_dependencies
cat &lt;&lt; EOF &gt; ${slicer_git_dependencies_file}
Slicer_zlib_GIT_REPOSITORY=git://github.com/commontk/zlib.git
Slicer_zlib_GIT_TAG=66a753054b356da85e1838a081aa94287226823e
Slicer_curl_GIT_REPOSITORY=git://github.com/Slicer/curl.git
Slicer_curl_GIT_TAG=ca5fe8e63df7faea0bfb988ef3fe58f538e6950b
Slicer_CTKAppLauncherLib_GIT_REPOSITORY=git://github.com/commontk/AppLauncher.git
Slicer_CTKAppLauncherLib_GIT_TAG=1367de4c6efde0c11e87835fb7245ea2b05074aa
Slicer_bzip2_GIT_REPOSITORY=git://github.com/commontk/bzip2.git
Slicer_bzip2_GIT_TAG=0e735f23032ececcf52ed49b27928390fff28e50
Slicer_LZMA_GIT_REPOSITORY=git://github.com/Slicer/lib_lzma.git
Slicer_LZMA_GIT_TAG=v5.2.2
Slicer_sqlite_GIT_REPOSITORY=git://github.com/azadkuh/sqlite-amalgamation.git
Slicer_sqlite_GIT_TAG=3.30.1
Slicer_python_GIT_REPOSITORY=git://github.com/python-cmake-buildsystem/python-cmake-buildsystem.git
Slicer_python_GIT_TAG=dca8bee81e29b452560bd969d67e7d08237e23d6
Slicer_VTK_GIT_REPOSITORY=git://github.com/slicer/VTK.git
Slicer_VTK_GIT_TAG=1076d8bc00f12c49af4e35a3e0e58beae6ad361b
Slicer_teem_GIT_REPOSITORY=git://github.com/Slicer/teem
Slicer_teem_GIT_TAG=e4746083c0e1dc0c137124c41eca5d23adf73bfa
Slicer_DCMTK_GIT_REPOSITORY=git://github.com/commontk/DCMTK.git
Slicer_DCMTK_GIT_TAG=patched-DCMTK-3.6.6_20210115
Slicer_ITK_GIT_REPOSITORY=git://github.com/InsightSoftwareConsortium/ITK
Slicer_ITK_GIT_TAG=2b34388159c20c0a6334d9b174fc6c230853988c
Slicer_CTK_GIT_REPOSITORY=git://github.com/commontk/CTK.git
Slicer_CTK_GIT_TAG=9a9573ec4e0653ee96fe02823ac7ee66b40d3b44
Slicer_LibArchive_GIT_REPOSITORY=git://github.com/libarchive/libarchive.git
Slicer_LibArchive_GIT_TAG=34940ef6ea0b21d77cb501d235164ad88f19d40c
Slicer_RapidJSON_GIT_REPOSITORY=git://github.com/miloyip/rapidjson.git
Slicer_RapidJSON_GIT_TAG=v1.1.0
Slicer_SimpleITK_GIT_REPOSITORY=git://github.com/SimpleITK/SimpleITK.git
Slicer_SimpleITK_GIT_TAG=460f9c1553621b649f376bb1c07c94d4bdf6f055
Slicer_JsonCpp_GIT_REPOSITORY=git://github.com/Slicer/jsoncpp.git
Slicer_JsonCpp_GIT_TAG=73b8e172d6615251ef851d883ef02f163e7075b2
Slicer_ParameterSerializer_GIT_REPOSITORY=git://github.com/Slicer/ParameterSerializer.git
Slicer_ParameterSerializer_GIT_TAG=70e95f1cdee52cc49dfc3375e956a8f5958240c7
Slicer_SlicerExecutionModel_GIT_REPOSITORY=git://github.com/Slicer/SlicerExecutionModel.git
Slicer_SlicerExecutionModel_GIT_TAG=f19d6e88a94ba8f31ddafcff4adf185fe90d7e72
Slicer_qRestAPI_GIT_REPOSITORY=git://github.com/commontk/qRestAPI.git
Slicer_qRestAPI_GIT_TAG=ddc0cfcc220d0ccd02b4afdd699d1e780dac3fa3

EOF

#
# List of variable obtained by locally modifying "ExternalProject_SetIfNotDefined"
#
# Patch:
#
# diff --git a/CMake/ExternalProjectDependency.cmake b/CMake/ExternalProjectDependency.cmake
# index 0f775d3ff0..c9a77856de 100644
# --- a/CMake/ExternalProjectDependency.cmake
# +++ b/CMake/ExternalProjectDependency.cmake
# @@ -1055,6 +1055,7 @@ macro(ExternalProject_SetIfNotDefined var defaultvalue)
#      endif()
#      set(${var} "${defaultvalue}")
#    endif()
# +  message(STATUS "${var}=${${var}}")
#  endmacro()
# 
#  #.rst:

# Collect project names
for entry in $(cat "${slicer_git_dependencies_file}" | grep "GIT_REPOSITORY"); do
  proj=$(echo ${entry} | cut -d= -f1 | cut -d_ -f2)
  repo=$(echo ${entry} | cut -d= -f2)
  sha=$(cat "${slicer_git_dependencies_file}" | grep ${proj}_GIT_TAG | cut -d= -f2)
  if [[ ! -d "${SLICER_DEPENDENCIES_DIR}/${proj}" ]]; then
    git clone ${repo} ${proj}
  fi
  (cd ${proj}; git fetch --tags origin; git reset --hard HEAD; git checkout ${sha})
  break
done

# List of options to configure Slicer
for entry in $(cat "${slicer_git_dependencies_file}" | grep "GIT_REPOSITORY"); do
  varname=$(echo ${entry} | cut -d= -f1)
  proj=$(echo ${entry} | cut -d= -f1 | cut -d_ -f2)
  local_path=${SLICER_DEPENDENCIES_DIR}/${proj}
  echo "-D${varname}=file://${local_path}"
done
</code></pre>
<h2>(2) download launcher</h2>
<p>Here are the steps:</p>
<ol>
<li>download launcher using script below</li>
<li>configure Slicer passing option <code>CTKAppLauncher_DIR</code>
</li>
</ol>
<p>Option to pass (as of Slicer d234b7ee9 from 2021.03.17):</p>
<pre><code class="lang-auto">-DCTKAppLauncher_DIR:PATH=/tmp/CTKAppLauncher-0.1.29-linux-amd64
</code></pre>
<p>Script:</p>
<pre><code class="lang-bash">
SLICER_DEPENDENCIES_DIR=/tmp

# Dependencies associated with Slicer d234b7ee9 from 2021.03.17
# See https://github.com/Slicer/Slicer/commit/d234b7ee9dd6f7ab7ed7d141c08db05f9e20a3d9

launcher_version=0.1.29

name=CTKAppLauncher-${launcher_version}-linux-amd64
curl -L# https://github.com/commontk/AppLauncher/releases/download/v${launcher_version}/${name}.tar.gz -o  ${name}.tar.gz
tar -xzvf ${name}.tar.gz

echo "-DCTKAppLauncher_DIR:PATH=${SLICER_DEPENDENCIES_DIR}/${name}"
</code></pre>
<p><em><code>launcher_version</code> can be discovered looking at <a href="https://github.com/Slicer/Slicer/blob/master/SuperBuild/External_CTKAPPLAUNCHER.cmake#L24-L46">External_CTKAPPLAUNCHER.cmake#L24-L46</a></em></p>

---

## Post #13 by @Andythe_great (2021-03-19 14:10 UTC)

<p>Thanks for the help. It looks good, I have nothing to add, let me know if it ready to be test.</p>

---

## Post #14 by @luarpy (2023-01-20 11:57 UTC)

<p>Has there been any progress? Do you need help?</p>

---

## Post #15 by @jamesobutler (2023-01-20 13:18 UTC)

<p>There hasn’t been much progress on this as far as I know. There also hasn’t been a large number of users in the community asking for it either. The Slicer community has primarily accepted going to <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a> to get the latest Stable release and latest Preview builds of Slicer.</p>
<p>If you’re interested in the project, feel free to help out! You will likely have to become the maintainer of this moving forward as well since sometimes things like this get working for one version, but then never maintained for future versions.</p>
<p>Regarding networkless builds I suggest you first read the conversation at <a href="https://github.com/commontk/CTK/issues/1047" class="inline-onebox" rel="noopener nofollow ugc">Plans for a new release? · Issue #1047 · commontk/CTK · GitHub</a> which has some recent thoughts on the topic of Slicer using custom versions of various dependencies rather than an OS level set of dependencies.</p>
<p>There is also a Slicer GitHub issue detailing the networkless support:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5271">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5271" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5271" target="_blank" rel="noopener nofollow ugc">Support networkless builds (i.e., let the superbuild use pre-downloaded sources)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-10-27" data-time="15:42:01" data-timezone="UTC">03:42PM - 27 Oct 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/twhitehead" target="_blank" rel="noopener nofollow ugc">
          <img alt="twhitehead" src="https://avatars.githubusercontent.com/u/787843?v=4" class="onebox-avatar-inline" width="20" height="20">
          twhitehead
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Systems like NixOS build in isolated build environments (i.e., no network access<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">) to strictly control dependencies in order to ensure reproducible builds. I spend some time trying to get slicer to build for this sort of environment, and have had a horrible time.

First I tried to build without the superbuild (setting `-DSlicer_SUPERBUILD=OFF` and then working through the issues that arose) and discovered that this had essentially become an unsupported option. While it has been awhile since I gave up on this approach, I believe the final issue that did me in was discovering that there are dependencies that simply no longer support being built outside of the superbuild.

Accepting the superbuild, even though it really sucks to not be able to use your regular system versions of core packages when possible, I switched to trying to get it to stop trying to download sources and instead use (the exact same version/git clone) of the sources that I provided. The only way to do this seemed to be to hack the cmake files one by one though, and this eventually also wore me down.

Which brings me to opening a bug report and asking the developers if it would be possible to tweaked the system to support networkless builds using pre-downloaded sources. :grin:</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #16 by @luarpy (2023-01-20 16:57 UTC)

<p>Thank you very much for the information. And it is a problem of modern software to have dependencies in so many projects, especially if there is a different version per linux distribution.</p>
<p>To be able to maintain it, I think I would have to be a direct participant of the <a href="http://Slicer.org" rel="noopener nofollow ugc">Slicer.org</a> project because now the Flatpak platform or at least the <a href="http://flathub.org" rel="noopener nofollow ugc">flathub.org</a> repository <a href="https://github.com/flathub/flathub/wiki/App-Submission" rel="noopener nofollow ugc">allows only to publish</a> the packaged application for the authors of the original software.</p>
<p>Nevertheless, I think it would be an important step forward to continue with the task of transporting it to a framework such as flatpak to facilitate access to different users for this application.</p>

---

## Post #17 by @muratmaga (2023-01-20 17:37 UTC)

<aside class="quote no-group" data-username="luarpy" data-post="16" data-topic="16532">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luarpy/48/67016_2.png" class="avatar"> luarpy:</div>
<blockquote>
<p>Nevertheless, I think it would be an important step forward to continue with the task of transporting it to a framework such as flatpak to facilitate access to different users for this application.</p>
</blockquote>
</aside>
<p>While having a stable flatpak makes sense, there is no point for preview versions, which change nightly. The other issue, is it even possible to install Slicer in a single read/only location (e.g., /usr/local/Slicer) and have the user files (extensions, pip packages) etc go in a local folder?</p>

---

## Post #18 by @RafaelPalomar (2023-01-21 09:22 UTC)

<p>I would like to see this happening and I definitely could contribute to this. I’m not acquainted with Flatkpaks, but in general terms, there are two issues that complicate the integration of 3D Slicer with package systems:</p>
<ul>
<li>
<p>One of the issues (as pointed out earlier in the thread and in the reference provided by <a class="mention" href="/u/jamesobutler">@jamesobutler</a>) is the superbuild approach, as many packaging systems require network isolation. In the <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SystoleOS/" rel="noopener nofollow ugc">SystoleOS</a> project, we have the same issue and have been advancing on building 3D Slicer without the superbuild (so far, Slicer without python support is available). I hope for further advances during <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/" rel="noopener nofollow ugc">PW38</a>.</p>
</li>
<li>
<p>Another issue is the divergence of some of the underlying dependencies from the official projects (most notably VTK, and to a minor degree, ITK). This makes difficult the co-existence of Slicer and other projects without some isolation mechanisms.</p>
</li>
</ul>
<p>It may be possible to hack our way through (i.e., repo injection, etc) to make a Flatpack with the superbuild (<a class="mention" href="/u/jcfr">@jcfr</a> posted some snippets earlier in this thread). In my view, it would be better to invest some effort to make 3D Slicer possible to build without the superbuild as this will improve the overall quality of the 3D Slicer project and facilitate other packaging approaches beyond Flatpak and GNU/Linux systems.</p>

---

## Post #19 by @Andythe_great (2023-01-25 13:44 UTC)

<p>There is not much progress since last time because Slicer relies on super build. I think when Slicer can build without network, it would be much easier to build and maintain Slicer flatpak.</p>

---

## Post #20 by @luarpy (2023-02-05 11:34 UTC)

<p>Hi Andy,<br>
I would like to be able to package Slicer inside with flatpak. Could you share the progress you made or comment on how far you got to go from there?<br>
Thanks a lot</p>

---

## Post #21 by @RafaelPalomar (2023-02-06 11:15 UTC)

<p><a class="mention" href="/u/andythe_great">@Andythe_great</a>, <a class="mention" href="/u/luarpy">@luarpy</a> we celebrated PW38 last week and we got good progress in the <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SystoleOS/" rel="noopener nofollow ugc">SystoleOS</a> project. Most of this progress can be utilized for breaking the superbuild. I could support this initiative by transferring this and any future progress in the SystoleOS (and more, if needed).</p>

---

## Post #22 by @luarpy (2023-02-06 15:09 UTC)

<p><a class="mention" href="/u/andythe_great">@Andythe_great</a> <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> where would you like to maintain the project progress and comunication?</p>

---

## Post #23 by @luarpy (2023-02-06 19:31 UTC)

<p>I have been thinking about how we might approach this case. It seems to me that while we try to solve the superbuild issue in Slicer, which doesn’t work, we could adapt the configuration files and download the dependencies through several scripts launched from a main one.</p>
<p>This way we do not force changes in the original project files and make only the right changes for this particular case. The changes should be no more than indicating where the dependencies are located with respect to the packaging path.</p>
<p>Then we would only have to apply the packaging via flatpak and everything should be fine (I’m sure bugs will come up during the process).</p>

---

## Post #24 by @RafaelPalomar (2023-02-07 09:08 UTC)

<p>I have created this repo and given <a class="mention" href="/u/luarpy">@luarpy</a> full access</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/RafaelPalomar/Slicer-Flatpak">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/RafaelPalomar/Slicer-Flatpak" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/e783c497806c9a1be5a0e25266242e40a6f14b16190cc3bdf8631798cddfef89/RafaelPalomar/Slicer-Flatpak" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/RafaelPalomar/Slicer-Flatpak" target="_blank" rel="noopener nofollow ugc">RafaelPalomar/Slicer-Flatpak</a></h3>

  <p>Flatpak for 3D Slicer. Contribute to RafaelPalomar/Slicer-Flatpak development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>As there are still some uncertainties related to the development and the maintenance of this project I think it is prudent to have it as a separate project. We can discuss with the Slicer core developers if at some point this could be integrated in the Slicer organization. <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a>, do you think this is a good plan?</p>

---

## Post #25 by @RafaelPalomar (2023-02-07 09:22 UTC)

<aside class="quote no-group" data-username="luarpy" data-post="23" data-topic="16532">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luarpy/48/67016_2.png" class="avatar"> luarpy:</div>
<blockquote>
<p>we could adapt the configuration files and download the dependencies through several scripts launched from a main one</p>
</blockquote>
</aside>
<p>I have quickly scanned the Flatpak documentation and found this info about <strong>bundled dependencies</strong> (<a href="https://docs.flatpak.org/en/latest/dependencies.html" class="inline-onebox" rel="noopener nofollow ugc">Dependencies — Flatpak documentation</a>):</p>
<pre data-code-wrap="txt"><code class="lang-txt">As will be seen, bundled dependencies can be automatically 
downloaded as part of the build process. It is also possible 
to apply patches and perform other transformations.
</code></pre>
<p>Having bundled dependencies directly linked to the repositories used by the Slicer superbuild and the SystoleOS <strong>patches</strong> available in the <a href="https://github.com/SystoleOS/gentoo-overlay" rel="noopener nofollow ugc">SystoleOS/gentoo-overlay</a> repository is one possibility. In the SystoleOS project we are trying to contribute all these patches to 3D Slicer, but some of them might take time and some others might not even be accepted.</p>

---

## Post #26 by @luarpy (2023-02-07 10:36 UTC)

<p>Yesterday I was preparing some of the main files: manifest.yaml (also the one made by <a class="mention" href="/u/andythe_great">@Andythe_great</a>), icon image and *.destkop file. All according to flatpak format. So I can do a push to start with something.</p>
<p>I also have a script I was preparing to automate the configuration process prior to packaging.</p>
<aside class="quote quote-modified" data-post="25" data-topic="16532">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/interest-to-create-flatpak-for-3d-slicer-have-issue-with-guisupportqtopengl-not-found/16532/25">Interest to create Flatpak for 3D Slicer, have issue with GUISupportQtOpenGL not found</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have quickly scanned the Flatpak documentation and found this info about bundled dependencies (<a href="https://docs.flatpak.org/en/latest/dependencies.html" class="inline-onebox-loading" rel="noopener nofollow ugc">https://docs.flatpak.org/en/latest/dependencies.html</a>): 
As will be seen, bundled dependencies can be automatically 
downloaded as part of the build process. It is also possible 
to apply patches and perform other transformations.

Having bundled dependencies directly linked to the repositories used by the Slicer superbuild and the SystoleOS patches available in the <a href="https://github.com/SystoleOS/gentoo-overlay" rel="noopener nofollow ugc">SystoleOS/gentoo-overlay</a> repositor…
  </blockquote>
</aside>

<p>On the subject of what you indicate, I also read it but I did not understand how or what is meant by these libraries. I would have liked to find an example showing how to indicate the libraries to download.</p>

---

## Post #27 by @RafaelPalomar (2023-02-07 10:55 UTC)

<p><a class="mention" href="/u/luarpy">@luarpy</a>, this is great.</p>
<aside class="quote no-group" data-username="luarpy" data-post="26" data-topic="16532">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luarpy/48/67016_2.png" class="avatar"> luarpy:</div>
<blockquote>
<p>On the subject of what you indicate, I also read it but I did not understand how or what is meant by these libraries. I would have liked to find an example showing how to indicate the libraries to download.</p>
</blockquote>
</aside>
<p>Here is a ChatGPT-generated manifest bundling an ITK and a VTK. Does it look plausible? Keep in mind that we need to use Slicer/VTK  and Slicer/ITK instead of vanilla ITK and VTK:</p>
<pre data-code-wrap="yaml"><code class="lang-yaml">{
  "app-id": "org.example.app",
  "runtime": "org.freedesktop.Platform",
  "runtime-version": "20.08",
  "sdk": "org.freedesktop.Sdk",
  "command": "app",
  "finish-args": [
    "--socket=x11",
    "--device=dri",
    "--filesystem=host"
  ],
  "modules": [
    {
      "name": "ITK",
      "buildsystem": "simple",
      "build-commands": [
        "wget https://github.com/InsightSoftwareConsortium/ITK/releases/download/v5.1.2/InsightToolkit-5.1.2.tar.gz",
        "tar -xzf InsightToolkit-5.1.2.tar.gz",
        "cd InsightToolkit-5.1.2",
        "mkdir build",
        "cd build",
        "cmake ..",
        "make",
        "make install DESTDIR=${FLATPAK_DEST}"
      ],
      "sources": [
        {
          "type": "file",
          "path": "InsightToolkit-5.1.2.tar.gz"
        }
      ]
    },
    {
      "name": "VTK",
      "buildsystem": "simple",
      "build-commands": [
        "wget https://github.com/Kitware/VTK/releases/download/v10.3.1/VTK-10.3.1.tar.gz",
        "tar -xzf VTK-10.3.1.tar.gz",
        "cd VTK-10.3.1",
        "mkdir build",
        "cd build",
        "cmake ..",
        "make",
        "make install DESTDIR=${FLATPAK_DEST}"
      ],
      "sources": [
        {
          "type": "file",
          "path": "VTK-10.3.1.tar.gz"
        }
      ]
    }
  ]
}
</code></pre>
<p>Getting this to work would be a good starting point.  I hope we can rely on the stock Flatpak runtime system for everything below VTK. This is de dependency graph for Slicer on SystoleOS (no python support yet):</p>
<pre data-code-wrap="txt"><code class="lang-txt"> * dependency graph for sci-medical/Slicer-9999
 `--  sci-medical/Slicer-9999
   `--  sci-medical/ctk-0.1.0  (sci-medical/ctk)   [python]
   `--  sci-libs/vtkAddon-0.1.0  (sci-libs/vtkAddon)   [python]
   `--  dev-qt/qtcore-5.15.8-r1  (dev-qt/qtcore) amd64
   `--  dev-qt/linguist-tools-5.15.8  (dev-qt/linguist-tools) amd64
   `--  dev-qt/qtmultimedia-5.15.8  (dev-qt/qtmultimedia) amd64  [widgets]
   `--  dev-qt/qtopengl-5.15.8  (dev-qt/qtopengl) amd64
   `--  dev-qt/qtsql-5.15.8  (dev-qt/qtsql) amd64
   `--  dev-qt/qtxmlpatterns-5.15.8  (dev-qt/qtxmlpatterns) amd64
   `--  dev-qt/qtx11extras-5.15.8  (dev-qt/qtx11extras) amd64
   `--  dev-qt/qtsvg-5.15.8  (dev-qt/qtsvg) amd64
   `--  dev-qt/qtwebengine-5.15.8_p20230112  (dev-qt/qtwebengine) amd64
   `--  dev-qt/qtwebchannel-5.15.8  (dev-qt/qtwebchannel) amd64
   `--  dev-qt/qtscript-5.15.8  (dev-qt/qtscript) amd64
   `--  dev-qt/designer-5.15.8  (dev-qt/designer) amd64
   `--  dev-libs/rapidjson-1.1.0-r3  (dev-libs/rapidjson) amd64
   `--  dev-libs/jsoncpp-1.9.5  (dev-libs/jsoncpp) amd64
   `--  dev-libs/qRestAPI-9999  (dev-libs/qRestAPI) ~amd64
   `--  sci-medical/CTKAppLauncherLib-1.0.0  (sci-medical/CTKAppLauncherLib) ~amd64
   `--  sci-medical/teem-1.12.0  (sci-medical/teem) ~amd64
   `--  Slicer-CLI/SlicerExecutionModel-1.0.0  (Slicer-CLI/SlicerExecutionModel)
   `--  sci-libs/itk-5.3.0  (sci-libs/itk)   [vtkglue deprecated]
   `--  sci-libs/vtk-9.1.0  (&gt;=sci-libs/vtk-9.1.0)   [qt5 rendering gl2ps]
   `--  dev-util/cmake-3.24.3  (&gt;=dev-util/cmake-3.23.1) amd64
   `--  dev-util/ninja-1.11.1-r2  (&gt;=dev-util/ninja-1.8.2) amd64
   `--  dev-vcs/git-2.39.1  (&gt;=dev-vcs/git-1.8.2.1) amd64  [curl]
</code></pre>

---

## Post #28 by @luarpy (2023-02-07 11:01 UTC)

<p>It is the most unexpected answer possible hahahahahaha <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=12" title=":rofl:" class="emoji" alt=":rofl:" loading="lazy" width="20" height="20">. It seems to be fine but needs some changes. I wrote it in YAML because it allows to add comments to the document.</p>
<p>This is what I wrote based in the documentation of flatpak and using the <a href="https://github.com/flathub/io.github.nroduit.Weasis" rel="noopener nofollow ugc">Weasis Flatpak</a> project as an example:</p>
<pre><code class="lang-auto">app-id: org.slicer.Slicer
runtime: org.freedesktop.Platform
runtime: '22.08'
sdk: org.freedesktop.Sdk
base-version: '22.08'
command: slicer
finish-args:
  # X11 + XShm access
  - --share=ipc
  - --socker=x11
  # Wayland access
  - --socket=wayland
  # Needs to talk to the network:
  - --share=network
  # Needs to save files locally
  - --filesystem=xdg-documents
  - --filesystem=xdg-download

modules:
  - name: VTK
    buildsystem: cmake
    builddir: true
    config-opts:
    - -DVTK_BUILD_ALL_MODULES=OFF 
    - -DBUILD_SHARED_LIBS=YES
    - -DOpenGL_GL_PREFERENCE=LEGACY
    - -DVTK_WRAP_JAVA=OFF
    - -DVTK_WRAP_PYTHON=YES
    - -DVTK_PYTHON_VERSION:STRING=3
    - -DVTK_GROUP_ENABLE_Qt=YES
    - -DVTK_GROUP_ENABLE_Views=YES
    - -DVTK_MODULE_ENABLE_VTK_GUISupportQt=YES
    - -DVTK_MODULE_ENABLE_VTK_GUISupportQtOpenGL=YES
    - -DVTK_MODULE_ENABLE_VTK_RenderingContextOpenGL2=YES
    - -DVTK_MODULE_ENABLE_VTK_RenderingFreeTypeFontConfig=YES
    - -DVTK_MODULE_ENABLE_VTK_RenderingQt=YES
    - -DVTK_MODULE_ENABLE_VTK_GUISupportQtSQL=YES
    - -DVTK_MODULE_ENABLE_VTK_FiltersExtraction=YES
    - -DVTK_MODULE_ENABLE_VTK_FiltersFlowPaths=YES
    - -DVTK_MODULE_ENABLE_VTK_FiltersGeometry=YES
    - -DVTK_MODULE_ENABLE_VTK_FiltersParallel=YES
    - -DVTK_MODULE_ENABLE_VTK_IOExport=YES
    - -DVTK_MODULE_ENABLE_VTK_IOImage=YES
    - -DVTK_MODULE_ENABLE_VTK_IOLegacy=YES
    - -DVTK_MODULE_ENABLE_VTK_IOPLY=YES
    - -DVTK_MODULE_ENABLE_VTK_IOXML=YES
    - -DVTK_MODULE_ENABLE_VTK_ImagingMath=YES
    - -DVTK_MODULE_ENABLE_VTK_ImagingMorphological=YES
    - -DVTK_MODULE_ENABLE_VTK_ImagingStatistics=YES
    - -DVTK_MODULE_ENABLE_VTK_ImagingStencil=YES
    - -DVTK_MODULE_ENABLE_VTK_InteractionImage=YES
    - -DVTK_MODULE_ENABLE_VTK_RenderingVolumeOpenGL2=YES
    - -DVTK_MODULE_ENABLE_VTK_TestingRendering=YES
    - -DVTK_MODULE_ENABLE_VTK_ViewsQt=YES
    - -DVTK_MODULE_ENABLE_VTK_zlib=YES
    #cleanup:
      #- /bin
    sources:
      - type: archive
        url: https://www.vtk.org/files/release/9.0/VTK-9.0.3.tar.gz
        sha256: bc3eb9625b2b8dbfecb6052a2ab091fc91405de4333b0ec68f3323815154ed8a

  - name: CTK
    buildsystem: cmake
    builddir: true
    config-opts:
      - -DCMAKE_BUILD_TYPE:STRING=Release
      - -DCTK_QT_VERSION=5
      - -DCTK_BUILD_SHARED_LIBS=ON
      - -DBUILD_TESTING=OFF
      - -DCTK_SUPERBUILD=OFF
      - -DCTK_ENABLE_DICOM=OFF
      - -DCTK_ENABLE_PluginFramework=ON
      - -DCTK_ENABLE_Widgets=ON
    sources:
      - type: git
        url: git://github.com/commontk/CTK.git
        commit: ec9fcee532fd9cdff74f96479197f626d8c71fe5

  - name: CTK-PythonQt
    buildsystem: cmake
    config-opts:
      - -DPythonQt_Wrap_QtAll=ON
    sources:
      - type: git
        url: git://github.com/commontk/PythonQt.git
        branch: patched-9
        
  - name: Slicer
    buildsystem: cmake
    builddir: true
    config-opts:
      - -DCMAKE_BUILD_TYPE:STRING=Release
      - -DSlicer_VTK_VERSION_MAJOR=9

    build-options:
      build-args:
    
    build-commands:
      - mkdir -p build
      - cd build
      - cmake ../Slicer/Slicer
      - make
      - mv Slicer-build/* ../app/
      - install -D slicer.png /app/share/icons/hicolor/400x400/apps/org.slicer.Slicer.png
      - install -D -t /app/share/applications/ org.slicer.Slicer.desktop
    sources:
      - type: file
        path: org.slicer.Slicer.desktop
      - type: file
        path: org.slicer.Slicer.png
      - type: git
        url: git://github.com/Slicer/Slicer.git
        tag: main
</code></pre>

---

## Post #29 by @RafaelPalomar (2023-02-07 11:08 UTC)

<p>A good mix of the two is a good start. Would you mind to make it a PR so I can give it a shot? As I see the problem now we can go a long way by translating the SystoleOS packages to this yaml representation.</p>

---

## Post #30 by @RafaelPalomar (2023-02-16 09:37 UTC)

<p>UPDATE: Based on the discussion held on <a href="https://discourse.slicer.org/t/2023-02-07-weekly-meeting/27680" class="inline-onebox">2023.02.07 Weekly Meeting</a> with the Slicer core devs, it seems reasonable to try approaching the Slicer flatpak <strong>under a  superbuild</strong> approach rather than a non-superbuild as I initially proposed. Reasons: (1) some of the SystoleOS patches may take time to land on the Slicer code base, some might not even make it; (2) the distributed Slicer should be the same (or very similar) regardless of whether this is a flatpak or a redistributable linux binary, as of today this a superbuild-based.</p>
<p><a class="mention" href="/u/luarpy">@luarpy</a> and <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> have started putting together a Flatpak manifest generator for Slicer (this is needed to set the right versions for the dependencies in the manifest) in here: <a href="https://github.com/RafaelPalomar/Slicer-Flatpak" class="inline-onebox" rel="noopener nofollow ugc">GitHub - RafaelPalomar/Slicer-Flatpak: Flatpak for 3D Slicer</a>. The final manifest will go on its own repository (so far, <a href="https://github.com/RafaelPalomar/org.slicer.Slicer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - RafaelPalomar/org.slicer.Slicer: Flatpak repository for Slicer</a>). It is still a non-usable work-in-progress, where we try to reproduce the suggestions above by <a class="mention" href="/u/jcfr">@jcfr</a>.</p>

---

## Post #31 by @lassoan (2023-02-16 12:28 UTC)

<p>It is great to see all the progress with the build. I can help with runtime questions. More specifically: what folders can be read-only and what temporary and persistent writable folders we need for application settings, extensions, Python packages, DICOM database, cached downloads, etc.</p>

---

## Post #32 by @RafaelPalomar (2023-02-16 15:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="31" data-topic="16532">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I can help with runtime questions</p>
</blockquote>
</aside>
<p>This is great <a class="mention" href="/u/lassoan">@lassoan</a>, thank you. For sure we will need help to deal with the runtime configuration. We’ll keep updating on the progress of this.</p>

---

## Post #33 by @RafaelPalomar (2023-02-23 12:01 UTC)

<p>I leave two interesting pieces of information I found recently:</p>
<ol>
<li>I don’t think it would affect this development, but <strong>Ubuntu is planning to drop Flatpak integration by default</strong> (users will still be able to install the support manually as it is for many other distributions). More information on this post:</li>
</ol>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.ubuntu.com/t/ubuntu-flavor-packaging-defaults/34061?u=d0od">
  <header class="source">
      <img src="https://ubuntucommunity.s3.dualstack.us-east-2.amazonaws.com/optimized/1X/fac87fdcf2e670741a9896b80966da69d06eceab_2_32x32.png" class="site-icon" width="" height="">

      <a href="https://discourse.ubuntu.com/t/ubuntu-flavor-packaging-defaults/34061?u=d0od" target="_blank" rel="noopener nofollow ugc" title="12:34PM - 21 February 2023">Ubuntu Community Hub – 21 Feb 23</a>
  </header>

  <article class="onebox-body">
    <img src="https://ubuntucommunity.s3.dualstack.us-east-2.amazonaws.com/original/2X/a/ab97232ecc5e625556173d73a30bd95743560f49.png" class="thumbnail" width="" height="">

<div class="title-wrapper">
  <h3><a href="https://discourse.ubuntu.com/t/ubuntu-flavor-packaging-defaults/34061?u=d0od" target="_blank" rel="noopener nofollow ugc">Ubuntu Flavor Packaging Defaults</a></h3>
</div>

  <p>Ubuntu flavors offer a unique way to experience Ubuntu, and are part of what makes Ubuntu not just an operating system, but an ecosystem of Linux variations that promote choice and diversity. Flavors build around a common core experience, where it...</p>

  <p>
    <span class="label1">Reading time: 9 mins 🕑</span>
      <span class="label2">Likes: 151 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<ol start="2">
<li>Also found an interesting FOSDEM 2023 talk about Flatpaks, Snaps and AppImages from an OpenSUSE developer:</li>
</ol>
<div class="youtube-onebox lazy-video-container" data-video-id="4WuYGcs0t6I" data-video-title="FOSDEM 2023 - I was wrong about Flatpak, AppImage, and Snap (Containerised Apps Presentation)" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=4WuYGcs0t6I" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/4WuYGcs0t6I/hqdefault.jpg" title="FOSDEM 2023 - I was wrong about Flatpak, AppImage, and Snap (Containerised Apps Presentation)" width="" height="">
  </a>
</div>


---

## Post #34 by @pieper (2023-02-23 14:37 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="33" data-topic="16532">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>Also found an interesting FOSDEM 2023 talk about Flatpaks, Snaps and AppImages from an OpenSUSE developer</p>
</blockquote>
</aside>
<p>What’s the TL;DW for this?</p>

---

## Post #35 by @RafaelPalomar (2023-02-23 19:58 UTC)

<p>From worse to better:</p>
<ol>
<li>AppImages: “fail in everything they set out to do” → Don’t use them.</li>
</ol>
<ul>
<li>Linux apps running everywhere → They don’t</li>
<li>Easy to install apps as in Windows or Mac → They are not.</li>
<li>Provide applications without the need to ‘get into a distribution’ or ‘build for a different distributions’ → Practically, you need to learn every distro and build one.</li>
</ul>
<ol start="2">
<li>Snaps → Practically confined to Canonical ecosystems.</li>
</ol>
<ul>
<li>
<p>Still very limited to Ubuntu ecosystem (won’t deliver confinement in most Linux distributions).</p>
</li>
<li>
<p>Very dependent of Canonical. There is a pricing model for serious delivery of apps and there is no open-source delivery option (open format, but not open delivery).</p>
</li>
</ul>
<ol start="3">
<li>Flatpak → The only option ready for primetime</li>
</ol>
<ul>
<li>
<p>Reasonable isolation model. The client is easy to integrate in any Linux distribution</p>
</li>
<li>
<p>Translates licensing and dependencies freedom and responsibility to the packagers</p>
</li>
</ul>

---

## Post #36 by @abitrolly (2025-09-04 14:48 UTC)

<p>What is required to resurrect the idea of Flatpak builds? Being able to discover it and install using package managers can be handy.</p>
<p>As I understand it, there a few problems.</p>
<ol>
<li>3D Slicer wants optimized binary, that’s why all libs are statically compiled with different options than come from Linux distributions</li>
<li>Linux distros prefer offline builds, and 3D Slicer fetches dependencies dynamically during build.</li>
<li>Not clear how to compile, discover and install extension, which should be built with the same options.</li>
</ol>

---

## Post #37 by @RafaelPalomar (2025-09-05 07:40 UTC)

<p><a class="mention" href="/u/abitrolly">@abitrolly</a>, I have participated deeply on the efforts to bring 3D Slicer to its distribution based on flatpaks, and even managed to produce a working 3D Slicer flatpak. After that process, I came up with the conclusion that these efforts won’t be sustainable in the current context, but maybe is worth re-visiting the topic in the future.</p>
<p><strong>TLDR: In my view, a sustainable flatpak offer would require 3D Slicer community to assume the equivalent effort of maintaining 3D Slicer for an additional operating system (Windows+Linux+MacOS+<em>Linux-Flatpak</em>).</strong></p>
<p><strong>Long answer:</strong></p>
<ul>
<li>3D Slicer is not just a desktop application but a complex software stack. It deploys components ranging from application (high level) to fundamental libraries (low level). The motivation to bring all these components along is to ensure a consistent ecosystem across platforms (Windows, GNU/Linux and MacOS). Flatpak builds are based on its own community-driven SDKs, which provide already a build ecosystem and base libraries. Adapting the development logic of 3D Slicer to one of these SDKs (1) won’t guarantee 3D Slicer runs on GNU/Linux without flatpak (which arguably many users would still want); (2) may (will) create divergences with other OS; and (3) may (will) impose a pace of changes to keep up the compatibility with the SDK.</li>
<li>3D Slicer has over 100 extensions, which will also need to be built on the premise of a flatpak SDK. In my experience, many extensions distributed through the Extensions Manager, were not compatible with flatpak 3D Slicer (ABI incompatibility). Migration of all of these to a flatpak SDK may require the developers of some extensions to assume an adaptation (superbuild extensions will be particularly painful).</li>
<li>Flatpak does not support file downloading during the build process and 3D Slicer largely builds as Superbuild. There are workarounds for this and the 3D Slicer CMake infrastructure has some support for inputting offline dependencies. My approach to flatpak was generating a script that pulls Slicer, configures and parses dependencies to automatically generate the flatpak manifest. This approach was very fragile. A sustainable approach would require the CMake infrastructure of 3D Slicer  (and not only, as other dependencies are also a Superbuilds e.g., CTK) to generate the flatpak manifest (e.g., <code>make flatpak-manifest</code>). This is not a small undertaking.</li>
<li>Even when a Slicer flatpak could be built, there are some additional changes required for Slicer to run in a flatpak environment. The flatpak underlying system is immutable at runtime. Currently Slicer relies on write access to directories inside its own Slicer root directory (both for new pip-installed python packages and for extensions). These can tecnichally move to user directories, but there is some work to do and considerations to what happens when a new Slicer version comes up, etc.</li>
</ul>

---

## Post #38 by @muratmaga (2025-09-06 15:48 UTC)

<p>Thanks for the detailed review <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> I agree this sounds like creating a fourth package, and will likely to create a quite a bit of extra burden on the maintainers. We are already quite stretched maintaining consistent functionality across three major OSes.</p>
<p>I am predominantly a linux user myself, and while I see the appeal of being able to install Slicer from a package manager, I think the download numbers are not going to justify to invest the time into this. I also don’t think the Linux usage will go off the roof after introducing flatpak version.</p>
<p>Having said that, there might be minor (hopefully) tweaks to improve the user experience in Linux:</p>
<ol>
<li>Perhaps we can embed a Slicer.desktop file to make Slicer part of the application list</li>
<li>If we can detect and return the list of missing base libraries necessary to run Slicer on that specific Linux environment after the first run. (As opposed to user going to the downloads page and try to troubleshoot that).</li>
</ol>
<p>Do you think these would be possible or worthwhile, without adding too many layers of complexity?</p>

---

## Post #39 by @pieper (2025-09-06 18:01 UTC)

<p>One thing I’d like to see, for all platforms, would be a lightweight Slicer installation manager.  This would be a small program, ideally with a CLI and GUI interface that would do the download and install steps for you and check for new versions of Slicer and extensions (possibly as a background service).  Maybe also clean up old versions and other tasks that would be hard to do in the application itself.</p>
<p>It could make sense to implement the functionality in <a href="https://github.com/lassoan/slicerio">slicerio</a> so it’s easy to get from pip, and then package up an application in flatpack, and the various OS app stores.</p>

---

## Post #40 by @ruffsl (2025-09-18 22:56 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="37" data-topic="16532">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>There are workarounds for this and the 3D Slicer CMake infrastructure has some support for inputting offline dependencies. My approach to flatpak was generating a script that pulls Slicer, configures and parses dependencies to automatically generate the flatpak manifest.</p>
</blockquote>
</aside>
<p>Is that script/cmake public? I’m particularly interested in building in a offline sandbox, as this would greatly aid efforts to build and run 3D Slicer using more rigorously controlled SBOM using Nix. E.g:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/NixOS/nixpkgs/pull/355116">
  <header class="source">

      <a href="https://github.com/NixOS/nixpkgs/pull/355116" target="_blank" rel="noopener nofollow ugc">github.com/NixOS/nixpkgs</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/NixOS/nixpkgs/pull/355116" target="_blank" rel="noopener nofollow ugc">slicer3d: init at 5.6.2</a>
      </h4>

    <div class="branches">
      <code>master</code> ← <code>purepani:push-tmsvzonwktrw</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-11-11" data-time="02:45:22" data-timezone="UTC">02:45AM - 11 Nov 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/purepani" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/7587353?v=4" class="onebox-avatar-inline" width="20" height="20">
            purepani
          </a>
        </div>

        <div class="lines" title="2 commits changed 2 files with 139 additions and 0 deletions">
          <a href="https://github.com/NixOS/nixpkgs/pull/355116/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+139</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Adds slicer 3d package. This is a qt5 package, so this isn't placed in by-name. <span class="show-more-container"><a href="https://github.com/NixOS/nixpkgs/pull/355116" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">Also, this isn't a source build due to the the source build seemingly requiring git clones that aren't able to be disabled with a cmake variable as far as I can tell.

I've tested and used the main executable, but not any of the other ones since there are many of them. 

There is a darwin version but I don't have use macos so I didn't add support for that here.

@bcdarwin this might be of interest to you to review if you'd like.
## Things done



- Built on platform(s)
  - [x] x86_64-linux
  - [ ] aarch64-linux
  - [ ] x86_64-darwin
  - [ ] aarch64-darwin
- For non-Linux: Is sandboxing enabled in `nix.conf`? (See [Nix manual](https://nixos.org/manual/nix/stable/command-ref/conf-file.html))
  - [ ] `sandbox = relaxed`
  - [ ] `sandbox = true`
- [x] Tested, as applicable:
  - [NixOS test(s)](https://nixos.org/manual/nixos/unstable/index.html#sec-nixos-tests) (look inside [nixos/tests](https://github.com/NixOS/nixpkgs/blob/master/nixos/tests))
  - and/or [package tests](https://github.com/NixOS/nixpkgs/blob/master/pkgs/README.md#package-tests)
  - or, for functions and "core" functionality, tests in [lib/tests](https://github.com/NixOS/nixpkgs/blob/master/lib/tests) or [pkgs/test](https://github.com/NixOS/nixpkgs/blob/master/pkgs/test)
  - made sure NixOS tests are [linked](https://github.com/NixOS/nixpkgs/blob/master/pkgs/README.md#linking-nixos-module-tests-to-a-package) to the relevant packages
- [ ] Tested compilation of all packages that depend on this change using `nix-shell -p nixpkgs-review --run "nixpkgs-review rev HEAD"`. Note: all changes have to be committed, also see [nixpkgs-review usage](https://github.com/Mic92/nixpkgs-review#usage)
- [ ] Tested basic functionality of all binary files (usually in `./result/bin/`)
- [24.11 Release Notes](https://github.com/NixOS/nixpkgs/blob/master/nixos/doc/manual/release-notes/rl-2411.section.md) (or backporting [23.11](https://github.com/NixOS/nixpkgs/blob/master/nixos/doc/manual/release-notes/rl-2311.section.md) and [24.05](https://github.com/NixOS/nixpkgs/blob/master/nixos/doc/manual/release-notes/rl-2405.section.md) Release notes)
  - [ ] (Package updates) Added a release notes entry if the change is major or breaking
  - [ ] (Module updates) Added a release notes entry if the change is significant
  - [ ] (Module addition) Added a release notes entry if adding a new NixOS module
- [ ] Fits [CONTRIBUTING.md](https://github.com/NixOS/nixpkgs/blob/master/CONTRIBUTING.md).



---

Add a :+1: [reaction] to [pull requests you find important].

[reaction]: https://github.blog/2016-03-10-add-reactions-to-pull-requests-issues-and-comments/
[pull requests you find important]: https://github.com/NixOS/nixpkgs/pulls?q=is%3Aopen+sort%3Areactions-%2B1-desc</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<hr>
<aside class="quote no-group" data-username="RafaelPalomar" data-post="37" data-topic="16532">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>These can tecnichally move to user directories, but there is some work to do and considerations to what happens when a new Slicer version comes up, etc.</p>
</blockquote>
</aside>
<p>Extensions are locked to a matching release version due to ABI compatibility, no? Wouldn’t that simply imply user appdata folders be similarly version namespaced, mimicking portable installs?</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/NixOS/nixpkgs/pull/355116#issuecomment-2614614589">
  <header class="source">

      <a href="https://github.com/NixOS/nixpkgs/pull/355116#issuecomment-2614614589" target="_blank" rel="noopener nofollow ugc">github.com/NixOS/nixpkgs</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">

    <div class="github-icon-container" title="Comment">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 2.75a.25.25 0 01.25-.25h8.5a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-3.5a.75.75 0 00-.53.22L3.5 11.44V9.25a.75.75 0 00-.75-.75h-1a.25.25 0 01-.25-.25v-5.5zM1.75 1A1.75 1.75 0 000 2.75v5.5C0 9.216.784 10 1.75 10H2v1.543a1.457 1.457 0 002.487 1.03L7.061 10h3.189A1.75 1.75 0 0012 8.25v-5.5A1.75 1.75 0 0010.25 1h-8.5zM14.5 4.75a.25.25 0 00-.25-.25h-.5a.75.75 0 110-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0114.25 12H14v1.543a1.457 1.457 0 01-2.487 1.03L9.22 12.28a.75.75 0 111.06-1.06l2.22 2.22v-2.19a.75.75 0 01.75-.75h1a.25.25 0 00.25-.25v-5.5z"></path></svg>
    </div>



  <div class="github-info-container">

      <h4>
        Comment by
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/15837524?u=77e23f0a30df57a25f193983b30b27790f224a1c&amp;v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a> - <a href="https://github.com/NixOS/nixpkgs/pull/355116#issuecomment-2614614589" target="_blank" rel="noopener nofollow ugc">slicer3d: init at 5.6.2</a>
      </h4>



    <div class="branches">
      <code>master</code> ← <code>purepani:push-tmsvzonwktrw</code>
    </div>

  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">&gt; a different solution should be found(maybe we can configure the extension loca<span class="show-more-container"><a href="https://github.com/NixOS/nixpkgs/pull/355116" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">tion

Per https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#extensions-settings, you can try setting the "Extensions installation path" setting.
![image](https://github.com/user-attachments/assets/d7b4ca55-9c34-4a73-aefa-ae2a78aeb42f)


&gt; or figure out how to fix this upstream, since this is arguably a bug)

A reason why Slicer stores extensions in the application directory is to make Slicer fully portable by default. See https://github.com/Slicer/Slicer/commit/008f8b9571452334e1d7a55cd5a13ec074905963. There is technically a built option `Slicer_STORE_SETTINGS_IN_APPLICATION_HOME_DIR` that can be adjusted. Setting it off would allow for situations on Windows to install to a system location such as "C:/Program Files", but install extensions into a user writable space in %APPDATA%.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<hr>
<aside class="quote no-group" data-username="RafaelPalomar" data-post="37" data-topic="16532">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>Adapting the development logic of 3D Slicer to one of these SDKs (1) won’t guarantee 3D Slicer runs on GNU/Linux without flatpak (which arguably many users would still want); (2) may (will) create divergences with other OS; and (3) may (will) impose a pace of changes to keep up the compatibility with the SDK.</p>
</blockquote>
</aside>
<p>Not sure I’m the best to add a pitch for Nix, but it does address quite a few of those points:</p>
<ol>
<li>If Nix can source build the package, there is no extra effort to maintain broader linux support
<ol>
<li>Nix is more strict at dependency management, but re-uses the same build systems</li>
</ol>
</li>
<li>Nix natively supports both MacOS and any Linux distro (not just NixOS) with binary caching<br>
2. Developing for a nix package re-uses much the same setup as installing a nix package</li>
<li>Nix has been around for two decades, with the language syntax being quite stable<br>
3. At the same time, nixpkgs is also quite fresh, enabling use of more up-to-date libraries</li>
</ol>
<div class="youtube-onebox lazy-video-container" data-video-id="5D3nUU1OVx8" data-video-title="Nix explained from the ground up" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=5D3nUU1OVx8" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/5D3nUU1OVx8/maxresdefault.jpg" title="Nix explained from the ground up" width="690" height="388">
  </a>
</div>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://zero-to-nix.com/start/">
  <header class="source">
      <img src="https://zero-to-nix.com/favicon.png" class="site-icon" alt="" width="576" height="500">

      <a href="https://zero-to-nix.com/start/" target="_blank" rel="noopener nofollow ugc">zero-to-nix.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:576/500;"><img src="https://zero-to-nix.com/favicon.png" class="thumbnail" alt="" width="576" height="500"></div>

<h3><a href="https://zero-to-nix.com/start/" target="_blank" rel="noopener nofollow ugc">Start</a></h3>

  <p>Get a taste of Nix's power and learn key concepts along the way</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #41 by @RafaelPalomar (2025-09-19 09:27 UTC)

<aside class="quote no-group" data-username="ruffsl" data-post="40" data-topic="16532">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ruffsl/48/80858_2.png" class="avatar"> ruffsl:</div>
<blockquote>
<p>Is that script/cmake public? I’m particularly interested in building in a offline sandbox, as this would greatly aid efforts to build and run 3D Slicer using more rigorously controlled SBOM using</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/ruffsl">@ruffsl</a> you can find the generator and the flatpak repo here:</p>
<ul>
<li><a href="https://github.com/RafaelPalomar/Slicer-Flatpak" class="inline-onebox" rel="noopener nofollow ugc">GitHub - RafaelPalomar/Slicer-Flatpak: Flatpak for 3D Slicer</a></li>
<li><a href="https://github.com/RafaelPalomar/org.slicer.Slicer-flatpak-repository" class="inline-onebox" rel="noopener nofollow ugc">GitHub - RafaelPalomar/org.slicer.Slicer-flatpak-repository: This is the repository containing the Flatpak-packaged version of Slicer</a></li>
</ul>
<p>I would be surprised if these work nowadays, but can be used for learning some useful patterns.</p>
<p>If you are thinking of NixOS, you may want to have a look at a GNU Guix environment definition that I played with not long ago ( <a href="https://github.com/RafaelPalomar/Slicer/blob/guix-5.8/.guix/modules/slicer.scm" class="inline-onebox" rel="noopener nofollow ugc">Slicer/.guix/modules/slicer.scm at guix-5.8 · RafaelPalomar/Slicer · GitHub</a> ). Be aware that the branch contains not only the Guix environment, but also Slicer changes needed to accommodate the offline build (see the latest commits I made in the history).</p>
<p>Another initiative you may want to have a look is the <a href="https://github.com/systoleos" rel="noopener nofollow ugc">SystoleOS</a>. The vision of this project is to package 3D Slicer in modules, together with an ecosystem of packages (PlusToolkit, etc.) to help developers building medical devices. We had an initial experience with GNU Gentoo, which can be found in the <a href="https://github.com/SystoleOS/gentoo-overlay" rel="noopener nofollow ugc">gentoo-overlay repository</a>, but conciliating different software stacks with common dependencies (in different versions) made it difficult to maintain. These days we are working on the <a href="https://github.com/SystoleOS/guix-systole" rel="noopener nofollow ugc">guix-systole channel</a>, which removes some of the problems we had with Gentoo. This is a not (yet) funded project and has limited functionality as of  today, but it is moving forward.</p>
<aside class="quote no-group" data-username="ruffsl" data-post="40" data-topic="16532">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ruffsl/48/80858_2.png" class="avatar"> ruffsl:</div>
<blockquote>
<p>Extensions are locked to a matching release version due to ABI compatibility, no? Wouldn’t that simply imply user appdata folders be similarly version namespaced, mimicking portable installs?</p>
</blockquote>
</aside>
<p>Yes, 3D Slicer is actively being developed, sometimes changes in the core or the building infrastructure breaks API/ABI. A matching revision between 3D Slicer and the extensions distributed guarantees compatibility. However, a matching revision does not guarantee that 3D Slicer built in one environment (e.g., Flatpak SDKs) will be compatible with Extensions binaries built by the 3D Slicer build servers.</p>
<aside class="quote no-group" data-username="ruffsl" data-post="40" data-topic="16532">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ruffsl/48/80858_2.png" class="avatar"> ruffsl:</div>
<blockquote>
<p>a pitch for Nix</p>
</blockquote>
</aside>
<p>As much as I love the idea of a packaged Slicer on Nix, Guix or Flatpak, at the end of the day, it does not solve any problem. 3D Slicer is already largely compatible with many GNU/Linux distributions and it is already compatible with MacOS without the need for its users to install the Nix package manager. Rather than Slicer developer chasing dependencies on Nix or Flatpak SDKs, communities in those spaces should maintain the package(s).</p>
<p>From the 3D Slicer perspective, I think there are legit cases for (1) enabling python packages to be installed in user space (containers, SystoleOS, Nix/Guix, etc. could benefit from it), (2) better decoupling of the extension manager (while there are options to disable a build with the extension manager, some minor changes are needed to honor this option). These changes, in my view, are independent, concise and can help communities to get close to their own packaged Slicer.</p>

---
