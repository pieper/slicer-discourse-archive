# Show a video sequence in Slicer

**Topic ID**: 34464
**Date**: 2024-02-22
**URL**: https://discourse.slicer.org/t/show-a-video-sequence-in-slicer/34464

---

## Post #1 by @schcat (2024-02-22 03:55 UTC)

<p>I connect video data to Slicer using OpenIGTLinkIF, and the video appeared as an vtkMRMLVectorVolumeNode in my scene, When I click it’s “Visible” buttom, it shows in my first slice view. But I want it to show in a new view, or in an independent window, slice view need to show my CT slice.<br>
I have find method to show a 3D view or slice view in an independent window: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-slice-view-outside-the-view-layout" rel="noopener nofollow ugc">this code</a>, but how to do in my situation?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5a81ad3712537919834364d7ac6aaaaf087a048.png" data-download-href="/uploads/short-url/wLDvdLFaXIXrMBibYJemjDO1fNS.png?dl=1" title="Screenshot from 2024-02-22 11-58-24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5a81ad3712537919834364d7ac6aaaaf087a048_2_690x297.png" alt="Screenshot from 2024-02-22 11-58-24" data-base62-sha1="wLDvdLFaXIXrMBibYJemjDO1fNS" width="690" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5a81ad3712537919834364d7ac6aaaaf087a048_2_690x297.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5a81ad3712537919834364d7ac6aaaaf087a048_2_1035x445.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5a81ad3712537919834364d7ac6aaaaf087a048.png 2x" data-dominant-color="5D5D6B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-02-22 11-58-24</span><span class="informations">1228×529 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @yulaomao (2024-02-22 06:33 UTC)

<p>You can achieve displaying your CT data in the existing three slice views by setting the foreground and background of the slices. Additionally, you can display a video in a new slice view.</p>

---
