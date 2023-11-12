from rest_framework import generics, permissions, status
from rest_framework.response import Response

from bot.models import TgUser
from bot.serializers import TgUserSerializer
from bot.tg.client import TgClient
from config.settings import dev


class VerificationView(generics.GenericAPIView):
    model = TgUser
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TgUserSerializer

    def patch(self, request, *args, **kwargs):
        s: TgUserSerializer = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)

        tg_user: TgUser = s.validated_data['tg_user']
        tg_user.user = self.request.user
        tg_user.save(update_fields=('user',))

        instance_s: TgUserSerializer = self.get_serializer(tg_user)
        TgClient(dev.BOT_TOKEN).send_message(tg_user.chat_id, '[verification_code_has_been_completed]')
        return Response(instance_s.data, status=status.HTTP_201_CREATED)
