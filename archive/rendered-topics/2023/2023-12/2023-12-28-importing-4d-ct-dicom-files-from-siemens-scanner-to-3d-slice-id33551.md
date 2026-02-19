---
topic_id: 33551
title: "Importing 4D Ct Dicom Files From Siemens Scanner To 3D Slice"
date: 2023-12-28
url: https://discourse.slicer.org/t/33551
---

# Importing 4D CT DICOM files from Siemens scanner to 3D Slicer

**Topic ID**: 33551
**Date**: 2023-12-28
**URL**: https://discourse.slicer.org/t/importing-4d-ct-dicom-files-from-siemens-scanner-to-3d-slicer/33551

---

## Post #1 by @SassanHashemi (2023-12-28 20:47 UTC)

<p>Win10<br>
Slicer 5.6.1<br>
Scanner: Siemens SOMATOM Force</p>
<p>Hi,</p>
<p>I am not able to import a time-resolved cardiac CT sequence, consisting of 10 time points and 300 slices. I tried exporting DICOMs both as separate folders for each time point, and also all the DICOMs in one single folder. I used the examine button and selected different Multivolume options available individually and together (see below). I also tried different combination of “DICOM Plugins” to no avail.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b6d0997eb74b323523d3a6efa697b5fd01d40e6.jpeg" data-download-href="/uploads/short-url/1D4RyMj1kEJ5PXZCjBhHxpRG5tI.jpeg?dl=1" title="01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b6d0997eb74b323523d3a6efa697b5fd01d40e6_2_690x479.jpeg" alt="01" data-base62-sha1="1D4RyMj1kEJ5PXZCjBhHxpRG5tI" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b6d0997eb74b323523d3a6efa697b5fd01d40e6_2_690x479.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b6d0997eb74b323523d3a6efa697b5fd01d40e6_2_1035x718.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b6d0997eb74b323523d3a6efa697b5fd01d40e6.jpeg 2x" data-dominant-color="3C4247"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01</span><span class="informations">1247×866 98.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1b30444c48ee64a99df28a45de551795604026e.jpeg" data-download-href="/uploads/short-url/n4spGb0SRnDk6DXxJWCQWITEUGO.jpeg?dl=1" title="02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1b30444c48ee64a99df28a45de551795604026e_2_688x500.jpeg" alt="02" data-base62-sha1="n4spGb0SRnDk6DXxJWCQWITEUGO" width="688" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1b30444c48ee64a99df28a45de551795604026e_2_688x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1b30444c48ee64a99df28a45de551795604026e_2_1032x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1b30444c48ee64a99df28a45de551795604026e.jpeg 2x" data-dominant-color="2C3136"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">02</span><span class="informations">1262×917 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I scroll through the images in metadata, it goes through all the slices in a time point before advancing to the next time point. Is there a way to sort/read the files in Slicer based on “slice position”?</p>
<p>I appreciate your help in advance.</p>
<p>Sassan</p>

---

## Post #2 by @mikebind (2023-12-28 21:12 UTC)

<p>Your screenshots look OK to me.  What happens if you click the “Load” button? In both screenshots, the top, checked option looks like it is a 10 frame volume sequence, which is what you want.  You can then go through each frame using the sequence browser.</p>

---

## Post #3 by @SassanHashemi (2023-12-29 15:24 UTC)

<p>Thanks for the reply.</p>
<p>When I click load, I get the error message on the screen in the 2nd screenshot:</p>
<p>Could not load @@@ 10 frames volume sequence by acquisition time as a Multivolume.</p>
<p>I link to the dataset down here and would really appreciate if you could take a look at your convenience.</p>
<p><a href="https://1drv.ms/f/s!An5lW2cr0wILgpskup_vMejEXjWCmw?e=Pb3Xrs" rel="noopener nofollow ugc">https://1drv.ms/f/s!An5lW2cr0wILgpskup_vMejEXjWCmw?e=Pb3Xrs</a></p>
<p>Sassan</p>

---

## Post #4 by @mikebind (2023-12-29 23:50 UTC)

<p>I tried your dataset and it loads OK for me:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecec892ef0b5c19b1c89d1584a4dee8da2447d6a.png" data-download-href="/uploads/short-url/xNVsrBPK7sjpSPGmcSHniRQbDHs.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecec892ef0b5c19b1c89d1584a4dee8da2447d6a_2_690x210.png" alt="image" data-base62-sha1="xNVsrBPK7sjpSPGmcSHniRQbDHs" width="690" height="210" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecec892ef0b5c19b1c89d1584a4dee8da2447d6a_2_690x210.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecec892ef0b5c19b1c89d1584a4dee8da2447d6a_2_1035x315.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecec892ef0b5c19b1c89d1584a4dee8da2447d6a_2_1380x420.png 2x" data-dominant-color="D4E5EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1391×425 62 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Both the first and second options load as Volume Sequences that I can play back.  The first is the right one to choose, the second one loads but has step/banding artifacts because it organizes by time instead of by cardiac cycle.</p>
<p>What version of Slicer are you using?  I loaded with 5.2.1, which is a little behind the current stable version.  If you are using an older version, try upgrading to the current stable and see if that works.  The DICOM plugin you need enabled is MultiVolumeImporterPlugin, and then make sure that the one you select is described as a Volume Sequence by CardiacCycle (not a MultiVolume by CardiacCycle; somewhat confusingly, MultiVolume is a deprecated predecessor to Volume Sequences.  It is OK that the “Reader” column says MultiVolume, you just don’t want that in the first column).  It is possible that the version you are using is getting tripped up by the StudyID, StudyDescription, and SeriesDescription DICOM tags being empty.  If you are unable to update your Slicer version, I would try filling in those tags with something and see if that allows you to load.</p>

---

## Post #5 by @jamesobutler (2023-12-30 15:53 UTC)

<aside class="quote no-group" data-username="SassanHashemi" data-post="1" data-topic="33551">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sassanhashemi/48/18415_2.png" class="avatar"> SassanHashemi:</div>
<blockquote>
<p>Slicer 5.6.1</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="mikebind" data-post="4" data-topic="33551">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>What version of Slicer are you using? I loaded with 5.2.1, which is a little behind the current stable version. If you are using an older version, try upgrading to the current stable and see if that works.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/mikebind">@mikebind</a> It appears <a class="mention" href="/u/sassanhashemi">@SassanHashemi</a> is using the latest version of Slicer (5.6.1). If it is working for you with Slicer 5.2.1, maybe you can confirm that it is also working with Slicer 5.6.1.</p>

---

## Post #6 by @SassanHashemi (2024-01-02 16:18 UTC)

<p>Apologies I didn’t have access to my laptop for a few days.</p>
<p>This is very strange! I had anonymized the data I shared with you under a different name. I loaded the version I shared with you and to my surprise it loaded fine, exactly the way it loaded for you!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b2a8833e498850d28b84bade3c8e32681bf6854.jpeg" data-download-href="/uploads/short-url/69REExJoRDsCA9oyHED4VaA29co.jpeg?dl=1" title="001" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b2a8833e498850d28b84bade3c8e32681bf6854_2_690x435.jpeg" alt="001" data-base62-sha1="69REExJoRDsCA9oyHED4VaA29co" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b2a8833e498850d28b84bade3c8e32681bf6854_2_690x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b2a8833e498850d28b84bade3c8e32681bf6854_2_1035x652.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b2a8833e498850d28b84bade3c8e32681bf6854.jpeg 2x" data-dominant-color="2B3035"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">001</span><span class="informations">1359×858 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I load the data with the other name I was having issues with, it still doesn’t load!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbd6bd865cede03704e86f4b3344fe450bfc5599.jpeg" data-download-href="/uploads/short-url/zVRVijUFlB76LSovYQmhYRbyQ5j.jpeg?dl=1" title="002" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbd6bd865cede03704e86f4b3344fe450bfc5599_2_690x434.jpeg" alt="002" data-base62-sha1="zVRVijUFlB76LSovYQmhYRbyQ5j" width="690" height="434" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbd6bd865cede03704e86f4b3344fe450bfc5599_2_690x434.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbd6bd865cede03704e86f4b3344fe450bfc5599_2_1035x651.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbd6bd865cede03704e86f4b3344fe450bfc5599.jpeg 2x" data-dominant-color="2A2F35"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">002</span><span class="informations">1357×855 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you think the name I chose for the dataset had anything to do with it? Just so that I can avoid this issue in the future.</p>
<p>Thanks again for the guidance.</p>
<p>Sassan</p>

---

## Post #7 by @lassoan (2024-01-02 16:23 UTC)

<p>This is very interesting, because anonymization usually breaks things.</p>
<p>How did you anonymize the images? What fields have you modified? Have you regenerated UIDs?<br>
Have you renamed the DICOM files?</p>

---

## Post #8 by @SassanHashemi (2024-01-02 19:06 UTC)

<p>I used the same Siemens software to anonymize without changing any settings between the two. Not sure which DICOM tags get deleted or re-written.</p>
<p>I uploaded the dataset with the other name for you to take a look.<br>
<a href="https://1drv.ms/f/s!An5lW2cr0wILgrJr3Jdi5mQZmd55pw?e=Wkiau4" rel="noopener nofollow ugc">https://1drv.ms/f/s!An5lW2cr0wILgrJr3Jdi5mQZmd55pw?e=Wkiau4</a></p>
<p>Thank you,<br>
Sassan</p>

---

## Post #9 by @lassoan (2024-01-02 22:44 UTC)

<p>For me, this dataset loaded correctly, too.</p>
<p>Maybe try to copy the files again, maybe to a folder that has shorter name.</p>
<p>You can also enable detailed DICOM logging (in menu: Edit / Application settings / DICOM) and check the application log after clicking “Examine” and see if there is any message related to <code>CardiacCycle</code>.</p>

---

## Post #10 by @SassanHashemi (2024-01-03 18:10 UTC)

<p>I think I found the culprit.</p>
<p>There was a comma in the folder name. Just took it out and it worked.</p>
<p>Thank you to all of you for helping me with this.</p>
<p>Cheers,<br>
Sassan</p>

---
