# How to build NVIDIA extension using CMake

**Topic ID**: 19681
**Date**: 2021-09-15
**URL**: https://discourse.slicer.org/t/how-to-build-nvidia-extension-using-cmake/19681

---

## Post #1 by @akmal871026 (2021-09-15 08:55 UTC)

<p>Hi all, I have followed this instruction to plug in NVIDIA.</p>
<p>But, how to build it in CMake. (attached picture is my C Make)</p>
<p>this step I did not get the last step.</p>
<p><strong>This one: To build extension package, build 3D Slicer then configure ai-assisted-annotation-client project using CMake, defining these variables: -DSlicer_DIR:PATH=… -DNvidiaAIAssistedAnnotation_BUILD_SLICER_EXTENSION:BOOL=ON</strong></p>
<h2><a name="p-66310-for-developers-1" class="anchor" href="#p-66310-for-developers-1" aria-label="Heading link"></a>For developers</h2>
<p>The plugin can be downloaded and installed directly from GitHub:</p>
<ul>
<li>git clone <a href="https://github.com/NVIDIA/ai-assisted-annotation-client.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - NVIDIA/ai-assisted-annotation-client: Client side integration example source code and libraries for AI-Assisted Annotation SDK</a></li>
<li>Open 3D Slicer: Go to Edit → Application Settings → Modules → Additional Module Paths
<ol>
<li>Add New Module Path: &lt;FULL_PATH&gt;/slicer-plugin/NvidiaAIAA</li>
<li>Restart</li>
</ol>
</li>
<li>To build extension package, build 3D Slicer then configure ai-assisted-annotation-client project using CMake, defining these variables: -DSlicer_DIR:PATH=… -DNvidiaAIAssistedAnnotation_BUILD_SLICER_EXTENSION:BOOL=ON<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/509b63267decac58fd1cd1db07abf0397824bd31.jpeg" data-download-href="/uploads/short-url/bv571Vj6dhWOJrsjOeUVFwEzIyt.jpeg?dl=1" title="CMake" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/509b63267decac58fd1cd1db07abf0397824bd31_2_690x468.jpeg" alt="CMake" data-base62-sha1="bv571Vj6dhWOJrsjOeUVFwEzIyt" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/509b63267decac58fd1cd1db07abf0397824bd31_2_690x468.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/509b63267decac58fd1cd1db07abf0397824bd31_2_1035x702.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/509b63267decac58fd1cd1db07abf0397824bd31_2_1380x936.jpeg 2x" data-dominant-color="FDFDFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CMake</span><span class="informations">2640×1792 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>

---

## Post #2 by @lassoan (2021-09-15 13:40 UTC)

<p>NVIDIA AI-assisted Annotation extension only contains Python-scripted modules, so there is no need to build it. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-an-extension">Developer guide</a>:</p>
<blockquote>
<p>To build extensions that contain modules implemented in C++, you need to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html">build Slicer from source</a> on your machine; they cannot be built against a binary download. If developing modules in Python only, then it is not necessary to build the extension.</p>
</blockquote>
<p>You can download and modify the extension and run it as described in the documentation that you quoted above or in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#run-slicer-with-your-custom-modules">Developer guide</a>.</p>

---

## Post #3 by @akmal871026 (2021-09-15 13:59 UTC)

<p>Yeah, I’ve tried it. But have the got error</p>

---

## Post #4 by @lassoan (2021-09-15 16:56 UTC)

<p>If you need any help resolving the error then tell us what the error is.</p>

---
