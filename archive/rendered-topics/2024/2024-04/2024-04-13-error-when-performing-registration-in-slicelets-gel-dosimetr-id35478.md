---
topic_id: 35478
title: "Error When Performing Registration In Slicelets Gel Dosimetr"
date: 2024-04-13
url: https://discourse.slicer.org/t/35478
---

# Error when Performing Registration in Slicelets > Gel Dosimetry Analysis

**Topic ID**: 35478
**Date**: 2024-04-13
**URL**: https://discourse.slicer.org/t/error-when-performing-registration-in-slicelets-gel-dosimetry-analysis/35478

---

## Post #1 by @sieunmiin96 (2024-04-13 15:57 UTC)

<p>I’m trying to perform gamma analysis of my data, but every time I press perform registration in 2.1 Register planning CT to CBCT of Gel Dosimetry Analysis under Slicelet, nothing happens and the loading icon by the mouse cursor doesn’t disappear unless I close the program.</p>
<h2><a name="p-109561-below-is-the-error-message-getparentplannode-failed-to-access-subject-hierarchy-node-getplanisocenterposition-failed-to-access-parent-plan-node-updateiectransformsfrombeam-failed-to-get-isocenter-position-for-beam-t320-cw-getplanisocenterposition-failed-to-access-parent-plan-node-updateiectransformsfrombeam-failed-to-get-isocenter-position-for-beam-t320-cw-getplanisocenterposition-failed-to-access-parent-plan-node-updateiectransformsfrombeam-failed-to-get-isocenter-position-for-beam-t320-cw-1" class="anchor" href="#p-109561-below-is-the-error-message-getparentplannode-failed-to-access-subject-hierarchy-node-getplanisocenterposition-failed-to-access-parent-plan-node-updateiectransformsfrombeam-failed-to-get-isocenter-position-for-beam-t320-cw-getplanisocenterposition-failed-to-access-parent-plan-node-updateiectransformsfrombeam-failed-to-get-isocenter-position-for-beam-t320-cw-getplanisocenterposition-failed-to-access-parent-plan-node-updateiectransformsfrombeam-failed-to-get-isocenter-position-for-beam-t320-cw-1" aria-label="Heading link"></a>Below is the error message:<br>
GetParentPlanNode: Failed to access subject hierarchy node<br>
GetPlanIsocenterPosition: Failed to access parent plan node<br>
UpdateIECTransformsFromBeam: Failed to get isocenter position for beam T320 CW<br>
GetPlanIsocenterPosition: Failed to access parent plan node<br>
UpdateIECTransformsFromBeam: Failed to get isocenter position for beam T320 CW<br>
GetPlanIsocenterPosition: Failed to access parent plan node<br>
UpdateIECTransformsFromBeam: Failed to get isocenter position for beam T320 CW</h2>
<h2><a name="p-109561-requestinformation-no-lookuptable-was-set-but-number-of-components-in-input-doesnt-match-outputformat-therefore-input-cant-be-passed-through-2" class="anchor" href="#p-109561-requestinformation-no-lookuptable-was-set-but-number-of-components-in-input-doesnt-match-outputformat-therefore-input-cant-be-passed-through-2" aria-label="Heading link"></a>RequestInformation: No LookupTable was set but number of components in input doesn’t match OutputFormat, therefore input can’t be passed through!</h2>
<h2><a name="p-109561-execute-component-1-is-not-in-input-3" class="anchor" href="#p-109561-execute-component-1-is-not-in-input-3" aria-label="Heading link"></a>Execute: Component 1 is not in input.</h2>
<p>Traceback (most recent call last):<br>
File “C:\Users\AppData\Local\slicer.org\Slicer 5.6.1\slicer.org\Extensions-32438\GelDosimetryAnalysis\lib\Slicer-5.6\qt-scripted-modules\GelDosimetryAnalysisLogic\GelDosimetryAnalysisLogic.py”, line 79, in registerPlanCtToCbctAutomatic<br>
self.delayDisplay( “Register PlanCT to CBCT using rigid registration… %d” % waitCount )<br>
AttributeError: ‘GelDosimetryAnalysisLogic’ object has no attribute ‘delayDisplay’<br>
Traceback (most recent call last):<br>
File “C:/Users/AppData/Local/slicer.org/Slicer 5.6.1/slicer.org/Extensions-32438/GelDosimetryAnalysis/lib/Slicer-5.6/qt-scripted-modules/GelDosimetryAnalysis.py”, line 1376, in onPlanCtToCbctAutomaticRegistration<br>
self.planCtVolumeNode.SetAndObserveTransformNodeID(cbctToPlanTransformNode.GetID())<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetID’</p>

---

## Post #2 by @cpinter (2024-04-30 12:10 UTC)

<p>Just to have some record of where this is going, here’s a little part of the email I just sent to the supervisor of the poster of this question:</p>
<p>“The problem is that the Gel Dosimetry extension was finished several years ago, and there has been no funding or any maintenance work on it since. And now it would require some real effort.”</p>
<p>We’ll think together how to update the extension in a sustainable, but hopefully not a one-off way.</p>
<p><a class="mention" href="/u/sieunmiin96">@sieunmiin96</a> Please keep the kind forum readers updated about any progress we make, here in this topic.</p>

---
