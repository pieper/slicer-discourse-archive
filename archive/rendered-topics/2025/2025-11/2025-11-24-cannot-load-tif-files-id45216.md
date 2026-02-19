---
topic_id: 45216
title: "Cannot Load Tif Files"
date: 2025-11-24
url: https://discourse.slicer.org/t/45216
---

# Cannot load tif files

**Topic ID**: 45216
**Date**: 2025-11-24
**URL**: https://discourse.slicer.org/t/cannot-load-tif-files/45216

---

## Post #1 by @Busra_Pullu1 (2025-11-24 20:30 UTC)

<p>I need to upload more than 2500 tiff files. I spent lots of time uploading them, but Slicer keeps crashing. What is the best way to do this? Btw, for some reason I have no image stacks on the modules. I added, like, add data—choose files (I couldn’t choose a directory file; it was crashing again), but the green and yellow sections are almost black. I just have something on the red section, but it’s still incomplete. What are your suggestions? I need to do volume rendering of a fossil mammal skull.</p>

---

## Post #2 by @cpinter (2025-11-24 21:28 UTC)

<p>I suggest you try the SlicerMorph extension. It has a module called <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">ImageStacks</a> that may help.</p>

---

## Post #3 by @muratmaga (2025-11-24 22:07 UTC)

<p>Yes use the ImageStacks from Slicermorph. 2500 tiff files quite a lot, you didnt specify xy dimensions but if 16bit thia data can be easily 10-20gb in size.</p>
<p>You migth want to load at half or preview resolution  first to makw sure you are not hitting your computer resource limits.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" target="_blank" rel="noopener nofollow ugc">Tutorials/ImageStacks at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Busra_Pullu1 (2025-11-26 17:07 UTC)

<p>Thank you. Could you please take a look at this ss? Am I doing it correctly? For some reason, the slicer couldn’t define automatically the spacing. I am just trying to find pixel sizes of documents to have voxel sizes manually.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3219d92785fd7942eb6abbcf21acefabc5f733e.jpeg" data-download-href="/uploads/short-url/wpipdmLVNA3UVcIHs1H5DqsWX9Q.jpeg?dl=1" title="Screenshot 2025-11-26 113032" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3219d92785fd7942eb6abbcf21acefabc5f733e_2_690x369.jpeg" alt="Screenshot 2025-11-26 113032" data-base62-sha1="wpipdmLVNA3UVcIHs1H5DqsWX9Q" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3219d92785fd7942eb6abbcf21acefabc5f733e_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3219d92785fd7942eb6abbcf21acefabc5f733e_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3219d92785fd7942eb6abbcf21acefabc5f733e_2_1380x738.jpeg 2x" data-dominant-color="68676E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-11-26 113032</span><span class="informations">1919×1028 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2025-11-26 18:38 UTC)

<aside class="quote no-group" data-username="Busra_Pullu1" data-post="4" data-topic="45216">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/busra_pullu1/48/79395_2.png" class="avatar"> Busra_Pullu1:</div>
<blockquote>
<p>For some reason, the slicer couldn’t define automatically the spacing.</p>
</blockquote>
</aside>
<p>Yes, most of the times formats do not provide that information. So we set the spacing to 0 to let user know that it didn’t work. In such cases you need to enter the value manually. Whoever gave you the dataset, they should have provided that informaiton to you. if you found this on MorphoSource, they will list the resolution on their website.</p>
<p>Otherwise all is good.</p>

---
