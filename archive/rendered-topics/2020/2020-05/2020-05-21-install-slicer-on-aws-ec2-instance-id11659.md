---
topic_id: 11659
title: "Install Slicer On Aws Ec2 Instance"
date: 2020-05-21
url: https://discourse.slicer.org/t/11659
---

# Install Slicer on AWS EC2 instance

**Topic ID**: 11659
**Date**: 2020-05-21
**URL**: https://discourse.slicer.org/t/install-slicer-on-aws-ec2-instance/11659

---

## Post #1 by @lennymartinez (2020-05-21 19:16 UTC)

<p>Anybody have experience installing Slicer on an AWS EC2 instance? I want to be able to send folders of Dicom images to be processed by a Slicer plugin (already made) in an EC2 instance but I’m not sure what the best way of going about this would be.</p>

---

## Post #2 by @pieper (2020-05-21 19:54 UTC)

<p>There some information on the page linked below about setting up on google cloud from a generic OS image.  Most would be the same on AWS.  This is kind of the manual method but I’ve also heard that amazon WorkSpaces are an easy way to get going.</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/QIICR/SlicerGCPSetup" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/5347127?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/QIICR/SlicerGCPSetup" target="_blank">QIICR/SlicerGCPSetup</a></h3>

<p>Contribute to QIICR/SlicerGCPSetup development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lennymartinez (2020-05-26 15:17 UTC)

<p>Thanks! I’m trying it out on GCP now and I’ll give it a shot to see how/if it works in both cases.</p>

---

## Post #4 by @bbkonk (2022-12-21 22:37 UTC)

<p>Hoping to revive this old thread, has anyone had any success running slicer on an EC2? I’m trying to configure an EC2 to support slicer but hitting issues with graphics support.</p>

---

## Post #5 by @pieper (2022-12-21 22:42 UTC)

<p>Yes, I run Slicer on EC2 all the time, very similar to the GCP setup described in the link above, or <a href="https://learn.canceridc.dev/cookbook/virtual-machines/idc-desktop">at this newer document</a>.  Note that you do need to have a quota approved in order to use a GPU with your instance if you want to use windows.  Linux can use GPU but can also <a href="https://github.com/ImagingDataCommons/IDC-Docs/pull/48/files">be used without GPU</a> if that suits your needs better.</p>
<p>EC2 also offers <a href="https://aws.amazon.com/appstream2/">AppStream</a>, which is also good if you plan to use it a lot.</p>

---

## Post #6 by @bbkonk (2022-12-21 23:04 UTC)

<p>Thanks for the quick reply! I’m currently running Windows on a g4 instance (g4dn.xl). I’m somewhat new to AWS, are quotas necessary if I’m not running elastic gpu?</p>
<p>Did you have to do any configuration within the Windows environment to allow Slicer to run?<br>
(I’ve spun up an AMI that isn’t really optimized for GPU (I’m limited in what I’m allowed to use in my current environment), installed what should be the compatible CUDA (11.7), disabled the built-in display in Device Manager and installed Media Foundation and Quality Windows Audio Video Experience. I’m seeing the Tesla GPU under Device Manager display options and with nvidia-smi.)</p>

---

## Post #7 by @pieper (2022-12-21 23:18 UTC)

<p>From what you describe I think it should work.  You might be hitting an issue with RDP (e.g. <a href="https://discourse.slicer.org/t/starting-error-in-windows-computer-showing-insufficient-graphics-capability/9569">this</a>), so trying an alternative like Chrome Remote Desktop or <a href="https://aws.amazon.com/hpc/dcv/">NICE DCV</a> could help.  I don’t usually use windows much so I can’t say for sure.  <a class="mention" href="/u/rbumm">@rbumm</a> has been trying to set up something like this too, so maybe tomorrow he can chime in with his experience since he was apparently hitting quota issues.</p>

---

## Post #8 by @bbkonk (2022-12-22 13:56 UTC)

<p>Thank you. I noticed that recommendation in another thread, but unfortunately in our case we can only use Remote Desktop Connection as other methods are currently unapproved.</p>

---

## Post #9 by @bbkonk (2022-12-27 15:13 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> I’d love to hear about your experience with this!</p>

---

## Post #10 by @rbumm (2022-12-27 15:43 UTC)

<p><a class="mention" href="/u/bbkonk">@bbkonk</a> will report progress, plus we have set up a project at the upcoming Project Week where we will document the workflow.</p>

---

## Post #11 by @rbumm (2023-01-10 10:13 UTC)

<p>We make good progress in setting up AWS Windows EC2 instances with GPU support.<br>
The <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerCloud/#readme">workflow is documented here</a> and will be a project of the upcoming 38th NA-MIC Project Week. Setting up a g5.xlarge instance takes around 20-30 min (unattended) and another 10 minutes to install 3D Slicer and extensions. Performance is great. You can stop and start the instance on demand.</p>
<p>The main hurdle is to let your local Amazon representative increase the instance_type “G and VT”  limit  to 8 vCPUs</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f48fec4ff6c31df249cf1e5f5717f5a1613f06bf.png" data-download-href="/uploads/short-url/yTuR6LtZrhMcN3mTCH1ubWjKLfx.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f48fec4ff6c31df249cf1e5f5717f5a1613f06bf_2_690x21.png" alt="image" data-base62-sha1="yTuR6LtZrhMcN3mTCH1ubWjKLfx" width="690" height="21" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f48fec4ff6c31df249cf1e5f5717f5a1613f06bf_2_690x21.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f48fec4ff6c31df249cf1e5f5717f5a1613f06bf_2_1035x31.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f48fec4ff6c31df249cf1e5f5717f5a1613f06bf_2_1380x42.png 2x" data-dominant-color="F4F4F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1388×43 4.57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>which is at 0 vCPUs by default in a private AWS account (for safety reasons).</p>

---
