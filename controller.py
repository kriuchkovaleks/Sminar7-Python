import export
import model
import view



def button_click():
    exp_type = view.export_type()
    if exp_type == '1':
        library = view.get_library_row()
        model.init(library)
        view.view_data(library)
        export.get_export_row(library)
    if exp_type == '2':
        library = view.get_library_column()
        model.init(library)
        view.view_data(library)
        export.get_export_column(library)    



'''
def button_click():
    library = view.get_library_column()
    model.init(library)
    view.view_data(library)
    export.get_export_column(library)


def button_click():
    library = view.get_library_row()
    model.init(library)
    view.view_data(library)
    export.get_export_row(library)
'''