# pyradiomics w/ fixed bin width: bin number varies significantly across derived images

**Topic ID**: 24498
**Date**: 2022-07-26
**URL**: https://discourse.slicer.org/t/pyradiomics-w-fixed-bin-width-bin-number-varies-significantly-across-derived-images/24498

---

## Post #1 by @stef (2022-07-26 14:14 UTC)

<p>Hi all,</p>
<p>When using the fixed bin width setting, the median number of bins per patient varies a lot across the different derived images and the original image. I know this can be in part addressed by selecting a different bin width for e.g. original, LoG filtered and wavelet images. However, the same issue occurs across different e.g. wavelet decompositions which only differ in their directionality. Here’s an example:</p>
<p>Image → median number of bins across patient cohort<br>
wavelet-LLH → 172.5<br>
wavelet-LHL → 210.7<br>
wavelet-LHH → 35.0<br>
wavelet-HLL → 197.6<br>
wavelet-HLH → 33.6<br>
wavelet-HHL → 35.2<br>
wavelet-HHH → 8.8<br>
wavelet-LLL → 1132.2</p>
<p>Anyone familiar with this behaviour? How can this be addressed? Can I specify different binWidth settings for the above decompositions?</p>
<p>Any help would be appreciated <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Thanks much!</p>

---
