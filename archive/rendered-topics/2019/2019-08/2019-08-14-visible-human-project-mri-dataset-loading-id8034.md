# Visible human project MRI dataset loading

**Topic ID**: 8034
**Date**: 2019-08-14
**URL**: https://discourse.slicer.org/t/visible-human-project-mri-dataset-loading/8034

---

## Post #1 by @aimly (2019-08-14 19:35 UTC)

<p>Operating system:Mac<br>
Slicer version:4.10.2<br>
Expected behavior: Trying to load dataset from Visible human project<br>
Actual behavior: Loading problems</p>

---

## Post #2 by @pieper (2019-08-14 20:47 UTC)

<p>Hi - can you be more specific about which data you were trying to load and the problems were?</p>

---

## Post #3 by @aimly (2019-08-16 08:45 UTC)

<p>Hi sorry, I’m quite new to all this an wasn’t sure where to describe the problem in detail.</p>
<p>I downloaded the open source VHP datasets and have mainly been working with the 4K tiff images which load into Slicer with no serious problems (despite there being no header info)and have managed to make segmentations and 3D print them.</p>
<p>Now I am trying to load in the MRI data. The files come in 2 directorys, MRI images and then a separate directory of MRI headers which are text files.</p>
<p>The MRI images have a format that my mac is interpreting as a zip file I think but when I try to open it I just get an exec file</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d695d0c0dfbbdba3f2578713fd5f644daf31f96.png" data-download-href="/uploads/short-url/b2OvkMN8dKCbPi1nIQrwQjQAVwO.png?dl=1" title="Screenshot 2019-08-16 09.39.37.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d695d0c0dfbbdba3f2578713fd5f644daf31f96_2_690x147.png" alt="Screenshot 2019-08-16 09.39.37.png" data-base62-sha1="b2OvkMN8dKCbPi1nIQrwQjQAVwO" width="690" height="147" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d695d0c0dfbbdba3f2578713fd5f644daf31f96_2_690x147.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d695d0c0dfbbdba3f2578713fd5f644daf31f96.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d695d0c0dfbbdba3f2578713fd5f644daf31f96.png 2x" data-dominant-color="DCDCDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2019-08-16 09.39.37.png</span><span class="informations">820×175 38.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I drag and drop this directory into 3Dslicer, nothing happens, and it also won’t load it into the DICOM database, presumably because the header files are in a separate directory.</p>
<p>My next plan is to separate the images into their individual series… t1, t2 etc and see if that works, but a link to a tutorial or any suggestions would be much appreciated.</p>
<p>I am very much a beginner at all this so am struggling a little bit with the language of this software. please excuse my naive questions.</p>
<p>Thanks</p>
<p>Amy</p>

---

## Post #4 by @Chris_Rorden (2019-08-16 15:53 UTC)

<p>The visible human data is not in DICOM format. It is distributes with <a href="https://www.nlm.nih.gov/research/visible/getting_data.html" rel="nofollow noopener"> “Z” compression, in the GE Signa format</a>. This format was <a href="https://www.dclunie.com/medical-image-faq/html/part4.html#ProprietaryMR" rel="nofollow noopener">proprietary</a> and pre-dates DICOM.</p>
<p>You can convert this format to NIfTI with the following steps</p>
<ul>
<li>Uncompress all of the images. From the command line, this would be <code>uncompress *.Z</code>
</li>
<li>Convert the images to NIfTI using dcm2nii (which pre-dates dcm2niix). This software was distributed with <a href="https://www.nitrc.org/projects/mricron" rel="nofollow noopener">MRIcron</a> - just get the 2016 version or earlier. The only benefit of this old software relative to dcm2niix is support for these archival proprietary formats. Be aware that the Signal format does not include much information about image spacing and orientation. Therefore, you may have to tune the resulting NIfTI header by hand.</li>
</ul>
<p>The visible human scans are very old, and you should keep your expectations realistic. While the color photographs (particularly for the female) are unique, the MRI and CT scans are obsolete. Pressing the “Download Sample Data” button in Slicer will provide you access to far better MRI and CT images.</p>

---

## Post #5 by @aimly (2019-08-17 10:57 UTC)

<p>Chris,<br>
Thank you sooo much for your super helpful reply. I didn’t realise that MRI and CT data formats had changed so much. I will definitely check out the sample data as you suggested and if I can’t find any of the areas I need, I’ll try converting the old dataset.  I’ll post a link to my project here when/if I have something interesting to show <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #6 by @lassoan (2019-10-28 21:50 UTC)

<p>What anatomy are you interested in?</p>

---

## Post #7 by @aimly (2019-10-29 12:51 UTC)

<p>I’m interested in looking at the negative spaces of our bodies and organs. The cavities within and ‘packing fascia’ between organs.<br>
I still haven’t managed to locate a free online dataset of the thorax that is good enough quality so if you know of any I’d be super grateful for a pointer.</p>
<p>Cheers</p>
<p>Amy</p>

---

## Post #8 by @pieper (2019-10-29 13:13 UTC)

<p>There are a lot of very good scans on <a href="https://www.cancerimagingarchive.net/">TCIA</a>.  Even though the folks are ill with cancer, much of rest of the anatomy is well represented.</p>

---

## Post #9 by @fedorov (2023-07-18 15:54 UTC)

<p>Visible Human is now available in DICOM format from NCI Imaging Data Commons - see announcement here: <a href="https://discourse.canceridc.dev/t/idc-july-2023-release/457" class="inline-onebox">IDC July 2023 release - Announcements - Imaging Data Commons</a>.</p>

---

## Post #10 by @Mouna_Taroua (2023-07-26 17:56 UTC)

<p>Hi Andrey, Can you please help me access the DICOM format. I have read the announcement but have hard time downloading the s5cmd. do you have detailed instruction on how to do so on windows, thank you</p>

---

## Post #11 by @curtislisle (2023-07-26 18:02 UTC)

<p>Dear Mouna,<br>
It might be that you are having trouble installing WGET on windows so you cannot then download s5cmd. Here is a page that discusses how to install the Wget program for Windows. Maybe this will help: <a href="https://www.tomshardware.com/how-to/use-wget-download-files-command-line" rel="noopener nofollow ugc">https://www.tomshardware.com/how-to/use-wget-download-files-command-line</a></p>

---

## Post #12 by @fedorov (2023-07-26 18:44 UTC)

<p><a class="mention" href="/u/mouna_taroua">@Mouna_Taroua</a> can you please let us know what exactly was the nature of the problems you had downloading the s5cmd?</p>
<p>All you have to do is open the <a href="https://github.com/peak/s5cmd">s5cmd GitHub page</a>, go to releases and download the binary for your platform, as shown in the screen demo below. What exactly is not working for you?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4437ee1e9ee0931bac9402808a26cf4646ea7784.gif" alt="2023-07-26_14-43-18" data-base62-sha1="9JuisIK9KRodVDmKphmwotuR9bu" width="619" height="318" class="animated"></p>

---

## Post #13 by @Mouna_Taroua (2023-07-28 17:09 UTC)

<p>Thank you Andrew! I am very new to this, so thank you for your patience. I did downloads the s5cmd, and run the commend  " s5cmd --no-sign-request --endpoint-url <a href="https://storage.googleapis.com" rel="noopener nofollow ugc">https://storage.googleapis.com</a> run file_manifest_gcs.s5cmd " while also downloading’s the s5cmd manifest but keep getting nothing back. I am not really sure what I am doing wrong</p>

---

## Post #14 by @fedorov (2023-07-28 17:28 UTC)

<p>I understand, and I do want to say that on my side, I greatly appreciate it that you were not afraid to ask these questions and seek help! I most definitely do want to help you resolve issues and make sure you can download the dataset!</p>
<p>Few questions:</p>
<ol>
<li>How did you create the manifest? Did you confirm it is not empty?</li>
<li>Since you use Windows - what kind of terminal / command line application do you use?</li>
</ol>
<p>At least in the past, my experience was that Windows had very sluggish support of the terminal, and console output produced by a command line tool would not (or would not always) show up in the console. The entire VHD is quite large (nearly 300 GB!), and may take a while to download even on a fast network. It might be that it is actually being downloaded, but you do not see any progress messages in the terminal because those do not show up on Windows.</p>
<p>To confirm that s5cmd works, you can run this test command (as listed in the IDC documentation here: <a href="https://learn.canceridc.dev/data/downloading-data#step-2-download-the-files-defined-by-the-manifest" class="inline-onebox">Downloading data - IDC User Guide</a>) and, assuming it completes without errors, check that you see file named <code>902b4588-6f10-4342-9c80-f1054e67ee83.dcm</code> with non-zero size.</p>
<pre><code class="lang-shell">s5cmd --no-sign-request --endpoint-url https://storage.googleapis.com cp s3://public-datasets-idc/cdac3f73-4fc9-4e0d-913b-b64aa3100977/902b4588-6f10-4342-9c80-f1054e67ee83.dcm .
</code></pre>

---

## Post #15 by @Mouna_Taroua (2023-07-28 21:37 UTC)

<p>I really appreciate your time! These are the steps I have done :<br>
I downloaded the s5cmd_manifest through the IDC page by selecting GCP - data storage and egress sponsored by Google Public Data Program option, and it has several datasets.<br>
The s5cmd is downloaded and compatible with my operating system. However when I run it, nothing is displayed. is it normal?<br>
then I go to the windows command prompt and type "s5cmd --no-sign-request --endpoint-url <a href="https://storage.googleapis.com/" rel="noopener nofollow ugc">https://storage.googleapis.com</a> run file_manifest_gcs.s5cmd " and get the following message</p>
<p><strong>‘s5cmd’ is not recognized as an internal or external command, operable program or batch file.</strong></p>
<p>I followed the same steps on a mac and it giving me the same error</p>

---

## Post #16 by @fedorov (2023-07-28 21:48 UTC)

<aside class="quote no-group" data-username="Mouna_Taroua" data-post="15" data-topic="8034">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mouna_taroua/48/66984_2.png" class="avatar"> Mouna_Taroua:</div>
<blockquote>
<p>I downloaded the s5cmd_manifest through the IDC page by selecting GCP - data storage and egress sponsored by Google Public Data Program option, and it has several datasets.</p>
</blockquote>
</aside>
<p>Sorry, I don’t understand what you did exactly. Can you maybe add links and more details? I still do not know what you downloaded exactly…</p>
<aside class="quote no-group" data-username="Mouna_Taroua" data-post="15" data-topic="8034">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mouna_taroua/48/66984_2.png" class="avatar"> Mouna_Taroua:</div>
<blockquote>
<p><strong>‘s5cmd’ is not recognized as an internal or external command, operable program or batch file.</strong></p>
</blockquote>
</aside>
<p>You will need to specify full path to the <code>s5cmd</code> executable, since it will not be in your system path automatically. You can do this by selecting <code>s5cmd</code> executable in the terminal as shown in the image below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38d60c4350bf07146568f3488b956e05815cdaab.jpeg" data-download-href="/uploads/short-url/86NkHmiJCJ3itLsZKdsqe5ovHLR.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38d60c4350bf07146568f3488b956e05815cdaab_2_603x500.jpeg" alt="image" data-base62-sha1="86NkHmiJCJ3itLsZKdsqe5ovHLR" width="603" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38d60c4350bf07146568f3488b956e05815cdaab_2_603x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38d60c4350bf07146568f3488b956e05815cdaab_2_904x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38d60c4350bf07146568f3488b956e05815cdaab.jpeg 2x" data-dominant-color="F3F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×820 88.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
