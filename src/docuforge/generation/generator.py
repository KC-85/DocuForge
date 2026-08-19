# PURPOSE:
#     Coordinate document generation.
#     This module does not know about Django, HTTP requests, or the filesystem.
#
# INPUTS:
#     template_source   The Markdown or RST template text.
#     requested_format  The output format selected by the caller.
#     context           The title, filename, and replacement variables.
#
# OUTPUT:
#     A generation result containing the generated file and any warnings.
#
#
# FUNCTION GENERATE_DOCUMENT(template_source, requested_format, context):
#     IF template_source is empty:
#         RAISE a template validation error
#
#     normalised_format = NORMALISE requested_format
#     format_generator = SELECT_FORMAT_GENERATOR(normalised_format)
#
#     VALIDATE template_source
#     required_variables = FIND_PLACEHOLDERS(template_source)
#     missing_variables = FIND_MISSING_VARIABLES(required_variables, context.variables)
#
#     IF missing_variables is not empty:
#         RAISE a template validation error listing the missing variables
#
#     generated_content = format_generator.GENERATE(template_source, context)
#     output_filename = BUILD_FILENAME(context.filename, format_generator.extension)
#
#     generated_file = CREATE_GENERATED_FILE(
#         filename = output_filename,
#         content = generated_content,
#         media_type = format_generator.media_type,
#     )
#
#     RETURN a generation result containing generated_file
#
#
# FUNCTION SELECT_FORMAT_GENERATOR(normalised_format):
#     IF normalised_format is Markdown:
#         RETURN the Markdown generator
#
#     IF normalised_format is reStructuredText:
#         RETURN the RST generator
#
#     RAISE an unsupported format error
#
#
# FUNCTION BUILD_FILENAME(requested_filename, extension):
#     REMOVE unsafe path characters from requested_filename
#     REMOVE any existing Markdown or RST extension
#
#     IF the remaining filename is empty:
#         USE a safe default filename
#
#     RETURN the safe filename with extension appended
