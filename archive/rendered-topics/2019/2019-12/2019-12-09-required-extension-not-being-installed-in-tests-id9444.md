# Required extension not being installed in tests

**Topic ID**: 9444
**Date**: 2019-12-09
**URL**: https://discourse.slicer.org/t/required-extension-not-being-installed-in-tests/9444

---

## Post #1 by @Alex_Vergara (2019-12-09 11:10 UTC)

<p>While building my extension I have set up a required extension (SlicerElastix) which runs fine, but when I want to test it in Docker it fails with this message:</p>
<pre><code class="lang-auto">144 CMake Warning at /usr/src/Slicer/Extensions/CMake/SlicerBlockAdditionalLauncherSettings.cmake:48 (message):
145   Dependent extension SlicerElastix cannot be found by CMake find_package(),
146   therefore paths variables cannot be imported from this extension.  The
147   problem can be resolved by generating SlicerElastixConfig.cmake by adding
148   include(${Slicer_EXTENSION_GENERATE_CONFIG}) to the top-level
149   CMakeLists.txt of the dependent extension.
</code></pre>
<p>I have a look at <a href="https://github.com/lassoan/SlicerElastix/blob/master/CMakeLists.txt" rel="nofollow noopener">the offending file</a> and indeed, it contains <a href="https://github.com/lassoan/SlicerElastix/blob/master/CMakeLists.txt#L50" rel="nofollow noopener">that line</a>. So, I don’t know what it is happening here.</p>

---

## Post #2 by @jamesobutler (2019-12-09 15:40 UTC)

<p>It appears that another extension, SequenceRegistration, is also having the same issue. That extension depends on Sequences and SlicerElastix. Here’s the nightly Windows build for SequenceRegistration that has the same CMake warning: <a href="http://slicer.cdash.org/viewConfigure.php?buildid=1770198" rel="nofollow noopener">http://slicer.cdash.org/viewConfigure.php?buildid=1770198</a>.</p>
<p>A previous SlicerElastix error due to being a dependency was brought up in <a href="https://discourse.slicer.org/t/failing-tests-importerror-no-module-named-elastix/7202" class="inline-onebox">Failing Tests - ImportError: No module named Elastix</a>, but that solution by <a class="mention" href="/u/jcfr">@jcfr</a> is evidently not working anymore.</p>

---

## Post #3 by @lassoan (2019-12-09 17:57 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="1" data-topic="9444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Dependent extension SlicerElastix cannot be found by CMake find_package(), 146 therefore paths variables cannot be imported from this extension.</p>
</blockquote>
</aside>
<p>When you build an extension, you need to pass location of all other extensions that it depends on, as CMake variables. For example, if you want to build Sequence Registration, then you need to set SlicerElastix_DIR=…</p>
<p>For 1-2 extensions with simple dependencies you may do this manually, but it may be simpler (especially when you build several extensions) to use Slicer’s extensions index build script: copy s4ext files that you want to build into a folder and specify that as Slicer_EXTENSION_DESCRIPTION_DIR. See the complete command-line <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_ExtensionsIndex#Build_slicer_extensions_associated_with_Slicer_trunk">here</a>. This script determines dependencies between extensions, builds them in the correct order and passes all required paths to dependent extensions.</p>

---

## Post #4 by @jamesobutler (2019-12-10 01:53 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Do you have insight on how to fix the factory build of SequenceRegistration extension which specifies SlicerElastix as a dependent extension. Looking to solve this <a href="http://slicer.cdash.org/testDetails.php?test=9803789&amp;build=1770127" rel="nofollow noopener">failing test</a> specifically.</p>

---

## Post #5 by @lassoan (2019-12-10 06:44 UTC)

<p>Maybe we just need to add the missing <code>["Sequences", "Elastix"]</code> dependency declaration here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/moselhy/SlicerSequenceRegistration/blob/master/SequenceRegistration/SequenceRegistration.py#L20" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/moselhy/SlicerSequenceRegistration/blob/master/SequenceRegistration/SequenceRegistration.py#L20" target="_blank">moselhy/SlicerSequenceRegistration/blob/master/SequenceRegistration/SequenceRegistration.py#L20</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="10" style="counter-reset: li-counter 9 ;">
<li>
</li>
<li>class SequenceRegistration(ScriptedLoadableModule):
</li>
<li>  """Uses ScriptedLoadableModule base class, available at:
</li>
<li>  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
</li>
<li>  """
</li>
<li>
</li>
<li>  def __init__(self, parent):
</li>
<li>    ScriptedLoadableModule.__init__(self, parent)
</li>
<li>    self.parent.title = "Sequence Registration"
</li>
<li>    self.parent.categories = ["Sequences"]
</li>
<li class="selected">    self.parent.dependencies = []
</li>
<li>    self.parent.contributors = ["Mohamed Moselhy (Western University), Andras Lasso (PerkLab, Queen's University), and Feng Su (Western University)"]
</li>
<li>    self.parent.helpText = """For up-to-date user guides, go to &lt;a href="https://github.com/moselhy/SlicerSequenceRegistration"&gt;the official GitHub page&lt;/a&gt;
</li>
<li>"""
</li>
<li>    self.parent.acknowledgementText = """
</li>
<li>"""
</li>
<li>
</li>
<li>#
</li>
<li># SequenceRegistrationWidget
</li>
<li>#
</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @Alex_Vergara (2019-12-11 14:07 UTC)

<p>Adding Elastix in parent dependencies is the detonant for the error</p>
<pre><code class="lang-auto">CMake Warning at /usr/src/Slicer/Extensions/CMake/SlicerBlockAdditionalLauncherSettings.cmake:48 (message):
  Dependent extension SlicerElastix cannot be found by CMake find_package(),
  therefore paths variables cannot be imported from this extension.  The
  problem can be resolved by generating SlicerElastixConfig.cmake by adding
  include(${Slicer_EXTENSION_GENERATE_CONFIG}) to the top-level
  CMakeLists.txt of the dependent extension.
Call Stack (most recent call first):
  /usr/src/Slicer-build/Slicer-build/UseSlicer.cmake:279 (include)
  CMakeLists.txt:18 (include)


-- Setting EXTENSION_SOURCE_DIR ................: /builds/project-0
-- Setting EXTENSION_SUPERBUILD_BINARY_DIR .....: /builds/dosimetry4d-build
-- Setting EXTENSION_BUILD_SUBDIRECTORY ........: .
-- Setting MIDAS_PACKAGE_URL ...................: http://slicer.kitware.com/midas3
-- Setting MIDAS_PACKAGE_EMAIL .................: OBFUSCATED
-- Setting MIDAS_PACKAGE_API_KEY ...............: OBFUSCATED
-- Setting EXTENSION_SVNUSERNAME ...............: NOT DEFINED
-- Setting EXTENSION_SVNPASSWORD ...............: NOT DEFINED
-- Setting EXTENSION_DEPENDS ...................: SlicerElastix
-- Setting EXTENSION_BUILD_SUBDIRECTORY ........: .
-- Setting EXTENSION_HOMEPAGE ..................: http://gitlab.com/opendose/opendose4d
-- Setting EXTENSION_CONTRIBUTORS ..............: Alex Vergara Gil (INSERM) and Janick Rueegger (KSA)
-- Setting EXTENSION_CATEGORY ..................: Dosimetry
-- Setting EXTENSION_ICONURL ...................: https://opendose.org/themes/default/images/opendose_favicon.png
-- Setting EXTENSION_DESCRIPTION ...............: This extension contains the entire dosimetry workflow for a multipoint st [...]
-- Setting EXTENSION_SCREENSHOTURLS ............: http://www.example.com/Slicer/Extensions/Dosimetry/Screenshots/1.png
-- Setting EXTENSION_ENABLED ...................: 1
-- Setting EXTENSION_STATUS ....................: NOT DEFINED
-- Setting default for EXTENSION_STATUS ........: 
-- Found Git: /usr/local/bin/git  
-- Found Subversion: /usr/bin/svn (found version "1.7.14") 
-- Configuring Scripted module: Dosimetry4D
CMake Error at /usr/src/Slicer/CMake/SlicerMacroBuildScriptedModule.cmake:78 (message):
  slicerMacroBuildScriptedModule(RESOURCES) given nonexistent file or
  directory 'Resources/JSON/DVK-F-18.json'
Call Stack (most recent call first):
  Dosimetry4D/CMakeLists.txt:53 (slicerMacroBuildScriptedModule)


-- Configuring incomplete, errors occurred!
See also "/builds/dosimetry4d-build/CMakeFiles/CMakeOutput.log".
See also "/builds/dosimetry4d-build/CMakeFiles/CMakeError.log".
e[0KAuthenticating with credentials from /Users/alexvergaragil/.docker/config.json
e[0;me[31;1mERROR: Job failed: exit code 1
e[0;m
</code></pre>

---

## Post #7 by @lassoan (2019-12-11 14:10 UTC)

<p>Make sure to add SlicerElastix_DIR when configuring you project in CMake (or put all s4ext files in a folder and let Slicer extension build script to figure out dependencies, build order, and set all necessary CMake variables).</p>

---

## Post #8 by @Alex_Vergara (2019-12-11 14:12 UTC)

<p>This is my CI file</p>
<pre><code class="lang-auto">image: unnmdnwb3/slicer3d-nightly:0.4.0

build-and-test:
  variables:
    DISPLAY: ":99.0"
  script:
    - mkdir $CI_BUILDS_DIR/dosimetry4d-build &amp;&amp; cd $CI_BUILDS_DIR/dosimetry4d-build 
    - mkdir /usr/src/SlicerDICOMDatabase
    - sed  '/\[General\]/a DatabaseDirectory=/usr/src/SlicerDICOMDatabase' /usr/src/Slicer-build/Slicer-build/SlicerLauncherSettings.ini
    - git clone git://github.com/Slicer/ExtensionsIndex.git $CI_BUILDS_DIR/SlicerExtensionsIndex-master
    - cmake -DSlicer_DIR:PATH=/usr/src/Slicer-build/Slicer-build -DBUILDNAME:STRING=dosimetry4d $CI_PROJECT_DIR -DSlicer_EXTENSION_DESCRIPTION_DIR:PATH=$CI_BUILDS_DIR/SlicerExtensionsIndex-master -DCMAKE_BUILD_TYPE:STRING=Testing -DENABLE_TESTS:BOOL=ON
    - make
    - /usr/src/Slicer-build/python-install/bin/PythonSlicer -m pip install --upgrade pip
    - /usr/src/Slicer-build/python-install/bin/PythonSlicer -m pip install 2to3 lmfit
    - 2to3 -w /usr/src/Slicer-build/python-install/lib/python3.6/site-packages/uncertainties
    - Xvfb :99 -screen 0 1024x768x24 &amp;&gt; xvfb.log &amp;
    - cd $CI_BUILDS_DIR/dosimetry4d-build
    - ctest -V
</code></pre>
<p>Do you mean adding <code>SlicerElastix_DIR</code> even when it is not there in the first place?<br>
How to copy the <code>s4ext</code> file, shall I copy from web or do I need to create a local copy? There is <a href="https://github.com/Slicer/Slicer/tree/master/Extensions" rel="nofollow noopener">already a folder</a> of <code>s4ext</code> inside Slicer</p>

---

## Post #9 by @lassoan (2019-12-11 16:21 UTC)

<p>Do you want to build extensions manually or make Slicer’s script build a list of extensions?</p>

---

## Post #10 by @Alex_Vergara (2019-12-12 03:59 UTC)

<p>Neither, I want Slicer to install required extensions automatically.</p>

---

## Post #11 by @lassoan (2019-12-12 05:40 UTC)

<p>Do you mean you bundle extensions with a custom Slicer build?</p>

---

## Post #12 by @Alex_Vergara (2019-12-12 05:42 UTC)

<p>I have made an extension that depends on another (Elastix) and I want that Slicer installs the required extension automatically. My extension shall be able to install in vanilla slicer-nightly.</p>

---

## Post #13 by @lassoan (2019-12-12 05:55 UTC)

<p>You need to specify the list of extensions yours depend on in the top-level CMakeLists.txt file (EXTENSION_DEPENDS variable). After this, you also need to regenerate the s4ext file and update it in ExtensionsIndex repository.</p>

---

## Post #14 by @Alex_Vergara (2019-12-13 11:14 UTC)

<p>I currently have (EXTENSION_DEPENDS variable)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecbe7d9f4d8129cdd32e5e7ba9412642f9e5f1e9.png" data-download-href="/uploads/short-url/xMkO40tXz75XT6rNeMJW57Bn6R3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecbe7d9f4d8129cdd32e5e7ba9412642f9e5f1e9_2_685x500.png" alt="image" data-base62-sha1="xMkO40tXz75XT6rNeMJW57Bn6R3" width="685" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecbe7d9f4d8129cdd32e5e7ba9412642f9e5f1e9_2_685x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecbe7d9f4d8129cdd32e5e7ba9412642f9e5f1e9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecbe7d9f4d8129cdd32e5e7ba9412642f9e5f1e9.png 2x" data-dominant-color="262625"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">819×597 69.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>May you please have a look to <a href="https://gitlab.com/opendose/opendose4d" rel="noopener nofollow ugc">my extension</a> and tell me what I am missing?</p>
<p>I am still having <a href="https://gitlab.com/opendose/opendose4d/-/jobs/373395246" rel="noopener nofollow ugc">these errors</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52ed23baafc9413a02008bb6129becb0406a0a40.png" data-download-href="/uploads/short-url/bPBdKqPBumvruGCNGO7ojC6Wz4I.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52ed23baafc9413a02008bb6129becb0406a0a40_2_690x359.png" alt="image" data-base62-sha1="bPBdKqPBumvruGCNGO7ojC6Wz4I" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52ed23baafc9413a02008bb6129becb0406a0a40_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52ed23baafc9413a02008bb6129becb0406a0a40.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52ed23baafc9413a02008bb6129becb0406a0a40.png 2x" data-dominant-color="2B2C2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">908×473 81.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @Alex_Vergara (2019-12-19 14:27 UTC)

<p>I still not able to force my extension to launch Elastix installation in tests</p>

---

## Post #16 by @Alex_Vergara (2020-03-02 14:38 UTC)

<p>I have found a way to force install SlicerElastix from within python, however this requires Slicer Restart, this is not optimal, I wanted to do it from within the gitlab-ci itself but I get several errors:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "installElastix.py", line 2, in &lt;module&gt;
    emm = slicer.app.extensionsManagerModel()
AttributeError: module 'slicer' has no attribute 'app'
vtkDebugLeaks has found no leaks.
</code></pre>
<p>My <code>installElastix.py</code> script contains</p>
<pre><code class="lang-python">import slicer
emm = slicer.app.extensionsManagerModel()
md = emm.retrieveExtensionMetadataByName('SlicerElastix')
emm.downloadAndInstallExtension(md['extension_id'])
</code></pre>
<p>In the environment there are</p>
<pre><code class="lang-auto">[Application]
path=&lt;APPLAUNCHER_DIR&gt;/bin/./SlicerApp-real
arguments=
name=Slicer
revision=e68a1a2
organizationDomain=www.na-mic.org
organizationName=NA-MIC

[ExtraApplicationToLaunch]

designer/shortArgument=
designer/help=Start Qt designer using Slicer plugins
designer/path=/opt/qt/5.11.2/gcc_64/bin/designer
designer/arguments=


[Environment]
additionalPathVariables=QT_PLUGIN_PATH,PYTHONPATH

[LibraryPaths]
1\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/bin/.
2\path=../lib/Slicer-4.11/qt-loadable-modules
3\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/lib/Slicer-4.11/cli-modules/.
4\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/lib/Slicer-4.11/qt-loadable-modules/.
5\path=/usr/src/Slicer-build/OpenSSL
6\path=/usr/src/Slicer-build/python-install/lib
7\path=/usr/src/Slicer-build/VTK-build/lib/.
8\path=/usr/src/Slicer-build/teem-build/bin/.
9\path=/usr/src/Slicer-build/DCMTK-build/lib/.
10\path=/usr/src/Slicer-build/ITK-build/lib/.
11\path=/usr/src/Slicer-build/CTK-build/CTK-build/bin/.
12\path=/usr/src/Slicer-build/CTK-build/PythonQt-build/.
13\path=/usr/src/Slicer-build/LibArchive-install/lib
14\path=/usr/src/Slicer-build/JsonCpp-build/src/lib_json/.
15\path=/usr/src/Slicer-build/ParameterSerializer-build/lib/.
16\path=/usr/src/Slicer-build/SlicerExecutionModel-build/ModuleDescriptionParser/bin/.
17\path=/usr/src/Slicer-build/python-install/lib/python3.6/site-packages/numpy/core
18\path=/usr/src/Slicer-build/python-install/lib/python3.6/site-packages/numpy/lib
size=18

[Paths]
1\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/bin/.
2\path=/opt/qt/5.11.2/gcc_64/bin
3\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/lib/Slicer-4.11/cli-modules/.
4\path=/usr/src/Slicer-build/python-install/bin
5\path=/usr/src/Slicer-build/teem-build/bin/.
size=5

[EnvironmentVariables]
SLICER_HOME=/usr/src/Slicer-build/Slicer-build
ITK_AUTOLOAD_PATH=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/lib/Slicer-4.11/ITKFactories/.
PIP_REQUIRE_VIRTUALENV=0
SSL_CERT_FILE=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/share/Slicer-4.11/Slicer.crt
PYTHONHOME=/usr/src/Slicer-build/python-install
PYTHONNOUSERSITE=1



[QT_PLUGIN_PATH]
1\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/bin
2\path=/usr/src/Slicer-build/CTK-build/CTK-build/bin
3\path=/opt/qt/5.11.2/gcc_64/plugins
size=3

[PYTHONPATH]
1\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/bin/.
2\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/bin/Python
3\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/lib/Slicer-4.11/qt-loadable-modules/.
4\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/lib/Slicer-4.11/qt-loadable-modules/Python
5\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/lib/Slicer-4.11/qt-scripted-modules
6\path=/usr/src/Slicer-build/python-install/lib/python3.6
7\path=/usr/src/Slicer-build/python-install/lib/python3.6/lib-dynload
8\path=/usr/src/Slicer-build/python-install/lib/python3.6/site-packages
9\path=/usr/src/Slicer-build/VTK-build/lib/python3.6/site-packages
10\path=/usr/src/Slicer-build/CTK-build/CTK-build/bin/Python
11\path=/usr/src/Slicer-build/CTK-build/CTK-build/bin/.
size=11
</code></pre>

---

## Post #17 by @Alex_Vergara (2020-03-02 16:15 UTC)

<p>I have tried to follow this <a href="https://github.com/Slicer/Slicer/blob/master/.circleci/config.yml" rel="nofollow noopener">circleci.yml</a> in the slicer repository using the <code>slicer-base</code>  docker image and it fails with</p>
<pre><code class="lang-auto">$ ../Slicer-build/BuildSlicer.sh
+ set -o pipefail
+ set -o
allexport       off
braceexpand     on
emacs           off
errexit         on
errtrace        off
functrace       off
hashall         on
histexpand      off
history         off
ignoreeof       off
interactive-comments    on
keyword         off
monitor         off
noclobber       off
noexec          off
noglob          off
nolog           off
notify          off
nounset         off
onecmd          off
physical        off
pipefail        on
posix           off
privileged      off
verbose         off
vi              off
xtrace          on
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
Authenticating with credentials from /Users/alexvergaragil/.docker/config.json
panic: runtime error: invalid memory address or nil pointer dereference
[signal SIGSEGV: segmentation violation code=0x1 addr=0x0 pc=0x19196db]
</code></pre>

---

## Post #18 by @lassoan (2020-03-03 02:48 UTC)

<p>I would recommend to build <a href="https://github.com/Slicer/Slicer/tree/master/Extensions/CMake">SlicerExtensions</a> project, which downloads, builds, and tests a list of extensions (by default, it takes the list from ExtensionsIndex repository, but you can provide your own list instead). This project takes care of dependencies between extensinos: it builds them in the right order, and also passes all needed build directories to extensions that depend on others. This is used every night to build all the extensions.</p>

---

## Post #19 by @Alex_Vergara (2020-03-04 12:38 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="16" data-topic="9444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>extensionsManagerModel()</p>
</blockquote>
</aside>
<p>I am trying to replicate the behaviour of the circleCI docker instance but I was unsuccessful. see:</p>
<pre><code class="lang-auto">alex@CRCTcalcul:~$ docker run -it slicer/slicer-base  /bin/bash
Unable to find image 'slicer/slicer-base:latest' locally
latest: Pulling from slicer/slicer-base
a02a4930cb5d: Already exists
6a788e5d573f: Already exists
a9afa5c4a530: Already exists
6383f75ec3ac: Already exists
ec1353604d1f: Already exists
a6a7f5d80d82: Already exists
87bee5282cdd: Already exists
63309cde1def: Pull complete
Digest: sha256:4a69f356475c2974de6d35722474f674912300ee01ee50e3b8ff418bbc31865d
Status: Downloaded newer image for slicer/slicer-base:latest
[root@72bd75fc099d Slicer-build]# cd /usr/src/Slicer
bash: cd: /usr/src/Slicer: No such file or directory
[root@72bd75fc099d Slicer-build]# ../Slicer-build/BuildSlicer.sh
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
[root@72bd75fc099d Slicer-build]#
</code></pre>
<p>I want to create an image with Slicer extensions built by default.</p>

---

## Post #20 by @Alex_Vergara (2020-03-04 13:58 UTC)

<p>Also, Is there a way to specify explicitly the list of extensions to make?</p>

---

## Post #21 by @lassoan (2020-03-05 02:10 UTC)

<p>Yes, you specify a folder where all the s4ext files are stored. It is not a simple list of extension names, because you also need repository URL and dependency information for each extension. The CMake scripts parse the s4ext files, determine dependencies and build them in the right order.</p>

---
