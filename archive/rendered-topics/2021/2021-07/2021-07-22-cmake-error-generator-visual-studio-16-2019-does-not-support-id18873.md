# CMake Error Generator Visual Studio 16 2019 does not support variabl CMAKE_DEFAULT_BUILD_TYPE but it has been specified

**Topic ID**: 18873
**Date**: 2021-07-22
**URL**: https://discourse.slicer.org/t/cmake-error-generator-visual-studio-16-2019-does-not-support-variabl-cmake-default-build-type-but-it-has-been-specified/18873

---

## Post #1 by @Ciparnieks (2021-07-22 13:22 UTC)

<p>Hello,</p>
<p>When i in Cmake GUI pushing the Generate i have the error<br>
CMake Error  Generator Visual Studio 16 2019 does not support variabl CMAKE_DEFAULT_BUILD_TYPE    but it has been specified.</p>
<p>How to solve this problem?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b69fae0e21579e7bd2968672de1da1157e55539.jpeg" data-download-href="/uploads/short-url/1CYjqbLvM9E15qjVhJpg1c2VT17.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b69fae0e21579e7bd2968672de1da1157e55539_2_561x500.jpeg" alt="Screenshot_1" data-base62-sha1="1CYjqbLvM9E15qjVhJpg1c2VT17" width="561" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b69fae0e21579e7bd2968672de1da1157e55539_2_561x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b69fae0e21579e7bd2968672de1da1157e55539_2_841x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b69fae0e21579e7bd2968672de1da1157e55539_2_1122x1000.jpeg 2x" data-dominant-color="EE9596"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1139×1014 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Ciparnieks (2021-07-22 13:22 UTC)

<p>Hello, Fallowed instruction in [Windows — 3D Slicer documentation]</p>
<p>After Configure - When i Push the Button in CMAKE GUI - &gt; Generate i got the ERROR mesage</p>
<p>CMake Error:<br>
Generator</p>
<pre><code>Visual Studio 16 2019
</code></pre>
<p>does not support variable</p>
<pre><code>CMAKE_DEFAULT_BUILD_TYPE
</code></pre>
<p>but it has been specified.</p>
<p>What i must to doo to avoid the this error? How to solve the this problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b69fae0e21579e7bd2968672de1da1157e55539.jpeg" data-download-href="/uploads/short-url/1CYjqbLvM9E15qjVhJpg1c2VT17.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b69fae0e21579e7bd2968672de1da1157e55539_2_561x500.jpeg" alt="Screenshot_1" data-base62-sha1="1CYjqbLvM9E15qjVhJpg1c2VT17" width="561" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b69fae0e21579e7bd2968672de1da1157e55539_2_561x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b69fae0e21579e7bd2968672de1da1157e55539_2_841x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b69fae0e21579e7bd2968672de1da1157e55539_2_1122x1000.jpeg 2x" data-dominant-color="EE9596"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1139×1014 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Program Versions:<br>
CMAKE 3.20.5<br>
QT 5.15.2  D:/QT/5.15.2/msvc2019_64/lib/cmake/Qt5</p>

---

## Post #3 by @lassoan (2021-07-22 13:27 UTC)

<p>The solution is not to specify this variable. Visual Studio is a multi-configuration generator. You can have all your configurations in one build tree.</p>
<p>Due to complexity of Slicer’s build system, we recommend to create a separate build tree for each configuration (we do not test if building with different configurations in the same build tree works or not, so probably it does not work). This means that after you build Slicer in Debug mode, you need to create a new build tree if you want to build in release mode as well.</p>

---
