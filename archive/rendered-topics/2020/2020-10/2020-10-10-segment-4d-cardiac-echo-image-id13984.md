# Segment 4D cardiac echo image

**Topic ID**: 13984
**Date**: 2020-10-10
**URL**: https://discourse.slicer.org/t/segment-4d-cardiac-echo-image/13984

---

## Post #1 by @J_Deng (2020-10-10 21:22 UTC)

<p>This thread sounds most relevant but it was last updated in Dec 2018. Any progress or new advice to address my query below?<br>
If I use Grow from Seeds, seeds I intend to place only for one time point during the cardiac cycle [one 3D volume] are also marked throughout the entire cardiac cycles [multiple volumes]. How could we limit the seeds only to one time point? Or shall I use another mode instead of the usual Segmentation Tool? I’ve tried to export the multiple [4D] volumes into individual, serial 3D volumes using MultipleVolume Support but found no way to go any further.</p>

---

## Post #2 by @lassoan (2020-10-11 02:53 UTC)

<p>We have made lots of progress since 2018. Still not everything is released publicly yet. What would you like to segment: leaflets? adult or pediatric? which valve? What is your end goal?</p>

---

## Post #3 by @J_Deng (2020-10-11 14:38 UTC)

<p>Thanks. It’s the fetal heart. Because of its tininess, I believe that we can only segment 4 major chambers and walls.</p>

---

## Post #4 by @J_Deng (2020-10-13 19:54 UTC)

<p>Dear Andras [and all 4D experts]</p>
<p>The nearest tool I could find is shown in this video: <a href="https://youtu.be/Ev-7mrz-bb0?t=35" rel="noopener nofollow ugc">https://youtu.be/Ev-7mrz-bb0?t=35</a> , but the Valve Annulus Analysis does not appear to be an option / extension to import/install on the latest Slicer 4.11.20200930<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff7ffc159511d781357f339891f30863adeb7596.jpeg" data-download-href="/uploads/short-url/AsfXzOg8KyC1FQUJ1syof5NgOJU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff7ffc159511d781357f339891f30863adeb7596_2_690x388.jpeg" alt="image" data-base62-sha1="AsfXzOg8KyC1FQUJ1syof5NgOJU" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff7ffc159511d781357f339891f30863adeb7596_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff7ffc159511d781357f339891f30863adeb7596_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff7ffc159511d781357f339891f30863adeb7596_2_1380x776.jpeg 2x" data-dominant-color="7D7F8E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 303 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My screen shot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d5fad24fd6d19276f61f41e3bac2087713d677f.jpeg" data-download-href="/uploads/short-url/dk1ocBLqnflf7rhJlMAyW9ZDb9J.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d5fad24fd6d19276f61f41e3bac2087713d677f_2_690x388.jpeg" alt="image" data-base62-sha1="dk1ocBLqnflf7rhJlMAyW9ZDb9J" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d5fad24fd6d19276f61f41e3bac2087713d677f_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d5fad24fd6d19276f61f41e3bac2087713d677f_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d5fad24fd6d19276f61f41e3bac2087713d677f_2_1380x776.jpeg 2x" data-dominant-color="86868C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As my dataset is in 4D, is there any option in Segmentation Editor [or other menus] that can segment a single time point through the 3D space? Then by moving from one time point to another, we segment the entire 4D volume.</p>
<p>If no such option is available, all we need is to add such one, namely 4D Segmentation Editor, to the current Segmentation Editor group.</p>
<p>I understand this will take lots of time and expertise to develop. For the moment, any automatic or semi-automatic option that can export/save one 4D dataset into/as serial individual 3D datasets? So we can segment them separately, then rebuild serial segmented 3D images/objects back to a 4D image/object.</p>
<p>Many thanks. Jing</p>

---

## Post #5 by @J_Deng (2021-08-23 02:05 UTC)

<p>Dear Andras,</p>
<p>I’ve noticed this thread was last updated in July.</p>
<ul>
<li>Any 3D/4D ultrasound image and ECG signal: if the user obtains <a href="https://github.com/SlicerHeart/SlicerHeart#open-image3d-api" rel="noopener nofollow ugc">Image3dAPI</a> plugin from the vendor (GE Voluson, Philips, Siemens, etc.)</li>
</ul>
<p>Does it mean that it can import Voluson 4D data now?</p>
<p>In the past and with your guidance, we managed to import GE Vivid [postnatal cardiac] 4D, but not GE Voluson [fetal cardiac] 4D datasets.</p>
<p>Many thanks in advance.</p>
<p>Jing</p>

---

## Post #6 by @lassoan (2021-08-23 12:44 UTC)

<p>Yes it can. Maybe not all models and not all software versions, though. If you send me a sample data set then I can check - or you can sign up for getting the plugin from GE and try it yourself.</p>

---

## Post #7 by @J_Deng (2021-08-24 00:36 UTC)

<p>Thanks a lot. I acquired some mock datasets tonight. How could I transfer the data to you?</p>
<p>If it is uncompressed *.4dv format that the App can deal with, I have saved them in two folders, one containing 4 data sets of a total 74 MB, the other 2 sets of a total 200 MB. To be on the safe side, I’ve also exported them in dicom, vol, cartesian vol formats.</p>

---

## Post #8 by @lassoan (2021-08-24 00:48 UTC)

<p>Please upload them somewhere (dropbox, onedrive, google drive,…) and post the download link here. Thanks!</p>

---

## Post #9 by @J_Deng (2021-08-24 01:26 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/08lbnrdoyy9313f/AADagzyFhYRkiu-v8bdwgkxHa?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/sh/08lbnrdoyy9313f/AADagzyFhYRkiu-v8bdwgkxHa?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/sh/08lbnrdoyy9313f/AADagzyFhYRkiu-v8bdwgkxHa?dl=0" target="_blank" rel="noopener nofollow ugc">Voluson</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Folder VOLS10RAB6D contains two *.4dv files, obtained using a RAB-6D probe [I believe it is a matrix probe with real-time 4D].</p>
<p>Folder VOLS10RM6C contains four *.4dr files, obtained using a RM-6C probe for the first three datasets.</p>
<p>Dataset 1 is a static 3D [also enclosed a corresponding STL file].<br>
Dataset 2 is a 4D dataset without motion gating [by rapid oscillating of imaging planes].<br>
Dataset 3 is a STIC 4D dataset [i.e., with motion gating, with a presumed HR at 71 bpm].</p>
<p>Dataset 4 is actually from a transvaginal probe but on carotid arterial branches.</p>
<p>None of the datasets are clinically meaningful, as I was basically playing the probe on my own chest and neck without ECG, mimicking 4D ob/gyn scans. But I hope that this is sufficient to test whether they are readable as 4D datasets [except Dataset 1, in 3D] by 3D Slicer plug-ins.</p>
<p>Thank you very much.</p>

---

## Post #10 by @J_Deng (2021-08-30 23:34 UTC)

<p>Dear Andras: Just a gentle follow up to bring my uploads to your attention. But take your time. As soon as we knew which formats are importable in 4D, I will let my collaborators in China know. So, they can acquire 4D datasets with meaningful anatomic info using Voluson E10. I use E95 for the same studies with 4D datasets already importable as shown in the posts above. Thanks a lot. Jing</p>

---

## Post #11 by @lassoan (2021-09-05 01:02 UTC)

<p>These are Kretz ultrasound files.</p>
<p>Slicer can read your uncompressed Kretz ultrasound volumes, such as the .vol files listed below, by using “Add data” (not using DICOM module, because they are not DICOM files):</p>
<ul>
<li>VOLS10RAB6D\IMG_20210823_4_1.vol</li>
<li>VOLS10RAB6D\IMG_20210823_4_2.vol</li>
<li>VOLS10RM6C/IMG_20210823_12_1.vol</li>
<li>VOLS10RM6C/IMG_20210823_12_2.vol</li>
<li>VOLS10RM6C/IMG_20210823_12_3.vol</li>
<li>VOLS10RM6C/IMG_20210823_12_4.vol</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a200b4ca55524a1623fb9ed2c9957818c57b4e6a.jpeg" data-download-href="/uploads/short-url/n78RwooNVH6FFODZaZdHD0zLpFw.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a200b4ca55524a1623fb9ed2c9957818c57b4e6a_2_690x419.jpeg" alt="image" data-base62-sha1="n78RwooNVH6FFODZaZdHD0zLpFw" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a200b4ca55524a1623fb9ed2c9957818c57b4e6a_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a200b4ca55524a1623fb9ed2c9957818c57b4e6a_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a200b4ca55524a1623fb9ed2c9957818c57b4e6a_2_1380x838.jpeg 2x" data-dominant-color="70706F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1167 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/919a58c6fdead20142532831949d257f5766571f.jpeg" data-download-href="/uploads/short-url/kM3V1frU0sH1ably45goPzkMYgL.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/919a58c6fdead20142532831949d257f5766571f_2_690x420.jpeg" alt="image" data-base62-sha1="kM3V1frU0sH1ably45goPzkMYgL" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/919a58c6fdead20142532831949d257f5766571f_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/919a58c6fdead20142532831949d257f5766571f_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/919a58c6fdead20142532831949d257f5766571f_2_1380x840.jpeg 2x" data-dominant-color="737476"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1170 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The others probably could not be loaded because they were compressed. You may be able to load them if you get the <code>KretzLoader.KretzImage3dFileLoader</code> Image3dAPI plugin from GE.</p>

---

## Post #12 by @J_Deng (2021-09-06 22:25 UTC)

<p>Thanks a lot. I now can open these files using what you’ve suggested Add Data. Let me take sometime to digest these as I do not appear to be able to open them in 4D, but only in 3D. BW!</p>

---
