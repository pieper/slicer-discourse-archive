# Film Dosimetry missing table

**Topic ID**: 15479
**Date**: 2021-01-12
**URL**: https://discourse.slicer.org/t/film-dosimetry-missing-table/15479

---

## Post #1 by @Michael_Costello (2021-01-12 19:12 UTC)

<p>I am attempting to use the SlicerRT and Film Dosimetry extensions to perform gamma analysis. However, I am unable to input any values to the plot. I have selected the films to be used for calibration and input the dose to each film. The next step should be selecting an ROI on each film that matches the appropriate recorded dose. Then the table of those values could be used to generate a plot. The program is not allowing me to either manually record or have the software record the mean of any ROIs added to the films. They just seem to exist without having any utility. Is there a simple step I’m missing? It feels like there is a button missing from the program which would open such a table as I’m describing. Any help would be greatly appreciated. Attached are steps 1.1 and 1.2 of the film calibration slicelet. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e23dd134f5845ce762c4baefbda41b0beb61a96.jpeg" data-download-href="/uploads/short-url/myYhdqOh9C8xpK00XCRvGjQJZhc.jpeg?dl=1" title="Slicer Film Dosimetry Error1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e23dd134f5845ce762c4baefbda41b0beb61a96_2_681x500.jpeg" alt="Slicer Film Dosimetry Error1" data-base62-sha1="myYhdqOh9C8xpK00XCRvGjQJZhc" width="681" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e23dd134f5845ce762c4baefbda41b0beb61a96_2_681x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e23dd134f5845ce762c4baefbda41b0beb61a96_2_1021x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e23dd134f5845ce762c4baefbda41b0beb61a96.jpeg 2x" data-dominant-color="7E8287"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer Film Dosimetry Error1</span><span class="informations">1205×884 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/800ad3b36355c361c56198eab96d1b5a73094a10.jpeg" data-download-href="/uploads/short-url/igIjoEbmADRvlC6YsaTXHeauRW0.jpeg?dl=1" title="Slicer Film Dosimetry Error2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/800ad3b36355c361c56198eab96d1b5a73094a10_2_682x500.jpeg" alt="Slicer Film Dosimetry Error2" data-base62-sha1="igIjoEbmADRvlC6YsaTXHeauRW0" width="682" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/800ad3b36355c361c56198eab96d1b5a73094a10_2_682x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/800ad3b36355c361c56198eab96d1b5a73094a10_2_1023x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/800ad3b36355c361c56198eab96d1b5a73094a10.jpeg 2x" data-dominant-color="82868B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer Film Dosimetry Error2</span><span class="informations">1200×879 74.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2021-01-13 12:07 UTC)

<p>The ROIs are used to calculate the calibration function and are definitely not without function.</p>
<p>I suggest reading <a href="https://www.researchgate.net/publication/317352557_Development_of_3D_Slicer_based_film_dosimetry_analysis">this paper</a> and and taking a look at <a href="https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/SlicerRT_Tutorial_FilmDosimetryAnalysis.pptx">this tutorial</a></p>

---

## Post #3 by @Michael_Costello (2021-01-14 00:02 UTC)

<p>Thank you for your response. Can I add multiple ROIs at a time or do I need to select the appropriate file, create the ROI, and run perform calibration to add that ROI’s average to the calibration file then repeat for the next dose level?</p>

---

## Post #4 by @cpinter (2021-01-15 10:50 UTC)

<p>The application supports a single, common ROI for all the dose images. The workflow is quite rigid and the project is not active any more. If you need additional features, contributions are welcome. Either by you personally if you are up to it, or by a collaborator you can find who needs it as well.</p>

---

## Post #5 by @Michael_Costello (2021-01-15 13:04 UTC)

<p>Ah thank you very much! I just couldn’t figure that from the material.</p>

---
