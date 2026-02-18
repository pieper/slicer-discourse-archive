# Extension contribution checklist

**Topic ID**: 4975
**Date**: 2018-12-05
**URL**: https://discourse.slicer.org/t/extension-contribution-checklist/4975

---

## Post #1 by @jcfr (2018-12-05 18:18 UTC)

<h3><a name="p-18535-extension-repository-name-1" class="anchor" href="#p-18535-extension-repository-name-1" aria-label="Heading link"></a>extension repository name</h3>
<p>Earlier today, following the submission of  a <a href="https://github.com/Slicer/ExtensionsIndex/pull/1597">pull request</a> adding a new extension to the Extension index, the associated test failed:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15a4b0bc0bbe4277a97d5a58db575c23ea3dc394.png" data-download-href="/uploads/short-url/35sSd4u2mBhqyEl85ycjyWGpLCc.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15a4b0bc0bbe4277a97d5a58db575c23ea3dc394.png" alt="image" data-base62-sha1="35sSd4u2mBhqyEl85ycjyWGpLCc" width="528" height="214"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">528×214 15.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>with the following message:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7d12506f40ee4f491e71cbb8f20c31a7ff1f332.png" data-download-href="/uploads/short-url/x4KnVKRztZRaZfatUTc2MgfApB8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7d12506f40ee4f491e71cbb8f20c31a7ff1f332_2_690x69.png" alt="image" data-base62-sha1="x4KnVKRztZRaZfatUTc2MgfApB8" width="690" height="69" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7d12506f40ee4f491e71cbb8f20c31a7ff1f332_2_690x69.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7d12506f40ee4f491e71cbb8f20c31a7ff1f332_2_1035x103.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7d12506f40ee4f491e71cbb8f20c31a7ff1f332_2_1380x138.png 2x" data-dominant-color="2B2B2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1418×143 14.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> .</p>
<p>Following <a href="https://github.com/Slicer/ExtensionsIndex/pull/1597#issuecomment-444535467">input</a> from <a class="mention" href="/u/fedorov">@fedorov</a>  , we tweaked the wording to mention that using the <code>Slicer</code> prefix was recommended but not mandatory. See <a href="https://github.com/Slicer/ExtensionsIndex/pull/1600">update</a> to the ci script and wiki.</p>
<h3><a name="p-18535-contribution-checklist-improvement-2" class="anchor" href="#p-18535-contribution-checklist-improvement-2" aria-label="Heading link"></a>contribution checklist improvement</h3>
<p>The checklist documented in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions#Contribution_Checklist">Step-by-step: How to create, publish, distribute and maintain an extension ?</a> guide has also been updated and is now in markdown format ready to be copied into new pull request. This should help extension index reviewer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f8336708a5c18f02d1bc605ba8d900a6ae0633b.png" data-download-href="/uploads/short-url/mL72shZzQQHfQB3xaR6ElMT0DsD.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f8336708a5c18f02d1bc605ba8d900a6ae0633b.png" alt="image" data-base62-sha1="mL72shZzQQHfQB3xaR6ElMT0DsD" width="644" height="147"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">644×147 6.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @brhoom (2018-12-06 17:59 UTC)

<p>Thanks for your effort.</p>
<p>I don’t know why <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerCochlea" rel="nofollow noopener">my modules tests always fail</a>?</p>
<p>The module download elastix binaries from our server and use them in its logic class. Is there anything I should to make things work? I run the testing in differentWindow and Ubuntu  machines and it works. The extension does not support Mac for now but mac users are welcome to modify it and I can help in this if needed (I don’t have mac).</p>

---

## Post #3 by @lassoan (2018-12-06 23:14 UTC)

<p>If you need Elastix, please do not download binaries from your own server. Instead, add SlicerElastix to EXTENSION_DEPENDS in your CMakeLists.txt file. When you install your extension, the extension manager will also install SlicerElastix extension, which has all the Elastix binaries on all platforms (including MacOS) and compatible with Slicer (uses Slicer’s ITK). Using the proper binaries might also fix your module tests.</p>

---

## Post #4 by @brhoom (2018-12-07 07:54 UTC)

<p>Thanks for the info. I will try that.</p>

---
