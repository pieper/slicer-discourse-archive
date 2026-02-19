---
topic_id: 638
title: "Need Help With Mesh Statistics Module"
date: 2017-07-06
url: https://discourse.slicer.org/t/638
---

# Need help with Mesh statistics module

**Topic ID**: 638
**Date**: 2017-07-06
**URL**: https://discourse.slicer.org/t/need-help-with-mesh-statistics-module/638

---

## Post #1 by @Carol (2017-07-06 17:25 UTC)

<p>Hi!</p>
<p>I am really need help.</p>
<p>I am using Slicer 4.5.0 and I am trying to download the mesh statistics module, but something is happening. The module is downloading with a error:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/Test/AppData/Roaming/NA-MIC/Extensions-24735/MeshStatisticsExtension/lib/Slicer-4.5/qt-scripted-modules/MeshStatistics.py”, line 68, in setup<br>
self.inputComboBox = self.logic.get(“inputComboBox”)<br>
File “C:/Users/Test/AppData/Roaming/NA-MIC/Extensions-24735/MeshStatisticsExtension/lib/Slicer-4.5/qt-scripted-modules/MeshStatistics.py”, line 191, in get<br>
return self.findWidget(self.interface.widget, objectName)<br>
File “C:/Users/Test/AppData/Roaming/NA-MIC/Extensions-24735/MeshStatisticsExtension/lib/Slicer-4.5/qt-scripted-modules/MeshStatistics.py”, line 196, in findWidget<br>
if widget.objectName == objectName:<br>
AttributeError: ‘NoneType’ object has no attribute ‘objectName’</p>
<p>what do I have to do? What is wrong?  It was working ok, but now I can not use it.</p>

---

## Post #2 by @lassoan (2017-07-06 17:27 UTC)

<p>Could you please try if it works in the latest nightly version of Slicer?</p>

---

## Post #3 by @Carol (2017-07-06 17:39 UTC)

<p>Ok I will try this… in a minute I will send you another message.</p>

---

## Post #4 by @Carol (2017-07-06 18:21 UTC)

<p>I download the nightly version and it is working again!</p>
<p>Thank you!!!</p>

---

## Post #5 by @Carol (2017-07-06 18:41 UTC)

<p>Hi Lassoan, I have another doubt.</p>
<p>Before the program was giving me the distances from point to point marked, now is providing me the ROI average, how do I provide the difference between the points marked in the models and not the change of ROI?</p>

---

## Post #6 by @lassoan (2017-07-06 19:13 UTC)

<aside class="quote no-group" data-username="Carol" data-post="5" data-topic="638">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/9d8465/48.png" class="avatar"> Carol:</div>
<blockquote>
<p>program was giving me the distances from point to point marked</p>
</blockquote>
</aside>
<p>What do you mean? What would you like to compute?</p>
<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a> - do you have any comments? (you are listed as one of the authors of the MeshStatistics extension)</p>

---

## Post #7 by @Carol (2017-07-06 19:18 UTC)

<p>I was using the Pick n paint module to mark some landmarks on my color map model, and than I was using the Mesh statistics module to measure the changes in each points marked. And the software was giving me the measurements point by point and in all directions (x,y and z).</p>
<p>I am doing measurements of the changes in bone before and after surgery. I saw a tutorial on youtube teaching me how to do it, and it was working, but now it isn’t.</p>

---

## Post #8 by @Carol (2017-07-06 19:26 UTC)

<div class="lazyYT" data-youtube-id="3kHT3IDoyy0" data-youtube-title="5C PickNPaint_Mesh Statistics" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>I was doing just like this video on youtube!</p>

---

## Post #9 by @Carol (2017-07-06 20:02 UTC)

<p>The module is seams to be a little different now, is there any upgrade of the module?</p>

---

## Post #11 by @lassoan (2017-07-06 22:44 UTC)

<p>The module has been updated and so the tutorial does not reflect how exactly the module works now. I agree that it is not easy to find out how the module should be used (I’ve spend a couple of minutes and I couldn’t figure it out).</p>
<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a> Could you please let us know where to find up-to-date documentation or tutorial?</p>

---

## Post #12 by @Carol (2017-07-06 22:46 UTC)

<p>OMG got it!</p>
<p>Do you know someone who can teach me what I have to do now to get this measurements?</p>

---

## Post #13 by @bpaniagua (2017-07-07 13:31 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/carol">@Carol</a></p>
<p>The reality is the videotutorials and the slicer wiki are the most up to date documentation for these extensions. We are in the process of securing funding right now to support all our <a href="http://cmf.slicer.org">slicercmf</a>, and yes, i agree we should update the documentation. Do you have specific questions about the measurements you want to generate?</p>
<p><a class="mention" href="/u/jbvimort">@jbvimort</a> mentioned that you also experienced some problems running these extensions, why not using them through the <a href="http://cmf.slicer.org/download/">SlicerCMF packages</a>? The extensions are all pre-installed on that custom distribution of Slicer.</p>
<p>If you have questions about SlicerCMF, please ask them <a href="https://discourse.slicer.org/c/community/slicercmf">here</a>.</p>

---

## Post #14 by @Carol (2017-07-07 19:53 UTC)

<p>Hello everybody!</p>
<p>I was doing like in youtube tutorial (<a href="https://www.youtube.com/watch?v=3kHT3IDoyy0" rel="nofollow noopener">https://www.youtube.com/watch?v=3kHT3IDoyy0</a>)</p>
<p>But since the modules were updated I can not do the measurements.</p>
<p>The steps are different but I can not figure it out how to perform it.</p>
<p>I am trying to get the changes in each points that I am marking in condyle surface. But the number that the SlicerCMF is give me is the change of the hole condyle not of each point like I was doing using the last version of the modules.</p>
<p>Previously, I was making the color map model (using model to model distance module), than I was placing the landmark on color map surface (using pink n paint module) and than I was going to Mesh statistics module and it was giving me the difference in each area, just like in the video above.</p>
<p>But now the steps are changed and I can not figure it out. I want you to show me the difference of the steps and how I have to do it from now on.</p>
<p>I am in the middle of my research and if I won’t figure it out I will have to do all measurements again.</p>
<p>I hope you can help me.</p>

---

## Post #15 by @jbvimort (2017-07-07 20:16 UTC)

<p>Could you please send us an example of your data? That way, we could try to replicate the procedure with the new modules?</p>

---

## Post #16 by @Carol (2017-07-07 20:25 UTC)

<p>I am going to send you pre and post treatment condyle model of one of my sample.</p>
<p>Could I send you the data by email? Because I can not upload here.</p>

---

## Post #17 by @jbvimort (2017-07-07 20:31 UTC)

<p>Could you put it on a drive (google drive for example) and share a link with everyone?</p>

---

## Post #18 by @Carol (2017-07-07 20:34 UTC)

<p>I’ve already sent to you e-mail.</p>

---

## Post #19 by @jbvimort (2017-07-07 21:05 UTC)

<p>Where you adding several landmarks/ROI on each colormap?</p>

---

## Post #20 by @Carol (2017-07-07 21:12 UTC)

<p>5 landmarks,</p>
<p>One at the most anterior part of the condyle;<br>
One at the most posterior part of the condyle;<br>
One at the most lateral part of the condyle;<br>
One at the most medial part of the condyle;<br>
One at the most superior part of the condyle.</p>

---

## Post #21 by @jbvimort (2017-07-07 21:22 UTC)

<p>It seems that the new version of the module now handle only one ROI per colormap, i.e. it’s not creating one ROI per landmark like before.<br>
Which mean that mesh statistic is only gonna give you one set of differences.<br>
Right now, if you want to have the same results than previously, you would have to create a ROI with one landmark and compute the statistics with mesh statistics  erase the first landmark and restart for the next landmark</p>

---

## Post #22 by @Carol (2017-07-07 21:28 UTC)

<p>In website there is an example of how to use it and seams to be all value of each number at the same time, just like the old version.</p>
<p>See the picture:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/2fa0d205d72c6652416371010a5bfd6913081782.jpg" data-download-href="/uploads/short-url/6NkZPmqtub8A28XyUZrqXdhwHjc.jpg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2fa0d205d72c6652416371010a5bfd6913081782_2_690x392.jpg" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2fa0d205d72c6652416371010a5bfd6913081782_2_690x392.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fa0d205d72c6652416371010a5bfd6913081782.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fa0d205d72c6652416371010a5bfd6913081782.jpeg 2x" data-dominant-color="BEBFD8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">800×455 94.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #23 by @jbvimort (2017-07-07 21:34 UTC)

<p>Yes, but the problem is not the new version of Mesh Statistics that did not change a lot and is still working in the same way, but the version of pick and paint that is not working the same way.</p>

---

## Post #24 by @Carol (2017-07-07 21:36 UTC)

<p>I tried to use the new methodology with an sample that I have already analysed and the values are different from the first evaluation (ps.: the evaluation was made two times before - with the old module as a part of our research to do the intraclass agreement) and the values were almost the same.</p>

---

## Post #25 by @jbvimort (2017-07-07 21:50 UTC)

<p>So you are able to obtain results with the new versions of the modules?<br>
But they are the same than before?</p>

---

## Post #26 by @Carol (2017-07-07 21:53 UTC)

<p>Yeah I got some results of the same parameters but the number are totally different from my first analysis.</p>

---

## Post #27 by @jbvimort (2017-07-07 21:55 UTC)

<p>How many landmarks have you placed on the model with the new version of the modules?</p>

---

## Post #28 by @Carol (2017-07-07 22:08 UTC)

<p>The same number as in my anterior analysis (5 landmarks), but the program just show one result that I cant  figure out of which landmarks came from.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/599375e796bd06b394f50c7726ca05b4fc3c9ef0.png" data-download-href="/uploads/short-url/cMqqvYyvhEll9EcviVZmNWQFUNW.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/599375e796bd06b394f50c7726ca05b4fc3c9ef0_2_690x431.png" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/599375e796bd06b394f50c7726ca05b4fc3c9ef0_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/599375e796bd06b394f50c7726ca05b4fc3c9ef0_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/599375e796bd06b394f50c7726ca05b4fc3c9ef0_2_1380x862.png 2x" data-dominant-color="C3C0D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1920×1200 356 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #29 by @jbvimort (2017-07-07 22:25 UTC)

<p>As you said before, I think it’s the average over the five regions of interest. So the result you got is not really exploitable.<br>
Try to put a single landmark,  the one on the anterior part of the condile, run mesh statistics with this only condile and try to compare this result with the previous ones.</p>

---

## Post #30 by @Carol (2017-07-07 22:33 UTC)

<p>I already did it … and all the result I got are totally different from the previous one.</p>
<p>I was trying to figure out what is the problem, and I think that the mesh statistic is not recognizing the models of the T1 and T2, because when I changed model the program show that is just one model available for analysis. So the pick n paint module is just saving the VTK file without any relation with the T1 and T2… what do you think that we can do it in order to see the 3 models (T1, T2 and VTK) in the mesh statistic module???</p>

---

## Post #31 by @jbvimort (2017-07-07 22:54 UTC)

<p>I think that Mesh statistics should never care about your T1 and t2 models.  the only thing it is using is the colormap you generated with model to model distance.</p>

---

## Post #32 by @Carol (2017-07-07 23:00 UTC)

<p>I got it. I really don’t know what is going on.</p>

---
