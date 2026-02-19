---
topic_id: 13310
title: "Libarchive Build Errors"
date: 2020-09-02
url: https://discourse.slicer.org/t/13310
---

# LibArchive build errors

**Topic ID**: 13310
**Date**: 2020-09-02
**URL**: https://discourse.slicer.org/t/libarchive-build-errors/13310

---

## Post #1 by @smrolfe (2020-09-02 22:30 UTC)

<p>I’m trying to compile the most recent preview version of Slicer on Windows 10. In debug mode, the LibArchive project is failing with the errors below. Does anyone have an idea what might cause this? Release mode is building without these errors.</p>
<pre><code>Error	C4061	enumerator 'WT_NONE' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_INFO' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_META' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_REQ' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_RVIS' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_CONV' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_CONT' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'LAST_WT' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_NONE' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'WT_INFO' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'WT_META' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'WT_REQ' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'WT_RVIS' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'WT_CONV' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'WT_CONT' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'LAST_WT' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'ENCRYPTION_NONE' in switch of enum 'encryption' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_write_set_format_zip.c	588	
Error	C4061	enumerator 'ENCRYPTION_NONE' in switch of enum 'encryption' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_write_set_format_zip.c	714	
Error	C4061	enumerator 'ENCRYPTION_NONE' in switch of enum 'encryption' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_write_set_format_zip.c	766	
Error	C4061	enumerator 'ENCRYPTION_NONE' in switch of enum 'encryption' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_write_set_format_zip.c	1033	
Error	C4061	enumerator 'COMPRESSION_UNSPECIFIED' in switch of enum 'compression' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_write_set_format_zip.c	1123	
Error	C4061	enumerator 'WT_NONE' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_INFO' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_META' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_REQ' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_RVIS' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_CONV' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_CONT' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'LAST_WT' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	344	
Error	C4061	enumerator 'WT_NONE' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'WT_INFO' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'WT_META' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'WT_REQ' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'WT_RVIS' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'WT_CONV' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'WT_CONT' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'LAST_WT' in switch of enum 'warc_type_t' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_read_support_format_warc.c	368	
Error	C4061	enumerator 'ENCRYPTION_NONE' in switch of enum 'encryption' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_write_set_format_zip.c	588	
Error	C4061	enumerator 'ENCRYPTION_NONE' in switch of enum 'encryption' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_write_set_format_zip.c	714	
Error	C4061	enumerator 'ENCRYPTION_NONE' in switch of enum 'encryption' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_write_set_format_zip.c	766	
Error	C4061	enumerator 'ENCRYPTION_NONE' in switch of enum 'encryption' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_write_set_format_zip.c	1033	
Error	C4061	enumerator 'COMPRESSION_UNSPECIFIED' in switch of enum 'compression' is not explicitly handled by a case label [C:\Slicer_LMU\LibArchive-build\libarchive\archive_static.vcxproj]	LibArchive	C:\Slicer_LMU\LibArchive\libarchive\archive_write_set_format_zip.c	1123</code></pre>

---

## Post #2 by @lassoan (2020-09-02 22:34 UTC)

<p>I’ve rebuilt Slicer on Windows 10 from scratch in debug and release modes yesterday without any problem. Is it a completely clean build? Which Visual Studio build tool version and Qt version do you use?</p>

---

## Post #3 by @smrolfe (2020-09-02 22:38 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, it’s a clean build and I recently updated to  VS 16 2019 and Qt 5.15.0</p>

---

## Post #4 by @lassoan (2020-09-02 22:40 UTC)

<p>Did you use x64 v142 toolset version?</p>

---

## Post #5 by @smrolfe (2020-09-02 22:42 UTC)

<p>Yes, that’s correct.</p>

---

## Post #6 by @lassoan (2020-09-02 22:47 UTC)

<p>What is the exact toolset version? There seems to be incompatibility between certain v142 toolset and libarchive versions (<a href="https://github.com/microsoft/vcpkg/issues/11481">https://github.com/microsoft/vcpkg/issues/11481</a>).</p>

---

## Post #7 by @smrolfe (2020-09-02 23:04 UTC)

<p>I am using the v14.27 toolset, which doesn’t appear in the thread, but I’ll keep looking.</p>

---

## Post #8 by @pieper (2020-09-02 23:06 UTC)

<p>Hi <a class="mention" href="/u/smrolfe">@smrolfe</a> - looks like you’ve hit this issue: <a href="https://github.com/libarchive/libarchive/pull/1395">https://github.com/libarchive/libarchive/pull/1395</a></p>

---

## Post #9 by @pieper (2020-09-02 23:08 UTC)

<p>i guess we haven’t migrated this to the Slicer fork of LibArchive.  For my windoiws builds I pointed to the upstream LibArchive as a workaround.</p>

---

## Post #10 by @pieper (2020-09-02 23:12 UTC)

<p>Here was the initial fix in the slicer fork of LibArchive: <a href="https://github.com/Slicer/libarchive/pull/2">https://github.com/Slicer/libarchive/pull/2</a></p>
<p>Since we fixed it upstream, now, I guess the right thing to do is go through the steps documented here: <a href="https://github.com/Slicer/libarchive">https://github.com/Slicer/libarchive</a>. Does anyone have time to do that?</p>

---

## Post #11 by @jamesobutler (2020-09-02 23:16 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Currently the only commit in the branch we are using that isn’t in the upstream is the following <a href="https://github.com/Slicer/libarchive/commit/92ad4c79e46805ce2dfbc46746e10d204108655e" class="inline-onebox" rel="noopener nofollow ugc">slicer: Disable LHA support · Slicer/libarchive@92ad4c7 · GitHub</a>.  It mentions</p>
<blockquote>
<p>“After we transition the Slicer build to a newer version macOS, we will be able to use the unmodified LibArchive sources”</p>
</blockquote>
<p>Can we use a direct version of the upstream now since we have updated to use newer versions of macOS?</p>

---

## Post #12 by @pieper (2020-09-02 23:44 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="11" data-topic="13310">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Can we use a direct version of the upstream now since we have updated to use newer versions of macOS?</p>
</blockquote>
</aside>
<p>Good question - I’m not sure if we’re still using the older clang compiler on the macOS factory.  it’s likely that the patch is out of date now.  <a class="mention" href="/u/jcfr">@jcfr</a> or <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>?</p>

---

## Post #13 by @jamesobutler (2020-09-03 00:06 UTC)

<p>Seems like that patch was originally committed in August 2017 so it is likely no longer needed, but we can wait on confirmation. I know we are using XCode 10.1, which has clang version 10.0.0, since it is the latest XCode version we can have on macOS 10.13.6</p>

---

## Post #14 by @pieper (2020-09-03 14:06 UTC)

<p>In case <a class="mention" href="/u/smrolfe">@smrolfe</a> or anyone else needs to build on visual studio 2019 before we sort out the Slicer/LibArchive fork issue, here’s the workaround I use.</p>
<pre><code class="lang-auto">$ git diff
diff --git a/SuperBuild/External_LibArchive.cmake b/SuperBuild/External_LibArchive.cmake
index 2107ba9..02d8cdf 100644
--- a/SuperBuild/External_LibArchive.cmake
+++ b/SuperBuild/External_LibArchive.cmake
@@ -38,7 +38,8 @@ if((NOT DEFINED LibArchive_INCLUDE_DIR

   ExternalProject_SetIfNotDefined(
     Slicer_${proj}_GIT_REPOSITORY
-    "${EP_GIT_PROTOCOL}://github.com/Slicer/LibArchive.git"
+    # "${EP_GIT_PROTOCOL}://github.com/Slicer/LibArchive.git"
+    "${EP_GIT_PROTOCOL}://github.com/libarchive/LibArchive.git"
     QUIET
     )

@@ -46,7 +47,8 @@ if((NOT DEFINED LibArchive_INCLUDE_DIR
   # - disabling LHA (See #4407)
   ExternalProject_SetIfNotDefined(
     Slicer_${proj}_GIT_TAG
-    "92ad4c79e46805ce2dfbc46746e10d204108655e" # slicer-v3.4.0-2019-06-11-614110e7
+    # "92ad4c79e46805ce2dfbc46746e10d204108655e" # slicer-v3.4.0-2019-06-11-614110e7
+    "master"
     QUIET
     )

</code></pre>

---

## Post #15 by @lassoan (2020-09-03 15:07 UTC)

<p>Could we just try to update to latest LibArchive and see if it builds fine on all platforms? I’ve submitted a pull request for this: <a href="https://github.com/Slicer/Slicer/pull/5170">https://github.com/Slicer/Slicer/pull/5170</a></p>

---

## Post #16 by @smrolfe (2020-09-03 15:18 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>, I will give this a try.</p>

---

## Post #17 by @lassoan (2020-09-03 15:19 UTC)

<p><a class="mention" href="/u/smrolfe">@smrolfe</a> please try the pull request that I linked above (cherry pick the <a href="https://github.com/Slicer/Slicer/pull/5170/commits/ae50246a9c7e0ee5a669fa05714b614467122879">commit that updates libarchive version</a>).</p>

---

## Post #18 by @smrolfe (2020-09-03 15:21 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> I will try that now.</p>

---

## Post #19 by @jcfr (2020-09-03 15:50 UTC)

<p>Thanks everyone for working on this <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>
<p>After checking that the updated LibArchive build on macOS and Linux, I integrated.</p>

---

## Post #20 by @jrl (2020-09-03 16:41 UTC)

<p>Did this resolve the issue for you? I’m receiving the same errors</p>

---

## Post #21 by @smrolfe (2020-09-03 17:03 UTC)

<p><a class="mention" href="/u/jrl">@jrl</a> it’s still building, I’ll update here when it’s done.</p>

---

## Post #22 by @pieper (2020-09-03 17:58 UTC)

<p>Still building is a good sign - probably libarchive would have failed early on.</p>

---

## Post #23 by @smrolfe (2020-09-03 18:07 UTC)

<p>Yes, it’s still compiling but the log shows LibArchive built without errors this time. Thanks everyone!</p>

---
