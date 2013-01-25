
from fanstatic import Library
from fanstatic import Resource
from fanstatic import Group


plone_example = Library('plone_example', 'plone_resources')

plone_javascript_variables = Resource(plone_example, 'plone_javascript_variables.js')
cookie_functions = Resource(plone_example, 'cookie_functions.js')
modernizr = Resource(plone_example, 'modernizr.js')

sarissa = Resource(plone_example, 'sarissa.js')
kukit = Resource(plone_example, 'kukit.js', depends=[sarissa])  # tiny_mce_init

tiny_mce = Resource(plone_example, 'tiny_mce.js')
tiny_mce_init = Resource(plone_example, 'tiny_mce_init.js', depends=[kukit, tiny_mce])

jquery = Resource(plone_example, 'jquery.js')
jquery_integration = Resource(plone_example, 'jquery-integration.js')

jquery_highlightsearchterms = Resource(plone_example, 'jquery.highlightsearchterms.js', depends=[jquery])
accessibility = Resource(plone_example, 'accessibility.js', depends=[jquery])
calendar_formfield = Resource(plone_example, 'calendar_formfield.js', depends=[jquery])
collapsibleformfields = Resource(plone_example, 'collapsibleformfields.js', depends=[jquery])
collapsiblesections = Resource(plone_example, 'collapsiblesections.js', depends=[jquery])
comments = Resource(plone_example, 'comments.js', depends=[jquery])
dragdropreorder = Resource(plone_example, 'dragdropreorder.js', depends=[jquery])
dropdown = Resource(plone_example, 'dropdown.js', depends=[jquery])
first_input_focus = Resource(plone_example, 'first_input_focus.js', depends=[jquery])
formUnload = Resource(plone_example, 'formUnload.js', depends=[jquery])
formsubmithelpers = Resource(plone_example, 'formsubmithelpers.js', depends=[jquery])
livesearch = Resource(plone_example, 'livesearch.js', depends=[jquery])
nodeutilities = Resource(plone_example, 'nodeutilities.js', depends=[jquery])
register_function = Resource(plone_example, 'register_function.js', depends=[jquery])
search = Resource(plone_example, 'search.js', depends=[jquery])
select_all = Resource(plone_example, 'select_all.js', depends=[jquery])
styleswitcher = Resource(plone_example, 'styleswitcher.js', depends=[jquery])
table_sorter = Resource(plone_example, 'table_sorter.js', depends=[jquery])
toc = Resource(plone_example, 'toc.js', depends=[jquery])
unlockOnFormUnload = Resource(plone_example, 'unlockOnFormUnload.js', depends=[jquery])

jquerytools = Resource(plone_example, 'plone.app.jquerytools.js', depends=[jquery])
jquerytools_form = Resource(plone_example, 'plone.app.jquerytools.form.js', depends=[jquerytools])
jquerytools_dateinput = Resource(plone_example, 'plone.app.jquerytools.dateinput.js', depends=[jquerytools])
jquerytools_overlayhelpers = Resource(plone_example, 'plone.app.jquerytools.overlayhelpers.js', depends=[jquerytools])
form_tabbing = Resource(plone_example, 'form_tabbing.js', depends=[jquerytools])
popupforms = Resource(plone_example, 'popupforms.js', depends=[jquerytools])

plone = Group([
        plone_javascript_variables,
        cookie_functions,
        modernizr,
        sarissa,
        kukit,
        tiny_mce,
        tiny_mce_init,
        jquery,
        jquery_integration,
        jquery_highlightsearchterms,
        accessibility,
        calendar_formfield,
        collapsibleformfields,
        collapsiblesections,
        comments,
        dragdropreorder,
        dropdown,
        first_input_focus,
        formUnload,
        formsubmithelpers,
        livesearch,
        nodeutilities,
        register_function,
        search,
        select_all,
        styleswitcher,
        table_sorter,
        toc,
        unlockOnFormUnload,
        jquerytools,
        jquerytools_form,
        jquerytools_dateinput,
        jquerytools_overlayhelpers,
        form_tabbing,
        popupforms,
        ])

groups = [plone,] # import and extend in addons
