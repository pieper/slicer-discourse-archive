---
topic_id: 33503
title: "Extension Configure Error For Mac Os On Cdash"
date: 2023-12-22
url: https://discourse.slicer.org/t/33503
---

# Extension configure error for Mac Os on cdash

**Topic ID**: 33503
**Date**: 2023-12-22
**URL**: https://discourse.slicer.org/t/extension-configure-error-for-mac-os-on-cdash/33503

---

## Post #1 by @chir.set (2023-12-22 19:28 UTC)

<p>Hi,</p>
<p>cdash is reporting a configure <a href="https://slicer.cdash.org/build/3247177/configure" rel="noopener nofollow ugc">error</a> for ExtraMarkups extension for Mac. This concerns Slicer stable only, while the extension builds for preview.</p>
<pre><code class="lang-auto">  Imported target "MRMLCore" includes non-existent path

    "/Applications/Xcode-14.2.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX14.0.sdk/System/Library/Frameworks/OpenGL.framework"

  in its INTERFACE_INCLUDE_DIRECTORIES.
</code></pre>
<p>Is it a missing path on the factory machine? Or should the CMakeLists files be updated? If the latter, what could be wrong in it?</p>
<p>Thank you.</p>

---
