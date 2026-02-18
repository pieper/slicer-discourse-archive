# Help needed - Segmentation

**Topic ID**: 31708
**Date**: 2023-09-14
**URL**: https://discourse.slicer.org/t/help-needed-segmentation/31708

---

## Post #1 by @Jakub (2023-09-14 11:25 UTC)

<p>Hi, I have a problem and hope someone could adivise. The problem is that the segmented teeth are moved outside the border of the CT image that is being worked on and are reduced in size so that they do not fit in the CT image as a whole. I don’t know how it could be fixed, please help! Many thanks in advance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7558dc7c43a4e61ba167379c1e5b7fdb0e138a3e.png" data-download-href="/uploads/short-url/gK6foZHvc8D4slbDcSKY0TJ1iRU.png?dl=1" title="Screen_of_issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7558dc7c43a4e61ba167379c1e5b7fdb0e138a3e_2_690x368.png" alt="Screen_of_issue" data-base62-sha1="gK6foZHvc8D4slbDcSKY0TJ1iRU" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7558dc7c43a4e61ba167379c1e5b7fdb0e138a3e_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7558dc7c43a4e61ba167379c1e5b7fdb0e138a3e_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7558dc7c43a4e61ba167379c1e5b7fdb0e138a3e_2_1380x736.png 2x" data-dominant-color="33333B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen_of_issue</span><span class="informations">1919×1025 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2023-09-14 15:07 UTC)

<p><a class="mention" href="/u/jakub">@Jakub</a> it looks like segmentation geometry and the volume doesn’t match.</p>
<p>In your screenshot there is no source volume set. does setting it to the CBCT fix it? If not, please explain how you generated this segmentation so that we can understand better where the mismatch is coming from.</p>
<p>Normally the segmentation geometry is matched to the source volume it is generated from.</p>

---

## Post #3 by @Jakub (2023-09-14 15:13 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> We are not really sure how it happend, because during segmentation 3D Slicer freezed and than the output like this, before freezening it was in order. Do you think it could be fixed?</p>
<p>How about skipping that one shot? The height of the layer (image) will be very high<br>
small and it would be possible to interpolate the missing data into the overall 3D.</p>
<p>Or replace the missing picture with a picture from around<br>
(previous/next).</p>
<p>Is that possible or another way would be better?</p>

---

## Post #4 by @muratmaga (2023-09-14 15:51 UTC)

<p>If this is indeed the segmentation of the displayed volume, you can try this:</p>
<ol>
<li>Right click on the segmentation and convert to labelmap</li>
<li>Obtain the Volume Information (under Volumes module, see the screenshot) of your CBCT</li>
<li>Edit the volume information of the labelmap to match the information from <span class="hashtag-raw">#2</span> exactly.</li>
<li>Right click on the labelmap and convert to segmentation.</li>
</ol>
<p>If this doesn’t fix, you need to provide your data so that we can take a close look.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/204038f86e6c07c72f490affb22281807fc516a9.jpeg" data-download-href="/uploads/short-url/4BiSgjQJXtt8XXFFj4ZYkuE9Kad.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/204038f86e6c07c72f490affb22281807fc516a9_2_690x357.jpeg" alt="image" data-base62-sha1="4BiSgjQJXtt8XXFFj4ZYkuE9Kad" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/204038f86e6c07c72f490affb22281807fc516a9_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/204038f86e6c07c72f490affb22281807fc516a9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/204038f86e6c07c72f490affb22281807fc516a9.jpeg 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">885×459 56 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Jakub (2023-09-15 03:59 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> After more thorough inspection by me and my colleagues we discovered that indeed the segmentation doesn’t match the volume. I apologize for the confusion. Thank you for your time and quick replies.</p>

---
