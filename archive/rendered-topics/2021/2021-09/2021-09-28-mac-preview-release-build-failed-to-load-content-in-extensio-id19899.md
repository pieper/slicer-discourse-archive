# Mac preview release build failed to load content in extension manager

**Topic ID**: 19899
**Date**: 2021-09-28
**URL**: https://discourse.slicer.org/t/mac-preview-release-build-failed-to-load-content-in-extension-manager/19899

---

## Post #1 by @RuoyanMeng (2021-09-28 18:48 UTC)

<p>Build env: MacOS 11.6, Qt 5.15.2, cmake 3.20.5</p>
<p>I fetched the latest slicer preview release(4.13.0-2021-09-27) from the slicer master branch. Cause SimpleITK cannot be built from mac, the solution mentioned here (<a href="https://github.com/Slicer/Slicer/issues/5498" rel="noopener nofollow ugc">issues 5498</a>) is not working for me, so I disabled the build for SimpleITK since our development doesn’t require this module. After a successful build, the extension manager is not working, error message in terminal:</p>
<pre><code class="lang-auto">[52428:95747:0928/065957.963701:ERROR:gl_context_cgl.cc(118)] Error creating context.
[0928/065958.085678:ERROR:icu_util.cc(251)] Couldn't mmap icu data file
[0928/065958.086204:ERROR:icu_util.cc(251)] Couldn't mmap icu data file
[0928/065958.884304:ERROR:icu_util.cc(251)] Couldn't mmap icu data file
</code></pre>
<p>And the extension manager looks:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f53da31595f5e1f827b73c566322391e972be7f.jpeg" data-download-href="/uploads/short-url/2bAOw91Pdl5dN2LSYiEaqy8FHm7.jpeg?dl=1" title="Screen Shot 2021-09-28 at 7.17.28 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f53da31595f5e1f827b73c566322391e972be7f_2_517x372.jpeg" alt="Screen Shot 2021-09-28 at 7.17.28 AM" data-base62-sha1="2bAOw91Pdl5dN2LSYiEaqy8FHm7" width="517" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f53da31595f5e1f827b73c566322391e972be7f_2_517x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f53da31595f5e1f827b73c566322391e972be7f_2_775x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f53da31595f5e1f827b73c566322391e972be7f_2_1034x744.jpeg 2x" data-dominant-color="3D3F41"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-09-28 at 7.17.28 AM</span><span class="informations">1662×1198 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After this, I try to restore the SlicerJupyter extension manually. I download it from <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/61529f30342a877cb3c8b4c5" rel="noopener nofollow ugc">here</a> and it installed successfully. However, the JupyterKernel is unable to load after restart Slicer.</p>
<p>I also download the package dmg file and run it, the extension manager works fine there:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/977850a8f1d9bf176e861db9708a98576066a265.jpeg" data-download-href="/uploads/short-url/lBXS3AYRu4E183csr2fD78yBMTr.jpeg?dl=1" title="Screen Shot 2021-09-28 at 7.16.26 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/977850a8f1d9bf176e861db9708a98576066a265_2_517x367.jpeg" alt="Screen Shot 2021-09-28 at 7.16.26 AM" data-base62-sha1="lBXS3AYRu4E183csr2fD78yBMTr" width="517" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/977850a8f1d9bf176e861db9708a98576066a265_2_517x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/977850a8f1d9bf176e861db9708a98576066a265_2_775x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/977850a8f1d9bf176e861db9708a98576066a265_2_1034x734.jpeg 2x" data-dominant-color="B0B0B1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-09-28 at 7.16.26 AM</span><span class="informations">1650×1174 88.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Does anyone have an idea of what leading to this?</p>

---

## Post #2 by @lassoan (2021-09-28 20:19 UTC)

<p>This is the expected behavior. If you build Slicer then you also need to build all the extenions that you want to use to ensure ABI compatibility.</p>
<aside class="quote" data-post="4" data-topic="19770">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/unable-to-access-extensions-with-latest-code-as-of-21st-sept-2021/19770/4">Unable to access extensions with latest code - as of 21st Sept 2021</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    The extension manager only supports installing extensions for versions of Slicer corresponding to the revisions of Slicer Preview builds. The latest Slicer Preview 4.13.0-2021-09-18 is revision 30223, so extensions from the factory server are available for that version but not for the revisions of any commits from today. If you have your own Slicer that you’ve manually built, you are expected to manually build any extensions you need as well.
  </blockquote>
</aside>

<p>After you have build Slicer on your computer (which is not very easy), building the extensions is trivial, just two CMake commands - see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-test-and-package">here</a>.</p>

---

## Post #3 by @RuoyanMeng (2021-09-29 08:18 UTC)

<p>Hi, Thanks for the suggestions.<br>
I’ve built Slicer on my Mac by disabling the simpleITK module. However, when I try to build SlicerJupyter, a problem caused by lacking argon2-cffi wheel occurred, I also posted this problem here:</p>
<blockquote>
<p><a href="https://discourse.slicer.org/t/slicerjupyter-build-failed-on-macosx-due-to-failed-building-wheel-for-argon2-cffi/19804" class="inline-onebox">SlicerJupyter build failed on MacOSX due to failed building wheel for argon2-cffi</a></p>
</blockquote>
<p>The advice received is to try to install it from extension manager.</p>

---
