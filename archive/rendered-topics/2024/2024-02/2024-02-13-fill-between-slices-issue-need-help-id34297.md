# Fill between slices issue : need help!

**Topic ID**: 34297
**Date**: 2024-02-13
**URL**: https://discourse.slicer.org/t/fill-between-slices-issue-need-help/34297

---

## Post #1 by @ThomasHusson (2024-02-13 15:52 UTC)

<p>Hello,<br>
I still try to do a liver volumetry (see topic here : <a href="https://discourse.slicer.org/t/beginner-question-liver-volumetry/33887" class="inline-onebox">Beginner question: liver volumetry</a>).</p>
<p>I succeed two or three times using a simple method :<br>
1- extract liver using totalsegmentator<br>
2- use “draw” tool to define the liver volume I want to extract (simulating a liver resection)<br>
3- use the tool “fill between slices” between slices on which I drew the liver resection</p>
<p>BUT : I have a problem with “fill between slices”</p>
<p>First case : without extracting the liver with totalsegmentator, I draw the liver resection and use “fill between slices”.<br>
I draw the liver resections in “everywhere area”, so I have to be very precise and it’s a bit difficult to do.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/0445837e9d2e0629b626cfef8d8517e7e3067b45.jpeg" data-download-href="/uploads/short-url/BMQdnQbgbxr1sXGuiCjd6bhZ4N.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0445837e9d2e0629b626cfef8d8517e7e3067b45_2_690x368.jpeg" alt="image" data-base62-sha1="BMQdnQbgbxr1sXGuiCjd6bhZ4N" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0445837e9d2e0629b626cfef8d8517e7e3067b45_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0445837e9d2e0629b626cfef8d8517e7e3067b45_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0445837e9d2e0629b626cfef8d8517e7e3067b45_2_1380x736.jpeg 2x" data-dominant-color="7C7A78"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1026 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>By this way, the tool “fill between slices” work well :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1da15b24c9096e1a81b73423ed4d3dc10460a7f6.jpeg" data-download-href="/uploads/short-url/4e7y7w9AIRF3FHPtfpCLPjgaltc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1da15b24c9096e1a81b73423ed4d3dc10460a7f6_2_690x382.jpeg" alt="image" data-base62-sha1="4e7y7w9AIRF3FHPtfpCLPjgaltc" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1da15b24c9096e1a81b73423ed4d3dc10460a7f6_2_690x382.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1da15b24c9096e1a81b73423ed4d3dc10460a7f6_2_1035x573.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1da15b24c9096e1a81b73423ed4d3dc10460a7f6_2_1380x764.jpeg 2x" data-dominant-color="817E7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1063 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What I want to do is :<br>
first, extract the liver using totalsegmentator, to do my liver resection inside the segment “liver”.</p>
<p>Then, draw the liver resections using settings “inside “liver””, because it’s much easier. See details here :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/0656a143e562ad8044438a08e0bafd108424fad0.jpeg" data-download-href="/uploads/short-url/U4t3mMVE5VV0YRyxIeFvExVYGI.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0656a143e562ad8044438a08e0bafd108424fad0_2_690x370.jpeg" alt="image" data-base62-sha1="U4t3mMVE5VV0YRyxIeFvExVYGI" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0656a143e562ad8044438a08e0bafd108424fad0_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0656a143e562ad8044438a08e0bafd108424fad0_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0656a143e562ad8044438a08e0bafd108424fad0_2_1380x740.jpeg 2x" data-dominant-color="827F7C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I made two slices, see pic here :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56754556b4e341bf8fb68dac7bad9e4146dc3bc2.jpeg" data-download-href="/uploads/short-url/ckQjtq3wyI7snF8GFWvAR0rxACm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56754556b4e341bf8fb68dac7bad9e4146dc3bc2_2_690x370.jpeg" alt="image" data-base62-sha1="ckQjtq3wyI7snF8GFWvAR0rxACm" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56754556b4e341bf8fb68dac7bad9e4146dc3bc2_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56754556b4e341bf8fb68dac7bad9e4146dc3bc2_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56754556b4e341bf8fb68dac7bad9e4146dc3bc2_2_1380x740.jpeg 2x" data-dominant-color="888480"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1031 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then, when I want to use the tool “fill between slices”, nothing happens, and I really don’t know why.<br>
I tried to change the settings of the fill between slices tool but it does’nt work, see here :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00d4b528d6e968307ed87a3e019c624f4661554f.jpeg" data-download-href="/uploads/short-url/7lITeRz1mwfUCS0RsTbkCeYrtt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00d4b528d6e968307ed87a3e019c624f4661554f_2_690x369.jpeg" alt="image" data-base62-sha1="7lITeRz1mwfUCS0RsTbkCeYrtt" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00d4b528d6e968307ed87a3e019c624f4661554f_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00d4b528d6e968307ed87a3e019c624f4661554f_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00d4b528d6e968307ed87a3e019c624f4661554f_2_1380x738.jpeg 2x" data-dominant-color="878480"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1028 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you have an idea ? I really don’t know</p>
<p>Thank you very much !!</p>

---

## Post #2 by @Matteboo (2024-02-19 10:29 UTC)

<p>Hello,<br>
One thing you could do is to segment the part that you want to resect before segmenting the liver as you explained in the first part of you post.<br>
Then you segment the liver.<br>
Once you have both segmentation you can do take the intersection to get what you want.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a71f117aa26bac5f9bcc5856d60539c3291c743b.png" data-download-href="/uploads/short-url/nQqiFcRWBL9yiNabZpHPk2PNvV9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a71f117aa26bac5f9bcc5856d60539c3291c743b_2_277x500.png" alt="image" data-base62-sha1="nQqiFcRWBL9yiNabZpHPk2PNvV9" width="277" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a71f117aa26bac5f9bcc5856d60539c3291c743b_2_277x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a71f117aa26bac5f9bcc5856d60539c3291c743b_2_415x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a71f117aa26bac5f9bcc5856d60539c3291c743b.png 2x" data-dominant-color="3C3D3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">532×957 57.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This will allow you to not be as precise when segmenting manually since if you draw outside the liver, the outside part will be deleted when doing the intersection.</p>

---

## Post #3 by @ThomasHusson (2024-02-25 17:35 UTC)

<p>Hey, thanks a lot. You just had the solution !!!<br>
First segment it with cut tool<br>
Use totalsegmentator to extract whole liver<br>
Then use intersect tool as you said, it worked very well !<br>
Thanks again</p>

---
