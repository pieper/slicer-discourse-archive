# Help submitting extension Breast DCE-MRI FTV

**Topic ID**: 18955
**Date**: 2021-07-28
**URL**: https://discourse.slicer.org/t/help-submitting-extension-breast-dce-mri-ftv/18955

---

## Post #1 by @rohan_n (2021-07-28 05:03 UTC)

<p>I just submitted pull request for my new extension to the master branch of Extensions Index.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ee6b91c979b3ac0f320a8c0cc3436c936cd5d75.png" data-download-href="/uploads/short-url/4pmE3s3h5JplPRouoEHenlLNCKN.png?dl=1" title="pullrequestmaster" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ee6b91c979b3ac0f320a8c0cc3436c936cd5d75_2_690x302.png" alt="pullrequestmaster" data-base62-sha1="4pmE3s3h5JplPRouoEHenlLNCKN" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ee6b91c979b3ac0f320a8c0cc3436c936cd5d75_2_690x302.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ee6b91c979b3ac0f320a8c0cc3436c936cd5d75_2_1035x453.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ee6b91c979b3ac0f320a8c0cc3436c936cd5d75_2_1380x604.png 2x" data-dominant-color="F4F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pullrequestmaster</span><span class="informations">1820×798 90 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The attached image says that 1 of the 3 checks failed. Is this something I need to fix? If so, how?</p>
<p>I submitted this pull request to master. Which other branches of ExtensionsIndex do you recommend that I submit pull request to?</p>
<p>Please let me know as soon as possible if there is anything in the SlicerBreast_DCEMRI_FTV repository that needs to be corrected. I really need complete this submission process before Friday.</p>
<p>Thanks!<br>
Rohan</p>

---

## Post #2 by @pieper (2021-07-28 14:58 UTC)

<p>Hi <a class="mention" href="/u/rohan_n">@rohan_n</a> this looks like a great extension and there were just a few comments in the PR.  For this one, you can click the “Details” button on the right side of the CI check and it should take you to this page with the issue and suggested change.  Thanks for the contribution!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/083677363a254043b248598341fcea15d3efdc5d.png" data-download-href="/uploads/short-url/1aEvJQhGwmUJC73qmbRalkQOO4J.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/083677363a254043b248598341fcea15d3efdc5d_2_690x466.png" alt="image" data-base62-sha1="1aEvJQhGwmUJC73qmbRalkQOO4J" width="690" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/083677363a254043b248598341fcea15d3efdc5d_2_690x466.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/083677363a254043b248598341fcea15d3efdc5d_2_1035x699.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/083677363a254043b248598341fcea15d3efdc5d_2_1380x932.png 2x" data-dominant-color="6F6D6D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1490×1007 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @rohan_n (2021-07-28 16:57 UTC)

<p>Thanks, I committed the changes suggested by you and James.<br>
When can I expect this to appear in extension manager, and will it be in latest nightly release or latest stable release?</p>

---

## Post #4 by @pieper (2021-07-28 18:56 UTC)

<p>I just merged the s4ext file into the ExtentionIndex master, so that means it should show up tomorrow mid-day as an extension for the Nightly build.  If you also want it to be available for the current stable release, you can make a PR against the 4.11 branch, assuming you have tested it there.  For a new extension usually you pick either one or the other for first tests, use the nightly if you need new features from the core that aren’t in the latest release or use the release to avoid incompatibilities popping up if the nightly changes.  Longer term projects often end up with a stable version of the extension pointing to a release, and a development branch is configured to work with the nightly.  You manage this with the branch of your extension repo that is referenced from the s4ext file in the corresponding branches of the ExtensionIndex.  (Hope that is all clear).</p>

---

## Post #5 by @rohan_n (2021-07-28 19:13 UTC)

<p>Thanks for the info. I actually did all of my testing in 4.11 so I just submitted a pull request to the 4.11 branch of the extensions index.</p>

---

## Post #6 by @pieper (2021-07-28 20:45 UTC)

<p>Perfect, it’s merged in both now.</p>

---

## Post #7 by @rohan_n (2021-07-30 05:47 UTC)

<p>Hello again.<br>
When I install the extension from the Extension Manager, I get the following error</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:\Users\rnadkarni\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\Lib\imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "C:/Users/rnadkarni/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/Breast_DCEMRI_FTV/lib/Slicer-4.11/qt-scripted-modules/DCE_TumorMapProcess.py", line 106, in &lt;module&gt;
    import Breast_DCEMRI_FTV_plugins2
ModuleNotFoundError: No module named 'Breast_DCEMRI_FTV_plugins2'
</code></pre>
<p>Would you be able to suggest the changes that would fix this error in a way that I can easily commit them to my Github repository?<br>
I’m guessing that a similar error might occur in DCE_IDandPhaseSelect.py, which imports Breast_DCEMRI_FTV_plugins1.<br>
Sorry about this. I tested the extension on 2 different computers prior to submitting it and did not see this error.</p>
<p>Thanks,<br>
Rohan Nadkarni</p>

---

## Post #8 by @jamesobutler (2021-07-30 12:34 UTC)

<p>Places like linked below are where you’re missing the build process to include your “Lib” type directory of files. To fully make sure your extension will work from being downloaded from the Extensions Manager, you should actually build your extension (not just using the additional-modules flag). Building the extension all the way to the ZIP file and installing it manually into Slicer will confirm it will work.  <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_build_an_extension_.3F" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/FAQ - Slicer Wiki</a></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/rnadkarni2/SlicerBreast_DCEMRI_FTV/blob/efe028b7dd776f263627a69bfcd3c922938ca3a9/DCE_TumorMapProcess/CMakeLists.txt#L6">
  <header class="source">

      <a href="https://github.com/rnadkarni2/SlicerBreast_DCEMRI_FTV/blob/efe028b7dd776f263627a69bfcd3c922938ca3a9/DCE_TumorMapProcess/CMakeLists.txt#L6" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/rnadkarni2/SlicerBreast_DCEMRI_FTV/blob/efe028b7dd776f263627a69bfcd3c922938ca3a9/DCE_TumorMapProcess/CMakeLists.txt#L6" target="_blank" rel="noopener nofollow ugc">rnadkarni2/SlicerBreast_DCEMRI_FTV/blob/efe028b7dd776f263627a69bfcd3c922938ca3a9/DCE_TumorMapProcess/CMakeLists.txt#L6</a></h4>



  <pre class="onebox">    <code class="lang-txt">
      <ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
          <li>#-----------------------------------------------------------------------------</li>
          <li>set(MODULE_NAME DCE_TumorMapProcess)</li>
          <li>
          </li>
<li>#-----------------------------------------------------------------------------</li>
          <li>set(MODULE_PYTHON_SCRIPTS</li>
          <li class="selected">  ${MODULE_NAME}.py</li>
          <li>  )</li>
          <li>
          </li>
<li>set(MODULE_PYTHON_RESOURCES</li>
          <li>  Resources/Icons/${MODULE_NAME}.png</li>
          <li>  Resources/UI/${MODULE_NAME}.ui</li>
          <li>  )</li>
          <li>
          </li>
<li>#-----------------------------------------------------------------------------</li>
          <li>slicerMacroBuildScriptedModule(</li>
          <li>  NAME ${MODULE_NAME}</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>See this other extension that has a “Lib” type directory for example</p><aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/86ccd9f223c0eddef913f7977ceeac67e84934ce/SegmentEditorSurfaceCut/CMakeLists.txt#L9">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/86ccd9f223c0eddef913f7977ceeac67e84934ce/SegmentEditorSurfaceCut/CMakeLists.txt#L9" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/86ccd9f223c0eddef913f7977ceeac67e84934ce/SegmentEditorSurfaceCut/CMakeLists.txt#L9" target="_blank" rel="noopener nofollow ugc">lassoan/SlicerSegmentEditorExtraEffects/blob/86ccd9f223c0eddef913f7977ceeac67e84934ce/SegmentEditorSurfaceCut/CMakeLists.txt#L9</a></h4>



  <pre class="onebox">    <code class="lang-txt">
      <ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
          <li>
          </li>
<li>#-----------------------------------------------------------------------------</li>
          <li>set(MODULE_NAME SegmentEditorSurfaceCut)</li>
          <li>
          </li>
<li>#-----------------------------------------------------------------------------</li>
          <li>set(MODULE_PYTHON_SCRIPTS</li>
          <li>  ${MODULE_NAME}.py</li>
          <li>  ${MODULE_NAME}Lib/__init__.py</li>
          <li class="selected">  ${MODULE_NAME}Lib/SegmentEditorEffect.py</li>
          <li>  )</li>
          <li>
          </li>
<li>set(MODULE_PYTHON_RESOURCES</li>
          <li>  ${MODULE_NAME}Lib/SegmentEditorEffect.png</li>
          <li>  )</li>
          <li>
          </li>
<li>#-----------------------------------------------------------------------------</li>
          <li>slicerMacroBuildScriptedModule(</li>
          <li>  NAME ${MODULE_NAME}</li>
          <li>  SCRIPTS ${MODULE_PYTHON_SCRIPTS}</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @rohan_n (2021-07-31 03:03 UTC)

<p>I’m sorry to be having so much trouble with this. This is the first time I’ve submitted an extension and I have no experience using CMake.<br>
If I’m trying to build this extension on Mac, I have latest nightly release of Slicer with location<br>
/Applications/Slicer.app, extension installed in location /Users/rohan_nadkarni/Desktop/Breast_DCEMRI_FTV and I just created the folder /Users/rohan_nadkarni/Desktop/Breast_DCEMRI_FTV-build, what is the correct way to modify this command</p>
<p><code>cmake -DCMAKE_BUILD_TYPE:STRING=Release -DSlicer_DIR:PATH=/path/to/Slicer-Superbuild/Slicer-build ../MyExtension</code></p>
<p>for my setup? Actually, I’m also confused about this part in the link you shared</p>
<p><strong>MaxOSX</strong> : Extension <strong>must be configured</strong> specifying <code>CMAKE_OSX_*</code> variables matching the one used to configure Slicer:</p>
<p>So if there are any additional commands I need to run besides the cmake and make commands, please let me know.</p>
<p>Thanks,<br>
Rohan</p>

---

## Post #10 by @pieper (2021-07-31 17:38 UTC)

<p>Hi <a class="mention" href="/u/rohan_n">@rohan_n</a> -</p>
<p>Yes, the process can be a bit confusing.  These are the scripts I use for building the SlicerDMRI extension on my mac, but they are pretty general purpose for any extension.  I believe your extension is pure python so you don’t need the parts about deployment targets or qt and cli modules but they won’t hurt anything.</p>
<p>First is a cmake-cmd.sh that you only need to run once in the build directory:</p>
<pre><code class="lang-auto"># run this from within build tree

SLICER_BUILD=/opt/s/Slicer-build

cmake \
        -DCMAKE_BUILD_TYPE:STRING=Debug \
        -DSlicer_DIR:PATH=${SLICER_BUILD} \
        -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.15 \
        ../SlicerDMRI
</code></pre>
<p>Then run <code>make</code> to build the extension.</p>
<p>The second is to run-slicer.sh sets all the paths to the extension’s modules:</p>
<pre><code class="lang-auto">#!/bin/zsh

# run this from within build tree

SLICER_BUILD=/opt/s/Slicer-build

LIB_PATH=$(pwd)/inner-build/lib/Slicer-4.13

SDKROOT=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk ${SLICER_BUILD}/Slicer $* \
  --additional-module-paths \
    ${LIB_PATH}/cli-modules ${LIB_PATH}/qt-loadable-modules ${LIB_PATH}/qt-scripted-modules
</code></pre>

---

## Post #11 by @rohan_n (2021-07-31 22:35 UTC)

<p>Thank you. Unfortunately I tried running your first shell script cmake-cmd.sh and got the following error.</p>
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


-- Configuring incomplete, errors occurred!

</code></pre>
<p>I thought at first this error occurred because I don’t have a directory /opt/s/Slicer-build.<br>
But I tried replacing setting SLICER_BUILD=/Applications/Slicer.app and got the same error.<br>
I don’t see SlicerConfig.cmake or slicer-config.cmake anywhere on my computer.</p>

---

## Post #12 by @pieper (2021-07-31 23:11 UTC)

<p>Ah, yes, that’s another important thing: I believe testing the extension building/packaging process locally requires that you have a local version of Slicer built from source.  This is a requirement for C++ based extension but it is a pain for Python extensions.  A consolation is that building from source on mac is fairly painless, but can take a long time depending on your computer.</p>

---

## Post #13 by @rohan_n (2021-07-31 23:41 UTC)

<p>Ok. But going back to the error</p>
<pre><code class="lang-auto">No module named 'Breast_DCEMRI_FTV_plugins2'
</code></pre>
<p>do I have to do anything other than use a text editor to add the type of corrections to the CMakeLists.txt files mentioned in James Butler’s reply? If that’s all I have to do to resolve that error, I won’t bother with building the extension locally for now.</p>

---

## Post #14 by @pieper (2021-08-01 15:10 UTC)

<p>Right, you don’t need to build everything locally to fix the installation issue.  You can even edit the files directly on github in the browser.  It may take a couple days but you can keep an eye on the nightly builds until you get the right formulation.  Basically yes, as <a class="mention" href="/u/jamesobutler">@jamesobutler</a> said it’s just a matter of making sure the non-module code is in the Lib directory and that they are listed for install in the CMakeLists.txt file.</p>

---

## Post #15 by @jamesobutler (2021-08-01 19:26 UTC)

<p>Yes, you can do the type of edits as I suggested and check each day to see if the factory machine built the extension successfully and it load properly. This is a iterative process.</p>
<p>If you don’t have the time to make changes, wait for the next day, etc and need the extension to be available and working properly, then building the extension from source using a Slicer build tree (Slicer built from source) you can make sure the extension is building, installing and loading appropriately. This will let you know for sure that everything is working.</p>

---

## Post #16 by @rohan_n (2021-08-04 18:25 UTC)

<p>I edited the CMakeLists.txt files for both modules on Aug 1 at 2pm pacific time. Feel free to look at the Github again to make sure I did it correctly.<br>
However, the latest nightly build of Slicer doesn’t have my extension at all, and Slicer 4.11.20210226 appears to have the version of my extension from before the edits to the CMakeLists.txt files.</p>
<p>Is there anything that can be done to speed up the process of updating the copy of my extension on extension manager?</p>
<p>Thank you so much,<br>
Rohan</p>

---

## Post #17 by @jamesobutler (2021-08-04 20:10 UTC)

<p>You can review if your extension is having configure/build/test issues on the Slicer CDash dashboard.</p>
<p>CDash results for the Slicer Preview from August 1 to August 4th:<br>
<a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;begin=2021-08-01&amp;end=2021-08-04&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Breast_DCEMRI_FTV" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/index.php?project=SlicerPreview&amp;begin=2021-08-01&amp;end=2021-08-04&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Breast_DCEMRI_FTV</a></p>
<p>CDash results for the latest Slicer Stable from August 1 to August 4th:<br>
<a href="https://slicer.cdash.org/index.php?project=Slicer4&amp;begin=2021-08-01&amp;end=2021-08-04&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Breast_DCEMRI_FTV" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/index.php?project=Slicer4&amp;begin=2021-08-01&amp;end=2021-08-04&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Breast_DCEMRI_FTV</a></p>
<p>It shows starting on August 2nd, the extension began to fail to configure likely due to the changes you made on August 1st.  The extensions are built each night. Any updates you make in your repo will be used for the next nightly build and doesn’t require any updates to the Slicer ExtensionsIndex repo as <a href="https://github.com/Slicer/ExtensionsIndex/blob/1a5117c6abdb35f9ee4d04bd53c325e2e9ebfd6d/Breast_DCEMRI_FTV.s4ext#L10" rel="noopener nofollow ugc">you specified</a> to use the <code>master</code> branch for your repo. Therefore it will use the latest of that branch.</p>
<p>Building the extension locally (requires Slicer built from source) would help you know if your changes resolve the issue with it being available through the Slicer ExtensionsManager. Otherwise you will have to make updates and wait to review the result on the Slicer dashboard from each nightly build. This was mentioned in</p><aside class="quote quote-modified" data-post="15" data-topic="18955">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/help-submitting-extension-breast-dce-mri-ftv/18955/15">Help submitting extension Breast DCE-MRI FTV</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Yes, you can do the type of edits as I suggested and check each day to see if the factory machine built the extension successfully and it load properly. This is a iterative process. 
If you don’t have the time to make changes, wait for the next day, etc and need the extension to be available and working properly, then building the extension from source using a Slicer build tree (Slicer built from source) you can make sure the extension is building, installing and loading appropriately. This will…
  </blockquote>
</aside>


---

## Post #18 by @jamesobutler (2021-08-04 23:23 UTC)

<p>See <a href="https://github.com/rnadkarni2/SlicerBreast_DCEMRI_FTV/pull/2" class="inline-onebox" rel="noopener nofollow ugc">Extension build improvements by jamesobutler · Pull Request #2 · rnadkarni2/SlicerBreast_DCEMRI_FTV · GitHub</a> to help out with building this extension.</p>

---

## Post #19 by @rohan_n (2021-08-06 22:22 UTC)

<p>The version built last night works fine when I download from Extension Manager.<br>
Thank you <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/jamesobutler">@jamesobutler</a> for your help!</p>

---

## Post #20 by @gekehe (2022-06-06 12:23 UTC)

<p>Hi <a class="mention" href="/u/rohan_n">@rohan_n</a> , Thanks for your great work by sharing and submitting the extension of Breast DCE-MRI FTV.  I’m interested in this extension and hope that I can use it to do some research about breast cancer.  However, errors occured when I tried to install it. It seems that Breast_DCEMRI_FTV is not compatible to the neweast version of 3D slicer (more detailed infomation: <a href="https://discourse.slicer.org/t/error-with-installing-extension-breast-dcemri-ftv/23569" class="inline-onebox">error with installing extension Breast_DCEMRI_FTV</a>). I checked the manual of Breast_DCEMRI_FTV and found a picture in the manual which showed you used 3D slicer version 4.11.20200930. But no usable extension of Breast_DCEMRI_FTV can be found for this older version of 3D slicer on the extension manager, nor on the official website.  Would you please help me and tell me where can I find the extension of Breast_DCEMRI_FTV compatible for 3D slicer version 4.11.20200930, or would you please help me to fix the problem. I really need to install the extension and start to use it as soon as posible.<br>
Thanks very much!</p>

---

## Post #21 by @rohan_n (2022-06-06 22:32 UTC)

<p><a class="mention" href="/u/gekehe">@gekehe</a> I’m sorry I didn’t hear about your trouble earlier. Definitely tag me in a post if you have further questions.</p>
<p>As far as I can tell from the post you sent a link to, Breast_DCEMRI_FTV did install correctly and you are getting an error because the DICOMs in the directory you selected are compressed. If they have the extension .DCM.gz or .dcm.gz, you will need to use the command line tool gunzip so that the DICOMs have extension .DCM or .dcm instead. Also, you want to select the directory containing the DICOMs, rather than the DICOM file itself.</p>
<p>I hope this helps, but let me know if you need more from me. It may help if you send screenshots.</p>
<p>Rohan</p>

---

## Post #22 by @rohan_n (2024-11-09 16:38 UTC)

<p>Hi, it has been a while since I submitted this extension and I don’t remember much about the process. But I just transferred ownership of this extension from user rnadkarni2 to user radiology-research, and I want to Slicer extension index to point to the updated URL.</p>
<p>To do this, do I simply edit this file in my fork</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/blob/main/Breast_DCEMRI_FTV.json">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/blob/main/Breast_DCEMRI_FTV.json" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/main/Breast_DCEMRI_FTV.json" target="_blank" rel="noopener nofollow ugc">Slicer/ExtensionsIndex/blob/main/Breast_DCEMRI_FTV.json</a></h4>


      <pre><code class="lang-json">{
  "$schema": "https://raw.githubusercontent.com/Slicer/Slicer/main/Schemas/slicer-extension-catalog-entry-schema-v1.0.0.json#",
  "build_dependencies": [],
  "build_subdirectory": ".",
  "category": "FTV Segmentation",
  "scm_revision": "master",
  "scm_url": "https://github.com/rnadkarni2/SlicerBreast_DCEMRI_FTV"
}
</code></pre>




  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
and send a new pull request? Or is there anything else I need to do?</p>
<p>Thanks,<br>
Rohan</p>

---
