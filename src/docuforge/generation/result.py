# PURPOSE:
#     Describe generated output without writing it to the filesystem.
#     Allow Django, a CLI, or another caller to decide how the output is delivered.
#
#
# DEFINE GENERATED_FILE:
#     filename
#     content
#     media_type
#     encoding = UTF-8
#
#
# WHEN A GENERATED_FILE IS CREATED:
#     IF filename is not text OR filename is empty:
#         RAISE a result validation error
#
#     IF filename contains a directory path:
#         RAISE a result validation error
#
#     IF content is not text:
#         RAISE a result validation error
#
#     IF media_type is not non-empty text:
#         RAISE a result validation error
#
#
# DEFINE GENERATION_RESULT:
#     files
#     warnings
#
#
# WHEN A GENERATION_RESULT IS CREATED:
#     IF files is empty:
#         RAISE a result validation error
#
#     FOR EACH file in files:
#         IF file is not a GENERATED_FILE:
#             RAISE a result validation error
#
#     FOR EACH warning in warnings:
#         IF warning is not text:
#             RAISE a result validation error
#
#     COPY files and warnings so the result cannot be changed unexpectedly
#
#
# FUNCTION GET_PRIMARY_FILE:
#     RETURN the first generated file
