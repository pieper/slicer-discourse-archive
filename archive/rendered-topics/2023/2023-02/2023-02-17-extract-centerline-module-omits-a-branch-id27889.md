---
topic_id: 27889
title: "Extract Centerline Module Omits A Branch"
date: 2023-02-17
url: https://discourse.slicer.org/t/27889
---

# Extract Centerline module omits a branch

**Topic ID**: 27889
**Date**: 2023-02-17
**URL**: https://discourse.slicer.org/t/extract-centerline-module-omits-a-branch/27889

---

## Post #1 by @mikebind (2023-02-17 20:49 UTC)

<p>I have a surface model of an airway including the trachea and two bronchi.  When I use the ExtractCenterline module with three endpoints (near the superior end of the trachea and near the ends of the bronchi) with the superior point marked as the “inlet”, I get two curves created as centerline curves, from the trachea to the branch point, and from the branch point down one of the bronchi.  These two curves are named “Centerline curve (0)” and “Centerline curve (2)”.  There is no “Centerline curve (1)”.  I suspect there might be some sort of bug somewhere because which bronchus the centerline curve goes down depends on the order of the endpoints in the “Endpoints” MarkupsPointList. Also, if I mark the right bronchus endpoint as the ‘inlet’, then I get a set of 3 centerline curves (right bronchus to branch point, branch point to left bronchus, and branch point to trachea), with curve (0), (1), and (2) all created.  As I was troubleshooting, I moved the brochus endpoints so that they sit on the voronoi surface to eliminate the possible issue that it couldn’t find a path to the endpoint.</p>
<p>If anyone is willing to take a look at this, the surface model is here: <a href="https://www.dropbox.com/s/ewvg138dwna9tps/Preprocessedmodel.vtk?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - Preprocessedmodel.vtk - Simplify your life</a> and the endpoints are here: <a href="https://www.dropbox.com/s/k3yd6w29jccqytm/BronchiStoma.mrk.json?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - BronchiStoma.mrk.json - Simplify your life</a></p>
<p>Just load both of those, and try to run “Extract Centerline” with the preprocessed model as the input surface, the BronchiStoma points as the endpoints, and with a “Centerline curve” output selected.  It’s fine to uncheck “Preprocess input surface” in the Advanced section because the input surface is already preprocessed.</p>
<p>Also, as additional information, if a “Centerline model” output is selected (in addition to the “Centerline curve” output), the generated centerline model has both branches included, but doesn’t work well for my purposes because it is not divided into segments the way the centerline curves are.</p>
<p>Thanks very much for any help you can provide!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/383e6e1901faf40af77490f24f49c2feddc13589.png" alt="image" data-base62-sha1="81yuDw5wStIvJsse92llz2fFyCB" width="485" height="477"><br>
Missing branch which goes to RightBronch!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db68a30d24c13c71f9edce6197015fca2c2796d4.jpeg" data-download-href="/uploads/short-url/viYKtrffC28b8LijQ3e3aqpUybi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db68a30d24c13c71f9edce6197015fca2c2796d4.jpeg" alt="image" data-base62-sha1="viYKtrffC28b8LijQ3e3aqpUybi" width="690" height="491" data-dominant-color="A09FBB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">735×524 52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
With surface shown.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dea34d72177639d2376973a69b7d75ddb04f2df.png" data-download-href="/uploads/short-url/b7gy6JsFzJyj0qMeE3Az6FHFidF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dea34d72177639d2376973a69b7d75ddb04f2df_2_690x491.png" alt="image" data-base62-sha1="b7gy6JsFzJyj0qMeE3Az6FHFidF" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dea34d72177639d2376973a69b7d75ddb04f2df_2_690x491.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dea34d72177639d2376973a69b7d75ddb04f2df.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dea34d72177639d2376973a69b7d75ddb04f2df.png 2x" data-dominant-color="A09FBB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">741×528 95 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
With “centerline model” shown in green. Centerline model has both branches, but centerline curves omit the right branch.</p>
<p>I am using Slicer 5.2.1 on Windows 10.</p>

---
