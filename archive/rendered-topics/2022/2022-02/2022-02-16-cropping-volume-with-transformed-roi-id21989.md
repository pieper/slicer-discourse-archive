# Cropping volume with transformed ROI

**Topic ID**: 21989
**Date**: 2022-02-16
**URL**: https://discourse.slicer.org/t/cropping-volume-with-transformed-roi/21989

---

## Post #1 by @hourglassnam (2022-02-16 05:08 UTC)

<p>Dear community,</p>
<p>I have two questions on creating py script for ROI and using it for cropping volume with Image stack.</p>
<p>Issue <span class="hashtag">#1</span><br>
My goal is to create ROI for each of the ten segments I have and make separate files with cropped volume.<br>
So for the first part, I found <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-keyboard-shortcut-for-toggling-sphere-brush-for-paint-and-erase-effects" rel="noopener nofollow ugc">this code</a><br>
When I tried using it on py interactor, it seems to me that the for loops does not end.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fd56e8aa6c3bbc21a4104a4ce2fdd2f37391a41.png" data-download-href="/uploads/short-url/96Hm56Ik7p0aaX22SDqZbHj0L1T.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fd56e8aa6c3bbc21a4104a4ce2fdd2f37391a41_2_690x213.png" alt="image" data-base62-sha1="96Hm56Ik7p0aaX22SDqZbHj0L1T" width="690" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fd56e8aa6c3bbc21a4104a4ce2fdd2f37391a41_2_690x213.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fd56e8aa6c3bbc21a4104a4ce2fdd2f37391a41_2_1035x319.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fd56e8aa6c3bbc21a4104a4ce2fdd2f37391a41_2_1380x426.png 2x" data-dominant-color="F6F6FF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3817×1180 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
The script works appropriately when I use it for one segment.<br>
I tried to break the loop, but it did not work.<br>
Can anyone tell me what I am doing wrong?</p>
<p>Issue <span class="hashtag">#2</span><br>
I created annotation ROI and markup ROI to see which one works better with the ImageStack, but the results were not what I expected.<br>
Using Annotation ROI gave me output volume outside the actual CT image, which is probably where the ROI box was before the transform.<br>
Markup ROI gave me output volume that does not match the actual ROI.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b75864e2dc2c2c539590da1638db76337fbcbf6e.png" data-download-href="/uploads/short-url/q9WL9yc9SagPj0f35Wj93UVZk98.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b75864e2dc2c2c539590da1638db76337fbcbf6e_2_602x500.png" alt="image" data-base62-sha1="q9WL9yc9SagPj0f35Wj93UVZk98" width="602" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b75864e2dc2c2c539590da1638db76337fbcbf6e_2_602x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b75864e2dc2c2c539590da1638db76337fbcbf6e_2_903x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b75864e2dc2c2c539590da1638db76337fbcbf6e_2_1204x1000.png 2x" data-dominant-color="635E75"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×1590 404 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Is there any way to solve this problem?</p>
<p>*I use Image stack because I work first in preview mode to separate each sample then work in full resolution for the segmentation process.</p>
<p>Thank you always for your valuable comments.</p>

---

## Post #2 by @muratmaga (2022-02-16 05:41 UTC)

<aside class="quote no-group" data-username="hourglassnam" data-post="1" data-topic="21989">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hourglassnam/48/11796_2.png" class="avatar"> hourglassnam:</div>
<blockquote>
<p>have two questions on creating py script for ROI and using it for cropping volume with Image stack.</p>
</blockquote>
</aside>
<p>Is your final goal to save all those 10 segments as individual volumes? If so, splitVolume effect of segment editor would do that without any scripting.</p>

---

## Post #3 by @hourglassnam (2022-02-16 06:37 UTC)

<p>That works way better than the mess I’ve been doing…<br>
Thank you so much for your suggestion!</p>
<p>Can I ask you one more question?<br>
Is there any way to change the existing segment pixel?<br>
The segment I create is in 0.028mm pixel, but I want to smooth this out to 0.007mm after changing the image to a higher resolution.<br>
I have been just resegmenting the sample, and I have a strong feeling that there must be a better method.</p>

---

## Post #4 by @muratmaga (2022-02-16 07:19 UTC)

<aside class="quote no-group" data-username="hourglassnam" data-post="3" data-topic="21989">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hourglassnam/48/11796_2.png" class="avatar"> hourglassnam:</div>
<blockquote>
<p>The segment I create is in 0.028mm pixel, but I want to smooth this out to 0.007mm</p>
</blockquote>
</aside>
<p>You mean you replaced your master volume with a higher resolution one? You can modify the segment geometry an do oversampling of 4. But that will increase your memory consumption quite a bit (64 times to be precise), which may create out memory errors or make everything go slower. If your goal is only splitting these segments at high resolution, then in splitVolume just change the matter volume to the high resolution one.</p>

---

## Post #5 by @hourglassnam (2022-02-17 05:48 UTC)

<p>I am sorry, I think I am not being clear enough.<br>
So after your advice, I used image stack to switch my volume to a higher resolution one and then used splitVolume to split them.<br>
This worked perfectly.<br>
My question is on after splitting the volume and saving them separately.<br>
I wondered if I could reuse the segment created in 0.028mm pixels and edit them in 0.007mm pixels.o<br>
I have changed the master volume of the existing segmentation node, but when I tried to edit the segments, they were still in 0.028mm pixel.<br>
I was able to edit the segments in 0.007 mm pixels after moving them to a new segmentation node.<br>
So I was wondering if this was normal.<br>
Is there any way to edit the segments without moving them to a new segmentation node?</p>

---

## Post #6 by @muratmaga (2022-02-17 06:51 UTC)

<p>I am also not very clear on what you are trying to do.</p>
<p>If you already split your segments, and while doing that if you chose the master volume to be one with 0.007 mm resolution, your newly derived individual volumes should be resolution. In other words it doesn’t matter if the segmentation is done 0.028 mm (provided that you are still capturing the detail you are need).</p>
<p>Regardless, you can increase the resolution by using the oversampling option of the segment geometry setting. I was just trying to make you aware of increased memory usage.</p>

---
