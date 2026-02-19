---
topic_id: 25457
title: "Pyhocon Exceptions Configmissingexception No Configuration S"
date: 2022-09-28
url: https://discourse.slicer.org/t/25457
---

# pyhocon.exceptions.ConfigMissingException: 'No configuration setting found for key HOME'

**Topic ID**: 25457
**Date**: 2022-09-28
**URL**: https://discourse.slicer.org/t/pyhocon-exceptions-configmissingexception-no-configuration-setting-found-for-key-home/25457

---

## Post #1 by @FUFU (2022-09-28 05:52 UTC)

<p>Our company developed a plug-in that supports version 4.8 of 3D-Slicer, but it reported some errors under version 5.0 of 3D-Slicer, as follows:：!!!setup<br>
Traceback (most recent call last):<br>
File “C:\Users\Admin\Desktop\SanmedSlicer_v3_0829\sigma\extras\pyhocon\config_parser.py”, line 305, in _resolve_variable<br>
return True, config.get(variable)<br>
File “C:\Users\Admin\Desktop\SanmedSlicer_v3_0829\sigma\extras\pyhocon\config_tree.py”, line 191, in get<br>
return self._get(ConfigTree.parse_key(key), 0, default)<br>
File “C:\Users\Admin\Desktop\SanmedSlicer_v3_0829\sigma\extras\pyhocon\config_tree.py”, line 140, in _get<br>
raise ConfigMissingException(u"No configuration setting found for key {key}".format(key=‘.’.join(key_path[:key_index + 1])))<br>
pyhocon.exceptions.ConfigMissingException: ‘No configuration setting found for key HOME’</p>

---

## Post #2 by @FUFU (2022-09-28 06:10 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf318394f5b03d54010e14fe77aff6b2fe623a32.png" alt="1664344684506" data-base62-sha1="rhnhmGaZpnNOQ6Bf3lbvt8MMk2C" width="638" height="280"></p>

---

## Post #4 by @FUFU (2022-09-28 06:15 UTC)

<p>If anyone has seen this error and solved it, please tell me how to solve it</p>

---

## Post #5 by @jamesobutler (2022-09-28 12:12 UTC)

<p>It appears your code uses an additional python package <a href="https://pypi.org/project/pyhocon/" class="inline-onebox" rel="noopener nofollow ugc">pyhocon · PyPI</a> for reading some config file. Is your config correct? I’m not sure what this config is doing because it is not standard Slicer functionality. Without access to the full code it is difficult to know what is the problem.</p>

---

## Post #6 by @FUFU (2022-09-29 02:41 UTC)

<p>the following is ConfigTree.py<br>
from pyparsing import lineno<br>
from pyparsing import col</p>
<p>try:  # pragma: no cover<br>
from collections import OrderedDict<br>
except ImportError:  # pragma: no cover<br>
from ordereddict import OrderedDict<br>
try:<br>
basestring<br>
except NameError:  # pragma: no cover<br>
basestring = str<br>
unicode = str</p>
<p>import re<br>
from .exceptions import ConfigException, ConfigWrongTypeException, ConfigMissingException</p>
<p>class UndefinedKey(object):<br>
pass</p>
<p>class NoneValue(object):<br>
pass</p>
<p>class ConfigTree(OrderedDict):<br>
KEY_SEP = ‘.’</p>
<pre><code>def __init__(self, *args, **kwds):
    self.root = kwds.pop('root') if 'root' in kwds else False
    if self.root:
        self.history = {}
    super(ConfigTree, self).__init__(*args, **kwds)
    for key, value in self.items():
        if isinstance(value, ConfigValues):
            value.parent = self
            value.index = key

@staticmethod
def merge_configs(a, b, copy_trees=False):
    """Merge config b into a

    :param a: target config
    :type a: ConfigTree
    :param b: source config
    :type b: ConfigTree
    :return: merged config a
    """
    for key, value in b.items():
        # if key is in both a and b and both values are dictionary then merge it otherwise override it
        if key in a and isinstance(a[key], ConfigTree) and isinstance(b[key], ConfigTree):
            if copy_trees:
                a[key] = a[key].copy()
            ConfigTree.merge_configs(a[key], b[key], copy_trees=copy_trees)
        else:
            if isinstance(value, ConfigValues):
                value.parent = a
                value.key = key
                value.overriden_value = a.get(key, None)
            a[key] = value
            if a.root:
                a.history[key] = (a.history.get(key) or []) + b.history.get(key)

    return a

def _put(self, key_path, value, append=False):
    key_elt = key_path[0]
    if len(key_path) == 1:
        # if value to set does not exist, override
        # if they are both configs then merge
        # if not then override
        if key_elt in self and isinstance(self[key_elt], ConfigTree) and isinstance(value, ConfigTree):
            if self.root:
                new_value = ConfigTree.merge_configs(ConfigTree(), self[key_elt], copy_trees=True)
                new_value = ConfigTree.merge_configs(new_value, value, copy_trees=True)
                self._push_history(key_elt, new_value)
                self[key_elt] = new_value
            else:
                ConfigTree.merge_configs(self[key_elt], value)
        elif append:
            # If we have t=1
            # and we try to put t.a=5 then t is replaced by {a: 5}
            l = self.get(key_elt, None)
            if isinstance(l, ConfigValues):
                l.tokens.append(value)
                l.recompute()
            elif isinstance(l, ConfigTree) and isinstance(value, ConfigValues):
                value.tokens.append(l)
                value.recompute()
                self._push_history(key_elt, value)
                self[key_elt] = value
            elif isinstance(l, list) and isinstance(value, ConfigValues):
                self._push_history(key_elt, value)
                self[key_elt] = value
            elif isinstance(l, list):
                l += value
                self._push_history(key_elt, l)
            elif l is None:
                self._push_history(key_elt, value)
                self[key_elt] = value

            else:
                raise ConfigWrongTypeException(
                    u"Cannot concatenate the list {key}: {value} to {prev_value} of {type}".format(
                        key='.'.join(key_path),
                        value=value,
                        prev_value=l,
                        type=l.__class__.__name__)
                )
        else:
            # if there was an override keep overide value
            if isinstance(value, ConfigValues):
                value.parent = self
                value.key = key_elt
                value.overriden_value = self.get(key_elt, None)
            self._push_history(key_elt, value)
            self[key_elt] = value
    else:
        next_config_tree = super(ConfigTree, self).get(key_elt)
        if not isinstance(next_config_tree, ConfigTree):
            # create a new dictionary or overwrite a previous value
            next_config_tree = ConfigTree()
            self._push_history(key_elt, value)
            self[key_elt] = next_config_tree
        next_config_tree._put(key_path[1:], value, append)

def _push_history(self, key, value):
    if self.root:
        hist = self.history.get(key)
        if hist is None:
            hist = self.history[key] = []
        hist.append(value)

def _get(self, key_path, key_index=0, default=UndefinedKey):
    key_elt = key_path[key_index]
    elt = super(ConfigTree, self).get(key_elt, UndefinedKey)

    if elt is UndefinedKey:
        if default is UndefinedKey:
            raise ConfigMissingException(u"No configuration setting found for key {key}".format(key='.'.join(key_path[:key_index + 1])))
        else:
            return default

    if key_index == len(key_path) - 1:
        if isinstance(elt, NoneValue):
            return None
        else:
            return elt
    elif isinstance(elt, ConfigTree):
        return elt._get(key_path, key_index + 1, default)
    else:
        if default is UndefinedKey:
            raise ConfigWrongTypeException(
                u"{key} has type {type} rather than dict".format(key='.'.join(key_path[:key_index + 1]),
                                                                 type=type(elt).__name__))
        else:
            return default

@staticmethod
def parse_key(string):
    """
    Split a key into path elements:
    - a.b.c =&gt; a, b, c
    - a."b.c" =&gt; a, QuotedKey("b.c")
    - "a" =&gt; a
    - a.b."c" =&gt; a, b, c (special case)
    :param str:
    :return:
    """
    tokens = re.findall('"[^"]+"|[^\.]+', string)
    return [token if '.' in token else token.strip('"') for token in tokens]

def put(self, key, value, append=False):
    """Put a value in the tree (dot separated)

    :param key: key to use (dot separated). E.g., a.b.c
    :type key: basestring
    :param value: value to put
    """
    self._put(ConfigTree.parse_key(key), value, append)

def get(self, key, default=UndefinedKey):
    """Get a value from the tree

    :param key: key to use (dot separated). E.g., a.b.c
    :type key: basestring
    :param default: default value if key not found
    :type default: object
    :return: value in the tree located at key
    """
    return self._get(ConfigTree.parse_key(key), 0, default)

def get_string(self, key, default=UndefinedKey):
    """Return string representation of value found at key

    :param key: key to use (dot separated). E.g., a.b.c
    :type key: basestring
    :param default: default value if key not found
    :type default: basestring
    :return: string value
    :type return: basestring
    """
    value = self.get(key, default)
    if value is None:
        return None

    string_value = unicode(value)
    if string_value in ['True', 'False']:
        return string_value.lower()
    return string_value

def pop(self, key, default=UndefinedKey):
    """Remove specified key and return the corresponding value.
    If key is not found, default is returned if given, otherwise ConfigMissingException is raised

    This method assumes the user wants to remove the last value in the chain so it parses via parse_key
    and pops the last value out of the dict.

    :param key: key to use (dot separated). E.g., a.b.c
    :type key: basestring
    :param default: default value if key not found
    :type default: object
    :param default: default value if key not found
    :return: value in the tree located at key
    """
    if default != UndefinedKey and key not in self:
        return default

    value = self.get(key, UndefinedKey)
    lst = ConfigTree.parse_key(key)
    parent = self.KEY_SEP.join(lst[0:-1])
    child = lst[-1]

    if parent:
        self.get(parent).__delitem__(child)
    else:
        self.__delitem__(child)
    return value

def get_int(self, key, default=UndefinedKey):
    """Return int representation of value found at key

    :param key: key to use (dot separated). E.g., a.b.c
    :type key: basestring
    :param default: default value if key not found
    :type default: int
    :return: int value
    :type return: int
    """
    value = self.get(key, default)
    return int(value) if value is not None else None

def get_float(self, key, default=UndefinedKey):
    """Return float representation of value found at key

    :param key: key to use (dot separated). E.g., a.b.c
    :type key: basestring
    :param default: default value if key not found
    :type default: float
    :return: float value
    :type return: float
    """
    value = self.get(key, default)
    return float(value) if value is not None else None

def get_bool(self, key, default=UndefinedKey):
    """Return boolean representation of value found at key

    :param key: key to use (dot separated). E.g., a.b.c
    :type key: basestring
    :param default: default value if key not found
    :type default: bool
    :return: boolean value
    :type return: bool
    """

    # String conversions as per API-recommendations:
    # https://github.com/typesafehub/config/blob/master/HOCON.md#automatic-type-conversions
    bool_conversions = {
        None: None,
        'true': True, 'yes': True, 'on': True,
        'false': False, 'no': False, 'off': False
    }
    try:
        return bool_conversions[self.get_string(key, default)]
    except KeyError:
        raise ConfigException(
            u"{key} does not translate to a Boolean value".format(key=key))

def get_list(self, key, default=UndefinedKey):
    """Return list representation of value found at key

    :param key: key to use (dot separated). E.g., a.b.c
    :type key: basestring
    :param default: default value if key not found
    :type default: list
    :return: list value
    :type return: list
    """
    value = self.get(key, default)
    if isinstance(value, list):
        return value
    elif value is None:
        return None
    else:
        raise ConfigException(
            u"{key} has type '{type}' rather than 'list'".format(key=key, type=type(value).__name__))

def get_config(self, key, default=UndefinedKey):
    """Return tree config representation of value found at key

    :param key: key to use (dot separated). E.g., a.b.c
    :type key: basestring
    :param default: default value if key not found
    :type default: config
    :return: config value
    :type return: ConfigTree
    """
    value = self.get(key, default)
    if isinstance(value, dict):
        return value
    elif value is None:
        return None
    else:
        raise ConfigException(
            u"{key} has type '{type}' rather than 'config'".format(key=key, type=type(value).__name__))

def __getitem__(self, item):
    val = self.get(item)
    if val is UndefinedKey:
        raise KeyError(item)
    return val

def __contains__(self, item):
    return self._get(self.parse_key(item), default=NoneValue) is not NoneValue

def with_fallback(self, config):
    """
    return a new config with fallback on config
    :param config: config or filename of the config to fallback on
    :return: new config with fallback on config
    """
    if isinstance(config, ConfigTree):
        result = ConfigTree.merge_configs(config, self)
    else:
        from .config_parser import ConfigFactory
        result = ConfigTree.merge_configs(ConfigFactory.parse_file(config, resolve=False), self)
    from .config_parser import ConfigParser
    ConfigParser.resolve_substitutions(result)
    return result

def as_plain_ordered_dict(self):
    """return a deep copy of this config as a plain OrderedDict

    The config tree should be fully resolved.

    This is useful to get an object with no special semantics such as path expansion for the keys.
    In particular this means that keys that contain dots are not surrounded with '"' in the plain OrderedDict.

    :return: this config as an OrderedDict
    :type return: OrderedDict
    """
    def plain_value(v):
        if isinstance(v, list):
            return [plain_value(e) for e in v]
        elif isinstance(v, ConfigTree):
            return v.as_plain_ordered_dict()
        else:
            if isinstance(v, ConfigValues):
                raise ConfigException("The config tree contains unresolved elements")
            return v

    return OrderedDict((key.strip('"'), plain_value(value)) for key, value in self.items())
</code></pre>
<p>class ConfigList(list):<br>
def <strong>init</strong>(self, iterable=<span class="chcklst-box fa fa-square-o fa-fw"></span>):<br>
l = list(iterable)<br>
super(ConfigList, self).<strong>init</strong>(l)<br>
for index, value in enumerate(l):<br>
if isinstance(value, ConfigValues):<br>
value.parent = self<br>
value.key = index</p>
<p>class ConfigInclude(object):<br>
def <strong>init</strong>(self, tokens):<br>
self.tokens = tokens</p>
<p>class ConfigValues(object):<br>
def <strong>init</strong>(self, tokens, instring, loc):<br>
self.tokens = tokens<br>
self.parent = None<br>
self.key = None<br>
self._instring = instring<br>
self._loc = loc<br>
self.overriden_value = None<br>
self.recompute()</p>
<pre><code>def recompute(self):
    for index, token in enumerate(self.tokens):
        if isinstance(token, ConfigSubstitution):
            token.parent = self
            token.index = index

    # no value return empty string
    if len(self.tokens) == 0:
        self.tokens = ['']

    # if the last token is an unquoted string then right strip it
    if isinstance(self.tokens[-1], ConfigUnquotedString):
        # rstrip only whitespaces, not \n\r because they would have been used escaped
        self.tokens[-1] = self.tokens[-1].rstrip(' \t')

def has_substitution(self):
    return len(self.get_substitutions()) &gt; 0

def get_substitutions(self):
    return [token for token in self.tokens if isinstance(token, ConfigSubstitution)]

def transform(self):
    def determine_type(token):
        return ConfigTree if isinstance(token, ConfigTree) else ConfigList if isinstance(token, list) else str

    def format_str(v, last=False):
        if isinstance(v, ConfigQuotedString):
            return v.value + ('' if last else v.ws)
        else:
            return '' if v is None else unicode(v)

    if self.has_substitution():
        return self

    # remove None tokens
    tokens = [token for token in self.tokens if token is not None]

    if not tokens:
        return None

    # check if all tokens are compatible
    first_tok_type = determine_type(tokens[0])
    for index, token in enumerate(tokens[1:]):
        tok_type = determine_type(token)
        if first_tok_type is not tok_type:
            raise ConfigWrongTypeException(
                "Token '{token}' of type {tok_type} (index {index}) must be of type {req_tok_type} (line: {line}, col: {col})".format(
                    token=token,
                    index=index + 1,
                    tok_type=tok_type.__name__,
                    req_tok_type=first_tok_type.__name__,
                    line=lineno(self._loc, self._instring),
                    col=col(self._loc, self._instring)))

    if first_tok_type is ConfigTree:
        result = ConfigTree()
        for token in tokens:
            ConfigTree.merge_configs(result, token, copy_trees=True)
        return result
    elif first_tok_type is ConfigList:
        result = []
        main_index = 0
        for sublist in tokens:
            sublist_result = ConfigList()
            for token in sublist:
                if isinstance(token, ConfigValues):
                    token.parent = result
                    token.key = main_index
                main_index += 1
                sublist_result.append(token)
            result.extend(sublist_result)
        return result
    else:
        if len(tokens) == 1:
            if isinstance(tokens[0], ConfigQuotedString):
                return tokens[0].value
            return tokens[0]
        else:
            return ''.join(format_str(token) for token in tokens[:-1]) + format_str(tokens[-1], True)

def put(self, index, value):
    self.tokens[index] = value

def __repr__(self):  # pragma: no cover
    return '[ConfigValues: ' + ','.join(str(o) for o in self.tokens) + ']'
</code></pre>
<p>class ConfigSubstitution(object):<br>
def <strong>init</strong>(self, variable, optional, ws, instring, loc):<br>
self.variable = variable<br>
self.optional = optional<br>
self.ws = ws<br>
self.index = None<br>
self.parent = None<br>
self.instring = instring<br>
self.loc = loc</p>
<pre><code>def __repr__(self):  # pragma: no cover
    return '[ConfigSubstitution: ' + self.variable + ']'
</code></pre>
<p>class ConfigUnquotedString(unicode):<br>
def <strong>new</strong>(cls, value):<br>
return super(ConfigUnquotedString, cls).<strong>new</strong>(cls, value)</p>
<p>class ConfigQuotedString(object):<br>
def <strong>init</strong>(self, value, ws, instring, loc):<br>
self.value = value<br>
self.ws = ws<br>
self.instring = instring<br>
self.loc = loc</p>
<pre><code>def __repr__(self):  # pragma: no cover
    return '[ConfigQuotedString: ' + self.value + ']'
</code></pre>

---

## Post #7 by @FUFU (2022-09-29 02:42 UTC)

<p>the following is config_parser.py<br>
import re<br>
import os<br>
import socket<br>
import contextlib<br>
import codecs<br>
from pyparsing import Forward, Keyword, QuotedString, Word, Literal, Suppress, Regex, Optional, SkipTo, ZeroOrMore, <br>
Group, lineno, col, TokenConverter, replaceWith, alphanums, alphas8bit, ParseSyntaxException, StringEnd<br>
from pyparsing import ParserElement<br>
from sigma.extras.pyhocon.config_tree import ConfigTree, ConfigSubstitution, ConfigList, ConfigValues, ConfigUnquotedString, <br>
ConfigInclude, NoneValue, ConfigQuotedString<br>
from sigma.extras.pyhocon.exceptions import ConfigSubstitutionException, ConfigMissingException, ConfigException<br>
import logging</p>
<p>use_urllib2 = False<br>
try:<br>
# For Python 3.0 and later<br>
from urllib.request import urlopen<br>
from urllib.error import HTTPError, URLError<br>
except ImportError:  # pragma: no cover<br>
# Fall back to Python 2’s urllib2<br>
from urllib2 import urlopen, HTTPError, URLError</p>
<pre><code>use_urllib2 = True
</code></pre>
<p>try:<br>
basestring<br>
except NameError:  # pragma: no cover<br>
basestring = str<br>
unicode = str</p>
<p>logger = logging.getLogger(<strong>name</strong>)</p>
<p>class ConfigFactory(object):<br>
<span class="mention">@staticmethod</span><br>
def parse_file(filename, encoding=‘utf-8’, required=True, resolve=True):<br>
“”"Parse file</p>
<pre><code>    :param filename: filename
    :type filename: basestring
    :param encoding: file encoding
    :type encoding: basestring
    :param required: If true, raises an exception if can't load file
    :type required: boolean
    :param resolve: If true, resolve substitutions
    :type resolve: boolean
    :return: Config object
    :type return: Config
    """
    try:
        with codecs.open(filename, 'r', encoding=encoding) as fd:
            content = fd.read()
            return ConfigFactory.parse_string(content, os.path.dirname(filename), resolve)
    except IOError as e:
        if required:
            raise e
        logger.warn('Cannot include file %s. File does not exist or cannot be read.', filename)
        return []

@staticmethod
def parse_URL(url, timeout=None, resolve=True, required=False):
    """Parse URL

    :param url: url to parse
    :type url: basestring
    :param resolve: If true, resolve substitutions
    :type resolve: boolean
    :return: Config object or []
    :type return: Config or list
    """
    socket_timeout = socket._GLOBAL_DEFAULT_TIMEOUT if timeout is None else timeout

    try:
        with contextlib.closing(urlopen(url, timeout=socket_timeout)) as fd:
            content = fd.read() if use_urllib2 else fd.read().decode('utf-8')
            return ConfigFactory.parse_string(content, os.path.dirname(url), resolve)
    except (HTTPError, URLError) as e:
        logger.warn('Cannot include url %s. Resource is inaccessible.', url)
        if required:
            raise e
        else:
            return []

@staticmethod
def parse_string(content, basedir=None, resolve=True):
    """Parse URL

    :param content: content to parse
    :type content: basestring
    :param resolve: If true, resolve substitutions
    :type resolve: boolean
    :return: Config object
    :type return: Config
    """
    return ConfigParser().parse(content, basedir, resolve)

@classmethod
def from_dict(cls, dictionary):
    """Convert dictionary (and ordered dictionary) into a ConfigTree
    :param dictionary: dictionary to convert
    :type dictionary: dict
    :return: Config object
    :type return: Config
    """

    def create_tree(value):
        if isinstance(value, dict):
            res = ConfigTree()
            for key, child_value in value.items():
                res.put(key, create_tree(child_value))
            return res
        if isinstance(value, list):
            return [create_tree(v) for v in value]
        else:
            return value

    return create_tree(dictionary)
</code></pre>
<p>class ConfigParser(object):<br>
“”"<br>
Parse HOCON files: <a href="https://github.com/typesafehub/config/blob/master/HOCON.md" class="inline-onebox" rel="noopener nofollow ugc">config/HOCON.md at master · lightbend/config · GitHub</a><br>
“”"</p>
<pre><code>REPLACEMENTS = {
    '\\\n': '\n',
    '\\n': '\n',
    '\\r': '\r',
    '\\t': '\t',
    '\\=': '=',
    '\\#': '#',
    '\\!': '!',
    '\\"': '"'
}

@staticmethod
def parse(content, basedir=None, resolve=True):
    """parse a HOCON content

    :param content: HOCON content to parse
    :type content: basestring
    :param resolve: If true, resolve substitutions
    :type resolve: boolean
    :return: a ConfigTree or a list
    """

    def norm_string(value):
        for k, v in ConfigParser.REPLACEMENTS.items():
            value = value.replace(k, v)
        return value

    def unescape_string(tokens):
        return ConfigUnquotedString(norm_string(tokens[0]))

    def parse_multi_string(tokens):
        # remove the first and last 3 "
        return tokens[0][3: -3]

    def convert_number(tokens):
        n = tokens[0]
        try:
            return int(n)
        except ValueError:
            return float(n)

    # ${path} or ${?path} for optional substitution
    SUBSTITUTION_PATTERN = "\$\{(?P&lt;optional&gt;\?)?(?P&lt;variable&gt;[^}]+)\}(?P&lt;ws&gt;[ \t]*)"

    def create_substitution(instring, loc, token):
        # remove the ${ and }
        match = re.match(SUBSTITUTION_PATTERN, token[0])
        variable = match.group('variable')
        ws = match.group('ws')
        optional = match.group('optional') == '?'
        substitution = ConfigSubstitution(variable, optional, ws, instring, loc)
        return substitution

    # ${path} or ${?path} for optional substitution
    STRING_PATTERN = '(")(?P&lt;value&gt;[^"]*)\\1(?P&lt;ws&gt;[ \t]*)'

    def create_quoted_string(instring, loc, token):
        # remove the ${ and }
        match = re.match(STRING_PATTERN, token[0])
        value = norm_string(match.group('value'))
        ws = match.group('ws')
        return ConfigQuotedString(value, ws, instring, loc)

    def include_config(instring, loc, token):
        url = None
        file = None
        required = False

        if token[0] == 'required':
            required = True
            final_tokens = token[1:]
        else:
            final_tokens = token

        if len(final_tokens) == 1:  # include "test"
            value = final_tokens[0].value if isinstance(final_tokens[0], ConfigQuotedString) else final_tokens[0]
            if value.startswith("http://") or value.startswith("https://") or value.startswith("file://"):
                url = value
            else:
                file = value
        elif len(final_tokens) == 2:  # include url("test") or file("test")
            value = final_tokens[1].value if isinstance(token[1], ConfigQuotedString) else final_tokens[1]
            if final_tokens[0] == 'url':
                url = value
            else:
                file = value

        if url is not None:
            logger.debug('Loading config from url %s', url)
            obj = ConfigFactory.parse_URL(url, resolve=False, required=required)
        elif file is not None:
            path = file if basedir is None else os.path.join(basedir, file)
            logger.debug('Loading config from file %s', path)
            obj = ConfigFactory.parse_file(path, resolve=False, required=required)
        else:
            raise ConfigException('No file or URL specified at: {loc}: {instring}', loc=loc, instring=instring)

        return ConfigInclude(obj if isinstance(obj, list) else obj.items())

    ParserElement.setDefaultWhitespaceChars(' \t')

    assign_expr = Forward()
    true_expr = Keyword("true", caseless=True).setParseAction(replaceWith(True))
    false_expr = Keyword("false", caseless=True).setParseAction(replaceWith(False))
    null_expr = Keyword("null", caseless=True).setParseAction(replaceWith(NoneValue()))
    key = QuotedString('"', escChar='\\', unquoteResults=False) | Word(alphanums + alphas8bit + '._- ')

    eol = Word('\n\r').suppress()
    eol_comma = Word('\n\r,').suppress()
    comment = (Literal('#') | Literal('//')) - SkipTo(eol | StringEnd())
    comment_eol = Suppress(Optional(eol_comma) + comment)
    comment_no_comma_eol = (comment | eol).suppress()
    number_expr = Regex('[+-]?(\d*\.\d+|\d+(\.\d+)?)([eE]\d+)?(?=$|[ \t]*([\$\}\],#\n\r]|//))',
                        re.DOTALL).setParseAction(convert_number)

    # multi line string using """
    # Using fix described in http://pyparsing.wikispaces.com/share/view/3778969
    multiline_string = Regex('""".*?"*"""', re.DOTALL | re.UNICODE).setParseAction(parse_multi_string)
    # single quoted line string
    quoted_string = Regex('".*?"[ \t]*', re.UNICODE).setParseAction(create_quoted_string)
    # unquoted string that takes the rest of the line until an optional comment
    # we support .properties multiline support which is like this:
    # line1  \
    # line2 \
    # so a backslash precedes the \n
    unquoted_string = Regex('(?:\\\\|[^\[\{\s\]\}#,=\$])+[ \t]*', re.UNICODE).setParseAction(unescape_string)
    substitution_expr = Regex('[ \t]*\$\{[^\}]+\}[ \t]*').setParseAction(create_substitution)
    string_expr = multiline_string | quoted_string | unquoted_string

    value_expr = number_expr | true_expr | false_expr | null_expr | string_expr

    include_content = (quoted_string | ((Keyword('url') | Keyword('file')) - Literal('(').suppress() - quoted_string - Literal(')').suppress()))
    include_expr = (
        Keyword("include", caseless=True).suppress() +
        (
            include_content |
            (
                Keyword("required") - Literal('(').suppress() - include_content - Literal(')').suppress()
            )
        )
    ).setParseAction(include_config)

    root_dict_expr = Forward()
    dict_expr = Forward()
    list_expr = Forward()
    multi_value_expr = ZeroOrMore(comment_eol | include_expr | substitution_expr | dict_expr | list_expr | value_expr | (Literal(
        '\\') - eol).suppress())
    # for a dictionary : or = is optional
    # last zeroOrMore is because we can have t = {a:4} {b: 6} {c: 7} which is dictionary concatenation
    inside_dict_expr = ConfigTreeParser(ZeroOrMore(comment_eol | include_expr | assign_expr | eol_comma))
    inside_root_dict_expr = ConfigTreeParser(ZeroOrMore(comment_eol | include_expr | assign_expr | eol_comma), root=True)
    dict_expr &lt;&lt; Suppress('{') - inside_dict_expr - Suppress('}')
    root_dict_expr &lt;&lt; Suppress('{') - inside_root_dict_expr - Suppress('}')
    list_entry = ConcatenatedValueParser(multi_value_expr)
    list_expr &lt;&lt; Suppress('[') - ListParser(list_entry - ZeroOrMore(eol_comma - list_entry)) - Suppress(']')

    # special case when we have a value assignment where the string can potentially be the remainder of the line
    assign_expr &lt;&lt; Group(
        key -
        ZeroOrMore(comment_no_comma_eol) -
        (dict_expr | (Literal('=') | Literal(':') | Literal('+=')) - ZeroOrMore(
            comment_no_comma_eol) - ConcatenatedValueParser(multi_value_expr))
    )

    # the file can be { ... } where {} can be omitted or []
    config_expr = ZeroOrMore(comment_eol | eol) + (list_expr | root_dict_expr | inside_root_dict_expr) + ZeroOrMore(
        comment_eol | eol_comma)
    config = config_expr.parseString(content, parseAll=True)[0]
    if resolve:
        ConfigParser.resolve_substitutions(config)
    return config

@staticmethod
def _resolve_variable(config, substitution):
    """
    :param config:
    :param substitution:
    :return: (is_resolved, resolved_variable)
    """
    variable = substitution.variable
    try:
        return True, config.get(variable)
    except ConfigMissingException:
        # default to environment variable
        value = os.environ.get(variable)

        if value is None:
            if substitution.optional:
                return False, None
            else:
                raise ConfigSubstitutionException(
                    "Cannot resolve variable ${{{variable}}} (line: {line}, col: {col})".format(
                        variable=variable,
                        line=lineno(substitution.loc, substitution.instring),
                        col=col(substitution.loc, substitution.instring)))
        elif isinstance(value, ConfigList) or isinstance(value, ConfigTree):
            raise ConfigSubstitutionException(
                "Cannot substitute variable ${{{variable}}} because it does not point to a "
                "string, int, float, boolean or null {type} (line:{line}, col: {col})".format(
                    variable=variable,
                    type=value.__class__.__name__,
                    line=lineno(substitution.loc, substitution.instring),
                    col=col(substitution.loc, substitution.instring)))
        return True, value

@staticmethod
def _fixup_self_references(config):
    if isinstance(config, ConfigTree) and config.root:
        for key in config:  # Traverse history of element
            history = config.history[key]
            previous_item = history[0]
            for current_item in history[1:]:
                for substitution in ConfigParser._find_substitutions(current_item):
                    prop_path = ConfigTree.parse_key(substitution.variable)
                    if len(prop_path) &gt; 1 and config.get(substitution.variable, None) is not None:
                        continue  # If value is present in latest version, don't do anything
                    if prop_path[0] == key:
                        if isinstance(previous_item, ConfigValues):  # We hit a dead end, we cannot evaluate
                            raise ConfigSubstitutionException("Property {variable} cannot be substituted. Check for cycles.".format(
                                variable=substitution.variable))
                        value = previous_item if len(prop_path) == 1 else previous_item.get(".".join(prop_path[1:]))
                        _, _, current_item = ConfigParser._do_substitute(substitution, value)
                previous_item = current_item

            if len(history) == 1:  # special case, when self optional referencing without existing
                for substitution in ConfigParser._find_substitutions(previous_item):
                    prop_path = ConfigTree.parse_key(substitution.variable)
                    if len(prop_path) &gt; 1 and config.get(substitution.variable, None) is not None:
                        continue  # If value is present in latest version, don't do anything
                    if prop_path[0] == key and substitution.optional:
                        ConfigParser._do_substitute(substitution, None)

# traverse config to find all the substitutions
@staticmethod
def _find_substitutions(item):
    """Convert HOCON input into a JSON output

    :return: JSON string representation
    :type return: basestring
    """
    if isinstance(item, ConfigValues):
        return item.get_substitutions()

    substitutions = []
    if isinstance(item, ConfigTree):
        for key, child in item.items():
            substitutions += ConfigParser._find_substitutions(child)
    elif isinstance(item, list):
        for child in item:
            substitutions += ConfigParser._find_substitutions(child)
    return substitutions

@staticmethod
def _do_substitute(substitution, resolved_value, is_optional_resolved=True):
    unresolved = False
    new_substitutions = []
    if isinstance(resolved_value, ConfigValues):
        resolved_value = resolved_value.transform()
    if isinstance(resolved_value, ConfigValues):
        unresolved = True
        result = resolved_value
    else:
        # replace token by substitution
        config_values = substitution.parent
        # if it is a string, then add the extra ws that was present in the original string after the substitution
        formatted_resolved_value = resolved_value \
            if resolved_value is None \
            or isinstance(resolved_value, (dict, list)) \
            or substitution.index == len(config_values.tokens) - 1 \
            else (str(resolved_value) + substitution.ws)
        config_values.put(substitution.index, formatted_resolved_value)
        transformation = config_values.transform()
        result = None
        if transformation is None and not is_optional_resolved:
            result = config_values.overriden_value
        else:
            result = transformation

        if result is None and config_values.key in config_values.parent:
            del config_values.parent[config_values.key]
        else:
            config_values.parent[config_values.key] = result
            s = ConfigParser._find_substitutions(result)
            if s:
                new_substitutions = s
                unresolved = True

    return (unresolved, new_substitutions, result)

@staticmethod
def _final_fixup(item):
    if isinstance(item, ConfigValues):
        return item.transform()
    elif isinstance(item, list):
        return list([ConfigParser._final_fixup(child) for child in item])
    elif isinstance(item, ConfigTree):
        items = list(item.items())
        for key, child in items:
            item[key] = ConfigParser._final_fixup(child)
    return item

@staticmethod
def resolve_substitutions(config):
    ConfigParser._fixup_self_references(config)
    substitutions = ConfigParser._find_substitutions(config)
    if len(substitutions) &gt; 0:
        unresolved = True
        any_unresolved = True
        _substitutions = []
        while any_unresolved and len(substitutions) &gt; 0 and set(substitutions) != set(_substitutions):
            unresolved = False
            any_unresolved = True
            _substitutions = substitutions[:]

            for substitution in _substitutions:
                is_optional_resolved, resolved_value = ConfigParser._resolve_variable(config, substitution)

                # if the substitution is optional
                if not is_optional_resolved and substitution.optional:
                    resolved_value = None

                unresolved, new_substitutions, result = ConfigParser._do_substitute(substitution, resolved_value, is_optional_resolved)
                any_unresolved = unresolved or any_unresolved
                substitutions.extend(new_substitutions)
                if not isinstance(result, ConfigValues):
                    substitutions.remove(substitution)

        ConfigParser._final_fixup(config)
        if unresolved:
            raise ConfigSubstitutionException("Cannot resolve {variables}. Check for cycles.".format(
                variables=', '.join('${{{variable}}}: (line: {line}, col: {col})'.format(
                    variable=substitution.variable,
                    line=lineno(substitution.loc, substitution.instring),
                    col=col(substitution.loc, substitution.instring)) for substitution in substitutions)))

    return config
</code></pre>
<p>class ListParser(TokenConverter):<br>
“”“Parse a list [elt1, etl2, …]<br>
“””</p>
<pre><code>def __init__(self, expr=None):
    super(ListParser, self).__init__(expr)
    self.saveAsList = True

def postParse(self, instring, loc, token_list):
    """Create a list from the tokens

    :param instring:
    :param loc:
    :param token_list:
    :return:
    """
    cleaned_token_list = [token for tokens in (token.tokens if isinstance(token, ConfigInclude) else [token]
                                               for token in token_list if token != '')
                          for token in tokens]
    config_list = ConfigList(cleaned_token_list)
    return [config_list]
</code></pre>
<p>class ConcatenatedValueParser(TokenConverter):<br>
def <strong>init</strong>(self, expr=None):<br>
super(ConcatenatedValueParser, self).<strong>init</strong>(expr)<br>
self.parent = None<br>
self.key = None</p>
<pre><code>def postParse(self, instring, loc, token_list):
    config_values = ConfigValues(token_list, instring, loc)
    return [config_values.transform()]
</code></pre>
<p>class ConfigTreeParser(TokenConverter):<br>
“”"<br>
Parse a config tree from tokens<br>
“”"</p>
<pre><code>def __init__(self, expr=None, root=False):
    super(ConfigTreeParser, self).__init__(expr)
    self.root = root
    self.saveAsList = True

def postParse(self, instring, loc, token_list):
    """Create ConfigTree from tokens

    :param instring:
    :param loc:
    :param token_list:
    :return:
    """
    config_tree = ConfigTree(root=self.root)
    for element in token_list:
        expanded_tokens = element.tokens if isinstance(element, ConfigInclude) else [element]

        for tokens in expanded_tokens:
            # key, value1 (optional), ...
            key = tokens[0].strip()
            operator = '='
            if len(tokens) == 3 and tokens[1].strip() in [':', '=', '+=']:
                operator = tokens[1].strip()
                values = tokens[2:]
            elif len(tokens) == 2:
                values = tokens[1:]
            else:
                raise ParseSyntaxException("Unknown tokens {tokens} received".format(tokens=tokens))
            # empty string
            if len(values) == 0:
                config_tree.put(key, '')
            else:
                value = values[0]
                if isinstance(value, list) and operator == "+=":
                    value = ConfigValues([ConfigSubstitution(key, True, '', False, loc), value], False, loc)
                    config_tree.put(key, value, False)
                elif isinstance(value, unicode) and operator == "+=":
                    value = ConfigValues([ConfigSubstitution(key, True, '', True, loc), ' ' + value], True, loc)
                    config_tree.put(key, value, False)
                elif isinstance(value, list):
                    config_tree.put(key, value, False)
                else:
                    existing_value = config_tree.get(key, None)
                    if isinstance(value, ConfigTree) and not isinstance(existing_value, list):
                        # Only Tree has to be merged with tree
                        config_tree.put(key, value, True)
                    elif isinstance(value, ConfigValues):
                        conf_value = value
                        value.parent = config_tree
                        value.key = key
                        if isinstance(existing_value, list) or isinstance(existing_value, ConfigTree):
                            config_tree.put(key, conf_value, True)
                        else:
                            config_tree.put(key, conf_value, False)
                    else:
                        config_tree.put(key, value, False)
    return config_tree
</code></pre>

---

## Post #8 by @lassoan (2022-11-24 02:53 UTC)

<p>So many things have changed since Slicer-4.8 that it is very hard to guess what could have led to this error. If <code>HOME</code> is expected to be an environment variable then check Slicer-4.8 source code what defined it. If it is a setting in some configuration files then check why it is no longer found in your files.</p>
<p>I would recommend to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/python.html">set up a Python debugger</a> and go through your code step by step.</p>

---
