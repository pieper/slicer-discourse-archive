---
topic_id: 30563
title: "Editor For Py Files Is Now Configurable"
date: 2023-07-12
url: https://discourse.slicer.org/t/30563
---

# Editor for .py files is now configurable

**Topic ID**: 30563
**Date**: 2023-07-12
**URL**: https://discourse.slicer.org/t/editor-for-py-files-is-now-configurable/30563

---

## Post #1 by @lassoan (2023-07-12 19:08 UTC)

<p>Until recently, when a developer clicked the <code>Edit</code> button in the module’s <code>Reload &amp; Test</code> section, Slicer opened the Python file of the module using the program associated with Python files in the operating system settings.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b01ccb3dc990583553e3a1224749554b9eea1d4e.png" data-download-href="/uploads/short-url/p7XIYHOHMo5RO7t5IA0wC9eIdGe.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b01ccb3dc990583553e3a1224749554b9eea1d4e_2_690x194.png" alt="image" data-base62-sha1="p7XIYHOHMo5RO7t5IA0wC9eIdGe" width="690" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b01ccb3dc990583553e3a1224749554b9eea1d4e_2_690x194.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b01ccb3dc990583553e3a1224749554b9eea1d4e_2_1035x291.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b01ccb3dc990583553e3a1224749554b9eea1d4e.png 2x" data-dominant-color="3F4040"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1145×323 22.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, sometimes the operating system settings did not have any program associated with Python files or it was not an editor, therefore this function did not open the .py file in an editor.</p>
<p>In recent Slicer Preview Releases, a new option is added in menu: Edit / Application Settings / Python / General: <code>Editor for .py files</code>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ac42ae68871e923fbe5b1f6f09b4278494c716e.png" data-download-href="/uploads/short-url/jNAb2k80NdlI2YZPC7DgSKQ5cGW.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ac42ae68871e923fbe5b1f6f09b4278494c716e_2_690x302.png" alt="image" data-base62-sha1="jNAb2k80NdlI2YZPC7DgSKQ5cGW" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ac42ae68871e923fbe5b1f6f09b4278494c716e_2_690x302.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ac42ae68871e923fbe5b1f6f09b4278494c716e_2_1035x453.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ac42ae68871e923fbe5b1f6f09b4278494c716e.png 2x" data-dominant-color="414241"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1378×604 30.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If path to an editor executable (such as Visual Studio Code, PyCharm, …) is specified there then Slicer will open .py files are opened using this program instead of the operating system default.</p>

---

## Post #2 by @Muhammed_Fatih_Talu (2023-07-12 19:15 UTC)

<p>Thanks for quick reply.<br>
But I dont see the “Editor for .py files:” parameter at Python-&gt;General.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d23ba49c18425ba3a8a0c549a0e7fb062b0e9b67.png" data-download-href="/uploads/short-url/tZO3j46eSjd960ULoEFuztfmY4v.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d23ba49c18425ba3a8a0c549a0e7fb062b0e9b67.png" alt="image" data-base62-sha1="tZO3j46eSjd960ULoEFuztfmY4v" width="574" height="500" data-dominant-color="F9FAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">673×586 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2023-07-12 19:20 UTC)

<aside class="quote no-group" data-username="Muhammed_Fatih_Talu" data-post="2" data-topic="30563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muhammed_fatih_talu/48/14646_2.png" class="avatar"> Muhammed_Fatih_Talu:</div>
<blockquote>
<p>But I dont see the “Editor for .py files:” parameter at Python-&gt;General.</p>
</blockquote>
</aside>
<p>As I wrote above, the feature was introduced in recent Slicer Preview Releases. Download the Slicer Preview Release to get this option.</p>

---

## Post #4 by @lassoan (2023-07-12 19:25 UTC)

<p>A post was split to a new topic: <a href="/t/surfacewrapsolidify-extension-does-not-work-in-latest-slicer-preview-release/30565">SurfaceWrapSolidify extension does not work in latest Slicer Preview Release</a></p>

---

## Post #5 by @moraleda (2023-10-10 20:10 UTC)

<p>Thanks for that. On Linux with Slicer 5.4, I can use Sublime as my editor. Sadly, on macOS with preview Slicer 5.5 this does not work. Am I doing something wrong? Should I put something different to the path? I am very new to macOS so there might be a mistake on my side. Thanks for your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f520ecdf500c4743c43c0de078af21cbb571afd5.png" data-download-href="/uploads/short-url/yYvwnVcx0ujzhC8f2WxsDawpvaR.png?dl=1" title="Screenshot 2023-10-10 at 22.05.52" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f520ecdf500c4743c43c0de078af21cbb571afd5_2_345x33.png" alt="Screenshot 2023-10-10 at 22.05.52" data-base62-sha1="yYvwnVcx0ujzhC8f2WxsDawpvaR" width="345" height="33" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f520ecdf500c4743c43c0de078af21cbb571afd5_2_345x33.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f520ecdf500c4743c43c0de078af21cbb571afd5_2_517x49.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f520ecdf500c4743c43c0de078af21cbb571afd5_2_690x66.png 2x" data-dominant-color="333333"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-10 at 22.05.52</span><span class="informations">1280×126 6.33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb99e621a0d8ca6abf702ba3514ea383bf1cb576.png" data-download-href="/uploads/short-url/t38EvZ6rjZrKddxBAOBdFNoCzJk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb99e621a0d8ca6abf702ba3514ea383bf1cb576_2_172x85.png" alt="image" data-base62-sha1="t38EvZ6rjZrKddxBAOBdFNoCzJk" width="172" height="85" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb99e621a0d8ca6abf702ba3514ea383bf1cb576_2_172x85.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb99e621a0d8ca6abf702ba3514ea383bf1cb576_2_258x127.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb99e621a0d8ca6abf702ba3514ea383bf1cb576_2_344x170.png 2x" data-dominant-color="444242"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">826×408 27.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2023-10-10 20:24 UTC)

<p>You need to specify the executable there. “For your convenience” macOS Finder hides the actual executable file path and just returns the path of the app bundle. You need to open the bundle (by right-clicking on it and choose to open contents), then locate the executable file, and then copy that path to the Slicer settings.</p>
<p>My impression is that macOS user experience designers are obsessed with trying to make things simpler for the crowds and they don’t care if that makes things really inconvenient for developers like you.</p>

---
