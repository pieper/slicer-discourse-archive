---
topic_id: 23580
title: "Completed With Errors"
date: 2022-05-25
url: https://discourse.slicer.org/t/23580
---

# Completed with errors 

**Topic ID**: 23580
**Date**: 2022-05-25
**URL**: https://discourse.slicer.org/t/completed-with-errors/23580

---

## Post #1 by @maria_2000 (2022-05-25 03:33 UTC)

<p>Hi.When I use the Matlab Module Generator I’m facing with these errors. How can I solve these errors?</p>
<p>ERROR: Unable to find Matlab executable defined in the SLICER_MATLAB_EXECUTABLE_PATH environment variable: 0</p>
<p>ERROR: Failed to start Matlab process</p>
<p>ERROR: Cannot connect to the server<br>
(Version:4.11)<br>
(Windows 10)</p>

---

## Post #2 by @lassoan (2022-05-25 03:55 UTC)

<p>It means that Matlab executable is not found. Have you specified it in “Matlab module generator” module?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/537b01571e3671af3b7fef86fd40925fd8e04d4e.png" data-download-href="/uploads/short-url/bUvao3D2hvHcjUXwLzkqdmC6UIm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/537b01571e3671af3b7fef86fd40925fd8e04d4e_2_690x426.png" alt="image" data-base62-sha1="bUvao3D2hvHcjUXwLzkqdmC6UIm" width="690" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/537b01571e3671af3b7fef86fd40925fd8e04d4e_2_690x426.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/537b01571e3671af3b7fef86fd40925fd8e04d4e_2_1035x639.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/537b01571e3671af3b7fef86fd40925fd8e04d4e_2_1380x852.png 2x" data-dominant-color="545565"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1467×906 73.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>That said, i haven’t tested the extension for a good while now. The extension was created about 10 years ago, when Matlab was still very widely used and Python was not yet that popular. Things have changed a lot since then so despite some advantages of Matlab (more consistent style, maturity, and documentation across all packages), Python is a much more favorable ecosystem overall. I would recommend switching to Python instead of investing any time into developing or troubleshooting Matlab-based solutions.</p>

---

## Post #3 by @maria_2000 (2022-05-25 08:59 UTC)

<p>Thank you so much for the detailed explanation.</p>

---
