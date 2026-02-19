---
topic_id: 479
title: "Flipped Nifti Image Compared To Original Nrrd File"
date: 2017-06-11
url: https://discourse.slicer.org/t/479
---

# Flipped NIFTI image compared to original Nrrd File

**Topic ID**: 479
**Date**: 2017-06-11
**URL**: https://discourse.slicer.org/t/flipped-nifti-image-compared-to-original-nrrd-file/479

---

## Post #1 by @belleauel (2017-06-11 19:27 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello Slicer Experts,</p>
<p>I had done some initial processing of my DTI data in Slicer.</p>
<p>Now, I have converted the files to nifti via DWIConvert  so that I can use some FSL tools.</p>
<p>When I load the nifti versus the .nrrd in Slicer, I notice the nifti file is flipped compared to the nrrd.</p>
<p>Indeed, when I look at the headers of both files, one says left-posterior-superior and the other says right-superior-anterior. How can I rectify this?</p>
<p>Thank you for your help!</p>
<p>Emily</p>

---

## Post #2 by @pieper (2017-06-12 19:49 UTC)

<p>Hi Emily -</p>
<p>Is there any chance you can share a dataset that exhibits this issue along with the specific tools and steps that lead to the problem?  Maybe you could reproduce the issue using the DWI dataset that is available in Slicer’s SampleData module?  Or maybe a scan of a phantom?</p>
<p>There are lots of ways to flip the image data, but correctly transforming the gradients can be tricky and maybe there’s an issue with the converter.</p>
<p>Best,<br>
Steve</p>

---

## Post #3 by @belleauel (2017-06-16 20:20 UTC)

<p>Hi Steve,</p>
<p>Thanks for the reply. I am attaching my .nrrd file that I have been using in Slicer.</p>
<p>Than I used the following command via Slicer to convert the .nrrd file to nifti. Looks like I cannot upload these types of files. Could I perhaps email them to you?</p>
<p>The command:</p>
<p>DWIConvert --allowLossyConversion --conversionMode NrrdToFSL --inputVolume X.nrrd --outputVolume X.nii --output BVectors x.bvec --output BValues X.bval</p>
<p>I appreciate any thoughts you have. I am not 100% sure if I have a problem or not.</p>
<p>Thanks,</p>
<p>Emily</p>

---

## Post #4 by @lassoan (2017-06-16 23:42 UTC)

<p>To share images, upload to your cloud storage account (Dropbox, OneDrive, Google drive) and copy-paste the link here.</p>

---

## Post #5 by @belleauel (2017-06-17 17:05 UTC)

<p>Hi Steve,</p>
<p>Here is the link to the data.</p>
<p>Thank you so much!</p>
<p>Emily</p>
<p>[<a href="https://drive.google.com/open?id=0BxJP5A6fFyuULVRjR19JSl9CZDA" rel="nofollow noopener">https://drive.google.com/open?id=0BxJP5A6fFyuULVRjR19JSl9CZDA</a>]</p>

---

## Post #6 by @belleauel (2017-06-17 17:05 UTC)

<p>Thank you very much!</p>

---

## Post #7 by @pieper (2017-06-20 22:55 UTC)

<p>Hi Emily -</p>
<p>Thanks for sharing the data - I was able to load it and work with it but wasn’t able to replicate the flipping issue you reported.</p>
<p>The command line I tested (below) was pretty much the same as yours.  I tried converting the nrrd you sent and when I loaded the resulting nii file there was no flipping.  Then I also downloaded the nii file you provided and again I didn’t see any flipping compared to the nrrd.</p>
<p>Can you doublecheck that when you load the nii and nrrd you uploaded into Slicer they don’t match?</p>
<p>I was using the nightly build from May 29 2017 on a mac.  If you were using the 4.6.2 version you might try a more recent nightly although I don’t think this code has changed much.</p>
<p>If you loaded and re-saved the nii file in other software then perhaps other things happened (nifti can be a tricky format which is why we try to avoid using it).</p>
<p>-Steve</p>
<p><code>./Contents/lib/Slicer-4.7/cli-modules/DWIConvert --conversionMode NrrdToFSL --inputVolume /tmp/ELS_002_dwi-xc_QCed_permute_Ed_epi.nrrd --outputVolume /tmp/ELS_002_dwi-xc_QCed_permute_Ed_epi-cli.nii --outputBValues /tmp/b.vals --outputBVectors /tmp/b.vecs</code></p>
<p>Best,<br>
Steve</p>

---

## Post #8 by @belleauel (2017-06-21 19:42 UTC)

<p>Hi Steve,</p>
<p>Thanks so much!!!</p>
<p>I am noticing that the nrrd file and the nifti file look the same on Slicer. However, when I load the nifti file in the fsl viewer, things look a bit different. It may just be a matter of differences in how Slicer and FSL present the data.</p>
<p>I had initially (not the files I sent you) converted the nrrd file from a type unsigned short to just a short and then converted the file to nifti. In that process, the nifti file was flipped compared to the nrrd file in Slicer.  When I left out the conversion to short from unsigned short, I did not see the flipping issue (the files I sent you).</p>
<p>Thanks,</p>
<p>Emily</p>

---

## Post #9 by @pieper (2017-06-21 20:15 UTC)

<p>Thanks for doublechecking Emily - there are a lot of issue with coordinates<br>
that can pop up when going between packages and formats.  This wiki page<br>
might help but also check the display options for other software (some use<br>
"neurological" convention while Slicer strictly uses "radiological"<br>
convention for display).</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #10 by @ReNeu (2024-08-08 06:16 UTC)

<p>Hi Steve and Andras,</p>
<p>I have the same problem discussed in this conversation. Yet, all the the steps I’m taking are done via slicer 5.6.1 (creating lesion map, exporting lesion map into nifti format and viewing the lesion map .nii separately).</p>
<p>Here is the link to my data:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1vIt6Z4W17UpNr2klbmDUSVdj0nGG8OBo%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1vIt6Z4W17UpNr2klbmDUSVdj0nGG8OBo%3Fusp%3Dsharing&amp;ifkv=AdF4I77pzTxk_sQX6_b7XvAWHTmfzjeU3HHj6vlpIBXYtPaVzsXr1ofBLe6344OgZl_YVZMchTAdbA&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-1710453034%3A1723097148936477">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1vIt6Z4W17UpNr2klbmDUSVdj0nGG8OBo%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1vIt6Z4W17UpNr2klbmDUSVdj0nGG8OBo%3Fusp%3Dsharing&amp;ifkv=AdF4I77pzTxk_sQX6_b7XvAWHTmfzjeU3HHj6vlpIBXYtPaVzsXr1ofBLe6344OgZl_YVZMchTAdbA&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-1710453034%3A1723097148936477" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1vIt6Z4W17UpNr2klbmDUSVdj0nGG8OBo%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1vIt6Z4W17UpNr2klbmDUSVdj0nGG8OBo%3Fusp%3Dsharing&amp;ifkv=AdF4I77pzTxk_sQX6_b7XvAWHTmfzjeU3HHj6vlpIBXYtPaVzsXr1ofBLe6344OgZl_YVZMchTAdbA&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin&amp;dsh=S-1710453034%3A1723097148936477" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The problem:</p>
<ol>
<li>When I open the scene / .nrrd file, the lesion appears in the correct location.</li>
<li>Note the lesion is more to the right superiorly and then moves to the middle of the brain in more inferior slices.</li>
<li>I  then export the lesion map in a .nii format</li>
<li>when I open the .nii file (in slicer) the lesion is to the left in the more superior slices and moves to the middle in more inferior slices.</li>
</ol>
<p>Why is this happening and how can I fix it?</p>
<p>Thank you in advance,</p>
<p>Ettie</p>

---

## Post #11 by @pieper (2024-08-08 13:15 UTC)

<p><a class="mention" href="/u/reneu">@ReNeu</a> - You’ll need to change the permissions on the google drive so that others can access it.</p>
<p>Also, please try the latest versions of Slicer to confirm there is still an issue.  If it is, please describe exactly what steps you take (add screenshots to clarify as needed).</p>

---

## Post #12 by @ReNeu (2024-08-12 12:22 UTC)

<p>Hi Steve,</p>
<p>Thanks for your prompt input. I’ve now installed 3D Slicer 5.6.2.</p>
<p>My steps:</p>
<ol>
<li>Open the saved scene in slicer</li>
<li>Inspect the lesion map + confirm it’s accurate to the lesion (1st image)</li>
<li>Save the lesion as .nii file in a different folder (2nd image)</li>
<li>Close the scene</li>
<li>Open the newly saved lesion map</li>
<li>The lesion map is now a mirror vision of the original lesion map</li>
</ol>
<p>Here is the link for the data for testing (permission granted): <a href="https://drive.google.com/drive/folders/1vIt6Z4W17UpNr2klbmDUSVdj0nGG8OBo?usp=drive_link" class="inline-onebox" rel="noopener nofollow ugc">CT subj38 testing - Google Drive</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5975f45aed54e18415887cf2239e21d40e1e35a5.jpeg" data-download-href="/uploads/short-url/cLpd629M0kOAWsyLkZixW3HzRU9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5975f45aed54e18415887cf2239e21d40e1e35a5_2_690x448.jpeg" alt="image" data-base62-sha1="cLpd629M0kOAWsyLkZixW3HzRU9" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5975f45aed54e18415887cf2239e21d40e1e35a5_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5975f45aed54e18415887cf2239e21d40e1e35a5_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5975f45aed54e18415887cf2239e21d40e1e35a5_2_1380x896.jpeg 2x" data-dominant-color="5E5B5B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1382×899 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/925104c6adb3aff359a0e0c322555d3a8ef150b7.png" data-download-href="/uploads/short-url/kSni7ONLMrsIp3VxwdGymjvQ4Gb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/925104c6adb3aff359a0e0c322555d3a8ef150b7_2_690x474.png" alt="image" data-base62-sha1="kSni7ONLMrsIp3VxwdGymjvQ4Gb" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/925104c6adb3aff359a0e0c322555d3a8ef150b7_2_690x474.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/925104c6adb3aff359a0e0c322555d3a8ef150b7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/925104c6adb3aff359a0e0c322555d3a8ef150b7.png 2x" data-dominant-color="848484"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">885×608 76.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @pieper (2024-08-12 20:56 UTC)

<p>Thanks for sharing - can you do one more test to see if you see this issue when saving to nrrd?</p>
<p>If you’ve looked you probably saw that the nifti format is not very popular among Slicer developers due to a long history of issues (the standard itself defines multiple, possibly contradictory, ways of encoding geometry information and many other software packages have inconsistent or buggy ways of interpreting this data, etc).</p>
<p>So, while we’ll probably be able to explain why this data doesn’t work, it’s likely something intrinsic to nifti.  Or it could be a regression in the Slicer/ITK nifti pipeline which has been edited in the last few years to try to better handle issues with the format.  Knowing if nrrd works will help whoever does the next level investigation.</p>

---
