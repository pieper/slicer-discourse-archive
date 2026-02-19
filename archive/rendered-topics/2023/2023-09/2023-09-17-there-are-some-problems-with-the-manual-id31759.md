---
topic_id: 31759
title: "There Are Some Problems With The Manual"
date: 2023-09-17
url: https://discourse.slicer.org/t/31759
---

# There are some problems with the manual

**Topic ID**: 31759
**Date**: 2023-09-17
**URL**: https://discourse.slicer.org/t/there-are-some-problems-with-the-manual/31759

---

## Post #1 by @slicer365 (2023-09-17 15:06 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4aa1b93e0e146d223d4cbf364645c78f5deafd8.png" data-download-href="/uploads/short-url/nuGL4EgdDZDtZHG2SZYziyugR7O.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4aa1b93e0e146d223d4cbf364645c78f5deafd8.png" alt="image" data-base62-sha1="nuGL4EgdDZDtZHG2SZYziyugR7O" width="517" height="327" data-dominant-color="EAF7D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">699×442 22.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b28bf0ae9406089924a4144d9d72546800085ef5.png" data-download-href="/uploads/short-url/ptuOefobB2IlIpdp49MB6tGvezX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b28bf0ae9406089924a4144d9d72546800085ef5_2_333x375.png" alt="image" data-base62-sha1="ptuOefobB2IlIpdp49MB6tGvezX" width="333" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b28bf0ae9406089924a4144d9d72546800085ef5_2_333x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b28bf0ae9406089924a4144d9d72546800085ef5_2_499x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b28bf0ae9406089924a4144d9d72546800085ef5_2_666x750.png 2x" data-dominant-color="E7F7CD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">726×815 49.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>These two layout files are not the same as described. When running on the console, the second configuration does not pop up the dock window.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/advanced_topics.html#view-layout-definition" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/advanced_topics.html#view-layout-definition</a></p>

---

## Post #2 by @lassoan (2023-09-18 16:44 UTC)

<p>Thanks for reporting, indeed, the <code>name</code> attribute was missed from the second layout. I’ve added it now - see the working version of the layout description <a href="https://slicer.readthedocs.io/en/latest/developer_guide/advanced_topics.html#example-layout-containing-two-viewports">here</a>.</p>

---
