from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import analyze_area

@api_view(['POST'])
def analyze_query(request):
    query = request.data.get("query")
    
    if not query:
        return Response({"error": "Query is required"}, status=400)

    summary, chart_data, table_data = analyze_area(query)

    return Response({
        "summary": summary,
        "chart_data": chart_data,
        "table_data": table_data
    })
