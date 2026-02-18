# DWIConvert NIFTI to NRRD issue

**Topic ID**: 2201
**Date**: 2018-02-27
**URL**: https://discourse.slicer.org/t/dwiconvert-nifti-to-nrrd-issue/2201

---

## Post #1 by @ryanhucla (2018-02-27 22:56 UTC)

<p>Hi all,</p>
<p>I am using DWIConvert to convert NIFTIs to NRRDs so that I can use DTIPrep’s artifact detection and denoising tools. I then plan to convert these NRRDs back to NIFTI so that I can use FSL’s eddy and then FSL’s TBSS analysis. However, after running DTIPrep preprocessing, converting back to NIFTI, and running FSL eddy, I’m seeing strange results. Eddy outputs a file called data.nii.gz.eddy_restricted_movement_rms in which there are estimates for movement (1) relative to the first volume (the b0) and (2) between each consecutive volumes. I use this movement estimation file to identify subjects with excess movement in the scanner to remove them from analysis.</p>
<p>Here is the puzzling output that I get, where the first column indicates type-(1) values and the second column indicates type-(2) values (bold emphasis mine):</p>
<p>0 0<br>
0.0004349732621 0.0004349732621<br>
0.1293237744 0.1290371457<br>
0.0770145743 0.0787793649<br>
0.1380966347 0.1334343518<br>
0.120617891 0.0671182883<br>
0.2690339005 0.164081166<br>
0.3256238628 0.07334808195<br>
0.1346585371 0.1988556541<br>
0.1346585371 <strong>0</strong><br>
0.1346585371 <strong>0</strong><br>
0.1346585371 <strong>0</strong><br>
0.1346585371 <strong>0</strong><br>
0.1364517787 0.06969197052<br>
0.2810317103 0.1871601272<br>
0.2053992891 0.1139292096<br>
0.1838997283 0.04258127975<br>
0.1850058225 0.03042424084<br>
0.1640395851 0.04978561965<br>
0.1441797516 0.03871081352<br>
0.1411901608 0.08651112032<br>
0.05642180761 0.09891716264<br>
0.1132709746 0.1019541404<br>
0.198486599 0.2614182835<br>
0.2152392961 0.02585408788<br>
0.2636229757 0.05646168819<br>
0.2057839289 0.111750168<br>
0.2018872141 0.06196124255<br>
0.3124672885 0.1476290345<br>
0.3520931575 0.07196218901<br>
0.2838850662 0.09389126276<br>
0.3076169748 0.04724860972<br>
0.3053632287 0.0193159719</p>
<p>According to this, there is absolutely zero movement between a consecutive 4 volumes, which seems unlikely, if not impossible. I get similar strange looking output for many other subjects processed using DTIPrep tools and then FSL eddy. Importantly, I get normal-looking movement estimation when I do not use DWIConvert or DTIPrep’s tools.</p>
<p>To identify the problem, I’ve tried only using DWIConvert from NIFTI to NRRD and then again from NRRD to NIFTI without using any of DTIPrep’s preprocessing tools. In theory, there should be no change in the NIFTI after converting to and from NRRD. However, after running FSL eddy again on this back-and-forth-converted dataset, I still get strange eddy movement estimation in that it indicates absolutely zero movement between certain volumes. So, it seems the issue is due to DWIConvert, a Slicer tool, and not due to DTIPrep’s preprocessing tools.</p>
<p>Does anyone have any insight into what may be causing the problem? Converting from NIFTI to NRRD back to NIFTI using DWIConvert seems to change the alignment of volumes. But I’m not quite sure.</p>
<p>I’ve gone through extensive troubleshooting thanks to help from Martin Styner over at the DTIPrep forums, but we haven’t been able to solve the issue. <a href="https://www.nitrc.org/forum/forum.php?thread_id=6671&amp;forum_id=1188" rel="nofollow noopener">Here’s the attempted troubleshooting in more detail.</a></p>
<p>Here’s what I’m calling in the command line to go from NIFTI --&gt; NRRD:<br>
DWIConvert --inputVolume raw_dwi.nii.gz -o dwi.nrrd --conversionMode FSLToNrrd --inputBValues bvals_col --inputBVectors bvecs_col</p>
<p>And from NRRD --&gt; NIFTI:<br>
DWIConvert --inputVolume dwi.nrrd --conversionMode NrrdToFSL --outputVolume raw_dwi_QCed.nii --outputBVectors bvecs_col_QCed --outputBValues bvals_col_QCed</p>
<p>Thank you very much in advance!</p>

---

## Post #2 by @ihnorton (2018-02-28 15:21 UTC)

<p>Hi Ryan,<br>
What version of DWIConvert are you using? I did some <a href="https://github.com/BRAINSia/BRAINSTools/issues/368#issuecomment-368223301">round-trip tests a few days ago</a> using the latest version of DWIConvert, stand-alone (command-line, not through Slicer), and got reasonable results. <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> and others have made a number of improvements to DWIConvert and ITK nifti support recently. So I would suggest trying the latest version, if you are not already using it.</p>
<p>Other things to look at are: compare raw image voxel values after the round-trip through DWIConvert, and check for difference in bvec files.</p>

---

## Post #3 by @ryanhucla (2018-03-01 18:40 UTC)

<p>Hey Isaiah, thanks for your help!</p>
<p>I’m using DWIConvert 1.2.4. Perhaps that’s the issue, because the bvecs/bvals are the same before and after conversion. Also, the intensity values are identical before and after conversion as well. I’ll try out updating Slicer and let you know how that goes.</p>

---

## Post #4 by @ihnorton (2018-03-01 20:00 UTC)

<aside class="quote no-group" data-username="ryanhucla" data-post="3" data-topic="2201">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/73ab20/48.png" class="avatar"> ryanhucla:</div>
<blockquote>
<p>the bvecs/bvals are the same before and after conversion. Also, the intensity values are identical before and after conversion as well.</p>
</blockquote>
</aside>
<p>If they are identical when doing just the nii → nrrd → nii trip via DWIConvert, then the only other difference I can think of is the orientations. You can check those with <code>fslorient -getsform</code> (or <code>-getqform</code>).</p>

---
