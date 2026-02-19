---
topic_id: 17457
title: "Multiple Errors About Simpleitk Libarchive Python When I Bui"
date: 2021-05-04
url: https://discourse.slicer.org/t/17457
---

# Multiple errors about SimpleITK, LibArchive, python when I build Slicer

**Topic ID**: 17457
**Date**: 2021-05-04
**URL**: https://discourse.slicer.org/t/multiple-errors-about-simpleitk-libarchive-python-when-i-build-slicer/17457

---

## Post #1 by @moonchi (2021-05-04 20:55 UTC)

<p>I used<br>
CMAKE 3.19.8<br>
Visual Studio 2019 x64 tool v142<br>
And refer to</p><aside class="quote quote-modified" data-post="1" data-topic="1024">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschwier/48/394_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/building-cli-extension-copies-to-wrong-output-directories-cmake-issue/1024">Building CLI Extension copies to wrong output directories (cmake issue)</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I hope I might find some help here. I recently started working on the PkModeling extension an I am trying to get it to build on various continuous integration platforms (Appveyor for Win and Travis CI for Linux and Mac). 
<a href="https://github.com/michaelschwier/PkModeling/tree/CI" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/michaelschwier/PkModeling/tree/CI</a> 
I got the build working on Appveyor but it copies some of the generated files to the wrong output. So the expected output would be “[pkmodeling-build]/bin/Release” (expected files there are: PkModeling.exe, PkModelingLib.dll…
  </blockquote>
</aside>
<p>
I first installed and compiled<br>
ITK DCMTK SlicerExecutionModel ZLIB<br>
And join them in CMAKE-GUI<br>
The following is my CMAKE interface<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0d1ec50177b8c1077e853480f80ed86e30056ef.png" data-download-href="/uploads/short-url/w4QI7alINUn02lJ6WkfBstM5Sqj.png?dl=1" title="20210505CMAKE1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0d1ec50177b8c1077e853480f80ed86e30056ef_2_690x370.png" alt="20210505CMAKE1" data-base62-sha1="w4QI7alINUn02lJ6WkfBstM5Sqj" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0d1ec50177b8c1077e853480f80ed86e30056ef_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0d1ec50177b8c1077e853480f80ed86e30056ef_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0d1ec50177b8c1077e853480f80ed86e30056ef_2_1380x740.png 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20210505CMAKE1</span><span class="informations">1920×1030 61 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa280ee81f8c5652f1cd982ae83425cf871d92fa.png" data-download-href="/uploads/short-url/ohgZEemnT65765aBu3QuyDEOxVo.png?dl=1" title="20210505CMAKE2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa280ee81f8c5652f1cd982ae83425cf871d92fa_2_690x370.png" alt="20210505CMAKE2" data-base62-sha1="ohgZEemnT65765aBu3QuyDEOxVo" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa280ee81f8c5652f1cd982ae83425cf871d92fa_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa280ee81f8c5652f1cd982ae83425cf871d92fa_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa280ee81f8c5652f1cd982ae83425cf871d92fa_2_1380x740.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20210505CMAKE2</span><span class="informations">1920×1031 50.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f43b25cd3ab84f379664bef8aa382f60f78bd14a.png" data-download-href="/uploads/short-url/yQze11rSFIuFX3r3eBfsdz5Nium.png?dl=1" title="20210505CMAKE3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43b25cd3ab84f379664bef8aa382f60f78bd14a_2_690x370.png" alt="20210505CMAKE3" data-base62-sha1="yQze11rSFIuFX3r3eBfsdz5Nium" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43b25cd3ab84f379664bef8aa382f60f78bd14a_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43b25cd3ab84f379664bef8aa382f60f78bd14a_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43b25cd3ab84f379664bef8aa382f60f78bd14a_2_1380x740.png 2x" data-dominant-color="F3F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20210505CMAKE3</span><span class="informations">1920×1031 45.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I used the Release mode to build<br>
Then here is my error list<br>
<a href="https://drive.google.com/file/d/1tK6oYtSseKDhCYNAM-koLDZsOAcAd8_U/view?usp=sharing" rel="noopener nofollow ugc">errorlist-Release</a><br>
<a href="https://drive.google.com/file/d/1u_3nxnkU3-96-UK47vJ-g9H63gUOGML3/view?usp=sharing" rel="noopener nofollow ugc">errorlog-Release</a><br>
I want to know what I should do to successfully build Slicer<br>
Thank you for your patience to read this</p>

---

## Post #2 by @jamesobutler (2021-05-04 23:21 UTC)

<p>You previously posted on the following thread. Did the solution provided there solve the issue?</p><aside class="quote" data-post="6" data-topic="15674">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/build-slicer-failed-on-win10/15674/6">Build Slicer failed on win10</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Probably the issue is that your system code page is set to 950 (Traditional Chinese) and c:\S4R\LibArchive\libarchive\archive_read_support_format_rar5.c contains characters that cannot be interpreted in this code page. 
The simplest is to remove the offending characters (remove entire line 74, it is just a comment): 
 * "Rar!→•☺·\x00"

If you will keep running into similar errors then you may consider switching to Latin1 code page for the build.
  </blockquote>
</aside>

<p>I do see in one of the logs you posted that it warns the following:</p>
<blockquote>
<p>warning C4819: The file contains a character that cannot be represented in the current code page (950)</p>
</blockquote>

---

## Post #3 by @moonchi (2021-05-04 23:56 UTC)

<p>Sorry this is my fault. I emptied the old folder before this construction, which caused the same error to reappear. I have fixed it, thank you<br>
This is the file I rebuilt, and the error is reduced to 9<br>
Below is the new list<br>
<a href="https://drive.google.com/file/d/1jK9qMOc32kfXCP8VOraWFBdbWam2iHSG/view?usp=sharing" rel="noopener nofollow ugc">errorlist-Release</a><br>
<a href="https://drive.google.com/file/d/1nvKUOFiUDm9kjYgoKuq-m1jeJAkOEAHH/view?usp=sharing" rel="noopener nofollow ugc">errorlog-Release</a></p>

---

## Post #4 by @lassoan (2021-05-07 13:41 UTC)

<p>Most probably you have run into this issue:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5498" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5498" target="_blank" rel="noopener">Slicer build error with VTK9 in debug mode due to SimpleITK Python configuration problem</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-01" data-time="16:01:57" data-timezone="UTC">04:01PM - 01 Mar 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">domain:vtk9</span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When building latest master version on Windows, using Visual Studio, in debug mo<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">de, then build fails with this error:

```
  -- Detecting CXX compiler ABI info - done
  -- Detecting CXX compile features
  -- Detecting CXX compile features - done
  CMake Error at C:/Program Files/CMake/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:146 (message):
    Could NOT find Python3 (missing: Python3_EXECUTABLE Interpreter) (found
    suitable version "3.7", minimum required is "3.6")
  Call Stack (most recent call first):
    C:/Program Files/CMake/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:393 (_FPHSA_FAILURE_MESSAGE)
    C:/D/S4D/VTK-build/lib/cmake/vtk-9.0/patches/3.18/FindPython/Support.cmake:2578 (find_package_handle_standard_args)
    C:/D/S4D/VTK-build/lib/cmake/vtk-9.0/patches/3.18/FindPython3.cmake:348 (include)
    C:/D/S4D/VTK-build/lib/cmake/vtk-9.0/VTK-vtk-module-find-packages.cmake:303 (find_package)
    C:/D/S4D/VTK-build/lib/cmake/vtk-9.0/vtk-config.cmake:138 (include)
    C:/D/S4D/VTK-build/vtk-config.cmake:1 (include)
    C:/D/S4D/ITK-build/lib/cmake/ITK-5.1/Modules/ITKVtkGlue.cmake:30 (find_package)
    C:/D/S4D/ITK/CMake/ITKModuleAPI.cmake:76 (include)
    C:/D/S4D/ITK/CMake/ITKModuleAPI.cmake:31 (itk_module_load)
    C:/D/S4D/ITK/CMake/ITKModuleAPI.cmake:129 (_itk_module_config_recurse)
    C:/D/S4D/ITK-build/ITKConfig.cmake:77 (itk_module_config)
    SuperBuild.cmake:386 (find_package)
    CMakeLists.txt:38 (include)


  -- Configuring incomplete, errors occurred!
  See also "C:/D/S4D/SimpleITK-build/CMakeFiles/CMakeOutput.log".
  See also "C:/D/S4D/SimpleITK-build/CMakeFiles/CMakeError.log".
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(238
,5): error MSB8066: Custom build for 'C:\D\S4D\CMakeFiles\76a3bb6e84cfb300f8ba64bbde6291e1\SimpleITK-mkdir.rule;C:\D\S4
D\CMakeFiles\76a3bb6e84cfb300f8ba64bbde6291e1\SimpleITK-download.rule;C:\D\S4D\CMakeFiles\76a3bb6e84cfb300f8ba64bbde629
1e1\SimpleITK-update.rule;C:\D\S4D\CMakeFiles\76a3bb6e84cfb300f8ba64bbde6291e1\SimpleITK-patch.rule;C:\D\S4D\CMakeFiles
\76a3bb6e84cfb300f8ba64bbde6291e1\SimpleITK-configure.rule;C:\D\S4D\CMakeFiles\76a3bb6e84cfb300f8ba64bbde6291e1\SimpleI
TK-build.rule;C:\D\S4D\CMakeFiles\76a3bb6e84cfb300f8ba64bbde6291e1\SimpleITK-install.rule;C:\D\S4D\CMakeFiles\55773c0e5
810be009a8f38bd18c05739\SimpleITK-complete.rule;C:\D\S4D\CMakeFiles\f5993a3ec64cf58c5707908b20f354e5\SimpleITK.rule;C:\
D\S4\CMakeLists.txt' exited with code 1. [C:\D\S4D\SimpleITK.vcxproj]
```

I don't know if it is related, but SimpleITK CMake cache (c:\D\S4D\SimpleITK-build\CMakeCache.txt) picks up pieces of anaconda, which is strange because my environment variables are clean (there is absolutely no mention of anaconda or python in any of the variables):

```
//Path to a program.
_Python3_CONFIG:INTERNAL=_Python3_CONFIG-NOTFOUND
_Python3_DEVELOPMENT_EMBED_SIGNATURE:INTERNAL=0993e8f7af6d2f88f03f3f71fd289925
_Python3_DEVELOPMENT_MODULE_SIGNATURE:INTERNAL=0993e8f7af6d2f88f03f3f71fd289925
//Path to a program.
_Python3_EXECUTABLE:INTERNAL=_Python3_EXECUTABLE-NOTFOUND
//Path to a file.
_Python3_INCLUDE_DIR:INTERNAL=C:/Users/andra/anaconda3/include
//Path to a library.
_Python3_LIBRARY_DEBUG:INTERNAL=_Python3_LIBRARY_DEBUG-NOTFOUND
//Path to a library.
_Python3_LIBRARY_RELEASE:INTERNAL=C:/Users/andra/anaconda3/libs/python37.lib
//Path to a library.
_Python3_RUNTIME_LIBRARY_RELEASE:INTERNAL=C:/Users/andra/anaconda3/python37.dll
//Result of TRY_COMPILE
project_compiles:INTERNAL=FALSE
```

You can find the full logs here: https://1drv.ms/u/s!Arm_AFxB9yqHxaN2aILYudYPjN5xdA?e=Fhpgcf</span></p>
  </div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>A workaround is to temporarily rename your other Python installation folder (anaconda, etc.). You can rename it back to the original name after Slicer build is complete.</p>

---

## Post #5 by @moonchi (2021-05-08 12:36 UTC)

<p>I tried the method you recommended, and successfully built the Release and Debug of Slicer. Thank you for your answers!</p>

---
