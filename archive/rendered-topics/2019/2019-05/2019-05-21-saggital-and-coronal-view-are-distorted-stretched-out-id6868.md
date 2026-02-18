# Saggital and Coronal view are distorted (stretched out)

**Topic ID**: 6868
**Date**: 2019-05-21
**URL**: https://discourse.slicer.org/t/saggital-and-coronal-view-are-distorted-stretched-out/6868

---

## Post #1 by @vinipaegle (2019-05-21 11:54 UTC)

<p>Operating system:Microsoft Windows 10<br>
Slicer version: 4.10.1<br>
Hi!<br>
My micro-CT data in tif format was loaded into 3D Slicer,the axinal  view display normally,but the coronal and saggital view was distored  like a line.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34fc48391ea5eeef1e59e689aa3b06d04723064b.png" data-download-href="/uploads/short-url/7yJl6yFrrqyqbGHPs8lVC62jcyn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34fc48391ea5eeef1e59e689aa3b06d04723064b_2_690x353.png" alt="image" data-base62-sha1="7yJl6yFrrqyqbGHPs8lVC62jcyn" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34fc48391ea5eeef1e59e689aa3b06d04723064b_2_690x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34fc48391ea5eeef1e59e689aa3b06d04723064b_2_1035x529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34fc48391ea5eeef1e59e689aa3b06d04723064b.png 2x" data-dominant-color="707087"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1365×700 99.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I´ve changed the Image Spacing but I dont the threes correct numbers. What are correct values of the Image Spacing ? Or How I solve this distortion ?<br>
Thanks!<br>
The Image Spacing chosen by 3D Slicer : <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c76c275e8ef9770b1e7a2af649d8effb5b594d77.png" data-download-href="/uploads/short-url/ssaJzufsU99gRpqtz6DydvzD4Fx.png?dl=1" title="slice_spacing" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c76c275e8ef9770b1e7a2af649d8effb5b594d77_2_690x307.png" alt="slice_spacing" data-base62-sha1="ssaJzufsU99gRpqtz6DydvzD4Fx" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c76c275e8ef9770b1e7a2af649d8effb5b594d77_2_690x307.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c76c275e8ef9770b1e7a2af649d8effb5b594d77_2_1035x460.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c76c275e8ef9770b1e7a2af649d8effb5b594d77.png 2x" data-dominant-color="9696A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slice_spacing</span><span class="informations">1359×606 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The expected image : <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ee6f1c942cd26dbc3bb41611bb9c8799e7a3632.png" data-download-href="/uploads/short-url/4pn7sIuFECeSjrCIEFN6rFWREJk.png?dl=1" title="exepected_images" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ee6f1c942cd26dbc3bb41611bb9c8799e7a3632_2_568x500.png" alt="exepected_images" data-base62-sha1="4pn7sIuFECeSjrCIEFN6rFWREJk" width="568" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ee6f1c942cd26dbc3bb41611bb9c8799e7a3632_2_568x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ee6f1c942cd26dbc3bb41611bb9c8799e7a3632.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ee6f1c942cd26dbc3bb41611bb9c8799e7a3632.png 2x" data-dominant-color="191919"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">exepected_images</span><span class="informations">700×616 45.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
MY micro CT datas :<a href="https://drive.google.com/file/d/1A7BYRmqL5j7q5a8e_cRe4Sc4RUEodsax/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1A7BYRmqL5j7q5a8e_cRe4Sc4RUEodsax/view?usp=sharing</a></p>

---

## Post #2 by @muratmaga (2019-05-21 12:13 UTC)

<p>You need to find the correct image spacing for your Z dimension. Looks like data came from a microCT scanner. File is too large for my to download on my current connection, but maybe there is a text file or some sort of description of scan settings. Perhaps people who scanned it can tell you those…</p>

---

## Post #3 by @vinipaegle (2019-05-21 13:50 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a>. The only informations that I have about how the microCT scanner was seted<br>
are those two :</p>
<ol>
<li>
<p>Current = 74.000000<br>
Data Type = ushort<br>
Image Height = 1013<br>
Image Width = 992<br>
Images Taken = 995<br>
Pixel Size = 6.233620<br>
Voltage = 40.000000</p>
</li>
<li>
<p>This report: <a href="https://drive.google.com/file/d/1m9efFsZeg-QDvd6ku4wmUxFhE12sq71B/view?usp=sharing" rel="nofollow noopener">https://drive.google.com/file/d/1m9efFsZeg-QDvd6ku4wmUxFhE12sq71B/view?usp=sharing</a></p>
</li>
</ol>

---

## Post #4 by @muratmaga (2019-05-21 17:55 UTC)

<p>Report shows pixel resolution as 6.23 micrometer. I  would try that for all axes</p>

---

## Post #5 by @vinipaegle (2019-05-22 18:51 UTC)

<p>muratmaga@ I tried do this, but Sagittal and Coronal images are completely black.<br>
Result: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d699d7025b524fa05a690b87cdfb1a91b2d2f30d.png" data-download-href="/uploads/short-url/uCrMiQVUIVWQw1hffaaYMjkR0bH.png?dl=1" title="tentativa1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d699d7025b524fa05a690b87cdfb1a91b2d2f30d_2_690x387.png" alt="tentativa1" data-base62-sha1="uCrMiQVUIVWQw1hffaaYMjkR0bH" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d699d7025b524fa05a690b87cdfb1a91b2d2f30d_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d699d7025b524fa05a690b87cdfb1a91b2d2f30d_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d699d7025b524fa05a690b87cdfb1a91b2d2f30d_2_1380x774.png 2x" data-dominant-color="9293AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">tentativa1</span><span class="informations">1920×1079 295 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I understanded that If I reduce the number in third box of the  Image Spacing the size of line that appears in the sagittal and coronal planes also decrease.</p>
<p>Image Spacing = 0.5mm<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56877fa1e839de9d8e65028e674b80961863dc81.png" data-download-href="/uploads/short-url/cltmJXcvc1fD7yYZaqmxiLZfseR.png?dl=1" title="5mm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56877fa1e839de9d8e65028e674b80961863dc81_2_690x371.png" alt="5mm" data-base62-sha1="cltmJXcvc1fD7yYZaqmxiLZfseR" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56877fa1e839de9d8e65028e674b80961863dc81_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56877fa1e839de9d8e65028e674b80961863dc81_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56877fa1e839de9d8e65028e674b80961863dc81_2_1380x742.png 2x" data-dominant-color="50504F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5mm</span><span class="informations">1916×1032 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Image Spacing = 0.05mm <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cd0d756500b2c5019fa7eb78baea11e6688c4e4.png" data-download-href="/uploads/short-url/df5mMiPnmoaVtG4Jj9f2AOtaw8Q.png?dl=1" title="05mm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cd0d756500b2c5019fa7eb78baea11e6688c4e4_2_690x374.png" alt="05mm" data-base62-sha1="df5mMiPnmoaVtG4Jj9f2AOtaw8Q" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cd0d756500b2c5019fa7eb78baea11e6688c4e4_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cd0d756500b2c5019fa7eb78baea11e6688c4e4_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cd0d756500b2c5019fa7eb78baea11e6688c4e4_2_1380x748.png 2x" data-dominant-color="515150"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">05mm</span><span class="informations">1920×1041 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @tsehrhardt (2019-05-24 17:35 UTC)

<p>From your screenshots, you only have 1 tiff file loaded rather than a stack.</p>
<p>You can import the tiff stack as an image sequence in Fiji or ImageJ and save as NRRD–you can also set the Image Resolution before saving the NRRD, then import the NRRD into Slicer.</p>

---

## Post #7 by @lassoan (2019-05-26 11:59 UTC)

<p>Conversion to nrrd using Fiji is a good option for special image formats, but in general you can import a tiff stack directly into Slicer by unchecking “single file” option in “Add data” window. See details <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/UserInterface#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F" rel="nofollow noopener">here</a>.</p>

---

## Post #8 by @muratmaga (2019-05-26 19:16 UTC)

<p><a class="mention" href="/u/vinipaegle">@vinipaegle</a>.</p>
<p>I meant that all values in your Image Spacing setting should be 0.00624, as you appear to have scan that has isotropic voxel size. Once you set that up, use the little square icon on the slice view to adjust the zoom level for each view.</p>

---

## Post #9 by @vinipaegle (2019-05-31 18:31 UTC)

<p><a class="mention" href="/u/tsehrhardt">@tsehrhardt</a>,</p>
<p>Thankyou. I imported the tiff stack as an image sequence in ImageJ and saved as tiff because I didn´t find nrrd. Then when I imported in 3D Slicer, the three views appears correctly proportionally,but I am not sure, and  the images appears much greater that it really is.<br>
Image of 3D Slicer: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4eae760660e43733efd1f0172a03f96a5dfbe862.jpeg" data-download-href="/uploads/short-url/be31tfuSvcQW9oKG6n1EZ1OMm9s.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4eae760660e43733efd1f0172a03f96a5dfbe862_2_690x373.jpeg" alt="image" data-base62-sha1="be31tfuSvcQW9oKG6n1EZ1OMm9s" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4eae760660e43733efd1f0172a03f96a5dfbe862_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4eae760660e43733efd1f0172a03f96a5dfbe862_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4eae760660e43733efd1f0172a03f96a5dfbe862_2_1380x746.jpeg 2x" data-dominant-color="9A9AA7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1038 391 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The real image: <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/4133d15a9da7d457acbf5aefd8315d5a408389bb.png" alt="image" data-base62-sha1="9iO3obLF1d4cZvTXL5Wz0IpnnmP" width="214" height="206"></p>

---

## Post #10 by @lassoan (2019-05-31 19:57 UTC)

<p>TIFF format cannot store slice spacing, and the volume does not look stretched out, so it means that scaling is incorrect on all axes now. You can fix it by setting known spacing value in Volumes module as written above.</p>

---

## Post #11 by @vinipaegle (2019-05-31 23:27 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a><br>
Thank you very much!  I have made your suggestion and the images now appear to be correct.<br>
The problem solved:   <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2842c6cadcea654b4fccc643ff7e8ca867a99592.jpeg" data-download-href="/uploads/short-url/5KaaluavbYD0l1sKrAnYrzBeegW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2842c6cadcea654b4fccc643ff7e8ca867a99592_2_690x362.jpeg" alt="image" data-base62-sha1="5KaaluavbYD0l1sKrAnYrzBeegW" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2842c6cadcea654b4fccc643ff7e8ca867a99592_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2842c6cadcea654b4fccc643ff7e8ca867a99592_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2842c6cadcea654b4fccc643ff7e8ca867a99592_2_1380x724.jpeg 2x" data-dominant-color="A7A7B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1010 460 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @vinipaegle (2019-06-01 00:33 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>When I impoted my datas I checked if the "single file was unchecked and was.But even so I had the sam problem with sagital and coronal planes. I belive the suggestion of muratmaga solved my problem.<br>
But whicht are special image formats?</p>

---

## Post #13 by @vinipaegle (2019-06-01 00:42 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thankyou for your explication. But I don´t understand two things</p>
<ol>
<li>The format tiff is bad to import</li>
<li>What you want sat say with " and the volume does not look stretched out"?. The image wasn’t distorced, the problem is just scale?</li>
</ol>

---

## Post #14 by @muratmaga (2019-06-01 15:39 UTC)

<p>Tiff is not ‘bad’ per se, just not convenient for this kind of data.</p>
<p>Tiff format does not have a way to preserve the voxel spacing you manually entered. Therefore, every time you import that dataset, you will have to manually enter those spacing values. Because of this, and various other reasons, people prefer to convert their image sequences into a volumetric formats such as NRRD, Nifti (nii) and others.</p>
<p>Once you imported your data and corrected the voxel spacing, all you need to do is to save it as a NRRD file through Slicer’s save dialogbox. After that you can open it in Slicer without having to worry about these issues. Here is a list of file formats support by Slicer:<br>
<a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SupportedDataFormat" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SupportedDataFormat</a></p>

---

## Post #15 by @tsehrhardt (2019-06-01 18:41 UTC)

<p>You can adjust the spacing in Fiji as well under Image --&gt; Properties before exporting. For microCT tiffs, I have found that they load quite slowly into Slicer and that’s why I import to Fiji, set the resolution, and save as NRRD–the NRRD loads much faster into Slicer. But yes as <a class="mention" href="/u/muratmaga">@muratmaga</a> mentioned too, even if you set the resolution in Slicer as you did above, you can just save the new NRRD with the correct resolution.</p>

---

## Post #16 by @muratmaga (2019-06-01 22:55 UTC)

<p><a class="mention" href="/u/tsehrhardt">@tsehrhardt</a> what version of the slicer are you using to import image stacks? It used to be slow, but in the last year or so, there is not much of a noticable speed difference between importing into Fiji or slicer for me. The only existing issue, if you import a non-tiff stack into Slicer, you need to run the vectortoscalar conversion.</p>

---

## Post #17 by @tsehrhardt (2019-06-02 11:58 UTC)

<p>I am currently on Slicer 4.10.1. I haven’t tried importing tiffs in a while, since I automatically use Fiji. I’ll have to try and see if it’s better for me now.</p>

---

## Post #18 by @muratmaga (2021-02-11 00:05 UTC)

<p>For posterity, <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" rel="noopener nofollow ugc"><code>ImageStacks</code></a> in SlicerMorph extension should be close to the performance you can get from FIJI importing an image sequence and saving it as NRRD.</p>

---

## Post #19 by @tsehrhardt (2021-02-11 00:52 UTC)

<p>Yes ImageStacks is much better than Fiji!</p>

---

## Post #20 by @lassoan (2021-03-13 00:53 UTC)

<p>2 posts were split to a new topic: <a href="/t/ct-image-appears-to-be-distorted/16519">CT image appears to be distorted</a></p>

---
