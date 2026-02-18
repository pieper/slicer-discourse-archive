# Build Python extenstion

**Topic ID**: 32904
**Date**: 2023-11-19
**URL**: https://discourse.slicer.org/t/build-python-extenstion/32904

---

## Post #1 by @d0rnkernsky (2023-11-19 18:33 UTC)

<p>Hello everyone!</p>
<p>I am working on a python extension, which I would like to make easily shareable only with people from my lab. Ideally, I would like to use Extension Manager’s  “Install from file…” functionality. I don’t have any experience building apps, and I am a little confused by the extension build manual <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html" class="inline-onebox" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a>.</p>
<p>My question is: do I need to build slicer first and then build the extension to be able to share it as a zip file? Or there is an easier way for a python-only extension?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2023-11-19 19:29 UTC)

<p>If it’s python-only then it’s very easy to share your extension with others.  Just share the folder (probably from a git checkout so that you can easily update) and then set the module path.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/625c79531a1de9f333b46758e141c86a02b64898.png" data-download-href="/uploads/short-url/e28UPj1m5YXtCUc6DY5uxK0mzlC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/625c79531a1de9f333b46758e141c86a02b64898_2_690x245.png" alt="image" data-base62-sha1="e28UPj1m5YXtCUc6DY5uxK0mzlC" width="690" height="245" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/625c79531a1de9f333b46758e141c86a02b64898_2_690x245.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/625c79531a1de9f333b46758e141c86a02b64898_2_1035x367.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/625c79531a1de9f333b46758e141c86a02b64898_2_1380x490.png 2x" data-dominant-color="E7E7E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1630×580 90.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @d0rnkernsky (2023-11-21 02:43 UTC)

<p>Thank you for a quick answer. But if I want it to work as “Install from file”, then the steps are: build slicer → build module → zip it, correct?</p>

---

## Post #4 by @jamesobutler (2023-11-21 04:22 UTC)

<p>Yes build Slicer, build extension and package extension is the correct steps.</p>
<p>For a python extension,</p>
<ul>
<li>Installing using the additional module paths method will take similar time and number of steps for people in your lab compared to using the Extensions Manager to “Install from file”.</li>
<li>The additional module paths approach is quickest for you if users are on different platforms such as Windows, macOS or on Linux because you don’t have to build Slicer, build extension and package extension for each of the platforms.</li>
<li>The building method is also for compatibility with a specific version of Slicer and not for multiple versions like Slicer stable (5.4.0) and latest Slicer Preview (5.5.0-2023-11-20).</li>
<li>The above two points are things to consider if you plan on updating the extension frequently once people in your lab begin to use it as you should plan on how you will distribute updates to them.</li>
</ul>

---
