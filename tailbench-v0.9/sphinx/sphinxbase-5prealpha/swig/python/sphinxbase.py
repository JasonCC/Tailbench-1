# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
This documentation was automatically generated using original comments in
Doxygen format. As some C types and data structures cannot be directly mapped
into Python types, some non-trivial type conversion could have place.
Basically a type is replaced with another one that has the closest match, and
sometimes one argument of generated function comprises several arguments of the
original function (usually two).

Functions having error code as the return value and returning effective
value in one of its arguments are transformed so that the effective value is
returned in a regular fashion and run-time exception is being thrown in case of
negative error code.
"""


from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_sphinxbase', [dirname(__file__)])
        except ImportError:
            import _sphinxbase
            return _sphinxbase
        if fp is not None:
            try:
                _mod = imp.load_module('_sphinxbase', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _sphinxbase = swig_import_helper()
    del swig_import_helper
else:
    import _sphinxbase
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class Config(_object):
    """Proxy of C Config struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Config, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Config, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _sphinxbase.delete_Config
    __del__ = lambda self: None

    def set_boolean(self, key, val):
        """set_boolean(Config self, char const * key, bool val)"""
        return _sphinxbase.Config_set_boolean(self, key, val)


    def set_int(self, key, val):
        """set_int(Config self, char const * key, int val)"""
        return _sphinxbase.Config_set_int(self, key, val)


    def set_float(self, key, val):
        """set_float(Config self, char const * key, double val)"""
        return _sphinxbase.Config_set_float(self, key, val)


    def set_string(self, key, val):
        """set_string(Config self, char const * key, char const * val)"""
        return _sphinxbase.Config_set_string(self, key, val)


    def exists(self, key):
        """exists(Config self, char const * key) -> bool"""
        return _sphinxbase.Config_exists(self, key)


    def get_boolean(self, key):
        """get_boolean(Config self, char const * key) -> bool"""
        return _sphinxbase.Config_get_boolean(self, key)


    def get_int(self, key):
        """get_int(Config self, char const * key) -> int"""
        return _sphinxbase.Config_get_int(self, key)


    def get_float(self, key):
        """get_float(Config self, char const * key) -> double"""
        return _sphinxbase.Config_get_float(self, key)


    def get_string(self, key):
        """get_string(Config self, char const * key) -> char const *"""
        return _sphinxbase.Config_get_string(self, key)

Config_swigregister = _sphinxbase.Config_swigregister
Config_swigregister(Config)

class FrontEnd(_object):
    """Proxy of C FrontEnd struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FrontEnd, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FrontEnd, name)
    __repr__ = _swig_repr

    def __init__(self, ptr):
        """__init__(FrontEnd self, fe_t * ptr) -> FrontEnd"""
        this = _sphinxbase.new_FrontEnd(ptr)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _sphinxbase.delete_FrontEnd
    __del__ = lambda self: None

    def output_size(self):
        """output_size(FrontEnd self) -> int"""
        return _sphinxbase.FrontEnd_output_size(self)


    def start_utt(self):
        """start_utt(FrontEnd self)"""
        return _sphinxbase.FrontEnd_start_utt(self)


    def process_utt(self, spch, nsamps, cep_block):
        """process_utt(FrontEnd self, int16 const * spch, size_t nsamps, mfcc_t *** cep_block) -> int32"""
        return _sphinxbase.FrontEnd_process_utt(self, spch, nsamps, cep_block)


    def end_utt(self, out_cepvector):
        """end_utt(FrontEnd self, mfcc_t * out_cepvector) -> int32"""
        return _sphinxbase.FrontEnd_end_utt(self, out_cepvector)

FrontEnd_swigregister = _sphinxbase.FrontEnd_swigregister
FrontEnd_swigregister(FrontEnd)

class Feature(_object):
    """Proxy of C Feature struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Feature, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Feature, name)
    __repr__ = _swig_repr

    def __init__(self, ptr):
        """__init__(Feature self, feat_t * ptr) -> Feature"""
        this = _sphinxbase.new_Feature(ptr)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _sphinxbase.delete_Feature
    __del__ = lambda self: None
Feature_swigregister = _sphinxbase.Feature_swigregister
Feature_swigregister(Feature)

class FsgModel(_object):
    """Proxy of C FsgModel struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FsgModel, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FsgModel, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(FsgModel self, char const * name, LogMath logmath, float lw, int32 n) -> FsgModel
        __init__(FsgModel self, fsg_model_t * ptr) -> FsgModel
        __init__(FsgModel self, char const * path, LogMath logmath, float lw) -> FsgModel
        """
        this = _sphinxbase.new_FsgModel(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _sphinxbase.delete_FsgModel
    __del__ = lambda self: None

    def word_id(self, word):
        """word_id(FsgModel self, char const * word) -> int"""
        return _sphinxbase.FsgModel_word_id(self, word)


    def word_add(self, word):
        """word_add(FsgModel self, char const * word) -> int"""
        return _sphinxbase.FsgModel_word_add(self, word)


    def trans_add(self, src, dst, logp, wid):
        """trans_add(FsgModel self, int32 src, int32 dst, int32 logp, int32 wid)"""
        return _sphinxbase.FsgModel_trans_add(self, src, dst, logp, wid)


    def null_trans_add(self, src, dst, logp):
        """null_trans_add(FsgModel self, int32 src, int32 dst, int32 logp) -> int32"""
        return _sphinxbase.FsgModel_null_trans_add(self, src, dst, logp)


    def tag_trans_add(self, src, dst, logp, wid):
        """tag_trans_add(FsgModel self, int32 src, int32 dst, int32 logp, int32 wid) -> int32"""
        return _sphinxbase.FsgModel_tag_trans_add(self, src, dst, logp, wid)


    def add_silence(self, silword, state, silprob):
        """add_silence(FsgModel self, char const * silword, int state, int32 silprob) -> int"""
        return _sphinxbase.FsgModel_add_silence(self, silword, state, silprob)


    def add_alt(self, baseword, altword):
        """add_alt(FsgModel self, char const * baseword, char const * altword) -> int"""
        return _sphinxbase.FsgModel_add_alt(self, baseword, altword)


    def writefile(self, path):
        """writefile(FsgModel self, char const * path)"""
        return _sphinxbase.FsgModel_writefile(self, path)

FsgModel_swigregister = _sphinxbase.FsgModel_swigregister
FsgModel_swigregister(FsgModel)

class JsgfRule(_object):
    """Proxy of C JsgfRule struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, JsgfRule, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, JsgfRule, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(JsgfRule self) -> JsgfRule"""
        this = _sphinxbase.new_JsgfRule()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _sphinxbase.delete_JsgfRule
    __del__ = lambda self: None

    def fromIter(itor):
        """fromIter(jsgf_rule_iter_t * itor) -> JsgfRule"""
        return _sphinxbase.JsgfRule_fromIter(itor)

    if _newclass:
        fromIter = staticmethod(fromIter)
    __swig_getmethods__["fromIter"] = lambda x: fromIter

    def name(self):
        """name(JsgfRule self) -> char const *"""
        return _sphinxbase.JsgfRule_name(self)


    def public(self):
        """public(JsgfRule self) -> bool"""
        return _sphinxbase.JsgfRule_public(self)

JsgfRule_swigregister = _sphinxbase.JsgfRule_swigregister
JsgfRule_swigregister(JsgfRule)

def JsgfRule_fromIter(itor):
    """JsgfRule_fromIter(jsgf_rule_iter_t * itor) -> JsgfRule"""
    return _sphinxbase.JsgfRule_fromIter(itor)

class NGramModel(_object):
    """Proxy of C NGramModel struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NGramModel, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NGramModel, name)
    __repr__ = _swig_repr

    def fromIter(itor):
        """fromIter(ngram_model_set_iter_t * itor) -> NGramModel"""
        return _sphinxbase.NGramModel_fromIter(itor)

    if _newclass:
        fromIter = staticmethod(fromIter)
    __swig_getmethods__["fromIter"] = lambda x: fromIter

    def __init__(self, *args):
        """
        __init__(NGramModel self, char const * path) -> NGramModel
        __init__(NGramModel self, Config config, LogMath logmath, char const * path) -> NGramModel
        """
        this = _sphinxbase.new_NGramModel(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _sphinxbase.delete_NGramModel
    __del__ = lambda self: None

    def write(self, path, ftype):
        """write(NGramModel self, char const * path, ngram_file_type_t ftype)"""
        return _sphinxbase.NGramModel_write(self, path, ftype)


    def str_to_type(self, str):
        """str_to_type(NGramModel self, char const * str) -> ngram_file_type_t"""
        return _sphinxbase.NGramModel_str_to_type(self, str)


    def type_to_str(self, type):
        """type_to_str(NGramModel self, int type) -> char const *"""
        return _sphinxbase.NGramModel_type_to_str(self, type)


    def casefold(self, kase):
        """casefold(NGramModel self, int kase)"""
        return _sphinxbase.NGramModel_casefold(self, kase)


    def size(self):
        """size(NGramModel self) -> int32"""
        return _sphinxbase.NGramModel_size(self)


    def add_word(self, word, weight):
        """add_word(NGramModel self, char const * word, float32 weight) -> int32"""
        return _sphinxbase.NGramModel_add_word(self, word, weight)


    def add_class(self, c, w, n, weights):
        """add_class(NGramModel self, char const * c, float32 w, size_t n, float32 const * weights) -> int32"""
        return _sphinxbase.NGramModel_add_class(self, c, w, n, weights)


    def prob(self, n):
        """prob(NGramModel self, size_t n) -> int32"""
        return _sphinxbase.NGramModel_prob(self, n)

NGramModel_swigregister = _sphinxbase.NGramModel_swigregister
NGramModel_swigregister(NGramModel)

def NGramModel_fromIter(itor):
    """NGramModel_fromIter(ngram_model_set_iter_t * itor) -> NGramModel"""
    return _sphinxbase.NGramModel_fromIter(itor)

class LogMath(_object):
    """Proxy of C LogMath struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LogMath, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LogMath, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(LogMath self) -> LogMath
        __init__(LogMath self, logmath_t * ptr) -> LogMath
        """
        this = _sphinxbase.new_LogMath(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _sphinxbase.delete_LogMath
    __del__ = lambda self: None
LogMath_swigregister = _sphinxbase.LogMath_swigregister
LogMath_swigregister(LogMath)

class NGramModelSetIterator(_object):
    """Proxy of C NGramModelSetIterator struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NGramModelSetIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NGramModelSetIterator, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ptr"] = _sphinxbase.NGramModelSetIterator_ptr_set
    __swig_getmethods__["ptr"] = _sphinxbase.NGramModelSetIterator_ptr_get
    if _newclass:
        ptr = _swig_property(_sphinxbase.NGramModelSetIterator_ptr_get, _sphinxbase.NGramModelSetIterator_ptr_set)

    def __init__(self, ptr):
        """__init__(NGramModelSetIterator self, ngram_model_set_iter_t * ptr) -> NGramModelSetIterator"""
        this = _sphinxbase.new_NGramModelSetIterator(ptr)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _sphinxbase.delete_NGramModelSetIterator
    __del__ = lambda self: None

    def next(self):
        """next(NGramModelSetIterator self) -> NGramModel"""
        return _sphinxbase.NGramModelSetIterator_next(self)


    def __next__(self):
        """__next__(NGramModelSetIterator self) -> NGramModel"""
        return _sphinxbase.NGramModelSetIterator___next__(self)

NGramModelSetIterator_swigregister = _sphinxbase.NGramModelSetIterator_swigregister
NGramModelSetIterator_swigregister(NGramModelSetIterator)

class JsgfIterator(_object):
    """Proxy of C JsgfIterator struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, JsgfIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, JsgfIterator, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ptr"] = _sphinxbase.JsgfIterator_ptr_set
    __swig_getmethods__["ptr"] = _sphinxbase.JsgfIterator_ptr_get
    if _newclass:
        ptr = _swig_property(_sphinxbase.JsgfIterator_ptr_get, _sphinxbase.JsgfIterator_ptr_set)

    def __init__(self, ptr):
        """__init__(JsgfIterator self, jsgf_rule_iter_t * ptr) -> JsgfIterator"""
        this = _sphinxbase.new_JsgfIterator(ptr)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _sphinxbase.delete_JsgfIterator
    __del__ = lambda self: None

    def next(self):
        """next(JsgfIterator self) -> JsgfRule"""
        return _sphinxbase.JsgfIterator_next(self)


    def __next__(self):
        """__next__(JsgfIterator self) -> JsgfRule"""
        return _sphinxbase.JsgfIterator___next__(self)

JsgfIterator_swigregister = _sphinxbase.JsgfIterator_swigregister
JsgfIterator_swigregister(JsgfIterator)

class NGramModelSet(_object):
    """Proxy of C NGramModelSet struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NGramModelSet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NGramModelSet, name)
    __repr__ = _swig_repr

    def __iter__(self):
        """__iter__(NGramModelSet self) -> NGramModelSetIterator"""
        return _sphinxbase.NGramModelSet___iter__(self)


    def __init__(self, config, logmath, path):
        """__init__(NGramModelSet self, Config config, LogMath logmath, char const * path) -> NGramModelSet"""
        this = _sphinxbase.new_NGramModelSet(config, logmath, path)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _sphinxbase.delete_NGramModelSet
    __del__ = lambda self: None

    def count(self):
        """count(NGramModelSet self) -> int32"""
        return _sphinxbase.NGramModelSet_count(self)


    def add(self, model, name, weight, reuse_widmap):
        """add(NGramModelSet self, NGramModel model, char const * name, float weight, bool reuse_widmap) -> NGramModel"""
        return _sphinxbase.NGramModelSet_add(self, model, name, weight, reuse_widmap)


    def select(self, name):
        """select(NGramModelSet self, char const * name) -> NGramModel"""
        return _sphinxbase.NGramModelSet_select(self, name)


    def lookup(self, name):
        """lookup(NGramModelSet self, char const * name) -> NGramModel"""
        return _sphinxbase.NGramModelSet_lookup(self, name)


    def current(self):
        """current(NGramModelSet self) -> char const *"""
        return _sphinxbase.NGramModelSet_current(self)

NGramModelSet_swigregister = _sphinxbase.NGramModelSet_swigregister
NGramModelSet_swigregister(NGramModelSet)

class Jsgf(_object):
    """Proxy of C Jsgf struct."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Jsgf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Jsgf, name)
    __repr__ = _swig_repr

    def __iter__(self):
        """__iter__(Jsgf self) -> JsgfIterator"""
        return _sphinxbase.Jsgf___iter__(self)


    def __init__(self, path):
        """__init__(Jsgf self, char const * path) -> Jsgf"""
        this = _sphinxbase.new_Jsgf(path)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _sphinxbase.delete_Jsgf
    __del__ = lambda self: None

    def name(self):
        """name(Jsgf self) -> char const *"""
        return _sphinxbase.Jsgf_name(self)


    def get_rule(self, name):
        """get_rule(Jsgf self, char const * name) -> JsgfRule"""
        return _sphinxbase.Jsgf_get_rule(self, name)


    def build_fsg(self, rule, logmath, lw):
        """build_fsg(Jsgf self, JsgfRule rule, LogMath logmath, float lw) -> FsgModel"""
        return _sphinxbase.Jsgf_build_fsg(self, rule, logmath, lw)

Jsgf_swigregister = _sphinxbase.Jsgf_swigregister
Jsgf_swigregister(Jsgf)

# This file is compatible with both classic and new-style classes.


