# Segmentation of large nodule from CT

**Topic ID**: 32550
**Date**: 2023-11-02
**URL**: https://discourse.slicer.org/t/segmentation-of-large-nodule-from-ct/32550

---

## Post #1 by @Caterina (2023-11-02 08:02 UTC)

<p>Good morning,<br>
I’m interested in performing segmentation of large nodule from CT dicom images.<br>
Is Lung CT Segmenter Module useful to identify large nodule or other abnormalities?<br>
Can you please suggest me the better segmentation process to do it?<br>
Thanks</p>

---

## Post #2 by @rbumm (2023-11-02 13:49 UTC)

<p>Lung CT Segmenter itself segments lungs, lobes, airways and a vesselmask. It creates an empty segment for “tumor” and  we do not yet have nodule or tumor recognition.<br>
For segmenting the tumor you could for example use the “Segment Editor” and it’s “Local Threshold” effect as shown here:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d72d6e2bc2af27565ca5c57c63ced1d7cb5178a7.mp4">
  </div><p></p>
<p>CTRL + left click into the tumor</p>

---

## Post #3 by @Caterina (2023-11-03 09:48 UTC)

<p>Thank you very much for reply and for information.<br>
Just another question in order to be sure to make sure I understood.<br>
Is Lung CT Segmenter Module able to independently identify a region that is anomalous compared to the anatomical regions it segments?<br>
Thanks</p>

---

## Post #4 by @rbumm (2023-11-03 15:47 UTC)

<p>The Segmenter just segments the basic structures, but  you can use the Lung CT Analyzer after the Segmenter to quantify infilrations or lung collapse of any cause (evaluated for COVID) as well as fibrosis and emhysema.</p>

---

## Post #5 by @Caterina (2023-11-07 07:52 UTC)

<p>Dear <a class="mention" href="/u/rbumm">@rbumm</a>,<br>
thank you very much for support and suggestion.<br>
I performed segmentation using Lung CT segmenter Module. It created a volume “tumor” that was empty. At this point, I tried the Local Threshold segmentation, as you suggested, but after CTRL + left click into the tumor, the region was not identified. Extraeffects module was installed.<br>
Can you please suggest me a solution?If you want, I can share with you private copy of the dicom.<br>
Thanks</p>

---

## Post #6 by @rbumm (2023-11-07 08:13 UTC)

<p>No problem, you can DM a link to your data, I can give it a try.<br>
Best<br>
r</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7bd2850d11acccbaa189a9f1efe728bad79854d.png" alt="image" data-base62-sha1="suYhEdXOjnh6YZkeTyE34G5udXL" width="613" height="253"></p>

---

## Post #7 by @rbumm (2023-11-07 09:43 UTC)

<p>So this is quite a noisy dataset - but the processing works.</p>
<ol>
<li>Run the dataset through the Lung CT Segmenter with airway segmentation and AI TotalSegmentator lung basic.<br>
This will give you the lungs, lobes and the unelegant airway.<br>
If you do not need the lungs or lobes skip this part. But at least admire the quality that AI can segment the lobes from these noisy data.</li>
</ol>
<p>Then go Segment editor and follow these steps very carefully.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5284eeeaed9c0b3cd32c6c992d76464a2f86313.mp4">
  </div><p></p>
<ul>
<li>Disable the upper lobe</li>
<li>Select the “tumor” segent</li>
<li>Make it visible (check the box)</li>
<li>Select the local threshold effect</li>
<li>Allow Overlap</li>
<li>Set minimum diameter to 3 mm</li>
<li>Now the most important part: Adjust the threshold in a way that only bones and the tumor are flickering. (-339 to 3071)</li>
<li>Then CTRL + left click into the tumor and wait.</li>
<li>This clip is unedited.</li>
<li>You will have to do some postprocessing to remove the vascular “fingers” from the tumor.<br>
Good luck.<br>
It you fail, just DM me for a Zoom call.</li>
</ul>
<p>Best<br>
r</p>

---

## Post #8 by @Caterina (2023-11-07 10:03 UTC)

<p>Thanks a lot.<br>
I will follow all your suggestions and I will inform you on results.<br>
Thanks</p>

---

## Post #9 by @Caterina (2023-11-07 14:22 UTC)

<p>Dear <a class="mention" href="/u/rbumm">@rbumm</a>,<br>
can you please share with me also the video of the first part (Lung Segmenter module).<br>
I have a different output also from the first part.<br>
Did you use Interactive segmentation module?I have no identification of upper and lower lobes.<br>
Concerning the step “CTRL + left click into the tumor and wait”, it takes a long time.<br>
I’m waiting ;-(</p>

---

## Post #10 by @rbumm (2023-11-07 16:53 UTC)

<p>Can you share your system specifications ? What computer, operating system, graphic system, does your system have a GPU ? What brand and model ?</p>

---

## Post #11 by @Caterina (2023-11-07 16:56 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f546438dee826ed74b7693f43713dacac21dc72a.png" alt="Screenshot 2023-11-07 alle 17.55.53" data-base62-sha1="yZNweDPhuupaUoOJ4j6qiQnNVKW" width="544" height="194"></p>

---

## Post #12 by @Caterina (2023-11-07 16:57 UTC)

<p>For the first step, did you use Interactive Lobe Segmentation module?<br>
Thanks</p>

---

## Post #13 by @rbumm (2023-11-07 17:16 UTC)

<p>No, I used the Lung CT Segmenter, part of the Lung CT Analyzer module. You will get this kind of automatic lobe segmentation by using the AI functions and selecting TotalSegmentator lung basic. However, unfortunately, your computer is too weak to run such sophisticated software. You will need a Windows or Linux system with an NVIDIA GPU with at least 8 GB of GPU memory. Alternatively, you could rent a GPU-enabled system in the cloud (Google, Amazon). But this would require a lengthy setup process and running costs of around 2-3 dollars per hour. I would recommend investing in a future-proof hardware system. The 3D Slicer guys should be able to provide recommendations for such a 3D Slicer and AI optimized configuration.</p>

---

## Post #14 by @Caterina (2023-11-07 17:32 UTC)

<p>Thank you very much for all.<br>
Your support and kindness are absolutely precious.<br>
Thanks again</p>

---

## Post #15 by @rbumm (2023-11-07 17:32 UTC)

<p>How many datasets do you have to analyze?</p>

---

## Post #16 by @Caterina (2023-11-08 14:49 UTC)

<p>Dear <a class="mention" href="/u/rbumm">@rbumm</a>,<br>
It depends on how well this pipeline performs.<br>
Is there a way to improve the nodule segmentation result (except having better quality images)?<br>
Does 3D Slicer include a module for the dimensional analysis of segmentations? In the Statistics module you can view volumes and surfaces. Any other parameters?</p>

---

## Post #17 by @rbumm (2023-11-08 16:16 UTC)

<aside class="quote no-group" data-username="Caterina" data-post="16" data-topic="32550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/439d5e/48.png" class="avatar"> Caterina:</div>
<blockquote>
<p>It depends on how well this pipeline performs.</p>
</blockquote>
</aside>
<p>There are a few things that initially work as intended by the researcher. But 3D Slicer is one if not the most cited medical image application to date.</p>
<aside class="quote no-group" data-username="Caterina" data-post="16" data-topic="32550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/439d5e/48.png" class="avatar"> Caterina:</div>
<blockquote>
<p>Is there a way to improve the nodule segmentation result (except having better quality images)?</p>
</blockquote>
</aside>
<p>This is just a start for experimentation, even commercial software has no reliable tumor or nodule recognition.</p>
<aside class="quote no-group" data-username="Caterina" data-post="16" data-topic="32550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/439d5e/48.png" class="avatar"> Caterina:</div>
<blockquote>
<p>Does 3D Slicer include a module for the dimensional analysis of segmentations?</p>
</blockquote>
</aside>
<p>Yes, you have segment statistics and radiomics.</p>
<aside class="quote no-group" data-username="Caterina" data-post="16" data-topic="32550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/439d5e/48.png" class="avatar"> Caterina:</div>
<blockquote>
<p>In the Statistics module you can view volumes and surfaces. Any other parameters?</p>
</blockquote>
</aside>
<p>Try it out <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">  there are many others.</p>

---

## Post #18 by @Caterina (2023-11-09 13:51 UTC)

<p>I would like to compare the segmentation performed using the pipeline you suggested me (Lung Segmentation with AI and airways and Local Threshold for nodule) with the manual segmentation of large nodule from TC using the free database SIMBA (Patient SL0058).</p>
<p>Results from the first case showed that a volume of nodule segment is around 18164 mm^3 from manual segmentation compared to 11695.2 mm^3 from Slicer (in attach the two results).<br>
The difference seems to be large.<br>
Can you please suggest a way to improve this problem?<br>
Do you think that with a cleaner database we can improve this difference? Do you have information on another free CT database in which nodules are evaluated?<br>
Thanks<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7534feefb48e9fafed8b0e1a0339d573bab8718.jpeg" data-download-href="/uploads/short-url/nSeesu3MfePAdPuxf1wnivvC70s.jpeg?dl=1" title="Results" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7534feefb48e9fafed8b0e1a0339d573bab8718_2_690x392.jpeg" alt="Results" data-base62-sha1="nSeesu3MfePAdPuxf1wnivvC70s" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7534feefb48e9fafed8b0e1a0339d573bab8718_2_690x392.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7534feefb48e9fafed8b0e1a0339d573bab8718_2_1035x588.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7534feefb48e9fafed8b0e1a0339d573bab8718_2_1380x784.jpeg 2x" data-dominant-color="D6D6E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Results</span><span class="informations">1426×811 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @rbumm (2023-11-09 14:36 UTC)

<p>Is this is the same dataset ? The one you have sent is SL0058 ? Because the one you sent is is identified S02A01 …</p>

---

## Post #20 by @Caterina (2023-11-09 14:42 UTC)

<p>Yes, is the same I shared with you <a class="mention" href="/u/rbumm">@rbumm</a>. The master folder is named SL0058.<br>
It contains a subfolder S02A01.</p>

---

## Post #21 by @rbumm (2023-11-09 17:04 UTC)

<p>It turns out that part of the tumor is hollow:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa5945fae2177d28f0774dd5364063b490733038.jpeg" data-download-href="/uploads/short-url/oiYr6QUZ74Fr7hukiVbQRcYinJ6.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa5945fae2177d28f0774dd5364063b490733038_2_690x335.jpeg" alt="image" data-base62-sha1="oiYr6QUZ74Fr7hukiVbQRcYinJ6" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa5945fae2177d28f0774dd5364063b490733038_2_690x335.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa5945fae2177d28f0774dd5364063b490733038_2_1035x502.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa5945fae2177d28f0774dd5364063b490733038_2_1380x670.jpeg 2x" data-dominant-color="7D7C7E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1407×684 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>With a little adaptation Iof threshold I (lower : -406) I get</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4fc1b1933b851e1a65ff5901dab8b2a824212fc.png" data-download-href="/uploads/short-url/wFGZQCXt6Mw7g9U4HXbJsJR3bE8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4fc1b1933b851e1a65ff5901dab8b2a824212fc.png" alt="image" data-base62-sha1="wFGZQCXt6Mw7g9U4HXbJsJR3bE8" width="690" height="34" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">969×48 1.57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>which is probably reasonable.</p>
<p>Your reference was probably done with a fill-between-slices effect of the segment editor which requires more work.</p>

---

## Post #22 by @Caterina (2023-11-10 09:53 UTC)

<p>Dear <a class="mention" href="/u/rbumm">@rbumm</a>,<br>
thank you very much for your suggestion and updates.<br>
I will perform another segmentation with the lower threshold of -406.<br>
In your new case volume is around 13000 compared to 18000.<br>
Is this a tolerable difference?<br>
I will try to perform the same procedure for the other cases.<br>
Concerning your observation “Your reference was probably done with a fill-between-slices effect of the segment editor which requires more work.”, is fill-between-slices effect a default option?<br>
Thanks</p>

---

## Post #23 by @rbumm (2023-11-10 14:14 UTC)

<p>Fill between slices is on option in which you paint every volume slice of the tumor with an intensity modified paint tool and later use the fill between slices effect to create the actual segmentation. It is much more work and looks often ugly, like a layered cake.</p>
<p>If you create a tumor segmentation with local threshold and maybe add some pixes here and there that are missin or remove some that are representing vessels 13000 is the reference value. (net volume with holes)</p>

---

## Post #24 by @Caterina (2023-11-11 10:15 UTC)

<p>Dear <a class="mention" href="/u/rbumm">@rbumm</a>,<br>
thank you for support.<br>
I will proceed with another case in order to evaluate if the differences still remains in the other cases of the same database. One more question:<br>
-the results of segmentation in 3d seems to be in transparency. How to convert them as opaque models?</p>

---

## Post #25 by @Caterina (2023-11-18 08:35 UTC)

<p>Good morning,<br>
I’m testing other cases of the same dataset.</p>
<p>I’m having trouble defining the local threshold on the nodule for them. More specifically, after imposing the threshold range, and command left click (Mac), not only the region of interest but also the other regions the other regions are also selected.  Can I have suggestions about it?<br>
Thanks</p>
<p>Thanks</p>

---

## Post #26 by @rbumm (2023-11-18 09:49 UTC)

<p>Could you provide one or two case numbers?</p>

---

## Post #27 by @Caterina (2023-11-18 10:24 UTC)

<p>The number of the same dataset are SL0078 SL0080 SL0081</p>

---

## Post #29 by @rbumm (2023-11-18 10:51 UTC)

<p>Where do I find these patients? Do you have a NBIA manifest for this series?</p>

---

## Post #30 by @Caterina (2023-11-18 11:01 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> I will share with you these cases soon. Thanks</p>

---

## Post #31 by @rbumm (2023-11-18 13:03 UTC)

<p>(1) Create a ROI<br>
(2) Place this ROI around the tumor<br>
(3) use Local Threshold effect with Grow Cut enabled</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9038518a71091a1c5f2bcca3cfff00e90af59672.jpeg" data-download-href="/uploads/short-url/kzPpTje3HIcteb2DXuZ01zkdFFE.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9038518a71091a1c5f2bcca3cfff00e90af59672_2_690x359.jpeg" alt="image" data-base62-sha1="kzPpTje3HIcteb2DXuZ01zkdFFE" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9038518a71091a1c5f2bcca3cfff00e90af59672_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9038518a71091a1c5f2bcca3cfff00e90af59672_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9038518a71091a1c5f2bcca3cfff00e90af59672_2_1380x718.jpeg 2x" data-dominant-color="B2A09E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1909×995 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(4) do some postprocessing (remove vessels)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63bd4626a53dfa8b343ef202801c620ec89297eb.jpeg" data-download-href="/uploads/short-url/eekMOppGL0s83NAMYnFblYzj8F5.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63bd4626a53dfa8b343ef202801c620ec89297eb_2_690x329.jpeg" alt="image" data-base62-sha1="eekMOppGL0s83NAMYnFblYzj8F5" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63bd4626a53dfa8b343ef202801c620ec89297eb_2_690x329.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63bd4626a53dfa8b343ef202801c620ec89297eb_2_1035x493.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63bd4626a53dfa8b343ef202801c620ec89297eb_2_1380x658.jpeg 2x" data-dominant-color="A9A6BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1404×670 84.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #32 by @Caterina (2023-11-19 17:31 UTC)

<p>Thank you very much <a class="mention" href="/u/rbumm">@rbumm</a>.<br>
I will use your suggestions and update you.<br>
Thanks</p>

---

## Post #33 by @Caterina (2023-11-30 14:23 UTC)

<p>Dear <a class="mention" href="/u/rbumm">@rbumm</a>,<br>
sorry for delay to reply and thank for support.<br>
Creating a ROI and performing the local threshold approach, I performed the segmentation.<br>
The problem is that the ROI created disappeared after several slices. It means that the segmentation segmentation neglects the region from a certain slice onwards. Can you suggest how to fix it?<br>
In addition, is it possible to create a “not cubed” ROI (a ROI with possibility to create curved ROI?)<br>
Thanks</p>

---

## Post #34 by @Caterina (2023-12-05 13:04 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Can you please suggest me how to fix the last problems?<br>
Thanks</p>

---

## Post #35 by @rbumm (2023-12-05 14:38 UTC)

<p>Unfortunately, there is no elliptical 3D ROI in Slicer.<br>
I would recommend segmenting the right lung with Lung CT Segmenter and using it as a mask → Editable area “Inside right lung” for the Growcut operation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39871f587b4e7a1c988b2edf3ddb10196ff25fb4.jpeg" data-download-href="/uploads/short-url/8cUIhPBKl7K9VkgWCHgkaRDllfm.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39871f587b4e7a1c988b2edf3ddb10196ff25fb4_2_690x312.jpeg" alt="image" data-base62-sha1="8cUIhPBKl7K9VkgWCHgkaRDllfm" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39871f587b4e7a1c988b2edf3ddb10196ff25fb4_2_690x312.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39871f587b4e7a1c988b2edf3ddb10196ff25fb4_2_1035x468.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39871f587b4e7a1c988b2edf3ddb10196ff25fb4_2_1380x624.jpeg 2x" data-dominant-color="A5A5A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1907×865 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #36 by @Caterina (2023-12-05 14:41 UTC)

<p>Thanks a lot.<br>
I will try. Concerning this problem “the ROI created disappeared after several slices” for the previous approach, can you please suggest how to fix it?<br>
Thanks</p>

---

## Post #37 by @rbumm (2023-12-05 15:00 UTC)

<p>I would recommend to resample the volume 1,1,1 for a test. Create a new volume as output. Try to use the ROI with the new volume.</p>

---

## Post #38 by @Caterina (2023-12-05 15:11 UTC)

<p>Thanks a lot.<br>
Just the last question.<br>
After performing Lung CT Segmenter, sometimes 3d models appear transparent and other times not.<br>
What is the function that makes them transparent so you can see the module inside? Thanks again</p>

---

## Post #39 by @rbumm (2023-12-05 15:53 UTC)

<p>Go “Segmentations”, select the structure you want, go “Advanced” and move the 3D slider.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42d135eb39de1ec4c6b098bd254bddb77b9d047a.mp4">
  </div><p></p>

---
