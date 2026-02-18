# missing slices when loading dicom data

**Topic ID**: 33992
**Date**: 2024-01-26
**URL**: https://discourse.slicer.org/t/missing-slices-when-loading-dicom-data/33992

---

## Post #1 by @zkb (2024-01-26 15:22 UTC)

<p>Operating system: windows<br>
Slicer version:4.10.2<br>
Expected behavior: I have a dicom folder which includes 50 dicom files, which means that this image include 50 slices or say the aixal images are 50 in total. However, after  loading it, it only remains 42 slices. I don’t know why but when I try loading it by other software or viewers, it is  actually 50 slices.<br>
Actual behavior:</p>

---

## Post #2 by @pieper (2024-01-26 17:45 UTC)

<p>Probably there are slices at duplicate positions or some similar issue.  Check the error log and also look at the dicom troubleshooting section of the manual.  If you can share data that replicates the issue then someone may be able to help you more.</p>
<p>Also try the latest version, 5.6.1</p>

---

## Post #5 by @zkb (2024-01-27 04:36 UTC)

<p>I have updated to the newest version. And I have seen the error log. But I don’t know how to solve this problem. Could you help me have a look?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e03a78858e9d183ea419bb360485aaf3d29970c.png" data-download-href="/uploads/short-url/4hw9wKyCR9dKs38jU0kyckHV924.png?dl=1" title="a2c6db3cd28da0dccde474dcc9fae51" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e03a78858e9d183ea419bb360485aaf3d29970c_2_690x373.png" alt="a2c6db3cd28da0dccde474dcc9fae51" data-base62-sha1="4hw9wKyCR9dKs38jU0kyckHV924" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e03a78858e9d183ea419bb360485aaf3d29970c_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e03a78858e9d183ea419bb360485aaf3d29970c_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e03a78858e9d183ea419bb360485aaf3d29970c_2_1380x746.png 2x" data-dominant-color="BFC0C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a2c6db3cd28da0dccde474dcc9fae51</span><span class="informations">1920×1039 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2864cf67c60ddcd57c4a564cf66151162c197e0d.png" data-download-href="/uploads/short-url/5Ll5bsxC2Wk49qD6DEWEop121xH.png?dl=1" title="c99605d562f56224441751661e83a8b" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/2864cf67c60ddcd57c4a564cf66151162c197e0d_2_690x373.png" alt="c99605d562f56224441751661e83a8b" data-base62-sha1="5Ll5bsxC2Wk49qD6DEWEop121xH" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/2864cf67c60ddcd57c4a564cf66151162c197e0d_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/2864cf67c60ddcd57c4a564cf66151162c197e0d_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/2864cf67c60ddcd57c4a564cf66151162c197e0d_2_1380x746.png 2x" data-dominant-color="C0C1C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">c99605d562f56224441751661e83a8b</span><span class="informations">1920×1039 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2024-01-28 10:01 UTC)

<p>The message is saying that there is non-uniform sampling in the original data, so probably more than one of the original 50 slices is at the same location in space, so only one of them is used to create the 3D volume.  So the volume has fewer Slices.  You will need to assess whether the volume is correct and use caution when doing any geometric calculations like measuring distances or volumes.</p>

---

## Post #7 by @zkb (2024-01-28 10:25 UTC)

<p>Sure. Thank you very much for your replying. But the biggest problem now is that the volume it  created missed many slices. Is there any way that I can ignore this warning and just load all the slices?  Like in the figure, I miss two slices so the volume it create only contains 48 slices but before loading it shows it has 50 slices.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30657c4381ae7636efa7040cfb77179cc2b50c86.png" data-download-href="/uploads/short-url/6U8lHCTkDWbcDNrzaP1y7MGmVJc.png?dl=1" title="70d6bcfe900f8e1ade239ffa04d1e8c" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30657c4381ae7636efa7040cfb77179cc2b50c86.png" alt="70d6bcfe900f8e1ade239ffa04d1e8c" data-base62-sha1="6U8lHCTkDWbcDNrzaP1y7MGmVJc" width="690" height="17" data-dominant-color="76B2D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">70d6bcfe900f8e1ade239ffa04d1e8c</span><span class="informations">1156×30 781 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4693239f8c2b54777cedd27c1ee2abdd9178ce0.png" data-download-href="/uploads/short-url/wACfc4h7DlsTP0FchZCGN2yBj2w.png?dl=1" title="fdd701c1d9bcdd8c071b7bc927c7565" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4693239f8c2b54777cedd27c1ee2abdd9178ce0_2_690x373.png" alt="fdd701c1d9bcdd8c071b7bc927c7565" data-base62-sha1="wACfc4h7DlsTP0FchZCGN2yBj2w" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4693239f8c2b54777cedd27c1ee2abdd9178ce0_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4693239f8c2b54777cedd27c1ee2abdd9178ce0_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4693239f8c2b54777cedd27c1ee2abdd9178ce0_2_1380x746.png 2x" data-dominant-color="B4B2B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fdd701c1d9bcdd8c071b7bc927c7565</span><span class="informations">1920×1039 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @pieper (2024-01-28 14:10 UTC)

<p>Since the data files themselves have questionable metadata it’s probably better for you to patch them, for example with a mall python script, so that they form the kind of coherent volume that you expect.  As things are now there’s no way for slicer to treat them as a volume.</p>

---
