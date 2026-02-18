# cannot import name 'featureextractor' from 'radiomics'

**Topic ID**: 12768
**Date**: 2020-07-29
**URL**: https://discourse.slicer.org/t/cannot-import-name-featureextractor-from-radiomics/12768

---

## Post #1 by @hanna (2020-07-29 12:59 UTC)

<p>I have installed the python 3.7 and the radiomics. when I ran the .py file there is an error"cannot import name ‘featureextractor’ from ‘radiomics’ ". What can I do to resolve the problem?</p>

---

## Post #2 by @jamesobutler (2020-07-29 13:19 UTC)

<p>Hi hanna,</p>
<p>Based on a recent git issue posted (<a href="https://github.com/Radiomics/pyradiomics/issues/588" rel="nofollow noopener">https://github.com/Radiomics/pyradiomics/issues/588</a>), it appears you might have installed the “<a href="https://pypi.org/project/radiomics/" rel="nofollow noopener">radiomics</a>” package instead of installing the “<a href="https://pypi.org/project/pyradiomics/#description" rel="nofollow noopener">pyradiomics</a>” package.</p>

---
