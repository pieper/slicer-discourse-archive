# Radiomics entropy=0?

**Topic ID**: 5583
**Date**: 2019-01-30
**URL**: https://discourse.slicer.org/t/radiomics-entropy-0/5583

---

## Post #1 by @carba86 (2019-01-30 18:12 UTC)

<p>Hi, a quick question.</p>
<p>No matter if I study a label after segmenting the largest cross section of the image or the tumor volume, I keep getting Entropy = -0.0 with Radiomics.</p>
<p>Any tip?<br>
Thanks.<br>
Leandro.</p>

---

## Post #2 by @JoostJM (2019-02-06 13:55 UTC)

<p><a class="mention" href="/u/carba86">@carba86</a> Is that the firstorder Entropy? If so, what are the values for firstorder:Range and the value for the setting “binWidth” you used during extraction?</p>
<p>An entropy of 0 usually points to a ‘flat region’, i.e. all voxels have the same gray value AFTER DISCRETIZATION, this can be caused in a situation where the range of grayvalues is (much) smaller than the binwidth, causing all voxels to belong to the same bin: i.e. same grayvalue and a ‘flat region’</p>
<p>Regards,</p>
<p>Joost</p>

---

## Post #3 by @carba86 (2019-04-17 13:14 UTC)

<p>Thanks Joost and sorry it’s taken me a while to write you back. Analyzing numbers obtained with Radiomics, I see that this inconsistency does not only happen with Entropy but with other features as well, firstorder specially. I attach screen captures of Radiomics settings and numbers obtained (each column representing a different patient).</p>
<p>I look forward to hearing from you guys, you are always of great help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9cef964e20a7db894ee76307b717538201c8a38.png" data-download-href="/uploads/short-url/oec8e083KnmUUsiCGu4u3cD2RUQ.png?dl=1" title="Snip20190417_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9cef964e20a7db894ee76307b717538201c8a38_2_690x259.png" alt="Snip20190417_2" data-base62-sha1="oec8e083KnmUUsiCGu4u3cD2RUQ" width="690" height="259" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9cef964e20a7db894ee76307b717538201c8a38_2_690x259.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9cef964e20a7db894ee76307b717538201c8a38_2_1035x388.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9cef964e20a7db894ee76307b717538201c8a38_2_1380x518.png 2x" data-dominant-color="817F88"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snip20190417_2</span><span class="informations">3332×1252 630 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/751346ffedd478c73a2d2d8a9a40bd73c6ed5e24.png" data-download-href="/uploads/short-url/gHHagphjrbSfqdzu7QzbOf0ELTS.png?dl=1" title="Snip20190417_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/751346ffedd478c73a2d2d8a9a40bd73c6ed5e24_2_626x500.png" alt="Snip20190417_1" data-base62-sha1="gHHagphjrbSfqdzu7QzbOf0ELTS" width="626" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/751346ffedd478c73a2d2d8a9a40bd73c6ed5e24_2_626x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/751346ffedd478c73a2d2d8a9a40bd73c6ed5e24_2_939x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/751346ffedd478c73a2d2d8a9a40bd73c6ed5e24.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snip20190417_1</span><span class="informations">1192×952 81.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4605cc3a87913a47851f64eb429e3b74dbaf8a8f.jpeg" data-download-href="/uploads/short-url/9ZrQmBZikUDwHATULbBSh3bD8p9.jpeg?dl=1" title="Snip20190417_3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4605cc3a87913a47851f64eb429e3b74dbaf8a8f_2_690x387.jpeg" alt="Snip20190417_3" data-base62-sha1="9ZrQmBZikUDwHATULbBSh3bD8p9" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4605cc3a87913a47851f64eb429e3b74dbaf8a8f_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4605cc3a87913a47851f64eb429e3b74dbaf8a8f_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4605cc3a87913a47851f64eb429e3b74dbaf8a8f_2_1380x774.jpeg 2x" data-dominant-color="C6C0AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snip20190417_3</span><span class="informations">2876×1616 1.63 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1ce3f5f19d4c078496f942ab57699630543a1cc.jpeg" data-download-href="/uploads/short-url/rEu2b0WmJBRYq8Z7fCEQpnZolVW.jpeg?dl=1" title="Snip20190417_4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ce3f5f19d4c078496f942ab57699630543a1cc_2_690x282.jpeg" alt="Snip20190417_4" data-base62-sha1="rEu2b0WmJBRYq8Z7fCEQpnZolVW" width="690" height="282" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ce3f5f19d4c078496f942ab57699630543a1cc_2_690x282.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ce3f5f19d4c078496f942ab57699630543a1cc_2_1035x423.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ce3f5f19d4c078496f942ab57699630543a1cc_2_1380x564.jpeg 2x" data-dominant-color="C4BEAA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snip20190417_4</span><span class="informations">2878×1180 1.24 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Kind regards,<br>
Leandro.</p>

---

## Post #4 by @JoostJM (2019-04-18 08:01 UTC)

<p>The entropy 0 is indeed caused by a too-large bin width (set to 25 in your case). Many of your scans show a lot lower range (max ~4, range &lt; 5). This will result in flat regions.</p>
<p>Moreover, some of your scans are VERY different (e.g. max ~15,000), which, as predicted, do not result in entropy = 0.</p>
<p>My advise would be to use a parameter file and enable normalization with an adapted bin width. See more on customizing the extraction and the parameter file in <a href="https://pyradiomics.readthedocs.io/en/latest/customization.html" rel="nofollow noopener">pyradiomics’ documentation</a></p>

---

## Post #5 by @carba86 (2019-04-19 19:07 UTC)

<p>Thanks Joost once again.<br>
Do you think binwidth setting will correct other discrepancies I see for example in ngtdm  or glcm ?</p>

---

## Post #6 by @JoostJM (2019-04-23 07:56 UTC)

<p>Yes, although I also advise to enable normalization, as the range in some of your images is very, very large, compared to most of your other images.</p>

---

## Post #7 by @carba86 (2019-04-27 00:12 UTC)

<p>Hi Joost, by adapted binwidth do you mean something like this? (my data are MR images, 3D volumes with apron 1 mm slice thickness)</p>
<p>imageType:<br>
Original: {}</p>
<p>featureClass:<br>
shape:<br>
firstorder:<br>
glcm:<br>
glrlm:<br>
glszm:<br>
gldm:</p>
<p>setting:<br>
normalize: true<br>
normalizeScale: 100<br>
interpolator: ‘sitkBSpline’<br>
resampledPixelSpacing: [1, 1, 1]<br>
binWidth: 5<br>
dynamicBinning: true<br>
voxelArrayShift: 300<br>
label: 1</p>

---

## Post #8 by @carba86 (2019-04-27 01:16 UTC)

<p>One more thing, I get to different scenes (values of firstorder:range) depending on how I normalize my original images.  Which would be the correct option?</p>
<ol>
<li><strong>NORMALIZING WITH THE SIMPLE FILTER EXTENSION IN 3DSLICER</strong></li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d161c12d8e1577b6140b5e236afde6b3b5b43573.png" data-download-href="/uploads/short-url/tSheey31qC6534UEW6CMkbBHx9F.png?dl=1" title="Snip20190426_40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d161c12d8e1577b6140b5e236afde6b3b5b43573_2_690x416.png" alt="Snip20190426_40" data-base62-sha1="tSheey31qC6534UEW6CMkbBHx9F" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d161c12d8e1577b6140b5e236afde6b3b5b43573_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d161c12d8e1577b6140b5e236afde6b3b5b43573_2_1035x624.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d161c12d8e1577b6140b5e236afde6b3b5b43573_2_1380x832.png 2x" data-dominant-color="B9B7B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snip20190426_40</span><span class="informations">3110×1876 684 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d03e52c244bbe21b456877f20df2e2357e194b04.png" data-download-href="/uploads/short-url/tIcQ8g2h3zljtf9bTYQTi9w3ELW.png?dl=1" title="Snip20190426_39" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d03e52c244bbe21b456877f20df2e2357e194b04_2_690x418.png" alt="Snip20190426_39" data-base62-sha1="tIcQ8g2h3zljtf9bTYQTi9w3ELW" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d03e52c244bbe21b456877f20df2e2357e194b04_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d03e52c244bbe21b456877f20df2e2357e194b04_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d03e52c244bbe21b456877f20df2e2357e194b04_2_1380x836.png 2x" data-dominant-color="B6B5B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snip20190426_39</span><span class="informations">3104×1882 777 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li><strong>NORMALIZING WITH PARAMETER FILE</strong></li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/846f55221018e7150e200177a4008026df493149.jpeg" data-download-href="/uploads/short-url/iTzypnAGakECo8vECTmG9WJ3VvH.jpeg?dl=1" title="Snip20190426_43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/846f55221018e7150e200177a4008026df493149_2_690x402.jpeg" alt="Snip20190426_43" data-base62-sha1="iTzypnAGakECo8vECTmG9WJ3VvH" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/846f55221018e7150e200177a4008026df493149_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/846f55221018e7150e200177a4008026df493149_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/846f55221018e7150e200177a4008026df493149_2_1380x804.jpeg 2x" data-dominant-color="949294"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snip20190426_43</span><span class="informations">3114×1818 756 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @JoostJM (2019-04-29 11:29 UTC)

<p>Out of your provided examples, I’d say go for method 2. Using it this way also includes the additional scaling factor (100) which is matched to the binwidth of 5. If you want to use Slicer’s normalization, update the binwidth to 0.05.</p>
<p>As to your parameter file. That looks fine to me. The only comment I have is that parameter <code>dynamicBinning</code> will not be accepted, as it is not part of the master branch of PyRadiomics and therefore also not part of the Radiomics module.</p>

---

## Post #10 by @carba86 (2019-05-08 13:27 UTC)

<p>Do you recommend using a binwidth of 5 although range in scene 2 is aprox&lt;350?</p>

---

## Post #11 by @JoostJM (2019-05-08 14:12 UTC)

<p><a class="mention" href="/u/carba86">@carba86</a> yes, I generally try to aim for a compromise that results in about 10-100 bins for the bulk of the cases in the dataset.</p>

---
