---
topic_id: 34983
title: "Help To Segment Multiple Sclerosis Plaques With Monai Label"
date: 2024-03-19
url: https://discourse.slicer.org/t/34983
---

# Help to Segment Multiple Sclerosis Plaques with MONAI Label

**Topic ID**: 34983
**Date**: 2024-03-19
**URL**: https://discourse.slicer.org/t/help-to-segment-multiple-sclerosis-plaques-with-monai-label/34983

---

## Post #1 by @franbuemi (2024-03-19 17:39 UTC)

<p>Hi everyone, I would like to train a model to segment multiple sclerosis plaques on 3D FLAIR images, one by one, each with distinct labels. I’ve started with a dataset of 10 patients just to get started before tackling segmentation on a larger number of cases. As described in the tutorial “MONAI Label - Training from Scratch (<a href="https://www.youtube.com/watch?v=3HTh2dqZqew" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=3HTh2dqZqew</a>)”, I modified the dictionary in the deepedit.py file by adding labels like “lesion1, lesion2, lesion3,” etc. (I’ve included 7 labels) and then changed “use_pretrained_model” to “false”. As seen in the screenshot, I’ve just reached an accuracy of 27%. However, even after adding additional labels for lesions in the segment editor (such as lesion8, lesion9, lesion10, etc., since some cases have more than 7 plaques), it seems that lesions beyond the seventh one are not considered during training (see the terminal screenshot). How can I resolve these issues? Would training on more cases lead to better accuracy?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9dc846480e6eacbffab25ef6c189ee43d4006205.jpeg" data-download-href="/uploads/short-url/mvO32ErupKyvzk4HzO8S9ZxTgAl.jpeg?dl=1" title="MS1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9dc846480e6eacbffab25ef6c189ee43d4006205_2_690x369.jpeg" alt="MS1" data-base62-sha1="mvO32ErupKyvzk4HzO8S9ZxTgAl" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9dc846480e6eacbffab25ef6c189ee43d4006205_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9dc846480e6eacbffab25ef6c189ee43d4006205_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9dc846480e6eacbffab25ef6c189ee43d4006205_2_1380x738.jpeg 2x" data-dominant-color="898B89"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MS1</span><span class="informations">1920×1027 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5897a8100c060621f67a88e15ba2bdbb0d564a6b.png" data-download-href="/uploads/short-url/cDIWh8jjlI2u3CFFvZM3KIvUT7J.png?dl=1" title="MS2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5897a8100c060621f67a88e15ba2bdbb0d564a6b.png" alt="MS2" data-base62-sha1="cDIWh8jjlI2u3CFFvZM3KIvUT7J" width="562" height="500" data-dominant-color="222222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MS2</span><span class="informations">1103×980 47.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
