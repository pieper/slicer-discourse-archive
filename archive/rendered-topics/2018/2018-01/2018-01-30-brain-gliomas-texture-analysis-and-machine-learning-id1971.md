# Brain Gliomas, Texture Analysis and Machine Learning

**Topic ID**: 1971
**Date**: 2018-01-30
**URL**: https://discourse.slicer.org/t/brain-gliomas-texture-analysis-and-machine-learning/1971

---

## Post #1 by @carba86 (2018-01-30 03:06 UTC)

<p>Operating system: Mac OS<br>
Slicer version: 4.9.0</p>
<p>Hi everyone,</p>
<p>I am a Neuroradiology Fellow with some background in Biomedical Engineering in Buenos Aires, Argentina and for the past 6 months I’ve been working with Texture Analysis. At first it was pretty hard to learn about different software in the market and which one would suit me best. Fortunately I got to understand Slicer a bit more after my visit at RSNA Congress in Chicago and now I am trying to do some research regarding the phenotype of brain gliomas.</p>
<p>So far, I am working with T1WI post Gd (volumes) from two different 3T GE Magnets.<br>
The first step of my project would be to obtain textural features and then decide whether to discriminate them between high or low grade gliomas or to analyze different molecular markers and gene mutations.<br>
If I get good results with this I will write later with questions on how to use Slicer on Knime. But first things first. These are a couple of  screen captures regarding the steps I am doing with every different tumor.<br>
Please feel free to write any suggestions or corrections you consider appropriate.<br>
Thanks,<br>
Leandro.</p>
<ol>
<li>loading the volume</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d96bd8dfe7eb0dca7debe24da9acbc2c304fe156.jpeg" data-download-href="/uploads/short-url/v1oFHnIprjYEwjBAlzFzyjAeNWm.jpg?dl=1" title="48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d96bd8dfe7eb0dca7debe24da9acbc2c304fe156_2_690x388.jpg" alt="48" data-base62-sha1="v1oFHnIprjYEwjBAlzFzyjAeNWm" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d96bd8dfe7eb0dca7debe24da9acbc2c304fe156_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d96bd8dfe7eb0dca7debe24da9acbc2c304fe156_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d96bd8dfe7eb0dca7debe24da9acbc2c304fe156_2_1380x776.jpg 2x" data-dominant-color="A9A8AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">48</span><span class="informations">3360×1890 745 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="2">
<li>normalizing the volumen with SimpleFilters extension</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5f510c26d7bd79d36643a173d1eb563d38cdcc7.png" data-download-href="/uploads/short-url/uwKKAWBgOolhQaU3vYp19lG31FJ.png?dl=1" title="00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5f510c26d7bd79d36643a173d1eb563d38cdcc7_2_690x384.png" alt="00" data-base62-sha1="uwKKAWBgOolhQaU3vYp19lG31FJ" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5f510c26d7bd79d36643a173d1eb563d38cdcc7_2_690x384.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5f510c26d7bd79d36643a173d1eb563d38cdcc7_2_1035x576.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5f510c26d7bd79d36643a173d1eb563d38cdcc7_2_1380x768.png 2x" data-dominant-color="A4A3A6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">00</span><span class="informations">3352×1870 1.11 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="3">
<li>manual segmentation of entire tumor (shall I consider only the slice with the largest transverse diameter or the entire tumor?)</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47ad03b28e7b7101118f797de937c4f47f151e3f.png" data-download-href="/uploads/short-url/ae4A5Jzq8MQig0Q8E6sgNwNoEcD.png?dl=1" title="28" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47ad03b28e7b7101118f797de937c4f47f151e3f_2_690x381.png" alt="28" data-base62-sha1="ae4A5Jzq8MQig0Q8E6sgNwNoEcD" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47ad03b28e7b7101118f797de937c4f47f151e3f_2_690x381.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47ad03b28e7b7101118f797de937c4f47f151e3f_2_1035x571.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47ad03b28e7b7101118f797de937c4f47f151e3f_2_1380x762.png 2x" data-dominant-color="9E9EA1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">28</span><span class="informations">3350×1852 1.05 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="4">
<li>obtain the detailed texture features with the PyRadiomics extension</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/247defd96b1724665a2e7ea42653419a3c2c57a6.png" data-download-href="/uploads/short-url/5cP0sVekMzAhAoWh6ezJZoOXhCC.png?dl=1" title="28" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/247defd96b1724665a2e7ea42653419a3c2c57a6_2_690x387.png" alt="28" data-base62-sha1="5cP0sVekMzAhAoWh6ezJZoOXhCC" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/247defd96b1724665a2e7ea42653419a3c2c57a6_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/247defd96b1724665a2e7ea42653419a3c2c57a6_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/247defd96b1724665a2e7ea42653419a3c2c57a6_2_1380x774.png 2x" data-dominant-color="9F9EA1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">28</span><span class="informations">3352×1882 1.12 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2018-01-30 15:08 UTC)

<p>Hi Leandro -</p>
<p>Thanks for sharing your project and workflow - it’s important work and I will be very interested to see what you discover.</p>
<p>A few thoughts / suggestions: a lot of work has gone into enhancing the new Segment Editor so it might try that.  Also in both editors the GrowCut algorithm (Grow from seeds in the Segment Editor) could help, but if not it would help us to know if any of the automated tools help or if you really prefer manual methods.</p>
<p>Also as you do multiple cases you might find the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator">CaseIterator</a> useful for managing your workflow.</p>
<p>Best of luck,<br>
Steve</p>

---

## Post #3 by @JoostJM (2018-01-30 15:31 UTC)

<p>Hello Leandro,</p>
<p>Very interesting project! As your using the PyRadiomics extension, you can also normalize as part of the feature extraction in this extension (saves you a processing step).</p>
<p>For this to work, you need to write a parameter file and pass the file location in the extension (select Parameter File Customization) and you’ll see a control where you can enter this file (comes with a browse button and path-auto-complete).</p>
<p>Using a parameter file has some other advantages too:</p>
<ol>
<li>it unlocks the full potential of PyRadiomics (filters, settings and specifying features to extract on a per-feature basis.</li>
<li>It’ll help you reproducibility, as you can reuse your parameter file at a later date to recreate your extraction.</li>
<li>You only have to make this file once, you can then apply it to your data (whether you are using the slicer extension of pyradiomics stand-alone, it works both ways)</li>
</ol>
<p>For the documentation on how to make this file (and what are the customization options in pyradiomics), see <a href="http://pyradiomics.readthedocs.io/en/latest/customization.html" rel="nofollow noopener">here</a>. Some examples of the parameter file can be found <a href="https://github.com/Radiomics/pyradiomics/tree/master/examples/exampleSettings" rel="nofollow noopener">here</a>.</p>
<p>Best,</p>
<p>Joost</p>

---

## Post #4 by @carba86 (2018-01-30 19:54 UTC)

<p>Thank you very much for your quick responses Steve and Joost! I 'll try to follow your piece of advice. Would you think I am in the right track? I mean in terms of the process</p>

---

## Post #5 by @pieper (2018-01-30 21:33 UTC)

<p>Seems very reasonable to me.  When you are comfortable with the tools you could formulate some hypotheses about what effect size you expect to see and that would give you a sense of how many subjects you need to segment to test it.</p>

---

## Post #6 by @carba86 (2018-03-21 12:18 UTC)

<p>Updates on this project for those interested. I segmented and analyzed texture features of 10 low grade brain gliomas and 9 high grade gliomas with original transformations (haven’t analyzed wavelets yet).<br>
It’s sort of difficult for me to see if any conclusions could be made. So far, I see that first order statistics have the best numbers in terms of sensitivity and sensibility (could this be due to analysis of only the largest cross-section image and not the entire tumor?). Features reflecting the largest variance from the mean were the most significant ones, suggesting lower homogeinity in high grade gliomas.<br>
Please feel free to add any comments.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b64cc588c083c71accec9148084214d0df1d2408.png" data-download-href="/uploads/short-url/q0HnGCicyT2ONbmIVBZO1rPQp0Q.png?dl=1" title="Snip20180321_5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b64cc588c083c71accec9148084214d0df1d2408_2_690x244.png" alt="Snip20180321_5" data-base62-sha1="q0HnGCicyT2ONbmIVBZO1rPQp0Q" width="690" height="244" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b64cc588c083c71accec9148084214d0df1d2408_2_690x244.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b64cc588c083c71accec9148084214d0df1d2408_2_1035x366.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b64cc588c083c71accec9148084214d0df1d2408_2_1380x488.png 2x" data-dominant-color="EAEAEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snip20180321_5</span><span class="informations">1916×678 69.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Cyril (2018-03-21 13:40 UTC)

<p>Hello,</p>
<p>first you need to test the correlation between your variable for example with a Pearson test. To check if for example, it is not the volume/surface that correlate with your variance than your high/low grade gliomas.</p>
<p>Than you must correct your test, i suppose wilcoxon? for multiple testing (bonferroni…)  see</p>
<p>A. Chalkidou, M. O’Doherty, P. Marsden, et al., PLoS one 10(5) (2015) e0124165.</p>
<p>It is better/necessary to do texture analysis in  3D.</p>
<p>See you,</p>
<p>Cyril Jaudet,</p>

---

## Post #8 by @ihnorton (2019-01-30 19:22 UTC)

<p>A post was split to a new topic: <a href="/t/radiomics-entropy-0/5583">Radiomics entropy=0?</a></p>

---
