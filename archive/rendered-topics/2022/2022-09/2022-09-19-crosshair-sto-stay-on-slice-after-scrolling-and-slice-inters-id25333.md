# Crosshair sto stay on slice after scrolling and slice intersections bug

**Topic ID**: 25333
**Date**: 2022-09-19
**URL**: https://discourse.slicer.org/t/crosshair-sto-stay-on-slice-after-scrolling-and-slice-intersections-bug/25333

---

## Post #1 by @JoeNajm (2022-09-19 09:59 UTC)

<p>Hello,</p>
<p>I was wondering if there was a way to keep the crosshair on the screen while scrolling through a slice. Currently, the crosshair disappear when we scroll through a slice (when we go from image 1 to image 2).<br>
Image 1 :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ef75c760b8d143385cb7f9edace9d5f8f6af387.jpeg" data-download-href="/uploads/short-url/bgzd7hgH6RxPXn6oB8KZKCxCb55.jpeg?dl=1" title="crosshair_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ef75c760b8d143385cb7f9edace9d5f8f6af387_2_690x464.jpeg" alt="crosshair_1" data-base62-sha1="bgzd7hgH6RxPXn6oB8KZKCxCb55" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ef75c760b8d143385cb7f9edace9d5f8f6af387_2_690x464.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ef75c760b8d143385cb7f9edace9d5f8f6af387_2_1035x696.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ef75c760b8d143385cb7f9edace9d5f8f6af387.jpeg 2x" data-dominant-color="898886"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">crosshair_1</span><span class="informations">1375×925 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Image 2 :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35588a6530be4d7e31fe12f520294e9f719718cc.jpeg" data-download-href="/uploads/short-url/7BV0cIuFyJEMS1GXEwDTdbqoHAE.jpeg?dl=1" title="crosshair_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35588a6530be4d7e31fe12f520294e9f719718cc_2_690x464.jpeg" alt="crosshair_2" data-base62-sha1="7BV0cIuFyJEMS1GXEwDTdbqoHAE" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35588a6530be4d7e31fe12f520294e9f719718cc_2_690x464.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35588a6530be4d7e31fe12f520294e9f719718cc_2_1035x696.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35588a6530be4d7e31fe12f520294e9f719718cc.jpeg 2x" data-dominant-color="868684"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">crosshair_2</span><span class="informations">1375×925 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The reason why I am using crosshair instead of “Slice Intersections” is because I noticed that some random colored lines would appear on the slices (image below) when using “Slice Intersections”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43de8c2f1aba1ffd3522e7eb408fe2efd5284623.jpeg" data-download-href="/uploads/short-url/9GoNnTX4kaUkWs5bG5BgW7yGNJ9.jpeg?dl=1" title="SliceIntersectionReformat" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43de8c2f1aba1ffd3522e7eb408fe2efd5284623_2_690x463.jpeg" alt="SliceIntersectionReformat" data-base62-sha1="9GoNnTX4kaUkWs5bG5BgW7yGNJ9" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43de8c2f1aba1ffd3522e7eb408fe2efd5284623_2_690x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43de8c2f1aba1ffd3522e7eb408fe2efd5284623_2_1035x694.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43de8c2f1aba1ffd3522e7eb408fe2efd5284623_2_1380x926.jpeg 2x" data-dominant-color="8A8A88"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SliceIntersectionReformat</span><span class="informations">1381×928 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>All the slices are set to Orientation “Reformat” in the “View Controllers” module because if I set them to axial/sagittal/coronal, the volumes become rotated (note that the slice intersections now become good and there isnt any unwanted colored lines)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9c991517a8f2b2b318c82993449ca965dabdc86.jpeg" data-download-href="/uploads/short-url/qvybHtKJNzTOTRXK8F3PXk97gKa.jpeg?dl=1" title="NotReformat" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9c991517a8f2b2b318c82993449ca965dabdc86_2_690x462.jpeg" alt="NotReformat" data-base62-sha1="qvybHtKJNzTOTRXK8F3PXk97gKa" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9c991517a8f2b2b318c82993449ca965dabdc86_2_690x462.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9c991517a8f2b2b318c82993449ca965dabdc86_2_1035x693.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9c991517a8f2b2b318c82993449ca965dabdc86_2_1380x924.jpeg 2x" data-dominant-color="878785"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">NotReformat</span><span class="informations">1382×927 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Could you please help me find a solution to either the crosshair problem or the slice intersection bug ?<br>
Best Regards,<br>
Joe</p>

---
