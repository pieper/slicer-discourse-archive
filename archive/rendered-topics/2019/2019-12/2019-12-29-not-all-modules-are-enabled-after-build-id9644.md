# Not all modules are enabled after build

**Topic ID**: 9644
**Date**: 2019-12-29
**URL**: https://discourse.slicer.org/t/not-all-modules-are-enabled-after-build/9644

---

## Post #1 by @harajyoti_das (2019-12-29 15:23 UTC)

<p><strong>Hi, I have build the 3d slicer following the instructions given in the document. I am getting the following error:</strong><br>
CUSTOMBUILD : error : Target (for copy_if_different command) “C:/D/D/Slicer-build/lib/Slicer-4.11/cli-modules/Debug” is not a directory. [C:\D\D\Slicer-build\Base\QTCLI\Testing\InstallPyCLITest4.vcxproj]</p>
<p><strong>This is what I get when I launch the slicer.exe</strong><br>
qt.network.ssl: QSslSocket: cannot resolve SSL_set_alpn_protos<br>
qt.network.ssl: QSslSocket: cannot resolve SSL_CTX_set_alpn_select_cb<br>
qt.network.ssl: QSslSocket: cannot resolve SSL_get0_alpn_selected<br>
When loading module  “DICOM” , the dependency “SubjectHierarchy” failed to be loaded.<br>
When loading module  “DICOM” , the dependency “SubjectHierarchy” failed to be loaded.<br>
When loading module  “DICOMPatcher” , the dependency “DICOM” failed to be loaded.<br>
When loading module  “MarkupsWidgetsSelfTest” , the dependency “Markups” failed to be loaded.<br>
When loading module  “MultiVolumeImporter” , the dependency “MultiVolumeExplorer” failed to be loaded.<br>
When loading module  “NeurosurgicalPlanningTutorialMarkupsSelfTest” , the dependency “Segmentations” failed to be loaded.<br>
When loading module  “PlotsSelfTest” , the dependency “Plots” failed to be loaded.<br>
When loading module  “SegmentEditor” , the dependency “Segmentations” failed to be loaded.<br>
When loading module  “SegmentStatistics” , the dependency “SubjectHierarchy” failed to be loaded.<br>
When loading module  “SubjectHierarchyCorePluginsSelfTest” , the dependency “SubjectHierarchy” failed to be loaded.<br>
When loading module  “SubjectHierarchyGenericSelfTest” , the dependency “SubjectHierarchy” failed to be loaded.<br>
When loading module  “TablesSelfTest” , the dependency “Tables” failed to be loaded.<br>
SliceAnnotations: Disable features relying on vtkPVScalarBarActor</p>
<p>These are the modules enabled. Please see the snapshot:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2aad80e0c281a8c91cafc387b7bf7449388a12b7.png" data-download-href="/uploads/short-url/65xMyoJKYu8CgYgSdQPGWfNxIXl.png?dl=1" title="3dslicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2aad80e0c281a8c91cafc387b7bf7449388a12b7_2_690x284.png" alt="3dslicer" data-base62-sha1="65xMyoJKYu8CgYgSdQPGWfNxIXl" width="690" height="284" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2aad80e0c281a8c91cafc387b7bf7449388a12b7_2_690x284.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2aad80e0c281a8c91cafc387b7bf7449388a12b7_2_1035x426.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2aad80e0c281a8c91cafc387b7bf7449388a12b7.png 2x" data-dominant-color="A0A0A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dslicer</span><span class="informations">1247×514 46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-12-29 19:19 UTC)

<p>There seems to be an error during your Slicer build. The build error you copied is probably not the first one but a consequence of previous errors. It would be important to identify the very first error occurred during build.</p>

---

## Post #3 by @harajyoti_das (2019-12-30 12:25 UTC)

<p>Thanks for your reply. But there is only one error. There is no cli_modules folders. Can you tell me which project creates the cli_modules folder?</p>

---

## Post #4 by @lassoan (2019-12-30 16:39 UTC)

<p>I don’t think cli_modules are created by any projects. CLI modules are built in <code>(build-dir)\Slicer-build\lib\Slicer-4.11\cli-modules</code>.</p>

---

## Post #5 by @harajyoti_das (2019-12-30 19:21 UTC)

<p>Do you mean that these files should be present when visual studio solution files are generated using cmake-gui?  If not then it should get downloaded while building? What could be the issue? Following same steps, I am able to build in an another laptop. The only difference is that one got professional visual studio and other got enterprise(not working here). I have exactly followed the steps given in the documentation link.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f9c3da9f483ae60fc0536621c1a9c458dbfcb22.png" data-download-href="/uploads/short-url/2e5UcUZ19Ww7fWoXcV7u6qfqHJM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f9c3da9f483ae60fc0536621c1a9c458dbfcb22.png" alt="image" data-base62-sha1="2e5UcUZ19Ww7fWoXcV7u6qfqHJM" width="690" height="44" data-dominant-color="F3F3F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1160×75 3.71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d9cb1d873daff5029f432aa632ba681bac6659e.png" alt="image" data-base62-sha1="1WpVhMHHL7OTevJkXXRP4tX9Hrw" width="675" height="210"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cee28f40388d93b1157389c74ed345bf235bfae.png" data-download-href="/uploads/short-url/8H0U1v8geB5ug8NmD3js4HClgNU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cee28f40388d93b1157389c74ed345bf235bfae.png" alt="image" data-base62-sha1="8H0U1v8geB5ug8NmD3js4HClgNU" width="366" height="500" data-dominant-color="373739"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">480×655 18 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56abdfd021d616cd20a57b85dccaee53bde45685.png" data-download-href="/uploads/short-url/cmJiGvZnuBTQZcXWmynhYhG9QB7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56abdfd021d616cd20a57b85dccaee53bde45685.png" alt="image" data-base62-sha1="cmJiGvZnuBTQZcXWmynhYhG9QB7" width="360" height="500" data-dominant-color="373739"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">474×657 20 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0869deb7d08d635f98c44f5d07268d0d065a6715.png" data-download-href="/uploads/short-url/1cqE03uPegWtZeT7oq0n26y2ka9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0869deb7d08d635f98c44f5d07268d0d065a6715.png" alt="image" data-base62-sha1="1cqE03uPegWtZeT7oq0n26y2ka9" width="690" height="151" data-dominant-color="F2AEAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1377×303 17.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @jamesobutler (2019-12-30 19:39 UTC)

<aside class="quote no-group" data-username="harajyoti_das" data-post="1" data-topic="9644">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/harajyoti_das/48/5529_2.png" class="avatar"> harajyoti_das:</div>
<blockquote>
<p>CUSTOMBUILD : error : Target (for copy_if_different command) “C:/D/D/Slicer-build/lib/Slicer-4.11/cli-modules/Debug” is not a directory. [C:\D\D\Slicer-build\Base\QTCLI\Testing\InstallPyCLITest4.vcxproj]</p>
</blockquote>
</aside>
<p>I actually ran into this exact same issue just recently as part of some testing for a PR. I had a clean build building ITK 5.1rc01 and then it ultimately failed at SimpleITK, as I expected, so I cleaned out all SimpleITK build directories and files and rebuilt using a newer SimpleITK version and it succeeded but then I noticed it kept getting stuck at this error in the Slicer build project.</p>
<p>As a workaround I just manually created the “ c:/D/D/Slicer-build/lib/Slicer-4.11/cli-modules/$BUILD_TYPE” directory and then ran the build process again and it completed the Slicer project successfully.</p>
<p>I’m unsure if the build error was originally because my SimpleITK project had failed in a prior run or something to do with the parallel build process as I specify 12 threads to use. I didn’t look much further into it as manually creating the missing directory fixed my issue.</p>

---

## Post #7 by @lassoan (2019-12-30 20:14 UTC)

<p>Partially cleaned out build trees and parallel builds are not guaranteed to work. The nightly dashboard shows that clean builds are successful on Windows and Mac (there is a <a href="https://discourse.slicer.org/t/import-sqlite-issue-in-slicelet/5691/20">build error on Linux due to a recent attempt to add sqlite3 to Python</a>, but that should not affect Windows).</p>
<p>Visual Studio Edition should not matter.</p>
<p>What CMake version do you use?<br>
Do you have any third-party antivirus software installed?</p>

---

## Post #8 by @harajyoti_das (2019-12-31 03:33 UTC)

<p>CMake Version 3.16.2. No third party antivirus software installed.</p>
<p>I again build it and got the same error. Here is the link to the build log.</p>
<p><a href="https://file.io/yXXICq" class="onebox" target="_blank" rel="nofollow noopener">https://file.io/yXXICq</a></p>
<p>Please check it and let me know if you get any clue.</p>

---

## Post #9 by @harajyoti_das (2019-12-31 03:34 UTC)

<p>I will try this tonight my time and let you know. Thanks for your advice.</p>
<blockquote>
<p>As a workaround I just manually created the “ c:/D/D/Slicer-build/lib/Slicer-4.11/cli-modules/$BUILD_TYPE” directory and then ran the build process again and it completed the Slicer project successfully.</p>
</blockquote>

---

## Post #10 by @lassoan (2019-12-31 03:39 UTC)

<aside class="quote no-group quote-modified" data-username="harajyoti_das" data-post="8" data-topic="9644">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/harajyoti_das/48/5529_2.png" class="avatar"> harajyoti_das:</div>
<blockquote>
<p>I again build it and got the same error. Here is the link to the build log.</p>
<p><a href="https://file.io/yXXICq" class="inline-onebox">Deleted</a></p>
</blockquote>
</aside>
<p>The page gives “404 Page not found” error.</p>
<aside class="quote no-group" data-username="harajyoti_das" data-post="8" data-topic="9644">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/harajyoti_das/48/5529_2.png" class="avatar"> harajyoti_das:</div>
<blockquote>
<p>CMake Version 3.16.2.</p>
</blockquote>
</aside>
<p>Bugs are quite often introduced in new CMake releases. You might try an earlier version to see if that works (I’ve built Slicer from scratch successfully, using CMake 3.14.3).</p>

---

## Post #11 by @harajyoti_das (2019-12-31 04:13 UTC)

<p>check this link.</p>
<p><a href="https://file.io/v67Kik" class="onebox" target="_blank" rel="nofollow noopener">https://file.io/v67Kik</a></p>

---

## Post #12 by @lassoan (2019-12-31 04:25 UTC)

<p>Same issue:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2785a3c647bde6ba4d4327bf724020a1b4a566e.png" data-download-href="/uploads/short-url/rKmtXHWtLBO6brKh6vKEEFg8zKu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2785a3c647bde6ba4d4327bf724020a1b4a566e_2_690x335.png" alt="image" data-base62-sha1="rKmtXHWtLBO6brKh6vKEEFg8zKu" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2785a3c647bde6ba4d4327bf724020a1b4a566e_2_690x335.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2785a3c647bde6ba4d4327bf724020a1b4a566e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2785a3c647bde6ba4d4327bf724020a1b4a566e.png 2x" data-dominant-color="7EB4E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">875×426 68.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @harajyoti_das (2019-12-31 05:49 UTC)

<p>This should work</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/s/1btpsrhh0o6e9zl/build_output.txt?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-txt-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/1btpsrhh0o6e9zl/build_output.txt?dl=0" target="_blank" rel="nofollow noopener">build_output.txt</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #14 by @jamesobutler (2019-12-31 12:02 UTC)

<p><a class="mention" href="/u/harajyoti_das">@harajyoti_das</a> Did you manually try creating the missing directory as I suggested? Did you do a regular build action of the Slicer project after this or did you do any cleaning actions? The error in your log indicates the directory isn’t present.</p>

---

## Post #15 by @lassoan (2019-12-31 14:51 UTC)

<p>I’ve checked the log and it seems you have enabled parallel build:</p>
<p>Your failed build logs (note how building of files from project 22 and 11 are interleaved):</p>
<pre><code class="lang-auto">22&gt;    archive_write_open_file.c
22&gt;    archive_write_open_filename.c
22&gt;    archive_write_open_memory.c
11&gt;    dcvrod.cc
22&gt;    archive_write_add_filter.c
22&gt;    Generating Code...
11&gt;    dcvrof.cc
22&gt;    Compiling...
22&gt;    archive_write_add_filter_b64encode.c
22&gt;    archive_write_add_filter_by_name.c
11&gt;    dcvrol.cc
</code></pre>
<p>My successful build logs (not that project 11 are not built while building project 22):</p>
<pre><code class="lang-auto">    archive_write_open_file.c
    archive_write_open_filename.c
    archive_write_open_memory.c
    archive_write_add_filter.c
    Generating Code...
    Compiling...
    archive_write_add_filter_b64encode.c
    archive_write_add_filter_by_name.c
</code></pre>
<p>In parallel builds, build order projects can randomly change (it is only guaranteed that a project build starts after all dependencies are built). This seems to cause an error because a copy is attempted to be copied into a folder that does not exist yet.</p>
<p>Have you intentionally enabled parallel build?<br>
Could you provide the content of your top-level CMakeCache.txt file?</p>

---

## Post #16 by @harajyoti_das (2020-01-01 10:31 UTC)

<p>No, I have not intentionally enabled parallel build.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/745004fe966289d54840cddd4e1920df2797de1c.png" data-download-href="/uploads/short-url/gAWPjdHZ3MRPE1zDuEhtiGVX86g.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/745004fe966289d54840cddd4e1920df2797de1c.png" alt="image" data-base62-sha1="gAWPjdHZ3MRPE1zDuEhtiGVX86g" width="690" height="405" data-dominant-color="EAECEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">758×445 18.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Shall I set this to 1?</p>
<p>Please see the CMakeCache.txt file for your reference.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/s5wvun1gngnpoo8/CMakeCache.txt?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/s/s5wvun1gngnpoo8/CMakeCache.txt?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img width="160" height="160" src="https://www.dropbox.com/static/metaserver/static/images/opengraph/opengraph-content-icon-file-text-landscape.png" class="thumbnail onebox-avatar">

<h3><a href="https://www.dropbox.com/s/s5wvun1gngnpoo8/CMakeCache.txt?dl=0" target="_blank" rel="noopener nofollow ugc">CMakeCache.txt</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #17 by @harajyoti_das (2020-01-01 10:48 UTC)

<p>I created the missing directory and built it but I got lot of linking errors after that. At present I don’t have that build log. Did you rebuild the solution after creating missing folder or just simply build it?</p>
<p>The shared log is of a fresh build.</p>

---

## Post #18 by @lassoan (2020-01-02 00:04 UTC)

<p>If the issue is indeed parallel building then restarting the build several times should eventually lead to a successful build.</p>

---

## Post #19 by @harajyoti_das (2020-01-02 03:16 UTC)

<p>Thanks a lot Lassoan, The build is successful now after I disabled the parallel build. I think this should be added in the documentation.</p>

---

## Post #20 by @lassoan (2020-01-02 04:56 UTC)

<p>Which exact option did you change (where was it, what was the original value and what did you set it to)?</p>

---

## Post #21 by @harajyoti_das (2020-01-02 05:37 UTC)

<p>I enabled the /MP flag in CMake and set the num_processors to 1.<br>
default the flag is unchecked and num of processors for my machine was 8(= no of cores)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01136b2d212c464387dd25835ec69deccb0c3d66.png" alt="image" data-base62-sha1="9w54fMVahu4MjQV2Nah0AGvYZ8" width="357" height="36"></p>
<p>I set the number of parallel projects build to 1 (default is 8 for my machine as I have 8 core) This is under Tools-&gt; option<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc36c0c5cd802e91a2dec057876b9bfabb3a5c35.png" data-download-href="/uploads/short-url/qR14tHZQ3zsuTpXELYv59wiSzXL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc36c0c5cd802e91a2dec057876b9bfabb3a5c35.png" alt="image" data-base62-sha1="qR14tHZQ3zsuTpXELYv59wiSzXL" width="690" height="394" data-dominant-color="E6E6E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">808×462 18.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #22 by @cpinter (2020-01-09 07:43 UTC)

<p>For reference, <a class="mention" href="/u/lassoan">@lassoan</a> committed a fix that creates the missing directory just before using it, so parallel build should work now as well.</p>
<aside class="quote" data-post="7" data-topic="9738">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/build-error-on-windows-related-to-cli-build-directory/9738/7">Build error on Windows related to CLI build directory</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Submitted a fix for this build error: <a href="https://github.com/Slicer/Slicer/commit/f59653b8b7aa527ceeaacfa3296b009064619bf7">https://github.com/Slicer/Slicer/commit/f59653b8b7aa527ceeaacfa3296b009064619bf7</a> 
It would be still nice to find out why CMake behavior is changed but right now I cannot spend more time with this investigation.
  </blockquote>
</aside>


---
