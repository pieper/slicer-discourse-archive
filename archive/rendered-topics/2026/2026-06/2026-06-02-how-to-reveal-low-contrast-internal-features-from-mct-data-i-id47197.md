---
topic_id: 47197
title: "How to reveal low-contrast internal features from mCT data in Volume Rendering?"
date: 2026-06-02
url: https://discourse.slicer.org/t/47197
last_bumped: 2026-06-02T04:11:06.607Z
---

# How to reveal low-contrast internal features from mCT data in Volume Rendering?

**Topic ID**: 47197
**Date**: 2026-06-02
**URL**: https://discourse.slicer.org/t/how-to-reveal-low-contrast-internal-features-from-mct-data-in-volume-rendering/47197

---

## Post #1 by @Akhmad_Fauzan (2026-06-02 01:19 UTC)

<div class="d-image-grid">
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7d79467f8cbe08718c903faa3b647b3c3ed88bf.jpeg" data-download-href="/uploads/short-url/nWNC7VMtbOcdegoXgUvmqEddKBF.jpeg?dl=1" title="Screenshot 2026-05-22 084644" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7d79467f8cbe08718c903faa3b647b3c3ed88bf_2_690x470.jpeg" alt="Screenshot 2026-05-22 084644" data-base62-sha1="nWNC7VMtbOcdegoXgUvmqEddKBF" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7d79467f8cbe08718c903faa3b647b3c3ed88bf_2_690x470.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7d79467f8cbe08718c903faa3b647b3c3ed88bf_2_1035x705.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7d79467f8cbe08718c903faa3b647b3c3ed88bf.jpeg 2x" data-dominant-color="BABBDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-05-22 084644</span><span class="informations">1127×769 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2afb2511979f1373396826c7a59174b158e2c64e.jpeg" data-download-href="/uploads/short-url/68e7ZUQ9VToIh1Ufa9xsMlgrZbE.jpeg?dl=1" title="Screenshot 2026-05-22 084529" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2afb2511979f1373396826c7a59174b158e2c64e_2_690x466.jpeg" alt="Screenshot 2026-05-22 084529" data-base62-sha1="68e7ZUQ9VToIh1Ufa9xsMlgrZbE" width="690" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2afb2511979f1373396826c7a59174b158e2c64e_2_690x466.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2afb2511979f1373396826c7a59174b158e2c64e_2_1035x699.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2afb2511979f1373396826c7a59174b158e2c64e.jpeg 2x" data-dominant-color="A3A4D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-05-22 084529</span><span class="informations">1132×766 81.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/473b915d74341dfa4427a365e9f495ea47b3db91.jpeg" data-download-href="/uploads/short-url/aa9wtQzSduJL9gKxkull67bdrfr.jpeg?dl=1" title="Screenshot 2026-05-22 084522" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/473b915d74341dfa4427a365e9f495ea47b3db91_2_399x500.jpeg" alt="Screenshot 2026-05-22 084522" data-base62-sha1="aa9wtQzSduJL9gKxkull67bdrfr" width="399" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/473b915d74341dfa4427a365e9f495ea47b3db91_2_399x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/473b915d74341dfa4427a365e9f495ea47b3db91.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/473b915d74341dfa4427a365e9f495ea47b3db91.jpeg 2x" data-dominant-color="A7A9CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-05-22 084522</span><span class="informations">444×556 35.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/0935d528418cce856cb7303ee49e8eed922a915c.jpeg" data-download-href="/uploads/short-url/1jtDfOd24ARq1BCzikHqupfRfLm.jpeg?dl=1" title="Screenshot 2026-05-22 084427" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/0935d528418cce856cb7303ee49e8eed922a915c_2_684x500.jpeg" alt="Screenshot 2026-05-22 084427" data-base62-sha1="1jtDfOd24ARq1BCzikHqupfRfLm" width="684" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/0935d528418cce856cb7303ee49e8eed922a915c_2_684x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/0935d528418cce856cb7303ee49e8eed922a915c_2_1026x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/0935d528418cce856cb7303ee49e8eed922a915c.jpeg 2x" data-dominant-color="9597C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-05-22 084427</span><span class="informations">1119×817 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</div>
<p>I am currently working on analyzing a micro-CT (mCT) dataset of a <strong>pseudobulb of Acriopsis liliifolia.</strong> I am trying to inspect and visualize its internal structures, but I have hit a roadblock.</p>
<p>As you can see from the attached screenshots, when I switch to <strong>Volume Rendering</strong>, the output appears mostly solid or completely hollow in areas where I expect detailed internal morphology. I cannot seem to resolve or distinguish any internal features. Any advice for this problems. Thank you very much.</p>

---

## Post #2 by @muratmaga (2026-06-02 02:06 UTC)

<p>What does your slice views show? There may not be much of an internal detail, if this is the scan is not contrast-enhanced.</p>

---

## Post #3 by @Akhmad_Fauzan (2026-06-02 03:44 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12b502a951609a59aaae16239d779aa103a8d96c.jpeg" data-download-href="/uploads/short-url/2Fupgfuf32qkEmPF7fsgymRoEqM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12b502a951609a59aaae16239d779aa103a8d96c_2_681x500.jpeg" alt="image" data-base62-sha1="2Fupgfuf32qkEmPF7fsgymRoEqM" width="681" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12b502a951609a59aaae16239d779aa103a8d96c_2_681x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12b502a951609a59aaae16239d779aa103a8d96c_2_1021x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12b502a951609a59aaae16239d779aa103a8d96c.jpeg 2x" data-dominant-color="62595D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1113×817 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is the slice view. I hope I can find something important here. But, I don’t know. What do you think? Thanks for the help.</p>

---

## Post #4 by @muratmaga (2026-06-02 03:47 UTC)

<p>I don’t know anything about plant anatomy but I don’t see any internal detail beyond the small air pockets. That’s why you are not seeing anything in the cropped volume rendering too. There is not much you can do with this data, if your goal is to see internal small structure detail, you should try different contrasts and see what gives the detail you are looking for.</p>

---

## Post #5 by @Akhmad_Fauzan (2026-06-02 03:54 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="47197">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>should try different contrasts</p>
</blockquote>
</aside>
<p>Could you clarify the meaning by trying ‘different contrasts’ in this context, and how I can adjust those settings in the 3D Slicer to better reveal the internal details? I am new to 3D Slicer. I might miss some extensions or feature there. Thanks.</p>

---

## Post #6 by @muratmaga (2026-06-02 04:11 UTC)

<p>This is not a slicer problem. it is an imaging problem. Slicer cannot display information that is not there. Again I do not know anything about internals of seeds, but I presume you wanted to see some fiber tracks of sorts. They are not there,  from signal point of view everything is similar (with the exception of air pockets), so you don’t see any internal detail.</p>
<p>You will need to dunk this seed into a solution like iodine, phosphotungstenic acid these are the two commonly used contrasts for vertebrate embryos. You may want to search the literature to find if they work for seed and plants and find others. After the treatment, you have to image again.</p>
<p>At that point you should be able to see internal structure.</p>

---
