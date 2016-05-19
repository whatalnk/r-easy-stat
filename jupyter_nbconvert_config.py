c = get_config()

c.Exporter.preprocessors = ['nbconvert.preprocessors.ExtractOutputPreprocessor']
c.ExtractOutputPreprocessor.extract_output_types = {'image/svg+xml'}
c.NbConvertApp.export_format = 'html'
c.Exporter.template_file = 'separate_image_html'
c.FilesWriter.build_directory = 'gh-pages'