---
topic_id: 40907
title: "Install Extension From Slicer Gui"
date: 2024-12-30
url: https://discourse.slicer.org/t/40907
---

# install extension from Slicer GUI

**Topic ID**: 40907
**Date**: 2024-12-30
**URL**: https://discourse.slicer.org/t/install-extension-from-slicer-gui/40907

---

## Post #1 by @danieldeidda (2024-12-30 16:22 UTC)

<p>Hi,<br>
I would like to use Slicer for brain segmentation of MR images I have installed Slicer stable version following the guidance. I run slicer GUI from Ubuntu 22 and click on “install extensions” I have tried many extensions but I always get the same error:</p>
<p>Retrieving extension metadata for PyTorch extension<br>
Retrieving PyTorch extension files (extensionId: 660f9f7930e435b0e355f56a)<br>
Downloading PyTorch extension (item_id: 660f9f7930e435b0e355f56a, file_id: 662a183e6a328ae4b08b3c12)<br>
Failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file/662a183e6a328ae4b08b3c12/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file/662a183e6a328ae4b08b3c12/download</a></p>
<p>Note that I manage to install some extension from file like Monai auto3d seg however when I want to use it for segmentation I get:<br>
<em>Failed to install required dependencies.</em></p>
<p><em>This module requires PyTorch extension. Install it from the Extensions Manager.</em></p>
<p>and I have again the installeation problem</p>

---

## Post #2 by @mau_igna_06 (2024-12-30 23:41 UTC)

<p>Could you try installing PyTorch extension through file installation method? I could download successfully from the link you posted, maybe try using a VPN?</p>
<p>After you install PyTorch extension, please try this:</p><aside class="quote quote-modified" data-post="2" data-topic="40866">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/why-can-not-use-dental-segmentator/40866/2">Why can not use dental segmentator?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Please: 


Restart the program 


Click this button 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9b235a3cd8f0f14afc671356beb8e50b30f820b.png" data-download-href="/uploads/short-url/odcvhVFYu2fbBXYySjZD7ZMucxJ.png?dl=1" title="0d41d64bac41f6e510654ab0aeb88bf871584ee0_2" rel="noopener nofollow ugc">[0d41d64bac41f6e510654ab0aeb88bf871584ee0_2]</a> 


Click this button 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d8b390ac1f1b0ba2b7ce127db1ccfa1fa5ba2ba.png" data-download-href="/uploads/short-url/4dm84kMIPQXILY1ya9BAZoVX7DQ.png?dl=1" title="0d41d64bac41f6e510654ab0aeb88bf871584ee0_3" rel="noopener nofollow ugc">[0d41d64bac41f6e510654ab0aeb88bf871584ee0_3]</a> 


Try to use Dental Segmentator 


Report if it still does not work (and add logs or a picture of the problem)
  </blockquote>
</aside>


---

## Post #3 by @danieldeidda (2025-01-02 16:11 UTC)

<p>Hi,<br>
thanks! this seems to have worked  though I noticed a few SSLCertificate errors during the  installation of Pytorch. I then tried MNAI Auto3DSeg and I get the following error when running the segmentation:</p>
<p>HTTPSConnectionPool(host=‘<a href="http://objects.githubusercontent.com" rel="noopener nofollow ugc">objects.githubusercontent.com</a>’, port=443): Max retries exceeded with url: /github-production-release-asset-2e65be/744050756/0ca59c89-8633-497e-92d4-6eb374333a50?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=releaseassetproduction%2F20250102%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20250102T160758Z&amp;X-Amz-Expires=300&amp;X-Amz-Signature=6b52fb925d49e2a03099a690856ac1bb1ec7833d9faf2a613c741bec97a3b822&amp;X-Amz-SignedHeaders=host&amp;response-content-disposition=attachment%3B%20filename%3Danatomy_and_icrh-v1.0.1.zip&amp;response-content-type=application%2Foctet-stream (Caused by SSLError(SSLCertVerificationError(1, ‘[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1129)’)))</p>

---
