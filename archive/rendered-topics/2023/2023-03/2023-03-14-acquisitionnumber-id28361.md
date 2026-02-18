# acquisitionNumber

**Topic ID**: 28361
**Date**: 2023-03-14
**URL**: https://discourse.slicer.org/t/acquisitionnumber/28361

---

## Post #1 by @analubonaldo (2023-03-14 00:00 UTC)

<p>Hi!</p>
<p>I’m trying to import a CT scan using the DICOM browser in Slicer 5.3.0. For some patients, instead of opening all slices, they only open a few with the additional name “acquisitionNumber”. Consequently, I lose most of the original cuts.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3182d3ef2eeb63e3b11c143d0ba99772f9ec50d.jpeg" data-download-href="/uploads/short-url/pylgt7CQyt4YGdKsjJvSAK3yAFL.jpeg?dl=1" title="WhatsApp Image 2023-03-13 at 3.21.05 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3182d3ef2eeb63e3b11c143d0ba99772f9ec50d_2_690x490.jpeg" alt="WhatsApp Image 2023-03-13 at 3.21.05 PM" data-base62-sha1="pylgt7CQyt4YGdKsjJvSAK3yAFL" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3182d3ef2eeb63e3b11c143d0ba99772f9ec50d_2_690x490.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3182d3ef2eeb63e3b11c143d0ba99772f9ec50d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3182d3ef2eeb63e3b11c143d0ba99772f9ec50d.jpeg 2x" data-dominant-color="242222"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2023-03-13 at 3.21.05 PM</span><span class="informations">905×643 75.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbfa873d938514c554e75e3fb26cf75dff5b8631.jpeg" data-download-href="/uploads/short-url/qOW2yVNiWDnXY1x2biTrCNwLh29.jpeg?dl=1" title="WhatsApp Image 2023-03-13 at 3.22.38 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbfa873d938514c554e75e3fb26cf75dff5b8631_2_690x487.jpeg" alt="WhatsApp Image 2023-03-13 at 3.22.38 PM" data-base62-sha1="qOW2yVNiWDnXY1x2biTrCNwLh29" width="690" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbfa873d938514c554e75e3fb26cf75dff5b8631_2_690x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbfa873d938514c554e75e3fb26cf75dff5b8631.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbfa873d938514c554e75e3fb26cf75dff5b8631.jpeg 2x" data-dominant-color="2C3339"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2023-03-13 at 3.22.38 PM</span><span class="informations">918×648 63.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I upload these studies completely? With all the slices so I can analyze them?</p>
<p>Thanks for the help!</p>

---

## Post #2 by @pieper (2023-03-14 15:06 UTC)

<p>This happens when the CT captured differently as the body moves through the scanner, e.g. the speed of the table may change and the slice spacing is different for different parts.  This may be done to minimize radiation exposure or capture more resolution in specific parts.</p>
<p>By default Slicer tries to load sensible pieces of the scan that map to volumes.  But you can override this by going into Advanced mode, running Examine, and picking the Scalar Volume option:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09a65da19ea7029b5a5ab63a6acfc4817d35e6b1.png" data-download-href="/uploads/short-url/1nmJwhlK3QzHnaE15fSqQk56S0V.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09a65da19ea7029b5a5ab63a6acfc4817d35e6b1_2_690x253.png" alt="image" data-base62-sha1="1nmJwhlK3QzHnaE15fSqQk56S0V" width="690" height="253" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09a65da19ea7029b5a5ab63a6acfc4817d35e6b1_2_690x253.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09a65da19ea7029b5a5ab63a6acfc4817d35e6b1_2_1035x379.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09a65da19ea7029b5a5ab63a6acfc4817d35e6b1.png 2x" data-dominant-color="F2F2F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1175×431 18.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Since the slice spacing varies, Slicer creates <a href="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0">a transform</a> to regularize the spacing.</p>
<p>You can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">Harden</a> this transform, which will create a regularly spaced volume for this data.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe6892e5a4d746191122593784f7ee29fe6e887e.jpeg" data-download-href="/uploads/short-url/AiBkcCed3L88qJkHx0Lfa4IBw7Q.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe6892e5a4d746191122593784f7ee29fe6e887e_2_690x353.jpeg" alt="image" data-base62-sha1="AiBkcCed3L88qJkHx0Lfa4IBw7Q" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe6892e5a4d746191122593784f7ee29fe6e887e_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe6892e5a4d746191122593784f7ee29fe6e887e_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe6892e5a4d746191122593784f7ee29fe6e887e_2_1380x706.jpeg 2x" data-dominant-color="8C8B8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×981 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>p.s. thanks for including the TCGA ID for this case in your screenshots.  For reference, I was able to get a copy from the <a href="https://portal.imaging.datacommons.cancer.gov/">Imaging Data Commons</a> by getting the download URLs from the BigQuery console with this:</p>
<pre><code class="lang-auto">SELECT gcs_url FROM `bigquery-public-data.idc_current.dicom_all` WHERE PatientID = "TCGA-13-0799" LIMIT 100000
</code></pre>
<p>After downloading the results as tcga.csv, I could download them to a local folder with this command:</p>
<pre><code class="lang-auto">tail -n +2 ../tcga.csv | gsutil -m cp -I .
</code></pre>

---
