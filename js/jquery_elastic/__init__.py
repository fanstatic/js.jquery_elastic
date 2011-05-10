from fanstatic import Library, Resource

library = Library('jquery_elastic', 'resources')

elastic = Resource(library,
                   'jquery.elastic.source.js',
                   minified='jquery.elastic.js')
