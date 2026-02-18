# Wrap_python build error in qt loadable widget

**Topic ID**: 37298
**Date**: 2024-07-10
**URL**: https://discourse.slicer.org/t/wrap-python-build-error-in-qt-loadable-widget/37298

---

## Post #1 by @fqzhice (2024-07-10 08:21 UTC)

<p>Hi,</p>
<pre><code>In custom qt loadable extension, I set "WRAP_PYTHON" and include "ctkDICOMDisplayedFieldGeneratorRuleFactory".
</code></pre>
<p>I found this class is singleton and generate wrapper itself</p>
<pre><code class="lang-auto">private:
 ...
  friend class PythonQtWrapper_ctkDICOMDisplayedFieldGeneratorRuleFactory; // Allow Python wrapping without enabling direct instantiation
</code></pre>
<p>but , in generated_cpp folder , the xxxxPythonQt project build fails becasue the constructer ctkDICOMDisplayedFieldGeneratorRuleFactory is private</p>
<pre><code class="lang-auto">class PythonQtWrapper_ctkDICOMDisplayedFieldGeneratorRuleFactory : public QObject
{
...
  ctkDICOMDisplayedFieldGeneratorRuleFactory* new_ctkDICOMDisplayedFieldGeneratorRuleFactory(QObject*  parent = 0)
    {
    return new ctkDICOMDisplayedFieldGeneratorRuleFactory(parent);
    }
...
};
</code></pre>
<p>can anyone help to solve it?</p>

---
