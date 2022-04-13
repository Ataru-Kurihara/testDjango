import json
import os

from rest_framework.views import APIView
from rest_framework.response import Response
import glob


class Project(APIView):

    def get(self, request, *args, **kwargs):
        project_id = kwargs['id']
        files = glob.glob(f"/minecraft/computer/{project_id}", recursive=True)
        try:
            for filename in os.listdir(files[0]):
                with open(os.path.join(files[0], filename), "r") as f:
                    file = f.read()
                    print(file)
            date = {
                'response': {
                    'id': project_id,
                    'path': files,
                    'date': file
                }
            }
            return Response(date)
        except IndexError:
            return Response("このファイルはないよ！")
