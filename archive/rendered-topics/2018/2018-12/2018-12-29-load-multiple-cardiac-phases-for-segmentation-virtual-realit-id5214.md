---
topic_id: 5214
title: "Load Multiple Cardiac Phases For Segmentation Virtual Realit"
date: 2018-12-29
url: https://discourse.slicer.org/t/5214
---

# Load multiple cardiac phases for segmentation/virtual reality

**Topic ID**: 5214
**Date**: 2018-12-29
**URL**: https://discourse.slicer.org/t/load-multiple-cardiac-phases-for-segmentation-virtual-reality/5214

---

## Post #1 by @sarvpriya1985 (2018-12-29 01:40 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.10<br>
Expected behavior: See cine motion of all phases in volume render/segmentation and then virtual reality<br>
Actual behavior: Not working<br>
Hello everyone,</p>
<p>I read the prior discussions about loading multiple volumes. I loaded a dicom file of CT Heart with 10 phases in order to segment them or see them in volume rendering. But after loading the file, all i see is one volume and have used sequences and sequence browser. But I am unable to work any further. My queries:</p>
<ol>
<li>How to load the multiple volume and play them in motion.</li>
<li>How to see the cine motion in volume rendering and then see the same in virtual reality.</li>
<li>If i need to segment the multiple phases using threshold, how to do that. I cant figure that out (whether to do that in one phase or all phases.</li>
</ol>
<p>Would appreciate everyone’s help.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @lassoan (2018-12-29 05:24 UTC)

<p>This post should clarify things: <a href="https://discourse.slicer.org/t/single-series-with-multiple-frames-separate-out/2285/2?u=lassoan" class="inline-onebox">Single series with multiple frames, separate out?</a></p>
<p>Let us know if you still have questions.</p>

---

## Post #3 by @sarvpriya1985 (2018-12-29 14:43 UTC)

<p>Hi Andras,<br>
Thanks for helping.<br>
I was able to load the volume as multiple phrase.<br>
But I am unable to segment multiple frames. What I am trying to do is the same as Nicholas had pointed out. Playing all frames as cine or animation.</p>
<ol>
<li>Wish to segment all 10 phases, so I may play them as an animation in 3D.</li>
<li>Then play the same animation/cine in virtual reality.</li>
<li>If I could do the same  in volume rendering.</li>
</ol>
<p>I would appreciate everyones help. My next step is to see how can I bring an external device into the frame and play it like that video of pedicle screw insertion.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #4 by @lassoan (2018-12-29 15:10 UTC)

<aside class="quote no-group" data-username="sarvpriya1985" data-post="3" data-topic="5214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>Wish to segment all 10 phases, so I may play them as an animation in 3D.</p>
</blockquote>
</aside>
<p>See instructions for how to create a segmentation sequence here: <a href="https://discourse.slicer.org/t/segmentation-of-multi-volume-sequence/5187/2" class="inline-onebox">Segmentation of multi volume sequence - #2 by lassoan</a></p>
<aside class="quote no-group" data-username="sarvpriya1985" data-post="3" data-topic="5214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>Then play the same animation/cine in virtual reality.</p>
</blockquote>
</aside>
<p>4D animation works the same way in virtual reality as on the desktop screen. You just need to click the virtual reality button to see content in virtual reality.</p>
<aside class="quote no-group" data-username="sarvpriya1985" data-post="3" data-topic="5214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>If I could do the same in volume rendering</p>
</blockquote>
</aside>
<p>Volume rendering works the same way in virtual reality as on the desktop screen. You may click the “optimize” button on the virtual reality toolbar to improve volume rendering performance settings.</p>

---

## Post #5 by @sarvpriya1985 (2018-12-29 16:36 UTC)

<ul>
<li>
<p>Create a new Segmentation node (e.g., by segmenting image at one timepoint): _I created a first segmentation on phase 0 of volume.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39d1d8657c707fa2d5ee94c0e632f928bb888641.jpeg" data-download-href="/uploads/short-url/8fuO3ePb9Ecn3HKWlduuZ1cxr8d.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39d1d8657c707fa2d5ee94c0e632f928bb888641_2_690x354.jpeg" alt="Capture" data-base62-sha1="8fuO3ePb9Ecn3HKWlduuZ1cxr8d" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39d1d8657c707fa2d5ee94c0e632f928bb888641_2_690x354.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39d1d8657c707fa2d5ee94c0e632f928bb888641_2_1035x531.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39d1d8657c707fa2d5ee94c0e632f928bb888641_2_1380x708.jpeg 2x" data-dominant-color="C8CBCE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1920×986 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> _</p>
</li>
<li>
<p>Go to Sequence browser module: Ws able to do that</p>
</li>
<li>
<p>Click the green “+” button next to “Create new sequence”. This creates a new sequence that will store the segmentation for each timepoint.: “Done”</p>
</li>
<li>
<p>Choose your segmentation node in the “Proxy node” column in the table (last row). This indicates that this sequence will store states of the chosen segmentation node.: " Don’t know which node to pick."</p>
</li>
<li>
<p>Check “Save changes” checkbox to allow modifying the sequence by editing the segmentation node." Can do but not sure which segmentation node to pick".</p>
</li>
</ul>
<p>"Also when i finished segmentation in phase 0, it was automatically (not by me) transferred to all the phases but was not correct. How can I avoid that. Or if i can propagate them correctly.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5d0b165e212a9472ab6d81a893cee31695822e2.jpeg" data-download-href="/uploads/short-url/uvuP4JvHXRDBbbW1GQL3lpgVR50.jpeg?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5d0b165e212a9472ab6d81a893cee31695822e2_2_690x356.jpeg" alt="Capture1" data-base62-sha1="uvuP4JvHXRDBbbW1GQL3lpgVR50" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5d0b165e212a9472ab6d81a893cee31695822e2_2_690x356.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5d0b165e212a9472ab6d81a893cee31695822e2_2_1035x534.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5d0b165e212a9472ab6d81a893cee31695822e2_2_1380x712.jpeg 2x" data-dominant-color="C8CBCD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">1915×989 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I think I am not able to follow the commands properly for this animation, so would appreciate a little detailed and step approach.</p>
<p>Would appreciate help.<br>
Thanks again,<br>
Sarv</p>

---

## Post #6 by @lassoan (2018-12-29 17:13 UTC)

<aside class="quote no-group" data-username="sarvpriya1985" data-post="5" data-topic="5214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>Choose your segmentation node in the “Proxy node” column in the table (last row). This indicates that this sequence will store states of the chosen segmentation node.: " Don’t know which node to pick."</p>
</blockquote>
</aside>
<p>“Choose your segmentation node” means pick the segmentation node. [quote=“sarvpriya1985, post:5, topic:5214”]<br>
when i finished segmentation in phase 0, it was automatically (not by me) transferred to all the phases but was not correct. How can I avoid that. Or if i can propagate them correctly<br>
[/quote]</p>
<p>When you switch frames, previous segmentation is automatically propagated to the current frame. If you want to start from an empty segmentation, go through the sequence before you start segmenting.</p>
<p>You can also run Sequence Registration to compute a displacement field that can be used to warp the segmentation of one frame to all other frames.</p>

---

## Post #7 by @sarvpriya1985 (2018-12-29 21:29 UTC)

<p>Thanks Andras.<br>
I am still left with the issue of animation playing and accurate segmenting.<br>
I used sequence registration and transform the segments but they were all inaccurate. In addition, whatever segments I got, I went back to segment editor and created 3d model. But the model doesnt show any cine/animation.<br>
Attaching a screenshot of sequence registration that I did.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c57c48ec9ac11351ef5a9261bc437644307f3efb.jpeg" data-download-href="/uploads/short-url/sb2l7TvfzAbNRdy8Yj1MAG2C25d.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c57c48ec9ac11351ef5a9261bc437644307f3efb_2_690x360.jpeg" alt="Capture" data-base62-sha1="sb2l7TvfzAbNRdy8Yj1MAG2C25d" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c57c48ec9ac11351ef5a9261bc437644307f3efb_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c57c48ec9ac11351ef5a9261bc437644307f3efb_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c57c48ec9ac11351ef5a9261bc437644307f3efb_2_1380x720.jpeg 2x" data-dominant-color="CACDCE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1916×1000 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
So if I say again, I would need two things.</p>
<ol>
<li>Accurate segmentation of each phase. 2. And then play it as animation.<br>
I have tried my best but would certainly need some additional help.</li>
</ol>
<p>Thanks,<br>
Sarv</p>

---

## Post #8 by @sarvpriya1985 (2018-12-30 02:58 UTC)

<p>Hi Andras,<br>
I would again tell how I am doing and where I am failing.<br>
I am attaching the screenshots in sequence that I was told. But I could not go beyond creating a new sequence. When I click play, no cine motion is seen.<br>
Even after using sequence registration, there is error message coming.</p>
<p>Sequence of my events:</p>
<ol>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c2baba3123c63b934eb0b11bba0f71bb26ef796.jpeg" data-download-href="/uploads/short-url/d9nuqEkkbCw5epRPJ6Y9DKRxwq2.jpeg?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c2baba3123c63b934eb0b11bba0f71bb26ef796_2_690x354.jpeg" alt="Capture1" data-base62-sha1="d9nuqEkkbCw5epRPJ6Y9DKRxwq2" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c2baba3123c63b934eb0b11bba0f71bb26ef796_2_690x354.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c2baba3123c63b934eb0b11bba0f71bb26ef796_2_1035x531.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c2baba3123c63b934eb0b11bba0f71bb26ef796_2_1380x708.jpeg 2x" data-dominant-color="C8CBCE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">1916×984 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></li>
<li>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4865f1ddc845c8166d2bd474da042198b33c5217.jpeg" alt="capture%206" data-base62-sha1="aksNcvX2Nd9WM0rvk6GV7yPijll" width="640" height="480"> (picked this segmentation node)</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8b37fffe5b8e25576871f62d79a1f529a6bb5a0.jpeg" data-download-href="/uploads/short-url/uV1I3vurECKk0cARInznQCOYmhG.jpeg?dl=1" title="Capture5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d8b37fffe5b8e25576871f62d79a1f529a6bb5a0_2_690x357.jpeg" alt="Capture5" data-base62-sha1="uV1I3vurECKk0cARInznQCOYmhG" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d8b37fffe5b8e25576871f62d79a1f529a6bb5a0_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d8b37fffe5b8e25576871f62d79a1f529a6bb5a0_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d8b37fffe5b8e25576871f62d79a1f529a6bb5a0_2_1380x714.jpeg 2x" data-dominant-color="C8CBCB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture5</span><span class="informations">1913×992 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></li>
<li>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78cab57c00125f3b210d4559491f0e6dbe86b51c.jpeg" data-download-href="/uploads/short-url/hezB5Wd7REfWUvLVMTBSuo0pGMs.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78cab57c00125f3b210d4559491f0e6dbe86b51c_2_690x355.jpeg" alt="Capture" data-base62-sha1="hezB5Wd7REfWUvLVMTBSuo0pGMs" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78cab57c00125f3b210d4559491f0e6dbe86b51c_2_690x355.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78cab57c00125f3b210d4559491f0e6dbe86b51c_2_1035x532.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78cab57c00125f3b210d4559491f0e6dbe86b51c_2_1380x710.jpeg 2x" data-dominant-color="C9CBCE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1918×989 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
<br>
I don’t know at which step I am doing wrong. Appreciate all the help.</li>
</ol>
<p>Thanks,<br>
Sarv</p>

---

## Post #9 by @lassoan (2018-12-30 02:59 UTC)

<p>Thanks, the screenshot helps. To set up registration correctly:</p>
<ol>
<li>Registration is computed from the “fixed frame index”-th frame. Make sure you choose the segmented frame.</li>
<li>Output volume sequence must not be the same as output transform sequence.</li>
<li>Use “generic (all)” preset first. If registration works with that then you may try more advanced, specialized presets.</li>
</ol>

---

## Post #10 by @lassoan (2018-12-30 03:01 UTC)

<p>In step 3 you chose a the master volume node as proxy node. You need to choose a segmentation node instead.</p>

---

## Post #11 by @sarvpriya1985 (2018-12-30 04:57 UTC)

<p>Thanks Andras,<br>
It all worked fine till phase 9 when I got this error message. How long should I expect to finish registration (it took about 20 minutes to finish phase 9 before it got stuck.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26ac8cd78143923252715a57d47842ea2420765d.jpeg" data-download-href="/uploads/short-url/5w7PvY20wN58hPwM3CGRBBjkOIZ.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26ac8cd78143923252715a57d47842ea2420765d_2_690x357.jpeg" alt="Capture" data-base62-sha1="5w7PvY20wN58hPwM3CGRBBjkOIZ" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26ac8cd78143923252715a57d47842ea2420765d_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26ac8cd78143923252715a57d47842ea2420765d_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26ac8cd78143923252715a57d47842ea2420765d_2_1380x714.jpeg 2x" data-dominant-color="CACDCF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1918×993 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also how can I segment each frame individually as I am not sure since this registration takes such long and may get stuck.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #12 by @sarvpriya1985 (2018-12-30 04:59 UTC)

<p>Also as these frames have lot of motion. It would be better if I could segment them separately as registration may fail due to excessive motion in between slices.</p>
<p>Sarv</p>

---

## Post #13 by @lassoan (2018-12-30 14:33 UTC)

<p>“bad allocation” error message means that you’ve run out of memory. Crop and/or resample your input image sequence using Sequence resample module or add more memory (upgrade your computer with more physical RAM or configure it to have more virtual memory).</p>

---

## Post #14 by @sarvpriya1985 (2018-12-30 15:56 UTC)

<p>Hi Andras<br>
I have a 16gb memory. Should not that be enough. I am not aware how much virtual memory I have.</p>
<p>Thanks<br>
Sarv</p>

---

## Post #15 by @sarvpriya1985 (2018-12-30 16:42 UTC)

<p>Is there a way i can share the multiphase file and see if you or someone else are able to recreate that animation movie. In that way I can learn the fine steps in a little more detail.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #16 by @lassoan (2018-12-30 17:43 UTC)

<aside class="quote no-group" data-username="sarvpriya1985" data-post="15" data-topic="5214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>Is there a way i can share the multiphase file</p>
</blockquote>
</aside>
<p>You can upload to Dropbox, OneDrive, or Google drive and post the link. Make sure to remove patient information.</p>
<p>16GB RAM is not too much, but OK (things will be slow if you don’t reduce image size). You must increase virtual memory size in Wibdiws system settings - probably 50GB will be enough.</p>

---

## Post #17 by @sarvpriya1985 (2018-12-30 19:44 UTC)

<p>Hi Andras,<br>
This is the link. Pls see if you could let me know a little more about my wrongdoing in creating this animation.</p>
<p>Thanks,<br>
Sarv<a href="https://iowa-my.sharepoint.com/:f:/g/personal/spriya_uiowa_edu/EuSlc2OcnvZNuAZt8OR2jFQBD1vD_f2bnr8Q9S42Ga9sqw?e=sQsLAn" rel="nofollow noopener">Multiphase cardiac CT</a></p>

---

## Post #18 by @sarvpriya1985 (2019-01-04 21:15 UTC)

<p>Hi Andras,<br>
Did you get chance to llok at the multiphase CT file that I shared. Inspite of all prior discussions, I am still struggling to segment all phases and play an animation. Would appreciate all help.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #19 by @lassoan (2019-01-05 19:01 UTC)

<p>I’ve tried the registration and found the followings:</p>
<ul>
<li>Image size is quite large, therefore I used “Crop volume sequence” module to crop and resample the image (used 1.7x isotropic spacing; resulting in an approximately 100x80x80 volume)</li>
<li>Segmented frame index=9 using thresholding and then used Sequence registration module (selected same frame index = 9 as fixed frame, “fixed frame to moving frames” direction). Applied output transform to segmentation. Registration result was not accurate enough. Probably the registration is hard because the difference between frames is quite significant (due to motion and difference in contrast distribution).</li>
<li>Tested “3D CT multi-contrast (cardiac)” preset (set both start frame index and end frame index values to 2 so that I don’t have to wait for registration of 10 frames) and I found that the registration is much better (maybe good enough), it was just very long - took almost 15 minutes. This indicates that the registration results can be improved by tuning registration parameters.</li>
</ul>
<p>If you are interested in developing a good registration preset that can be used to register such image sequences then I think “3D CT multi-contrast (cardiac)” is a good starting point. Try to simplify (reduce number of steps, etc) and see if you can make the registration faster without making registration results worse. You may ask help on <a href="https://groups.google.com/forum/#!categories/elastix-imageregistration/elastix" rel="nofollow noopener">Elastix forum</a>.</p>
<p>If you don’t want to spend much time with automated registration and you just need segmentation for all time points then you may try the more manual, landmark-based registration (for example, using Fiducial registration wizard module in SlicerIGT extension; or maybe Landmark registration in Slicer core).</p>
<p>You might also make segmentation faster by defining seed regions on one frame and then use the same seed regions for “Grow from seeds” in each frame to get complete segmentation.</p>

---

## Post #20 by @sarvpriya1985 (2019-01-19 22:37 UTC)

<p>Hi Andras,<br>
I spent many days struggling to do multi phase cardiac segmentation. I am happy to do segmentation on individual cardiac phases as registration is not working. But how to do that is still eluding me and I was hoping to do a presentation on seeing animated cardiac cine on virtual reality here at my facility. I am unable to proceed further and still stuck at single phase segmentation. I know its a lot to ask for from the forum, but I would appreciate some extra help to move further in this aspect.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #21 by @Shambhavi_Malik (2021-10-31 08:17 UTC)

<p>Hi Andras <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
Is it possible for you to upload a video tutorial regarding this?  I am working on the sample data CT Cardio volume sequence. I have segmented frame 4 by thresholding and I want to automatically segment the other frames. I’ve followed all the steps but I am not able to modify the segmentation for the rest of the time frames. If not a video tutorial then could you give the detailed steps to achieve this?<br>
Thanks in advance.</p>

---

## Post #22 by @Cody_Xie (2021-12-21 19:14 UTC)

<p>Hi Sarv, may I know if you have solved this problem? Now I want to segment the 4D heart CT, just like you did before. I was wondering if there is a method that could segment the other phases automatically. Any help from your side will be much appreciated!</p>

---

## Post #23 by @lassoan (2022-03-12 04:13 UTC)

<p>This video tutorial may help:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="qVgXdXEEVFU" data-video-title="Create an animated 4D surface model by segmenting a single 3D frame" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=qVgXdXEEVFU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/qVgXdXEEVFU/maxresdefault.jpg" title="Create an animated 4D surface model by segmenting a single 3D frame" width="" height="">
  </a>
</div>


---

## Post #25 by @lassoan (2023-03-03 04:23 UTC)

<p>If the generic preset works then I would recommend to start from that and tune registration settings one by one (by editing the parameter files) to see if you can improve the robustness or accuracy.</p>

---

## Post #26 by @Gening_Dong (2023-03-03 18:11 UTC)

<p>Thanks for the advice! I checked the folder RegistrationParameters and found 103 files. Does each file relate to a different registration preset? If so, could you please point out which one is for the generic preset? Thanks much!</p>

---

## Post #27 by @lassoan (2023-03-04 04:09 UTC)

<p>The ElastixParameterSetDatabase.xml file describes which parameters are used for which preset.</p>

---
