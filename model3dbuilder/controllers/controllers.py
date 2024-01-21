from django.http import JsonResponse

class RestController:
    def get_ortese(self, ortese_id):
        # Lógica para recuperar e retornar a ortese
        return JsonResponse({"message": "Detalhes de Ortese recuperados com sucesso!"})

