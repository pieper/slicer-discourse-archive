# Mirror the 3D view

**Topic ID**: 20909
**Date**: 2021-12-04
**URL**: https://discourse.slicer.org/t/mirror-the-3d-view/20909

---

## Post #1 by @mau_igna_06 (2021-12-04 12:06 UTC)

<p>Hi devs.</p>
<p>In my application the user may input CTs with mismatched directions. The user can solve this by turning on mirroring (or may be he wants mirroring for another valid reason).<br>
I have already set up mirroring on sliceViews and it works well. I was trying to mirror the 3D view but I cannot find another way that is not applying a transform to the CT. The disadvantage of this method is that I have other planning models that would need the same transform applied to them. That transform should be applied through out the whole software to all objects in the scene. That would increase the complexity of the code unnecessary if there is another way.</p>
<p>Can this be done in other way?</p>

---

## Post #2 by @pieper (2021-12-04 16:52 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="20909">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>In my application the user may input CTs with mismatched directions.</p>
</blockquote>
</aside>
<p>I’m not sure exactly what you mean here, but fixing the data sounds like a much better solution than trying to support mirrored data through the whole app.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="20909">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>or may be he wants mirroring for another valid reason</p>
</blockquote>
</aside>
<p>Can you give examples?</p>

---

## Post #3 by @mau_igna_06 (2021-12-04 17:32 UTC)

<p>I’m not really sure why me client asked me for this. I’ll ask him.</p>
<p>But one reason could be that he sent me a cadaver CT that was taken on prone position and the radiologist didn’t know how to fix it and he wanted to use it in the software anyway. And it is hard for him to mirror the CT like you and I would do on Slicer normally using the transforms module.</p>
<p>Another reason would be that I have seen software of the competence that has this feature.</p>

---

## Post #4 by @mau_igna_06 (2021-12-04 18:41 UTC)

<p>Here is a video of what we’d like to achieve:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b4cc057f3c70d5f1077654f64c47b0675487aec.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b4cc057f3c70d5f1077654f64c47b0675487aec.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b4cc057f3c70d5f1077654f64c47b0675487aec.mp4</a>
    </source></video>
  </div><p></p>
<p>There are flipHorizontal and flipVertical 3D-view buttons. In this example they are clicked twice fastly.</p>

---

## Post #5 by @pieper (2021-12-04 21:05 UTC)

<p>Flipping the data left/right on a surgery guidance system sounds just wrong and dangerous to me.  Please try to work with them to get the data correct with respect to patient coordinates and only implement flipping if you completely understand why it is an okay operation.</p>

---

## Post #6 by @mau_igna_06 (2021-12-04 22:01 UTC)

<p>Thank you for your concern Steve. You have a really valid point. I haven’t realized about this risk.<br>
I’ll ask my client if he understands the potencial missuse of the software this feature would allow.<br>
I think he asked me for development of a lot of these toolbar features like zoom, rotate, flip just because he saw it on software of big companies</p>

---

## Post #7 by @drvarunagarwal (2021-12-05 17:17 UTC)

<p>Hi,</p>
<p>This is a valid concern.<br>
however situation is mostly the opposite.</p>
<p>What if you are all prepped up for surgery and during surgery one finds that the sides in the IGS system is flipped with respect to the patient and there is no way to correct this</p>
<p>then the surgeon will be in trouble</p>

---
