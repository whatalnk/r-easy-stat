c = get_config()

c.Exporter.preprocessors = ['nbconvert.preprocessors.ExtractOutputPreprocessor']
c.NbConvertApp.export_format = 'html'
c.Exporter.template_file = 'separate_image_html'
c.FilesWriter.build_directory = 'gh-pages'