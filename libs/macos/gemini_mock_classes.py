# Function to load mock classes to avoid library conflicts in mac
def load_mock_classes():
    load_tqdm_mock()
    load_typing_extension_mock()
    load_google_types_mock()

class MockType(type):
    def __getattr__(cls, name):
        if name.startswith('__') and name.endswith('__'):
            raise AttributeError(name)
        return cls
        
    def __getitem__(cls, item):
        if isinstance(item, int):
            raise IndexError("Mock no iterable")
        return cls

class GenericMockBase(metaclass=MockType):
    def __init__(self, *args, **kwargs): pass
    def __call__(self, *args, **kwargs): return self

def load_tqdm_mock():
    import sys
    import types
    import tqdm

    if 'tqdm.auto' not in sys.modules:
        tqdm_auto_mock = types.ModuleType('tqdm.auto')
        tqdm_auto_mock.tqdm = tqdm.tqdm
        sys.modules['tqdm.auto'] = tqdm_auto_mock
        setattr(tqdm, 'auto', tqdm_auto_mock)


def load_typing_extension_mock():
    import sys
    import typing_extensions

    modern_types = [
        'NotRequired', 'Required', 'TypeAliasType', 'Literal',
        'TypedDict', 'Annotated', 'Doc', 'Unpack', 'TypeGuard', 'Self',
        'override', 'dataclass_transform', 'TypeVarTuple', 'ParamSpec',
        'Concatenate', 'Final', 'TypeAlias', 'Never', 'assert_never',
        'assert_type', 'clear_overloads', 'get_overloads', 'overload',
        'get_type_hints', 'get_origin', 'get_args', 'is_typeddict', 'Any'
    ]

    for type_name in modern_types:
        if not hasattr(typing_extensions, type_name):
            setattr(typing_extensions, type_name, GenericMockBase)
            sys.modules['typing_extensions'].__dict__[type_name] = GenericMockBase

    if not hasattr(typing_extensions, 'Sentinel'):
        #We create a special Mock Class for Sentinel.
        class Sentinel:
            def __init__(self, name, repr=None):
                self._name = name
                self._repr = repr if repr is not None else f'<{name}>'
            def __repr__(self): return self._repr
            def __copy__(self): return self
            def __deepcopy__(self, memo): return self
        typing_extensions.Sentinel = Sentinel
        sys.modules['typing_extensions'].Sentinel = Sentinel


def load_google_types_mock():
    import sys
    import types

    parent_mod_name = 'google.generativeai.types'
    
    
    if parent_mod_name not in sys.modules:
        sys.modules[parent_mod_name] = types.ModuleType(parent_mod_name)
    parent_mod = sys.modules[parent_mod_name]
    parent_mod.__path__ = []

    new_mods = [
        'citation_types', 'content_types', 'generation_types', 
        'safety_types', 'model_types', 'retriever_types',
        'file_types', 'discuss_types', 'permission_types',
        'caching_types','helper_types', 'tool_types',
        'system_instruction_types', 'answer_types', 'tuned_model_types',
        'text_types', 'blob_types', 'GenerationConfig'
    ]

    for mod_name in new_mods:
        full_path = f'{parent_mod_name}.{mod_name}'
        mock_mod = types.ModuleType(full_path)
        mock_mod.__all__ = ['GenericMockBase'] 
        mock_mod.__path__ = []
        mock_mod.__dict__['__getattr__'] = lambda name: GenericMockBase
        mock_mod.__dict__['GenericMockBase'] = GenericMockBase
        
        sys.modules[full_path] = mock_mod
        setattr(parent_mod, mod_name, mock_mod)