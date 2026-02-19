---
topic_id: 4676
title: "Segment Has Invisible Bounds Smaller Than Master Volume"
date: 2018-11-07
url: https://discourse.slicer.org/t/4676
---

# Segment has invisible bounds smaller than master volume

**Topic ID**: 4676
**Date**: 2018-11-07
**URL**: https://discourse.slicer.org/t/segment-has-invisible-bounds-smaller-than-master-volume/4676

---

## Post #1 by @kayarre (2018-11-07 22:07 UTC)

<p>when I am editing a segment there appears to be an issue with the invisible ROI that bounds the limits of what is included. I can’t figure out how to make this invisible roi larger.</p>
<p>this picture depicts an exaggerated case, its obvious that its bounded by a box.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/697305a8fe1b1aa705b409f6ec2adc028a443a91.jpeg" data-download-href="/uploads/short-url/f2QzdTwJ3HqO68zINnolHZDHOtb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/697305a8fe1b1aa705b409f6ec2adc028a443a91_2_690x384.jpeg" alt="image" data-base62-sha1="f2QzdTwJ3HqO68zINnolHZDHOtb" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/697305a8fe1b1aa705b409f6ec2adc028a443a91_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/697305a8fe1b1aa705b409f6ec2adc028a443a91.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/697305a8fe1b1aa705b409f6ec2adc028a443a91.jpeg 2x" data-dominant-color="A19CB4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">807×450 85.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I think the problem is that when you import from a model it sets the pixel size a default, so you get what looks like a nicer resolution, but then the pixel dimensions aren’t large enough.</p>

---

## Post #2 by @cpinter (2018-11-07 22:56 UTC)

<p>The master volume determines the editable area. The volume that is set when you add the first segment is the one that’s used for the geometry. You can either start it over, or change the geometry using the small box icon next to the master volume selector. Available in 4.10.</p>

---

## Post #3 by @kayarre (2018-11-08 17:34 UTC)

<p>I tried this and it appeared to not let me edit it directly, I would like to be able to “simply?” increase the geometry size? I can change the spacing of the source geometry but not the dimensions or origin.</p>
<p>I tried the upsampling from a different volume to match the same spacing and slicer appears to freeze, or die (will investigate steps to reproduce further)</p>

---

## Post #4 by @cpinter (2018-11-08 17:43 UTC)

<p>Segmentation is about identifying regions in a volume. It doesn’t make sense to paint outside the image you want to segment. So simply choose the volume you’re segmenting and the editable area will match it.</p>

---

## Post #5 by @kayarre (2018-11-08 17:48 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> but the resolution is not the same.</p>
<p>on import:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8ffb7a5c0007f0a3b42daee3870cf21a0ba6dd4d.jpeg" alt="image" data-base62-sha1="kxJ4aP8I7jExpdFcl7wIFppJYW9" width="495" height="367"></p>
<p>on modifying the source geometry:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5058c03ef0a109960140c158f4fbee18c2bff77.jpeg" alt="image" data-base62-sha1="s6VWEa4e1bbMBpyqpWOPwVTmWXB" width="495" height="367"></p>
<p>I am thinking that the import giving this refined “looking” mask is setting my expectations to high.</p>
<p><strong>My work around:</strong></p>
<ul>
<li>export the segmentation to a labelmap</li>
<li>crop volume and expand the ROI to create new volume that is bigger than the bounds of the imported segmentation.</li>
<li>Threshold this label map  such that the whole of the image is included</li>
<li>import this label map into the segmentation node</li>
<li>apply something that will grow the region, margin, hollow… etc</li>
<li>observe the bounds of the segmentation are larger than initial import segmentation</li>
</ul>

---

## Post #6 by @lassoan (2018-11-08 18:19 UTC)

<p>If you use a recent Slicer version, you can set very high resolution for your internal labelmap representation and set any region size. To specify an arbitrary region size, create an annotation ROI node and choose that as “Source geometry” in the Segmentation geometry popup.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce6778641a4a527c146377c1a7a7d1fd13414f9.png" data-download-href="/uploads/short-url/A5g5Vsqv2RuOsZKEYeQPJzDYq2B.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce6778641a4a527c146377c1a7a7d1fd13414f9_2_690x279.png" alt="image" data-base62-sha1="A5g5Vsqv2RuOsZKEYeQPJzDYq2B" width="690" height="279" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce6778641a4a527c146377c1a7a7d1fd13414f9_2_690x279.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce6778641a4a527c146377c1a7a7d1fd13414f9_2_1035x418.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce6778641a4a527c146377c1a7a7d1fd13414f9.png 2x" data-dominant-color="C4C6C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1036×419 66 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @cpinter (2018-11-08 18:19 UTC)

<aside class="quote no-group" data-username="kayarre" data-post="5" data-topic="4676">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>but the resolution is not the same</p>
</blockquote>
</aside>
<p>You need to use oversampling in the geometry widget. Choose the volume and increase oversampling to 2 or more if you need. Then the bounding box will be the same but the resolution will be higher.</p>

---

## Post #8 by @cpinter (2018-11-08 18:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="4676">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>annotation ROI node</p>
</blockquote>
</aside>
<p>However you have a volume node so it’s much simpler to use that with oversampling and possibly isotropic spacing.</p>

---

## Post #9 by @kayarre (2018-11-08 18:28 UTC)

<aside class="quote no-group quote-modified" data-username="cpinter" data-post="7" data-topic="4676">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<blockquote>
<p>but the resolution is not the same</p>
</blockquote>
<p>You need to use oversampling in the geometry widget. Choose the volume and increase oversampling to 2 or more if you need. Then the bounding box will be the same but the resolution will be higher.</p>
</blockquote>
</aside>
<p>I tried this but in some instance it causes slicer to crash. (still need to refine those steps to reproduce)</p>

---

## Post #10 by @lassoan (2018-11-08 18:32 UTC)

<p>The only limit to segmentation’s resolution is the amount of memory you make available (on Windows you can increase virtual memory in your computer settings, on Linux it is called swap size, on Mac you need to have plenty of free disk space). If a process runs out of memory, it crashes. So, as a general rule I would recommend to have 10x more memory available than your data set size. If you set a small voxel size then you may need tens of GB of memory - preferably physical RAM, but at least virtual memory.</p>

---

## Post #11 by @kayarre (2018-11-08 18:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> That makes sense and is a possible cause, I do have a 64Gb memory machine so I guess I would be a little surprised by that, but I haven’t checked and would make sense. (It’s amazing how easy it is to run out of memory these days)</p>
<p>also: Thank you so much for your support <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/cpinter">@cpinter</a>, You have been super responsive and helpful. I really appreciate all the hard work and help. most and best help I have gotten from any open source software out there.</p>

---
