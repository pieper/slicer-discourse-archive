# Using Slicer to create a model of middle ear anatomy

**Topic ID**: 5169
**Date**: 2018-12-21
**URL**: https://discourse.slicer.org/t/using-slicer-to-create-a-model-of-middle-ear-anatomy/5169

---

## Post #1 by @Kunal_Sareen (2018-12-21 17:47 UTC)

<p>I’m currently working on trying to use Slicer for segmenting the anatomical structures significant to the middle ear. I’m having troubles in trying to segment structures in a high resolution Brain CT. Is there any solution on how to go about it? I’ve tried using the Segment Editor tool and tried to grow from seeds, but the structures aren’t clearly identifiable. Can anyone suggest some other approach? Do I need a Ear CT or Temporal CT specifically for decreasing the FOV or brain CT is sufficient?</p>

---

## Post #2 by @pieper (2018-12-21 21:26 UTC)

<p>Have you looked at SlicerCochlea?</p>
<p><a href="https://mtixnat.uni-koblenz.de/downloads.html" class="onebox" target="_blank" rel="nofollow noopener">https://mtixnat.uni-koblenz.de/downloads.html</a></p>
<p><a href="https://medicalimageanalysistutorials.github.io/SlicerCochlea/" class="onebox" target="_blank" rel="nofollow noopener">https://medicalimageanalysistutorials.github.io/SlicerCochlea/</a></p>

---

## Post #3 by @Kunal_Sareen (2018-12-22 02:26 UTC)

<p>Thank you for your quick reply. I did check out the Slicer Cochlea. But my main field of interest is segmenting the middle ear and its parts and not the cochlea. Is there any other way I can do that?</p>

---

## Post #4 by @pieper (2018-12-22 02:44 UTC)

<p>There’s no pre-defined extension for the middle ear that I know of, but the Segment Editor and related tools should provide what you need to do it semi-automatically.</p>

---

## Post #5 by @nagy.attila (2018-12-22 14:14 UTC)

<p>Hi,</p>
<p>well, middle ear scans that I have seen were mostly “hospital” scans, so not really high resolution, and/or not really well windowed.<br>
I usually ended up adjusting the threshold and then simply using the threshold-paint tool to mark structures and then adjust the threshold again and then use the paint tool… There are very fine structured bones, the eardrum, the tensor tympani and m. stapedius… making a good scan isn’t that easy either.<br>
Because of their sizes and the relatively big differences in HU it isn’t really easy to segment these. If you adjust the threshold to visualize the bones, you won’t see the muscles and the eardrum well, and vice versa. Since in my practice these usually span only a few slices (around 20 at most) I usually ended up doing it by hand.<br>
But I’m not a big expert <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @Kunal_Sareen (2018-12-22 14:28 UTC)

<p>Thanks for the reply. I’m trying to manually segment the structures but the low resolution and poor intensity is becoming a huge difficulty. Any suggestion how to increase the intensity in a way that segmentation becomes a bit easier?</p>

---

## Post #7 by @cpinter (2018-12-22 14:34 UTC)

<p>Optimizing the brightness/contrast (we call it window/level) is a must, but you probably figured that out yourself. Otherwise please refer to the gif on this page<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Volumes" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Volumes</a></p>

---

## Post #8 by @Young_Wang (2022-12-02 18:36 UTC)

<p><a class="mention" href="/u/kunal_sareen">@Kunal_Sareen</a> there is also ABL temporal bone module that you can find <a href="https://github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation" rel="noopener nofollow ugc">here</a> but I haven’t had success using it.</p>

---

## Post #9 by @Nadine_Nabil (2025-06-21 15:07 UTC)

<p>Hello, I am also trying to find a way to do segmentation of the middle ear. Can you tell me if you have reached a result?</p>
<p>Were you able to find these parts in the segmentation?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87c489e35345fd8ea701529a180281974ee81636.png" data-download-href="/uploads/short-url/jn3xvXAaonFLOfA89VdQ7RlHlUW.png?dl=1" title="Screenshot 2025-06-21 180648" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87c489e35345fd8ea701529a180281974ee81636_2_541x500.png" alt="Screenshot 2025-06-21 180648" data-base62-sha1="jn3xvXAaonFLOfA89VdQ7RlHlUW" width="541" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87c489e35345fd8ea701529a180281974ee81636_2_541x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87c489e35345fd8ea701529a180281974ee81636.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87c489e35345fd8ea701529a180281974ee81636.png 2x" data-dominant-color="C49079"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-06-21 180648</span><span class="informations">765×707 567 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
