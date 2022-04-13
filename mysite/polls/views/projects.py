import glob
import json

from rest_framework.response import Response
from rest_framework.views import APIView


class Projects(APIView):

    def get(self, request, *args, **kargs):
        files = glob.glob("/minecraft/computer/*[!lastid.txt]", recursive=True)
        files_json = json.dumps(files, ensure_ascii=False, indent=2)
        date = {
            'date': files
        }
        return Response(date)

