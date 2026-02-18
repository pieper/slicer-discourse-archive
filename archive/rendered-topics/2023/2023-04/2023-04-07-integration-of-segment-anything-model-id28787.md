# Integration of “Segment Anything Model”?

**Topic ID**: 28787
**Date**: 2023-04-07
**URL**: https://discourse.slicer.org/t/integration-of-segment-anything-model/28787

---

## Post #1 by @Dominick_Dickerson (2023-04-07 03:36 UTC)

<p>Hi all,</p>
<p>Wondering if there’s a way to get the new open source segment anything model that meta ai released recently integrated into the AIAA server?</p>
<p>The model seems incredibly powerful and integration with Slicer seems like it would be a godsend to those of us in the natural history space utilizing Slicer for things beyond human/mouse scans.</p>

---

## Post #2 by @pieper (2023-04-07 13:53 UTC)

<p>It should be pretty easy to integrate, but does anyone know if it would work well on 3D data?  I’d be afraid that each slice would segment differently and you’d end up with jagged segmentations in 3D.</p>

---

## Post #3 by @Dominick_Dickerson (2023-04-07 17:51 UTC)

<p>Maybe?</p>
<p>My thought was that I could pretty easily import an image of a single slice into the model and using the segment from prompt functionality was able to mask out the outline of entire organs trivially.</p>
<p>Youre right that as currently implemented the automatic mask generator in SAM doesnt really have a way to insure that fidelity of a given segment between multiple slices in the image stack so I doubt  it would function as a unsupervised tool right out the gate.</p>
<p>But my concept would be to use the prompt based segmentation as part of a semi-supervised work flow.  Once an adequate number of semi-supervised human expert verified segmentations have been generated,  that data can be used to generate taxon specific training sets to further refine the model.</p>

---

## Post #4 by @dzenanz (2023-04-07 18:11 UTC)

<p>The prompt for a segmentation can be a mask. For 3D images it would be reasonable to have the user segment one slice, then use that slice’s segmentation as a prompt to segment adjacent slices, and so on recursively. Some special logic would be needed to handle multiple user-segmented slices, which would be needed if the single slice initialized segmentation is not satisfactory.</p>
<p>I tried it, and it works well on dental xrays and slices from CT and MR images.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2868b80a8c32b47966dfc973e70c5336f925b65d.png" data-download-href="/uploads/short-url/5LtsoK7Cy00b2qIpcwm9Oe1wWO9.png?dl=1" title="dzzSlice" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2868b80a8c32b47966dfc973e70c5336f925b65d.png" alt="dzzSlice" data-base62-sha1="5LtsoK7Cy00b2qIpcwm9Oe1wWO9" width="500" height="500" data-dominant-color="1F1F1F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dzzSlice</span><span class="informations">512×512 97.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Its automatic segmentation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/118f929f615819764f7a1fa35fdc9058e37b1ce6.png" data-download-href="/uploads/short-url/2vlIEo0gPFPVfK63EQ1gBz7yERM.png?dl=1" title="segment-anything.com_demo" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/118f929f615819764f7a1fa35fdc9058e37b1ce6_2_500x500.png" alt="segment-anything.com_demo" data-base62-sha1="2vlIEo0gPFPVfK63EQ1gBz7yERM" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/118f929f615819764f7a1fa35fdc9058e37b1ce6_2_500x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/118f929f615819764f7a1fa35fdc9058e37b1ce6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/118f929f615819764f7a1fa35fdc9058e37b1ce6.png 2x" data-dominant-color="574742"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segment-anything.com_demo</span><span class="informations">512×512 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Hovering with mouse segments vertebral bodies and disks well.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb8bfe687edc064ece53baf92d04d190afee7e1d.png" data-download-href="/uploads/short-url/zThMnLLjcmlGwIeKNqYLGVTFDel.png?dl=1" title="Screenshot 2023-04-07 14.08.06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb8bfe687edc064ece53baf92d04d190afee7e1d.png" alt="Screenshot 2023-04-07 14.08.06" data-base62-sha1="zThMnLLjcmlGwIeKNqYLGVTFDel" width="500" height="500" data-dominant-color="1F1F20"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-04-07 14.08.06</span><span class="informations">512×512 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e70ad626ed17ae12b1cecd024ea8c7b5e6f8171.png" data-download-href="/uploads/short-url/mBCQIxygAuYzv2786mDRT8n1N05.png?dl=1" title="Screenshot 2023-04-07 14.09.02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e70ad626ed17ae12b1cecd024ea8c7b5e6f8171.png" alt="Screenshot 2023-04-07 14.09.02" data-base62-sha1="mBCQIxygAuYzv2786mDRT8n1N05" width="500" height="500" data-dominant-color="1F1F1F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-04-07 14.09.02</span><span class="informations">512×512 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @Dominick_Dickerson (2023-04-07 22:41 UTC)

<p>Could it use a similar logic to what is used during the “fill between slices” tool to handle multiple slices?</p>

---

## Post #6 by @muratmaga (2023-04-07 22:43 UTC)

<p>At the minimum it would be a great seeding tool for fill between the slices.</p>

---

## Post #7 by @Dominick_Dickerson (2023-04-07 23:44 UTC)

<p>Exactly my thoughts.</p>

---

## Post #8 by @muratmaga (2023-04-08 05:11 UTC)

<p>I can only use it via a screen capture module snapshots, and while playing with window/level settings, it seems to capture different features. These are all same slice. I couldn’t figure out how to do multiple masks manually. All from automatic parsing of the images.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2bd4d0c384ba236c3b22fb95e4120c00571234a.jpeg" data-download-href="/uploads/short-url/wlPtZCXN9ReAtnDreZT1dLoZSNs.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2bd4d0c384ba236c3b22fb95e4120c00571234a_2_690x285.jpeg" alt="image" data-base62-sha1="wlPtZCXN9ReAtnDreZT1dLoZSNs" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2bd4d0c384ba236c3b22fb95e4120c00571234a_2_690x285.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2bd4d0c384ba236c3b22fb95e4120c00571234a_2_1035x427.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2bd4d0c384ba236c3b22fb95e4120c00571234a.jpeg 2x" data-dominant-color="574A46"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1241×513 64.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/185840778edecc84599d1a19afc9494cf7698c0b.jpeg" data-download-href="/uploads/short-url/3tmxlT6zWsC8TbpDlcAYLCk1Rcn.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/185840778edecc84599d1a19afc9494cf7698c0b_2_690x278.jpeg" alt="image" data-base62-sha1="3tmxlT6zWsC8TbpDlcAYLCk1Rcn" width="690" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/185840778edecc84599d1a19afc9494cf7698c0b_2_690x278.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/185840778edecc84599d1a19afc9494cf7698c0b_2_1035x417.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/185840778edecc84599d1a19afc9494cf7698c0b.jpeg 2x" data-dominant-color="312D30"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1090×440 81.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e86e055162691ad2b6c747642a5355b898aafd7.jpeg" data-download-href="/uploads/short-url/24vEEB56jDSymRq4hSUmV2kYQjd.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e86e055162691ad2b6c747642a5355b898aafd7_2_690x301.jpeg" alt="image" data-base62-sha1="24vEEB56jDSymRq4hSUmV2kYQjd" width="690" height="301" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e86e055162691ad2b6c747642a5355b898aafd7_2_690x301.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e86e055162691ad2b6c747642a5355b898aafd7_2_1035x451.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e86e055162691ad2b6c747642a5355b898aafd7.jpeg 2x" data-dominant-color="89888B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1102×482 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @Dominick_Dickerson (2023-04-08 17:54 UTC)

<p>That’s about where I am with it running it through google colab and just seeing how the model behaves with cephalopod contrast enhanced CT images.</p>
<p>Unfortunately I’m not in the position to host my own server for implementing the backend of the AIAA and rather than developing an extension around the SAM,  it seems like would be easier to use the existing AIAA UI scheme for marking up individual segments to use as seeds for “fill between slices” (although I admit this may be a naive notion)</p>

---

## Post #10 by @lassoan (2023-04-08 20:12 UTC)

<p>“Segment anything” works considerably better than “Remove background” function in PowePoint and it is nice that it is made easily accessible in a web application and that the training data is published as well. But I don’t really get the excitement about using it for medical images.</p>
<p>To me it its performance seems to be comparable to 20-year-old classic Watershed segmentation, but Watershed can be used in 3D as well. See a simple comparison on an easy segmentation problem:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21479481e68c11e815715606906633eeb5f7eeeb.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21479481e68c11e815715606906633eeb5f7eeeb.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21479481e68c11e815715606906633eeb5f7eeeb.mp4</a>
    </source></video>
  </div><p></p>
<p>SegmentAnyhing is simpler and more convenient in that you don’t need to switch between effects, segments, etc. But even with the inconveniences of switching between effects, segments, etc. the overall task completion time is comparable. Updates take a bit longer in Slicer, as in Slicer we update a 3D segmentation consisting of 9 slices, while SegmentAnything just segments only 1 slice.</p>
<p>MONAILabel also has similar interactive neural network based tools (deepedit, etc.) that are supposed to work much better, because they are trained on medical images and some of them can also work in 3D.</p>
<p>For me, the main conclusion is that we need to make Slicer’s segmentation tools simpler to use and make more people aware that they exist.</p>

---

## Post #11 by @Dominick_Dickerson (2023-04-09 20:20 UTC)

<p>Perhaps im misguided in thinking that models trained on human and mouse data are not gonna work well for segmenting unconventional organisms.</p>
<p>I work on cephalopods and other mollusks (ex vivo CEμCT) and have found flood filling and grow from seeds to be inconsistent/needing a lot of correction but I’m fully willing to concede that it could just be that I don’t know how to best use those tools.</p>

---

## Post #12 by @muratmaga (2023-04-10 03:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="28787">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For me, the main conclusion is that we need to make Slicer’s segmentation tools simpler to use and make more people aware that they exist.</p>
</blockquote>
</aside>
<p>That would be wonderful. However, the need for manual segmentation in non-medical 3D dataset is high mostly due to the fact the there is really no intensity difference between structures (e.g., cranial bones of skull) where semi-automated tools like watershed or grow from the seed is of little use. Or scans are poorly calibrated ore constructed.  SO any possibility of reducing manual segmentation (which is extremely costly, since non-medical CTs are much bigger in data size compared to clinical images) is what the appeal is.</p>
<p>When I played with the level/window in that contrast-enhanced scanned, I did obtain more uniform looking boundaries in SAM than then I often get from watershed or grow from the seeds.  I don’t know how well this would translate to 3D. But if it does help me cut down the number of slices I have to mark by say 50% (and I do the rest via interpolation using fill between slices), that’s still a huge time gain.</p>
<p>I wasn’t able to successfully use deepedit in MonaiLabel for any new non-clinical dataset. Another issue we tend to have in 3D scans of natural history specimens is that there are only a handful of one class/species (if that many), so leveraging deep-learning approaches in this context (beyond mouse and zebrafish) has been limited (too many classes, very few per class representation).</p>

---

## Post #13 by @lassoan (2023-04-10 03:36 UTC)

<p>I think we should be able to do much better than SAM, but if you want to explore its usability in Slicer then you can try this Slicer extension that has just been created:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/bingogome/samm">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/bingogome/samm" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/a9d3bb2aae634748ba3c85bc445b55fa2f9ec192e14eb4eccfd3c79fc6dd22ac/bingogome/samm" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/bingogome/samm" target="_blank" rel="noopener">GitHub - bingogome/samm: A 3D Slicer integration to Meta's SAM.</a></h3>

  <p>A 3D Slicer integration to Meta's SAM. Contribute to bingogome/samm development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="muratmaga" data-post="12" data-topic="28787">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I wasn’t able to successfully use deepedit in MonaiLabel for any new non-clinical dataset.</p>
</blockquote>
</aside>
<p>Hopefully <a class="mention" href="/u/sachidanandalle">@SachidanandAlle</a> and <a class="mention" href="/u/diazandr3s">@diazandr3s</a> will have an answer to this soon.</p>

---

## Post #14 by @Shivam_Sharma (2023-04-11 12:32 UTC)

<p>Hi all! I’m the founder of RedBrick AI and wanted to share my thoughts on SAM.</p>
<p>Our experimentation with SAM showed that it was VERY effective in most medical imaging segmentation tasks. SAM cannot automatically segment the whole image <em>without prompting</em>. However, with simple key point/bounding box prompts, it’s the fastest interactive segmentation algorithm we have experienced.</p>
<p>We’ve experimented with many traditional segmentation algorithms, like Watershed, Otsu, Level tracing, etc., and so far have found SAM to be the most effective and most ergonomic.</p>
<p>See this comparison video for SAM vs. Watershed segmentation on MRI spine. Apologies in advance if I’m not using Watershed correctly, but I tried this on several modalities/objects and continue to be extremely excited by SAMs performance!</p>
<p>FYI - You can try out SAM for free on RedBrick AI <a href="https://blog.redbrickai.com/blog-posts/fast-meta-sam-for-medical-imaging" class="inline-onebox" rel="noopener nofollow ugc">F.A.S.T. ⚡️ Meta AI’s Segment Anything for Medical Imaging. | RedBrick AI Blog</a> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">  <a class="mention" href="/u/dominick_dickerson">@Dominick_Dickerson</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/760f0d9a6b2c9774d69b32572110eb5483146547.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/760f0d9a6b2c9774d69b32572110eb5483146547.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/760f0d9a6b2c9774d69b32572110eb5483146547.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #15 by @dzenanz (2023-04-11 17:10 UTC)

<p><a class="mention" href="/u/shivam_sharma">@Shivam_Sharma</a> it looks like you haven’t tackled the problem of propagation into 3D. Do you intend to work on that?</p>

---

## Post #16 by @Shivam_Sharma (2023-04-11 17:17 UTC)

<p>Yep! It’ll be released in a few days.</p>

---

## Post #17 by @jamesobutler (2023-04-11 17:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="28787">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For me, the main conclusion is that we need to make Slicer’s segmentation tools simpler to use and make more people aware that they exist.</p>
</blockquote>
</aside>
<p>I think this is clear by <a class="mention" href="/u/shivam_sharma">@Shivam_Sharma</a> 's usage of Slicer compared to your video <a class="mention" href="/u/lassoan">@lassoan</a> segmenting the same things.</p>
<p><a class="mention" href="/u/shivam_sharma">@Shivam_Sharma</a> 's 10 seed points and initial result:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d2ff28353803f39562cb52c979f39246444a5f0.png" alt="image" data-base62-sha1="1SEVToUY6BZuWYMXHT7lI1wpq80" width="261" height="227"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/290b467f6fe5d52140abd6e00c6e4d83fe376ab0.png" alt="image" data-base62-sha1="5R5JuhcFXMWHWwadC7lPlzp8P4Y" width="214" height="184"></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> 's 6 seed points and initial result:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/785acb5613af9380b8ef3cd2017ae264af24810a.jpeg" alt="image" data-base62-sha1="haHOYWCm8HbFwY6ZOPgAaiNvfyW" width="297" height="414"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe07a5af589d98fb12c253216f29e9ebe4d3d7bb.png" alt="image" data-base62-sha1="AffF123FPYwErbyCM5yUIJH6udZ" width="571" height="392"></p>

---

## Post #18 by @lassoan (2023-04-11 18:54 UTC)

<aside class="quote no-group" data-username="Shivam_Sharma" data-post="14" data-topic="28787">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shivam_sharma/48/65582_2.png" class="avatar"> Shivam_Sharma:</div>
<blockquote>
<p>Our experimentation with SAM showed that it was VERY effective in most medical imaging segmentation tasks</p>
</blockquote>
</aside>
<p>My experience is that SAM is quick and simple, which is good, but it <strong>only works for very easy, 2D segmentation tasks</strong>. These easy tasks are mostly either already solved or if not solved then it is because they are not clinically relevant problems. Many people feel the same way - see for example this discussion: <a href="https://www.linkedin.com/posts/samyakhtukra_holy-smokes-sam-segment-anything-model-activity-7049699206206283776-_fva?utm_source=share&amp;utm_medium=member_desktop" class="inline-onebox">Samyakh (Sam) Tukra on LinkedIn: Holy smokes SAM (Segment Anything Model) works even on medical images out… | 128 comments</a></p>
<p>SAM might be a good basis for creating medical image segmentation tools, but you would need improvements to segment in 3D and probably you would need to do some training specifically on medical images, too. So, most likely SAM is actually not the best approach to start from. Instead, you could start from an inherently 3D segmentation tool, or one that has been already trained on medical images. Before jumping into investing time into extending SAM for 3D medical image segmentation, I would recommend to check out MONAI/MONAILabel based tools and other promising tools described in the literature can do.</p>

---

## Post #19 by @Shivam_Sharma (2023-04-11 19:17 UTC)

<p>Fair points! However, we have experimented with all the tools (traditional and deep learning based) and still are impressed by SAMs abilities on a variety of use cases <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #20 by @Slicer3D (2023-05-03 16:01 UTC)

<p>What tool are you using here in 3D slicer?</p>

---

## Post #21 by @lassoan (2023-05-21 00:25 UTC)

<p>It is the Watershed effect, provided by SegmentEditorExtraEffects extension.</p>

---

## Post #22 by @Slicer3D (2023-06-05 23:40 UTC)

<p>Hi,</p>
<p>Can anyone help me with integrating the SAM into slicer? I keep running into issues with the instructions</p>

---

## Post #23 by @lassoan (2023-06-05 23:50 UTC)

<p>I’m not sure if the module’s developer reads subscribed to this forum, so it is probably better if you post your questions or problems as issues in the <a href="https://github.com/bingogome/samm">Slicer SAMM git repository</a>.</p>

---

## Post #24 by @fsemerar (2023-06-17 01:31 UTC)

<p>Hi everybody!  My team and I have just released a new extension called TomoSAM that integrates SAM into Slicer:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/fsemerar/SlicerTomoSAM">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/fsemerar/SlicerTomoSAM" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/7814a309ff5c9942e21bca459b18e60c74dfcce736fe0b0bc2a2d901b03b4048/fsemerar/SlicerTomoSAM" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/fsemerar/SlicerTomoSAM" target="_blank" rel="noopener nofollow ugc">GitHub - fsemerar/SlicerTomoSAM: An extension of 3D Slicer using the Segment...</a></h3>

  <p>An extension of 3D Slicer using the Segment Anything Model (SAM) to aid the segmentation of 3D data from tomography or other imaging techniques. - GitHub - fsemerar/SlicerTomoSAM: An extension of 3...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Here is a youtube tutorial video to get started with it:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="4nXCYrvBSjk" data-video-title="TomoSAM Tutorial" data-video-start-time="0" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=4nXCYrvBSjk" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/4nXCYrvBSjk/maxresdefault.jpg" title="TomoSAM Tutorial" width="" height="">
  </a>
</div>


---
