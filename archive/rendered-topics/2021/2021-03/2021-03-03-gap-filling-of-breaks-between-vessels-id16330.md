# gap filling of breaks between vessels

**Topic ID**: 16330
**Date**: 2021-03-03
**URL**: https://discourse.slicer.org/t/gap-filling-of-breaks-between-vessels/16330

---

## Post #1 by @fuentesdt (2021-03-03 14:58 UTC)

<p>Hi, Is there any functionality in vmtk, slicer, or itk for gap filling? something like this tensor voting method: Risser, Laurent, Franck Plouraboué, and Xavier Descombes. “Gap filling of 3-D microvascular networks by tensor voting.” <em>IEEE transactions on medical imaging</em> 27.5 (2008): 674-687.</p>
<p>We have pre-processed enhanced our imaging data and applied vesselness filters, but there are still some breaks in the vessel structure segmentations that need to be joined before generating the surface mesh for vmtk.</p>

---

## Post #2 by @lassoan (2021-03-03 15:27 UTC)

<p>There are various general-purpose hole-filling algorithms in ITK (and thus in Slicer), but I’m not aware of anything specific to vessels. You can ask on the <a href="https://discourse.itk.org">ITK forum</a> maybe they know more.</p>
<p>If you are interested in trying the method referenced above then contact the authors and tell them you would like to reproduce their results on your data. If they don’t respond or not willing to provide the source code or even a binary implementation then you can try to contact authors of papers that cite this paper. If nobody can give you anything useful then it is quite likely that the method does not actually work in practice and you can look for alternative solutions.</p>

---
