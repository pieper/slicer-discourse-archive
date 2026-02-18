# Build failure  using Visual Studio 2015  

**Topic ID**: 7351
**Date**: 2019-06-28
**URL**: https://discourse.slicer.org/t/build-failure-using-visual-studio-2015/7351

---

## Post #1 by @pradhan.arun479 (2019-06-28 11:24 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4<br>
Expected behavior: Should build successfully<br>
Actual behavior: Build failure .</p>
<p>I am new to 3D slicer , I installed on tools required and checked out sources from Github.<br>
I configured  the project using Cmake gui.<br>
Source  Path :F:/KS/Slicer<br>
Build Path : F:/KS/Slicer-SuperBuild-Debug</p>
<p>After  opening .sln file and building ALL_BUILD , I am getting  several errors<br>
First few errors are</p>
<ol>
<li>
<p>Error	MSB6006	“cmd.exe” exited with code 1.	python-PyGithub	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets	171</p>
</li>
<li>
<p>Error	MSB6006	“cmd.exe” exited with code 1. [F:\KS\Slicer-SuperBuild-Debug\CTK-build\CTK-build\Libs\Widgets\CTKWidgetsPythonQt.vcxproj] [F:\KS\Slicer-SuperBuild-Debug\CTK-build\CTK.vcxproj]	CTK	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets                                               171</p>
</li>
</ol>
<p>Can I get some support on how to build successfully.</p>
<p>Thanks<br>
Arun Pradhan</p>

---

## Post #2 by @lassoan (2019-06-28 15:08 UTC)

<p>Only focus on the very first build error, because all the other may be just consequences of that first one. Which one is the very first error?</p>
<p>Which Qt version do you use?</p>

---

## Post #3 by @pradhan.arun479 (2019-06-28 15:58 UTC)

<p>Correct .<br>
The Qt ver 5.13.0<br>
First error<br>
Error	MSB6006	“cmd.exe” exited with code 1.	python-PyGithub	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets	171</p>

---

## Post #4 by @jamesobutler (2019-06-28 16:06 UTC)

<blockquote>
<p>The Qt ver 5.13.0</p>
</blockquote>
<p>This is likely the source of the problem.</p>
<p>Follow <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Build Instructions - Slicer Wiki</a> which specifies that to build Slicer for Windows, Qt 5.10.X or older is required.</p>

---

## Post #5 by @pradhan.arun479 (2019-06-28 16:56 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Sorry ,I gave you incorrect information <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
The Qt ver 5.10.1</p>

---

## Post #6 by @lassoan (2019-06-28 22:22 UTC)

<p>I don’t remember seeing such an error. Since this message only indicates that python-PyGithub build failed but does not contain the actual error message, we cannot do much. You need to find the error message printed by this subproject. Try to build just this subproject and have a look at all the most recently modified files in all the build folders to find the relevant log file (probably .log or .txt file).</p>

---

## Post #7 by @pradhan.arun479 (2019-06-29 06:06 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I just complied  this sub project and got these errors , few of these are mentioned here</p>
<p>Error	MSB6006	“cmd.exe” exited with code 1.	python-PyGithub	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets	171	<br>
Error	LNK1120	154 unresolved externals [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_ssl\extension_ssl.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug\python-build\Lib\lib-dynload\Release_ssl.pyd	1	<br>
Error	LNK1120	24 unresolved externals [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_hashlib\extension_hashlib.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug\python-build\Lib\lib-dynload\Release_hashlib.pyd	1	<br>
Error	LNK2019	unresolved external symbol ASN1_INTEGER_get referenced in function _decode_certificate [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_ssl\extension_ssl.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug_ssl.obj	1	<br>
Error	LNK2019	unresolved external symbol ASN1_item_d2i referenced in function _get_peer_alt_names [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_ssl\extension_ssl.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug_ssl.obj	1	<br>
Error	LNK2019	unresolved external symbol ASN1_OBJECT_free referenced in function _ssl_nid2obj_impl [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_ssl\extension_ssl.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug_ssl.obj	1	<br>
Error	LNK2019	unresolved external symbol ASN1_STRING_data referenced in function _get_peer_alt_names [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_ssl\extension_ssl.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug_ssl.obj	1	<br>
Error	LNK2019	unresolved external symbol ASN1_STRING_length referenced in function _get_peer_alt_names [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_ssl\extension_ssl.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug_ssl.obj	1	<br>
Error	LNK2019	unresolved external symbol ASN1_STRING_to_UTF8 referenced in function _create_tuple_for_attribute [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_ssl\extension_ssl.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug_ssl.obj	1	<br>
Error	LNK2019	unresolved external symbol ASN1_TIME_print referenced in function _decode_certificate [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_ssl\extension_ssl.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug_ssl.obj	1	<br>
Error	LNK2019	unresolved external symbol AUTHORITY_INFO_ACCESS_free referenced in function _get_aia_uri [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_ssl\extension_ssl.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug_ssl.obj	1</p>

---

## Post #8 by @lassoan (2019-06-29 13:25 UTC)

<p>Build paths as long as “F:\KS\Slicer-Superbuild-Debug” are known to cause various build issues. Retry the build from scratch, putting source code in F:\S4 and build in F:\S4D.</p>
<p>If you build Slicer using Qt that was built without SSL (I think Qt binaries that you download from Qt installer are built without SSL) then you may need to disable SSL support when you configure your Slicer build in CMake.</p>

---

## Post #9 by @pradhan.arun479 (2019-06-29 17:07 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>Thanks for pointing .<br>
May I know which Cmake I should make a change as there many in multiple level ?<br>
This would really help.</p>

---

## Post #10 by @lassoan (2019-06-30 01:16 UTC)

<p>You can search for CMake variables by name in CMake GUI. To disable SSL, configure top-level build with Slicer_USE_PYTHONQT_WITH_OPENSSL set to OFF. But first just try to build Slicer in a shorter path (F:\S4, F:\S4D).</p>

---

## Post #11 by @pradhan.arun479 (2019-06-30 10:31 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thanks , Now I am getting less errors .  Ilisted  down 1st error and few warnings.<br>
Now these are  the   link errors</p>
<ol>
<li>Error	LNK1120	24 unresolved externals [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_hashlib\extension_hashlib.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug\python-build\Lib\lib-dynload\Release_hashlib.pyd	1	<br>
Warning	LNK4098	defaultlib ‘MSVCRTD’ conflicts with use of other libs; use /NODEFAULTLIB:library [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_binascii\extension_binascii.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug\LINK	1	<br>
Warning	LNK4098	defaultlib ‘MSVCRTD’ conflicts with use of other libs; use /NODEFAULTLIB:library [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_bz2\extension_bz2.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug\LINK	1	<br>
Warning	LNK4272	library machine type ‘X86’ conflicts with target machine type ‘x64’ [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_hashlib\extension_hashlib.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug\OpenSSL-install\Release\lib\ssleay32.lib	1	<br>
Warning	LNK4272	library machine type ‘X86’ conflicts with target machine type ‘x64’ [F:\KS\Slicer-SuperBuild-Debug\python-build\CMakeBuild\extensions\extension_hashlib\extension_hashlib.vcxproj]	python	F:\KS\Slicer-SuperBuild-Debug\OpenSSL-install\Release\lib\libeay32.lib	1</li>
</ol>

---

## Post #12 by @lassoan (2019-06-30 12:16 UTC)

<p>Build paths as long as “F:\KS\Slicer-Superbuild-Debug” are known to cause various build issues. Retry the build from scratch, putting source code in F:\S4 and build in F:\S4D.</p>

---

## Post #13 by @gcsharp (2019-06-30 15:07 UTC)

<p>The wiki page says 50 character limit.  The recommended path was:</p>
<p>For example: <code>C:\Slicer-SuperBuild-Debug</code> or <code>C:\Slicer-SuperBuild-Release</code> .</p>
<p>I updated the page to make the recommended path shorter, but not sure what to do about the 50 character limit.</p>

---

## Post #14 by @lassoan (2019-06-30 16:24 UTC)

<p>50 character limit is not accurate (especially since VTK modularization, which dramatically increased number of include directories). I’ve updated the build instructions to recommend limiting the source and build directory path lengths to <em>10</em> characters.</p>

---

## Post #15 by @jcfr (2019-06-30 18:37 UTC)

<p>Since it is hard to reliably warn developer, should we just remove the <a href="https://github.com/Slicer/Slicer/blob/master/CMake/PreventDirWithTooManyChars.cmake" rel="nofollow noopener">PreventDirWithTooManyChars</a> module and only rely on the documentation ?</p>
<p>I am also wondering if the generated solutions files (or makefile,  ninja file) could be analyzed after configuration to detect use of long command line and long path.</p>

---

## Post #16 by @lassoan (2019-06-30 20:39 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="15" data-topic="7351">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>I am also wondering if the generated solutions files (or makefile, ninja file) could be analyzed after configuration to detect use of long command line and long path.</p>
</blockquote>
</aside>
<p>There are a couple of different things that may fail with long paths. It would be very hard to detect them all.</p>
<p>Instead, we could fix many issues by installing VTK and ITK and use that install tree from Slicer. It would reduce the number of include and library directories, so command lines would less likely to become too long. We tried this in Plus toolkit and I think there were no major complications.</p>

---

## Post #17 by @pradhan.arun479 (2019-07-01 02:35 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>the shorter directory length works for me , I could compile the Slicer .<br>
Thanks<br>
Arun</p>

---
