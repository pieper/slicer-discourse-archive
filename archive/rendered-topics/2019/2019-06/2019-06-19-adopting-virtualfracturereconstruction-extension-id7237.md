---
topic_id: 7237
title: "Adopting Virtualfracturereconstruction Extension"
date: 2019-06-19
url: https://discourse.slicer.org/t/7237
---

# Adopting VirtualFractureReconstruction extension?

**Topic ID**: 7237
**Date**: 2019-06-19
**URL**: https://discourse.slicer.org/t/adopting-virtualfracturereconstruction-extension/7237

---

## Post #1 by @jcfr (2019-06-19 13:23 UTC)

<p>Dear Slicers,</p>
<p>The VirtualFractureReconstruction extension implements modules allowing to automatically reposition bone fragments after a fracture (fracture reduction).</p>
<p>You can read more on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/VirtualFractureReconstruction">wiki</a></p>
<p>Associated repo is <a href="https://github.com/kfritscher/VirtualFractureReconstructionSlicerExtension" class="inline-onebox">GitHub - kfritscher/VirtualFractureReconstructionSlicerExtension</a></p>
<h2><a name="p-25437-question-1" class="anchor" href="#p-25437-question-1" aria-label="Heading link"></a>Question</h2>
<p>Considering that the original developers do not have interested in maintaining the extension, is there any interest from the community in adopting the extension ?</p>
<h2><a name="p-25437-anticipated-work-2" class="anchor" href="#p-25437-anticipated-work-2" aria-label="Heading link"></a>Anticipated work</h2>
<p>Since there are already pull requests fixing the extension build adding support for building against Qt5 and Slicer(see <a href="https://github.com/kfritscher/VirtualFractureReconstructionSlicerExtension/pull/3">here</a> and  <a href="https://github.com/kfritscher/VirtualFractureReconstructionSlicerExtension/pull/4">here</a>), I anticipate the first step would be:</p>
<ul>
<li>update module to use SegmentEdtor instead of legacy Editor</li>
</ul>
<p>Additional remarks (copied from the release note):</p>
<p><small><em>The functionality, GUI and workflows may change in the subsequent releases of the module. Moreover, parts of the original algorithm are written in CUDA. Due to some limitations for Slicer extensions, this CUDA code can currently not be provided in this extension. The CUDA part of the code is implementing a more flexible registration algorithm (EM-ICP), which can potentially lead to better reconstruction results. If you are interested in using this extended version of the code, please contact me.</em></small></p>
<p><small><em>At the moment ICP and EM-ICP were used for the actual registration part. However, the module has been designed in a way that the integration of additional algorithms for point set registration can easily be added. So if you are interested in testing and/or providing suitable registration algorithms, please contact me.</em></small></p>
<h2><a name="p-25437-illustrations-3" class="anchor" href="#p-25437-illustrations-3" aria-label="Heading link"></a>Illustrations</h2>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/158dd8f42ceace56ac54874d078ebd3b5f04fc9d.png" data-download-href="/uploads/short-url/34FVT7BIzo3xzIS4gRaYcJ4GvIF.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/158dd8f42ceace56ac54874d078ebd3b5f04fc9d.png" alt="image" data-base62-sha1="34FVT7BIzo3xzIS4gRaYcJ4GvIF" width="300" height="349"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">300×349 45.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c884244ed8c98c8b8640281a4983ea2a484da6e9.png" data-download-href="/uploads/short-url/sBQBBXStSMCPEbpYfe7sY3p4sCR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c884244ed8c98c8b8640281a4983ea2a484da6e9.png" alt="image" data-base62-sha1="sBQBBXStSMCPEbpYfe7sY3p4sCR" width="300" height="212"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">300×212 43.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
