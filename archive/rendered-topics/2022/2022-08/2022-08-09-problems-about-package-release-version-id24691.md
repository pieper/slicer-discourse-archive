# Problems about package release version

**Topic ID**: 24691
**Date**: 2022-08-09
**URL**: https://discourse.slicer.org/t/problems-about-package-release-version/24691

---

## Post #1 by @zhang_ming (2022-08-09 11:43 UTC)

<h2><a name="p-81904-package-slicer-create-installer-packagehttpsslicerreadthedocsioenlatestdeveloper_guidebuild_instructionswindowshtmlpackage-slicer-create-installer-package-1" class="anchor" href="#p-81904-package-slicer-create-installer-packagehttpsslicerreadthedocsioenlatestdeveloper_guidebuild_instructionswindowshtmlpackage-slicer-create-installer-package-1" aria-label="Heading link"></a>Package Slicer (create installer package)<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#package-slicer-create-installer-package" rel="noopener nofollow ugc">¶</a></h2>
<ul>
<li>Start Visual Studio with the launcher:</li>
</ul>
<p>Slicer.exe --VisualStudioProject</p>
<ul>
<li>Select <code>Release</code> build configuration.</li>
<li>In the “Solution Explorer”, right click on <code>PACKAGE</code> project (in the CMakePredefinedTargets folder) and then select <code>Build</code>.</li>
</ul>
<p>the latest version, using vs 2022 ,but can’t find the ‘PACKAGE’ button or related thing.<br>
I want find out  what package tools is suggested , NSIS or vs extensions ? if NSIS,may I have a look at you scripts?</p>

---

## Post #2 by @zhang_ming (2022-08-09 12:26 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb57f6a2786a48b5d2f49e25bc9f7793796c68cc.png" alt="20220809202445" data-base62-sha1="t0Ro0B0sVzQUEeXMZfPaFzY0rEg" width="272" height="286"><br>
I find it, the doc is not in detail, I need open slicer-build folder, and the double click the Slicer.sln solution，LOL</p>

---
