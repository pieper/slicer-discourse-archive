# Saving landmark files for ALPACA - details requested

**Topic ID**: 38248
**Date**: 2024-09-06
**URL**: https://discourse.slicer.org/t/saving-landmark-files-for-alpaca-details-requested/38248

---

## Post #1 by @pamelaeck (2024-09-06 00:20 UTC)

<p>Still a newbie here … I created a landmark template for a fifth cervical vertebra and want to transfer the landmarks to more C5 vertebrae via ALPACA.</p>
<p>I see in the ALPACA tutorial that the source mesh is a .ply and the source landmark file is .fcsv, but I have several landmarks saved as .json.</p>
<p>Could you be more specific as to how to save the landmark template files to use in ALPACA?</p>
<p>Thank you SO much!<br>
Pamela<br>
Equus Soma Osteology &amp; Anatomy Learning Center</p>

---

## Post #2 by @muratmaga (2024-09-06 01:18 UTC)

<p>The final outcome is called <strong>Final ALPACA landmark estimate</strong> and that’s what’s displayed in the screen when the ALPACA execution is completed.</p>
<p>Are you following this tutorial: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ALPACA" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/ALPACA at main · SlicerMorph/Tutorials · GitHub</a></p>

---

## Post #3 by @jamesobutler (2024-09-06 02:18 UTC)

<p>There appears to be confusion that the tutorial uses sample data that includes a .fcsv file however the original poster is doing their own work and only has .mrk.json files.</p>

---

## Post #4 by @muratmaga (2024-09-06 03:05 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="38248">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>poster</p>
</blockquote>
</aside>
<p>from ALPACA’s operability perspective fcsv and json (or .mrk.json) are the same. To encourage its usage, we have the default option to save the files in .json format (when ALPACA is run in batch mode).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd9ae87fea9bc0edf7ebf2da4ed13bc49b77d1aa.png" data-download-href="/uploads/short-url/tkRLMHsw4tG4g8F225nvcO9YohY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd9ae87fea9bc0edf7ebf2da4ed13bc49b77d1aa_2_533x500.png" alt="image" data-base62-sha1="tkRLMHsw4tG4g8F225nvcO9YohY" width="533" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd9ae87fea9bc0edf7ebf2da4ed13bc49b77d1aa_2_533x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd9ae87fea9bc0edf7ebf2da4ed13bc49b77d1aa_2_799x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd9ae87fea9bc0edf7ebf2da4ed13bc49b77d1aa_2_1066x1000.png 2x" data-dominant-color="F2F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1308×1226 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This can be set back to FCSV if the user chooses to do so.</p>

---

## Post #5 by @jamesobutler (2024-09-06 04:06 UTC)

<p>It may be clearer for new users if the sample data for the ALPACA tutorial was also in the latest file formats. In this case updating the ALPACA tutorial to use .mrk.json files may be more helpful to match how things look when using latest Slicer today.</p>

---

## Post #6 by @pamelaeck (2024-09-06 11:56 UTC)

<p>Yes, I started following that tutorial.</p>
<p>I first watched this video which describes exactly what I want to do. <a href="https://youtu.be/ZRikzsUBeAE?si=GASvFcEDnk9ymzL9" rel="noopener nofollow ugc">https://youtu.be/ZRikzsUBeAE?si=GASvFcEDnk9ymzL9</a>.</p>
<p>I realize it is 3 years old, but nevertheless the gentleman is demonstrating how to transfer the landmarks between 2 bones and he uses the single alignment which “requires” .fcsv format for the landmarks.</p>
<p>My specimens (equine cervical vertebrae) have a combination of point landmarks (17), closed and open lines (10).  I created a template on C5 (fifth cervical). Now I want to duplicate the template on the other 40+ C5 bones.</p>
<p>I understand that .fcsv format is used for the Single Alignment Source Landmark Set. Do I need to put all of the landmarks in a single folder?  Or is there a way to save the all the landmarks in the template as one .fcvs file?</p>
<p>Thank you for your patience!</p>

---

## Post #7 by @muratmaga (2024-09-06 15:04 UTC)

<aside class="quote no-group" data-username="pamelaeck" data-post="6" data-topic="38248">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/3bc359/48.png" class="avatar"> pamelaeck:</div>
<blockquote>
<p>I understand that .fcsv format is used for the Single Alignment Source Landmark Set. Do I need to put all of the landmarks in a single folder? Or is there a way to save the all the landmarks in the template as one .fcvs file?</p>
</blockquote>
</aside>
<p>Please follow this section of the tutorial on batch processing: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ALPACA#batch-processing" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/ALPACA at main · SlicerMorph/Tutorials · GitHub</a></p>
<p>Yes, just specify the output folder for landmarks to be saved. In batch mode you will enter the location of the source model and landmark pair you used. If you are using the single-template, there will be only one pair. If you are using multi-template (MALPACA), there should be as many pairs as your models. Make sure the file prefixes before the extension (.ply, .fcsv, ,json) are identical, as we use that to match the landmarks to the models.</p>
<p>Your landmarks for the new models will be saved into the output landmark folder you specify.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9dba1ac8567bb46b75cf7983acf39daa37b32d94.png" data-download-href="/uploads/short-url/mvjGN0wlotDmOFqiubt11j9gnfC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9dba1ac8567bb46b75cf7983acf39daa37b32d94_2_690x371.png" alt="image" data-base62-sha1="mvjGN0wlotDmOFqiubt11j9gnfC" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9dba1ac8567bb46b75cf7983acf39daa37b32d94_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9dba1ac8567bb46b75cf7983acf39daa37b32d94_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9dba1ac8567bb46b75cf7983acf39daa37b32d94.png 2x" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1342×722 51.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @pamelaeck (2024-09-07 13:20 UTC)

<p>Thank you!</p>
<p>I just generated my first target with the LMs from the source, yaay!!</p>
<p>These LMs are the points I placed on the source, but I also used open and closed lines.</p>
<p>How can I add these so they are also transferred to the targets?</p>
<p>Screenshot of my source template:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2ce7770206575f00062d229f755c32bea70d1fe6.jpeg" data-download-href="/uploads/short-url/6peV27uxKwLmwS4gyYOokB9kDwW.jpeg?dl=1" title="Template-C5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2ce7770206575f00062d229f755c32bea70d1fe6_2_562x499.jpeg" alt="Template-C5" data-base62-sha1="6peV27uxKwLmwS4gyYOokB9kDwW" width="562" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2ce7770206575f00062d229f755c32bea70d1fe6_2_562x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2ce7770206575f00062d229f755c32bea70d1fe6_2_843x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2ce7770206575f00062d229f755c32bea70d1fe6_2_1124x998.jpeg 2x" data-dominant-color="979A95"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Template-C5</span><span class="informations">1322×1176 75.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @muratmaga (2024-09-07 19:01 UTC)

<p>Just load a new vertebra (one that you want to transfer LMs too), then choose this model as target and just run alpaca.</p>
<p>Note that if you transfer equidistant curve semi LM with ALPACA, transferred semiLMs may not be equidistant anymore.</p>

---

## Post #12 by @pamelaeck (2024-09-08 15:18 UTC)

<p>I must be missing an important file saving option in Slicer…</p>
<p>When I save this model, which I created as a template, the point list is all one file, but the curves are saved as individual files.</p>
<p>When I try to load this model in ALPACA/Batch, I can select only the point list or just one of the curve nodes, not the complete template.</p>
<p>In other words, how do I save both the points and curves as a “set”?  That I can then enter for the Source landmarks?</p>
<p>Thank you … again!</p>

---

## Post #13 by @pamelaeck (2024-09-08 16:55 UTC)

<p>Replying to myself with an update on my question … I did a search and found reference in some 2021 posts to using the “MergeMarkups” so I’ll study the tutorial and hopefully that will be my solution!</p>

---

## Post #14 by @muratmaga (2024-09-08 17:16 UTC)

<p>Yes, ALPACA will transfer only one set of LMs. So if you have landmarks into two different files, you will need to merge them, and then run ALPACA.</p>
<p>However, as I said above I do not suggest using ALPACA to transfer equidistant semiLMs that you generate using the curve resampling option.</p>

---

## Post #15 by @pamelaeck (2024-09-08 17:29 UTC)

<p>Can you suggest another/better method?</p>

---

## Post #16 by @muratmaga (2024-09-08 19:56 UTC)

<p>If am not aware of a method that will reliably transfer semiLMs from a manually drawn curve to the targets, while preserving the equal distance criteria.</p>
<p>What you can possibly do, is to draw the curves on all your samples, and then use python script to load the associated model, run the resample curve method, and save the output as a new curve object. However, unless you are planning to do hundreds of them, the time investment of development of script is probably not worthwhile. Resample is so fast, the script is only going to save you a few seconds and a few clicks per specimen.</p>

---

## Post #17 by @pamelaeck (2024-09-08 23:09 UTC)

<p>Since I know nothing about python or any other scripts, I’ll think of a work around.</p>
<p>Meanwhile, one more question. When I import 2 or more meshes into Slicer, they appear as such:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2ceb827ebf581d64d02df68251aaca524784600f.jpeg" data-download-href="/uploads/short-url/6pnAkBivrEGBC93HdkT1u3gpfoH.jpeg?dl=1" title="2 Model registration" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2ceb827ebf581d64d02df68251aaca524784600f_2_576x500.jpeg" alt="2 Model registration" data-base62-sha1="6pnAkBivrEGBC93HdkT1u3gpfoH" width="576" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2ceb827ebf581d64d02df68251aaca524784600f_2_576x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2ceb827ebf581d64d02df68251aaca524784600f_2_864x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2ceb827ebf581d64d02df68251aaca524784600f.jpeg 2x" data-dominant-color="8C8589"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2 Model registration</span><span class="informations">954×828 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>A lovely “hug”, but is there an option for the models to remain separate as shown in the ALPACA tutorial?</p>

---

## Post #18 by @muratmaga (2024-09-08 23:33 UTC)

<aside class="quote no-group" data-username="pamelaeck" data-post="17" data-topic="38248">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/3bc359/48.png" class="avatar"> pamelaeck:</div>
<blockquote>
<p>A lovely “hug”, but is there an option for the models to remain separate as shown in the ALPACA tutorial?</p>
</blockquote>
</aside>
<p>3D Slicer will display models based on the image dimensions provided by the model. You can turn on/off the visibility of each model so see one at a time, or you can use dual 3D viewer, and assign each model to different vewiers. I suggest making yourself more familiar with these types of operations in Slicer. A good place to start is the Slicer user tutorial. <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#" class="inline-onebox" rel="noopener nofollow ugc">User Interface — 3D Slicer documentation</a></p>
<p>If you want to translate move one of them to elsewhere in the scene, you can use the Transforms module (see the same link on how to use the transforms module). However, I suggest only moving the target model. If you translate the source model, you should also translate the corresponding landmarks.</p>

---

## Post #19 by @pamelaeck (2024-09-08 23:56 UTC)

<p>Once again  thank you for your quick reply and suggestions.</p>
<p>I am trying to learn as much of the basics of Slicer/SlicerMorph as I can.  However, I know you will appreciate the urgency involved when one is on a time-line to publish, LOL.</p>
<p>Your help and time providing it is greatly appreciated.</p>
<p>Pamela<br>
Equus Soma Osteology &amp; Anatomy Learning Center.</p>

---

## Post #20 by @pamelaeck (2024-10-04 23:24 UTC)

<p>Is there a way to save /export these 2 models together as a .ply or .stl so I can share them with colleagues as one 3D model?</p>
<p>Thanks!</p>
<p><a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/853def4df347e90c4638fde55f01a45e83ed15bb.jpeg" alt="Dual C6" data-base62-sha1="j0IchZVr0loYFBTxFmYAjpCuvBV" width="690" height="427"><br>
</a></p>

---

## Post #21 by @muratmaga (2024-10-04 23:28 UTC)

<p>You can merge them, but then your colleagues will loose the ability to turn one on/off. They will be blocking each other.</p>
<p>Your safest option is to export them individually, and share that way. Or better yet, if they are using Slicer package your scene as MRB and share that with them.</p>

---

## Post #22 by @pamelaeck (2024-10-04 23:44 UTC)

<p>I don’t want them to turn on/off, just be able to roll them around and inspect them from all sides to relate the relative morphological characteristics.</p>

---

## Post #23 by @muratmaga (2024-10-04 23:46 UTC)

<p>I don’t understand how they can do that when one model is blocking the other.</p>
<p>In any event, try the <code>Merge Models</code> module to turn them into a single model.</p>

---

## Post #24 by @pamelaeck (2024-10-05 00:03 UTC)

<p>I have the opacity reduced on one model, so we can see what lies underneath on the other model.</p>
<p>Horses have a congenital malformation in the lower cervical vertebrae where one transforms into the physical identity of the one before it, i.e., C6 assumes physical characteristics of C5; C7 assumes characteristics of C6. All this during embryogenesis.  The end result is a spectrum of stages of the transformations (hometic) that we are finding via X-ray and dissection.</p>
<p>My goal is to use GMM to prove that the morphological characteristics (landmarks) are homologous. But the learning curve of GMM for me is steep and I discovered this illustration is great way to show my colleagues in the meantime.</p>
<p>Sorry for the long explanation, but I figured you would understand.  I will try the Merge Models module as you suggested.  I assume then I can save/export the merged model as a .ply or .stl?</p>

---

## Post #25 by @muratmaga (2024-10-05 00:25 UTC)

<aside class="quote no-group" data-username="pamelaeck" data-post="24" data-topic="38248">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/3bc359/48.png" class="avatar"> pamelaeck:</div>
<blockquote>
<p>I have the opacity reduced on one model, so we can see what lies underneath on the other model.</p>
</blockquote>
</aside>
<p>That’s a visualization technique that works when you have two <strong>separate</strong> models, one opaque one translucent. When you merge them into one, you can’t do that anymore.</p>
<p>If you want to share it that way, your best option is to package the scene as a MRB file as I mentioned before, share it with your colleagues and ask them to open it with Slicer.</p>

---
