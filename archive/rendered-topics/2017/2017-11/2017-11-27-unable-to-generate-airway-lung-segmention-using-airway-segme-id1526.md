# Unable to generate airway lung segmention using Airway Segmentation Module

**Topic ID**: 1526
**Date**: 2017-11-27
**URL**: https://discourse.slicer.org/t/unable-to-generate-airway-lung-segmention-using-airway-segmentation-module/1526

---

## Post #1 by @ashlyshaji (2017-11-27 14:13 UTC)

<p>Hello,<br>
I am new to 3d slicer . I tried to generate airway segment from CT DICOM images using Airway Segmentation Module . But only the location of seed point is getting generated in 3d viewer, instead of  the whole airway.<br>
I have attached the screenshot ,showing the output and also the parameters I have given.<br>
Could anyone advice me on this issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6470b6ff6c8e6c36299ad37f21264194bf062dc8.png" data-download-href="/uploads/short-url/ekxeIOzDZ5ADw9OyTxtFR7IHCoo.png?dl=1" title="screenshot_slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6470b6ff6c8e6c36299ad37f21264194bf062dc8_2_690x365.png" alt="screenshot_slicer" data-base62-sha1="ekxeIOzDZ5ADw9OyTxtFR7IHCoo" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6470b6ff6c8e6c36299ad37f21264194bf062dc8_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6470b6ff6c8e6c36299ad37f21264194bf062dc8_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6470b6ff6c8e6c36299ad37f21264194bf062dc8.png 2x" data-dominant-color="93959D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot_slicer</span><span class="informations">1361×721 251 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jcfr (2017-11-27 14:16 UTC)

<p>Hi <a class="mention" href="/u/ashlyshaji">@ashlyshaji</a>,</p>
<p>Thanks for you report.</p>
<p>To better understand the problem, I suggest you also include the content of the error log as well as a link to the corresponding data.</p>
<p>Reading this guide can also be useful: <a href="https://www.slicer.org/wiki/Documentation/4.8/Report_a_problem">https://www.slicer.org/wiki/Documentation/4.8/Report_a_problem</a></p>

---

## Post #3 by @ashlyshaji (2017-11-28 13:59 UTC)

<p>Hello,</p>
<p>I have attached the error log with this mail.</p>
<p>Regards</p>
<p>Ashly</p>

---

## Post #4 by @ashlyshaji (2017-11-28 14:19 UTC)

<p>I also used another set of DICOM files ,downloaded from below  link.<br>
tar.gz</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?dsh=S-1677424281%3A1679384770626041&amp;continue=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D0B12TS1PH6H6QMDRFOEtSWWY3dmc&amp;followup=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D0B12TS1PH6H6QMDRFOEtSWWY3dmc&amp;ifkv=AWnogHcF_dPxtuR-Q1cmvFi1fvtYTS5kI8r5qpn5glQHrcqYbU2nKTh4jfQXWopugN35t71dOQKoVQ&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?dsh=S-1677424281%3A1679384770626041&amp;continue=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D0B12TS1PH6H6QMDRFOEtSWWY3dmc&amp;followup=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D0B12TS1PH6H6QMDRFOEtSWWY3dmc&amp;ifkv=AWnogHcF_dPxtuR-Q1cmvFi1fvtYTS5kI8r5qpn5glQHrcqYbU2nKTh4jfQXWopugN35t71dOQKoVQ&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?dsh=S-1677424281%3A1679384770626041&amp;continue=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D0B12TS1PH6H6QMDRFOEtSWWY3dmc&amp;followup=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D0B12TS1PH6H6QMDRFOEtSWWY3dmc&amp;ifkv=AWnogHcF_dPxtuR-Q1cmvFi1fvtYTS5kI8r5qpn5glQHrcqYbU2nKTh4jfQXWopugN35t71dOQKoVQ&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>.zip</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?dsh=S1141585324%3A1679384771146550&amp;continue=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D0B12TS1PH6H6QY0d2cmEtSVJ0aFE&amp;followup=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D0B12TS1PH6H6QY0d2cmEtSVJ0aFE&amp;ifkv=AWnogHe22L12AMHLt9fJyMgyMFVyzM_-oKUVokyWBh_Ivi1IwBKXeV3boNbFXqBgmIPktTu4sstv&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?dsh=S1141585324%3A1679384771146550&amp;continue=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D0B12TS1PH6H6QY0d2cmEtSVJ0aFE&amp;followup=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D0B12TS1PH6H6QY0d2cmEtSVJ0aFE&amp;ifkv=AWnogHe22L12AMHLt9fJyMgyMFVyzM_-oKUVokyWBh_Ivi1IwBKXeV3boNbFXqBgmIPktTu4sstv&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?dsh=S1141585324%3A1679384771146550&amp;continue=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D0B12TS1PH6H6QY0d2cmEtSVJ0aFE&amp;followup=https%3A%2F%2Fdrive.google.com%2Fopen%3Fid%3D0B12TS1PH6H6QY0d2cmEtSVJ0aFE&amp;ifkv=AWnogHe22L12AMHLt9fJyMgyMFVyzM_-oKUVokyWBh_Ivi1IwBKXeV3boNbFXqBgmIPktTu4sstv&amp;osid=1&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>But still ,its not working .</p>
<p>Regards</p>
<p>Ashly</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/54d222605eb32edb203273415965d9a2c3da12ad.jpg" data-download-href="/uploads/short-url/c6mjIWj2Hfpo5wL7b3oSk4jeSn3.jpg?dl=1" title="screenshot1.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/54d222605eb32edb203273415965d9a2c3da12ad_2_690x367.jpg" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/54d222605eb32edb203273415965d9a2c3da12ad_2_690x367.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/54d222605eb32edb203273415965d9a2c3da12ad_2_1035x550.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54d222605eb32edb203273415965d9a2c3da12ad.jpeg 2x" data-dominant-color="ACAFC5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot1.jpg</span><span class="informations">1365×727 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
