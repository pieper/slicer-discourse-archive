# Loading GPA results from geomorph into Slicermorph?

**Topic ID**: 41982
**Date**: 2025-03-06
**URL**: https://discourse.slicer.org/t/loading-gpa-results-from-geomorph-into-slicermorph/41982

---

## Post #1 by @stineblom (2025-03-06 10:39 UTC)

<p>Hi community,</p>
<p>I have created a dataset of 499 pseudolandmarks for 107 bones using ALPACA. I compared the GPA+PCA results from geomorph and Slicermorph and noticed that geomorph describes ~10% more variance along PC1, possibly due to my correction for the ‘sliding’ factor.</p>
<p>Now, I want to explore the data generated in geomorph within Slicermorph. How can I import these data, and in what format? I noticed that Slicermorph’s GPA results generate multiple .csv files—do I need to create similar files to successfully import my data into Slicermorph?</p>
<p>I hope I’ve explained this clearly. Thanks in advance for any help!</p>
<p>/Stine</p>

---

## Post #2 by @muratmaga (2025-03-06 16:25 UTC)

<p>Please look at this example. At this point you we “hack” the GPA module’s “Load an existing analysis” feature to bring results from R and geomorph specifically:</p>
<p>basically all you have to do is to point out the variables that store aligned coordinates and PCA results from geomorph and pass it to function called <code>geomorph2slicermorph2</code>.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerMorph/SlicerMorphR?tab=readme-ov-file#how-to-run-a-geomorph-analysis-with-slicermorph-data-and-get-the-results-back-into-slicermorph-for-visualization">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorphR?tab=readme-ov-file#how-to-run-a-geomorph-analysis-with-slicermorph-data-and-get-the-results-back-into-slicermorph-for-visualization" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/c016f0151502c622487029b2fbaae435/SlicerMorph/SlicerMorphR?tab=readme-ov-file#how-to-run-a-geomorph-analysis-with-slicermorph-data-and-get-the-results-back-into-slicermorph-for-visualization" class="thumbnail">

  <h3><a href="https://github.com/SlicerMorph/SlicerMorphR?tab=readme-ov-file#how-to-run-a-geomorph-analysis-with-slicermorph-data-and-get-the-results-back-into-slicermorph-for-visualization" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerMorphR: R convenience functions for importing SlicerMorph...</a></h3>

    <p><span class="github-repo-description">R convenience functions for importing SlicerMorph dataset</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
