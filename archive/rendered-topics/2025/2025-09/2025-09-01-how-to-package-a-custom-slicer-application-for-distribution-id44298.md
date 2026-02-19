---
topic_id: 44298
title: "How To Package A Custom Slicer Application For Distribution"
date: 2025-09-01
url: https://discourse.slicer.org/t/44298
---

# How to Package a Custom Slicer Application for Distribution

**Topic ID**: 44298
**Date**: 2025-09-01
**URL**: https://discourse.slicer.org/t/how-to-package-a-custom-slicer-application-for-distribution/44298

---

## Post #1 by @software (2025-09-01 11:43 UTC)

<p>I have built a custom Slicer application using the <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">Kitware SlicerCustomAppTemplate</a>. I have also integrated 5 custom scripted modules successfully.</p>
<p>Now, I would like to package the application so that it can be distributed and installed on other PCs.</p>
<p>What is the recommended way to package and distribute a custom Slicer application with all included modules? Are there specific steps or best practices for creating installers for Windows/Linux/Mac so others can run it without rebuilding?</p>
<p>Any guidance or references would be greatly appreciated. Thank you!</p>

---

## Post #2 by @cpinter (2025-09-01 12:29 UTC)

<p>You simply need to build the Package project in the inner <code>Slicer-build</code> directory, just like when you want to package the vanilla Slicer. All the custom modules (and open-source extensions) you have included in the main CMake will be packaged as well, along with all the resources that are included in CMake as resources.</p>
<p>On Windows it is starting build for the PACKAGE project only in said solution. On Linux, it is running <code>make package</code> from said directory. On Mac I’m not sure exactly but you basically need to build that project.</p>
<p>The installer will be generated in the same <code>Slicer-build</code> directory.</p>

---

## Post #3 by @software (2025-09-01 18:38 UTC)

<p>Do we just need to open the <code>Slicer-build</code> solution (<code>Slicer.sln</code>) in Visual Studio and build the <strong>PACKAGE</strong> project directly, or is it necessary to make changes in the root CMake for packaging?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf5ec77a7cf7c65868ca5c8b99ca5b8ce4e35d08.png" data-download-href="/uploads/short-url/tAtTNfHwCqt11EGDYoUpyv7tHjq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf5ec77a7cf7c65868ca5c8b99ca5b8ce4e35d08_2_690x401.png" alt="image" data-base62-sha1="tAtTNfHwCqt11EGDYoUpyv7tHjq" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf5ec77a7cf7c65868ca5c8b99ca5b8ce4e35d08_2_690x401.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf5ec77a7cf7c65868ca5c8b99ca5b8ce4e35d08_2_1035x601.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf5ec77a7cf7c65868ca5c8b99ca5b8ce4e35d08_2_1380x802.png 2x" data-dominant-color="242424"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1537×895 47.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2025-09-02 08:45 UTC)

<p>No need to change anything.</p>
<blockquote>
<p>Do we just need to open the <code>Slicer-build</code> solution (<code>Slicer.sln</code>) in Visual Studio and build the <strong>PACKAGE</strong> project directly</p>
</blockquote>
<p>Yes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31258faf3d1be3e2e58a6a63ad6e15659e0b222b.png" data-download-href="/uploads/short-url/70LRYXrpJWepQ8F2NDsypxgtAuv.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31258faf3d1be3e2e58a6a63ad6e15659e0b222b.png" alt="image" data-base62-sha1="70LRYXrpJWepQ8F2NDsypxgtAuv" width="690" height="337" data-dominant-color="2B2B2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">725×355 14.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @software (2025-09-02 10:37 UTC)

<p>I followed the same steps you mentioned, but when I click on <strong>Build</strong> Only Packages, I get these two errors:<br>
PACKAGE    EXEC    1<br>
PACKAGE    Microsoft.CppCommon.targets    166</p>
<p>C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc7a0e1c5e38d4f1c1aedeb8e65e2d5331556e41.png" data-download-href="/uploads/short-url/taSUa81KytuhpQi4dlkNRiRBHsB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc7a0e1c5e38d4f1c1aedeb8e65e2d5331556e41_2_690x64.png" alt="image" data-base62-sha1="taSUa81KytuhpQi4dlkNRiRBHsB" width="690" height="64" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc7a0e1c5e38d4f1c1aedeb8e65e2d5331556e41_2_690x64.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc7a0e1c5e38d4f1c1aedeb8e65e2d5331556e41_2_1035x96.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc7a0e1c5e38d4f1c1aedeb8e65e2d5331556e41_2_1380x128.png 2x" data-dominant-color="2A292B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1904×178 11.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @cpinter (2025-09-02 11:20 UTC)

<p>Well, the project in my screenshot does not seem to be the correct one (I never do this via VS, at least not in the past few years). But basically you need to build this one:</p>
<p><code>c:\d\S5R\Slicer-build\PACKAGE.vcxproj</code></p>

---

## Post #7 by @software (2025-09-04 09:07 UTC)

<p>Okay, but I have one confusion. All my custom scripted modules depend on several libraries that are not included in Slicer by default.</p>
<p>Before packaging, I integrated the modules and built them using <em>All Build</em> without any errors. While using the modules, I installed the required libraries through the Python console.</p>
<p>Now my question is: before packaging, do I need to install all these libraries again, or will they be included automatically in the packaged application?</p>

---
