---
topic_id: 11312
title: "Tracking Tumors Growth Shrinkage In Slicer 3D"
date: 2020-04-27
url: https://discourse.slicer.org/t/11312
---

# Tracking tumors growth/ shrinkage in Slicer 3D

**Topic ID**: 11312
**Date**: 2020-04-27
**URL**: https://discourse.slicer.org/t/tracking-tumors-growth-shrinkage-in-slicer-3d/11312

---

## Post #1 by @emipaw (2020-04-27 10:50 UTC)

<p>Hi,<br>
I want to compare liver tumors growth and shrinkage - I read that there is a special extension for this purpose - ChangeTracker, but I also read that it is dedicated specifically for meningioma growth analysis. And I just wonder if I would be able to use it for comparing liver tumors (I have CT scans and USG 3D images). If no do you have any idea how could I deal with comparing tumors sizes? Should I segment tumors and use<br>
Segment Statistics mode?</p>

---

## Post #2 by @lassoan (2020-04-27 16:33 UTC)

<p>ChangeTracker automates some aspects of the comparison, so if the assumptions that are listed in the documentation are true for your images then you may save some time using this extension.</p>
<p>Otherwise, you can segment the tumors using Segment Editor and compare their volume using Segment Statistics.</p>
<p>You can can also get some additional metrics on boundary distance and volume overlap using Segment Comparison module (provided by SlicerRT extension).</p>
<p>You can get dense displacement field of how the tumor moved and deformed using Segment Registration extension.</p>
<p>If you have many time points then you can put all your volumes into a volume sequence and track tumor changes in time using Sequence Registration module.</p>
<p>There are more analysis options, if you can tell what data you have and exactly you are interested in then we can give more specific advice.</p>

---

## Post #3 by @emipaw (2020-05-12 20:41 UTC)

<p>Hi,</p>
<p>When I loaded my DICOM data into Change Tracker I couldn’t choose the ROI - the “frames” won’t appears on my images - only in 3D model window:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/263750e2a77033b66d1a62a9ad69715b7bbf081a.png" data-download-href="/uploads/short-url/5s4EMtmFnndA1gMTCzQrS7JFuwW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/263750e2a77033b66d1a62a9ad69715b7bbf081a_2_431x500.png" alt="image" data-base62-sha1="5s4EMtmFnndA1gMTCzQrS7JFuwW" width="431" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/263750e2a77033b66d1a62a9ad69715b7bbf081a_2_431x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/263750e2a77033b66d1a62a9ad69715b7bbf081a_2_646x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/263750e2a77033b66d1a62a9ad69715b7bbf081a.png 2x" data-dominant-color="737593"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">681×789 92.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But it appears when I am using test data:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95a4cdd05ebc9dae156e367bacf927ddd31110b1.png" data-download-href="/uploads/short-url/llOevjRHJWOvWOwCyh6jbIBviOR.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95a4cdd05ebc9dae156e367bacf927ddd31110b1_2_411x499.png" alt="2" data-base62-sha1="llOevjRHJWOvWOwCyh6jbIBviOR" width="411" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95a4cdd05ebc9dae156e367bacf927ddd31110b1_2_411x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95a4cdd05ebc9dae156e367bacf927ddd31110b1_2_616x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95a4cdd05ebc9dae156e367bacf927ddd31110b1.png 2x" data-dominant-color="747594"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">662×805 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can you tell if it is something wrong with my data?</p>
<p>First of all I want to campare liver tumors - CT images. I want to assess tumor shrinkage/growth between exams: baseline from April 2019, follow up October 2019 and I am looking for proper tools for that. I thought ChangeTracker sounded reasonable, but I am not sure what about this ROI situation.</p>
<p>I am not sure about Segment Comparison module - should I firstly segment tumor from April 2019, later from October? And try to upload both simultaneously? Is it doable? Because when I uploaded both of this exams and try use Segment Editor it looked like it’s stuck. How to proceed with that?</p>

---
