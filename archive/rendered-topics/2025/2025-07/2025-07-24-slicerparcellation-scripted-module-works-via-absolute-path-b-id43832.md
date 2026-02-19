---
topic_id: 43832
title: "Slicerparcellation Scripted Module Works Via Absolute Path B"
date: 2025-07-24
url: https://discourse.slicer.org/t/43832
---

# SlicerParcellation Scripted Module Works via Absolute Path but Fails When Added to Custom Slicer Build via CMake

**Topic ID**: 43832
**Date**: 2025-07-24
**URL**: https://discourse.slicer.org/t/slicerparcellation-scripted-module-works-via-absolute-path-but-fails-when-added-to-custom-slicer-build-via-cmake/43832

---

## Post #1 by @software (2025-07-24 09:43 UTC)

<p>Hi Slicer community,</p>
<p>I’ve been customizing my own Slicer build and integrating several external modules. Most of them, including other scripted modules, have been successfully added and built using <code>CMake</code>.</p>
<p>Now I’m trying to integrate this repository:<br>
<img src="https://emoji.discourse-cdn.com/twitter/link.png?v=15" title=":link:" class="emoji" alt=":link:" loading="lazy" width="20" height="20"> <a href="https://github.com/fepegar/SlicerParcellation" class="inline-onebox" rel="noopener nofollow ugc">GitHub - fepegar/SlicerParcellation: 3D Slicer modules for brain segmentation using deep learning.</a></p>
<p><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> When I manually set its <strong>absolute path</strong> in <code>Application Settings &gt; Modules</code>, the module loads and runs correctly in my custom Slicer build — so the code itself is functional.</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/cross_mark.png?v=15" title=":cross_mark:" class="emoji" alt=":cross_mark:" loading="lazy" width="20" height="20"> However, when I try to <strong>add it to my custom Slicer build via CMake</strong>, even after creating a <code>CMakeLists.txt</code> inside the module and setting it up like other scripted modules, I get build errors during the configuration or compilation step.</p>
<p>This issue only happens during the build process. Other scripted modules I’ve added are building fine.</p>
<h3><a name="p-127027-what-ive-done-1" class="anchor" href="#p-127027-what-ive-done-1" aria-label="Heading link"></a>What I’ve done:</h3>
<ul>
<li>Cloned the repo into the Slicer source tree (e.g., <code>Modules/Scripted/SlicerParcellation</code>).</li>
<li>Created a <code>CMakeLists.txt</code> for the module.</li>
<li>Registered it like other modules in my custom build’s <code>CMakeLists.txt</code>.</li>
<li>Confirmed it works when loaded manually.</li>
</ul>
<p>##<a class="hashtag-cooked" href="/tag/cmake" data-type="tag" data-slug="cmake" data-id="429" data-style-type="icon" data-icon="tag"><span class="hashtag-icon-placeholder"><svg class="fa d-icon d-icon-square-full svg-icon svg-node"><use href="#square-full"></use></svg></span><span>cmake</span></a>.txt</p>
<p><span class="hashtag-raw">#-----------------------------------------------------------------------------</span></p>
<p>set(MODULE_GROUP_NAME SlicerParcellation)</p>
<p><span class="hashtag-raw">#-----------------------------------------------------------------------------</span></p>
<p>set(MODULE_PYTHON_SCRIPTS<br>
BrainParcellation.py<br>
BrainResectionCavitySegmentation.py<br>
InferenceUtils.py<br>
PyTorchUtils.py<br>
TorchIOUtils.py<br>
)</p>
<p><span class="hashtag-raw">#-----------------------------------------------------------------------------</span></p>
<p>set(MODULE_PYTHON_LIBS<br>
lib/GeneralUtils.py<br>
lib/sitkUtils.py<br>
lib/<strong>init</strong>.py<br>
)</p>
<p><span class="hashtag-raw">#-----------------------------------------------------------------------------</span></p>
<p>set(MODULE_PYTHON_RESOURCES<br>
Resources/Icons/BrainParcellation.png<br>
Resources/Icons/BrainResectionCavitySegmentation.png<br>
GIFNiftyNet.ctbl<br>
)</p>
<p><span class="hashtag-raw">#-----------------------------------------------------------------------------</span></p>
<p>slicerMacroBuildScriptedModule(<br>
NAME ${MODULE_GROUP_NAME}<br>
SCRIPTS ${MODULE_PYTHON_SCRIPTS}<br>
LIBS ${MODULE_PYTHON_LIBS}<br>
RESOURCES ${MODULE_PYTHON_RESOURCES}<br>
WITH_GENERIC_TESTS<br>
)</p>
<h3><a name="p-127027-module-in-my-scripted-modules-folder-2" class="anchor" href="#p-127027-module-in-my-scripted-modules-folder-2" aria-label="Heading link"></a>Module in my scripted Modules folder</h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b0210d47bc53c110b420b29101cfd3305be0c0c.png" data-download-href="/uploads/short-url/aHyeDD3BXaMLPbpjNhLFaeK6bko.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b0210d47bc53c110b420b29101cfd3305be0c0c.png" alt="image" data-base62-sha1="aHyeDD3BXaMLPbpjNhLFaeK6bko" width="690" height="408" data-dominant-color="262A2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">804×476 14.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
