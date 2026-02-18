# Extensions from github

**Topic ID**: 17421
**Date**: 2021-05-03
**URL**: https://discourse.slicer.org/t/extensions-from-github/17421

---

## Post #1 by @KAVIYA_DHARSHINI (2021-05-03 14:22 UTC)

<p>Operating system:Windows 64 bit<br>
Slicer version: 4.13<br>
Expected behavior: Matlab bridge extensions visible under developer tools after getting cloned from github.<br>
Actual behavior: not able to find the matlab bridge extension under the developer tools.<br>
Generally, how to add extensions from github?<br>
Thanks in advance.</p>

---

## Post #2 by @jamesobutler (2021-05-03 15:06 UTC)

<p>The MatlabBridge extension is currently failing to build across all platforms when using the latest Slicer preview build. It is building successfully and would be available through the Extensions Manager if you use Slicer 4.11.0-20210226.</p>
<p>If you’re up to it, you could try to resolve the build issue with the extension for Slicer preview. You will need to build Slicer from source first and use that build tree to build the extension. <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_build_an_extension_.3F" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/FAQ/Extensions - Slicer Wiki</a></p>

---

## Post #3 by @KAVIYA_DHARSHINI (2021-05-03 15:51 UTC)

<p>Hello Jamesobutler,<br>
I will try with Slicer 4.11.0-20210226. I built the slicer 4.13 with source code but unable to get the MatlabBridge through extension manager. Then I got it from github. Some extensions from github was added as per the expectation and some do not. Is there anything I have to follow while getting extensions from github.<br>
Note : I tried building the MatlabBridge extension in CMake and got errors.<br>
Thanks again.</p>

---

## Post #4 by @jamesobutler (2021-05-03 19:32 UTC)

<p>Yes  using your Slicer 4.13 build tree you would have to build MatlabBridge from source as well since it is a C++ based Slicer module and not a python scripted based Slicer module.</p>
<p>If you are still trying with Slicer 4.13, what CMake errors do you see when you try to configure building of MatlabBridge?</p>
<p>Hopefully the Slicer 4.11.20210226 is sufficient for you and allows you to download it by just using the ExtensionsManager.</p>

---

## Post #5 by @KAVIYA_DHARSHINI (2021-05-04 02:31 UTC)

<p>Hello James Butler, I got the extension using Slicer 4.11.20210226 . And the error with CMAKE is as below:</p>
<p>CMake Error at C:/D/S4R/CTK/Utilities/CMake/FindOpenIGTLink.cmake:85 (message):<br>
Please set OpenIGTLink_DIR to the directory containing<br>
OpenIGTLinkConfig.cmake.  This is either the root of the build tree, or<br>
PREFIX/lib/igtl for an installation.<br>
Call Stack (most recent call first):<br>
MatlabCommander/CMakeLists.txt:4 (find_package)</p>
<p>Thank you.</p>

---
