# Manual Surface Registration

**Topic ID**: 44899
**Date**: 2025-10-28
**URL**: https://discourse.slicer.org/t/manual-surface-registration/44899

---

## Post #1 by @Davi_Matos (2025-10-28 00:27 UTC)

<p>Is there a way to do something like this on 3D slicer?</p>
<p>Basically, I’m trying to allign this two models for a planned condylectomy. I’ve used surface registration module on Slicer CMF, wich gave me a good match of the two models (hyperplasic side x Mirrored good side). However, I’m trying to fine ajust this and it’s been difficult. I’m planning using this guide and I wonder if 3D slicer would have something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fee24b6fd563b57ac0935034694ec1065954f7a.jpeg" data-download-href="/uploads/short-url/mOO8xorGqCX9FwlEJAuB9bUGsqK.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fee24b6fd563b57ac0935034694ec1065954f7a_2_690x256.jpeg" alt="image" data-base62-sha1="mOO8xorGqCX9FwlEJAuB9bUGsqK" width="690" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fee24b6fd563b57ac0935034694ec1065954f7a_2_690x256.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fee24b6fd563b57ac0935034694ec1065954f7a_2_1035x384.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fee24b6fd563b57ac0935034694ec1065954f7a.jpeg 2x" data-dominant-color="EBEAE2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1084×403 65.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>A way for me to put a fulcrum point on the mandible angle and have the rotation e translations on screen, like we can do on plane cuts. I’ve tried doing this with the transforms module, but it’s not quite what I am looking for. Wich is this kind of superposition:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3102cfe27f0ead26c3021e80dea21f55ab04a1e1.jpeg" data-download-href="/uploads/short-url/6Zzq5Ib38sY2J6Awv1f5umRuvAd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3102cfe27f0ead26c3021e80dea21f55ab04a1e1_2_690x379.jpeg" alt="image" data-base62-sha1="6Zzq5Ib38sY2J6Awv1f5umRuvAd" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3102cfe27f0ead26c3021e80dea21f55ab04a1e1_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3102cfe27f0ead26c3021e80dea21f55ab04a1e1_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3102cfe27f0ead26c3021e80dea21f55ab04a1e1.jpeg 2x" data-dominant-color="BABFBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1037×570 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is what Ive achieved so far:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb1eff347a2acfa3b10a57d5240aa9d7567f6569.png" data-download-href="/uploads/short-url/sYTkTAnKXPjZkINHRgswNXsKigh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb1eff347a2acfa3b10a57d5240aa9d7567f6569_2_690x294.png" alt="image" data-base62-sha1="sYTkTAnKXPjZkINHRgswNXsKigh" width="690" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb1eff347a2acfa3b10a57d5240aa9d7567f6569_2_690x294.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb1eff347a2acfa3b10a57d5240aa9d7567f6569_2_1035x441.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb1eff347a2acfa3b10a57d5240aa9d7567f6569_2_1380x588.png 2x" data-dominant-color="717293"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1909×814 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I appreciate the help!</p>

---

## Post #2 by @pieper (2025-10-28 13:17 UTC)

<p>Have you tried the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#interaction">interactive transform options</a>?  You may want to use the latest preview version of Slicer.</p>

---

## Post #4 by @Davi_Matos (2025-10-28 16:07 UTC)

<p>Yes, I did. But the rotation axis wasnt showing. But I figured it out, it was very far away from the models. Clicking on “reset center of transformation” putted the rotation closer of the model, and the link you sent had instructions on how to move the fulcrum point. Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1a3283b959b9923c0b031d8e79d80ebb02b8f7e.jpeg" data-download-href="/uploads/short-url/pls4DNPaCpZ7e3cXANAysD9o5TE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1a3283b959b9923c0b031d8e79d80ebb02b8f7e_2_659x500.jpeg" alt="image" data-base62-sha1="pls4DNPaCpZ7e3cXANAysD9o5TE" width="659" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1a3283b959b9923c0b031d8e79d80ebb02b8f7e_2_659x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1a3283b959b9923c0b031d8e79d80ebb02b8f7e_2_988x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1a3283b959b9923c0b031d8e79d80ebb02b8f7e.jpeg 2x" data-dominant-color="9B8EBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">997×756 89.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Bay_6 (2025-11-10 13:29 UTC)

<p>You can also move the center freely by holding down the <strong>Alt</strong> key</p>

---
