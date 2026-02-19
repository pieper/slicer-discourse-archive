---
topic_id: 16476
title: "Error Configuring 3D Slicer Cmake Does Not Support The Https"
date: 2021-03-10
url: https://discourse.slicer.org/t/16476
---

# Error configuring 3D Slicer - CMake does not support the HTTPS protocol

**Topic ID**: 16476
**Date**: 2021-03-10
**URL**: https://discourse.slicer.org/t/error-configuring-3d-slicer-cmake-does-not-support-the-https-protocol/16476

---

## Post #1 by @VivianTetzner (2021-03-10 19:06 UTC)

<p>Hi, I’m having trouble while trying to configure, and then generate, de 3D Slicer using CMake.</p>
<p> → <strong>3D Slicer 4.8</strong>: from git SlicerGitSVNArchieve, using <strong>git checkout</strong> to config the right commit where is the tree for the 4.8 version of 3D Slicer.<br>
 → <strong>CMake 3.10.3</strong>: built from source – Following <a href="https://askubuntu.com/questions/355565/how-do-i-install-the-latest-version-of-cmake-from-the-command-line/865294#865294" rel="noopener nofollow ugc">software installation - How do I install the latest version of cmake from the command line? - Ask Ubuntu</a> Teocci’s <strong>A</strong> path to install<br>
 → <strong>gcc and g++ available</strong>: 9.3 and 5.3.1<br>
 → <strong>Qt</strong>: 4 and 5</p>
<p><strong>The error</strong>:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f0ebcb63e8cec9d48bddda7e146dbf865a154ec.png" data-download-href="/uploads/short-url/29cJEd9E5pxS6OkYjqqAD1zk6vy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f0ebcb63e8cec9d48bddda7e146dbf865a154ec_2_690x127.png" alt="image" data-base62-sha1="29cJEd9E5pxS6OkYjqqAD1zk6vy" width="690" height="127" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f0ebcb63e8cec9d48bddda7e146dbf865a154ec_2_690x127.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f0ebcb63e8cec9d48bddda7e146dbf865a154ec_2_1035x190.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f0ebcb63e8cec9d48bddda7e146dbf865a154ec.png 2x" data-dominant-color="FCF6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1078×199 28.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried to follow this <a href="https://github.com/Slicer/Slicer/issues/4839" rel="noopener nofollow ugc">error: This CMake does not support the HTTPS protocol. Ensure that CMake is compiled with CMAKE_USE_OPENSSL enabled. · Issue #4839 · Slicer/Slicer · GitHub</a>, but when I tryed the steps, these were the answers:</p>
<p> → /path/to/cmake -P /path/to/Slicer/CMake/SlicerCheckCMakeHTTPS.cmake<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f958e6fd3bc4598e53a2c8793f3dc5e85d45f4b.png" data-download-href="/uploads/short-url/mLKl8pp6dm5OP97LToLJcUIuGhR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f958e6fd3bc4598e53a2c8793f3dc5e85d45f4b_2_690x110.png" alt="image" data-base62-sha1="mLKl8pp6dm5OP97LToLJcUIuGhR" width="690" height="110" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f958e6fd3bc4598e53a2c8793f3dc5e85d45f4b_2_690x110.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f958e6fd3bc4598e53a2c8793f3dc5e85d45f4b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f958e6fd3bc4598e53a2c8793f3dc5e85d45f4b.png 2x" data-dominant-color="411F36"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">955×153 32.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p> → update file CMake/SlicerCheckCMakeHTTPS.cmake:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/854a01228e6c671720b785cf0c7a1f9a6cc0caeb.png" data-download-href="/uploads/short-url/j183yp5KQhtdLET9eLTh5i4JB8f.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/854a01228e6c671720b785cf0c7a1f9a6cc0caeb_2_690x110.png" alt="image" data-base62-sha1="j183yp5KQhtdLET9eLTh5i4JB8f" width="690" height="110" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/854a01228e6c671720b785cf0c7a1f9a6cc0caeb_2_690x110.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/854a01228e6c671720b785cf0c7a1f9a6cc0caeb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/854a01228e6c671720b785cf0c7a1f9a6cc0caeb.png 2x" data-dominant-color="3E1A32"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">952×153 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p> → Replacing <a href="https://raw.githubusercontent.com/Slicer/Slicer/master/CMakeLists.txt" rel="noopener nofollow ugc">https://raw.githubusercontent.com/Slicer/Slicer/master/CMakeLists.txt</a> with <a href="https://google.com" rel="noopener nofollow ugc">https://google.com</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1b7c39bf600839c1825ae6f779c0c2e2a4932d8.png" data-download-href="/uploads/short-url/pmadX25Ej01MW0lFnzCruc4Zw24.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1b7c39bf600839c1825ae6f779c0c2e2a4932d8_2_690x120.png" alt="image" data-base62-sha1="pmadX25Ej01MW0lFnzCruc4Zw24" width="690" height="120" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1b7c39bf600839c1825ae6f779c0c2e2a4932d8_2_690x120.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1b7c39bf600839c1825ae6f779c0c2e2a4932d8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1b7c39bf600839c1825ae6f779c0c2e2a4932d8.png 2x" data-dominant-color="401D35"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">943×165 32.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I couldn’t find a way to fix it</p>

---

## Post #2 by @lassoan (2021-03-10 19:26 UTC)

<p>Is there a reason you are trying to build Slicer-4.8 instead latest master? We cannot spend much time with helping developers trying to make very old Slicer versions work.</p>

---

## Post #3 by @VivianTetzner (2021-03-10 19:38 UTC)

<p>Yes, I’m trying to build a program that a lab collegue did for his PhD, in 2018. I have the full code, which is open in github: <a href="https://github.com/CSIM-Toolkits/MRCardio" rel="noopener nofollow ugc">GitHub - CSIM-Toolkits/MRCardio: 3D Slicer extension that provides a set of modules of segmentation, registration and cardiac images analysis</a>. But I can’t build it, so I started going “back in time” and using older versions of configurations. I thought of changing the ITK version for start, but it implied that I changed the other, in order to work.</p>

---

## Post #4 by @lassoan (2021-03-10 19:50 UTC)

<p>In this field, 3 years is a long time. Instead of struggling with trying to review an old software stack, trying to nag application and library developers with supporting old code, and in the end producing something that most people cannot use (since nobody uses Slicer-4.8 anymore), I would recommend to skip forward and build the extension with the latest Slicer version. Lots of things have changed in ITK, VTK, Slicer, Python, etc. but you can always get help for updating software to work with latest application/library versions. If you run into any trouble with Slicer we can definitely help here, and probably with most VTK, ITK, Python problems, too.</p>

---

## Post #5 by @VivianTetzner (2021-03-10 20:02 UTC)

<p>Got it. This solution was a long-term plan, to update the extension, but I will change my plans and start working on it. Thanks for the attention <a class="mention" href="/u/lassoan">@lassoan</a>, for sure I will need more help in the near future <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=9" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>

---
