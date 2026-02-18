# Can the modeled files be moved?

**Topic ID**: 22286
**Date**: 2022-03-03
**URL**: https://discourse.slicer.org/t/can-the-modeled-files-be-moved/22286

---

## Post #1 by @zhuyingxinxs (2022-03-03 13:20 UTC)

<p>Can modeled files be dragged to locations? The modeled skin and bones are in the wrong position and need to be moved<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e82f67a8fe0e914d1ec70d8f4c31b522ff93b689.png" data-download-href="/uploads/short-url/x80kWcAWZad8ucN1Ua7ICN9Yz7X.png?dl=1" title="7PWNEV4O}8H)PCEVB`NJS29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e82f67a8fe0e914d1ec70d8f4c31b522ff93b689_2_690x277.png" alt="7PWNEV4O}8H)PCEVB`NJS29" data-base62-sha1="x80kWcAWZad8ucN1Ua7ICN9Yz7X" width="690" height="277" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e82f67a8fe0e914d1ec70d8f4c31b522ff93b689_2_690x277.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e82f67a8fe0e914d1ec70d8f4c31b522ff93b689_2_1035x415.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e82f67a8fe0e914d1ec70d8f4c31b522ff93b689.png 2x" data-dominant-color="9A9BC8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">7PWNEV4O}8H)PCEVB`NJS29</span><span class="informations">1099×442 77.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df5b6a5e44a9b5aebe4e5a17e410ed1c3186938e.png" data-download-href="/uploads/short-url/vRUkCXUGCEFxVaSVL1vcC3WyjU2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df5b6a5e44a9b5aebe4e5a17e410ed1c3186938e_2_621x500.png" alt="image" data-base62-sha1="vRUkCXUGCEFxVaSVL1vcC3WyjU2" width="621" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df5b6a5e44a9b5aebe4e5a17e410ed1c3186938e_2_621x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df5b6a5e44a9b5aebe4e5a17e410ed1c3186938e_2_931x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df5b6a5e44a9b5aebe4e5a17e410ed1c3186938e.png 2x" data-dominant-color="9E9DC4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1100×885 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2022-03-03 20:07 UTC)

<p>You can move models (and anything else in displayed in Slicer) by applying transforms. Create a new linear transform node using the Transforms module (in the Active Transform dropbox, choose “Create new Linear Transform as…”).  Then expand the “Display” section (this seems to be necessary to create the default display node which enables interaction).  Check the “Visible in 3D view” checkbox, and then uncheck “Enable rotation” (because it looks like your models are rotationally aligned and only need to be translated).  In the “Apply transform” section, select the model you want to move on the list of “Transformable” items, and press the right green arrow button to apply the current transform to it, moving it to the “Transformed” list.  Now, the transformed model will move as you move the transform.<br>
In the “Interaction” section of the “Display” section of the “Transforms” module, click the “Update bounds” button, and the display of the transform bounding box in the 3D view should now match the extent of the transformed model.  To translate the model in 3D, click and drag with the <strong>middle</strong> mouse button.  If you need to rotate the models to match, then enable rotation, and you can rotate by left clicking and dragging on the bounding box of the transform.</p>

---

## Post #3 by @zhuyingxinxs (2022-03-05 08:00 UTC)

<p>Thank you very much for your reply!</p>

---

## Post #4 by @lassoan (2023-03-21 02:00 UTC)



---
