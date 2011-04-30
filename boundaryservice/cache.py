from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from tastypie.cache import SimpleCache

try:
    import importlib
except ImportError:
    from django.utils import importlib

__all__ = ('CacheClass',)

# set this here, and only override if nothing else fails
CacheClass = SimpleCache

cache_path = getattr(settings, 'BOUNDARYSERVICE_CACHE_CLASS', None)

if cache_path:
    try:
        mod_name, cls_name = cache_path.rsplit('.', 1)
    except ValueError:
        raise ImproperlyConfigured("%s isn't a cache class" % cache_path)
    
    try:
        mod = importlib.import_module(mod_name)
    except ImportError, e:
        raise ImproperlyConfigured("Couldn't import module %s: %s" % (mod_name, e))
    
    try:
        CacheClass = getattr(mod, cls_name)
    except AttributeError:
        raise ImproperlyConfigured("%s doesn't define a %s class" % (mod_name, cls_name))
