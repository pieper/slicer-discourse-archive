# Can you turn a video into a 3d model

**Topic ID**: 29677
**Date**: 2023-05-26
**URL**: https://discourse.slicer.org/t/can-you-turn-a-video-into-a-3d-model/29677

---

## Post #1 by @studyskin (2023-05-26 23:25 UTC)

<p>hello, im wondering if there is a way to turn pictures from a ct scan video into a 3d model in slicer. digimorph has a scan of an african wildcat but does not have the ct scan but they do have a video of each slice (<a href="http://www.digimorph.org/specimens/Felis_sylvestris_lybica/male/" class="inline-onebox" rel="noopener nofollow ugc">Digimorph - Felis silvestris lybica (African Wildcat) - male</a>), if i download all three videos and turn them into separate slices is there a way i can load them into slicer and tell it what axis it is? i assume when you normally load data the files have metadata telling the programme what axis and the slice width, thank you to anyone who can help i dont know if this is actually possible</p>

---

## Post #2 by @muratmaga (2023-05-26 23:30 UTC)

<p>You can extract individual frames from the video using ffmpeg and then import the resultant sequence into slicer via imagestacks. Unfortunately you will have no idea about spacing and have to approximate it by trial and error.</p>

---

## Post #3 by @studyskin (2023-06-01 21:41 UTC)

<p>thank you so much for the reply! how do i tell it what images to use for what plane? i loaded them in and it looks like this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00fa3986b41e318fc77752a8295ff434af13a7f7.png" data-download-href="/uploads/short-url/8E6rFuXLbU8cDCTdvy9uF31GhF.png?dl=1" title="slicercatnowork" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00fa3986b41e318fc77752a8295ff434af13a7f7_2_690x388.png" alt="slicercatnowork" data-base62-sha1="8E6rFuXLbU8cDCTdvy9uF31GhF" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00fa3986b41e318fc77752a8295ff434af13a7f7_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00fa3986b41e318fc77752a8295ff434af13a7f7_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00fa3986b41e318fc77752a8295ff434af13a7f7_2_1380x776.png 2x" data-dominant-color="717379"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicercatnowork</span><span class="informations">1920×1080 387 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @muratmaga (2023-06-02 00:11 UTC)

<p>There is something weird. I think you might have more than one stack in the same folder, as the ImageStacks is reporting the file dimensions as 4 (it should have been 3). The issue is also clear in green and yellow slices, you have more than more orientation stacked in them.</p>
<p>When you are exporting frames from the video, make sure you are exporting frames belonging the same plane.</p>

---

## Post #5 by @muratmaga (2023-06-02 05:12 UTC)

<p>Here is what my import looks like (I used the coronal.mp4). Of course the proportions are wrong since I do not know what the spacing needs to be.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72fdb1fc5aadb59a53be172c6e2764ae088e72a8.jpeg" data-download-href="/uploads/short-url/gpfYdl4E8X5mzp3iKHYASW93r6g.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72fdb1fc5aadb59a53be172c6e2764ae088e72a8_2_690x401.jpeg" alt="image" data-base62-sha1="gpfYdl4E8X5mzp3iKHYASW93r6g" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72fdb1fc5aadb59a53be172c6e2764ae088e72a8_2_690x401.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72fdb1fc5aadb59a53be172c6e2764ae088e72a8_2_1035x601.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72fdb1fc5aadb59a53be172c6e2764ae088e72a8_2_1380x802.jpeg 2x" data-dominant-color="98959D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1529×890 239 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @studyskin (2023-06-03 21:58 UTC)

<p>it works thank you! just one more question, your model is more detailed than mine, did you do anything extra? i just loaded it and selected with segment editor and turned into a model<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24d6fd166248e83ae54d27506e76d58d71206aeb.png" data-download-href="/uploads/short-url/5fTNAXc7esCC6skIVrgGSXUnmUr.png?dl=1" title="digicatwork" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d6fd166248e83ae54d27506e76d58d71206aeb_2_690x388.png" alt="digicatwork" data-base62-sha1="5fTNAXc7esCC6skIVrgGSXUnmUr" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d6fd166248e83ae54d27506e76d58d71206aeb_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d6fd166248e83ae54d27506e76d58d71206aeb_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d6fd166248e83ae54d27506e76d58d71206aeb_2_1380x776.png 2x" data-dominant-color="6F7276"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">digicatwork</span><span class="informations">1920×1080 418 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @muratmaga (2023-06-04 03:58 UTC)

<p>I used volume rendering, which often results in better looking visualization then surface rerndering of segmented objects.</p>

---

## Post #8 by @studyskin (2023-06-04 08:54 UTC)

<p>ah! ok thank you, can you export the volume rendering model? im trying but cant find a way too, if there is one, thank you again for your help</p>

---

## Post #9 by @muratmaga (2023-06-04 15:52 UTC)

<p>No, volume rendering is just a visualization technique. If you need to export a model, you need to segment.</p>

---
