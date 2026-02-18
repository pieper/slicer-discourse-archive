# New feature: Install modules by drag-and-drop Python files

**Topic ID**: 28311
**Date**: 2023-03-11
**URL**: https://discourse.slicer.org/t/new-feature-install-modules-by-drag-and-drop-python-files/28311

---

## Post #1 by @lassoan (2023-03-11 16:09 UTC)

<p>Until now, if developers wanted to add custom modules to Slicer, they had to open application settings, go to developer section, and append folders to the module list there.</p>
<p>Now there is <strong>a simpler way to install modules: just drag-and-drop the .py file (or parent folder) to the Slicer application screen</strong> and click OK to “Add Python scripted modules to the application”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7925a0e9454c2e36efcf9d22e4327446f78830b0.png" data-download-href="/uploads/short-url/hhIolHcsH5zpC73HePmt8RlkcsE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/7925a0e9454c2e36efcf9d22e4327446f78830b0_2_690x449.png" alt="image" data-base62-sha1="hhIolHcsH5zpC73HePmt8RlkcsE" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/7925a0e9454c2e36efcf9d22e4327446f78830b0_2_690x449.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/7925a0e9454c2e36efcf9d22e4327446f78830b0_2_1035x673.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/7925a0e9454c2e36efcf9d22e4327446f78830b0_2_1380x898.png 2x" data-dominant-color="3F3E43"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1820×1186 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then you are offered an option to select certain modules or add all the modules that are found in the folder. Modules are immediately loaded and ready to use - no need to restart Slicer (only if the module performs initializations at application startup).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a5b2eed19b1207b0ce5ec2a4322549da322fb51.png" data-download-href="/uploads/short-url/cTkkyWwEzXR0bYs5fhWJ94QRBwB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a5b2eed19b1207b0ce5ec2a4322549da322fb51_2_690x449.png" alt="image" data-base62-sha1="cTkkyWwEzXR0bYs5fhWJ94QRBwB" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a5b2eed19b1207b0ce5ec2a4322549da322fb51_2_690x449.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a5b2eed19b1207b0ce5ec2a4322549da322fb51_2_1035x673.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a5b2eed19b1207b0ce5ec2a4322549da322fb51_2_1380x898.png 2x" data-dominant-color="424146"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1820×1186 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The feature is available in latest Slicer Preview Release (Slicer-5.3 rev 31632 and later). Any comments and suggestions are welcome.</p>

---
