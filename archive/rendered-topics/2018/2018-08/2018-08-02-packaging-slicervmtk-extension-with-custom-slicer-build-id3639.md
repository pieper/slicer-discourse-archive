# Packaging SlicerVMTK extension with custom Slicer build

**Topic ID**: 3639
**Date**: 2018-08-02
**URL**: https://discourse.slicer.org/t/packaging-slicervmtk-extension-with-custom-slicer-build/3639

---

## Post #1 by @mschumaker (2018-08-02 19:49 UTC)

<p>I have added a Slicer_EXTENSION_SOURCE_DIRS entry to my CMakeCache.txt for a Slicer build (Aug 1 nightly). I have entered the source directory for one extension, the SlicerExtension-VMTK, which depends on the external VMTK package. The build error I’m getting is that it can’t find the External_VMTK.cmake file.</p>
<p>What appears to be happening is the extension’s SuperBuild.cmake file calls a macro, ExternalProject_Include_Dependencies. I’ve searched, and there is a file that contains this macro in Slicer/CMake/ExternalProjectDependency.cmake, but that’s not the macro that gets called. Instead, it looks like it picks up the macro in the BRAINSTools extension, in Slicer-SuperBuild/BRAINSTools/CMake/ExternalProjectDependency.cmake. These files are very different.</p>
<p>The macro starts around line 450 of the file in BRAINSTools, and the error message I get is on line 639. There are three places it looks for the External_VMTK.cmake file:</p>
<ul>
<li>/workingdir/Slicer/SuperBuild/External_VMTK.cmake</li>
<li>(blank)</li>
<li>/External_VMTK.cmake</li>
</ul>
<p>The correct location is /workingdir/Extensions/SlicerExtension-VMTK/SuperBuild.</p>
<p>My questions are: which version of the macro should it be using? Is it calling the wrong one? Would the version of the macro in Slicer/CMake be able to pick up the correct location for the External_VMTK.cmake file? Is there a way to correct this?</p>
<p>Thanks very much. The full text of the error I get is below.</p>
<blockquote>
<p>– Configuring extension directory: SlicerExtension-VMTK<br>
CMake Warning (dev) at /short/Extensions/SlicerExtension-VMTK/CMakeLists.txt:4 (project):<br>
Policy CMP0048 is not set: project() command manages VERSION variables.<br>
Run “cmake --help-policy CMP0048” for policy details.  Use the cmake_policy<br>
command to set the policy and suppress this warning.</p>
</blockquote>
<blockquote>
<p>The following variable(s) would be set to empty:</p>
</blockquote>
<pre><code>PROJECT_VERSION
PROJECT_VERSION_MAJOR
PROJECT_VERSION_MINOR
PROJECT_VERSION_PATCH
</code></pre>
<blockquote>
<p>This warning is for project developers.  Use -Wno-dev to suppress it.</p>
</blockquote>
<blockquote>
<p>– Checking EXTENSION_NAME variable<br>
– Checking EXTENSION_NAME variable - NOTDEFINED<br>
– Checking MODULE_NAME variable<br>
– Checking MODULE_NAME variable - NOTDEFINED<br>
– Checking PROJECT_NAME variable<br>
– Checking PROJECT_NAME variable - SlicerVMTK<br>
– Setting EXTENSION_NAME …: SlicerVMTK<br>
– SuperBuild - First pass<br>
CMake Error at /short/Slicer-SuperBuild/BRAINSTools/CMake/ExternalProjectDependency.cmake:639 (message):<br>
Can’t find External_VMTK.cmake</p>
</blockquote>
<blockquote>
<p>Call Stack (most recent call first):<br>
/short/Extensions/SlicerExtension-VMTK/SuperBuild.cmake:32 (ExternalProject_Include_Dependencies)<br>
/short/Extensions/SlicerExtension-VMTK/CMakeLists.txt:33 (include)</p>
</blockquote>
<blockquote>
<p>– Configuring incomplete, errors occurred!<br>
See also “/short/Slicer-SuperBuild/Slicer-build/CMakeFiles/CMakeOutput.log”.<br>
See also “/short/Slicer-SuperBuild/Slicer-build/CMakeFiles/CMakeError.log”.<br>
make[2]: *** [Slicer-prefix/src/Slicer-stamp/Slicer-configure] Error 1<br>
make[1]: *** [CMakeFiles/Slicer.dir/all] Error 2<br>
make: *** [all] Error 2</p>
</blockquote>

---

## Post #2 by @mschumaker (2018-08-02 20:01 UTC)

<p>The SlicerExtension-VMTK code I’m using is at <a href="https://github.com/mschumak/SlicerExtension-VMTK.git" rel="nofollow noopener">https://github.com/mschumak/SlicerExtension-VMTK.git</a> commit 550c2813a756d8bec0bb5b8286ed68afc93860f2.</p>

---

## Post #3 by @mschumaker (2018-08-07 21:55 UTC)

<p>Perhaps I’ll start with a more basic question. What is the best way to package an extension with a custom build? I’ve tried doing it by setting a Slicer_EXTENSION_SOURCE_DIRS CMake value before building, and have encountered problems, though these may be specific to the SlicerVMTK extension. Should I continue approaching it this way?</p>

---

## Post #4 by @jcfr (2018-08-07 22:07 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="3" data-topic="3639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>Should I continue approaching it this way?</p>
</blockquote>
</aside>
<p>Yes.</p>
<p>Please, report here the errors you encountered.</p>

---

## Post #5 by @mschumaker (2018-08-08 20:54 UTC)

<p>Thank you. I’ve set up a project using cookiecutter (thanks again for help using it). Before building, I added Slicer_EXTENSION_SOURCE_DIRS to the CMakeCache.<br>
Right now, I’m trying to get my own scripted modules to link with the application. I specified a directory with my extension, which was set up using the ExtensionWizard. It has 10 modules. An error occurs when it reads the CMakeLists file for a module. It may not recognize the slicerMacroBuildScriptedModule macro?</p>
<blockquote>
<p>– Configuring extension directory: PADFusion<br>
CMake Warning (dev) at /Users/michaelschumaker/Development/mschumaker/Slicelets/PADFusion/PADFusion/CMakeLists.txt:3 (project):<br>
Policy CMP0048 is not set: project() command manages VERSION variables.<br>
Run “cmake --help-policy CMP0048” for policy details.  Use the cmake_policy<br>
command to set the policy and suppress this warning.</p>
<p>The following variable(s) would be set to empty:</p>
<pre><code>PROJECT_VERSION
PROJECT_VERSION_MAJOR
PROJECT_VERSION_MINOR
PROJECT_VERSION_PATCH
</code></pre>
<p>This warning is for project developers.  Use -Wno-dev to suppress it.</p>
<p>– Checking EXTENSION_NAME variable<br>
– Checking EXTENSION_NAME variable - NOTDEFINED<br>
– Checking MODULE_NAME variable<br>
– Checking MODULE_NAME variable - NOTDEFINED<br>
– Checking PROJECT_NAME variable<br>
– Checking PROJECT_NAME variable - PADFusion<br>
– Setting EXTENSION_NAME …: PADFusion<br>
CMake Error at /Users/michaelschumaker/Development/mschumaker/Slicelets/PADFusion/PADFusion/FusionWorkflow/CMakeLists.txt:14 (slicerMacroBuildScriptedModule):<br>
Unknown CMake command “slicerMacroBuildScriptedModule”.</p>
<p>– Configuring incomplete, errors occurred!<br>
See also “/short/appTemplate/PADPlanner-SuperBuild/Slicer-build/CMakeFiles/CMakeOutput.log”.<br>
See also “/short/appTemplate/PADPlanner-SuperBuild/Slicer-build/CMakeFiles/CMakeError.log”.<br>
make[2]: *** [slicersources-build/Slicer-prefix/src/Slicer-stamp/Slicer-configure] Error 1<br>
make[1]: *** [slicersources-build/CMakeFiles/Slicer.dir/all] Error 2<br>
make: *** [all] Error 2</p>
</blockquote>

---

## Post #6 by @mschumaker (2018-08-08 20:59 UTC)

<p><s>Noticed I was still working within the cookiecutter virtual environment we discussed here <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/issues/5" rel="nofollow noopener">https://github.com/KitwareMedical/SlicerCustomAppTemplate/issues/5</a>. I’m trying it again from my regular shell.</s></p>
<p>Same error.</p>

---

## Post #7 by @jcfr (2018-08-08 21:14 UTC)

<blockquote>
<p>Unknown CMake command “slicerMacroBuildScriptedModule</p>
</blockquote>
<p>This is most likely explained by the fact <code>Slicer_USE_PYTHONQT</code> is disabled by default in the template.</p>
<p>After integrating the following PR a more obvious error message will be reported:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/996">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/996" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/996" target="_blank" rel="noopener">import of xnat xcat files not working properly</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:35:50" data-timezone="UTC">10:35PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:35:50" data-timezone="UTC">10:35PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=996). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @mschumaker (2018-08-08 21:18 UTC)

<p>Thanks. Yes, that will make it easier to figure out why it failed. I’ll turn Slicer_USE_PYTHONQT on.</p>

---

## Post #9 by @jcfr (2018-08-08 21:19 UTC)

<blockquote>
<p>Before building, I added Slicer_EXTENSION_SOURCE_DIRS</p>
</blockquote>
<p>Also, the download of the module or extension source can be automatic using an approach similar to this one:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/c463c1aed20a2ede2bb741533404bd0c09d1530e/%7B%7Bcookiecutter.project_name%7D%7D/CMakeLists.txt#L115-L125">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/c463c1aed20a2ede2bb741533404bd0c09d1530e/%7B%7Bcookiecutter.project_name%7D%7D/CMakeLists.txt#L115-L125" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/c463c1aed20a2ede2bb741533404bd0c09d1530e/%7B%7Bcookiecutter.project_name%7D%7D/CMakeLists.txt#L115-L125" target="_blank" rel="noopener">KitwareMedical/SlicerCustomAppTemplate/blob/c463c1aed20a2ede2bb741533404bd0c09d1530e/{{cookiecutter.project_name}}/CMakeLists.txt#L115-L125</a></h4>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="115" style="counter-reset: li-counter 114 ;">
          <li># SlicerOpenIGTLink</li>
          <li>#set(extension_name "SlicerOpenIGTLink")</li>
          <li>#set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")</li>
          <li>#FetchContent_Populate(${extension_name}</li>
          <li>#  SOURCE_DIR     ${${extension_name}_SOURCE_DIR}</li>
          <li>#  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/openigtlink/SlicerOpenIGTLink.git</li>
          <li>#  GIT_TAG        2b92f7b1ffe02403109b671f28424e8770e902a0</li>
          <li>#  GIT_PROGRESS   1</li>
          <li>#  QUIET</li>
          <li>#  )</li>
          <li>#list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @mschumaker (2018-08-10 16:11 UTC)

<p>I’m making progress with an application started with cookiecutter, and including my scripted modules. One question I have is about additional files for a module. I have some tables in plist files in the Resources directory of a scripted module. How do I make sure these will be copied to the qt-scripted-modules/Resources directory when building?</p>
<p>Another minor thing I noticed is a problem with the version numbers and dates that appear in the compiled application. In the Mac menu bar, the version number and date are for Slicer, while at the top of the application window, the version number is what I defined, but the date is all zeros. I’ve included an image. Is this a bug, or is there something I need to do?<br>
Thanks!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a88ff78c1b7fce2f7ac3e67b66ac12428609df1f.jpeg" data-download-href="/uploads/short-url/o3aF64IPS5tReja2n0ooGoWMxVJ.jpg?dl=1" title="version-date-question" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a88ff78c1b7fce2f7ac3e67b66ac12428609df1f_2_690x225.jpg" alt="version-date-question" data-base62-sha1="o3aF64IPS5tReja2n0ooGoWMxVJ" width="690" height="225" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a88ff78c1b7fce2f7ac3e67b66ac12428609df1f_2_690x225.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a88ff78c1b7fce2f7ac3e67b66ac12428609df1f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a88ff78c1b7fce2f7ac3e67b66ac12428609df1f.jpeg 2x" data-dominant-color="8188A2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">version-date-question</span><span class="informations">803×263 80.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @jcfr (2018-08-10 16:54 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="10" data-topic="3639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>I defined, but the date is all zero</p>
</blockquote>
</aside>
<p>This is because you do not yet have a git repository associated with your custom application source code. In that case, the there is now way to know the date associated with the last commit.</p>
<aside class="quote no-group" data-username="mschumaker" data-post="10" data-topic="3639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>In the Mac menu bar, the version number and date are for Slicer</p>
</blockquote>
</aside>
<p>This is indeed a bug, for now the following lines need to be changed to use <code>Slicer_MAIN_PROJECT_VERSION_FULL</code>.  (Note that ideally it should <code>SLICER_APP_VERSION_FULL</code> but this is not yet possible because repository info are only extracted for Slicer itself and the main application only)</p>
<p>Could you create a Slicer PR to address this ? Thanks</p>
<p><a href="https://github.com/Slicer/Slicer/blob/ad3fcd4ddf367363f9fb258b6dc2fcee06cd2039/CMake/SlicerMacroBuildApplication.cmake#L449-L450" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/ad3fcd4ddf367363f9fb258b6dc2fcee06cd2039/CMake/SlicerMacroBuildApplication.cmake#L449-L450</a></p>

---

## Post #12 by @mschumaker (2018-08-10 18:57 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="11" data-topic="3639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Could you create a Slicer PR to address this ? Thanks</p>
</blockquote>
</aside>
<p>Ok, I’ve submitted a PR with those lines changed.</p>
<aside class="quote no-group" data-username="jcfr" data-post="11" data-topic="3639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>This is because you do not yet have a git repository associated with your custom application source code. In that case, the there is now way to know the date associated with the last commit.</p>
</blockquote>
</aside>
<p>Ok, thanks. I put the application code in a sub-directory of a project, so the .git directory is two levels up. I’ll reorganize things once I have a better idea what I’m doing.</p>

---

## Post #13 by @mschumaker (2018-08-10 19:50 UTC)

<p>I also had this question:</p>
<aside class="quote no-group" data-username="mschumaker" data-post="10" data-topic="3639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>I have some tables in plist files in the Resources directory of a scripted module. How do I make sure these will be copied to the qt-scripted-modules/Resources directory when building?</p>
</blockquote>
</aside>
<p>Thanks!</p>

---

## Post #14 by @jcfr (2018-08-10 19:58 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="12" data-topic="3639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>Ok, I’ve submitted a PR with those lines changed.</p>
</blockquote>
</aside>
<p>Thanks for the contribution. <a href="https://github.com/Slicer/Slicer/pull/1003">PR#1003</a> has just been integrated as  <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27343">27343</a></p>
<aside class="quote no-group" data-username="mschumaker" data-post="13" data-topic="3639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>I have some tables in plist files in the Resources directory of a scripted module. How do I make sure these will be copied to the qt-scripted-modules/Resources directory when building?</p>
</blockquote>
</aside>
<p>What do you mean exactly by <code>some tables in plist files</code> ?</p>
<p>There are two approaches for associated resources with scripted module:</p>
<ul>
<li>
<p>You can associate resources with scripted module by listing them as <code>RESOURCES</code>. For example, see <a href="https://github.com/Slicer/Slicer/blob/87e8a89274eca8c0a249df8785ded16a060006ab/Modules/Scripted/DataProbe/CMakeLists.txt">DataProbe</a>. See also you previous post: <a href="https://discourse.slicer.org/t/adding-an-icon-to-a-button/1012/15" class="inline-onebox">Adding an icon to a button - #15 by mschumaker</a></p>
</li>
<li>
<p>You can generate a Qt resource file. Also already discussed in <a href="https://discourse.slicer.org/t/adding-an-icon-to-a-button/1012/15" class="inline-onebox">Adding an icon to a button - #15 by mschumaker</a></p>
</li>
</ul>

---

## Post #15 by @mschumaker (2018-08-10 20:15 UTC)

<p>Oh… the answer was in my own previous post! <img src="https://emoji.discourse-cdn.com/twitter/man_facepalming.png?v=5" title=":man_facepalming:" class="emoji" alt=":man_facepalming:"><br>
I hadn’t added the files to the MODULE_PYTHON_RESOURCES list.<br>
Property list (.plist) files are an XML-based data format on Mac/iOS. Python has a plistlib library to read them. I’m using some color look-up tables that are stored that way.</p>

---

## Post #16 by @jcfr (2018-08-10 20:22 UTC)

<blockquote>
<p>Property list (.plist) files are an XML-based data format on Mac/iOS. Python has a plistlib library to read them.</p>
</blockquote>
<p>I see. The Slicer build system currently provides its one template for the <code>plist</code> file integrated in the <code>Slicer.app</code> (or `Custom.app):</p>
<p><a href="https://github.com/Slicer/Slicer/blob/87e8a89274eca8c0a249df8785ded16a060006ab/CMake/SlicerMacroBuildApplication.cmake#L451" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/87e8a89274eca8c0a249df8785ded16a060006ab/CMake/SlicerMacroBuildApplication.cmake#L451</a></p>
<p>This was done back in 2014 to ensure the application would work with High DPI monitor. See <a href="https://github.com/Slicer/Slicer/commit/a913ea9af8705fc766d5acd7d9689a8202ba2310">https://github.com/Slicer/Slicer/commit/a913ea9af8705fc766d5acd7d9689a8202ba2310</a></p>
<p>If really needed, we could provide custom application with a way to provide their own template, would that help you ?</p>
<p>That said, using a more traditional approach would ensure the work you do is portable on windows, linux, …</p>

---

## Post #17 by @mschumaker (2018-08-10 21:27 UTC)

<p>Thanks, that’s probably more work than necessary. Reading them isn’t a problem, it’s that I forgot that I should include them in the CMakeLists file. <img src="https://emoji.discourse-cdn.com/twitter/flushed.png?v=5" title=":flushed:" class="emoji" alt=":flushed:"> I just tested that, and it worked.<br>
I’m finding the files by starting from the path of the module’s Python script, then the function plistlib.readPlist reads a file and generates a dictionary. It should still be portable to other systems. Here’s what I’m doing:</p>
<pre><code>    self.moduleDir = os.path.dirname(slicer.util.modulePath(self.__module__))
    ...
    clutDir = "Resources/CLUT"
    NIHFile = "NIH.plist"
    NIHFullPath = self.moduleDir+"/"+clutDir+"/"+NIHFile

    import plistlib
    plistOutput = plistlib.readPlist(NIHFullPath)
    plistRed = plistOutput['Red']
    plistGreen = plistOutput['Green']
    plistBlue = plistOutput['Blue']
</code></pre>
<p>Then I build a vtkMRMLColorTableNode from these arrays.</p>

---

## Post #18 by @mschumaker (2018-08-15 14:58 UTC)

<p>Thanks for your previous assistance.<br>
I’m back to trying to get SlicerVMTK to build with my application. I’m working from an application started using cookiecutter. The build is able to identify a dependency on VMTK and build it, but when it gets to building SlicerVMTK via the ExternalProjectDependency.cmake script, it can’t find SuperBuild/External_VMTK.cmake. The line that produces the error message I get is at:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/CMake/ExternalProjectDependency.cmake#L858">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/CMake/ExternalProjectDependency.cmake#L858" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/CMake/ExternalProjectDependency.cmake#L858" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/main/CMake/ExternalProjectDependency.cmake#L858</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="848" style="counter-reset: li-counter 847 ;">
          <li>  #message(${_sb_proj} "[${_sb_proj}] Property SB_${dep}_OPTIONAL set to ${_optional}")</li>
          <li>  if(NOT _optional)</li>
          <li>    list(APPEND _sb_REQUIRED_DEPENDS ${dep})</li>
          <li>  endif()</li>
          <li>endforeach()</li>
          <li></li>
          <li># Display dependency of project being processed</li>
          <li>if(_sb_REQUIRED_DEPENDS AND SB_SECOND_PASS AND ${_sb_SB_VAR})</li>
          <li>  set(dependency_str "")</li>
          <li>  foreach(dep ${_sb_REQUIRED_DEPENDS})</li>
          <li class="selected">    get_property(_is_included GLOBAL PROPERTY SB_${dep}_FILE_INCLUDED)</li>
          <li>    set(_include_status "")</li>
          <li>    if(_is_included)</li>
          <li>      set(_include_status "[INCLUDED]")</li>
          <li>    endif()</li>
          <li>    set(dependency_str "${dependency_str}${dep}${_include_status}, ")</li>
          <li>  endforeach()</li>
          <li>  ExternalProject_Message(${_sb_proj} "${_sb_proj} =&gt; Requires ${dependency_str}")</li>
          <li>endif()</li>
          <li></li>
          <li># Save variables</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The error I get is:</p>
<blockquote>
<p>– Setting EXTENSION_NAME …: SlicerVMTK<br>
– SuperBuild - First pass<br>
CMake Error at /short/pack/PADPlanner-SB/slicersources-src/CMake/ExternalProjectDependency.cmake:858 (message):<br>
Can’t find External_VMTK.cmake<br>
Call Stack (most recent call first):<br>
/short/pack/PADPlanner-SB/SlicerExtension-VMTK/SuperBuild.cmake:32 (ExternalProject_Include_Dependencies)<br>
/short/pack/PADPlanner-SB/SlicerExtension-VMTK/CMakeLists.txt:33 (include)</p>
</blockquote>
<p>I’m fetching the extension code from a repository, and so the extension source is being placed in SlicerExtension-VMTK in the main project-SuperBuild directory. I need help with how to get the build script to find the External_VMTK.cmake file.</p>

---

## Post #19 by @mschumaker (2018-08-15 17:58 UTC)

<p>It looks like when the build is at the stage of configuring the extension directory for SlicerExtension-VMTK, the value of EXTERNAL_PROJECT_DIR is /short/pack/PADPlanner-SB/slicersources-src/SuperBuild/External_VMTK.cmake, rather than the location of the extension.</p>

---

## Post #20 by @mschumaker (2018-08-17 16:30 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a>, any thoughts on this? I may test another extension, because I’m not sure if this is a general problem with including extensions that have dependencies via Slicer_EXTENSION_SOURCE_DIRS, or just with SlicerVMTK. I looked at the elastix extension to see if I could see something SlicerVMTK was missing, and it looked about the same, but apparently that wasn’t the best choice for comparison.</p>

---

## Post #21 by @lassoan (2018-08-18 07:07 UTC)

<p>Slicer build process automatically finds ExternalX.cmake files to build dependencies and rely on their correct implementation to find potential additional dependencies, build, and install them.</p>
<p>SlicerIGT, SlicerOpenIGTLink, and SlicerVirtualReality extensions are all superbuild extensions that are tested to work well when used in a custom Slicer application. Test if they work correctly for you and if they do then compare what is different in VMTK.</p>

---

## Post #22 by @mschumaker (2018-08-18 13:59 UTC)

<p>Thanks, I’ll try those ones.</p>

---

## Post #23 by @mschumaker (2018-08-30 15:20 UTC)

<p>I’m still trying to identify differences between the CMake scripts for SlicerOpenIGTLink and SlicerVMTK, but looking at the CDash results for the three extensions you suggested, I see that <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerVirtualReality" rel="nofollow noopener">SlicerVirtualReality</a> is not able to build for Mac, and the build error relates to finding an include file from its external package OpenVR. I’m not sure if this is related, but <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerVirtualReality" rel="nofollow noopener">SlicerVirtualReality</a>, <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerVMTK" rel="nofollow noopener">SlicerVMTK</a>, and <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerElastix" rel="nofollow noopener">SlicerElastix</a> are all failing to build on Mac, and Mac only. I may start a separate thread about this.</p>

---

## Post #24 by @lassoan (2018-08-30 16:26 UTC)

<p>First you need to make sure that the extension builds without problems when it is built standalone. Once it works, you can try to build it as part of a custom Slicer application. There may be additional complications in superbuild extensions, because if the extension is built as part of Slicer then Slicer’s build system must build and package all the third-party libraries that the extension depends on.</p>

---

## Post #25 by @mschumaker (2018-08-30 17:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="24" data-topic="3639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>First you need to make sure that the extension builds without problems when it is built standalone. Once it works, you can try to build it as part of a custom Slicer application.</p>
</blockquote>
</aside>
<p>Absolutely. I just re-tested the up-to-date extension and VMTK, with the most recent Slicer’s VTK and ITK, and it is able to build on its own. The problem is when I try to include it in a custom application, either by referencing the pre-downloaded extension source directory, or using the FetchContent_Populate macro to fetch the source.</p>
<aside class="quote no-group" data-username="lassoan" data-post="24" data-topic="3639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There may be additional complications in superbuild extensions, because if the extension is built as part of Slicer then Slicer’s build system must build and package all the third-party libraries that the extension depends on.</p>
</blockquote>
</aside>
<p>The SuperBuild seems able to recognize the dependence on VMTK and build it, then it puts the shared object libraries from VMTK in the main SuperBuild directory, but then when running the ExternalProject_Include_Dependencies macro when building Slicer itself, it can’t find External_VMTK.cmake.<br>
Other than that, I ran into a minor issue when doing a completely fresh build because VMTK’s dependence on ITK and VTK wasn’t specified, but that was a quick fix.</p>

---

## Post #26 by @lassoan (2018-08-31 05:07 UTC)

<p>The extension must store External_(dependency).cmake files in SuperBuild subfolder.</p>

---

## Post #27 by @mschumaker (2018-08-31 15:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="26" data-topic="3639" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The extension must store External_(dependency).cmake files in SuperBuild subfolder.</p>
</blockquote>
</aside>
<p>That’s the confusing thing - it does. The file is in SlicerExtension-VMTK/SuperBuild, but the ExternalProject_Include_Dependencies macro doesn’t check there when building Slicer. If I print out where it tries to access the file when building Slicer, it tries:</p>
<ul>
<li>~/app-SuperBuild/slicersources-src/SuperBuild/External_VMTK.cmake</li>
<li>(blank)</li>
<li>/External_VMTK.cmake</li>
<li>a foreach statement that’s not entered</li>
</ul>
<p>The last two are supposed to use values from EXTERNAL_PROJECT_ADDITIONAL_DIR and a list called EXTERNAL_PROJECT_ADDITIONAL_DIRS, but they are blank.<br>
The relevant code is here: <a href="https://github.com/Slicer/Slicer/blob/master/CMake/ExternalProjectDependency.cmake#L858" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/master/CMake/ExternalProjectDependency.cmake#L858</a><br>
For some reason, the values of EXTERNAL_PROJECT_ADDITIONAL_DIR and the EXTERNAL_PROJECT_ADDITIONAL_DIRS list aren’t being set, or are being cleared? At the Configure stage for the superbuild, these values are present, though.</p>

---

## Post #28 by @lassoan (2018-08-31 17:50 UTC)

<p>Try to add SlicerOpenIGTLink extension to your project, too, and see if there is any difference between where OpenIGTLink library shows up and VMTK library shows up. We would then have a better idea where the problem might be.</p>

---

## Post #29 by @mschumaker (2018-08-31 20:44 UTC)

<p>I’m having trouble getting SlicerOpenIGTLink to compile, but it’s a different problem, and I can’t tell if it’s getting past the place where SlicerExtension-VMTK stops. Here’s the error:</p>
<blockquote>
<p>[ 97%] <strong>Performing configure step for ‘Slicer’</strong><br>
…<br>
– Configuring extension directory: SlicerOpenIGTLink<br>
– Checking EXTENSION_NAME variable<br>
– Checking EXTENSION_NAME variable - NOTDEFINED<br>
– Checking MODULE_NAME variable<br>
– Checking MODULE_NAME variable - NOTDEFINED<br>
– Checking PROJECT_NAME variable<br>
– Checking PROJECT_NAME variable - SlicerOpenIGTLink<br>
– Setting EXTENSION_NAME …: SlicerOpenIGTLink<br>
– Checking EXTENSION_NAME variable<br>
– Checking EXTENSION_NAME variable - SlicerOpenIGTLink<br>
– Looking for decorator header qSlicerOpenIGTLinkIFModuleWidgetsPythonQtDecorators.h</p>
<p>– Looking for decorator header qSlicerOpenIGTLinkIFModuleWidgetsPythonQtDecorators.h - Not found</p>
<p>– Configuring Loadable module: OpenIGTLinkIF [qSlicerOpenIGTLinkIFModuleExport.h]</p>
<p>CMake Error at /short/pack/PADPlanner-SB/SlicerOpenIGTLink/OpenIGTLinkIF/Testing/CMakeLists.txt:29 (list):<br>
list sub-command INSERT requires at least three arguments.</p>
</blockquote>
<p>I’m still not certain about what’s happening, but something that may be interesting is that with OpenIGTLink, I don’t see the message output lines that I added to ExternalProjectDependency.cmake in the build output. In both cases, I see them in the Configure stage in the CMake GUI, but with SlicerExtension-VMTK, I see them again in the Slicer build configuration phase. It makes me think that OpenIGTLink doesn’t re-run the macro during the build.</p>
<p>Here’s the build output leading up to the error when I try adding SlicerExtension-VMTK to Slicer. The four lines after “SuperBuild - First pass” are my additions.</p>
<blockquote>
<p>[ 97%] <strong>Performing configure step for ‘Slicer’</strong><br>
…<br>
– Configuring extension directory: SlicerExtension-VMTK<br>
CMake Warning (dev) at /short/pack/PADPlanner-SB/SlicerExtension-VMTK/CMakeLists.txt:4 (project):<br>
Policy CMP0048 is not set: project() command manages VERSION variables.<br>
Run “cmake --help-policy CMP0048” for policy details.  Use the cmake_policy<br>
command to set the policy and suppress this warning.</p>
<p>The following variable(s) would be set to empty:</p>
<pre><code>PROJECT_VERSION
PROJECT_VERSION_MAJOR
PROJECT_VERSION_MINOR
PROJECT_VERSION_PATCH
</code></pre>
<p>This warning is for project developers.  Use -Wno-dev to suppress it.</p>
<p>– Checking EXTENSION_NAME variable<br>
– Checking EXTENSION_NAME variable - NOTDEFINED<br>
– Checking MODULE_NAME variable<br>
– Checking MODULE_NAME variable - NOTDEFINED<br>
– Checking PROJECT_NAME variable<br>
– Checking PROJECT_NAME variable - SlicerVMTK<br>
– Setting EXTENSION_NAME …: SlicerVMTK<br>
– SuperBuild - First pass<br>
EXTERNAL_PROJECT_DIR location is /short/pack/PADPlanner-SB/slicersources-src/SuperBuild/External_VMTK.cmake<br>
dep_FILEPATH location is<br>
EXTERNAL_PROJECT_ADDITIONAL_DIR location is /External_VMTK.cmake<br>
This is the whole EXTERNAL_PROJECT_ADDITIONAL_DIRS list:<br>
CMake Error at /short/pack/PADPlanner-SB/slicersources-src/CMake/ExternalProjectDependency.cmake:862 (message):<br>
Can’t find External_VMTK.cmake<br>
Call Stack (most recent call first):<br>
/short/pack/PADPlanner-SB/SlicerExtension-VMTK/SuperBuild.cmake:32 (ExternalProject_Include_Dependencies)<br>
/short/pack/PADPlanner-SB/SlicerExtension-VMTK/CMakeLists.txt:33 (include)</p>
<p>-- Configuring incomplete, errors occurred!<br>
See also “/short/pack/PADPlanner-SB/Slicer-build/CMakeFiles/CMakeOutput.log”.<br>
See also “/short/pack/PADPlanner-SB/Slicer-build/CMakeFiles/CMakeError.log”.<br>
make[2]: *** [slicersources-build/Slicer-prefix/src/Slicer-stamp/Slicer-configure] Error 1<br>
make[1]: *** [slicersources-build/CMakeFiles/Slicer.dir/all] Error 2<br>
make: *** [all] Error 2</p>
</blockquote>

---

## Post #30 by @mschumaker (2018-08-31 21:29 UTC)

<p>Actually, I tried commenting out the line OpenIGTLink was failing on, the list sub-command, and the configuration carries on, and completes, without writing the messages I added to ExternalProjectDependency.cmake. Here’s the new extension configuration output for OpenIGTLink:</p>
<blockquote>
<p>– Configuring extension directory: SlicerOpenIGTLink<br>
– Checking EXTENSION_NAME variable<br>
– Checking EXTENSION_NAME variable - NOTDEFINED<br>
– Checking MODULE_NAME variable<br>
– Checking MODULE_NAME variable - NOTDEFINED<br>
– Checking PROJECT_NAME variable<br>
– Checking PROJECT_NAME variable - SlicerOpenIGTLink<br>
– Setting EXTENSION_NAME …: SlicerOpenIGTLink<br>
– Checking EXTENSION_NAME variable<br>
– Checking EXTENSION_NAME variable - SlicerOpenIGTLink<br>
– Looking for decorator header qSlicerOpenIGTLinkIFModuleWidgetsPythonQtDecorators.h<br>
– Looking for decorator header qSlicerOpenIGTLinkIFModuleWidgetsPythonQtDecorators.h - Not found<br>
– Configuring Loadable module: OpenIGTLinkIF [qSlicerOpenIGTLinkIFModuleExport.h]<br>
– Looking for decorator header qSlicerOpenIGTLinkRemoteModuleWidgetsPythonQtDecorators.h<br>
– Looking for decorator header qSlicerOpenIGTLinkRemoteModuleWidgetsPythonQtDecorators.h - Not found<br>
– Configuring Loadable module: OpenIGTLinkRemote [qSlicerOpenIGTLinkRemoteModuleExport.h]<br>
– Looking for decorator header qSlicerPlusRemoteModuleWidgetsPythonQtDecorators.h<br>
– Looking for decorator header qSlicerPlusRemoteModuleWidgetsPythonQtDecorators.h - Not found<br>
– Configuring Loadable module: PlusRemote [qSlicerPlusRemoteModuleExport.h]<br>
– Looking for decorator header qSlicerUltrasoundRemoteControlModuleWidgetsPythonQtDecorators.h<br>
– Looking for decorator header qSlicerUltrasoundRemoteControlModuleWidgetsPythonQtDecorators.h - Not found<br>
– Configuring Scripted module: UltrasoundRemoteControl<br>
– Skipping extension packaging: SlicerOpenIGTLink - Slicer_SOURCE_DIR is defined.<br>
CMake Warning at Utilities/Scripts/SlicerWizard/doc/CMakeLists.txt:41 (message):<br>
Warning: sphinx-build not found: Python documentation will not be created</p>
<p>– Setting ‘CTEST_MODEL’ variable with default value ‘Experimental’<br>
– Setting ‘MIDAS_PACKAGE_URL’ variable with default value ‘<a href="http://slicer.kitware.com/midas3" rel="noopener nofollow ugc">http://slicer.kitware.com/midas3</a>’<br>
– Setting ‘MIDAS_PACKAGE_EMAIL’ variable with default value ‘OBFUSCATED’<br>
– Setting ‘MIDAS_PACKAGE_API_KEY’ variable with default value ‘OBFUSCATED’<br>
– Setting CPACK_PACKAGE_NAME to ‘PADPlanner’<br>
– Setting CPACK_PACKAGE_VENDOR to ‘Sunnybrook Research Institute’<br>
– Setting CPACK_PACKAGE_VERSION_MAJOR to ‘4’<br>
– Setting CPACK_PACKAGE_VERSION_MINOR to ‘9’<br>
– Setting CPACK_PACKAGE_VERSION_PATCH to ‘0’<br>
– Setting CPACK_PACKAGE_VERSION to ‘4.9.0-2018-08-28’<br>
– Setting CPACK_PACKAGE_INSTALL_DIRECTORY to ‘PADPlanner 4.9.0-2018-08-28’<br>
– Setting CPACK_PACKAGE_DESCRIPTION_FILE to ‘/short/pack/PADPlanner-SB/slicersources-src/README.txt’<br>
– Setting CPACK_RESOURCE_FILE_LICENSE to ‘/short/pack/PADPlanner-SB/slicersources-src/License.txt’<br>
– Setting CPACK_PACKAGE_DESCRIPTION_SUMMARY to ‘Surgical planning tool for Peripheral Artery Disease’<br>
– Setting CPACK_PACKAGE_ICON to ‘/Users/michaelschumaker/Development/mschumaker/Slicelets/PADFusion/CustomAppTemplateConfig/PADPlanner/Applications/PADPlannerApp/Resources/App.icns’<br>
– Configuring done<br>
– Generating done<br>
– Build files have been written to: /short/pack/PADPlanner-SB/Slicer-build<br>
[ 98%] <strong>Performing build step for ‘Slicer’</strong></p>
</blockquote>

---

## Post #31 by @jcfr (2018-08-31 21:47 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="29" data-topic="3639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>– Configuring Loadable module: OpenIGTLinkIF [qSlicerOpenIGTLinkIFModuleExport.h]</p>
<p>CMake Error at /short/pack/PADPlanner-SB/SlicerOpenIGTLink/OpenIGTLinkIF/Testing/CMakeLists.txt:29 (list):<br>
list sub-command INSERT requires at least three arguments.</p>
</blockquote>
</aside>
<p>We tried the bundling of <code>SlicerOpenIGTLink</code> with <code>BUILD_TESTING</code> set to <code>OFF</code>, this explain why you see this error. In the following bloc:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/openigtlink/SlicerOpenIGTLink/blob/17ef646fe711ac7db9c48388218ee18eaf0839f5/OpenIGTLinkIF/Testing/CMakeLists.txt#L27-L29">
  <header class="source">

      <a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/17ef646fe711ac7db9c48388218ee18eaf0839f5/OpenIGTLinkIF/Testing/CMakeLists.txt#L27-L29" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/17ef646fe711ac7db9c48388218ee18eaf0839f5/OpenIGTLinkIF/Testing/CMakeLists.txt#L27-L29" target="_blank" rel="noopener">openigtlink/SlicerOpenIGTLink/blob/17ef646fe711ac7db9c48388218ee18eaf0839f5/OpenIGTLinkIF/Testing/CMakeLists.txt#L27-L29</a></h4>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="27" style="counter-reset: li-counter 26 ;">
          <li># Add '--launcher-additional-settings' to launch command</li>
          <li>list(FIND Slicer_LAUNCH_COMMAND "--launch" launch_index)</li>
          <li>list(INSERT Slicer_LAUNCH_COMMAND ${launch_index} ${Slicer_ADDITIONAL_LAUNCHER_SETTINGS}) </li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The fix is most likely to change it if with:</p>
<pre><code class="lang-auto"># Add '--launcher-additional-settings' to launch command unless it is bundled in Slicer
if(NOT DEFINED Slicer_SOURCE_DIR)
  list(FIND Slicer_LAUNCH_COMMAND "--launch" launch_index)
  list(INSERT Slicer_LAUNCH_COMMAND ${launch_index} ${Slicer_ADDITIONAL_LAUNCHER_SETTINGS}) 
endif()
</code></pre>

---

## Post #32 by @mschumaker (2018-08-31 21:52 UTC)

<p>Thanks, that makes sense. With those lines omitted, it’s able to carry on past the configuration stage.</p>

---

## Post #33 by @jcfr (2018-08-31 21:55 UTC)

<p>Now the bundling of the SlicerVMTK should be done doing something like this:</p>
<pre><code class="lang-auto"># SlicerVMTK
set(extension_name "SlicerVMTK")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")
FetchContent_Populate(${extension_name}
  SOURCE_DIR     ${${extension_name}_SOURCE_DIR}
  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/vmtk/SlicerExtension-VMTK.git
  GIT_TAG        c5dd07e2df6834342035cbdb1e0c461b452009d4
  GIT_PROGRESS   1
  QUIET
  )
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})
</code></pre>
<p>Few things would have to be updated in the extension:</p>
<ul>
<li>
<p>The <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/c5dd07e2df6834342035cbdb1e0c461b452009d4/CMakeLists.txt#L42-L49">block dealing with CPack</a> need to be updated. For an example, see <a href="https://github.com/openigtlink/SlicerOpenIGTLink/commit/da0bc5ce5c9a528da4f0a734c4bd099e579492d0">https://github.com/openigtlink/SlicerOpenIGTLink/commit/da0bc5ce5c9a528da4f0a734c4bd099e579492d0</a></p>
</li>
<li>
<p>Instead of checking out <code>master</code> of VMTK, it should be changed to specific commit. See <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/c5dd07e2df6834342035cbdb1e0c461b452009d4/SuperBuild/External_VMTK.cmake#L27">here</a></p>
</li>
</ul>
<p>As a side note, it would be great if you could search for other occurrence that pattern and submit a PR fixing OpenIGTLinkIF.</p>

---

## Post #34 by @mschumaker (2018-08-31 22:05 UTC)

<p>Ok, I can update the block dealing with CPack, and I’ll make sure to specify a commit. Once all this is sorted out, I can make that change to OpenIGTLinkIF as well.</p>
<p>One thing that’s confusing is the different naming of the extension. In a number of places it’s SlicerVMTK, but the repository is SlicerExtension-VMTK. I’m not sure when to use which name.</p>

---

## Post #35 by @jcfr (2018-09-04 05:01 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="34" data-topic="3639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>One thing that’s confusing is the different naming of the extension. In a number of places it’s SlicerVMTK, but the repository is SlicerExtension-VMTK. I’m not sure when to use which name.</p>
</blockquote>
</aside>
<p>In doubt, use the name of the project found in the <code>project(NameOfProject)</code> statement.</p>

---

## Post #36 by @mschumaker (2018-09-05 19:28 UTC)

<p>So after everything… the problem has been solved by setting the extension_name to be SlicerVMTK. At the point where it was failing, the project name was being assigned as the expected extension name, and so the extension source files couldn’t be found.</p>
<p>As discussed, I’ve revised the block dealing with CPack, and I’ll submit a PR, though I would also like to add ITK and VTK as dependencies of the extension. When I tried a completely fresh superbuild, it attempted to build VMTK before ITK, and stopped. How can I add those dependencies correctly?<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/mschumak/SlicerExtension-VMTK/blob/Sept4-application-superbuild-fix/CMakeLists.txt#L19" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/mschumak/SlicerExtension-VMTK/blob/Sept4-application-superbuild-fix/CMakeLists.txt#L19" target="_blank" rel="nofollow noopener">mschumak/SlicerExtension-VMTK/blob/Sept4-application-superbuild-fix/CMakeLists.txt#L19</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="9" style="counter-reset: li-counter 8 ;">
<li>set(EXTENSION_CONTRIBUTORS "Daniel Haehn (Boston Childrens Hospital), Luca Antiga (Orobix), Steve Pieper (Isomics), Jean-Christophe Fillion-Robin (Kitware)")</li>
<li>set(EXTENSION_DESCRIPTION "Vascular Modeling Toolkit for vessel tree segmentation and centerline extraction.")</li>
<li>set(EXTENSION_STATUS "Beta")</li>
<li>set(EXTENSION_ICONURL "http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269")</li>
<li>set(EXTENSION_SCREENSHOTURLS "http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=126 http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=227 http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=228 http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=229")</li>
<li>set(EXTENSION_LICENSE_FILE ${Slicer_LICENSE_FILE})</li>
<li>set(EXTENSION_README_FILE ${Slicer_README_FILE})</li>
<li>set(EXTENSION_BUILD_SUBDIRECTORY inner-build)</li>
<li>
</li>
<li>set(EXTENSION_DEPENDS "")</li>
<li class="selected">#list(APPEND EXTENSION_DEPENDS ITKv4)</li>
<li>#list(APPEND EXTENSION_DEPENDS VTKv9)</li>
<li>
</li>
<li>set(SUPERBUILD_TOPLEVEL_PROJECT inner)</li>
<li>
</li>
<li>#-----------------------------------------------------------------------------</li>
<li>find_package(Slicer REQUIRED)</li>
<li>include(${Slicer_USE_FILE})</li>
<li>mark_as_superbuild(Slicer_DIR)</li>
<li>
</li>
<li>find_package(Git REQUIRED)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #37 by @lassoan (2018-09-05 20:40 UTC)

<p>Sounds great!</p>
<p>You should be able to define dependencies by setting <code>${proj}_DEPENDS</code> in <code>External_(yourlibrary).cmake</code>, as it is done for example for this external library:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/master/SuperBuild/External_OpenIGTLinkIO.cmake#L4" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/master/SuperBuild/External_OpenIGTLinkIO.cmake#L4" target="_blank">openigtlink/SlicerOpenIGTLink/blob/master/SuperBuild/External_OpenIGTLinkIO.cmake#L4</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
<li>set(proj OpenIGTLinkIO)</li>
<li>
</li>
<li># Set dependency list</li>
<li class="selected">set(${proj}_DEPENDS OpenIGTLink)</li>
<li>
</li>
<li># Include dependent projects if any</li>
<li>ExternalProject_Include_Dependencies(${proj} PROJECT_VAR proj DEPENDS_VAR ${proj}_DEPENDS)</li>
<li>
</li>
<li>if(${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj})</li>
<li>unset(OpenIGTLinkIO_DIR CACHE)</li>
<li>find_package(OpenIGTLinkIO REQUIRED)</li>
<li>endif()</li>
<li>
</li>
<li># Sanity checks</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #38 by @mschumaker (2018-09-05 21:34 UTC)

<p>Ok, thanks, I’ll do that.</p>
<p>Thank you for your help, <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/jcfr">@jcfr</a>!</p>

---

## Post #39 by @mschumaker (2018-09-06 20:26 UTC)

<p>It’s almost there… but not quite. Everything compiles, but I’m unable to access the Python libraries for VMTK from the interpreter. Also, there was a problem when I attempted to package the app. The VMTK-build directory is in ~/app-SuperBuild/slicersources-build, but the script was expecting it to be in ~/app-SuperBuild, so “make package” failed.</p>
<p>Do you have any suggestions?</p>

---

## Post #40 by @jcfr (2018-09-06 22:44 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="39" data-topic="3639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>~/app-SuperBuild/slicersources-build, but the script was expecting it to be in ~/app-SuperBuild, so “make package” failed.</p>
</blockquote>
</aside>
<p>This section</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/blob/547eb4710e1da103899e7ab63e3023c2bcfab83c/SuperBuild/External_VMTK.cmake#L20-L29">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/547eb4710e1da103899e7ab63e3023c2bcfab83c/SuperBuild/External_VMTK.cmake#L20-L29" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/547eb4710e1da103899e7ab63e3023c2bcfab83c/SuperBuild/External_VMTK.cmake#L20-L29" target="_blank" rel="noopener">vmtk/SlicerExtension-VMTK/blob/547eb4710e1da103899e7ab63e3023c2bcfab83c/SuperBuild/External_VMTK.cmake#L20-L29</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="20" style="counter-reset: li-counter 19 ;">
          <li>if(NOT DEFINED git_protocol)</li>
          <li>  set(git_protocol "git")</li>
          <li>endif()</li>
          <li></li>
          <li>ExternalProject_Add(${proj}</li>
          <li>  ${${proj}_EP_ARGS}</li>
          <li>  GIT_REPOSITORY "${git_protocol}://github.com/vmtk/vmtk.git"</li>
          <li>  GIT_TAG "a0dacdc2499a3828d7a649c9c1d32363ce407b1a"</li>
          <li>  SOURCE_DIR ${CMAKE_BINARY_DIR}/${proj}</li>
          <li>  BINARY_DIR ${proj}-build</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>should be updated based on</p>
<p><a href="https://github.com/Slicer/Slicer/blob/f08936e114b0cff769d6e4cb196d697848f29194/Utilities/Templates/Extensions/SuperBuild/SuperBuild/External_Foo.cmake#L23-L45" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/f08936e114b0cff769d6e4cb196d697848f29194/Utilities/Templates/Extensions/SuperBuild/SuperBuild/External_Foo.cmake#L23-L45</a></p>
<p>consider also removing <code>git_protocol</code> and instead using <code>EP_GIT_PROTOCOL</code> as well as <code>ExternalProject_SetIfNotDefined</code></p>

---

## Post #41 by @mschumaker (2018-10-26 17:47 UTC)

<p>I’m back at this after having to set it aside for some other work. I’m still trying to get SlicerVMTK to work from within a custom application that I started using cookiecutter. Thank you for your previous help.</p>
<p>I made the changes to External_VMTK.cmake described in the previous comment, and I can build and package the application, but I still can’t access the VMTK classes from the Python interpreter. When I try to import one of the VMTK libraries, I get the error:</p>
<blockquote>
<p>Python 2.7.13 (default, Oct 24 2018, 15:58:48)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on Darwin<br>
&gt;&gt;&gt; import vtkvmtkMiscPython<br>
Traceback (most recent call last):<br>
File “&lt;console&gt;”, line 1, in &lt;module&gt;<br>
ImportError: dlopen(/Applications/PADPlanner.app/Contents/lib/PADPlanner-4.9/qt-loadable-modules/Python/vtkvmtkMiscPython.so, 2): Library not loaded: libvtkvmtkMiscPythonD.dylib<br>
Referenced from: /Applications/PADPlanner.app/Contents/lib/PADPlanner-4.9/qt-loadable-modules/Python/vtkvmtkMiscPython.so<br>
Reason: image not found</p>
</blockquote>
<p>So the vtkvmtkMiscPython.so file can’t find libvtkvmtkMiscPythonD.dylib. Just as a test, I copied the .dylib files to the same file as the .so file, and restarted the app, but that didn’t change anything.</p>
<p>What am I missing to link these libraries?</p>
<p>My External_VMTK.cmake file with changes is here:<br>
<a href="https://github.com/mschumak/SlicerExtension-VMTK/blob/Oct24-refixing/SuperBuild/External_VMTK.cmake#L20-L41" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/mschumak/SlicerExtension-VMTK/blob/Oct24-refixing/SuperBuild/External_VMTK.cmake#L20-L41</a></p>
<p>The section of the CMakeLists.txt file for my custom application that deals with extensions is:</p>
<blockquote>
<p># Enable/Disable Slicer custom modules: To create a new module, use the SlicerExtensionWizard.<br>
set(Slicer_EXTENSION_SOURCE_DIRS<br>
/Users/michaelschumaker/Development/mschumaker/Slicelets/PADFusion/PADFusion<br>
)<br>
# Add remote extension source directories<br>
<span class="hashtag-raw">#SlicerVMTK</span><br>
set(extension_name “SlicerVMTK”)<br>
set(${extension_name}_SOURCE_DIR “${CMAKE_BINARY_DIR}/${extension_name}”)</p>
</blockquote>
<blockquote>
<p>FetchContent_Populate(${extension_name}<br>
SOURCE_DIR     ${${extension_name}_SOURCE_DIR}<br>
GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/mschumak/SlicerExtension-VMTK.git<br>
GIT_TAG        a847b808cd772ea77992b64a6fb3bdf9388d2171<br>
GIT_PROGRESS   1<br>
)<br>
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})<br>
<br>
# Add Slicer sources<br>
add_subdirectory(${slicersources_SOURCE_DIR} ${slicersources_BINARY_DIR})</p>
</blockquote>
<p>Thank you for your help!</p>

---

## Post #42 by @mschumaker (2018-10-31 14:23 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a>, any thoughts?<br>
Thanks!</p>

---
