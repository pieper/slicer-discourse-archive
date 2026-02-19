---
topic_id: 16271
title: "Get Average Deformation From Model To Model"
date: 2021-02-28
url: https://discourse.slicer.org/t/16271
---

# Get average deformation from model to model

**Topic ID**: 16271
**Date**: 2021-02-28
**URL**: https://discourse.slicer.org/t/get-average-deformation-from-model-to-model/16271

---

## Post #1 by @BORIPHAT (2021-02-28 11:32 UTC)

<p>Hello, Lassoan</p>
<p>I would like to get the average deformation from model to model, too. Now I install SlicerSALT and which module use for analyzing? and what’s kind of file that I must attach to the input and output directory? Now I have the deformation model (.nrrd) and I would like to compare it with the original model (.nrrd).  Should I select both of them in the input directory or I have to do something before choose it? Thank you very much for your time and assistance in this matter.</p>
<p>Best regards,</p>

---

## Post #2 by @lassoan (2021-02-28 13:41 UTC)

<p>You can use ModelToModelDistance extension to compute displacement for each model point. You can then get the displacements as a numpy array using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromModelPointData">slicer.util.arrayFromModelPointData</a> and compute any statistics that you need.</p>
<p>If you don’t have corresponding point sets in your models or want to do more sophisticated analysis then you can use SlicerSALT. You can reach SlicerSALT developers by posting in this category:</p>
<aside class="onebox category-onebox" style="box-shadow: -5px 0px #652D90;">
  <article class="onebox-body category-onebox-body">
    <h3>
      <a class="badge-wrapper bullet" href="/c/community/slicer-salt/14">
          <span class="badge-category-bg" style="background-color: #652D90"></span>
        <span class="clear-badge"><span>SlicerSALT</span></span>
      </a>
    </h3>
      <div>
        <span class="description">
          <p>SlicerSALT is an under development customized Slicer with the aim of consolidating the various statistical shape analysis tools in one place. You can find more information about SlicerSALT at its <a href="http://salt.slicer.org">website</a>.</p>
        </span>
      </div>
  </article>
  <div class="clearfix"></div>
</aside>


---

## Post #3 by @BORIPHAT (2021-03-01 10:56 UTC)

<p>Thank you very much for your kindness. Now I can solve my problem by following your suggestion.</p>

---
