# PURPOSE:
#     Describe all values needed to generate a document.
#     Keep generation inputs independent from Django models and HTTP requests.
#
#
# DEFINE GENERATION_CONTEXT:
#     title
#     filename
#     variables
#     strict_mode
#
#
# WHEN A GENERATION_CONTEXT IS CREATED:
#     IF title is not text:
#         RAISE a context validation error
#
#     IF filename is not text OR filename is empty:
#         RAISE a context validation error
#
#     IF variables is not a collection of names and values:
#         RAISE a context validation error
#
#     FOR EACH variable name:
#         IF the name is not non-empty text:
#             RAISE a context validation error
#
#     COPY variables so changes made by the caller cannot alter this context
#
#
# FUNCTION GET_TEMPLATE_VARIABLES:
#     template_variables = COPY the stored variables
#     SET template_variables["title"] to title
#
#     RETURN template_variables
