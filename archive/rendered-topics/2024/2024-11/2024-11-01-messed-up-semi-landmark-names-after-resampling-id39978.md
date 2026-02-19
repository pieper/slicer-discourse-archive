---
topic_id: 39978
title: "Messed Up Semi Landmark Names After Resampling"
date: 2024-11-01
url: https://discourse.slicer.org/t/39978
---

# Messed up semi-landmark names after resampling

**Topic ID**: 39978
**Date**: 2024-11-01
**URL**: https://discourse.slicer.org/t/messed-up-semi-landmark-names-after-resampling/39978

---

## Post #1 by @Ruiqi-CUB (2024-11-01 11:07 UTC)

<p>Hi all, I have a few CT scannings of shells, and I have reconstructed 3D meshes in stl format. I would like to use semi-landmarks to capture some curves, the do a PCA in R with geomorph. My slicer version is 5.6.2.</p>
<p>I used Curve function under markups, after manually placing the semi-landmarks, I used Resample fuction to make them evenly distributed.</p>
<p>However, if the number of resampled points are not equal to the number of points that I manually placed, the name of those landmarks will be messed up: either missing names, or with combined names.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f847a65ff3e4894cfe76288c483db38fae31936.png" data-download-href="/uploads/short-url/ic4tfCYhLh6sIJZMSJWdYZQPnym.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f847a65ff3e4894cfe76288c483db38fae31936_2_639x500.png" alt="image" data-base62-sha1="ic4tfCYhLh6sIJZMSJWdYZQPnym" width="639" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f847a65ff3e4894cfe76288c483db38fae31936_2_639x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f847a65ff3e4894cfe76288c483db38fae31936.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f847a65ff3e4894cfe76288c483db38fae31936.png 2x" data-dominant-color="E9E9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">641×501 55.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f12aee82b6e06ff9f7661db753b4bbf2c17a1453.png" data-download-href="/uploads/short-url/ypt3amsrnhRX8zBiJ0koRPDzDDd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f12aee82b6e06ff9f7661db753b4bbf2c17a1453_2_556x500.png" alt="image" data-base62-sha1="ypt3amsrnhRX8zBiJ0koRPDzDDd" width="556" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f12aee82b6e06ff9f7661db753b4bbf2c17a1453_2_556x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f12aee82b6e06ff9f7661db753b4bbf2c17a1453.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f12aee82b6e06ff9f7661db753b4bbf2c17a1453.png 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">626×562 52.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My question is: do the individual semi-landmark names matter in the subsequent analyses? There will be more than one curves, and I think it would be nice to keep names consistent across specimens. Is there a way to fix this?</p>

---

## Post #2 by @muratmaga (2024-11-01 18:45 UTC)

<aside class="quote no-group" data-username="Ruiqi-CUB" data-post="1" data-topic="39978">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/b38774/48.png" class="avatar"> Ruiqi-CUB:</div>
<blockquote>
<p>My question is: do the individual semi-landmark names matter in the subsequent analyses?</p>
</blockquote>
</aside>
<p>No, not for SlicerMorph, nor any package I know of. However, the number and sequence of landmarks matter. You need to have exactly the same number of points on your samples, recorded exactly in the same way. So if you go point 1-2-3, but po 3-1-2 in another sample, results will be incorrect.</p>

---

## Post #3 by @Ruiqi-CUB (2024-11-07 18:13 UTC)

<p>Sounds good! Glad to know that I don’t need manually rename all the semi-landmarks.</p>
<p>But it would be great if you could automatically update the names of semilandmarks after resampling.</p>

---

## Post #4 by @muratmaga (2024-11-07 18:27 UTC)

<p>You can write a couple lines of python code to do that. See example of how to get control point properties:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-to-markups-point-list-properties" rel="noopener nofollow ugc">Just make sure that the</a></p>

---
