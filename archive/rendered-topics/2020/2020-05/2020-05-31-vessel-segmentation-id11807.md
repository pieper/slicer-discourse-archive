---
topic_id: 11807
title: "Vessel Segmentation"
date: 2020-05-31
url: https://discourse.slicer.org/t/11807
---

# Vessel segmentation

**Topic ID**: 11807
**Date**: 2020-05-31
**URL**: https://discourse.slicer.org/t/vessel-segmentation/11807

---

## Post #1 by @cotozakot (2020-05-31 15:04 UTC)

<p>Hey!  I need help because I’m just starting with Slicer3D.  I have to segment the carotid arteries from CT images (80kV and 140kV).  All images with contrast.  I tried with Vesselness Filtering but did not get the expected results.  Can somebody help me and explain how to do it?<br>
Below is a photo of what I was able to do manually (tiring and not accurate)<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32c8d84ed06ecab6a60c702166490ab4131361f6.jpeg" data-download-href="/uploads/short-url/7fgbh1FOjIIddaYqT5TCmPhNzAa.jpeg?dl=1" title="IMG_20200531_112459" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32c8d84ed06ecab6a60c702166490ab4131361f6_2_666x500.jpeg" alt="IMG_20200531_112459" data-base62-sha1="7fgbh1FOjIIddaYqT5TCmPhNzAa" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32c8d84ed06ecab6a60c702166490ab4131361f6_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32c8d84ed06ecab6a60c702166490ab4131361f6_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32c8d84ed06ecab6a60c702166490ab4131361f6_2_1332x1000.jpeg 2x" data-dominant-color="717072"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20200531_112459</span><span class="informations">2000×1500 541 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2020-05-31 17:30 UTC)

<p>I have rather quick and good results with FloodFilling from SlicerSegmentEditorExtraEffects available as an extension.</p>
<p>With ‘Intensity tolerance’ between 90 and 130, and ‘Neighbourhood size’ between 2 and 5, a few clicks on the contrast media would isolate the lumen quite nicely. The result is not perfect for things like 3D printing. Many factors influence the result, like the contrast homogeneity, proximity of bones and too much contrast in the veins. In fact, I rarely do that for the carotids (for surgical planning).</p>
<p>There are certainly other techniques, it’s the fastest I’ve seen and I found it quite reliable.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ec7b4da7fc567dc7269407e70ff9981a8230b8f.jpeg" data-download-href="/uploads/short-url/i5y1SPcDs6EpKuoizRYhQq1B8pV.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ec7b4da7fc567dc7269407e70ff9981a8230b8f_2_649x500.jpeg" alt="Screenshot" data-base62-sha1="i5y1SPcDs6EpKuoizRYhQq1B8pV" width="649" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ec7b4da7fc567dc7269407e70ff9981a8230b8f_2_649x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ec7b4da7fc567dc7269407e70ff9981a8230b8f_2_973x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ec7b4da7fc567dc7269407e70ff9981a8230b8f.jpeg 2x" data-dominant-color="3B3735"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1212×933 333 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @cotozakot (2020-05-31 17:58 UTC)

<p>Thank you very much for your answer! Could I ask for accurate information about FloodFilling from SlicerSegmentEditorExtraEffects. Where can I find this extension? How to use it?</p>
<p>niedz., 31 maj 2020, 19:41 użytkownik SET via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; napisał:</p>

---

## Post #4 by @chir.set (2020-05-31 18:37 UTC)

<p>The simplest way to install an extension is, well, using the ‘Extension manager’ menu.</p>
<p>Using it is straightforward :</p>
<ul>
<li>Go to the ‘Segment Editor’ module</li>
<li>Add a new segment</li>
<li>Select Flood Filling tool</li>
<li>Set its two parameters as stated above</li>
<li>Click on the contrast in the 2D views, a few clicks might be needed</li>
</ul>
<p>Undo if necessary, and adjust the two parameters of Flood Filling.<br>
Destroy everything and start again.</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:"></p>

---

## Post #5 by @harrykwon0524 (2022-07-21 18:14 UTC)

<p>Hi i have just got into the 3d slicer program and have been working on the same topic(vessel segmentation) I tried to follow your instructions on the post and had question on doing the contrast in 2d views. What does this step mean and how should I perform this? Your answer would make my day. Thank you</p>

---

## Post #6 by @chir.set (2022-07-22 06:58 UTC)

<aside class="quote no-group" data-username="harrykwon0524" data-post="5" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/harrykwon0524/48/16121_2.png" class="avatar"> harrykwon0524:</div>
<blockquote>
<p>had question on doing the contrast in 2d views</p>
</blockquote>
</aside>
<p>Please check <a href="https://disk.yandex.com/i/g3HwiJnwgu7QYw" rel="noopener nofollow ugc">this</a> short video.</p>

---

## Post #7 by @rbumm (2022-07-22 10:45 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="2" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>I rarely do that for the carotids (for surgical planning)</p>
</blockquote>
</aside>
<p>What are you doing for the carotids? Thank you for this interesting thread.</p>

---

## Post #8 by @chir.set (2022-07-22 21:06 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="7" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>What are you doing for the carotids?</p>
</blockquote>
</aside>
<p>I’ll detail a reply when I resume work from summer vacation, too complicated now, sorry.</p>

---

## Post #9 by @chir.set (2022-07-31 18:45 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="7" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>What are you doing for the carotids?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>In general, when we receive patients in consultation, carotid stenosis assessment has already been worked out by duplex ultrasound in the hands of the angiologist here (or radiologist in many countries), or with automatic measurements on the radiologist’s platform.</p>
<p>I use Slicer to analyze all four supra-aortic trunks entirely, using slice views and volume rendering.</p>
<p>Reformatting the slice views with intersection and interaction activated is fast and very handy.</p>
<p>Volume rendering gives a 3D synthetic summary of the arterial status that neither slice views nor traditional angiograms can produce. The picture below shows <em>main</em> information obtained from volume rendering at a single glance. Combining the 3D view and placing slice views precisely with ‘Shift + mouse move’ become more informational to the surgeon at targeted places.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d0e7b955a3084c5a41abcdd81460ab2e1d8e26b.jpeg" data-download-href="/uploads/short-url/k7QlQVasQEPPMN9kASlvoqFxqKn.jpeg?dl=1" title="carotid_bifurcation_3D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d0e7b955a3084c5a41abcdd81460ab2e1d8e26b_2_690x494.jpeg" alt="carotid_bifurcation_3D" data-base62-sha1="k7QlQVasQEPPMN9kASlvoqFxqKn" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d0e7b955a3084c5a41abcdd81460ab2e1d8e26b_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d0e7b955a3084c5a41abcdd81460ab2e1d8e26b_2_1035x741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d0e7b955a3084c5a41abcdd81460ab2e1d8e26b.jpeg 2x" data-dominant-color="736345"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">carotid_bifurcation_3D</span><span class="informations">1215×871 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To analyze the Willis circle, volume rendering is gold. It cannot be studied in an efficient way, even less in a reproducible way, with slice views only. The arteries of the circle of Willis are tiny, and intensities of veins in the skull are quite close to those of the arteries (fortunately, veins in the skull are not satellite to the arteries). The picture below shows these very well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83b9e935cb3c730b00e6fca247ae9566c214c9fa.jpeg" data-download-href="/uploads/short-url/iNiRnUL9xTMRRCfvCGpmD0raazU.jpeg?dl=1" title="Willis_Circle" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83b9e935cb3c730b00e6fca247ae9566c214c9fa_2_690x494.jpeg" alt="Willis_Circle" data-base62-sha1="iNiRnUL9xTMRRCfvCGpmD0raazU" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83b9e935cb3c730b00e6fca247ae9566c214c9fa_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83b9e935cb3c730b00e6fca247ae9566c214c9fa_2_1035x741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83b9e935cb3c730b00e6fca247ae9566c214c9fa.jpeg 2x" data-dominant-color="A57F62"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Willis_Circle</span><span class="informations">1215×871 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>More recently, it is possible to <em>draw</em> a theoretical arterial <a href="https://github.com/chir-set/ExtraMarkups/tree/main/Shape/" rel="noopener nofollow ugc">wall</a> around the plaque. It’s manual, completely observer dependent. This allows a better comprehension of the carotid bulb, as shown below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4fda987fb27be1c79ae915b2c0e0dd687dfdaca.jpeg" data-download-href="/uploads/short-url/s6F3hQXVID9GWkdop6OKD3r17Qe.jpeg?dl=1" title="Theoretical_Wall" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4fda987fb27be1c79ae915b2c0e0dd687dfdaca_2_690x494.jpeg" alt="Theoretical_Wall" data-base62-sha1="s6F3hQXVID9GWkdop6OKD3r17Qe" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4fda987fb27be1c79ae915b2c0e0dd687dfdaca_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4fda987fb27be1c79ae915b2c0e0dd687dfdaca_2_1035x741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4fda987fb27be1c79ae915b2c0e0dd687dfdaca.jpeg 2x" data-dominant-color="0D1120"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Theoretical_Wall</span><span class="informations">1215×871 76.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The latter becomes very handy to <em>help</em> measuring the maximum stenosis should the need arise (discrepancy between results given by the angiologist and the radiologist, or surgeon disagreeing with both, or a requirement of clinical studies on patient groups, or …). We can use the many tools available in SlicerWMTK extension for this, as shown below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f6d0129c8902f8aa21bde3b8b3b50ad5f6e9df0.jpeg" data-download-href="/uploads/short-url/4u0lfv0pQrzro8JFG0oqVqV221G.jpeg?dl=1" title="Measurements_1D_2D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f6d0129c8902f8aa21bde3b8b3b50ad5f6e9df0_2_668x500.jpeg" alt="Measurements_1D_2D" data-base62-sha1="4u0lfv0pQrzro8JFG0oqVqV221G" width="668" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f6d0129c8902f8aa21bde3b8b3b50ad5f6e9df0_2_668x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f6d0129c8902f8aa21bde3b8b3b50ad5f6e9df0_2_1002x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f6d0129c8902f8aa21bde3b8b3b50ad5f6e9df0.jpeg 2x" data-dominant-color="302E39"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Measurements_1D_2D</span><span class="informations">1196×894 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f23ab38cdfa1e762e6240db51a87de2c00a7ceb.png" alt="Measurement_1D_Results" data-base62-sha1="kqgHiEIG60zxGCL6x9c1UI9k6AH" width="671" height="350"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ae2ea923d43af57f2fc30f014dcf40963c49a98.png" data-download-href="/uploads/short-url/m6bHaPGSkfBW7nGXzzO3JdTOSfu.png?dl=1" title="Measurement_2D_Results" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ae2ea923d43af57f2fc30f014dcf40963c49a98_2_657x500.png" alt="Measurement_2D_Results" data-base62-sha1="m6bHaPGSkfBW7nGXzzO3JdTOSfu" width="657" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ae2ea923d43af57f2fc30f014dcf40963c49a98_2_657x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ae2ea923d43af57f2fc30f014dcf40963c49a98.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ae2ea923d43af57f2fc30f014dcf40963c49a98.png 2x" data-dominant-color="383838"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Measurement_2D_Results</span><span class="informations">671×510 39 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If we don’t need to measure anything using segments, everything is quickly done. Else, it takes some or much time, and should not and cannot be done for every patient.</p>
<p>In the future, I’ll probably try to exploit the custom Shape markups in a yet-to-be-created module, to measure a short stenosis in 3D. It takes time, which is a significant factor for all of us. I’ve got some vague ideas for now. To my knowledge (vascular surgery is far reaching too!), 3D stenosis measurement has not been used clinically yet. So it might be one more tool to investigate, whatever it may finally worth.</p>
<p>Regards.</p>

---

## Post #10 by @rbumm (2022-07-31 20:29 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> .</p>
<p>This is stunning, beautiful work. Thank you !<br>
I use volume rendering (CT-Muscle preset)  a lot these days for pulmonary vessels. Maybe we can bundle our efforts.</p>
<p>Many questions arise, two may be trivial:<br>
How do you add the label texts with arrows and the orientation figure ?</p>
<p>BTW Surgeons never disagree.</p>

---

## Post #11 by @chir.set (2022-07-31 21:41 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="10" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>How do you add the label texts with arrows and the orientation figure ?</p>
</blockquote>
</aside>
<p>The label texts are from a <a href="https://github.com/chir-set/ExtraMarkups/tree/main/Label/" rel="noopener nofollow ugc">custom</a> Markups. Here, there’s one node for one arrow. It’s not perfect, yet sufficiently helpful.</p>
<p>The orientation marker is Slicer built-in, see ‘Application settings/Views’.</p>

---

## Post #12 by @rbumm (2022-08-01 16:12 UTC)

<p>Nice. Thank you <a class="mention" href="/u/chir.set">@chir.set</a> .</p>
<aside class="quote no-group" data-username="chir.set" data-post="11" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>The label texts are from a <a href="https://github.com/chir-set/ExtraMarkups/tree/main/Label/">custom </a> Markups</p>
</blockquote>
</aside>
<p>How are you supposed to implement those? During a Slicer build?</p>

---

## Post #13 by @chir.set (2022-08-01 17:03 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="12" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>How are you supposed to implement those?</p>
</blockquote>
</aside>
<p>Slicer must be built first, then any extension can be built against the Slicer build tree and packaged. I understood from previous posts that you are fluent with C++, so it should not be a problem for you.</p>
<p>In any case, it’s quite straightforward on Linux :</p>
<pre><code class="lang-auto">cd ExtraMarkups
mkdir build
cd $_
cmake -DSlicer_DIR:PATH=/path/to/src/Slicer-SuperBuild/Slicer-build -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo ../
make -j8
make package
</code></pre>

---

## Post #14 by @Redalligator291 (2023-09-19 02:52 UTC)

<p>Hi guys, I just stumbled upon this page, and for good reason. I have to segment the carotid arteries in a t2-weighted MRI (no contrast), and I am having trouble doing that. Does anybody have any ways I can do that?</p>

---

## Post #15 by @chir.set (2023-09-19 06:11 UTC)

<aside class="quote no-group" data-username="Redalligator291" data-post="14" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/a9a28c/48.png" class="avatar"> Redalligator291:</div>
<blockquote>
<p>segment the carotid arteries in a t2-weighted MRI (no contrast)</p>
</blockquote>
</aside>
<p>Can you provide your volume stripped of any patient/clinician information? It’s hard to guess things based on vague descriptions.</p>
<p>(You could also start a new thread for specific requests.)</p>

---

## Post #16 by @Redalligator291 (2023-09-19 22:41 UTC)

<p>I’m not really sure what you mean by volume. I got the images from the OASIS-3 dataset. Let me provide a few screenshots of my data.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85a0d664b7a21301c951767ee3a95d29202285e9.jpeg" data-download-href="/uploads/short-url/j485Y3EkyEDFFEkgdyjTSe8VpDr.jpeg?dl=1" title="Screenshot 2023-09-19 154124" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85a0d664b7a21301c951767ee3a95d29202285e9_2_689x486.jpeg" alt="Screenshot 2023-09-19 154124" data-base62-sha1="j485Y3EkyEDFFEkgdyjTSe8VpDr" width="689" height="486" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85a0d664b7a21301c951767ee3a95d29202285e9_2_689x486.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85a0d664b7a21301c951767ee3a95d29202285e9_2_1033x729.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85a0d664b7a21301c951767ee3a95d29202285e9.jpeg 2x" data-dominant-color="3B3C48"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-19 154124</span><span class="informations">1240×875 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @mikebind (2023-09-19 23:01 UTC)

<p>Slicer (somewhat confusingly) uses the term “volume” as short for “image volume”, meaning (typically) a 3D array of voxels with a location in a spatial coordinate system.  If your image data set is public, a link to where someone could get the data to help you is what <a class="mention" href="/u/chir.set">@chir.set</a> was suggesting.</p>

---

## Post #18 by @Redalligator291 (2023-09-19 23:03 UTC)

<p>Oh yeah sorry for not providing the link. This is the link: <a href="https://www.oasis-brains.org/#" class="inline-onebox" rel="noopener nofollow ugc">OASIS Brains - Open Access Series of Imaging Studies</a></p>

---

## Post #19 by @chir.set (2023-09-20 06:37 UTC)

<p>Nothing could be downloaded there, it’s getting too complicated.</p>

---

## Post #20 by @Redalligator291 (2023-09-20 23:59 UTC)

<p>Ok. I forgot to mention this but you have to request access from the people, even though it is a public dataset. So let me attach a drive link with some of the data: <a href="https://drive.google.com/drive/folders/1fA54bkKKeS9txM9oYLjtY41HuVLPYnbc?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">OASIS-3 T2 dataset - Google Drive</a></p>

---

## Post #21 by @chir.set (2023-09-21 15:09 UTC)

<aside class="quote no-group" data-username="Redalligator291" data-post="20" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/a9a28c/48.png" class="avatar"> Redalligator291:</div>
<blockquote>
<p>some of the data</p>
</blockquote>
</aside>
<p>I found sub-OAS30001_ses-d0757_T2w more suitable for tinkering. And it’s really that, because these studies target the brain and not blood vessels.</p>
<p>Without contrast, it is difficult to identify veins and arteries in slice views, at bifurcations namely.</p>
<p>You may use the ‘Grow from seeds’ effect of the ‘Segment editor’. Place seeds with 2 segments like below in a few slices where you can identify the structures of interest.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06f19f4a433103698dc64ee996088b3f5765a0a3.png" data-download-href="/uploads/short-url/ZqxmhTuQG5lW0j95iAvkEzCbgn.png?dl=1" title="Seeding" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06f19f4a433103698dc64ee996088b3f5765a0a3_2_386x500.png" alt="Seeding" data-base62-sha1="ZqxmhTuQG5lW0j95iAvkEzCbgn" width="386" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06f19f4a433103698dc64ee996088b3f5765a0a3_2_386x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06f19f4a433103698dc64ee996088b3f5765a0a3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06f19f4a433103698dc64ee996088b3f5765a0a3.png 2x" data-dominant-color="2D2D2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Seeding</span><span class="informations">480×621 54.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The green is the target structure, the yellow for anything else. Preview, fix with more seeds and apply. I could thus get the result below. Arteries and veins are fused. Each seeding will produce its unique result.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a1e0118a92226dfff1fba87563c8d51e14d7152.png" data-download-href="/uploads/short-url/f8KTxfsQ576Hn9AXwyPkqb6eYhQ.png?dl=1" title="With_Grow_From_Seeds" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a1e0118a92226dfff1fba87563c8d51e14d7152_2_579x500.png" alt="With_Grow_From_Seeds" data-base62-sha1="f8KTxfsQ576Hn9AXwyPkqb6eYhQ" width="579" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a1e0118a92226dfff1fba87563c8d51e14d7152_2_579x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a1e0118a92226dfff1fba87563c8d51e14d7152.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a1e0118a92226dfff1fba87563c8d51e14d7152.png 2x" data-dominant-color="0D0E0C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">With_Grow_From_Seeds</span><span class="informations">720×621 61.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You may also try ‘<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/GuidedVeinSegmentation.md" rel="noopener nofollow ugc">Guided vein segmentation</a>’ in SlicerVMTK extension. Place an open curve following what you identify as the carotid artery, set parameters and apply. I could get the result below. Better, but not much extensible towards the the skull.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac520e2562945d373739138b75d6accccfad696b.png" data-download-href="/uploads/short-url/oApVvipsLJ5YURjnt6bRJe8xQxB.png?dl=1" title="With_Guided_Vein_Segmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac520e2562945d373739138b75d6accccfad696b_2_579x500.png" alt="With_Guided_Vein_Segmentation" data-base62-sha1="oApVvipsLJ5YURjnt6bRJe8xQxB" width="579" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac520e2562945d373739138b75d6accccfad696b_2_579x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac520e2562945d373739138b75d6accccfad696b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac520e2562945d373739138b75d6accccfad696b.png 2x" data-dominant-color="0B0A08"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">With_Guided_Vein_Segmentation</span><span class="informations">720×621 47.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Overall, figuratively, it’s spending time trying to create a valuable byproduct from waste material. Sometimes we have good results, sometimes not. It’s better to use series that study the carotids specifically, if possible.</p>

---

## Post #22 by @Redalligator291 (2023-09-22 01:33 UTC)

<p>Thanks, this has been really helpful. I am just having a bit of trouble knowing exactly where to place the seeds. When I placed the seeds I got nothing like what you got for the 3d. Maybe can you show me where you placed the seeds in the image? and also how do you use the guided vein segmentation. It always asks me for an open curve and I have know idea what that is. Can you please explain to me what that is?</p>

---

## Post #23 by @chir.set (2023-09-22 12:21 UTC)

<aside class="quote no-group" data-username="Redalligator291" data-post="22" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/a9a28c/48.png" class="avatar"> Redalligator291:</div>
<blockquote>
<p>Maybe can you show me where you placed the seeds in the image?</p>
</blockquote>
</aside>
<p>Well I might not be understanding your question in full.</p>
<p>You want to segment the carotids. Identify these while scrolling in slice views. Every time you think a structure is the carotid, place a seed there with the ‘Paint’ effect of the segment editor. And all around it, a few seeds of another segment that target anything around. The <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06f19f4a433103698dc64ee996088b3f5765a0a3.png" rel="noopener nofollow ugc">first</a> image is explicit.</p>
<p>The seeding step is totally on you, as well as refining the preview with more seeds.</p>
<p>This is <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#grow-from-seeds" rel="noopener nofollow ugc">one</a> method where you do everything by yourself. If you go for the second method referenced above, it’s globally less demanding and the result may be more satisfactory.</p>

---

## Post #24 by @Redalligator291 (2023-09-23 00:56 UTC)

<p>Yeah my question was kinda phrased bad. I am really new to medical imaging and so I have no idea if I am being honest where the carotid arteries are in the image, so I was thinking if you could like export the  “seeds” drawing (segmentation) so I then can just download that and then use the grow from seeds to replicate what you did in the second image.</p>

---

## Post #25 by @chir.set (2023-09-23 09:53 UTC)

<aside class="quote no-group" data-username="Redalligator291" data-post="24" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/a9a28c/48.png" class="avatar"> Redalligator291:</div>
<blockquote>
<p>export the “seeds” drawing (segmentation)</p>
</blockquote>
</aside>
<p><a href="https://disk.yandex.com/d/5esOr0RULY2jvg" rel="noopener nofollow ugc">Here</a> is an MRB file with the seeds. It contains the initial seeds and those that refine the preview.</p>
<p>Remember that every seeding gives a unique result, so the final result is different from that in the second image above, better in this case.</p>
<p>You should probably do some training with datasets that study blood vessels. In the sample module of Slicer, CTA-cardio is a good starting point. Learning segmentation from inadequate volumes will be much deceiving, it’s like trying to run before learning to walk.</p>

---

## Post #26 by @Redalligator291 (2023-09-23 23:21 UTC)

<p>Thanks this has been really helpful. Is this all the segmentation you did, because when I download your .mrb I only get a little of bit what you got for the second image</p>

---

## Post #27 by @chir.set (2023-09-24 06:49 UTC)

<aside class="quote no-group" data-username="Redalligator291" data-post="26" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/a9a28c/48.png" class="avatar"> Redalligator291:</div>
<blockquote>
<p>Is this all the segmentation you did</p>
</blockquote>
</aside>
<p>It’s just the seeding that you requested. You must then select ‘Grow from seeds’ effect in the ‘Segment editor’ module, preview, fix with more seeds as required and apply.</p>
<p>You’ll get more encouraging results if you play with contrast enhanced CT scans.</p>

---

## Post #28 by @Redalligator291 (2023-09-24 15:28 UTC)

<p>Ok, thank you. Is there a way to apply contrast to the t2 weighted images I already have now?</p>

---

## Post #29 by @chir.set (2023-09-24 17:46 UTC)

<aside class="quote no-group" data-username="Redalligator291" data-post="28" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/a9a28c/48.png" class="avatar"> Redalligator291:</div>
<blockquote>
<p>apply contrast to the t2 weighted images I already have now</p>
</blockquote>
</aside>
<p>No, applying contrast  is a physical event. It is injected in the subject’s vein by the assistant of the radiologist. It’s loaded in the injector device that is remotely controlled. That holds true for both MRI and CT scans, though different products.</p>

---

## Post #30 by @Redalligator291 (2023-10-06 02:53 UTC)

<p>Hi. I’m back once again. I am trying to segment the carotid arteries in an MRA (Magnetic Resonance Angiogram), and I have about 900 images in the dataset. I was using the threshold effect from SegmentEditorExtraEffect, but it isn’t accurate, and every time, I have to use the scissors function and delete some of the unnecessary junk from the threshold. And this take me about thirty minutes to do for each image, and so to do it for about 900 images, it would take ages, and I am kinda of in a time cramp right now, so I was wondering if there are other ways to segment the carotid arteries in an MRA much faster than the way I am doing right now. Maybe there is an extension on github I can download and then upload to 3d slicer and use that? If anyone wants to view my data I will provide a link to some of it: <a href="https://drive.google.com/drive/folders/1N_E6AB1d0z29d4fbikXRnCayXcKQVIJP?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">OASIS-3 Angiogram Dataset - Google Drive</a></p>

---

## Post #31 by @chir.set (2023-10-06 18:32 UTC)

<aside class="quote no-group" data-username="Redalligator291" data-post="30" data-topic="11807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/a9a28c/48.png" class="avatar"> Redalligator291:</div>
<blockquote>
<p>much faster</p>
</blockquote>
</aside>
<p>Using sub-OAS30001_ses-d2430_acq-TOF_angio_1, I could get all contrasted arteries with the ‘Threshold’ effect of the ‘Segment editor’, and it’s really fast. The noise can easily be removed using the ‘Islands’ effect with ‘Keep selected island’. The online manual will help you concerning how these effects should be used.</p>

---

## Post #32 by @Redalligator291 (2023-10-07 01:10 UTC)

<p>OH MY GOD. Thank you so MUCH. That was so helpful. Now each image takes like 30 sec</p>

---

## Post #33 by @Redalligator291 (2023-10-14 01:47 UTC)

<p>Hi. I have another quick question. I am trying to save both the original image and the segmentation into one file. How is that possible? The only way I am seeing is mrb, but I need either a Dicom file format or NIFTI. So if you know any way to do this please help me out!</p>

---

## Post #34 by @seraphkz (2023-11-27 05:40 UTC)

<p>How does your volume rendering look so good? And how do you make the vessels a different color?</p>

---

## Post #35 by @chir.set (2023-11-27 09:19 UTC)

<p><a class="mention" href="/u/seraphkz">@seraphkz</a></p>
<p>You will benefit from an in-depth dive in the ‘<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" rel="noopener nofollow ugc">Segment Editor</a>’ documentation.</p>

---

## Post #36 by @lradams1970 (2025-01-07 05:55 UTC)

<p>I just wanted to say THANK YOU for this entire thread!! I am SMAS (Superior Mesenteric Artery Syndrome) survivor who is 3 years post op and was recently diagnosed with Nutcracker Syndrome. I decided this time around I wanted to understand the compression better. A few searches later sent me down the road of 3D Slicer and then into different segmentation methods. I have gotten ok “for a newbie” at using the full body segmentation AI tools. Now that I am “starting” to understand the concepts of the tool, file structures, and extensions, I have started to focus on how best to visualize/render the compression of my left renal vein by SMA/Aorta branch based on my set of CT scans.  I don’t have any questions at this time I just wanted to thank you for all of the detailed information you have included. It is helping me understand and put the pieces together.</p>

---
