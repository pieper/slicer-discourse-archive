---
topic_id: 4856
title: "Loadable Module Not Loading Json File Into Combo Box Correct"
date: 2018-11-23
url: https://discourse.slicer.org/t/4856
---

# loadable Module not loading .json file into combo box correctly

**Topic ID**: 4856
**Date**: 2018-11-23
**URL**: https://discourse.slicer.org/t/loadable-module-not-loading-json-file-into-combo-box-correctly/4856

---

## Post #1 by @Marcos_Soares (2018-11-23 02:56 UTC)

<p>Operating system: Mint 18<br>
Slicer version: 4.8<br>
Expected behavior: A list of data in the combo box should be exhibited<br>
Actual behavior: Nothing is displayed.</p>
<p>Hi everyone, i am new here and i am having a problem third party slicer extension called SEEG-Assistant, and i would appreciate any help with that.</p>
<p>I am working with a loadable module for electrodes segmentation through fiducial marks.<br>
Those Fiducial markers should be loaded and displayed by the module automatically, but that doesn’t happen.<br>
I am not really sure that the provided instructions in the original code is right or is enough for that.<br>
i am sending parts of the code with the related configurations, github link for the original code, and print screen of the module interface.</p>
<p><a href="https://github.com/mnarizzano/SEEGA" rel="noopener nofollow ugc">Full code link</a></p>
<p>Thank you!</p>
<p>relevant code parts</p>
<pre><code> #### Configure Segmentation - Section
    ### Read from files the list of the modules
    with open(slicer.modules.ContactPositionEstimatorInstance.electrodeTypesPath) as data_file:
        # models is a dictionary with the name of electrode type is the key
        self.models = json.load(data_file)

    #### Create the caption table for the configuration
    self.tableCaption = ["Name", "Type/Model", "TP", "cEP"]
    self.tableHsize = [80, 180, 50, 50]
    self.captionGB = qt.QGroupBox(self.segmentationCB)
    self.captionBL = qt.QHBoxLayout(self.captionGB)
    self.captionBL.setMargin(1)
    for i in (xrange(len(self.tableCaption))):
        a = qt.QLabel(self.tableCaption[i], self.captionGB)
        a.setMaximumWidth(self.tableHsize[i])
        a.setMaximumHeight(20)
        a.setStyleSheet("qproperty-alignment: AlignCenter;")
        self.captionBL.addWidget(a)

    self.segmentationFL.addRow("", self.captionGB)
    self.electrodeList = []
</code></pre>
<p>PrintScreen</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c51a17836a76d1867fbf7e4cd0cf45fb27cfa610.png" data-download-href="/uploads/short-url/s7DXIze6Vm685Y3ewGhDQPBvQs0.png?dl=1" title="Screenshot%20from%202018-11-23%2000-31-15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c51a17836a76d1867fbf7e4cd0cf45fb27cfa610_2_690x345.png" alt="Screenshot%20from%202018-11-23%2000-31-15" data-base62-sha1="s7DXIze6Vm685Y3ewGhDQPBvQs0" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c51a17836a76d1867fbf7e4cd0cf45fb27cfa610_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c51a17836a76d1867fbf7e4cd0cf45fb27cfa610_2_1035x517.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c51a17836a76d1867fbf7e4cd0cf45fb27cfa610_2_1380x690.png 2x" data-dominant-color="8D8C92"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-11-23%2000-31-15</span><span class="informations">1617×810 54.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-11-23 03:48 UTC)

<p>I had a look at the code and it seems that first you need to specify markup points and set name of entry and target points to have the exact same name:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d67f2cd5146cfcebf5f8e211b6887c087b8d73db.png" data-download-href="/uploads/short-url/uBwEj5CFFrkU6WHcUu7T8SZZZOz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d67f2cd5146cfcebf5f8e211b6887c087b8d73db_2_690x371.png" alt="image" data-base62-sha1="uBwEj5CFFrkU6WHcUu7T8SZZZOz" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d67f2cd5146cfcebf5f8e211b6887c087b8d73db_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d67f2cd5146cfcebf5f8e211b6887c087b8d73db_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d67f2cd5146cfcebf5f8e211b6887c087b8d73db_2_1380x742.png 2x" data-dominant-color="C0C1C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1701×916 60.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then in Contact position estimator module, select the markup list in the “Fiducial list” selector:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd08e23222f28cd4385044630272ddaaba094894.png" data-download-href="/uploads/short-url/A6rPE3nPKq0XQMeL2enCKBoSnHu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd08e23222f28cd4385044630272ddaaba094894_2_681x500.png" alt="image" data-base62-sha1="A6rPE3nPKq0XQMeL2enCKBoSnHu" width="681" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd08e23222f28cd4385044630272ddaaba094894_2_681x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd08e23222f28cd4385044630272ddaaba094894_2_1021x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd08e23222f28cd4385044630272ddaaba094894.png 2x" data-dominant-color="F8F8F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1224×898 39.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For further questions, I would recommend to contact the developers of this extension. If they are not available, you can <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_use_a_visual_debugger_for_step-by-step_debugging">attach a debugger</a> and run the code step by step to see how exactly it works.</p>

---
