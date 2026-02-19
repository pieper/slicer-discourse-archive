---
topic_id: 4206
title: "Ply File Colors Not Displayed"
date: 2018-09-27
url: https://discourse.slicer.org/t/4206
---

# PLY file colors not displayed

**Topic ID**: 4206
**Date**: 2018-09-27
**URL**: https://discourse.slicer.org/t/ply-file-colors-not-displayed/4206

---

## Post #1 by @Niels (2018-09-27 10:24 UTC)

<p>I have an exported ply file that contains color information that I would like to see and be able to access from python. If I load the file I see the model but I do not see the color. I looked at the header of the file and by the looks of it the color is given per vertex. Is color supported?</p>
<p>[START PLY HEADER]<br>
ply<br>
format binary_little_endian 1.0<br>
comment Exported model<br>
element vertex 238415<br>
property float x<br>
property float y<br>
property float z<br>
property float nx<br>
property float ny<br>
property float nz<br>
property uchar red<br>
property uchar green<br>
property uchar blue<br>
element face 473991<br>
property list uchar int vertex_indices<br>
end_header<br>
[END PLY HEADER]</p>

---

## Post #2 by @Niels (2018-09-27 12:20 UTC)

<p>After reading this: <a href="https://discourse.slicer.org/t/displaying-textured-3d-models/2521/9">https://discourse.slicer.org/t/displaying-textured-3d-models/2521/9</a></p>
<p>I think colors per vertex are supported, I tried the Models module and enabled the scalars. I have set it to RGB and can select a colormap, but I get strange colors. do I need a colormap to get the colors from the model to display?</p>

---

## Post #3 by @lassoan (2018-09-27 12:33 UTC)

<p>Both vertex and cell scalars can be used for coloring. There were some fixes in color table mapping a 1-2 months ago, so make sure you use a recent nightly version.</p>

---

## Post #4 by @Niels (2018-09-28 14:58 UTC)

<p>Hi Andras, I just tried the nightly build version 4.9.0-2018-09-27 with no luck. Also here no colors (at least not the colors from the file )<br>
STR:</p>
<ul>
<li>I load the ply (it shows in gray)</li>
<li>I open the Models module</li>
<li>select the scalars tab</li>
<li>set the checkbox to: visible</li>
<li>select active scalar: rgb</li>
</ul>
<p>I can play with the colortable to get some colors, but those are not the colors from the file. In MeshLab the colors seem to work fine, so the file is correct.</p>

---

## Post #5 by @Niels (2018-09-28 16:03 UTC)

<p>Update: I got some color of the original colors to display when I tried flipping the rgb values in the data. Not sure how it suddenly happened and I am unable to reproduce it now. Can anybody confirm that vertex colors work with the nightly build?</p>

---

## Post #6 by @lassoan (2018-10-01 00:02 UTC)

<p>We usually use single-component scalars + a lookup-table for coloring, as it is much more flexible than burnt-in RGB values (you can threshold, recolor, etc. dynamically) . For displaying an arbitrarily textured model, we typically use .obj file format, because this is how we usually get these models.</p>
<p>Per-verted colored .ply files are not very common, but might be useful to display them directly, so I’ve added a new option “Direct color mapping” to colors module / display / scalars section. You can use this option to use per-vertex 3-component scalar values directly as RGB values (without mapping it through a lookup table). This feature will be available in Slicer nightly version that you download tomorrow or later.</p>

---

## Post #7 by @Niels (2018-10-02 07:09 UTC)

<p>Hi Andras, Thanks for your explanation. I tested the “direct color mapping” feature you added in the nightly build and I would like to confirm that it works perfectly. Thanks for adding the feature on such short notice.</p>

---

## Post #8 by @manjula (2024-08-22 06:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="4206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>ve added a new option “Direct color m</p>
</blockquote>
</aside>
<p>Dear Prof Andras</p>
<p>I am having trouble in displaying colours from IOS scans exported as ply or obj.  The export files works well in exocad viewer or similar softwares but in 3D Slicer i cannot reproduce the colour.  What needs to be done ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa4f5b8ba6a81df61870bc70e6535a46b268a88f.png" data-download-href="/uploads/short-url/oiDbXjqsPSZiZ3sBCojxMyFUd9t.png?dl=1" title="Screenshot 2024-08-22 115655" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa4f5b8ba6a81df61870bc70e6535a46b268a88f_2_690x431.png" alt="Screenshot 2024-08-22 115655" data-base62-sha1="oiDbXjqsPSZiZ3sBCojxMyFUd9t" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa4f5b8ba6a81df61870bc70e6535a46b268a88f_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa4f5b8ba6a81df61870bc70e6535a46b268a88f_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa4f5b8ba6a81df61870bc70e6535a46b268a88f_2_1380x862.png 2x" data-dominant-color="B9C0D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-08-22 115655</span><span class="informations">1919×1199 432 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1df09b31225a9dc4d424af36305e153610fa8de7.jpeg" data-download-href="/uploads/short-url/4gRlgPDrghFeI2sHfbYDSB37rxB.jpeg?dl=1" title="Screenshot 2024-08-22 115731" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1df09b31225a9dc4d424af36305e153610fa8de7_2_595x500.jpeg" alt="Screenshot 2024-08-22 115731" data-base62-sha1="4gRlgPDrghFeI2sHfbYDSB37rxB" width="595" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1df09b31225a9dc4d424af36305e153610fa8de7_2_595x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1df09b31225a9dc4d424af36305e153610fa8de7_2_892x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1df09b31225a9dc4d424af36305e153610fa8de7_2_1190x1000.jpeg 2x" data-dominant-color="534269"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-08-22 115731</span><span class="informations">1281×1075 77.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>thank you</p>

---

## Post #9 by @pieper (2024-08-22 12:16 UTC)

<p>This can probably be fixed if you share some sample datasets.</p>

---

## Post #10 by @manjula (2024-08-22 17:06 UTC)

<p>Dear Steve</p>
<p>Please find the ply and the obj file formats of the same scan from a Intra oral scanner.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1G3dSSzqrY1jPlVURahYv7ro4kpEWZ7f3%2Fview%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1G3dSSzqrY1jPlVURahYv7ro4kpEWZ7f3%2Fview%3Fusp%3Ddrive_link&amp;ifkv=Ab5oB3qQY6oU47LhCJTZQQPHl_2cSmclL_qQe8ZXAjXe78Bgn2j0l-U6VpV5iiF6ZUHcxMXuSdWD4Q&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-802000182%3A1724346319818695&amp;ddm=0">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1G3dSSzqrY1jPlVURahYv7ro4kpEWZ7f3%2Fview%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1G3dSSzqrY1jPlVURahYv7ro4kpEWZ7f3%2Fview%3Fusp%3Ddrive_link&amp;ifkv=Ab5oB3qQY6oU47LhCJTZQQPHl_2cSmclL_qQe8ZXAjXe78Bgn2j0l-U6VpV5iiF6ZUHcxMXuSdWD4Q&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-802000182%3A1724346319818695&amp;ddm=0" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1G3dSSzqrY1jPlVURahYv7ro4kpEWZ7f3%2Fview%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1G3dSSzqrY1jPlVURahYv7ro4kpEWZ7f3%2Fview%3Fusp%3Ddrive_link&amp;ifkv=Ab5oB3qQY6oU47LhCJTZQQPHl_2cSmclL_qQe8ZXAjXe78Bgn2j0l-U6VpV5iiF6ZUHcxMXuSdWD4Q&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-802000182%3A1724346319818695&amp;ddm=0" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1DLR1nahQkwX_LdVLiv9nVyiTi7aRDBKE%2Fview%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1DLR1nahQkwX_LdVLiv9nVyiTi7aRDBKE%2Fview%3Fusp%3Ddrive_link&amp;ifkv=Ab5oB3ptWyHybIF2A08GZxPk04F2CUn01jp4Wzs2AapMjnxSUkaMNaQeSTucYtAlj7bWO4zjcwph&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-1120258562%3A1724346328151081&amp;ddm=0">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1DLR1nahQkwX_LdVLiv9nVyiTi7aRDBKE%2Fview%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1DLR1nahQkwX_LdVLiv9nVyiTi7aRDBKE%2Fview%3Fusp%3Ddrive_link&amp;ifkv=Ab5oB3ptWyHybIF2A08GZxPk04F2CUn01jp4Wzs2AapMjnxSUkaMNaQeSTucYtAlj7bWO4zjcwph&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-1120258562%3A1724346328151081&amp;ddm=0" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1DLR1nahQkwX_LdVLiv9nVyiTi7aRDBKE%2Fview%3Fusp%3Ddrive_link&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1DLR1nahQkwX_LdVLiv9nVyiTi7aRDBKE%2Fview%3Fusp%3Ddrive_link&amp;ifkv=Ab5oB3ptWyHybIF2A08GZxPk04F2CUn01jp4Wzs2AapMjnxSUkaMNaQeSTucYtAlj7bWO4zjcwph&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-1120258562%3A1724346328151081&amp;ddm=0" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>thank you for your time and effort.</p>

---

## Post #11 by @muratmaga (2024-08-22 17:35 UTC)

<aside class="quote no-group" data-username="manjula" data-post="8" data-topic="4206">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>cannot reproduce the colour</p>
</blockquote>
</aside>
<p>I don’t think you need the Normals as Active scalars. What else do you have in that drop down?</p>

---

## Post #12 by @manjula (2024-08-22 18:04 UTC)

<p>i tried all available options and combinations but didnt work.</p>

---

## Post #13 by @pieper (2024-08-22 20:42 UTC)

<p>I loaded the ply file in my local build and this is what I got with no changes needed in the models module.  It looks right to me.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ee1ee4d911230ac80cad19c10b8848e6771cc73.jpeg" data-download-href="/uploads/short-url/dxmW5mZbJT1mLT91zuoX6WnmZB9.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ee1ee4d911230ac80cad19c10b8848e6771cc73_2_690x313.jpeg" alt="image" data-base62-sha1="dxmW5mZbJT1mLT91zuoX6WnmZB9" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ee1ee4d911230ac80cad19c10b8848e6771cc73_2_690x313.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ee1ee4d911230ac80cad19c10b8848e6771cc73_2_1035x469.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ee1ee4d911230ac80cad19c10b8848e6771cc73.jpeg 2x" data-dominant-color="94798A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1066×485 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @manjula (2024-08-23 01:45 UTC)

<p>ohh this looks great . but i dont see get this. i will share my version details as well as try the newest version and see</p>

---

## Post #15 by @manjula (2024-08-27 18:32 UTC)

<p>Dear Steve,</p>
<p>I tried with my 3D Slicer windows and Linux versions 5.7.0 2024.05.30 and ,latest windows version 2024.08.27 and unfortunately for me the no colours are shown .</p>
<p>What could be the issue ?</p>
<p>thank you</p>

---

## Post #16 by @muratmaga (2024-08-27 18:38 UTC)

<p>It works fine with the preview and stable versions on my Mac. Maybe you have some initialization scripts (.slicerrc.py) or other things? did you try with a vanilla install.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/973a6e07495b1d1451144ad926473e53a245088e.jpeg" data-download-href="/uploads/short-url/lzPhz1j97qIjH7WZfAM7bnKe92u.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/973a6e07495b1d1451144ad926473e53a245088e_2_690x267.jpeg" alt="image" data-base62-sha1="lzPhz1j97qIjH7WZfAM7bnKe92u" width="690" height="267" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/973a6e07495b1d1451144ad926473e53a245088e_2_690x267.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/973a6e07495b1d1451144ad926473e53a245088e_2_1035x400.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/973a6e07495b1d1451144ad926473e53a245088e_2_1380x534.jpeg 2x" data-dominant-color="CDC6D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×744 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @manjula (2024-08-27 19:28 UTC)

<p>I tried with vanilla installation as well.</p>
<p>just to clarify I am working on the <strong>obj</strong> file not the ply file. ply file i get the colours in the recent release but not on the <strong>obj</strong> file.</p>

---

## Post #18 by @pieper (2024-08-27 19:59 UTC)

<p>I only tried the ply file since the obj file link didn’t have the correct permissions.  I just requested access to the obj version.</p>

---

## Post #19 by @muratmaga (2024-08-27 20:09 UTC)

<aside class="quote no-group" data-username="manjula" data-post="17" data-topic="4206">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>I am working on the <strong>obj</strong> file not the ply</p>
</blockquote>
</aside>
<p>Yeah, I obj doesn’t want to download. If you are trying obj, try with the SlicerMorph install, and when you drag it into Slicer, choose the file description from model to Textured OBJ. That might help.</p>

---

## Post #20 by @manjula (2024-08-28 17:35 UTC)

<p>Hi all</p>
<p>Just to confirm the behaviour in my computer. the obj file does not show colour. I tried importing as obj textured model and it doesnt work either. however the ply works with colors.</p>
<p>In the scalar tab the obj file does not show RGB option like in the ply files.<br>
(i have changed the privacy settings for the obj file if someone wish to try it)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aead4f6779b0a1011563078d949a9054a48ce6b7.png" data-download-href="/uploads/short-url/oVgov6YCrTx01nCEvBvrtnZltlB.png?dl=1" title="Screenshot 2024-08-28 173217" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aead4f6779b0a1011563078d949a9054a48ce6b7_2_690x430.png" alt="Screenshot 2024-08-28 173217" data-base62-sha1="oVgov6YCrTx01nCEvBvrtnZltlB" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aead4f6779b0a1011563078d949a9054a48ce6b7_2_690x430.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aead4f6779b0a1011563078d949a9054a48ce6b7_2_1035x645.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aead4f6779b0a1011563078d949a9054a48ce6b7_2_1380x860.png 2x" data-dominant-color="A2A4B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-08-28 173217</span><span class="informations">1387×866 70.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b960fcb835b90e091efd7782cb2861f8e4e1c56b.png" data-download-href="/uploads/short-url/qrW7OO0LukcQ7HJSmORD9UX9Hzt.png?dl=1" title="Screenshot 2024-08-28 173243" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b960fcb835b90e091efd7782cb2861f8e4e1c56b_2_690x381.png" alt="Screenshot 2024-08-28 173243" data-base62-sha1="qrW7OO0LukcQ7HJSmORD9UX9Hzt" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b960fcb835b90e091efd7782cb2861f8e4e1c56b_2_690x381.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b960fcb835b90e091efd7782cb2861f8e4e1c56b_2_1035x571.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b960fcb835b90e091efd7782cb2861f8e4e1c56b_2_1380x762.png 2x" data-dominant-color="B2B4C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-08-28 173243</span><span class="informations">1690×934 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you</p>

---

## Post #21 by @muratmaga (2024-08-28 17:56 UTC)

<p>Are you sure this is not a data problem? Does meshlab display the obj with texture?</p>

---

## Post #22 by @pieper (2024-08-28 18:50 UTC)

<p>The colors show up for the obj file on the mac’s built in viewer but it’s true they don’t show up in Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/910fd4fd77cb0b2b71ba1313dced3ce4de527ee5.jpeg" data-download-href="/uploads/short-url/kHh9uwHaulHzgYJbwoUavWDJpgp.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/910fd4fd77cb0b2b71ba1313dced3ce4de527ee5_2_266x250.jpeg" alt="image" data-base62-sha1="kHh9uwHaulHzgYJbwoUavWDJpgp" width="266" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/910fd4fd77cb0b2b71ba1313dced3ce4de527ee5_2_266x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/910fd4fd77cb0b2b71ba1313dced3ce4de527ee5_2_399x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/910fd4fd77cb0b2b71ba1313dced3ce4de527ee5_2_532x500.jpeg 2x" data-dominant-color="E7DCD7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">802×752 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>From looking at the file it appears the obj file has lines like:</p>
<pre><code class="lang-auto">v -18.0948 -12.9899 -14.4861 0.664791 0.228153 0.278322
</code></pre>
<p>which are presumably x, y, z, r, g, b.</p>
<p>But VTK’s importer doesn’t read this kind of data:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Kitware/VTK/blob/master/IO/Geometry/vtkOBJReader.cxx#L60-L122">
  <header class="source">

      <a href="https://github.com/Kitware/VTK/blob/master/IO/Geometry/vtkOBJReader.cxx#L60-L122" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/VTK/blob/master/IO/Geometry/vtkOBJReader.cxx#L60-L122" target="_blank" rel="noopener">Kitware/VTK/blob/master/IO/Geometry/vtkOBJReader.cxx#L60-L122</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="60" style="counter-reset: li-counter 59 ;">
          <li>/*---------------------------------------------------------------------------*\</li>
          <li></li>
          <li>This is only partial support for the OBJ format, which is quite complicated.</li>
          <li>To find a full specification, search the net for "OBJ format", eg.:</li>
          <li></li>
          <li>    https://en.wikipedia.org/wiki/Wavefront_.obj_file</li>
          <li>    http://netghost.narod.ru/gff/graphics/summary/waveobj.htm</li>
          <li>    http://paulbourke.net/dataformats/obj/</li>
          <li></li>
          <li>We support the following types:</li>
          <li></li>
          <li>g &lt;groupName&gt;  [... &lt;groupNameN]</li>
          <li></li>
          <li>    group name, primarily for faces</li>
          <li></li>
          <li>v &lt;x&gt; &lt;y&gt; &lt;z&gt;</li>
          <li></li>
          <li>    vertex</li>
          <li></li>
          <li>vn &lt;x&gt; &lt;y&gt; &lt;z&gt;</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Kitware/VTK/blob/master/IO/Geometry/vtkOBJReader.cxx#L60-L122" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If this kind of obj file is common in the wild then it’s probably not hard to extend the VTK code to read them.</p>

---

## Post #23 by @muratmaga (2024-08-28 19:32 UTC)

<aside class="quote no-group" data-username="pieper" data-post="22" data-topic="4206">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>If this kind of obj file is common in the wild</p>
</blockquote>
</aside>
<p>I think it is fairly common to bake texture to vertices to avoid external texture files and the complications arise from it. Since VTK already supports PLYs with vertex colors, it is reasonable to support the OBJ as well.</p>

---

## Post #24 by @pieper (2024-08-28 20:11 UTC)

<p>Sure, I can see that it’s there in this real case.  As the VTK comment says, OBJ format has many variants and they didn’t cover everything.  Adding support for this variant would be a good project for someone who wants to do a little C++ project.  It seems reasonable that the VTK maintainers would welcome the addition.</p>

---
