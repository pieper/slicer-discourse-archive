# Interpretation of Lung CT Analyzer results

**Topic ID**: 28729
**Date**: 2023-04-03
**URL**: https://discourse.slicer.org/t/interpretation-of-lung-ct-analyzer-results/28729

---

## Post #1 by @duan (2023-04-03 14:18 UTC)

<p>Excuse me,I have explained the relevant indicators in the lung segment analyzer,and would like you to see if my explanation is correct.As shown below<br>
“Total lungs” is all lungs volume that includes the volume of healthy lungs and the volume of unhealthy lungs as well as the gases they contain<br>
“InflatedThe” volume of functional lungs inflated that inclueds healthy lungs and damaged but still fuctional lungs<br>
“Emphysema” is a pulmonary lesion in which the distal end of the terminal bronchioles has decreased airway elasticity, excessive inflation, and increased lung volume, or is accompanied by destruction of the airway wall.In 3Dslicer ,emphyzema is the degree of expansion and destruction of air spaces in lung tissue<br>
Lung “infiltrated” mainly refers to the abnormal cells in the lungs, as well as cells outside the body, as well as the diffusion of certain pathological tissues around the lungs.In 3Dslicer ,infiltration represents inflammation、infection、edema ect of lung tissues or lung disease.<br>
“collapsed” generally refers to the collapse of lung in previously Lung tissue that was already filled with gas due to the loss of internal gas, which may be caused by airway obstruction, lung tissue compression, and other reasons.</p>

---

## Post #2 by @rbumm (2023-04-03 14:57 UTC)

<p>Lung CT Analyzer measures the volume of the mentioned indicators by the radiodensity of lung parenchyma expressed in HU units.<br>
The thresholds for the respective areas are predefined from experience but can be modified by the user.</p>
<aside class="quote no-group" data-username="duan" data-post="1" data-topic="28729" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/a9adbd/48.png" class="avatar"> duan:</div>
<blockquote>
<p>Excuse me,I have explained the relevant indicators in the lung segment analyzer,and would like you to see if my explanation is correct.As shown below</p>
<p>“Total lungs” is all lungs volume that includes the volume of healthy lungs and the volume of unhealthy lungs as well as the gases they contain</p>
</blockquote>
</aside>
<p>correct</p>
<aside class="quote no-group" data-username="duan" data-post="1" data-topic="28729" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/a9adbd/48.png" class="avatar"> duan:</div>
<blockquote>
<p>“InflatedThe” volume of functional lungs inflated that inclueds healthy lungs and damaged but still fuctional lungs</p>
</blockquote>
</aside>
<p>inflated refers to areas of the lung, where their density suggests that they are ventilated well and functioning normally</p>
<aside class="quote no-group quote-modified" data-username="duan" data-post="1" data-topic="28729" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/a9adbd/48.png" class="avatar"> duan:</div>
<blockquote>
<p>“Emphysema” is a pulmonary lesion in which the distal end of the terminal bronchioles has decreased airway elasticity, excessive inflation, and increased lung volume, or is accompanied by destruction of the airway wall 3Dslicer ,emphyzema is the degree of expansion and destruction of air spaces in lung tissue</p>
</blockquote>
</aside>
<p>correct</p>
<aside class="quote no-group quote-modified" data-username="duan" data-post="1" data-topic="28729" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/a9adbd/48.png" class="avatar"> duan:</div>
<blockquote>
<p>Lung “infiltrated” mainly refers to the abnormal cells in the lungs, as well as cells outside the body, as well as the diffusion of certain pathological tissues around the lungse 3Dslicer ,infiltration represents inflammation、infection、edema ect of lung tissues or lung disease.</p>
</blockquote>
</aside>
<p>correct</p>
<aside class="quote no-group" data-username="duan" data-post="1" data-topic="28729" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/a9adbd/48.png" class="avatar"> duan:</div>
<blockquote>
<p>“collapsed” generally refers to the collapse of lung in previously Lung tissue that was already filled with gas due to the loss of internal gas, which may be caused by airway obstruction, lung tissue compression, and other reasons.</p>
</blockquote>
</aside>
<p>“collapsed” refers to areas of lung parenchyma where a high radiodensity suggests that the tissue is not ventilated anymore. “collapsed” areas can be mimicked by lung vessels.</p>
<p>In COVID or pneumonia analysis, “total affected” is the volume (ml) of "infiltrated + “collapsed” in % of “total lung volume” (ml).</p>

---
