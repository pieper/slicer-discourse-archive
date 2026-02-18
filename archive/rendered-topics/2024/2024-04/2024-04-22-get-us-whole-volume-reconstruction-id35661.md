# Get US whole volume reconstruction

**Topic ID**: 35661
**Date**: 2024-04-22
**URL**: https://discourse.slicer.org/t/get-us-whole-volume-reconstruction/35661

---

## Post #1 by @LeidyMoraV (2024-04-22 21:09 UTC)

<p>Hi,</p>
<p>I want to reconstruct the whole vertebrae volume based on the ultrasound reconstruction (Img 1). for this I’m using the module ALPACA-SlicerMorph having as source other vertebrae reconstructed from CT(Img. 2), but when I see the TPS Warped source model this one is distorted (Img. 3). I’ve tried with cut reconstruction from CT to only take the posterior park and they work, but when I use the US reconstruction it doesn’t. What can I do?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87695411c6291a974bed98f6ac5ce38a0d4aacfa.png" data-download-href="/uploads/short-url/jjU7EXvzixxIaJCpgHm5Qf83AGS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87695411c6291a974bed98f6ac5ce38a0d4aacfa_2_452x500.png" alt="image" data-base62-sha1="jjU7EXvzixxIaJCpgHm5Qf83AGS" width="452" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87695411c6291a974bed98f6ac5ce38a0d4aacfa_2_452x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87695411c6291a974bed98f6ac5ce38a0d4aacfa.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87695411c6291a974bed98f6ac5ce38a0d4aacfa.png 2x" data-dominant-color="9198C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">623×689 54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40adc3dcaf57804900cf702294a524dc81b96fb3.png" alt="image" data-base62-sha1="9eaQA3j4iJTmNMk1HyYPmDPxu3V" width="474" height="497"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67bf6994ddbe7a15b9d870edada2af875c61a776.png" data-download-href="/uploads/short-url/eNNhhhXA4z81nAjOJiRxO9Svkwu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67bf6994ddbe7a15b9d870edada2af875c61a776_2_423x500.png" alt="image" data-base62-sha1="eNNhhhXA4z81nAjOJiRxO9Svkwu" width="423" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67bf6994ddbe7a15b9d870edada2af875c61a776_2_423x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67bf6994ddbe7a15b9d870edada2af875c61a776.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67bf6994ddbe7a15b9d870edada2af875c61a776.png 2x" data-dominant-color="88A5AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">575×679 46.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-04-24 01:42 UTC)

<p>Do you see the entire veetebra in ultrasound? Is it in humans?</p>
<p>Many research group has been working on this problem, including our lab. You can also find PhD dissertations of students of Purang Abolmaesumi. All these were classic methods, such as image registration methods constrained by ultrasound-&gt;CT conversion, constrained by statistical shape models, biomechanics simulation, using free-form deformation, thin-plate splines, etc. Ultimately all these attempts failed to reach the quality needed for clinical usability.</p>
<p>Instead of retrying all these methods (PCA, thin-plate-splines, etc.) I would recommend to try deep learning based apporaches. Probably you could manually/semi-automatically segment a few hundred vertebrae using partial 3D ultrasound imaging as input and CT as output.</p>

---

## Post #3 by @LeidyMoraV (2024-04-24 21:25 UTC)

<p>Yes, it is within humans. In the ultrasound, I’m only able to visualize the posterior aspect of the vertebra, and that’s what I’m utilizing for the slicerIGT reconstruction.</p>
<p>Could you share with me any previous research conducted on this topic? Or perhaps suggest how I might find such studies?</p>
<p>I plan to explore the deep learning approach and determine how to integrate it into my research. Thank you!</p>

---

## Post #4 by @lassoan (2024-04-24 21:57 UTC)

<p>You can search for spine related papers from Purang Abolmaesumi <a href="https://scholar.google.com/scholar?hl=en&amp;as_sdt=0%2C33&amp;q=abolmaesumi+spine&amp;btnG=" class="inline-onebox">Google Scholar</a> or have a look at this <a href="https://qspace.library.queensu.ca/bitstream/handle/1974/6104/Khallaghi_Siavash_201009_MAS.pdf">PhD thesis</a>.</p>

---

## Post #5 by @LeidyMoraV (2024-05-01 21:37 UTC)

<p>Hi Andras,</p>
<p>While reviewing some of the spine-related papers you shared with me, I came across a research paper (<a href="https://link.springer.com/article/10.1007/s11548-015-1206-1" rel="noopener nofollow ugc">Towards real-time, tracker-less 3D ultrasound guidance for spine anaesthesia</a>) with results similar to what I’m aiming for, particularly in terms of adjusting the ultrasound surface to a shape model. I noticed you’re one of the authors of this paper. Is the logic code for the Registration thread available?</p>
<p>Thank you!</p>

---
