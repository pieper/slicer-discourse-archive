# MR image loaded from DICOM format is not 3D

**Topic ID**: 10106
**Date**: 2020-02-04
**URL**: https://discourse.slicer.org/t/mr-image-loaded-from-dicom-format-is-not-3d/10106

---

## Post #1 by @Onur_Goncu (2020-02-04 14:46 UTC)

<p>Operating system:Windows 10 - i7- 9700K - 32GB Ram - 4GB GTX1030<br>
Slicer version:4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello Friends! I am a master degree student in Turkey. I am interested in using of this program and want to make my thesis on it. Now, we have some images from MR files in dcm format. I will study on aorta. When we import a file, we can’t see everything clear, we can only get closer or move away from the picture. On example files, we can see details using middle button of mouse. I hope i could make you understand my problem ^^’. Or , as an alternative, is there a way i can combine all my images and get a image that i can clearly analyse. I need help friends, i would very appreciate your help. Thanks a lot.</p>
<p>Very best regards.</p>

---

## Post #2 by @JanWitowski (2020-02-04 16:04 UTC)

<p>Hi, could you provide some screenshots of loaded images?</p>

---

## Post #3 by @timeanddoctor (2020-02-06 11:57 UTC)

<p>Did you mean stack a serial pictrues as a single one?</p>

---

## Post #4 by @Onur_Goncu (2020-02-07 10:49 UTC)

<p>Hello again sir, thanks a lot for the answer. Let me show you the problem.<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/0445726a9ad73a78ab60b828bbb9e3704322d7e9.png" alt="Screenshot_1" data-base62-sha1="BMHlXTbuy4CTBwrgZZEtJRNcGB" width="419" height="45"></p>

---

## Post #5 by @Onur_Goncu (2020-02-07 10:50 UTC)

<p>Yes sir. Absolutely.</p>

---

## Post #6 by @Onur_Goncu (2020-02-07 10:53 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc0684266f84e309a94b9aa874c20b4171cabb20.png" data-download-href="/uploads/short-url/zXwhzFhDeN6wEIfTca0gwq0IEtq.png?dl=1" title="example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc0684266f84e309a94b9aa874c20b4171cabb20_2_690x382.png" alt="example" data-base62-sha1="zXwhzFhDeN6wEIfTca0gwq0IEtq" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc0684266f84e309a94b9aa874c20b4171cabb20_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc0684266f84e309a94b9aa874c20b4171cabb20.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc0684266f84e309a94b9aa874c20b4171cabb20.png 2x" data-dominant-color="474852"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">example</span><span class="informations">955×529 87.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
you can see the difference. The first one is the example i found on youtube. You can see many veins when you use the middle button of mouse. But below, I have many images like that , i cant use the middle button of mouse to see the details.</p>

---

## Post #7 by @timeanddoctor (2020-02-07 11:00 UTC)

<p>Maybe you lost the z axis of the DICOM.<br>
You can modify the parameter of the volume  information to change from the pic2 to pic1.</p>

---

## Post #8 by @timeanddoctor (2020-02-07 11:01 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1e1f799fca99ec30441bd9637e4167b552425d8.png" alt="image" data-base62-sha1="pnCDYpDj8Dk60CW8RGZouWFpdj2" width="647" height="347"></p>

---

## Post #9 by @lassoan (2020-02-07 14:01 UTC)

<p>Maybe you did not use the DICOM module to load the data set? Please use latest Slicer Preview release (as it has greatly improved DICOM browser) and the DICOM module to load the image and let us know how it worked.</p>

---
