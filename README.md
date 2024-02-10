# OCA - Open Cel Animation importer for Krita

Imports Animation cells to Krita from [OCA](https://rxlaboratory.org/tools/oca), a *JSON* + *PNG*/*EXR* format.
This tools complements OCA-Krita exporter from Duduf http://oca-krita.rxlab.guide/
Currently, only 8 bits compositions are supported.
It's a workaround, because Krita animation api is not yet fully accessable from python.
It's very minimal for now (no layer blending modes, etc...), but functional for my need,
to integrate tahoma2d great traditional animation tool with krita fantastic brush painting tool.
