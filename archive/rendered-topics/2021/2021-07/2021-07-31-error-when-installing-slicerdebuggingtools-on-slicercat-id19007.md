---
topic_id: 19007
title: "Error When Installing Slicerdebuggingtools On Slicercat"
date: 2021-07-31
url: https://discourse.slicer.org/t/19007
---

# Error when installing SlicerDebuggingTools on SlicerCAT

**Topic ID**: 19007
**Date**: 2021-07-31
**URL**: https://discourse.slicer.org/t/error-when-installing-slicerdebuggingtools-on-slicercat/19007

---

## Post #1 by @keri (2021-07-31 20:45 UTC)

<p>Hi,</p>
<p>I’m trying to install <code>SlicerDebuggingTools</code> on SlicerCAT via Extension manager.<br>
Here are my steps:</p>
<ol>
<li>clone zipped <a href="https://github.com/SlicerRt/SlicerDebuggingTools" rel="noopener nofollow ugc">SlicerDebuggingTools</a> to <code>C:\C\Extensions</code></li>
<li>in Extension Manager I click on <code>Install from file</code> and choose zipped <code>C:\C\Extensions\SlicerDebuggingTools.zip</code><br>
and here I get error:<br>
<strong>No extension description found in archive C:\C\Extensions\SlicerDebuggingTools.zip</strong></li>
</ol>
<p>I do not have much experience of writing extensions so I don’t know yet the requirements to extension. What is the possible reason for this?</p>
<p>By the way I work with my SlicerCAT wich is built (Debug) but NOT installed yet.<br>
Windows 10 x64, MSVC 2019<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9794649a67d3ab91746a49105df10cad006e7156.png" data-download-href="/uploads/short-url/lCW1LGjfDCuz9fiPg43iTVDrmw6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9794649a67d3ab91746a49105df10cad006e7156_2_690x377.png" alt="image" data-base62-sha1="lCW1LGjfDCuz9fiPg43iTVDrmw6" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9794649a67d3ab91746a49105df10cad006e7156_2_690x377.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/9794649a67d3ab91746a49105df10cad006e7156_2_1035x565.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9794649a67d3ab91746a49105df10cad006e7156.png 2x" data-dominant-color="F0F5F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1160×634 33.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-07-31 22:12 UTC)

<p>If you build a custom application then you need to build the extensions as well. Normally you bundle all the extensions, because setting up your own extension server and asking users to install extensions is more complicated for both the custom application developers and users.</p>

---

## Post #3 by @keri (2021-08-12 17:45 UTC)

<p>Thank you,</p>
<p>I did it by adding these lines of code to the main <code>CMakeLists.txt</code> of my SlicerCAT:</p>
<pre><code class="lang-auto"># SlicerDebuggingTools
set(extension_name "SlicerDebuggingTools")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")
FetchContent_Populate(${extension_name}
  SOURCE_DIR     ${${extension_name}_SOURCE_DIR}
  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/SlicerRt/SlicerDebuggingTools
  GIT_TAG        8f5436b8519e10163fd88a86f5641fe70fc6697d
  GIT_PROGRESS   1
  QUIET
  )
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})
</code></pre>

---
