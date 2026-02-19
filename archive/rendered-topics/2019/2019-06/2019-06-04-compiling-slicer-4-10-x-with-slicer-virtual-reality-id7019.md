---
topic_id: 7019
title: "Compiling Slicer 4 10 X With Slicer Virtual Reality"
date: 2019-06-04
url: https://discourse.slicer.org/t/7019
---

# Compiling slicer 4.10.x with slicer Virtual Reality

**Topic ID**: 7019
**Date**: 2019-06-04
**URL**: https://discourse.slicer.org/t/compiling-slicer-4-10-x-with-slicer-virtual-reality/7019

---

## Post #1 by @mikecsu (2019-06-04 11:06 UTC)

<p>Operating system:win10 ,visual Studio 2015<br>
Slicer version: 4.10.0 or 4.10.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi, everyone. I am compiling slicer 4.10.x (using VTK 7) with slicer Virtual Reality source code and trying to get slicerVR work with the slicer 4.10.x . but i didn’t succeed and it always show the problem(see pic below) with vtkRenderingOpenVR .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8984ae90bbd44b37387db8dc9de598dc19f37e9.png" data-download-href="/uploads/short-url/xbD3D9WtHnBapmq98u5WKYiv7DP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8984ae90bbd44b37387db8dc9de598dc19f37e9.png" alt="image" data-base62-sha1="xbD3D9WtHnBapmq98u5WKYiv7DP" width="690" height="52" data-dominant-color="303033"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1628×124 5.91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Since the slicerVR installed from Extension manager can work perfectly with the slicer 4.10.x released(not source code compiled), so i wonder where i did wrong when compiling the source code .</p>
<p>I think this problem may come from the VTK version or the CMakeLists (in slicerVR source code).<br>
Slicer 4.10.x can be compiled successfully with VTK 7 or 8, but i noticed some small differences when i do the cmake:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8eca0ec2d63cd894bdf6e97d44cd21382d494c2.png" data-download-href="/uploads/short-url/uX06Hoj6spO1xq7WEvrLyXZ9B06.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8eca0ec2d63cd894bdf6e97d44cd21382d494c2.png" alt="image" data-base62-sha1="uX06Hoj6spO1xq7WEvrLyXZ9B06" width="690" height="58" data-dominant-color="F5696A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">867×74 2.21 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/392f1d79af6b3abab67f4deb013118ec1e981023.png" alt="image" data-base62-sha1="89S9TfeYyjGWaSUtSHLXoz5EYcr" width="664" height="73"></p>
<p>The slicer_VTK_RENDERING_BACKEND is different. OpenGL  and OpenGL2.</p>
<p>When compiling slicerVR with slicer4.10.x(VTK 7), cmake can easily get through, but the problem shows in vs 2015(see the first pic).</p>
<p>However, when compiling slicerVR with slicer4.10.x(VTK 8), the problem shows in cmake,  it cannot find the module : vtkRenderingOpenGL. While we can see from the above pics that VTK 8 connects to OpenGL2, which makes me really confused.</p>
<p>Anyone’s help would be appreciated.</p>

---

## Post #2 by @jcfr (2019-06-04 17:55 UTC)

<p>To better address this type of question, I suggest you provide a <code>.bat</code> file with the configure and build commands allowing to reproduce the problem.</p>
<p>That said, here are the steps I recommend to move forward:</p>
<p><strong>Step1</strong>: Virtual reality support was added in VTK8, for this reason I suggest you compile Slicer by simply padding <code>Qt5_DIR</code> variable, this will allow the build system to initialize everything else for you .</p>
<p><strong>Step2</strong> Once, you have a Slicer build tree, you should be able to build the <a href="https://github.com/KitwareMedical/SlicerOpenVR" rel="nofollow noopener">SlicerOpenVR</a> extension against it.</p>
<h3>additional info</h3>
<p>The <code>4.10.x</code> series still support building against <code>Qt4/VTK7/C++98</code> or <code>Qt5/VTK8/C++11</code>.</p>
<p>In the latest version available on Github, support for <code>Qt4/VTK7/C++98</code> was removed.</p>

---

## Post #3 by @mikecsu (2019-06-05 06:41 UTC)

<p>Thanks for your quick response. I followed your advice and here are the results:</p>
<p>1 . Slicer4.10.0 + parent_hmd_transform<br>
(<a href="https://github.com/KitwareMedical/SlicerVirtualReality/tree/parent_hmd_transform" class="inline-onebox" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerVirtualReality at parent_hmd_transform</a>)<br>
works perfectly !<img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<ol start="2">
<li>Slicer4.10.0 + SlicerVirtualReality<br>
(<a href="https://github.com/KitwareMedical/SlicerVirtualReality" class="inline-onebox" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerVirtualReality: A Slicer extension that enables user to interact with a Slicer scene using virtual reality.</a>)</li>
</ol>
<p>problem shows in VS 2015  when compiling the SlicerVR<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dad140b6058c019badfdd321b302f0b3c1ecc3f.png" data-download-href="/uploads/short-url/8NBWxFhVd22gx4tOvmmhSFbid4j.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dad140b6058c019badfdd321b302f0b3c1ecc3f.png" alt="image" data-base62-sha1="8NBWxFhVd22gx4tOvmmhSFbid4j" width="690" height="41" data-dominant-color="3A3A3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1584×95 7.04 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="3">
<li>Slicer4.10.1 + SlicerVirtualReality(no matter which slicerVR ‘s version)<br>
problem shows in cmake （see below pic):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c336ffbb53a42ee4c06ae07976828c6f7b72ae6a.png" data-download-href="/uploads/short-url/rQWWmVFxO2yZ6lKMrUzaxEvTgfg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c336ffbb53a42ee4c06ae07976828c6f7b72ae6a.png" alt="image" data-base62-sha1="rQWWmVFxO2yZ6lKMrUzaxEvTgfg" width="690" height="401" data-dominant-color="F6E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1134×660 33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>For all above ways, i compiled slicer source code by using VTK 8.</p>

---
