# Averaging models (again and again)

**Topic ID**: 36754
**Date**: 2024-06-13
**URL**: https://discourse.slicer.org/t/averaging-models-again-and-again/36754

---

## Post #1 by @coco (2024-06-13 11:16 UTC)

<p>Dear all,<br>
There have been several posts about averaging models and some answers, including one marked as solutions. But I am still left unable to actually do this myself and forgive me, but I don’t feel it was very explicit how to do the averaging.<br>
My guess is that people have been succesful at averaging several models or creating an average model based on slicermorph and using mark ups. Unfortunately, I don’t understand how. Could there be a demonstration or clear instructions on how to achieve this ?<br>
Many thanks</p>

---

## Post #2 by @muratmaga (2024-06-13 14:55 UTC)

<p>If you run a GPA on your dataset, to get an average model all you have to do is to go to visualization tab, select the 3d model visualization and specify which what reference model and its corresponding set of landmarks to use, and hit apply.</p>
<p>Then you blue model that appears in your right viewer is your “average model” based on the landmarks and samples you included in the analysis.</p>
<p>If you want to export that, go to the data model, right click on the node that says PCA Warped Volume (blue model), and the choose export to file. There are bunch of things there, you only care for the PLY model.</p>
<p>However, if you want to preserve the scale of the original data, before proceeding with GPA, you need to enable the Boas coordinates option. Otherwise everything will be in unit dimensions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/688ee7f7d6c0c709920d5decdecfba59ddc50dce.jpeg" data-download-href="/uploads/short-url/eUXPzMjovX5xtVXV31ki7ajRSsC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/688ee7f7d6c0c709920d5decdecfba59ddc50dce_2_690x313.jpeg" alt="image" data-base62-sha1="eUXPzMjovX5xtVXV31ki7ajRSsC" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/688ee7f7d6c0c709920d5decdecfba59ddc50dce_2_690x313.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/688ee7f7d6c0c709920d5decdecfba59ddc50dce_2_1035x469.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/688ee7f7d6c0c709920d5decdecfba59ddc50dce_2_1380x626.jpeg 2x" data-dominant-color="B9B6C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×872 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @coco (2024-06-13 15:27 UTC)

<p>Thanks Murat!<br>
This is where I am confused. I’m obviously mistaking “reference model” and “averaged model”. I have a series of brains I want to average so I don’t have a single reference brain. Does this make sense ?</p>
<p>ps small personal note if I am allowed: We got some excellent results with nnUnet for automated segmentation <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
<p>Thanks again</p>

---

## Post #4 by @muratmaga (2024-06-13 15:53 UTC)

<aside class="quote no-group" data-username="coco" data-post="3" data-topic="36754">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/8797f3/48.png" class="avatar"> coco:</div>
<blockquote>
<p>ins I want to average so I don’t have a single reference brain.</p>
</blockquote>
</aside>
<p>If you are going to do this with landmarks, you do have to have a reference model. That’s because that reference model gets warped to the calculated mean shape and becomes the average model. The denser your landmarks are, the closer the warping is.</p>
<p>If you do want to generate a new “average brain” from a set of segmented images, there are many pipelines (e.g., <a href="https://github.com/ANTsX/ANTs/blob/master/Scripts/antsMultivariateTemplateConstruction2.sh" class="inline-onebox">ANTs/Scripts/antsMultivariateTemplateConstruction2.sh at master · ANTsX/ANTs · GitHub</a>). We will soon have that in SlicerANTs, but it is probably couple months out.</p>
<p>You can read more about template reconstruction with ANTs here: <a href="https://github.com/ntustison/TemplateBuildingExample" class="inline-onebox">GitHub - ntustison/TemplateBuildingExample: Just when I thought you couldn’t possibly be any dumber, you go and do something like this… and totally redeem yourself!</a></p>

---

## Post #5 by @coco (2024-06-13 16:09 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="36754">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>you do have to have a reference model.</p>
</blockquote>
</aside>
<p>Dear Murat, thank you again for taking the time explaining and my apologies for needing further clarifications:<br>
If I have a series of “control” brains, I could use any of them as reference and they will be warped according to the calculated mean shape, essentially giving the same result each time I use a different “control” reference ?<br>
Great news for the ANTs implementation, looking forward to this !<br>
s</p>

---

## Post #6 by @muratmaga (2024-06-13 16:54 UTC)

<aside class="quote no-group" data-username="coco" data-post="5" data-topic="36754">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/8797f3/48.png" class="avatar"> coco:</div>
<blockquote>
<p>If I have a series of “control” brains, I could use any of them as reference and they will be warped according to the calculated mean shape, essentially giving the same result each time I use a different “control” reference ?</p>
</blockquote>
</aside>
<p>This in principle is true. However, in practice the reference will have bias (that’s a fact of all template based methods). This bias will be a factor of (1) how different is the reference with respect to the true mean; (2) how sparse these landmarks are.</p>
<p>(1) is usually not too much a concern in within population analysis provided and provided that for (2) you are using at least a couple dozen points.</p>
<p>In GPA output the samples closest to the mean (in landmark space) is provided. Our suggetion is to use that as the reference model.</p>

---
