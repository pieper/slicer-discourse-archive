# Distance measurement and rendering of microscopy images

**Topic ID**: 791
**Date**: 2017-07-31
**URL**: https://discourse.slicer.org/t/distance-measurement-and-rendering-of-microscopy-images/791

---

## Post #1 by @AJ_ZHU (2017-07-31 13:38 UTC)

<p>Hi again I am new so please forgive whatever I show in a silly way.<br>
So while I use the spatial bar, if image-spacing was set as 1mm, no problem to display slices and record movies. But if I set the imaging-spacing as 0.00006mm (0.06um), then the display in slices-view got lagged and movies horrible not right.<br>
I guess it must be a bug or something. Since the spacial-bar meaning how much for a pixel/voxel size is, there should be nothing with relation to matrix/array of data as shown there.<br>
Please help.<br>
regards,<br>
Aijun</p>

---

## Post #2 by @lassoan (2017-07-31 13:45 UTC)

<p>What do you mean by “spatial bar”? Can you include a screenshot and mark it there?<br>
Due to numerical tolerances, you cannot expect any software to work at any size scales (the same way as for many numerical methods you must normalize your inputs).<br>
If your image spacing is 0.06um then you should use micrometer instead of mm as unit (set 0.06 as image spacing instead of 0.00006). If you set length unit in menu from mm to um (Edit / Application settings / Units, Show advanced options, Length / Suffix, change it from mm to um) then most places the unit will be shown as um instead of mm (some places the suffix is hardcoded to be mm, you just have to ignore those and interpret it as um).</p>

---

## Post #3 by @AJ_ZHU (2017-08-02 12:56 UTC)

<p>Thanks a lot for your response, Lassoan.<br>
Simply say, the issue comes as this units setting:</p>
<p>while trying to change the unit (after preset),<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b19d203c1f1b29f0941e242e3fdbddccc96d4de2.png" data-download-href="/uploads/short-url/plf9u6Y4xUsXqPx41UCADw4AmI2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b19d203c1f1b29f0941e242e3fdbddccc96d4de2_2_690x218.png" alt="image" data-base62-sha1="plf9u6Y4xUsXqPx41UCADw4AmI2" width="690" height="218" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b19d203c1f1b29f0941e242e3fdbddccc96d4de2_2_690x218.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b19d203c1f1b29f0941e242e3fdbddccc96d4de2_2_1035x327.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b19d203c1f1b29f0941e242e3fdbddccc96d4de2.png 2x" data-dominant-color="E9EAEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1202×381 78.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
say, I pick up micrometer (um), then restart slicer, it goes back to mm, not um which I need.<br>
or after I open slicer, and then go to the units setting pick up um, and then load a data, the unit goes back to mm as well.</p>
<p>So under mm as unit, if I go to use 0.006um, the screen-capture records a movie, which shows lagged slices.</p>
<p>Regards,<br>
Aijun</p>

---

## Post #4 by @lassoan (2017-08-02 13:14 UTC)

<p>I’m not sure if greek letters are supported. Try using um instead of μm.</p>

---

## Post #5 by @AJ_ZHU (2017-08-02 13:16 UTC)

<p>Actually I did use “um”, not that greek letters there, LOL.<br>
<img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"><br>
Aijun</p>

---

## Post #6 by @lassoan (2017-08-02 13:21 UTC)

<p>I’ve just checked and it works for me correctly.</p>
<p>You can double-check that the unit is saved correctly in your application settings file (search for <code>length</code> word in the file):</p>
<pre><code> c:\Users\&lt;your-user-name&gt;\AppData\Roaming\NA-MIC\Slicer-&lt;your-slicer-revision&gt;.ini</code></pre>

---

## Post #7 by @AJ_ZHU (2017-08-02 14:02 UTC)

<p>Hi Lassoan,<br>
To put it clearly, I use some screen-shots to show what I may get step-by-step.<br>
Firstly I open slicer, and go to set units as followings:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9acf67e68bb0a21838a98f673fdeb996bfd542e.png" data-download-href="/uploads/short-url/v3EbiPQP7toVuKWRigZHJsbE9Xg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9acf67e68bb0a21838a98f673fdeb996bfd542e_2_690x223.png" alt="image" data-base62-sha1="v3EbiPQP7toVuKWRigZHJsbE9Xg" width="690" height="223" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9acf67e68bb0a21838a98f673fdeb996bfd542e_2_690x223.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9acf67e68bb0a21838a98f673fdeb996bfd542e_2_1035x334.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9acf67e68bb0a21838a98f673fdeb996bfd542e.png 2x" data-dominant-color="E8EAEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1064×344 67.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
and then close the slicer, and go to check the .ini file which shows as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6bde7dfb8c7e8be0881734a7036e5d86c3751f0.png" data-download-href="/uploads/short-url/zcMkorsS1qhcHYZp9Qi3cLB97pu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6bde7dfb8c7e8be0881734a7036e5d86c3751f0.png" alt="image" data-base62-sha1="zcMkorsS1qhcHYZp9Qi3cLB97pu" width="690" height="236" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">997×342 8.88 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
which seems ok to me so far; and then<br>
open the slicer again and load a test.img, and go to volume to see the volume-info, which shows as:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6df823c5089a675c361c1df0a72f631b3863302b.jpeg" data-download-href="/uploads/short-url/fGPGeugFtVWSsmCvakd3fk1Ksqf.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6df823c5089a675c361c1df0a72f631b3863302b_2_690x417.jpg" alt="image" data-base62-sha1="fGPGeugFtVWSsmCvakd3fk1Ksqf" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6df823c5089a675c361c1df0a72f631b3863302b_2_690x417.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6df823c5089a675c361c1df0a72f631b3863302b_2_1035x625.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6df823c5089a675c361c1df0a72f631b3863302b.jpeg 2x" data-dominant-color="BDBABB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1052×637 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The spatial-bar is totally wrong there.</p>
<p>That’s what I got so far if I do as mentioned above.<br>
Aijun</p>

---

## Post #8 by @AJ_ZHU (2017-08-02 14:19 UTC)

<p>So then I change units back to the default mm and then load the test img:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f2da379fae77cf82002acc7ea5dd80ab1f3abec.jpeg" data-download-href="/uploads/short-url/birv1qHRqNsEjgOpM5o2O9um3uc.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4f2da379fae77cf82002acc7ea5dd80ab1f3abec_2_690x348.jpg" alt="image" data-base62-sha1="birv1qHRqNsEjgOpM5o2O9um3uc" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4f2da379fae77cf82002acc7ea5dd80ab1f3abec_2_690x348.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4f2da379fae77cf82002acc7ea5dd80ab1f3abec_2_1035x522.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f2da379fae77cf82002acc7ea5dd80ab1f3abec.jpeg 2x" data-dominant-color="B8B8B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1048×530 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
which shows correct spatial bar;</p>
<p>Aijun</p>

---

## Post #9 by @lassoan (2017-08-02 15:06 UTC)

<p>Now I understand what your question is (I’ve updated the subject line accordingly). What you call “spatial bar” is called “ruler” in Slicer.</p>
<p>As you can see, image spacing is now correctly shown in the volumes module (unit is um).</p>
<p>Ruler in slice view can be customized using a different mechanism, by specifying a list of distances and corresponding major/minor tick number, unit, and scale. See an example for micrometer here in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_up_custom_units_in_slice_view_ruler">script repository</a>.</p>

---

## Post #10 by @AJ_ZHU (2017-08-02 16:31 UTC)

<p>Thanks a lot, Iassoan.<br>
I will try that as you suggested there.<br>
Aiden</p>

---

## Post #11 by @AJ_ZHU (2017-08-03 04:31 UTC)

<p>Thank you so much for your expertise, Iassoan!<br>
It works Well now!</p>
<p>Thank you very much again and have a great day!<br>
Aijun</p>

---
