---
topic_id: 24102
title: "How To Get Airways Using Lungctanalyzer"
date: 2022-06-29
url: https://discourse.slicer.org/t/24102
---

# How to get airways using LungCTAnalyzer

**Topic ID**: 24102
**Date**: 2022-06-29
**URL**: https://discourse.slicer.org/t/how-to-get-airways-using-lungctanalyzer/24102

---

## Post #1 by @ekmungi (2022-06-29 12:52 UTC)

<p>This question is a continuation to an <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/issues/34" rel="noopener nofollow ugc">issue</a> I posted on github. I am posting follow-up here.</p>
<p>I performed the steps as suggested. However, as can be seen in the second picture. Somehow the lung lobes and airways are being mixed up.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4c14360738dde652727b605c5c6a9e17fe842ce.jpeg" data-download-href="/uploads/short-url/pN20zcjOKgZx71q2wtkwpOWxrnU.jpeg?dl=1" title="Screenshot_20220629_115204" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4c14360738dde652727b605c5c6a9e17fe842ce_2_690x378.jpeg" alt="Screenshot_20220629_115204" data-base62-sha1="pN20zcjOKgZx71q2wtkwpOWxrnU" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4c14360738dde652727b605c5c6a9e17fe842ce_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4c14360738dde652727b605c5c6a9e17fe842ce_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4c14360738dde652727b605c5c6a9e17fe842ce_2_1380x756.jpeg 2x" data-dominant-color="5C5D5F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20220629_115204</span><span class="informations">1920×1054 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41131c921a654f6800122dd00c9910b59451efb1.jpeg" data-download-href="/uploads/short-url/9hFYSOJxH9k6yfIDqkWMMa5g0JX.jpeg?dl=1" title="Screenshot_20220629_115900" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41131c921a654f6800122dd00c9910b59451efb1_2_690x378.jpeg" alt="Screenshot_20220629_115900" data-base62-sha1="9hFYSOJxH9k6yfIDqkWMMa5g0JX" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41131c921a654f6800122dd00c9910b59451efb1_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41131c921a654f6800122dd00c9910b59451efb1_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41131c921a654f6800122dd00c9910b59451efb1_2_1380x756.jpeg 2x" data-dominant-color="565A5F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20220629_115900</span><span class="informations">1920×1054 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The ONLY blue colored segmentation includes both Lung lobes + Airways + Bronchus – As seen in the picture below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ac95612c603fb72e7942427327b92b1e350c7ad.jpeg" data-download-href="/uploads/short-url/66vpHPLzL5vf6LQ2Npr0M6ZmFaZ.jpeg?dl=1" title="Screenshot_20220629_120816" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ac95612c603fb72e7942427327b92b1e350c7ad_2_690x378.jpeg" alt="Screenshot_20220629_120816" data-base62-sha1="66vpHPLzL5vf6LQ2Npr0M6ZmFaZ" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ac95612c603fb72e7942427327b92b1e350c7ad_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ac95612c603fb72e7942427327b92b1e350c7ad_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ac95612c603fb72e7942427327b92b1e350c7ad_2_1380x756.jpeg 2x" data-dominant-color="666D89"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20220629_120816</span><span class="informations">1920×1054 93.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However when I deselect the segmentation labeled as airway, this is what I see<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f0c19358e6eb027d85b8b3018553c6487b3091c.png" data-download-href="/uploads/short-url/8ZK05L2LAlTVPZ5IPwC5OkvzYAs.png?dl=1" title="Screenshot_20220629_120620" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f0c19358e6eb027d85b8b3018553c6487b3091c_2_690x378.png" alt="Screenshot_20220629_120620" data-base62-sha1="8ZK05L2LAlTVPZ5IPwC5OkvzYAs" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f0c19358e6eb027d85b8b3018553c6487b3091c_2_690x378.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f0c19358e6eb027d85b8b3018553c6487b3091c_2_1035x567.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f0c19358e6eb027d85b8b3018553c6487b3091c_2_1380x756.png 2x" data-dominant-color="6B6D8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20220629_120620</span><span class="informations">2560×1405 327 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks for any help</p>

---

## Post #2 by @pieper (2022-06-29 13:31 UTC)

<p>That data is incorrectly formatted (the body is upside down).  This should never happen for dicom data or any data that’s been consistently processed.  Check the pipeline from scanner to slicer to correct any processing steps that might have introduced this issue.  We take coordinate system issues very seriously so if your research indicates there might be a bug in Slicer please report all the details so it can be investigated.</p>

---

## Post #3 by @ekmungi (2022-06-30 08:58 UTC)

<p>Thanks for the comment <a class="mention" href="/u/pieper">@pieper</a>. I received this data this way from my collaborating physician. I will check back with them.</p>
<p>But do you think this is causing the segmentation issues I described in my original post?</p>

---

## Post #4 by @ekmungi (2022-06-30 09:06 UTC)

<p><strong>Update</strong>:</p>
<p>I have 3 other datasets and I am having the same issue described in the original post. I could really use some help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Thank you.</p>

---

## Post #5 by @rbumm (2022-06-30 09:51 UTC)

<p>Hi,</p>
<p>This looks like a big “leak” from the airway segmentation. From your screenshot, it appears that your threshold sliders are all out of range.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bc5063dab17344f370e1b77c927035f6898656e.jpeg" data-download-href="/uploads/short-url/hEUQNJSAPZx2oOyiyL8jLzqdWH4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7bc5063dab17344f370e1b77c927035f6898656e_2_690x298.jpeg" alt="image" data-base62-sha1="hEUQNJSAPZx2oOyiyL8jLzqdWH4" width="690" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7bc5063dab17344f370e1b77c927035f6898656e_2_690x298.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7bc5063dab17344f370e1b77c927035f6898656e_2_1035x447.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7bc5063dab17344f370e1b77c927035f6898656e_2_1380x596.jpeg 2x" data-dominant-color="8F9091"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1905×823 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>set your upper lung threshold to -400 (should be almost always ok)</li>
<li>set your upper airway threshold to -800 (play with that between -900 and -700, see toolext help when you move your mouse over the slider)</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9d8391ba039d47bcb4f67552150a64044effc57.png" alt="image" data-base62-sha1="oevWNjFs70PEciuJksNSP4HaZUP" width="538" height="110"></p>
<p>If you have a large trachea, set airway segmentation → “low detail”<br>
With a normal trachea, set → medium detail" or even “high detail”.</p>
<p>We are working to get those fine-tuning parameters better preset, but once you find good thresholds for your scanner you should be ok.</p>

---

## Post #6 by @pieper (2022-06-30 13:16 UTC)

<aside class="quote no-group" data-username="ekmungi" data-post="3" data-topic="24102">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/e480ec/48.png" class="avatar"> ekmungi:</div>
<blockquote>
<p>But do you think this is causing the segmentation issues I described in my original post?</p>
</blockquote>
</aside>
<p>I think yes, the segmentation relies on the orientation being standard; maybe not but I think so.  You can use the Transforms module to rotate (or maybe flip) the data and then harden it before running the algorithm.  Together with the updates to the thresholds you should be okay.</p>

---

## Post #7 by @ekmungi (2022-06-30 17:36 UTC)

<p>Thanks for the feedback <a class="mention" href="/u/rbumm">@rbumm</a>. I tried the complete range you suggested, but unfortunately, that did not work. I can see the airways are being segmented. However, they are still combined with the Pleura.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e1925df8628b5e9921abb1790f82a75bbb7af68.jpeg" data-download-href="/uploads/short-url/fHYoRjysiNwmr8koXisdK8R5Df2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e1925df8628b5e9921abb1790f82a75bbb7af68_2_690x378.jpeg" alt="image" data-base62-sha1="fHYoRjysiNwmr8koXisdK8R5Df2" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e1925df8628b5e9921abb1790f82a75bbb7af68_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e1925df8628b5e9921abb1790f82a75bbb7af68_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e1925df8628b5e9921abb1790f82a75bbb7af68_2_1380x756.jpeg 2x" data-dominant-color="686F8B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1054 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a037b840e313841c1e6f9e470738b76e76b1537a.jpeg" data-download-href="/uploads/short-url/mRlM0gTtj1Jl7ZJcHdlYn92drnA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a037b840e313841c1e6f9e470738b76e76b1537a_2_690x378.jpeg" alt="image" data-base62-sha1="mRlM0gTtj1Jl7ZJcHdlYn92drnA" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a037b840e313841c1e6f9e470738b76e76b1537a_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a037b840e313841c1e6f9e470738b76e76b1537a_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a037b840e313841c1e6f9e470738b76e76b1537a_2_1380x756.jpeg 2x" data-dominant-color="6A6D89"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1054 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I tried the segmentation editor option (as explained in this <a href="https://www.youtube.com/watch?v=tJMGe3FMTk0" rel="noopener nofollow ugc">video</a>). It works but the segmentation quality is not so good. I can see the airways are being segmented nicely, but as you said there is a leak. But not sure how to find this out <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20">.</p>
<p>I haven’t tried the suggestion given by Steve yet.</p>

---

## Post #8 by @rbumm (2022-06-30 18:41 UTC)

<p>Sorry but I think I read a name on the dataset you provided above …<br>
Maybe you better delete that post?</p>
<p>Then do the following:<br>
Download Slicer´s lung demo dataset</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcb76283bf50b0cc11d822682568e5534d616cb8.png" alt="image" data-base62-sha1="vuxWvsTildClbpf2NUl7LmlLCs0" width="538" height="389"></p>
<p>and run the latest version of Lung CT Segmenter on this.<br>
Use these settings:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/3557d0e49d83dc8cdec41408237a667733606338.png" alt="image" data-base62-sha1="7BTrWXjLfzd0kCDIGlrZhuCAu24" width="542" height="428"></p>
<p>Will work <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"><br>
Then identify the difference between your patient volume and the demo dataset.<br>
Good luck !</p>

---

## Post #9 by @ekmungi (2022-07-20 03:57 UTC)

<p>Thanks <a class="mention" href="/u/rbumm">@rbumm</a>. Apologies for the delay in my reply. I can confirm that the sample dataset works. However, on the data I collected, it still has this issue.</p>
<p>I tried using the seed-based segmentation shown in this example(<a href="https://youtu.be/tJMGe3FMTk0" class="inline-onebox" rel="noopener nofollow ugc">Airway segmentation from CT in 1 minute using 3D Slicer - YouTube</a>). It works without segmenting the lung as part of the airway; however I am not happy with the details in the segmentation.</p>
<p>Any suggestions on how to proceed? Do you have any suggestions on alternate tools that I can try to segment my data?</p>
<p>Thanks!</p>

---

## Post #10 by @rbumm (2022-07-20 05:20 UTC)

<p>Could you share one of your non-working data sets on google drive or dropbox?</p>

---

## Post #11 by @D_Dand (2024-02-06 17:05 UTC)

<p>Thank you for your advice. I wonder if lung CT segmented can segment the upper airway?</p>

---

## Post #12 by @rbumm (2024-02-06 18:07 UTC)

<p>Depends a little bit on your dataset. You may experience leaks from nose and mouse if they are connected with air around the patient in your CT. You could still handle this issue by postprocessing.</p>

---

## Post #13 by @D_Dand (2024-02-06 19:28 UTC)

<p>Would you mind specifying what postprocessing step is? I had this issue when I tried with the upper airway. And is it possible to reconstruct the entire human airway (from the bronchi to the nasal cavity)? Would you suggest an efficient process?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31e875fbe12987ae9fe96e34e8c23097e334c385.jpeg" data-download-href="/uploads/short-url/77vrlTi8muENceYewkTSxqwBBtj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31e875fbe12987ae9fe96e34e8c23097e334c385_2_690x390.jpeg" alt="image" data-base62-sha1="77vrlTi8muENceYewkTSxqwBBtj" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31e875fbe12987ae9fe96e34e8c23097e334c385_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31e875fbe12987ae9fe96e34e8c23097e334c385_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31e875fbe12987ae9fe96e34e8c23097e334c385.jpeg 2x" data-dominant-color="B2B3B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1045×591 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e8427112cf7d29c1969860ce3b82c196b559bfd.jpeg" data-download-href="/uploads/short-url/6Dv69GglMtbLM4nbMVea0r2JvSl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e8427112cf7d29c1969860ce3b82c196b559bfd_2_690x371.jpeg" alt="image" data-base62-sha1="6Dv69GglMtbLM4nbMVea0r2JvSl" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e8427112cf7d29c1969860ce3b82c196b559bfd_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e8427112cf7d29c1969860ce3b82c196b559bfd_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e8427112cf7d29c1969860ce3b82c196b559bfd.jpeg 2x" data-dominant-color="AFB1B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1085×584 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b48fb4c24fa17ecaecef69453c7b0b1a5eff14c6.jpeg" data-download-href="/uploads/short-url/pLjPGclGzjtiZNIkpOprg0sCjmm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b48fb4c24fa17ecaecef69453c7b0b1a5eff14c6_2_690x377.jpeg" alt="image" data-base62-sha1="pLjPGclGzjtiZNIkpOprg0sCjmm" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b48fb4c24fa17ecaecef69453c7b0b1a5eff14c6_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b48fb4c24fa17ecaecef69453c7b0b1a5eff14c6_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b48fb4c24fa17ecaecef69453c7b0b1a5eff14c6.jpeg 2x" data-dominant-color="B2B2B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1085×593 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @rbumm (2024-02-09 13:51 UTC)

<p>I would go into the Segment Editor → Islands effect and select check “Remove selected island”, then click on the blue air around your segmentation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1c52cfff3a5faeaf5190606ec98ea0e32dfdcf8.jpeg" data-download-href="/uploads/short-url/pmCXu3fKWeKv84jLWHEccBgQBvy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1c52cfff3a5faeaf5190606ec98ea0e32dfdcf8_2_690x299.jpeg" alt="image" data-base62-sha1="pmCXu3fKWeKv84jLWHEccBgQBvy" width="690" height="299" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1c52cfff3a5faeaf5190606ec98ea0e32dfdcf8_2_690x299.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1c52cfff3a5faeaf5190606ec98ea0e32dfdcf8_2_1035x448.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1c52cfff3a5faeaf5190606ec98ea0e32dfdcf8_2_1380x598.jpeg 2x" data-dominant-color="ADB0B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×832 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and check out what remains.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9ae836c0a7952cf1328ca783eba450b9b2d9dc5.jpeg" data-download-href="/uploads/short-url/zCMMz1YmhWj2gMHeKuK7BEyTOZf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9ae836c0a7952cf1328ca783eba450b9b2d9dc5_2_690x276.jpeg" alt="image" data-base62-sha1="zCMMz1YmhWj2gMHeKuK7BEyTOZf" width="690" height="276" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9ae836c0a7952cf1328ca783eba450b9b2d9dc5_2_690x276.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9ae836c0a7952cf1328ca783eba450b9b2d9dc5_2_1035x414.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9ae836c0a7952cf1328ca783eba450b9b2d9dc5_2_1380x552.jpeg 2x" data-dominant-color="A6A6AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1909×764 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @D_Dand (2024-02-12 22:56 UTC)

<p>Very helpful! Thank you!</p>

---
