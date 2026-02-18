# Create a parameterNode for a toolbar?

**Topic ID**: 20709
**Date**: 2021-11-19
**URL**: https://discourse.slicer.org/t/create-a-parameternode-for-a-toolbar/20709

---

## Post #1 by @mau_igna_06 (2021-11-19 22:19 UTC)

<p>Hi devs.</p>
<p>I’m creating a toolbar that will have several actions. Some of them are zoom, rotate, brightness&amp;contrast and flipView. These are special because when the corresponding toolbar button is checked, a popup widget per view will appear to let the user change the corresponding settings.</p>
<p>See the pictures below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3efc60be1d9d2a8fa67f92367c102b1a0eea77c.jpeg" data-download-href="/uploads/short-url/yNXJKAX1uOSjq8ioZC7gNeKZdbC.jpeg?dl=1" title="6558c3bb-06aa-4791-bd9e-90a16f18fa25" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3efc60be1d9d2a8fa67f92367c102b1a0eea77c_2_666x500.jpeg" alt="6558c3bb-06aa-4791-bd9e-90a16f18fa25" data-base62-sha1="yNXJKAX1uOSjq8ioZC7gNeKZdbC" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3efc60be1d9d2a8fa67f92367c102b1a0eea77c_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3efc60be1d9d2a8fa67f92367c102b1a0eea77c_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3efc60be1d9d2a8fa67f92367c102b1a0eea77c.jpeg 2x" data-dominant-color="2E4E61"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">6558c3bb-06aa-4791-bd9e-90a16f18fa25</span><span class="informations">1280×960 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75417081e092b0beccdf3833ee97ba4c0efac2db.jpeg" data-download-href="/uploads/short-url/gJi4bpIb1s6mgtZy8k878pkn1ZF.jpeg?dl=1" title="0bd915b3-d8b7-40c0-a662-9ede2057925c" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75417081e092b0beccdf3833ee97ba4c0efac2db_2_666x500.jpeg" alt="0bd915b3-d8b7-40c0-a662-9ede2057925c" data-base62-sha1="gJi4bpIb1s6mgtZy8k878pkn1ZF" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75417081e092b0beccdf3833ee97ba4c0efac2db_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75417081e092b0beccdf3833ee97ba4c0efac2db_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75417081e092b0beccdf3833ee97ba4c0efac2db.jpeg 2x" data-dominant-color="354E5D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0bd915b3-d8b7-40c0-a662-9ede2057925c</span><span class="informations">1280×960 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83468587158f30b512961be8481a8a109f3398bc.jpeg" data-download-href="/uploads/short-url/iJjDHRHMM1AMhufzRNIgERC15c8.jpeg?dl=1" title="f65c28c4-10dc-4d47-80bf-0091b461906d" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83468587158f30b512961be8481a8a109f3398bc_2_666x500.jpeg" alt="f65c28c4-10dc-4d47-80bf-0091b461906d" data-base62-sha1="iJjDHRHMM1AMhufzRNIgERC15c8" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83468587158f30b512961be8481a8a109f3398bc_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83468587158f30b512961be8481a8a109f3398bc_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83468587158f30b512961be8481a8a109f3398bc.jpeg 2x" data-dominant-color="384E5C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">f65c28c4-10dc-4d47-80bf-0091b461906d</span><span class="informations">1280×960 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8ab89dac0b61a491215f724953faccae5f16852.jpeg" data-download-href="/uploads/short-url/sDd0QlGhblLnd0fD4Xq7DIgo8Ke.jpeg?dl=1" title="7c0c3ca7-c135-4e02-989a-3e24933acd95" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8ab89dac0b61a491215f724953faccae5f16852_2_666x500.jpeg" alt="7c0c3ca7-c135-4e02-989a-3e24933acd95" data-base62-sha1="sDd0QlGhblLnd0fD4Xq7DIgo8Ke" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8ab89dac0b61a491215f724953faccae5f16852_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8ab89dac0b61a491215f724953faccae5f16852_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8ab89dac0b61a491215f724953faccae5f16852.jpeg 2x" data-dominant-color="394E5D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">7c0c3ca7-c135-4e02-989a-3e24933acd95</span><span class="informations">1280×960 236 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Some of the correponding states can be saved on a particular node (e.g. brightness and contrast on the displaynode of the current background scalar volume) so changes can be recognized if the observed node changes (by changeBrightness&amp;Contrast mouseMode). Another one like this would be zoom, the zoomFactor can be recovered from the fieldOfView of the sliceNode. <em>But other states (e.g. flipView) need to be saved on a parameterNode (or elsewhere) compulsorily because other logic functions need to access this info. And since I will need a parameterNode to control which of these (zoom, rotate, brightness&amp;contrast and flipView) toolbuttons is checked because they are exclusive (this is not easy to code on Qt). I was thinking on doing it this way.</em></p>
<p>Is this the correct way of implementing this functionality? Should I try to do more on Qt? Should I save all the states on the toolbar parameterNode?</p>
<p>Thanks</p>

---

## Post #2 by @jamesobutler (2021-11-19 22:57 UTC)

<p>You can put the various buttons into a QButtonGroup and set the state as exclusive so only one is selected at one time. Have you tried this already? We’re you having trouble using this?</p>
<p><a href="https://doc.qt.io/qt-5/qbuttongroup.html#exclusive-prop" class="onebox" target="_blank" rel="noopener nofollow ugc">https://doc.qt.io/qt-5/qbuttongroup.html#exclusive-prop</a></p>

---

## Post #3 by @mau_igna_06 (2021-11-19 23:16 UTC)

<p>The problem is that setting the exclusive option of the QButtonGroup: you have to obligatorily check one of the buttons and I want the possibility of not having any button checked.<br>
They are ways hackish ways (that I found online) to side-step this problem but I remember they were not-possible to implement on Slicer’s python</p>

---

## Post #4 by @lassoan (2021-11-20 14:19 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="20709">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>But other states (e.g. flipView) need to be saved on a parameterNode (or elsewhere) compulsorily because other logic</p>
</blockquote>
</aside>
<p>You don’t need custom attributes for slice view properties, such as flips or zoom. Each slice view has a default SliceToRas and a current SliceToRas transform. If you detect that the angle between default and current slice X is more than 90 degrees then it means that that view is horizontally flipped. It would be redundant to specify a parameter node for this. The same apply for all slip directions, zoom, etc - just compare various defaults to current values.</p>
<p>If your add some additional properties that you want to control using an application toolbar then it makes sense to adjust properties or attribute of a singleton node. If you specify some custom slice view properties that users can adjust with a per-slice toolbar then you can store them as attributes in each slice node.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="3" data-topic="20709">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>The problem is that setting the exclusive option of the QButtonGroup: you have to obligatorily check one of the buttons and I want the possibility of not having any button checked</p>
</blockquote>
</aside>
<p>I don’t remember ever having an issue with this. After you uncheck the only checked button in an exclusive button group and then all the buttons should be unchecked.</p>

---

## Post #5 by @cpinter (2021-11-30 10:15 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="3" data-topic="20709">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>The problem is that setting the exclusive option of the QButtonGroup: you have to obligatorily check one of the buttons and I want the possibility of not having any button checked</p>
</blockquote>
</aside>
<p>Try just using the <code>autoExclusive</code> property and put the buttons in their own layout.</p>

---
