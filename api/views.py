import pandas as pd
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Challenge
from .serializers import ChallengeSerializer

@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_csv(request):
    file = request.FILES.get('file')

    if not file:
        return Response({"error": "No file provided"}, status=400)

    try:
        df = pd.read_csv(file)
        challenges = [
            Challenge(challengeId=row['ChallengeID'], challengeName=row['ChallengeName'], challengeDifficulty=['ChallengeDifficulty'])
            for _, row in df.iterrows()
        ]
        Challenge.objects.bulk_create(challenges)
        return Response({"message": "File uploaded successfully!"})
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(['GET'])
def get_challenges(request):
    challenges = Challenge.objects.all()
    serializer = ChallengeSerializer(challenges, many=True)
    return JsonResponse(serializer.data, safe=False)
