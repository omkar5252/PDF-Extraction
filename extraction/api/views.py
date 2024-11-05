import os
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PDFUploadSerializer
from extraction.utils import extract_insights_from_pdf
from drf_spectacular.utils import extend_schema
import tempfile

class PDFExtractView(APIView):
    @extend_schema(
        request=PDFUploadSerializer, 
        responses={200: dict}
    )
    def post(self, request, *args, **kwargs):
        serializer = PDFUploadSerializer(data=request.data)
        if serializer.is_valid():
            pdf_file = serializer.validated_data['pdf_file']
            
            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(pdf_file.read())
                temp_file_path = temp_file.name
            
            # Extract insights (assuming extract_insights_from_pdf is defined)
            insights = extract_insights_from_pdf(temp_file_path)
            
            # Clean up the temp file
            os.remove(temp_file_path)

            return Response(insights, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
