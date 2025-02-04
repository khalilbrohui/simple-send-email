# from rest_framework.views import APIView
# from django.conf import settings
# from django.core.exceptions import ValidationError
# from django.core.mail import send_mail
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny
# from smtplib import SMTPException

# from .serializers import EmailSerializer

# class SendEmailView(APIView):
#     serializer_class = EmailSerializer
#     permission_classes = [AllowAny]

#     def post(self, request):
#         try:
#             # Extract data
#             subject = request.data.get("subject")
#             message = request.data.get("message")
#             recipient_email = request.data.get("recipient_email")

#             # Validate required fields
#             if not all([subject, message, recipient_email]):
#                 return Response(
#                     {
#                         "error": "All fields (subject, message, recipient_email) are required."
#                     },
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#             # Send the email
#             send_mail(
#                 subject=subject,
#                 message=message,
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 recipient_list=[recipient_email],
#                 fail_silently=False,
#             )

#             return Response(
#                 {"message": "Email sent successfully!"}, status=status.HTTP_200_OK
#             )

#         except ValidationError as e:
#             return Response(
#                 {"error": "Invalid email address.", "details": str(e)},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         except SMTPException as e:
#             return Response(
#                 {
#                     "error": "Failed to send email due to an SMTP issue.",
#                     "details": str(e),
#                 },
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )
#         except Exception as e:
#             return Response(
#                 {"error": "An unexpected error occurred.", "details": str(e)},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )

import logging
from rest_framework.views import APIView
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from smtplib import SMTPException
from .serializers import EmailSerializer

# Set up logger
logger = logging.getLogger(__name__)


class SendEmailView(APIView):
    serializer_class = EmailSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            # Extract data
            subject = request.data.get("subject")
            message = request.data.get("message")
            recipient_email = request.data.get("recipient_email")

            # Validate required fields
            if not all([subject, message, recipient_email]):
                logger.error(
                    "Missing required fields: subject, message, or recipient_email"
                )
                return Response(
                    {
                        "error": "All fields (subject, message, recipient_email) are required."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Send the email
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient_email],
                fail_silently=False,
            )

            logger.info(f"Email sent successfully to {recipient_email}")
            return Response(
                {"message": "Email sent successfully!"}, status=status.HTTP_200_OK
            )

        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            return Response(
                {"error": "Invalid email address.", "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except SMTPException as e:
            logger.error(f"SMTP error: {e}")
            return Response(
                {
                    "error": "Failed to send email due to an SMTP issue.",
                    "details": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
            return Response(
                {"error": "An unexpected error occurred.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
