from plugins.interface import PluginInterface

from plugins.window.window import filter_methods

from functools import reduce

class Plugin(PluginInterface):
    def __repr__(self):
        return 'A plugin for getting window handle'

    def perform(self, command):
        match command:
            case {'type': 'handle', **rest}:
                """
                Get window handle, and save it.
                The intersection of handles filtered by all conditions is computed, then:
                If more than one handle exists, return the first. 
                If no handle is obtained, return None.
                
                Args:
                    title: Window title
                    title_part: A part of window title
                    cls: Window className
                    cls_part: A part of window className
                    width: Window width
                    height: Window height
                    save: Stored in robot vars, defaults to '__handle'
                """
                __save = rest.get('save', '__handle')
                handle_sets = []
                for condition in 'title, title_part, cls, cls_part, width, height'.split(', '):
                    if rest.get(condition):
                        method = filter_methods[f'filter_handle_by_{condition}']
                        handle_sets.append(method(rest.get(condition)))

                handles = list(reduce(set.intersection, handle_sets))
                if len(handles) == 0:
                    self.robot.vars[__save] = None
                    return
                self.robot.vars[__save] = handles[0]
                return
            case {'type': 'handle_child', **rest}:
                """
                Find the child that match the condition from the parent handle.

                Args:
                    name: The name of the parent handle stored in robot vars, defaults to '__handle'
                    title: Window title
                    title_part: A part of window title
                    cls: Window className
                    cls_part: A part of window className
                    width: Window width
                    height: Window height
                    save: Stored in robot vars, defaults to '__handle'
                """
                __save = rest.get('save', '__handle')
                __name = rest.get('name', '__handle')
                parent = self.robot.vars.get(__name)
                if parent is not None:
                    handle_sets = []
                    for condition in 'title, title_part, cls, cls_part, width, height'.split(', '):
                        if rest.get(condition):
                            method = filter_methods[f'filter_handle_by_{condition}']
                            handle_sets.append(method(rest.get(condition), parent))

                    handles = list(reduce(set.intersection, handle_sets))
                    if len(handles) == 0:
                        self.robot.vars[__save] = None
                        return
                    self.robot.vars[__save] = handles[0]
                    return


            case _:
                raise RuntimeError
