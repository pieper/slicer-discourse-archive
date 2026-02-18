# Installing SlicerRadiomics Extension

**Topic ID**: 41397
**Date**: 2025-01-31
**URL**: https://discourse.slicer.org/t/installing-slicerradiomics-extension/41397

---

## Post #1 by @pprior99999 (2025-01-31 11:25 UTC)

<p>Hi,</p>
<p>I’m struggling to install SlicerRadiomics extension in 3D Slicer 5.6.2 using the Extension Manager within slicer. I get the following warning, " Failed to open extensions settings file: C:/ProgramData/slicer.org/Slicer 5.6.2./bin/…/slicer.org/Slicer-32448.ini " …</p>
<p>“<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>” 0 “Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png</a>’. This content should also be served over HTTPS.”</p>
<p>I’m not sure how to get past this issue as my institution has given limited access permissions to the *.ini file. My IT group has suggested that I need to contact the “vendor” to get instructions on resolving the issue.</p>
<p>Can anyone in the Slicer community help?</p>
<p>Thanks in advance,<br>
Phil</p>

---

## Post #2 by @pieper (2025-02-27 21:44 UTC)

<p>Not sure if you figured this out already, but probably you don’t have write access to the c:/ProgramData directory.  Slicer should by default be installed in a user directory so that things like extensions can be added.  The https errors are unrelated and can be ignored.</p>

---

## Post #3 by @pprior99999 (2025-04-15 14:09 UTC)

<p>Hey Steve, I was thinking that write access was the issue.  Essentially, the issues got resolved by uninstalling and re-installing Slicer with a different IT person.</p>

---
