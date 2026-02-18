# Applying semi-landmarks obtained with PseudoLMGenerator to other models

**Topic ID**: 44783
**Date**: 2025-10-16
**URL**: https://discourse.slicer.org/t/applying-semi-landmarks-obtained-with-pseudolmgenerator-to-other-models/44783

---

## Post #1 by @BerfinSuYlcnts (2025-10-16 12:05 UTC)

<p>Hello,</p>
<p>I successfully completed the semi-landmark acquisition process on a sample model using the PseudoLMGenerator plugin. However, I only performed it for one sample.</p>
<p>Now, I want to apply the same number and equally spaced semi-landmarks to all my other models. For PCA analysis, the coordinates of all models must be consistent with each other.</p>
<p>How can I apply this process to all models in the most accurate and automated way?</p>
<p>Thank you very much in advance,<br>
Berfin</p>

---

## Post #2 by @muratmaga (2025-10-16 15:24 UTC)

<p>The idea behind PseudoLMGenerator is to use one sample as a representative of a population of samples to represent their geometry and then transfer this template set of points onto new samples by other means. You can do this in two ways:</p>
<ol>
<li>If you have set of sparse anatomical landmarks on all your samples, you can use SlicerMorph→Utilities→ProjectSemiLMs, which uses a combination of TPS deformation and point projection to move points to the target models. Note that if your manual landmarks are too sparse you may not get good results.</li>
<li>You can use ALPACA for a totally automated process: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ALPACA" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/ALPACA at main · SlicerMorph/Tutorials · GitHub</a> . It is default settings are usually OK for most samples, but you do want to experiment to improve the deformation and point correspondences.</li>
</ol>

---
