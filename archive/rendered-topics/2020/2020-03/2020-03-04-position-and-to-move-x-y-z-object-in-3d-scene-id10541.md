# position and to move (x,y,z)  object in 3D Scene

**Topic ID**: 10541
**Date**: 2020-03-04
**URL**: https://discourse.slicer.org/t/position-and-to-move-x-y-z-object-in-3d-scene/10541

---

## Post #1 by @kobidk (2020-03-04 13:23 UTC)

<p>I would like to know whether the package 3D Slicer  ( C++ Windows OS)  provides APIs which allow to position and to move (x,y,z)  object in 3D Scene ( build from DICOM CT scan files)  and update the object position R.T (10 Hz) in the scene.<br>
Could you please provide an example code that shows how to do it?</p>
<p>Thanks<br>
Kobi</p>

---

## Post #2 by @lassoan (2020-03-05 01:44 UTC)

<p>Yes, this should be no problem at all. Slicer is used widely in various real-time image guidance and robotic applications. In general, achieving 30Hz update rate should be no problem. See <a href="http://www.slicerigt.org/">SlicerIGT website</a> for more details and lots of step-by-step tutorials. You can also do all these real-time object manipulations in <a href="https://github.com/KitwareMedical/SlicerVirtualReality">virtual reality</a>, using 6-DoF controllers.</p>

---

## Post #3 by @kobidk (2020-03-09 14:04 UTC)

<p>Hi  Andras,</p>
<p>Thank you for your valuable information. I looked over the material and it looks like it is a very good platform to be based on.</p>
<p>I tried to investigate it a little further, unfortunately, I got some error (see below) when I built the package SlicerIGT-mater using CMake. The file “SlicerConfig.cmake” is missing and I couldn’t find it in either one of the packages ( the above and the Slicer-master).</p>
<p>I appreciate your assistance.</p>
<p>BR</p>
<p>Kobi</p>
<p>CMake Error at CMakeLists.txt:20 (find_package):<br>
By not providing “FindSlicer.cmake” in CMAKE_MODULE_PATH this project has<br>
asked CMake to find a package configuration file provided by “Slicer”, but<br>
CMake did not find one.</p>
<p>Could not find a package configuration file provided by “Slicer” with any<br>
of the following names:</p>
<pre><code>SlicerConfig.cmake
slicer-config.cmake
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f17e1e6ea504fc01d3a45f11060b000bb73da86.jpeg" alt="image001.jpg" data-base62-sha1="fQMami7GKY3v4Y3kjEJcsxtMF2S" width="200" height="74"></p>

---

## Post #4 by @lassoan (2020-03-09 14:36 UTC)

<p>You don’t need to build SlicerIGT but you can install it from the extension manager.</p>
<p>If you want to build an extension then you need to build Slicer first, then follow <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_build_an_extension_.3F">these instructions</a>.</p>

---

## Post #5 by @kobidk (2020-03-11 15:25 UTC)

<p>Andres,</p>
<p>Thanks for ref material.</p>
<p>I attached 5 slides describe shortly what we are trying to do and my general understating about the 3DSlicer+ Extensions.</p>
<p>In slide <span class="hashtag">#6</span>, I added some questions.</p>
<p>I would appreciate your advice.</p>
<p>BR</p>
<p>Kobi</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f17e1e6ea504fc01d3a45f11060b000bb73da86.jpeg" alt="image001.jpg" data-base62-sha1="fQMami7GKY3v4Y3kjEJcsxtMF2S" width="200" height="74"></p>
<p>(Attachment Epidutech_SW_3DSlicer.pdf is missing)</p>

---

## Post #6 by @lassoan (2020-03-11 16:20 UTC)

<p>The attachment did not come through. Please upload the file to dropbox/onedrive/googledrive and post the link here.</p>

---

## Post #7 by @kobidk (2020-03-11 19:20 UTC)

<p>Thanks for letting me know and I am sorry about that.</p>
<p>Here is the file dropbox link.</p>
<p><a href="https://www.dropbox.com/s/z0fj2fz2woympps/Epidutech_SW_3DSlicer.pdf?dl=0" rel="noopener nofollow ugc">https://www.dropbox.com/s/z0fj2fz2woympps/Epidutech_SW_3DSlicer.pdf?dl=0</a>.</p>
<p>BR</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f17e1e6ea504fc01d3a45f11060b000bb73da86.jpeg" alt="image001.jpg" data-base62-sha1="fQMami7GKY3v4Y3kjEJcsxtMF2S" width="200" height="74"></p>

---
