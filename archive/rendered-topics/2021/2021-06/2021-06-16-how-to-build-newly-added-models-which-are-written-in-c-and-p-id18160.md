# How to build newly added models which are written in C++ and python

**Topic ID**: 18160
**Date**: 2021-06-16
**URL**: https://discourse.slicer.org/t/how-to-build-newly-added-models-which-are-written-in-c-and-python/18160

---

## Post #1 by @Mahesh_Timmanagoudar (2021-06-16 09:51 UTC)

<p>Hello There are some custom models we are able to build it using old version of slicer 4.05, VS 2013 and QT 4.X.</p>
<p>Now I wanted to upgrade the slicer into latest version that is 4.13 and along with custom models.</p>
<p>While I was building our custom models. Cmake files are throwing error.</p>
<p>Please let me know what is correct format to build the slicer with custom  models(which are written in C++,Qt,Python)</p>
<p>Please share me if there is any example cmake files for building that is written in C++.</p>

---

## Post #2 by @lassoan (2021-06-17 03:28 UTC)

<p>You can have a look at how other extensions that were ported from old Slicer versions and Qt4 to current version. For example <a href="https://github.com/SlicerIGT/SlicerIGT/search?q=qt5&amp;type=commits">SlicerIGT</a> and <a href="https://github.com/SlicerRT/SlicerRT/search?q=qt5&amp;type=commits">SlicerRT</a>. You can search for <code>Qt5</code> in commits to see what changes were required for Qt5 compatibility.</p>

---

## Post #3 by @Mahesh_Timmanagoudar (2021-06-17 05:40 UTC)

<p>I ran below command for building.</p>
<p>“C:\Program Files\CMake\bin\cmake.exe” -G “Visual Studio 16 2019” -A x64 -DQt5_DIR:PATH=C:\Qt\5.15.2\msvc2019_64\lib\cmake\Qt5 C:\D\S4</p>
<p>After running above command I got below error.</p>
<p>– SuperBuild -       JOM_EXECUTABLE:D:/W2/SPMTR-rel/jom/jom.exe<br>
– SuperBuild -     Qt4[OK]<br>
CMake Error at CMake/Superbuild/External_Qt4.cmake:71 (message):<br>
Building Qt using visual studio 1928 is <em>NOT</em> supported !<br>
Call Stack (most recent call first):<br>
D:/W2/SPMTR-rel/slicersources-src/CMake/ExternalProjectDependency.cmake:842 (include)</p>
<p>External_Qt4.cmake file snapshot is like below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21615f5fe778b8d02e153002627b469a34d9a5e9.png" data-download-href="/uploads/short-url/4LinkmNI6nZf1j5jO7CPtlpJ26B.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21615f5fe778b8d02e153002627b469a34d9a5e9_2_690x347.png" alt="image" data-base62-sha1="4LinkmNI6nZf1j5jO7CPtlpJ26B" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21615f5fe778b8d02e153002627b469a34d9a5e9_2_690x347.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21615f5fe778b8d02e153002627b469a34d9a5e9_2_1035x520.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21615f5fe778b8d02e153002627b469a34d9a5e9_2_1380x694.png 2x" data-dominant-color="F6F6E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×968 59.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Through above config openSSL file not downloaded.</p>
<p>I have marked the line where the error occurs. Actually the above one is worked for old QT, Now Its is giving error for building through QT5.15.2.</p>
<p>Please guide me how can i fix these build issues.</p>

---

## Post #4 by @lassoan (2021-06-17 13:15 UTC)

<p>I would recommend to first build Slicer by following <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#">build instructions</a> word by word. Once that you confirm that everything works well, then if you want you can start experimenting with changing things (building your own Qt, using different versions of libraries, etc.), one step at a time, and always starting from a clean build.</p>

---

## Post #5 by @Mahesh_Timmanagoudar (2021-06-28 17:12 UTC)

<p>Hi, Thanks for the reply. I have followed the build instruction. I have built the <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">SlicerCAT</a>  without any problem. I have added some models to it and started building. I got following build error.</p>
<p>38&gt;-- Setting AB LAUNCHER_SPLASHSCREEN_FILE to ‘D:/W4/AB/Applications/App/Resources/Images/SplashScreen.png’<br>
38&gt;-- Setting AB APPLE_ICON_FILE to ‘D:/W4/AB/Applications/App/Resources/Icons/XLarge/DesktopIcon.icns’<br>
38&gt;-- Setting AB WIN_ICON_FILE to ‘D:/W4/AB/Applications/App/Resources/App.ico’<br>
38&gt;-- Setting AB LICENSE_FILE to ‘D:/W4/AB/LICENSE’<br>
38&gt;-- Setting AB executable name to ‘ABApp-real.exe’<br>
38&gt;-- Setting AB EXECUTABLE to ‘D:/W4/AB-rel/S-bld/Slicer-build/bin/ABApp-real.exe’<br>
38&gt;-- --------------------------------------------------</p>
<p>38&gt;-- Setting ‘CTEST_MODEL’ variable with default value ‘Experimental’<br>
38&gt;-- Setting ‘MIDAS_PACKAGE_URL’ variable with default value ‘<a href="http://slicer.kitware.com/midas3" class="inline-onebox" rel="noopener nofollow ugc">Slicer Server by Kitware - Release</a>’<br>
38&gt;-- Setting ‘MIDAS_PACKAGE_EMAIL’ variable with default value ‘OBFUSCATED’<br>
38&gt;-- Setting ‘MIDAS_PACKAGE_API_KEY’ variable with default value ‘OBFUSCATED’<br>
38&gt;-- Setting ‘SLICER_PACKAGE_MANAGER_CLIENT_EXECUTABLE’ variable with default value ‘SLICER_PACKAGE_MANAGER_CLIENT_EXECUTABLE-NOTDEFINED’<br>
38&gt;-- Setting ‘SLICER_PACKAGE_MANAGER_URL’ variable with default value ‘SLICER_PACKAGE_MANAGER_URL-NOTDEFINED’<br>
38&gt;-- Setting ‘SLICER_PACKAGE_MANAGER_API_KEY’ variable with default value ‘OBFUSCATED’<br>
38&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake<br>
38&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok<br>
38&gt;-- Setting CPACK_PACKAGE_NAME to ‘AB’<br>
38&gt;-- Setting CPACK_PACKAGE_VENDOR to ‘AB Corporation’<br>
38&gt;-- Setting CPACK_PACKAGE_VERSION_MAJOR to ‘0’<br>
38&gt;-- Setting CPACK_PACKAGE_VERSION_MINOR to ‘1’<br>
38&gt;-- Setting CPACK_PACKAGE_VERSION_PATCH to ‘0’<br>
38&gt;-- Setting CPACK_PACKAGE_VERSION to ‘0.1.0-2021-06-11’<br>
38&gt;-- Setting CPACK_PACKAGE_INSTALL_DIRECTORY to ‘AB 0.1.0-2021-06-11’<br>
38&gt;CMake Error at CMake/SlicerCPack.cmake:290 (message):<br>
38&gt;  Failed to set variable CPACK_PACKAGE_DESCRIPTION_FILE.  Neither<br>
38&gt;  Slicer_CPACK_PACKAGE_DESCRIPTION_FILE or<br>
38&gt;  AB_CPACK_PACKAGE_DESCRIPTION_FILE are defined.<br>
38&gt;Call Stack (most recent call first):<br>
38&gt;  CMake/SlicerCPack.cmake:333 (slicer_cpack_set)<br>
38&gt;  CMake/LastConfigureStep/CMakeLists.txt:44 (include)<br>
38&gt;<br>
38&gt;<br>
38&gt;-- Configuring incomplete, errors occurred!<br>
38&gt;See also “D:/W4/AB-rel/S-bld/Slicer-build/CMakeFiles/CMakeOutput.log”.<br>
38&gt;See also “D:/W4/AB-rel/S-bld/Slicer-build/CMakeFiles/CMakeError.log”.<br>
38&gt;D:\Visual Studio 2019\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(240,5): error MSB8066: Custom build for ‘D:\W4\AB-rel\S-bld\CMakeFiles\988e155199b8f1a7ecac7f93bffe4834\Slicer-configure.rule;D:\W4\AB-rel\S-bld\CMakeFiles\988e155199b8f1a7ecac7f93bffe4834\Slicer-build.rule;D:\W4\AB-rel\S-bld\CMakeFiles\988e155199b8f1a7ecac7f93bffe4834\Slicer-forcebuild.rule;D:\W4\AB-rel\S-bld\CMakeFiles\988e155199b8f1a7ecac7f93bffe4834\Slicer-install.rule;D:\W4\AB-rel\S-bld\CMakeFiles\ef186b732632fd846b27be20eeffe050\Slicer-complete.rule;D:\W4\AB-rel\S-bld\CMakeFiles\0f36f1efb3987a0e049d3f8d21feab06\Slicer.rule’ exited with code 1.<br>
38&gt;Done building project “Slicer.vcxproj” – FAILED.</p>
<p>Please suggest me how can i fix this  issue.</p>

---

## Post #6 by @lassoan (2021-06-28 21:38 UTC)

<aside class="quote no-group" data-username="Mahesh_Timmanagoudar" data-post="5" data-topic="18160">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mahesh_timmanagoudar/48/10914_2.png" class="avatar"> Mahesh_Timmanagoudar:</div>
<blockquote>
<p>I have added some models to it and started building.</p>
</blockquote>
</aside>
<p>Which files did you modify? How? Can you send a link to your repository?</p>

---
