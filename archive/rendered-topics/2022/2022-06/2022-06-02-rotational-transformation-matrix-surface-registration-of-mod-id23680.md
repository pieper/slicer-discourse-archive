---
topic_id: 23680
title: "Rotational Transformation Matrix Surface Registration Of Mod"
date: 2022-06-02
url: https://discourse.slicer.org/t/23680
---

# Rotational transformation matrix & surface registration of models

**Topic ID**: 23680
**Date**: 2022-06-02
**URL**: https://discourse.slicer.org/t/rotational-transformation-matrix-surface-registration-of-models/23680

---

## Post #1 by @mdhan (2022-06-02 04:10 UTC)

<p>Hello,</p>
<p>Sorry for troubling you all, but I’d be grateful if you could kindly help with me with something I’m struggling with. I’ve been having trouble utilizing the rotational transformation matrix to suit my needs, and wanted to make sure I was interpreting things correctly.</p>
<p>What I am interested in knowing is the rotational transformation matrix in degrees, and I have been using an online calculator (<a href="https://www.andre-gaschler.com/rotationconverter/" rel="noopener nofollow ugc">3D Rotation Converter</a>) to convert the 3x3 part of Slicer’s 4x4 matrix.</p>
<p>As a test, I created a cube on Meshmixer, and duplicated it. Then, I rotated the duplicate 11.1, 22.2, 33.3 degrees in the x, y, and z axes, respectively. After exporting these 2 surfaces, I then used the Slicer CMF registration and got the transformation matrix in the 4x4 matrix format.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b1167b3e8029b8f45fb07a60bebcc9eb1e2df53.jpeg" data-download-href="/uploads/short-url/cZCJSIH7g8npqjDZEJgp7x309R9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b1167b3e8029b8f45fb07a60bebcc9eb1e2df53_2_638x500.jpeg" alt="image" data-base62-sha1="cZCJSIH7g8npqjDZEJgp7x309R9" width="638" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b1167b3e8029b8f45fb07a60bebcc9eb1e2df53_2_638x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b1167b3e8029b8f45fb07a60bebcc9eb1e2df53_2_957x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b1167b3e8029b8f45fb07a60bebcc9eb1e2df53_2_1276x1000.jpeg 2x" data-dominant-color="252722"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1436×1125 91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d93896fa83267449c862870e8e50773eaf32484.png" data-download-href="/uploads/short-url/4dDWsxjN6XmsDudc8r7lxLtrZ76.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d93896fa83267449c862870e8e50773eaf32484_2_683x500.png" alt="image" data-base62-sha1="4dDWsxjN6XmsDudc8r7lxLtrZ76" width="683" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d93896fa83267449c862870e8e50773eaf32484_2_683x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d93896fa83267449c862870e8e50773eaf32484.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d93896fa83267449c862870e8e50773eaf32484.png 2x" data-dominant-color="A88A8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">808×591 57.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d55047a37ff516b14cd3fe61aa6d57672fb2f24.jpeg" alt="MATRIX" data-base62-sha1="8Kzh2rysVhUggRJgM8c330JS96I" width="483" height="137"></p>
<p>However, when I tried to convert the 3x3 matrix to angles, all of the numbers seemed quite off from the 11.1, 22.2, 33.3 degrees. Even when accounting for possible registration errors, the discrepancies seem quite severe (plus on visual inspection the registration seems accurate).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81437bdcd1847c31bfe9094d3537c1065ddee799.jpeg" data-download-href="/uploads/short-url/irwaYWta5KXV67vRySIFG2uI7Ox.jpeg?dl=1" title="OUTPUT" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81437bdcd1847c31bfe9094d3537c1065ddee799_2_690x283.jpeg" alt="OUTPUT" data-base62-sha1="irwaYWta5KXV67vRySIFG2uI7Ox" width="690" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81437bdcd1847c31bfe9094d3537c1065ddee799_2_690x283.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81437bdcd1847c31bfe9094d3537c1065ddee799_2_1035x424.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81437bdcd1847c31bfe9094d3537c1065ddee799.jpeg 2x" data-dominant-color="EEEEF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">OUTPUT</span><span class="informations">1329×547 88.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would again be grateful for everyone’s wisdom on this!!</p>

---

## Post #2 by @mau_igna_06 (2022-06-02 16:46 UTC)

<p>If you can build Slicer, you could test my Dynamicmodeler Tool: transformMaker<br>
It let’s you compose any number of angles, convert them in transforms and it will return the resulting rotation matrix angle</p>
<p>See more info here:</p><aside class="quote quote-modified" data-post="8" data-topic="23626">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/dynamicmodeler-transform-maker/23626/8">DynamicModeler Transform Maker</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    Hi Andras. 
I’ll take time to give a full answer on the afternoon but here you have a preview video: 
 
    
   
And here is the branch, thanks for testing: 

Please don’t be confused by the name of the branch, the idea of the transform maker came while I was developing the AddGeometries tool so it’s on this branch 
Best regards, 
Mauro
  </blockquote>
</aside>


---

## Post #3 by @mikebind (2022-06-02 20:21 UTC)

<p>You might also find this module helpful:  <a href="https://github.com/mikebind/SlicerCharacterizeTransformMatrix" class="inline-onebox">GitHub - mikebind/SlicerCharacterizeTransformMatrix</a></p>
<p>Could your issue be that there are multiple ways to decompose a net rotation into series of rotations?</p>

---

## Post #4 by @mdhan (2022-06-13 03:08 UTC)

<p>Thank you very much mau_igna_06 and mikebind, it’s incredibly helpful and I’m now able to do what I wanted thanks to you! Hope one day I’d be able to contribute to the community like you folks!</p>

---

## Post #5 by @lassoan (2022-06-13 13:43 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="3" data-topic="23680">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>You might also find this module helpful: <a href="https://github.com/mikebind/SlicerCharacterizeTransformMatrix">GitHub - mikebind/SlicerCharacterizeTransformMatrix </a></p>
</blockquote>
</aside>
<p><a class="mention" href="/u/mikebind">@mikebind</a> Would you consider adding this module to the <a href="https://github.com/PerkLab/SlicerSandbox">Sandbox extension</a>? We maintain this extension to make it easier for users to install small, experimental modules (few clicks instead of downloading and extracting a zip package, setting additional module paths, etc.).</p>

---

## Post #6 by @mikebind (2022-06-13 22:09 UTC)

<p>Yes, I’ll work on that.  I have already forked the Sandbox repo to work on adding the DICOM stitching module but got bogged down trying to improve it and add some tests, so had not finished that process yet.  This transformation matrix module is very simple and I think will not really require much modification, so it should be quicker to add when I get a chance.  I’ll try to get to that soon.</p>

---
