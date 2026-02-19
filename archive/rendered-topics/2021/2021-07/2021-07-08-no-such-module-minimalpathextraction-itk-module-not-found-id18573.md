---
topic_id: 18573
title: "No Such Module Minimalpathextraction Itk Module Not Found"
date: 2021-07-08
url: https://discourse.slicer.org/t/18573
---

# No such module "MinimalPathExtraction" ITK module not found

**Topic ID**: 18573
**Date**: 2021-07-08
**URL**: https://discourse.slicer.org/t/no-such-module-minimalpathextraction-itk-module-not-found/18573

---

## Post #1 by @Mahesh_Timmanagoudar (2021-07-08 04:06 UTC)

<p>Hello,</p>
<p>I am building TubeTK with latest slicer repository.</p>
<p>TubeTK I have cloned from the following link.</p>
<p><a href="https://itktubetk/" rel="noopener nofollow ugc">https://github.com/InsightSoftwareConsortium/ITKTubeTK</a></p>
<p>While I am building slicer along with TubeTK I got the below error.</p>
<p>– Configuring extension directory: TubeTK<br>
CMake Error at D:/W6/S-rel/S-bld/ITK/CMake/ITKModuleAPI.cmake:78 (message):<br>
No such module: “MinimalPathExtraction”<br>
Call Stack (most recent call first):<br>
D:/W6/S-rel/S-bld/ITK/CMake/ITKModuleAPI.cmake:31 (itk_module_load)<br>
D:/W6/S-rel/S-bld/ITK/CMake/ITKModuleAPI.cmake:129 (_itk_module_config_recurse)<br>
D:/W6/S-rel/S-bld/ITK-build/ITKConfig.cmake:86 (itk_module_config)<br>
D:/W6/S-rel/S-bld/TubeTK/CMakeLists.txt:159 (find_package)<br>
– Configuring incomplete, errors occurred!</p>
<p>I have tried by setting below values in CMake <code>-DSlicer_DIR:PATH=%SLICER_BIN_DIR_DBG_X64% -DTubeTK_BUILD_SLICER_EXTENSION:BOOL=ON</code> .</p>
<p>As per below reference but no luck.</p><aside class="quote quote-modified" data-post="1" data-topic="858">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leochan2009/48/519_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/tubetk-build-with-slicer/858">TubeTK build with Slicer</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi, 
Does anyone build TubeTk successfully with the latest slicer? 
i receive this kind of error message 
Make Error at /usr/local/Cellar/cmake/3.9.0/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:137 (message): 
Could NOT find JsonCpp (missing: JsonCpp_LIBRARIES JsonCpp_INCLUDE_DIRS) 
Call Stack (most recent call first): 
/usr/local/Cellar/cmake/3.9.0/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:377 (_FPHSA_FAILURE_MESSAGE) 
/Users/longquanchen/Desktop/Github/Slicer-build/Sl…
  </blockquote>
</aside>

<p>Please let me know about it, How can i build TubeTK with slicer.</p>

---

## Post #2 by @lassoan (2021-07-12 13:14 UTC)

<p>The error message suggests that you need to enable <code>MinimalPathExtraction</code> ITK remote module enabled when you configure the ITK build. You can reconfigure your ITK build tree manually in CMake, but it would be nice if this ITK remote module could be built additionally when the extension is built. If you are not sure how then you can write to the <a href="https://discourse.itk.org/">ITK forum</a>.</p>

---
