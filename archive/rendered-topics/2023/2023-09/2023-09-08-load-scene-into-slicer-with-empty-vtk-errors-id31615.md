---
topic_id: 31615
title: "Load Scene Into Slicer With Empty Vtk Errors"
date: 2023-09-08
url: https://discourse.slicer.org/t/31615
---

# Load scene into Slicer with empty vtk errors

**Topic ID**: 31615
**Date**: 2023-09-08
**URL**: https://discourse.slicer.org/t/load-scene-into-slicer-with-empty-vtk-errors/31615

---

## Post #1 by @Kening_Zhang (2023-09-08 07:20 UTC)

<p>Dear developers,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/896c0fb8deccc66625e9ea25fa5778f8f424f849.png" data-download-href="/uploads/short-url/jBGVU9Vl5rJfVnPhikojIoImb2h.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/896c0fb8deccc66625e9ea25fa5778f8f424f849.png" alt="image" data-base62-sha1="jBGVU9Vl5rJfVnPhikojIoImb2h" width="690" height="96" data-dominant-color="525C67"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">984×138 20.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When I try to load a scene in Slicer, error happened,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f404826d61721f824a2dc55b4355d94457cd115.png" data-download-href="/uploads/short-url/4sswxjHwrf2njI4rFQXeEqV1jXT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f404826d61721f824a2dc55b4355d94457cd115_2_690x318.png" alt="image" data-base62-sha1="4sswxjHwrf2njI4rFQXeEqV1jXT" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f404826d61721f824a2dc55b4355d94457cd115_2_690x318.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f404826d61721f824a2dc55b4355d94457cd115_2_1035x477.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f404826d61721f824a2dc55b4355d94457cd115_2_1380x636.png 2x" data-dominant-color="FDE0E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1380×636 327 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
VTK may report it as an error when I attempt to read or write an empty file, while it may be normal that a fiber is empty.<br>
According to Iassoan, a possible fix would be to apply the same technique as it is done in the model storage node: use the <a href="https://github.com/Slicer/Slicer/blob/4540594f5ff293cb387fd252e24e32be13e377c8/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx#L160C32-L160C45" rel="noopener nofollow ugc"><code>SkippedNoData</code> write state</a> to indicate that the file is expected to be empty.<br>
Best wishes,<br>
Zhang Kening</p>

---
