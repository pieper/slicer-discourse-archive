---
topic_id: 28056
title: "Trouble Combining Fscv Files"
date: 2023-02-27
url: https://discourse.slicer.org/t/28056
---

# trouble combining .fscv files

**Topic ID**: 28056
**Date**: 2023-02-27
**URL**: https://discourse.slicer.org/t/trouble-combining-fscv-files/28056

---

## Post #1 by @sedwards (2023-02-27 03:34 UTC)

<p>I have been merging .fcsv files from online sources and my own data. But when I try to analyze the files altogether in GPA, I get an error like: "Error: load file failed: There are 459 landmarks instead of 431. How does GPA decide which number of landmarks to use and how can I generate the correct number in the PseudoLMgenerator?</p>
<p>Scott</p>

---

## Post #2 by @muratmaga (2023-02-27 03:57 UTC)

<p>It is not clear to me what you are trying to do. For GPA you do not need to merge files or anything. Simply provide all fcsv (or jsons) in one folder, or select them via the dialog box. However, for GPA module to work all included files need to have exactly the same number of landmarks.</p>
<p>The error you included indicates that your files have different number of landmarks (first one had 459, and the second 431).</p>
<p>There is no “correct” number of LMs that PseudoLMGenerator generates. It will generate hundreds to thousands LM based on the geometry of the sample you chose as reference, and the sparsity you requested. You can read the tutorial here: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/PseudoLMGenerator" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/PseudoLMGenerator at main · SlicerMorph/Tutorials · GitHub</a></p>
<p>Are you trying to use the PseudoLMGenerator with more than one 3D model? If you do that you will get different sets of LMs, because each model have a different geometry. PseudoLMGenerator should be used only on reference specimen, and to landmark rest of your models, you can use the ALPACA module, which will transfer those LMs to based on their geometry.</p>
<p>Please explain what you are trying to do a bit more clearly.</p>

---

## Post #3 by @sedwards (2023-02-27 12:23 UTC)

<p>Dear Murat,</p>
<p>Thank you very much for this quick and informative response. Indeed I was inadvertently trying to merge .fcsv files generated from two different models. I see now that this is a mistake and will go back and use only one model.</p>
<p>I am still curious how Slicer decides what is the correct number of landmarks when doing GPA when there is a mixture of different row numbers. Is it the number that is first encountered in the fcsvs? I see now that it is important to save the one model for any analysis, so that it can be applied to different targets in different sessions.</p>
<p>Thanks again,</p>
<p>Scott</p>

---

## Post #4 by @muratmaga (2023-02-27 15:41 UTC)

<aside class="quote no-group" data-username="sedwards" data-post="3" data-topic="28056">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/838e76/48.png" class="avatar"> sedwards:</div>
<blockquote>
<p>how Slicer decides what is the correct number of landmarks when doing GPA</p>
</blockquote>
</aside>
<p>Yes, we obtain the number of landmark from the first file read and assume every other file has identical number of lms (as they should, since it is a requirement of Procrustes analysis). İf they don’t, the error you encounter is generated.</p>

---
