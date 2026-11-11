---
topic_id: 48810
title: "Transform applied to multiple volumes misbehaves when edited"
date: 2026-11-09
url: https://discourse.slicer.org/t/48810
last_bumped: 2026-11-11T09:38:47.628Z
---

# Transform applied to multiple volumes misbehaves when edited

**Topic ID**: 48810
**Date**: 2026-11-09
**URL**: https://discourse.slicer.org/t/transform-applied-to-multiple-volumes-misbehaves-when-edited/48810

---

## Post #1 by @shai-ikko (2026-11-09 15:38 UTC)

<p>When a transform is applied to more than one volume, and you then go to the Transforms module and edit it, weird things happen. When switching the presentation between the views, the transform (as applied to the volumes) changes (without changing in the module).</p>
<p>I did the following actions:</p>
<ul>
<li>
<p>Open Slicer 5.12.4</p>
</li>
<li>
<p>Open the “Sample Data” module</p>
</li>
<li>
<p>Click “MRHead” and “MRBrainTumor1”. MRBrainTumor1 is presented in the slices.</p>
</li>
<li>
<p>Go To “Data” module</p>
</li>
<li>
<p>Right click on the right side of MRHead (the transform context menu), and pick “create new transform”</p>
</li>
<li>
<p>Move to the “Transform Hierarchy” tab, and drag MRBrainTumor1 under the transform</p>
</li>
<li>
<p>Go to the “Transforms” module. Using the “Rotation” scrollbar “IS”, rotate by 45°. The MRBrainTumor1 volume is rotated as expected.</p>
</li>
<li>
<p>Go back to the “Data” module. Click the MRHead eye to make it visible. Result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69fa1975d8d34eea51b3e7bb5f335bcf99a75618.jpeg" data-download-href="/uploads/short-url/f7vY8HQlgGCMJ9FyjnOzXTorJXi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69fa1975d8d34eea51b3e7bb5f335bcf99a75618_2_690x339.jpeg" alt="image" data-base62-sha1="f7vY8HQlgGCMJ9FyjnOzXTorJXi" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69fa1975d8d34eea51b3e7bb5f335bcf99a75618_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69fa1975d8d34eea51b3e7bb5f335bcf99a75618_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69fa1975d8d34eea51b3e7bb5f335bcf99a75618_2_1380x678.jpeg 2x" data-dominant-color="9FA0AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1545×761 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Going back to the Transforms module, it still shows the 45°:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eee8a8a58f770cc2ac76e7e291b7eefc3039a5b6.jpeg" data-download-href="/uploads/short-url/y5u6DFZDqceuzAV1Khl84tIp6WW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eee8a8a58f770cc2ac76e7e291b7eefc3039a5b6_2_690x339.jpeg" alt="image" data-base62-sha1="y5u6DFZDqceuzAV1Khl84tIp6WW" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eee8a8a58f770cc2ac76e7e291b7eefc3039a5b6_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eee8a8a58f770cc2ac76e7e291b7eefc3039a5b6_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eee8a8a58f770cc2ac76e7e291b7eefc3039a5b6_2_1380x678.jpeg 2x" data-dominant-color="A2A3B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1545×761 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Now, clicking “Identity” to reset the transform:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d3ddd6d7fdee80bb1d9689f7c6f1ca33f25ac48.jpeg" data-download-href="/uploads/short-url/8JLFAlxg1EMvyY1JEM63xrZCkoE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d3ddd6d7fdee80bb1d9689f7c6f1ca33f25ac48_2_690x339.jpeg" alt="image" data-base62-sha1="8JLFAlxg1EMvyY1JEM63xrZCkoE" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d3ddd6d7fdee80bb1d9689f7c6f1ca33f25ac48_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d3ddd6d7fdee80bb1d9689f7c6f1ca33f25ac48_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d3ddd6d7fdee80bb1d9689f7c6f1ca33f25ac48_2_1380x678.jpeg 2x" data-dominant-color="A2A3B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1545×761 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>And finally, “compare volumes”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff789e88a96bbd82ea72b79658b89545256606d9.jpeg" data-download-href="/uploads/short-url/As0bc5Bx6POfZBKomko2is2zr5L.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff789e88a96bbd82ea72b79658b89545256606d9_2_690x339.jpeg" alt="image" data-base62-sha1="As0bc5Bx6POfZBKomko2is2zr5L" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff789e88a96bbd82ea72b79658b89545256606d9_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff789e88a96bbd82ea72b79658b89545256606d9_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff789e88a96bbd82ea72b79658b89545256606d9_2_1380x678.jpeg 2x" data-dominant-color="878887"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1545×761 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ul>
<p>If you now return to the “conventional” view, you get the head in 45° again.</p>
<p>This last move seems to imply that the problem is mostly in the slice views, but that does not make it “just presentation” or “cosmetic”, because the transform is edited based on this presentation – leading to wrong transformation matrices being selected.</p>

---

## Post #2 by @mikebind (2026-11-10 04:17 UTC)

<p>Thanks for the clear steps to try, that’s very helpful for troubleshooting. I tried to reproduce the issue following your steps exactly and did not see any problems in Slicer 5.10 (I haven’t upgraded yet to 5.12.4).  In your first and second screenshots, it appears that the heads are rotated 90 degrees rather than 45 degrees. Is it possible you had generated two 45 degree transforms and only reset one of them to identity? That doesn’t explain your final screenshot, but the images also don’t seem to match your description of the incorrect behavior.</p>

---

## Post #3 by @shai-ikko (2026-11-11 09:38 UTC)

<p>Thanks for taking the time to check this.</p>
<aside class="quote no-group" data-username="mikebind" data-post="2" data-topic="48810">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>In your first and second screenshots, it appears that the heads are rotated 90 degrees rather than 45 degrees. Is it possible you had generated two 45 degree transforms and only reset one of them to identity?</p>
</blockquote>
</aside>
<p>No – I had started a fresh Slicer session to make sure that the steps are exactly as I described them.</p>
<aside class="quote no-group" data-username="mikebind" data-post="2" data-topic="48810">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>the images also don’t seem to match your description of the incorrect behavior.</p>
</blockquote>
</aside>
<p>Where do you see a mismatch between my description and my images? In case that’s the issue – in the second image, I’m well aware that the head is rotated ~90°; when I say “it still shows 45°”, I’m referring to the transform as it is shown in the Transforms module.</p>
<p>And finally,</p>
<aside class="quote no-group" data-username="mikebind" data-post="2" data-topic="48810">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I tried to reproduce the issue following your steps exactly and did not see any problems in Slicer 5.10</p>
</blockquote>
</aside>
<p>I did the reproduction in 5.12.4 because it is the latest released version, and also because I have an installation that is clean of extensions and other distractions – but we’ve seen similar behavior on 5.10 and 5.8.</p>
<p>We are producing a set of volumes in a non-standard format, which represent different measurements (analogous to T1 and T2 in an MRI), and we have an extension to load them into Slicer and tie them together to a transform so they can be manipulated together. That is the context where we first encountered the issue, so naturally the first thought was that the connection is somehow messed up; but the reproduction in a clean environment convinced us otherwise.</p>
<p>I wanted to attach the session log, to give more details, and then realized the installation I had used wasn’t as clean as I thought – it didn’t have our extensions, but it did have MarkupToModel and SegmentEditorExtraEffects. So I uninstalled them, and tried again, this time rotating by 30 degrees instead of 45. The misbehavior was slightly different – the transform was just “reverted” when going back to the first volume (the transform itself wasn’t changed, as you can see below, it was just visually “unapplied”).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/893efcb14e171f77dc7ae82c6f23e65e4c3259ff.jpeg" data-download-href="/uploads/short-url/jA8mu1pSkx13ds2hkgyywj82vuL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/893efcb14e171f77dc7ae82c6f23e65e4c3259ff_2_690x289.jpeg" alt="image" data-base62-sha1="jA8mu1pSkx13ds2hkgyywj82vuL" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/893efcb14e171f77dc7ae82c6f23e65e4c3259ff_2_690x289.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/893efcb14e171f77dc7ae82c6f23e65e4c3259ff_2_1035x433.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/893efcb14e171f77dc7ae82c6f23e65e4c3259ff_2_1380x578.jpeg 2x" data-dominant-color="9999AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1542×646 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4b9586e881d49a91c9d7645381acdf743f05531.jpeg" data-download-href="/uploads/short-url/s4iGt2B20UaXODOH5Q4SFjrONqx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4b9586e881d49a91c9d7645381acdf743f05531_2_690x289.jpeg" alt="image" data-base62-sha1="s4iGt2B20UaXODOH5Q4SFjrONqx" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4b9586e881d49a91c9d7645381acdf743f05531_2_690x289.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4b9586e881d49a91c9d7645381acdf743f05531_2_1035x433.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4b9586e881d49a91c9d7645381acdf743f05531_2_1380x578.jpeg 2x" data-dominant-color="9697A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1542×646 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec4a3e48331a4a93e2d3233911938e80d4a94815.jpeg" data-download-href="/uploads/short-url/xIjKpnUgLNj0TcsiuVMtEL93Ful.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec4a3e48331a4a93e2d3233911938e80d4a94815_2_690x271.jpeg" alt="image" data-base62-sha1="xIjKpnUgLNj0TcsiuVMtEL93Ful" width="690" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec4a3e48331a4a93e2d3233911938e80d4a94815_2_690x271.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec4a3e48331a4a93e2d3233911938e80d4a94815_2_1035x406.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec4a3e48331a4a93e2d3233911938e80d4a94815_2_1380x542.jpeg 2x" data-dominant-color="9495A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1543×607 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Adding here images to verify the hierarchy situation:</p>
<ol>
<li>Clicking the transform in Data to show that it is still applied to the two volumes (and that it is the only one)</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a38edfb8bac014aef46e070769d942e4b58e5b3e.jpeg" data-download-href="/uploads/short-url/nkTVSRVtzmAMEMhtf04BF5E3WnY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a38edfb8bac014aef46e070769d942e4b58e5b3e_2_690x271.jpeg" alt="image" data-base62-sha1="nkTVSRVtzmAMEMhtf04BF5E3WnY" width="690" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a38edfb8bac014aef46e070769d942e4b58e5b3e_2_690x271.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a38edfb8bac014aef46e070769d942e4b58e5b3e_2_1035x406.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a38edfb8bac014aef46e070769d942e4b58e5b3e_2_1380x542.jpeg 2x" data-dominant-color="9093A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1544×607 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>Going to the Transforms module to show that it still has the 30-degree-rotation matrix</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75caa4061af7d371cd807e949e5006a217443f4b.jpeg" data-download-href="/uploads/short-url/gO21e1RyQz9irSYo15EcL9x4bDt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75caa4061af7d371cd807e949e5006a217443f4b_2_690x271.jpeg" alt="image" data-base62-sha1="gO21e1RyQz9irSYo15EcL9x4bDt" width="690" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75caa4061af7d371cd807e949e5006a217443f4b_2_690x271.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75caa4061af7d371cd807e949e5006a217443f4b_2_1035x406.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75caa4061af7d371cd807e949e5006a217443f4b_2_1380x542.jpeg 2x" data-dominant-color="9192A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1544×607 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It also became visually unapplied in the other volume, when changing using the eyes in Data</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac4b929b8b436d4590e0cce64d4d9864c0885676.jpeg" data-download-href="/uploads/short-url/oAc2ozonXsmwokzLOPZ8jb5bIqy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac4b929b8b436d4590e0cce64d4d9864c0885676_2_690x271.jpeg" alt="image" data-base62-sha1="oAc2ozonXsmwokzLOPZ8jb5bIqy" width="690" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac4b929b8b436d4590e0cce64d4d9864c0885676_2_690x271.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac4b929b8b436d4590e0cce64d4d9864c0885676_2_1035x406.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac4b929b8b436d4590e0cce64d4d9864c0885676_2_1380x542.jpeg 2x" data-dominant-color="8C8F9F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1544×607 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And again, “compare volumes” (opening new slice views) shows things as they should be</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1a532fa57ebbe34826b4c4039974ffeb7f2603b.jpeg" data-download-href="/uploads/short-url/plwrSWMAlP07Ohvq0JXbed2hm7V.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1a532fa57ebbe34826b4c4039974ffeb7f2603b_2_690x271.jpeg" alt="image" data-base62-sha1="plwrSWMAlP07Ohvq0JXbed2hm7V" width="690" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1a532fa57ebbe34826b4c4039974ffeb7f2603b_2_690x271.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1a532fa57ebbe34826b4c4039974ffeb7f2603b_2_1035x406.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1a532fa57ebbe34826b4c4039974ffeb7f2603b_2_1380x542.jpeg 2x" data-dominant-color="636361"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1544×607 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Full session log:</p>
<pre><code class="lang-auto">Python 3.12.10 (main, Sep  9 2026, 18:32:48) [GCC 14.2.1 20250110 (Red Hat 14.2.1-7)] on linux
&gt;&gt;&gt; 
[Qt] Session start time .......: 20261111_112054
[Qt] Slicer version ...........: 5.12.4 (revision 34645 / 4e21c19) linux-amd64 - installed release
[Qt] Operating system .........: Linux / 6.8.0-1064-nvidia / #67~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep 17 21:53:31 UTC 2 / UTF-8 - 64-bit
[Qt] Memory ...................: 63717 MB physical, 64911 MB virtual
[Qt] CPU ......................: AuthenticAMD AMD Ryzen 7 5800H with Radeon Graphics, 8 cores, 16 logical processors
[Qt] VTK configuration ........: OpenGL2 rendering, TBB threading
[Qt] Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)
[Qt] DCMTK configuration ......: version 3.7.0, no SSL
[Qt] Internationalization .....: disabled, language=
[Qt] Developer mode ...........: enabled
[Qt] Application path .........: /home/shai/Programs/Slicer/Slicer-5.12.4-linux-amd64/bin
[Qt] Additional module paths ..: (none)
[Python] Scripted subject hierarchy plugin registered: SegmentEditor
[Python] Scripted subject hierarchy plugin registered: SegmentStatistics
[Qt] Switch to module:  "Welcome"
[Qt] Switch to module:  "SampleData"
[Python] Verifying checksum
[Python] File already exists and checksum is OK - reusing it.
[Python] Requesting load MRHead from /home/shai/.cache/slicer.org/Slicer/SlicerIO/MR-head.nrrd ...
[Qt] "Volume" Reader has successfully read the file "/home/shai/.cache/slicer.org/Slicer/SlicerIO/MR-head.nrrd" "[0.12s]"
[Python] Load finished
[Python] Verifying checksum
[Python] File already exists and checksum is OK - reusing it.
[Python] Requesting load MRBrainTumor1 from /home/shai/.cache/slicer.org/Slicer/SlicerIO/RegLib_C01_1.nrrd ...
[Qt] "Volume" Reader has successfully read the file "/home/shai/.cache/slicer.org/Slicer/SlicerIO/RegLib_C01_1.nrrd" "[0.08s]"
[Python] Load finished
[Qt] Switch to module:  "Data"
[Qt] Switch to module:  "Transforms"
[Qt] Switch to module:  "Data"
[Qt] Switch to module:  "Transforms"
[Qt] Switch to module:  "Data"
[Qt] Switch to module:  "CompareVolumes"

</code></pre>

---
