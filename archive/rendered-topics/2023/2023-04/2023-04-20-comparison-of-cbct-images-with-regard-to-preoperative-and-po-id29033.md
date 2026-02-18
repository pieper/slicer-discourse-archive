# Comparison of CBCT images with regard to preoperative and postoperative position and relation

**Topic ID**: 29033
**Date**: 2023-04-20
**URL**: https://discourse.slicer.org/t/comparison-of-cbct-images-with-regard-to-preoperative-and-postoperative-position-and-relation/29033

---

## Post #1 by @vollmer_a (2023-04-20 22:03 UTC)

<p>Dear colleagues,</p>
<p>I work as a facial surgeon at a German university hospital and we would very much like to compare the position of a mandible using CBCT images. This is to compare tumour patients and orthopaedic dysgnathia patients to ensure the best possible outcome.</p>
<p>We have already tried different things but always without satisfactory results.</p>
<ol>
<li>is there a possibility to overlay the two CBCT images directly, automated and standardised?</li>
<li>is there a possibility to determine the degree of agreement on the basis of numerical values (e.g. percentage or other numerical scales)?</li>
<li>is it possible to display the degree of superimposition using a colour scheme?</li>
</ol>
<p>Thank you for your support</p>
<p>Kind regards</p>
<p>A. Vollmer</p>
<p>Translated with <a href="http://www.DeepL.com/Translator" class="inline-onebox" rel="noopener nofollow ugc">DeepL Translate: The world's most accurate translator</a> (free version)</p>

---

## Post #2 by @finetjul (2023-04-21 17:46 UTC)

<p>Dear Andreas,</p>
<p>Regarding question 1) :<br>
a) To overlay, you need to select your CBCT volumes as background AND background volumes (see here how to do so <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view" class="inline-onebox" rel="noopener nofollow ugc">User Interface — 3D Slicer documentation</a>). You can then change foreground opacity to see the underlying background volume.<br>
b) For manually aligning volumes, you need to play with the “transform” module: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html" class="inline-onebox" rel="noopener nofollow ugc">Transforms — 3D Slicer documentation</a><br>
c) For automatic alignment, you need to “register” the volumes: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Registration" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Training - Slicer Wiki</a></p>
<p>For you other questions, it is doable, but my understanding is that requires a bit of Python coding.</p>
<p>Regards, Julien.</p>

---

## Post #3 by @lassoan (2023-04-21 21:13 UTC)

<p>You can get numerical (maximum distance) and visual comparison (with coloring) without Python scripting if you can segment the same  anatomical structure in both images. You can get distance between segments using Segment Comparison module (in SlicerRT extension) and coloring based on distance using Model To Model Distance module (in ModelToModelDistance extension).</p>

---

## Post #4 by @danik (2023-12-24 19:47 UTC)

<p>Good afternoon. I did everything as you said, everything was successful, thank you very much. I would like to know whether it is possible to perform a superimposition in a certain area, for example, sphenoethmoidal synchondrosis develops by the age of 8 and it is beneficial to do an overlay on this structure; also, during orthodontic treatment, the teeth move and the overlay of the full volume of CT is not correct.</p>

---
