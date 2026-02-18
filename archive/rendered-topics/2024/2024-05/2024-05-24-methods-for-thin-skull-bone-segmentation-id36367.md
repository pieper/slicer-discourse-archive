# Methods for thin skull bone segmentation

**Topic ID**: 36367
**Date**: 2024-05-24
**URL**: https://discourse.slicer.org/t/methods-for-thin-skull-bone-segmentation/36367

---

## Post #1 by @ThomasVanParys (2024-05-24 08:43 UTC)

<p>Hello,<br>
I would like to know the best method of capturing fine/thin bone elements in the occipital/craniofacial region of a segmented skull model.</p>
<p>I have a whole-body DICOM CT scan (from the NMDID), which I have cropped to only include the head-neck region, slice thickness: 1mm.<br>
Here I have used the <em>grayscale model maker</em> (threshold: 400):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/195f0b4c924cf24fed3093c4365cc3fdc70f8178.jpeg" data-download-href="/uploads/short-url/3CrzcX6ZiF75SR45aZFrT1vXlEY.jpeg?dl=1" title="Screenshot 2024-05-24 093949" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/195f0b4c924cf24fed3093c4365cc3fdc70f8178_2_690x374.jpeg" alt="Screenshot 2024-05-24 093949" data-base62-sha1="3CrzcX6ZiF75SR45aZFrT1vXlEY" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/195f0b4c924cf24fed3093c4365cc3fdc70f8178_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/195f0b4c924cf24fed3093c4365cc3fdc70f8178_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/195f0b4c924cf24fed3093c4365cc3fdc70f8178_2_1380x748.jpeg 2x" data-dominant-color="BCBEBF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-24 093949</span><span class="informations">1920×1043 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It has come out reasonably well on the first run, except for finer elements with a threshold similar to surrounding soft tissue.<br>
Any methods or advice would be most welcome.<br>
My (ambitious) goal is to have models good enough for skull base segmentation and morphometric analysis of sphenoid size and shape.</p>
<p>Basic CT Bone volume rendering shows reasonably good detail, with skull suture lines:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53b9dceea6a1cb12c4e600a186eb18ed1e4a9d03.jpeg" data-download-href="/uploads/short-url/bWFQ3TENVLhx6BHlYHMKCCqUNUf.jpeg?dl=1" title="Screenshot 2024-05-24 095329" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53b9dceea6a1cb12c4e600a186eb18ed1e4a9d03_2_690x375.jpeg" alt="Screenshot 2024-05-24 095329" data-base62-sha1="bWFQ3TENVLhx6BHlYHMKCCqUNUf" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53b9dceea6a1cb12c4e600a186eb18ed1e4a9d03_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53b9dceea6a1cb12c4e600a186eb18ed1e4a9d03_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53b9dceea6a1cb12c4e600a186eb18ed1e4a9d03_2_1380x750.jpeg 2x" data-dominant-color="C0A8B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-24 095329</span><span class="informations">1920×1045 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you.</p>

---

## Post #2 by @muratmaga (2024-05-24 14:08 UTC)

<p>I think you are on the right track. To preserve thin bone like orbital walls, or wings of sphenoid, you probably need to increase the resolution of the segmentation (oversampling) using the Segment Geometry option.</p>
<p>Due to partial volume effect thin bones will likely have lower intensity values than the other parts of the bone, so chances are you need to manually fix those using a slightly lower threshold range and using the paint brush to selectively add them to the rest of the skull.</p>

---

## Post #4 by @ThomasVanParys (2024-05-24 14:50 UTC)

<p>Thank you for the advice.<br>
The issue may be in the (PM)CT scan quality themselves, and not suitable for such analysis. I would use mCT skulls, but larger datasets for a study of sexual dimorphism is very difficult. If you know of any human mCT skull datasets, that would be amazing.<br>
I would segment the sphenoid structure manually from the 2D slices, but this takes considerable time and anatomical skill, on top of relatively poor pixel quality close-up. A similar result is achieved using Segment Geometry and Thresholding:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfa8e68ce7c142207f34c3de4d8da6ac4f512b8c.jpeg" data-download-href="/uploads/short-url/tD2HF21sySlgiAu7PI1YXRyckXi.jpeg?dl=1" title="Screenshot 2024-05-24 154453" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfa8e68ce7c142207f34c3de4d8da6ac4f512b8c_2_690x375.jpeg" alt="Screenshot 2024-05-24 154453" data-base62-sha1="tD2HF21sySlgiAu7PI1YXRyckXi" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfa8e68ce7c142207f34c3de4d8da6ac4f512b8c_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfa8e68ce7c142207f34c3de4d8da6ac4f512b8c_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfa8e68ce7c142207f34c3de4d8da6ac4f512b8c_2_1380x750.jpeg 2x" data-dominant-color="7F8182"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-24 154453</span><span class="informations">1920×1045 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I have 200 scans (100 males, 100 females), so some semi-automated function may be needed. I wanted to landmark a template specimen, then use ALPACA and GPA for a GM workflow.<br>
Thank you.</p>

---

## Post #5 by @muratmaga (2024-05-24 15:54 UTC)

<aside class="quote no-group" data-username="ThomasVanParys" data-post="4" data-topic="36367">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ThomasVanParys:</div>
<blockquote>
<p>. I would use mCT skulls,</p>
</blockquote>
</aside>
<p>Yes, that would be nice. I am not aware of any mostly, because even at 0.1mm resolution each dataset would be tens of gigabytes in size, and most people can’t really use such large datasets, and definitely you would be able to find hundreds.</p>
<p>As I recall NMDID scans have multiple different acquisitions, each of which has different resolution. A few datasets I looked at had 0.5x0.5x0.625mm resolution, which should be sufficient for your purposes. You may want to talk to them to see if you can query the samples for resolution.</p>

---

## Post #6 by @ThomasVanParys (2024-05-24 16:53 UTC)

<p>Thank you</p>
<p>Although their head-neck scanning protocol only mentions 1mm thickness ([<a href="https://nmdid.unm.edu/docs/CT_OMI_protocol.pdf" rel="noopener nofollow ugc">https://nmdid.unm.edu/docs/CT_OMI_protocol.pdf</a>]) I will definitely approach them.</p>
<p>If I do have a good bone threshold that has segmented the skull well, what is the best method for further sphenoid segmentation? Ideally I want clear suture lines to help distinguish it.<br>
Volume rendering for landmarking each model isn’t really an option if I want to use ALPACA either, I assume.</p>
<p>Tom</p>

---

## Post #7 by @muratmaga (2024-05-24 17:12 UTC)

<p>I would download the head/neck bone reconstruction (d in the table below), resample isotopically to 0.5mm and then segment to see what you get:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91e9725b020fc01ef18ca43bee3f287e9bcd0f3f.png" alt="image" data-base62-sha1="kONocWU0jyADJzciX17yrWXdQzJ" width="474" height="165"></p>
<p>You can do the landmarking on volume rendering, there is no problem there. However, for ALPACA you need extract 3D models.</p>

---

## Post #8 by @ThomasVanParys (2024-05-28 15:53 UTC)

<p>Thank you for the advice.<br>
I have since been recommended this CT skull database: [<a href="https://www.lynncopes.com/human-ct-scans.html" class="inline-onebox" rel="noopener nofollow ugc">Human CT scans</a>]</p>
<p>They are better resolution than the NMDID head-neck scans, and I have isotopically resampled the volumes (from 0.468 to 0.234).<br>
Here is what the stitched volumes look like at a glance:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2920d82cc8d291e18b2bba3b3b45ac288e2a539.jpeg" data-download-href="/uploads/short-url/rLfxQqZ2DbOJhLngbCNtLUkWcOZ.jpeg?dl=1" title="Screenshot 2024-05-28 163542" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2920d82cc8d291e18b2bba3b3b45ac288e2a539_2_690x374.jpeg" alt="Screenshot 2024-05-28 163542" data-base62-sha1="rLfxQqZ2DbOJhLngbCNtLUkWcOZ" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2920d82cc8d291e18b2bba3b3b45ac288e2a539_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2920d82cc8d291e18b2bba3b3b45ac288e2a539_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2920d82cc8d291e18b2bba3b3b45ac288e2a539_2_1380x748.jpeg 2x" data-dominant-color="B8B7D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-28 163542</span><span class="informations">1920×1041 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And here is a quick skull threshold/segmentation, with sufficient skull base detail that I can crop further and segment the sphenoid bone. Manually segmenting each specimen (200) is slower, but should produce the best results for my landmarking procedure:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e5cd5c24da65168d89d717f6ae9354c81e8f15e.jpeg" data-download-href="/uploads/short-url/dsLMnpwJgucbLJHhfPhCWezEdPw.jpeg?dl=1" title="Screenshot 2024-05-28 164258" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e5cd5c24da65168d89d717f6ae9354c81e8f15e_2_690x374.jpeg" alt="Screenshot 2024-05-28 164258" data-base62-sha1="dsLMnpwJgucbLJHhfPhCWezEdPw" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e5cd5c24da65168d89d717f6ae9354c81e8f15e_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e5cd5c24da65168d89d717f6ae9354c81e8f15e_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e5cd5c24da65168d89d717f6ae9354c81e8f15e_2_1380x748.jpeg 2x" data-dominant-color="BFBDCC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-28 164258</span><span class="informations">1920×1043 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My landmarking procedure for the sphenoid bone is also shown below, I hope this will provide sufficient coverage of the 3D morphology (it’s probably overkill):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/277b2706dabcd60eb5edb7dbb069206bbc0eadc9.png" data-download-href="/uploads/short-url/5Dgtp1lavk8Soxju02hO4sj9AMN.png?dl=1" title="Screenshot 2024-05-28 165044" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/277b2706dabcd60eb5edb7dbb069206bbc0eadc9.png" alt="Screenshot 2024-05-28 165044" data-base62-sha1="5Dgtp1lavk8Soxju02hO4sj9AMN" width="644" height="500" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-28 165044</span><span class="informations">881×683 30.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you!<br>
Tom</p>

---

## Post #9 by @Inka_Saraswati (2024-09-26 10:19 UTC)

<p>I’m sorry for hijacking the thread but I have a related question.</p>
<p>I also have a similar task to segment skulls with a lot of thin bone from different CBCT machines which have various voxel size. I want to preprocess data for standardising the voxel sizes.</p>
<p>How do you determine ideal resampled voxel size (and while we’re at it, is there any resampling algorithm that is more recommended for bone segmentation)?</p>
<p>Thank you.</p>

---

## Post #10 by @Basil_Berinyuy (2024-11-26 13:53 UTC)

<p>Dear Tom,<br>
May I ask if the 200 CT datasets (100 male, 100 female) you mentioned are open source data?. We have a project currently dealing with automated bone reconstruction in maxillofacialsurgery and for this we need head CT scans of patients with healthy skulls. If not could you recommend any other open source database?<br>
Thanks a lot in advance for your response</p>

---

## Post #11 by @ThomasVanParys (2024-11-26 14:08 UTC)

<p>The NMDID PMCT data can be applied for using an official university/research institute email, please see the website for more info: <a href="https://nmdid.unm.edu/" rel="noopener nofollow ugc">https://nmdid.unm.edu/</a>.</p>
<p>The following data you don’t need to apply for, there may be a CT head-neck dataset in here: <a href="https://www.cancerimagingarchive.net/browse-collections/" class="inline-onebox" rel="noopener nofollow ugc">Browse Collections - The Cancer Imaging Archive (TCIA)</a>.</p>
<p>Best Wishes,<br>
Tom</p>

---
