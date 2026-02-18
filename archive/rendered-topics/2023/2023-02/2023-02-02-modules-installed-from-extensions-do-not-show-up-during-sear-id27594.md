# Modules installed from extensions do not show up during search

**Topic ID**: 27594
**Date**: 2023-02-02
**URL**: https://discourse.slicer.org/t/modules-installed-from-extensions-do-not-show-up-during-search/27594

---

## Post #1 by @sm-philips (2023-02-02 00:48 UTC)

<p>Operating system: Windows 10<br>
Slicer version: Slicer 5.3.0 and 5.2.1<br>
Expected behavior: Installed extension should show up when I search for modules after Slicer restart<br>
Actual behavior: I cannot use online extension installer due to corporate network. So when using the offline installer, the restart button stays grayed-out. When I manually restart, the extension manager says the modules are installed, but when I search for them, they do not show up. I have tried this on both the stable release and the preview release, with no success. I know some modules wont show up during search, but the ones I am using (IGT modules), do specifically show up.</p>
<p>Any help would be highly appreciated!</p>

---

## Post #2 by @lassoan (2023-02-02 01:02 UTC)

<p>What you describe indicates that the extension package you were trying to install did not match your Slicer version. If you open the Extensions Catalog website from the the Extensions Manager in Slicer then it will show the extension packages that match your Slicer version:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/607e34cad6d9c11fc2bbe2a246b4be697f2097b5.png" data-download-href="/uploads/short-url/dLCeqF4Blz413OULXFqgSTlTHZb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/607e34cad6d9c11fc2bbe2a246b4be697f2097b5_2_690x232.png" alt="image" data-base62-sha1="dLCeqF4Blz413OULXFqgSTlTHZb" width="690" height="232" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/607e34cad6d9c11fc2bbe2a246b4be697f2097b5_2_690x232.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/607e34cad6d9c11fc2bbe2a246b4be697f2097b5_2_1035x348.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/607e34cad6d9c11fc2bbe2a246b4be697f2097b5.png 2x" data-dominant-color="414345"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1245×420 28.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @jamesobutler (2023-02-02 03:00 UTC)

<p>Yes, your extension zip file has a revision number such as 31317 which means it was built specifically for Slicer 5.2.1. Other versions can’t be installed because there could be compatibility issues.</p>

---

## Post #4 by @sm-philips (2023-02-02 19:59 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> Thank you for your replies. I did open the catalog website from the extension manager. I installed the SlicerIGT, SlicerIGSIO which are built for 5.2.1. They are still not showing up in the module menu. I also double checked if the extensions were built for 5.2.1 here (<a href="https://slicer-packages.kitware.com/#folder/637f77ce517443dc5dc72829" class="inline-onebox" rel="noopener nofollow ugc">SPKC</a>).</p>
<p>Just for curiosity, the other extensions I have installed are modelcropper, easy clip, SlicerJupyter and SlicerOpenIGTLink. None of them show up in the menu after installation.</p>

---

## Post #5 by @lassoan (2023-02-04 23:32 UTC)

<p>Is your Slicer installation folder writable?</p>

---

## Post #6 by @sm-philips (2023-02-07 21:15 UTC)

<p>Yes. I actually ended up getting admin access to the system and installed Slicer as an admin. Allowed Slicer access through the Firewall as well.</p>
<p>It still refuses to download extension directly from the extension manager (error: Failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file/637f856d517443dc5dc73f55/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file/637f856d517443dc5dc73f55/download</a>)</p>
<p>And installing from file still doesnt show the module in Slicer.</p>
<p>Edit: Python console had the following:</p>
<pre><code class="lang-auto">[Qt] Could not get the INetworkConnection instance for the adapter GUID.

[Qt] Could not get the INetworkConnection instance for the adapter GUID.

[Qt] Failed downloading: https://slicer-packages.kitware.com/api/v1/file/637f856d517443dc5dc73f55/download
</code></pre>

---

## Post #7 by @lassoan (2023-02-08 11:23 UTC)

<p>It seems that network access restrictions on your system are so strict that it becomes very difficult to access the internet. This list error indicates that the application does not even authorized to query the list of network interfaces. Try launching Slicer as an administrator. If you use some third-party security or firewall, try to add Slicer.exe and SlicerApp-real.exe to the whitelisted applications.</p>
<p>If none of these help then the easiest could be to download and install Slicer at your home computer, install all the extensions that you need, and then copy the entire Slicer installation to a USB stick. Since recent Slicer versions are fully portable, you can run it on any computer directly from the USB stick; or you can copy the entire Slicer folder to the restricted computer and run it there.</p>

---

## Post #8 by @lassoan (2023-02-08 11:37 UTC)

<p>There are also some overly aggressive antivirus systems that remove DLL and exe files after they are installed. That may be another reason why they don’t show up when you install them from a downloaded extension package. You can have a look in the NAMIC subfolder in your Slicer installation folder to see if there are any DLL or exe files after you install an extension. If there aren’t then you can try to add an exception for Slicer to allow installation of additional executables.</p>
<p>If the distrust in third-party applications is so strong in your organization then they may consider letting you installing applications on your computer in a virtual machine.</p>

---

## Post #9 by @sm-philips (2023-02-08 18:54 UTC)

<p>It was this. Antivirus was the issue. Adding exception for Slicer.exe solved the problem. Now I can install from file and work with the extensions. The internet installation is still not solved (I dont think it will be unless there is a company-wide change in policy).</p>
<p>Thank you for all the help!</p>

---

## Post #10 by @lassoan (2023-02-08 20:21 UTC)

<p>Thanks for the update. Which antivirus software caused this trouble? In the past some users had this problem with Avast.</p>

---

## Post #11 by @sm-philips (2023-02-09 18:58 UTC)

<p>They actually use Windows Defender. I had to contact IT support to add the extension. So I do not know more details about how they dealt with the exception.</p>

---
